#!/usr/bin/env python3
"""Supervise a continuous headless Claude run until the extraction is actually done.

    python autorun.py                 # start or resume
    python autorun.py --fresh         # forget the saved session and start over

Completion is read out of prophecy.db, not out of a checklist, so it cannot be declared
early: the run ends when no past-due claim is missing evidence, no strong fulfilment assertion
is unlinked, and tier 2 is fully read. The supervisor restarts the same Claude session after a
crash and otherwise stays out of the way.

Stops on: all three counters at zero, a STOP file in this directory, an unrecoverable
auth/billing failure, or six cycles in a row that change nothing. Nothing else.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

HERE = Path(__file__).resolve().parent
GOAL_FILE = HERE / "EXTRACT-GOAL.md"
STATE = HERE / ".autorun" / "session.json"
LOGS = HERE / ".autorun"

STALL_LIMIT = 6      # cycles that change nothing before the run is called broken

FATAL = ("authentication failed", "authentication_error", "billing error", "billing_error",
         "credit balance", "insufficient credits", "invalid api key", "not logged in",
         "model not found", "model_not_found", "organization has been disabled")

RESUME = ("Continue the goal. Re-read EXTRACT-GOAL.md and PROGRESS.md, run "
          "`python prophecy.py todo` to see where you are, and carry on from durable state. "
          "Do not narrow the scope and do not ask questions.")


def remaining() -> tuple[int, str]:
    """Work left, straight from the database, plus a line to print.

    Three counters, and the run ends only when all three are zero: unchecked past-due claims,
    unlinked fulfilment assertions, and unread tier-2 passages. Reading it out of the database
    rather than off a checklist is what stops the worker declaring itself finished early."""
    out = subprocess.run([sys.executable, "prophecy.py", "todo", "--limit", "0"],
                         cwd=HERE, capture_output=True, text=True,
                         encoding="utf-8", errors="replace").stdout
    num = lambda pat: (int(m.group(1).replace(",", ""))
                       if (m := re.search(pat, out)) else -1)
    due = num(r"past-due claims with no evidence recorded\s*:\s*(\d[\d,]*)")
    unlinked = num(r"strong fulfilment assertions not yet linked\s*:\s*(\d[\d,]*)")
    t2 = re.search(r"tier 2\s+\S.*?(\d[\d,]*)\s+of\s+([\d,]+)\s+read", out)
    t2left = (int(t2.group(2).replace(",", "")) - int(t2.group(1).replace(",", ""))
              if t2 else -1)
    t1 = re.search(r"tier 1\s+\S.*?(\d[\d,]*)\s+of\s+([\d,]+)\s+read", out)
    t1left = (int(t1.group(2).replace(",", "")) - int(t1.group(1).replace(",", ""))
              if t1 else -1)
    fq = re.search(r"focus\s+tier 3.*?(\d[\d,]*)\s+of\s+([\d,]+)\s+read", out)
    fqleft = (int(fq.group(2).replace(",", "")) - int(fq.group(1).replace(",", ""))
              if fq else -1)
    if min(due, unlinked, t2left, t1left, fqleft) < 0:   # todo changed shape: never call that done
        return (-1, "could not read progress out of the database")
    return (due + unlinked + t2left + t1left + fqleft,
            f"{due} unchecked past-due, {unlinked} unlinked fulfilments, {t1left} tier-1 unread, "
            f"{t2left} tier-2 unread, {fqleft} econ/politics/health tier-3 unread")


def rate_limited_until(tail: str):
    """Epoch seconds to wait until, if the cycle ended on a usage limit. None otherwise."""
    if not re.search(r"session limit|usage limit|rate.?limit", tail):
        return None
    resets = [int(m) for m in re.findall(r'"resetsat"\s*:\s*(\d{10})', tail)]
    if not resets:
        return time.time() + 900          # unknown reset: a quarter hour is enough to stop spinning
    future = [r for r in resets if r > time.time()]
    # a limit with only stale reset stamps still means wait; returning None here would
    # reinstate the 3-second spin this function exists to prevent
    return min(future) if future else time.time() + 900


def session_from(line: str):
    try:
        ev = json.loads(line)
    except ValueError:
        return None
    sid = ev.get("session_id") if isinstance(ev, dict) else None
    return sid if isinstance(sid, str) and sid else None


def run_once(session_id, model, permission_mode, log_file):
    # The goal condition is capped at 4000 characters, so the goal points at the rules file
    # instead of carrying it. Pasting the file inline fails silently: the cycle returns
    # success, does nothing, and the supervisor spins.
    prompt = RESUME if session_id else (
        "/goal Read EXTRACT-GOAL.md in this directory and work through it, top to bottom, "
        "without stopping. Done when `python prophecy.py todo` shows no past-due claim "
        "without evidence, no unlinked strong fulfilment assertion, tiers 1 and 2 at 100 "
        "percent, and the econ/politics/health focus line at 100 percent. "
        "Nobody needs to approve a batch. Do not ask questions. If a batch fails, fix it and "
        "carry on.")
    cmd = ["claude", "-p", prompt, "--model", model,
           "--permission-mode", permission_mode,
           "--output-format", "stream-json", "--verbose"]
    if session_id:
        cmd += ["--resume", session_id]
    tail, found = "", session_id
    with log_file.open("w", encoding="utf-8") as log:
        proc = subprocess.Popen(cmd, cwd=HERE, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True,
                                encoding="utf-8", errors="replace", bufsize=1)
        try:
            for line in proc.stdout:
                log.write(line)
                log.flush()
                tail = (tail + line.lower())[-60_000:]
                sid = session_from(line)
                if sid and sid != found:
                    found = sid
                    STATE.write_text(json.dumps({"session_id": sid}), encoding="utf-8")
            return proc.wait(), tail, found
        except KeyboardInterrupt:
            proc.terminate()
            raise


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="opus")
    ap.add_argument("--permission-mode", default="bypassPermissions",
                    help="headless runs cannot answer prompts; this keeps the worker moving")
    ap.add_argument("--fresh", action="store_true")
    args = ap.parse_args()

    LOGS.mkdir(exist_ok=True)
    if args.fresh:
        STATE.unlink(missing_ok=True)
    if shutil.which("claude") is None:
        print("claude not on PATH", file=sys.stderr)
        return 2
    if not GOAL_FILE.is_file():
        print(f"missing {GOAL_FILE.name}", file=sys.stderr)
        return 2

    session_id = None
    if STATE.is_file():
        try:
            session_id = json.loads(STATE.read_text(encoding="utf-8")).get("session_id")
        except (OSError, ValueError):
            session_id = None

    attempt = stalls = 0
    while True:
        if (HERE / "STOP").exists():
            print("STOP file present; leaving the session resumable")
            return 0
        left, line = remaining()
        if left == 0:
            STATE.unlink(missing_ok=True)
            print(f"Done: nothing left ({line})")
            return 0

        attempt += 1
        stamp = time.strftime("%Y%m%d-%H%M%S")
        log_file = LOGS / f"{stamp}-{attempt:04d}.jsonl"
        print(f"[{stamp}] {line}; "
              f"{'resuming ' + session_id if session_id else 'starting new goal'}; "
              f"log {log_file.name}", flush=True)

        try:
            code, tail, found = run_once(session_id, args.model, args.permission_mode, log_file)
        except KeyboardInterrupt:
            print("\ninterrupted; rerun to resume", file=sys.stderr)
            return 130
        if found:
            session_id = found

        if any(f in tail for f in FATAL):
            print(f"unrecoverable access failure, see {log_file}", file=sys.stderr)
            return code or 1

        after, after_line = remaining()
        print(f"  cycle {attempt} ended (exit {code}); {left} -> {after} items left "
              f"({after_line})", flush=True)

        # A usage limit is not a failure to retry against: hammering it every 3 seconds
        # burns cycles and does no work. Wait for the reset the CLI reports, then resume.
        resume_at = rate_limited_until(tail)
        if resume_at:
            wait = max(60, int(resume_at - time.time()) + 30)
            until = time.strftime("%H:%M:%S", time.localtime(resume_at))
            print(f"  usage limit reached; sleeping {wait // 60} min until {until}", flush=True)
            slept = 0
            while slept < wait:
                if (HERE / "STOP").exists():
                    print("STOP file present during backoff; exiting")
                    return 0
                time.sleep(min(30, wait - slept))
                slept += 30
            continue
        if after >= left and code == 0:
            # the worker returned without moving the number: give it a fresh nudge rather
            # than spinning on the same resumed context
            stalls += 1
            print(f"  no progress this cycle ({stalls} in a row); "
                  f"nudging with a fresh goal prompt", flush=True)
            session_id = None
        else:
            stalls = 0
        # A cycle that returns success in seconds and changes nothing is a broken prompt, not
        # a slow worker, and retrying it every three seconds burns quota for nothing. Back off,
        # then give up with the worker's own last words rather than spinning all night.
        if stalls >= STALL_LIMIT:
            print(f"\n{stalls} cycles in a row did nothing. The worker's last output:\n"
                  f"  {tail[-600:].strip()}\n"
                  f"Full log: {log_file}", file=sys.stderr)
            return 3
        time.sleep(min(600, 3 * 2 ** stalls) if stalls else 3)


if __name__ == "__main__":
    sys.exit(main())

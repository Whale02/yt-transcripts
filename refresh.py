#!/usr/bin/env python3
"""Pull anything the channel has published since the last run, and put it in the database.

    python refresh.py              # fetch, ingest, date, type, report
    python refresh.py --dry-run    # say what is new without changing anything

Both tabs are fetched, videos and streams, because he uses each for different material and
the archive files make the fetch resumable. Transcripts are always fetched WITH timestamps:
without them the segmenter produces nothing and the video lands in the database with zero
passages, which looks like success and is not. This script exists so that cannot happen by
hand again.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sqlite3
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

HERE = Path(__file__).resolve().parent
DB = HERE / "prophecy.db"
CHANNEL = "https://www.youtube.com/@lastdays247"
TABS = [("videos", "corpus"), ("streams", "corpus-streams")]


def run(args, **kw):
    return subprocess.run([sys.executable, *args], cwd=HERE, text=True,
                          encoding="utf-8", errors="replace", **kw)


def known() -> set[str]:
    if not DB.is_file():
        return set()
    con = sqlite3.connect(DB)
    return {r[0] for r in con.execute("SELECT video_id FROM video")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    before = known()
    print(f"{len(before)} videos already in the database")

    for tab, out in TABS:
        if args.dry_run:
            print(f"  would fetch {CHANNEL}/{tab} -> {out}/")
            continue
        print(f"  fetching {tab} ...", flush=True)
        # --timestamps is not optional: see the module docstring
        r = run(["yt_transcripts.py", f"{CHANNEL}/{tab}", "-o", out, "--timestamps"],
                capture_output=True)
        tail = (r.stdout or "").strip().splitlines()[-3:]
        for line in tail:
            print(f"    {line}")
        # a missing yt-dlp exits nonzero with empty stdout, which used to read as "nothing new"
        if r.returncode != 0 and not tail:
            print(f"    fetch failed (exit {r.returncode}): {(r.stderr or '').strip()[-300:]}")
            return 1

    if args.dry_run:
        return 0

    for step in (["prophecy.py", "ingest", "corpus/"],
                 ["prophecy.py", "ingest", "corpus-streams/"],
                 ["prophecy.py", "dates"],
                 ["prophecy.py", "type"]):
        r = run(step, capture_output=True)
        last = (r.stdout or "").strip().splitlines()
        print(f"  {' '.join(step[1:]):<26} {last[-1] if last else '(no output)'}")

    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    new = [r for r in con.execute("SELECT video_id,uploaded_on,title FROM video ORDER BY uploaded_on")
           if r["video_id"] not in before]
    if not new:
        print("\nnothing new on the channel")
    else:
        print(f"\n{len(new)} new video{'s' if len(new) != 1 else ''}:")
        for r in new:
            n = con.execute("SELECT COUNT(*) FROM segment WHERE video_id=?",
                            (r["video_id"],)).fetchone()[0]
            flag = "" if n else "   <-- NO SEGMENTS: transcript has no timestamps, refetch it"
            print(f"  {r['uploaded_on']}  {r['video_id']}  {n:>4} passages  "
                  f"{r['title'][:52]}{flag}")

    out = run(["prophecy.py", "todo", "--limit", "0"], capture_output=True).stdout
    print("\n" + "\n".join(l for l in out.splitlines()
                           if re.search(r"tier \d|not yet linked|no evidence", l)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

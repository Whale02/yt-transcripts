#!/usr/bin/env python3
"""Rekey a review file onto the mention ids produced by one extract run, and mark collisions.

Two workers have been running against this database at once, so the same passage sometimes gets
extracted twice within minutes. `review` refuses a row keyed by video_id and start_s when two
mentions share them, which is correct, and this turns that refusal into a decision: if the other
worker's row already carries a live assignment, mine is marked duplicate_of theirs; otherwise mine
is adjudicated normally from the review file.

    python t2review.py reviews-t2w-11.json            # uses the newest extract run
    python t2review.py reviews-t2w-11.json 779        # or a run_id you name
"""
import json
import sqlite3
import subprocess
import sys
from pathlib import Path

con = sqlite3.connect("prophecy.db")
con.row_factory = sqlite3.Row

src = Path(sys.argv[1])
run_id = int(sys.argv[2]) if len(sys.argv) > 2 else con.execute(
    "SELECT MAX(run_id) FROM run WHERE kind='extract'").fetchone()[0]

wanted = json.loads(src.read_text(encoding="utf-8"))
wanted = wanted["reviews"] if isinstance(wanted, dict) else wanted
by_key = {(r["video_id"], int(r["start_s"])): r for r in wanted}

out, dupes = [], 0
for m in con.execute("SELECT mention_id, video_id, start_s FROM mention WHERE run_id=?",
                     (run_id,)).fetchall():
    r = by_key.get((m["video_id"], m["start_s"]))
    if not r:
        continue
    sib = con.execute(
        """SELECT m2.mention_id FROM mention m2
           WHERE m2.video_id=? AND m2.start_s=? AND m2.mention_id!=?
             AND EXISTS (SELECT 1 FROM assignment a
                         WHERE a.mention_id=m2.mention_id AND a.superseded_by IS NULL)""",
        (m["video_id"], m["start_s"], m["mention_id"])).fetchone()
    if sib:
        out.append({"mention_id": m["mention_id"], "duplicate_of": sib["mention_id"],
                    "note": "same passage extracted twice on 30 August 2026 by two workers on one "
                            "database; this is the later row and carries no claim"})
        dupes += 1
    else:
        out.append({"mention_id": m["mention_id"], "claim_id": r.get("claim_id"),
                    "same_event": r.get("same_event", "yes"), "delta_type": r["delta_type"],
                    "confidence": r.get("confidence", 0.8), "note": r.get("note")})

dst = src.with_name(src.stem + "-keyed.json")
dst.write_text(json.dumps({"reviews": out}, indent=0), encoding="utf-8")
print(f"run {run_id}: {len(out)} rows written to {dst.name}, {dupes} marked duplicate")
subprocess.run([sys.executable, "prophecy.py", "review", str(dst), "--tool", "claude-opus-5"])

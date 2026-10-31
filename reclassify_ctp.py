#!/usr/bin/env python3
"""Re-apply the corrected fulfilment-cue strength rule to rows already in the database.

`cmd_scan` decided strength from the cue string alone, which made every "come to pass" a
strong fulfilment assertion. Three different things say those words: "it came to pass"
asserts a word landed, "it shall come to pass in the last days" is Acts 2:17 or a promise,
and "it never came to pass" concedes a miss. Only the first belongs in the strong queue.

Re-running `scan` would fix new rows but would also delete and reinsert, which would
duplicate the assertions autolink has already attached. So this pass updates in place,
stamped with its own run_id, and never touches a row a reader has reviewed.
"""
import sqlite3
import sys

from prophecy import cue_strength, new_run, now

DB = sys.argv[1] if len(sys.argv) > 1 else "prophecy.db"
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row

run_id = new_run(con, "scan", "rules-v2", note="cue strength re-read with tense and negation")
rows = con.execute("""SELECT f.fa_id, f.cue, f.strength, COALESCE(f.quote, s.text) AS window
                      FROM fulfilment_assertion f
                      LEFT JOIN segment s ON s.segment_id = f.segment_id
                      WHERE f.reviewed = 0""").fetchall()

down = up = 0
for r in rows:
    want = cue_strength(r["cue"] or "", r["window"] or "")
    if want == r["strength"]:
        continue
    con.execute("UPDATE fulfilment_assertion SET strength=?, run_id=? WHERE fa_id=?",
                (want, run_id, r["fa_id"]))
    if want == "weak":
        down += 1
    else:
        up += 1
con.commit()

strong = con.execute("SELECT COUNT(*) FROM fulfilment_assertion WHERE strength='strong'").fetchone()[0]
unlinked = con.execute("SELECT COUNT(*) FROM fulfilment_assertion "
                       "WHERE strength='strong' AND claim_id IS NULL").fetchone()[0]
print(f"run {run_id}: {len(rows)} unreviewed rows re-read, "
      f"{down} downgraded to weak, {up} upgraded to strong")
print(f"  {strong} strong assertions remain, {unlinked} of them still unlinked")

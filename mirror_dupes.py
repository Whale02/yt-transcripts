#!/usr/bin/env python3
"""Copy a segment's adjudication onto duplicate extractions of the same segment.

Two extractors working the same corpus produce two mention rows for one passage. The review
command resolves a (video_id, start_s) to the newest mention only, so the older duplicate keeps
whatever the lexical clustering guessed and shows up forever as unreviewed. This mirrors the
human-or-model judgment from the reviewed sibling onto the duplicate rather than inventing a
second opinion, and supersedes the lexical row so the earlier guess stays auditable.
"""
import sqlite3, sys
from datetime import datetime, timezone

con = sqlite3.connect("prophecy.db")
con.row_factory = sqlite3.Row
now = datetime.now(timezone.utc).isoformat(timespec="seconds")
cur = con.execute("INSERT INTO run (kind,tool,prompt_version,note,started_at) VALUES (?,?,?,?,?)",
                  ("cluster", "claude-opus-5", "v1",
                   "mirror adjudication onto duplicate mentions of the same segment", now))
run_id = cur.lastrowid

stale = con.execute("""
    SELECT a.assignment_id, m.mention_id, m.video_id, m.start_s
    FROM assignment a JOIN mention m ON m.mention_id = a.mention_id
    WHERE a.superseded_by IS NULL AND a.delta_type = 'unreviewed'""").fetchall()

moved = skipped = 0
for s in stale:
    src = con.execute("""
        SELECT a.claim_id, a.same_event, a.confidence, a.delta_type, a.delta_note
        FROM assignment a JOIN mention m ON m.mention_id = a.mention_id
        WHERE m.video_id=? AND m.start_s=? AND m.mention_id!=?
          AND a.superseded_by IS NULL AND a.delta_type != 'unreviewed'
        ORDER BY a.assignment_id DESC LIMIT 1""",
        (s["video_id"], s["start_s"], s["mention_id"])).fetchone()
    if not src:
        skipped += 1
        continue
    note = (src["delta_note"] or "")
    note = (note + " | " if note else "") + \
           "mirrored from the reviewed extraction of the same segment; duplicate arose from two extractors"
    new = con.execute("""INSERT INTO assignment (mention_id,claim_id,run_id,same_event,confidence,
                         delta_type,delta_note,method,created_at) VALUES (?,?,?,?,?,?,?,?,?)""",
                      (s["mention_id"], src["claim_id"], run_id, src["same_event"],
                       src["confidence"], src["delta_type"], note, "claude-opus-5", now))
    con.execute("UPDATE assignment SET superseded_by=? WHERE assignment_id=?",
                (new.lastrowid, s["assignment_id"]))
    moved += 1
con.commit()
print(f"run {run_id}: {moved} duplicate assignments mirrored, {skipped} left "
      f"(no reviewed sibling to copy from)")

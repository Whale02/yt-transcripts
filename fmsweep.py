"""Rebuild the first_mention markers so each claim marks its chronologically earliest live telling.

The markers drifted because the corpus was extracted out of upload order by two workers: a thread
first met in July gets the marker, and the January origin found later comes in as new_detail.
first_mention is definitional rather than a judgement, so this is mechanical. Prior notes are
carried forward with a line saying what moved, and the review pass supersedes rather than rewrites.
"""
import json
import sqlite3

con = sqlite3.connect("prophecy.db")
con.row_factory = sqlite3.Row
rows = con.execute(
    """SELECT a.claim_id, a.mention_id, a.delta_type, a.confidence, a.delta_note,
              v.uploaded_on AS d, m.video_id, m.start_s
       FROM assignment a
       JOIN mention m ON m.mention_id = a.mention_id
       JOIN video v ON v.video_id = m.video_id
       WHERE a.superseded_by IS NULL AND a.claim_id IS NOT NULL"""
).fetchall()

by_claim = {}
for r in rows:
    by_claim.setdefault(r["claim_id"], []).append(r)

out = []
promoted = demoted = 0
for cid, rs in by_claim.items():
    rs.sort(key=lambda r: (r["d"], r["start_s"]))
    earliest = rs[0]
    marked = [r for r in rs if r["delta_type"] == "first_mention"]
    if len(marked) == 1 and marked[0]["mention_id"] == earliest["mention_id"]:
        continue
    for r in marked:
        if r["mention_id"] == earliest["mention_id"]:
            continue
        note = (r["delta_note"] or "").strip()
        note = (note + " | " if note else "") + (
            "repointed from first_mention: the %s telling comes first" % earliest["d"]
        )
        out.append(
            {
                "video_id": r["video_id"],
                "start_s": r["start_s"],
                "mention_id": r["mention_id"],
                "claim_id": cid,
                "same_event": "yes",
                "delta_type": "new_detail",
                "confidence": r["confidence"] if r["confidence"] is not None else 0.8,
                "note": note[:500],
            }
        )
        demoted += 1
    if earliest["delta_type"] != "first_mention":
        note = (earliest["delta_note"] or "").strip()
        note = (note + " | " if note else "") + (
            "marked first_mention: earliest live telling of this claim in the corpus"
        )
        out.append(
            {
                "video_id": earliest["video_id"],
                "start_s": earliest["start_s"],
                "mention_id": earliest["mention_id"],
                "claim_id": cid,
                "same_event": "yes",
                "delta_type": "first_mention",
                "confidence": earliest["confidence"] if earliest["confidence"] is not None else 0.8,
                "note": note[:500],
            }
        )
        promoted += 1

with open("reviews-c2o-fmsweep.json", "w", encoding="utf-8") as fh:
    json.dump({"reviews": out}, fh, indent=1, ensure_ascii=False)
print("rows", len(out), "promoted", promoted, "demoted", demoted, "claims touched",
      len({r["claim_id"] for r in out}))

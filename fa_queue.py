#!/usr/bin/env python3
"""Dump the unlinked strong fulfilment assertions with candidate claims beside each one.

autolink attaches only the unambiguous ones. What is left is the work: a tie between two
claims means the passage is generic, and a passage with no alias hit at all means the claim
it points back at is named in words no alias covers. Both need a reader, so this prints what
a reader needs: the passage around the cue, and the claims whose aliases it touches.
"""
import re
import sqlite3
import sys
from collections import defaultdict

DB = "prophecy.db"
OFFSET = int(sys.argv[1]) if len(sys.argv) > 1 else 0
LIMIT = int(sys.argv[2]) if len(sys.argv) > 2 else 60

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row

aliases = defaultdict(list)
for r in con.execute("SELECT claim_id, alias FROM claim_alias"):
    if len(r["alias"]) >= 5:
        aliases[r["claim_id"]].append(r["alias"].lower())
labels = {r["claim_id"]: r["label"]
          for r in con.execute("SELECT claim_id, label FROM canonical_claim WHERE merged_into IS NULL")}

rows = con.execute("""SELECT f.fa_id, f.video_id, f.start_s, f.uttered_at, f.cue, f.quote,
                             COALESCE(s.text, f.quote) AS full
                      FROM fulfilment_assertion f
                      LEFT JOIN segment s ON s.segment_id = f.segment_id
                      WHERE f.strength='strong' AND f.claim_id IS NULL
                      ORDER BY f.uttered_at DESC, f.fa_id
                      LIMIT ? OFFSET ?""", (LIMIT, OFFSET)).fetchall()

for r in rows:
    text = r["full"] or ""
    low = " " + re.sub(r"[^a-z0-9 ]", " ", text.lower()) + " "
    low = re.sub(r"\s+", " ", low)
    hits = []
    for cid, als in aliases.items():
        score = sum(2 for a in als if f" {a} " in low)
        lab = labels.get(cid, "").lower()
        if len(lab) > 8 and f" {lab} " in low:
            score += 3
        if score:
            hits.append((score, cid))
    hits.sort(reverse=True)
    idx = text.lower().find((r["cue"] or "").lower())
    if idx < 0:
        idx = 0
    window = " ".join(text[max(0, idx - 260): idx + 260].split())
    print(f"\n@@ {r['fa_id']}  {r['video_id']}@{r['start_s']}  {r['uttered_at']}  cue=\"{r['cue']}\"")
    print(f"   {window}")
    for score, cid in hits[:5]:
        print(f"   [{score}] {cid} :: {labels.get(cid, '')}")
    if not hits:
        print("   [no alias hit]")

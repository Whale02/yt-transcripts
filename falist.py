import sqlite3, re, sys
from collections import defaultdict, Counter
con = sqlite3.connect('prophecy.db'); con.row_factory = sqlite3.Row
off = int(sys.argv[1]) if len(sys.argv) > 1 else 0
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 30
aliases = defaultdict(list)
for r in con.execute("SELECT claim_id, alias FROM claim_alias"):
    if len(r["alias"]) >= 5: aliases[r["claim_id"]].append(r["alias"].lower())
labels = {r["claim_id"]: r["label"] for r in
          con.execute("SELECT claim_id,label FROM canonical_claim WHERE merged_into IS NULL")}
rows = con.execute("""SELECT f.fa_id,f.video_id,f.start_s,f.uttered_at,f.cue,f.quote,s.text
     FROM fulfilment_assertion f LEFT JOIN segment s ON s.segment_id=f.segment_id
     WHERE f.strength='strong' AND f.claim_id IS NULL
     ORDER BY f.uttered_at, f.fa_id LIMIT ? OFFSET ?""", (lim, off)).fetchall()
for r in rows:
    txt = r['text'] or r['quote'] or ''
    low = " " + re.sub(r"\s+"," ", re.sub(r"[^a-z0-9 ]"," ", txt.lower())) + " "
    hits = []
    for cid, als in aliases.items():
        sc = sum(2 for a in als if f" {a} " in low)
        lb = labels.get(cid,"").lower()
        if len(lb) > 8 and f" {lb} " in low: sc += 3
        if sc: hits.append((sc,cid))
    hits.sort(reverse=True)
    print(f"### fa{r['fa_id']} | {r['uttered_at']} | {r['video_id']}@{r['start_s']} | cue={r['cue']}")
    print("CTX:", " ".join(txt.split())[:900])
    if hits: print("CAND:", ", ".join(f"{c}({s})" for s,c in hits[:6]))
    print()

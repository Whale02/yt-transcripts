import sqlite3, json, sys
con = sqlite3.connect('prophecy.db'); con.row_factory = sqlite3.Row
have = {r[0]: r[1] for r in con.execute("SELECT claim_id, merged_into FROM canonical_claim")}
bad = 0
for f in sys.argv[1:]:
    d = json.loads(open(f, encoding='utf-8').read())
    rows = d.get("links") or d.get("evidence") or d.get("reviews") or d.get("mentions") or d
    if rows and isinstance(rows[0], str): continue
    for it in rows:
        cid = it.get("claim_id")
        if cid is None: continue
        if cid not in have:
            print(f"  MISSING {f}: {cid}"); bad += 1
        elif have[cid]:
            print(f"  MERGED  {f}: {cid} -> {have[cid]}"); bad += 1
print("OK" if not bad else f"{bad} bad claim_id(s)")
sys.exit(1 if bad else 0)

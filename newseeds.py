#!/usr/bin/env python3
"""Merge only genuinely new canonical claims from a candidate file into seeds.json, then
seed just those. Two extractors share this database; replacing a claim another worker
already wrote would silently rewrite its label and aliases, so anything that already
exists in seeds.json or in canonical_claim is left exactly as it is."""
import json, pathlib, sqlite3, subprocess, sys

cand = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "seeds-new.json")
master = pathlib.Path("seeds.json")
have = {c["claim_id"]: c for c in json.loads(master.read_text(encoding="utf-8"))}
with sqlite3.connect("prophecy.db") as con:
    have_db = {r[0] for r in con.execute("SELECT claim_id FROM canonical_claim")}

new = [c for c in json.loads(cand.read_text(encoding="utf-8"))
       if c["claim_id"] not in have and c["claim_id"] not in have_db]
skipped = [c["claim_id"] for c in json.loads(cand.read_text(encoding="utf-8"))
           if c["claim_id"] in have or c["claim_id"] in have_db]
if not new:
    print(f"no new claims ({len(skipped)} already present)")
    sys.exit(0)
for c in new:
    have[c["claim_id"]] = c
master.write_text(json.dumps(sorted(have.values(), key=lambda x: x["claim_id"]),
                             indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
only = pathlib.Path(".seed-only.json")
only.write_text(json.dumps(new, indent=2, ensure_ascii=False), encoding="utf-8")
subprocess.run([sys.executable, "prophecy.py", "seed", str(only)], check=True)
print(f"{len(new)} new: {', '.join(c['claim_id'] for c in new)}")
if skipped:
    print(f"{len(skipped)} left untouched: {', '.join(skipped)}")

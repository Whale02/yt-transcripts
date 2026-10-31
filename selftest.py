#!/usr/bin/env python3
"""Checks that can fail. Run after any change to prophecy.py.

  python selftest.py            # exits non-zero on the first failure

Three families:
  * dead flags   - every registered CLI argument must actually be read by its handler
  * partitions   - the tier filter must filter, and the tiers must cover the set exactly
  * integrity    - the database invariants the schema cannot enforce on its own
"""

from __future__ import annotations

import ast
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

SRC = Path("prophecy.py")
DB = "prophecy.db"
fails: list[str] = []


def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
    if not ok:
        fails.append(name)


# ------------------------------------------------------------- dead flags
def dead_flags():
    """A flag registered on a subparser but never read by the command is a lie in --help."""
    src = SRC.read_text(encoding="utf-8")
    tree = ast.parse(src)
    bodies = {n.name: ast.dump(n) for n in ast.walk(tree)
              if isinstance(n, ast.FunctionDef) and n.name.startswith("cmd_")}
    # sub.add_parser("x") ... p.add_argument("--y")  on the same source line
    for line in src.splitlines():
        m = re.search(r'sub\.add_parser\("([a-z_-]+)"\)', line)
        if not m:
            continue
        cmd = m.group(1)
        fn = "cmd_" + cmd.replace("-", "_")
        if fn not in bodies:
            continue
        for arg in re.findall(r'add_argument\("--([a-z-]+)"', line):
            attr = arg.replace("-", "_")
            used = f"attr='{attr}'" in bodies[fn]
            check(f"flag --{arg} is read by {fn}", used,
                  "" if used else "registered but never read")


# ------------------------------------------------------------- partitions
def tier_partition():
    def count(extra):
        out = subprocess.run([sys.executable, "prophecy.py", "pick", "--since", "2026-06-01",
                              "--limit", "0"] + extra, capture_output=True, text=True).stdout
        m = re.search(r"^(\d+) unextracted", out, re.M)
        return int(m.group(1)) if m else -1

    total = count([])
    tiers = {t: count(["--tier", str(t)]) for t in (1, 2, 3)}
    # A tier may legitimately hold the whole remaining queue once the other tiers are fully
    # read, which is where tiers 1 and 2 landed. The failure this guards against is a --tier
    # flag that gets ignored, and that shows up as every tier returning the total; the
    # partition check below catches it, because the sum would then be three times the total.
    check("tier filter actually filters", all(0 <= n <= total for n in tiers.values()),
          f"total={total} tiers={tiers}")
    check("tiers 1-3 partition the queue", sum(tiers.values()) == total,
          f"sum={sum(tiers.values())} total={total}")
    check("tier 4 never survives the cue filter", count(["--tier", "4"]) == 0)


# ------------------------------------------------------------- integrity
def integrity():
    con = sqlite3.connect(DB)
    q = lambda s: con.execute(s).fetchone()[0]
    for name, sql in {
        "no mention carries two live assignments":
            "SELECT COUNT(*) FROM (SELECT mention_id FROM assignment WHERE superseded_by IS NULL"
            " GROUP BY mention_id HAVING COUNT(*)>1)",
        "no duplicate mentions":
            "SELECT COUNT(*) FROM (SELECT video_id,start_s,claim_text FROM mention"
            " GROUP BY video_id,start_s,claim_text HAVING COUNT(*)>1)",
        "search indexes match their tables":
            "SELECT abs((SELECT COUNT(*) FROM mention_fts)-(SELECT COUNT(*) FROM mention))"
            " + abs((SELECT COUNT(*) FROM segment_fts)-(SELECT COUNT(*) FROM segment))",
        "no canonical claim is orphaned":
            "SELECT COUNT(*) FROM canonical_claim c WHERE c.merged_into IS NULL"
            " AND NOT EXISTS (SELECT 1 FROM assignment a"
            " WHERE a.claim_id=c.claim_id AND a.superseded_by IS NULL)",
        "no live assignment points at a folded claim":
            "SELECT COUNT(*) FROM assignment a JOIN canonical_claim c ON c.claim_id=a.claim_id"
            " WHERE a.superseded_by IS NULL AND c.merged_into IS NOT NULL",
        "a fold never points at another fold":
            "SELECT COUNT(*) FROM canonical_claim c JOIN canonical_claim t"
            " ON t.claim_id=c.merged_into WHERE t.merged_into IS NOT NULL",
        "reality follows the fold":
            "SELECT (SELECT COUNT(*) FROM validation_evidence e JOIN canonical_claim c"
            " ON c.claim_id=e.claim_id WHERE c.merged_into IS NOT NULL)"
            " + (SELECT COUNT(*) FROM validation_state v JOIN canonical_claim c"
            " ON c.claim_id=v.claim_id WHERE c.merged_into IS NOT NULL)",
        "no edge claims he asserted it without evidence":
            "SELECT COUNT(*) FROM relationship WHERE asserted_by='brandon'"
            " AND evidence_mention IS NULL",
        "every mention carries a falsifier":
            "SELECT COUNT(*) FROM mention WHERE falsify_match IS NULL OR TRIM(falsify_match)=''",
        "no quote runs past fifteen words":
            "SELECT COUNT(*) FROM mention"
            " WHERE (LENGTH(quote)-LENGTH(REPLACE(quote,' ','')))+1 > 15",
        "no assignment left unreviewed":
            "SELECT COUNT(*) FROM assignment WHERE superseded_by IS NULL"
            " AND delta_type='unreviewed'",
        "every video is dated":
            "SELECT COUNT(*) FROM video WHERE uploaded_on IS NULL",
        "every segment is typed by the latest run":
            "SELECT COUNT(*) FROM segment s WHERE NOT EXISTS (SELECT 1 FROM segment_type t"
            " WHERE t.segment_id=s.segment_id AND t.run_id=(SELECT MAX(run_id) FROM run"
            " WHERE kind='type'))",
        "no verdict overwritten by the mechanical pass":
            "SELECT COUNT(*) FROM validation_state v JOIN run r ON r.run_id=v.run_id"
            " WHERE r.tool='rules-v1' AND v.claim_id IN (SELECT claim_id FROM validation_evidence)"
            " AND v.state_id = (SELECT MAX(state_id) FROM validation_state x"
            " WHERE x.claim_id=v.claim_id)",
    }.items():
        n = q(sql)
        check(name, n == 0, "" if n == 0 else f"{n} offending rows")


print("dead flags")
dead_flags()
print("\npartitions")
tier_partition()
print("\nintegrity")
integrity()
print(f"\n{'ALL CHECKS PASS' if not fails else str(len(fails)) + ' FAILED: ' + ', '.join(fails)}")
sys.exit(1 if fails else 0)

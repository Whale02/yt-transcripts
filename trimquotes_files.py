# -*- coding: utf-8 -*-
"""Apply the same trims to the mentions-*.json source files, so reloading one
cannot put an over-cap quote back into the database. Each over-cap file quote is
matched to its trimmed form by substring; an ambiguous or absent match is
reported rather than guessed."""
import json, glob, re, sys
from trimquotes import FIX

trimmed = sorted(set(FIX.values()), key=len, reverse=True)
changed, unmatched, ambiguous = 0, [], []

for path in sorted(glob.glob("mentions-*.json")):
    raw = open(path, encoding="utf-8").read()
    d = json.loads(raw)
    ms = d["mentions"] if isinstance(d, dict) else d
    edits = []
    for m in ms:
        q = m.get("quote", "")
        if len(q.split()) <= 15:
            continue
        cands = [t for t in trimmed if t in q]
        if not cands:
            unmatched.append((path, m["video_id"], m["start_s"], q))
            continue
        best = cands[0]
        if len(cands) > 1 and len(cands[1]) == len(best):
            ambiguous.append((path, m["video_id"], m["start_s"], q, cands[:2]))
            continue
        edits.append((q, best))
    for old, new in edits:
        needle = json.dumps(old, ensure_ascii=False)
        repl = json.dumps(new, ensure_ascii=False)
        if raw.count(needle) < 1:
            unmatched.append((path, "raw-miss", 0, old))
            continue
        raw = raw.replace(needle, repl)
        changed += 1
    if edits:
        json.loads(raw)  # refuse to write anything that no longer parses
        open(path, "w", encoding="utf-8").write(raw)

print("quotes rewritten in source files:", changed)
if ambiguous:
    print("ambiguous, left alone:")
    for a in ambiguous:
        print("  ", a)
if unmatched:
    print("no trimmed form on file, left alone:")
    for u in unmatched:
        print("  ", u)

still = 0
for path in sorted(glob.glob("mentions-*.json")):
    d = json.loads(open(path, encoding="utf-8").read())
    ms = d["mentions"] if isinstance(d, dict) else d
    for m in ms:
        if len(m.get("quote", "").split()) > 15:
            still += 1
            print("still over cap:", path, m["video_id"], m["start_s"])
print("source files still over cap:", still)

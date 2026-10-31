import sqlite3, sys, json
con = sqlite3.connect('prophecy.db'); con.row_factory = sqlite3.Row
for cid in sys.argv[1:]:
    c = con.execute("SELECT * FROM canonical_claim WHERE claim_id=?", (cid,)).fetchone()
    print("="*90)
    print(f"[{cid}] {c['label'] if c else '(no claim row)'}")
    if c and c['description']: print("  desc:", c['description'])
    rows = con.execute("""SELECT m.uttered_at,m.video_id,m.start_s,m.claim_text,m.time_phrase,m.due_at,
                            m.conditionality,m.certainty,m.falsify_match,m.falsify_miss,a.delta_type
                          FROM assignment a JOIN mention m ON m.mention_id=a.mention_id
                          WHERE a.superseded_by IS NULL AND a.claim_id=?
                          ORDER BY m.uttered_at""",(cid,)).fetchall()
    for r in rows:
        print(f"  {r['uttered_at']} {r['video_id']}@{r['start_s']} [{r['delta_type']}] when={r['time_phrase']} due={r['due_at']} cond={r['conditionality']}")
        print(f"     {r['claim_text']}")
    if rows:
        print(f"  FALSIFY_MATCH: {rows[0]['falsify_match']}")
        print(f"  FALSIFY_MISS : {rows[0]['falsify_miss']}")

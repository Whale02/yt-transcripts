#!/usr/bin/env python3
"""Render the current database to a single self-contained HTML page.

  python export_view.py               # writes prophecy-db.html from prophecy.db

Every number on the page is read out of the database at render time, so the page is a
view and never a second copy of the truth. Re-run it after any load, review or evidence
pass and republish the same file.
"""

from __future__ import annotations

import html
import json
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

DB = sys.argv[1] if len(sys.argv) > 1 else "prophecy.db"
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else "prophecy-db.html")

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
q1 = lambda s, p=(): con.execute(s, p).fetchone()[0]
e = html.escape


def ts(sec):
    sec = int(sec or 0)
    return f"{sec // 3600}:{(sec % 3600) // 60:02d}:{sec % 60:02d}" if sec >= 3600 \
        else f"{sec // 60}:{sec % 60:02d}"


# ------------------------------------------------------------------ gather
videos = q1("SELECT COUNT(*) FROM video")
hours = q1("SELECT COALESCE(SUM(duration_s),0)/3600 FROM video")
segs = q1("SELECT COUNT(*) FROM segment")
words = q1("SELECT COALESCE(SUM(word_count),0) FROM segment")
span = con.execute("SELECT MIN(uploaded_on) a, MAX(uploaded_on) b FROM video").fetchone()
mentions = q1("SELECT COUNT(*) FROM mention")
extracted_vids = q1("SELECT COUNT(DISTINCT video_id) FROM mention")
type_run = q1("SELECT MAX(run_id) FROM run WHERE kind='type'")
types = con.execute("""SELECT content_type, COUNT(*) n, SUM(has_payload) p
                       FROM segment_type WHERE run_id=? GROUP BY content_type
                       ORDER BY n DESC""", (type_run,)).fetchall()
in_pack = q1("""SELECT COUNT(*) FROM segment_type WHERE run_id=?
                AND (content_type='content' OR has_payload=1)""", (type_run,))
fa_total = q1("SELECT COUNT(*) FROM fulfilment_assertion")
fa_strong = q1("SELECT COUNT(*) FROM fulfilment_assertion WHERE strength='strong'")

claims = con.execute("""
  SELECT c.claim_id, c.label, c.domain, c.description,
         COUNT(a.assignment_id) n,
         COUNT(DISTINCT m.video_id) vids,
         MIN(m.uttered_at) first_said, MAX(m.uttered_at) last_said
  FROM canonical_claim c
  LEFT JOIN assignment a ON a.claim_id=c.claim_id AND a.superseded_by IS NULL
                        AND a.same_event IN ('yes','unsure')
  LEFT JOIN mention m ON m.mention_id=a.mention_id
  WHERE c.merged_into IS NULL          -- a folded duplicate would show its event twice
  GROUP BY c.claim_id ORDER BY n DESC, c.claim_id""").fetchall()

state_of = {r["claim_id"]: r for r in con.execute("""
  SELECT claim_id, state, rationale FROM validation_state v WHERE state_id =
    (SELECT MAX(state_id) FROM validation_state x WHERE x.claim_id=v.claim_id)""")}

evidence = defaultdict(list)
for r in con.execute("SELECT * FROM validation_evidence ORDER BY observed_on"):
    evidence[r["claim_id"]].append(r)

threads = defaultdict(list)
for r in con.execute("""
  SELECT a.claim_id, a.delta_type, a.same_event, a.delta_note, m.*, v.title
  FROM assignment a JOIN mention m ON m.mention_id=a.mention_id
  JOIN video v ON v.video_id=m.video_id
  WHERE a.superseded_by IS NULL AND a.claim_id IS NOT NULL AND a.same_event IN ('yes','unsure')
  ORDER BY m.uttered_at, m.start_s"""):
    threads[r["claim_id"]].append(r)

rels = con.execute("""SELECT r.*, c1.label l1, c2.label l2 FROM relationship r
                      JOIN canonical_claim c1 ON c1.claim_id=r.from_claim
                      JOIN canonical_claim c2 ON c2.claim_id=r.to_claim
                      ORDER BY r.asserted_by DESC, c1.label""").fetchall()

fulfils = con.execute("""SELECT f.*, v.title FROM fulfilment_assertion f
                         JOIN video v ON v.video_id=f.video_id
                         WHERE f.strength='strong'
                         ORDER BY f.uttered_at DESC LIMIT 24""").fetchall()

STATE_CLASS = {"CONTRADICTED": "bad", "EXPIRED_WITHOUT_MATCH": "bad",
               "STRONG_MATCH": "good", "PARTIAL_MATCH": "mid", "POTENTIAL_MATCH": "mid",
               "NOT_YET_DUE": "pend", "UNRESOLVED": "pend", "UNFALSIFIABLE": "null",
               "SUPERSEDED": "null"}
DELTA_CLASS = {"first_mention": "d-first", "contradiction": "d-contra", "delay_claim": "d-contra",
               "severity_update": "d-sev", "timing_update": "d-time",
               "new_detail": "d-new", "elaboration": "d-elab", "restatement": "d-rep",
               "exact_repeat": "d-rep", "branch": "d-branch", "unreviewed": "d-none",
               "new_event": "d-none"}

# ------------------------------------------------------------------- render
P = []
w = P.append

w(f"""<title>Last Days Claim Database</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
:root {{
  --paper:#EFF1F3; --surface:#FFF; --ink:#15181E; --muted:#5B6472; --faint:#8B95A2;
  --rule:#D6DAE1; --accent:#2F4858; --good:#1C6B4B; --mid:#8A6212; --bad:#973232;
  --pend:#4A5568; --null:#7A828E;
  --shadow:0 1px 2px rgba(20,24,30,.05),0 8px 22px rgba(20,24,30,.05);
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --paper:#111419; --surface:#181C22; --ink:#E2E6EB; --muted:#98A1AD; --faint:#6C7683;
    --rule:#272D36; --accent:#8FB3C4; --good:#5FBE94; --mid:#D6A44B; --bad:#E0776F;
    --pend:#9AA4B2; --null:#7B8593;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 26px rgba(0,0,0,.3);
  }}
}}
:root[data-theme="dark"] {{
  --paper:#111419; --surface:#181C22; --ink:#E2E6EB; --muted:#98A1AD; --faint:#6C7683;
  --rule:#272D36; --accent:#8FB3C4; --good:#5FBE94; --mid:#D6A44B; --bad:#E0776F;
  --pend:#9AA4B2; --null:#7B8593;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 26px rgba(0,0,0,.3);
}}
*{{box-sizing:border-box}}
body{{background:var(--paper);color:var(--ink);font-family:"IBM Plex Sans",system-ui,sans-serif;
 font-size:15px;line-height:1.6}}
.wrap{{max-width:1000px;margin:0 auto;padding:0 22px 90px}}
header.top{{padding:52px 0 24px;border-bottom:1px solid var(--rule);margin-bottom:36px}}
.eyebrow{{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.14em;
 text-transform:uppercase;color:var(--faint)}}
h1{{font-family:Newsreader,Georgia,serif;font-weight:500;font-size:clamp(30px,5vw,46px);
 line-height:1.1;margin:10px 0 12px;letter-spacing:-.015em}}
.lede{{font-family:Newsreader,Georgia,serif;font-size:18px;color:var(--muted);max-width:62ch;margin:0}}
h2{{font-family:Newsreader,Georgia,serif;font-weight:500;font-size:25px;margin:44px 0 4px}}
h2:first-of-type{{margin-top:0}}
.sub{{color:var(--muted);max-width:70ch;margin:0 0 18px}}
.grid{{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));margin:18px 0 8px}}
.stat{{background:var(--surface);border:1px solid var(--rule);border-radius:2px;padding:12px 14px;
 box-shadow:var(--shadow)}}
.stat .k{{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.1em;
 text-transform:uppercase;color:var(--faint)}}
.stat .v{{font-family:"IBM Plex Mono",monospace;font-size:22px;font-variant-numeric:tabular-nums;
 margin-top:3px}}
.stat .n{{color:var(--muted);font-size:12.5px;margin-top:2px}}
.tw{{overflow-x:auto;border:1px solid var(--rule);border-radius:2px;background:var(--surface);
 box-shadow:var(--shadow);margin-bottom:14px}}
table{{border-collapse:collapse;width:100%;min-width:600px;font-size:14px}}
th{{text-align:left;font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:.1em;
 text-transform:uppercase;color:var(--faint);font-weight:500;padding:10px 12px;
 border-bottom:1px solid var(--rule);white-space:nowrap}}
td{{padding:10px 12px;border-bottom:1px solid var(--rule);vertical-align:top}}
tr:last-child td{{border-bottom:none}}
td.num{{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;text-align:right;
 white-space:nowrap;color:var(--muted)}}
a{{color:var(--accent);text-decoration:none;border-bottom:1px solid color-mix(in srgb,var(--accent) 32%,transparent)}}
a:hover{{border-bottom-color:var(--accent)}}
a:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
.pill{{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:9.5px;letter-spacing:.07em;
 text-transform:uppercase;padding:2px 6px;border:1px solid currentColor;border-radius:2px;white-space:nowrap}}
.good{{color:var(--good)}} .mid{{color:var(--mid)}} .bad{{color:var(--bad)}}
.pend{{color:var(--pend)}} .null{{color:var(--null)}}
details.claim{{background:var(--surface);border:1px solid var(--rule);border-radius:2px;
 margin-bottom:8px;box-shadow:var(--shadow)}}
details.claim>summary{{padding:13px 16px;cursor:pointer;list-style:none;display:flex;
 gap:12px;align-items:baseline;flex-wrap:wrap}}
details.claim>summary::-webkit-details-marker{{display:none}}
summary .lab{{font-weight:600;flex:1;min-width:250px}}
summary .meta{{font-family:"IBM Plex Mono",monospace;font-size:11.5px;color:var(--faint);
 font-variant-numeric:tabular-nums}}
.body{{padding:0 16px 16px;border-top:1px solid var(--rule)}}
.desc{{color:var(--muted);font-size:14px;margin:12px 0 16px;max-width:74ch}}
.ev{{border-left:2px solid var(--rule);padding:0 0 0 14px;margin:0 0 16px}}
.ev .row{{padding:9px 0;border-bottom:1px dotted var(--rule)}}
.ev .row:last-child{{border-bottom:none}}
.ev .hd{{font-family:"IBM Plex Mono",monospace;font-size:11.5px;color:var(--faint);
 display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;font-variant-numeric:tabular-nums}}
.ev .claimtext{{margin:4px 0 3px}}
.ev .fields{{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--faint)}}
.ev q{{color:var(--muted);font-style:italic}}
.ev .note{{color:var(--muted);font-size:13px;margin-top:4px}}
.d-first{{color:var(--accent)}} .d-contra{{color:var(--bad)}} .d-sev{{color:var(--mid)}}
.d-time{{color:var(--mid)}} .d-new{{color:var(--good)}} .d-elab{{color:var(--muted)}}
.d-rep{{color:var(--faint)}} .d-branch{{color:var(--mid)}} .d-none{{color:var(--faint)}}
.verdict{{background:var(--paper);border:1px solid var(--rule);border-radius:2px;padding:12px 14px;
 margin-top:6px}}
.verdict h4{{margin:0 0 6px;font-family:"IBM Plex Mono",monospace;font-size:10.5px;
 letter-spacing:.1em;text-transform:uppercase;color:var(--faint);font-weight:500}}
.verdict p{{margin:0 0 8px;font-size:13.5px;color:var(--muted)}}
footer{{border-top:1px solid var(--rule);margin-top:56px;padding-top:18px;color:var(--faint);
 font-size:12.5px}}
code{{font-family:"IBM Plex Mono",monospace;font-size:12.5px;background:var(--surface);
 border:1px solid var(--rule);border-radius:2px;padding:1px 5px}}
.filter{{width:100%;max-width:520px;padding:9px 12px;margin:0 0 6px;font:14px "IBM Plex Sans",
 system-ui,sans-serif;color:var(--ink);background:var(--surface);border:1px solid var(--rule);
 border-radius:3px}}
.filter:focus{{outline:2px solid var(--accent);outline-offset:1px}}
</style>
<div class="wrap">
<header class="top">
  <div class="eyebrow">generated from prophecy.db &middot; every figure read at render time</div>
  <h1>Last Days Claim Database</h1>
  <p class="lede">Every video Brandon Biggs has published, cut into timestamped passages, filtered,
  and turned into event threads that show what each new video added to a claim he had already made.</p>
</header>

<h2>Corpus</h2>
<p class="sub">The source layer is complete and immutable. Everything below it is derived and can be
rebuilt from these transcripts.</p>
<div class="grid">""")

for k, v, n in [("videos", f"{videos}", f"of 577 on the channel"),
                ("hours", f"{hours:,}", f"{span['a']} to {span['b']}"),
                ("passages", f"{segs:,}", "roughly 110 words each"),
                ("words", f"{words/1e6:.2f}M", "auto-captions, cleaned"),
                ("claims extracted", f"{mentions}", f"from {extracted_vids} videos so far"),
                ("fulfilment claims", f"{fa_total:,}", f"{fa_strong} strong assertions")]:
    w(f'<div class="stat"><div class="k">{k}</div><div class="v">{v}</div><div class="n">{n}</div></div>')
w("</div>")

w("""<h2>What the filter removes</h2>
<p class="sub">Prayer, worship, promotion and personal stories are typed out of the extraction queue,
but never deleted, and a prayer that carries a forecast inside it stays in.</p>
<div class="tw"><table>
<thead><tr><th>bucket</th><th>passages</th><th>carrying a claim</th><th>queued for extraction</th></tr></thead><tbody>""")
for t in types:
    keep = "all" if t["content_type"] == "content" else (f"{t['p']:,}" if t["p"] else "none")
    w(f"<tr><td>{e(t['content_type'])}</td><td class='num'>{t['n']:,}</td>"
      f"<td class='num'>{t['p']:,}</td><td class='num'>{keep}</td></tr>")
w(f"</tbody></table></div><p class='sub'>{in_pack:,} passages are queued for claim extraction; "
  f"{segs - in_pack:,} are filtered out.</p>")

# ---- scoreboard: the claims that have actually been checked, above the pile of 1,000 ----
ORDER = {"CONTRADICTED": 0, "EXPIRED_WITHOUT_MATCH": 1, "PARTIAL_MATCH": 2,
         "STRONG_MATCH": 3, "NOT_YET_DUE": 4, "UNFALSIFIABLE": 5}
judged = [c for c in claims if evidence.get(c["claim_id"])]
judged.sort(key=lambda c: (ORDER.get(state_of.get(c["claim_id"], {})["state"]
                                     if state_of.get(c["claim_id"]) else "", 9),
                           -c["n"]))
w(f"""<h2>Scored against reality</h2>
<p class="sub">The {len(judged)} claims checked against live sources so far, worst first. Everything
else in the table below is either not yet due, unfalsifiable as he stated it, or still unchecked.
The rationale is where the base rate lives: a claim that would have happened anyway is held at
partial no matter how precisely it was dated.</p>
<div class="tw"><table><thead><tr><th>verdict</th><th>claim</th><th>what happened</th></tr></thead>
<tbody>""")
for c in judged:
    st = state_of.get(c["claim_id"])
    cls = STATE_CLASS.get(st["state"], "pend") if st else "pend"
    ev1 = evidence[c["claim_id"]][0]
    w(f'<tr><td><span class="pill {cls}">{e(st["state"] if st else "")}</span></td>'
      f'<td><strong>{e(c["label"])}</strong><div class="fields">said {c["first_said"]}'
      f'{" to " + c["last_said"] if c["last_said"] != c["first_said"] else ""}'
      f' &middot; {c["n"]} telling{"s" if c["n"] != 1 else ""}</div></td>'
      f'<td>{e((ev1["summary"] or "")[:260])} '
      f'<a href="{e(ev1["source_url"] or "#")}">source</a></td></tr>')
w("</tbody></table></div>")

w("""<h2>Claims</h2>
<p class="sub">Each row is one underlying event, not one video. Open it to see every time he
returned to it and what changed. Verdicts are ours and live in their own table; they never
edit his words.</p>
<input id="q" class="filter" type="search" placeholder="filter claims: try famine, 2027, crypto, earthquake">
<p class="sub" id="qn"></p>""")

for c in claims:
    st = state_of.get(c["claim_id"])
    cls = STATE_CLASS.get(st["state"], "pend") if st else "pend"
    label = st["state"] if st else "NO VERDICT"
    rows = threads.get(c["claim_id"], [])
    w(f"""<details class="claim"><summary>
      <span class="lab">{e(c['label'])}</span>
      <span class="pill {cls}">{e(label)}</span>
      <span class="meta">{c['n']} mention{'s' if c['n'] != 1 else ''} &middot; {c['vids']} video{'s' if c['vids'] != 1 else ''}"""
      + (f" &middot; {c['first_said']} to {c['last_said']}" if c["first_said"] else "")
      + "</span></summary><div class=\"body\">")
    w(f'<p class="desc">{e(c["description"] or "")}</p>')
    if rows:
        w('<div class="ev">')
        for r in rows:
            dc = DELTA_CLASS.get(r["delta_type"], "d-none")
            w(f'<div class="row"><div class="hd"><span>{r["uttered_at"] or "????-??-??"}</span>'
              f'<span class="pill {dc}">{e(r["delta_type"])}</span>'
              f'<a href="https://youtu.be/{r["video_id"]}?t={r["start_s"]}">{ts(r["start_s"])}</a>'
              f'<span>{e((r["title"] or "")[:56])}</span></div>')
            w(f'<div class="claimtext">{e(r["claim_text"])}</div>')
            bits = [f'mode={r["source_mode"] or "?"}', f'certainty={r["certainty"] or "?"}',
                    f'conditional={r["conditionality"] or "?"}']
            if r["time_phrase"]:
                bits.insert(0, f'when="{e(r["time_phrase"])}"')
            if r["magnitude"]:
                bits.append(f'magnitude={e(r["magnitude"])}')
            w(f'<div class="fields">{" &middot; ".join(bits)}</div>')
            if r["quote"]:
                w(f'<div><q>{e(r["quote"])}</q></div>')
            if r["delta_note"]:
                w(f'<div class="note">{e(r["delta_note"])}</div>')
            w("</div>")
        w("</div>")
    evs = evidence.get(c["claim_id"], [])
    if evs or st:
        w('<div class="verdict"><h4>what actually happened</h4>')
        if evs:
            for x in evs:
                w(f'<p><strong>{x["observed_on"] or ""}</strong> {e(x["summary"] or "")} '
                  f'<a href="{e(x["source_url"] or "#")}">source</a></p>')
        else:
            w('<p>No external evidence recorded yet.</p>')
        if st:
            w(f'<h4>our verdict</h4><p><span class="pill {cls}">{e(st["state"])}</span> '
              f'{e(st["rationale"] or "")}</p>')
        w("</div>")
    w("</div></details>")

w("""<h2>What he says already came true</h2>
<p class="sub">His own fulfilment claims, kept in a separate table because they are speech, not
evidence. The scan found """ + f"{fa_total:,} candidates and rated {fa_strong} as strong assertions "
  """rather than discourse filler. Most recent first.</p>
<div class="tw"><table><thead><tr><th>said on</th><th>cue</th><th>passage</th><th>at</th></tr></thead><tbody>""")
for f in fulfils:
    w(f'<tr><td class="num">{f["uttered_at"] or ""}</td><td><span class="pill mid">{e(f["cue"])}</span></td>'
      f'<td>{e((f["quote"] or "")[:190])}</td>'
      f'<td class="num"><a href="https://youtu.be/{f["video_id"]}?t={f["start_s"]}">{ts(f["start_s"])}</a></td></tr>')
w("</tbody></table></div>")

if rels:
    w("""<h2>Event graph</h2>
    <p class="sub">Links between claims. The system refuses to record an edge as his unless it names
    the passage where he states it, so our inferences can never be mistaken for his.</p>
    <div class="tw"><table><thead><tr><th>from</th><th>relation</th><th>to</th><th>asserted by</th></tr></thead><tbody>""")
    for r in rels:
        who = "he states it" if r["asserted_by"] == "brandon" else "we infer it"
        cls = "good" if r["asserted_by"] == "brandon" else "null"
        w(f'<tr><td>{e(r["l1"])}</td><td><code>{e(r["rel_type"])}</code></td><td>{e(r["l2"])}</td>'
          f'<td><span class="pill {cls}">{who}</span></td></tr>')
    w("</tbody></table></div>")

w(f"""<h2>Honest coverage</h2>
<p class="sub">The corpus is complete; the claim extraction is not. {mentions} claims have been
pulled from {extracted_vids} of {videos} videos. The remaining {in_pack:,} queued passages need the
same reading pass before the threads above can be called exhaustive. Nothing on this page is
inferred from an unread video.</p>""")

# plain string, not an f-string: the braces below are JavaScript
w("""<script>
(function () {
  var q = document.getElementById("q"), n = document.getElementById("qn");
  if (!q) return;
  var rows = Array.prototype.slice.call(document.querySelectorAll("details.claim"));
  rows.forEach(function (r) { r.dataset.hay = r.textContent.toLowerCase(); });
  function run() {
    var t = q.value.trim().toLowerCase(), shown = 0;
    rows.forEach(function (r) {
      var hit = !t || r.dataset.hay.indexOf(t) !== -1;
      r.hidden = !hit;
      if (hit) shown++;
    });
    n.textContent = t ? shown + " of " + rows.length + " claims match “" + q.value.trim() + "”"
                      : rows.length + " claims";
  }
  q.addEventListener("input", run);
  run();
})();
</script>
<footer>Rendered from prophecy.db by export_view.py. Passage timestamps link to the moment on
YouTube, so every claim here can be checked against the source. Verdicts, his fulfilment claims,
and his original words are three separate tables and are never merged.</footer>
</div>""")

OUT.write_text("\n".join(P), encoding="utf-8")
print(f"{OUT} written ({OUT.stat().st_size/1024:.0f} KB) from {DB}")

#!/usr/bin/env python3
"""Longitudinal claim database for a prophetic source.

  python prophecy.py init
  python prophecy.py ingest corpus/          # transcripts -> videos + segments (immutable)
  python prophecy.py dates                   # fill uttered_at from YouTube upload dates
  python prophecy.py type                    # segment content-type + payload flag (rules pass)
  python prophecy.py pack -o packs/          # extraction prompts for content segments
  python prophecy.py load mentions.json      # mentions from any extractor, version stamped
  python prophecy.py seed seeds.json         # canonical claims (hand-seeded anchors)
  python prophecy.py cluster                 # blocking + assignment, append-only
  python prophecy.py scan                    # find where he says an earlier word landed
  python prophecy.py fulfilled --strong      # HIS fulfilment claims, kept apart from reality
  python prophecy.py search "new madrid"     # raw corpus, before any extraction
  python prophecy.py thread new-madrid       # the full history of one claim
  python prophecy.py timeline --year 2028
  python prophecy.py graph
  python prophecy.py stats

Design rules enforced by the schema, not by discipline:
  * video and segment rows are immutable; everything else is derived and re-runnable
  * every derived row carries a run_id naming the extractor and prompt version
  * assignments are append-only; a changed judgment supersedes, never overwrites
  * "same event?" and "what did this mention add?" are separate fields
  * four things never share a field: what he predicted (mention), what he later claims
    was fulfilled (fulfilment_assertion), what actually happened (validation_evidence),
    and our verdict on the match (validation_state)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sqlite3
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

DB_DEFAULT = "prophecy.db"

SCHEMA = """
PRAGMA journal_mode=WAL;

-- ---------------------------------------------------------------- immutable
CREATE TABLE IF NOT EXISTS video (
  video_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  duration_s INTEGER,
  uploaded_on TEXT,              -- uttered_at anchor for every mention in it
  transcript_sha256 TEXT NOT NULL,
  fetched_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS segment (
  segment_id TEXT PRIMARY KEY,   -- <video_id>:<start_s>
  video_id TEXT NOT NULL REFERENCES video(video_id),
  start_s INTEGER NOT NULL,
  end_s INTEGER,
  word_count INTEGER NOT NULL,
  text TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_segment_video ON segment(video_id, start_s);
CREATE VIRTUAL TABLE IF NOT EXISTS segment_fts USING fts5(segment_id UNINDEXED, text);

-- ------------------------------------------------------------------ derived
CREATE TABLE IF NOT EXISTS run (
  run_id INTEGER PRIMARY KEY AUTOINCREMENT,
  kind TEXT NOT NULL,            -- type | extract | cluster | validate
  tool TEXT NOT NULL,            -- rules-v1 | ollama:qwen3 | claude-opus-5 | human
  prompt_version TEXT,
  started_at TEXT NOT NULL,
  note TEXT
);

CREATE TABLE IF NOT EXISTS segment_type (
  segment_id TEXT NOT NULL REFERENCES segment(segment_id),
  run_id INTEGER NOT NULL REFERENCES run(run_id),
  content_type TEXT NOT NULL,    -- prayer | worship | promo | testimony | commentary | content
  has_payload INTEGER NOT NULL,  -- prayer/worship that still carries a claim
  confidence REAL,
  evidence TEXT,
  PRIMARY KEY (segment_id, run_id)
);

CREATE TABLE IF NOT EXISTS mention (
  mention_id TEXT PRIMARY KEY,
  run_id INTEGER NOT NULL REFERENCES run(run_id),
  duplicate_of TEXT REFERENCES mention(mention_id),  -- a second extraction of one utterance
  video_id TEXT NOT NULL REFERENCES video(video_id),
  segment_id TEXT REFERENCES segment(segment_id),
  start_s INTEGER NOT NULL,
  uttered_at TEXT,               -- axis 1: when he said it (video upload date)
  origin_date TEXT,              -- when the vision/dream itself is dated, if he says
  claim_text TEXT NOT NULL,      -- neutral paraphrase
  quote TEXT,                    -- short verbatim anchor for audit
  content_type TEXT,
  source_mode TEXT,              -- VISION|DREAM|LORD_SAID|IMPRESSION|INTERPRETATION|
                                 -- PERSONAL_INFERENCE|NEWS_COMMENTARY|QUOTING_SOMEONE_ELSE
  certainty TEXT,                -- definite|strong|tentative|speculative
  conditionality TEXT,           -- unconditional|if_x|unless_x|prayer_may_prevent|
                                 -- prayer_may_delay|prayer_may_reduce|multiple_paths|unclear
  condition_text TEXT,
  topics TEXT,                   -- json array, multi-label
  entities TEXT,                 -- json array
  locations TEXT,                -- json array
  time_phrase TEXT,              -- exactly as said
  window_start TEXT,             -- axis 2: predicted_event_time, resolved against uttered_at
  window_end TEXT,
  time_precision TEXT,           -- exact_date|month|season|year|range|relative|none
  due_at TEXT,                   -- when it becomes falsifiable
  severity TEXT,
  magnitude TEXT,
  causes TEXT,                   -- json array, only what he states
  consequences TEXT,             -- json array, only what he states
  falsify_match TEXT,            -- pre-registered: what would count as a hit
  falsify_miss TEXT,             -- pre-registered: what would count as a miss
  created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_mention_video ON mention(video_id, start_s);
CREATE VIRTUAL TABLE IF NOT EXISTS mention_fts USING fts5(mention_id UNINDEXED, claim_text, quote);

CREATE TABLE IF NOT EXISTS canonical_claim (
  claim_id TEXT PRIMARY KEY,     -- stable slug, never regenerated
  label TEXT NOT NULL,
  domain TEXT,
  description TEXT,
  seeded INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL,
  merged_into TEXT REFERENCES canonical_claim(claim_id)  -- set when this id was a duplicate
);
CREATE TABLE IF NOT EXISTS claim_alias (
  claim_id TEXT NOT NULL REFERENCES canonical_claim(claim_id),
  alias TEXT NOT NULL,
  PRIMARY KEY (claim_id, alias)
);

CREATE TABLE IF NOT EXISTS assignment (
  assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
  mention_id TEXT NOT NULL REFERENCES mention(mention_id),
  claim_id TEXT REFERENCES canonical_claim(claim_id),
  run_id INTEGER NOT NULL REFERENCES run(run_id),
  same_event TEXT NOT NULL,      -- yes | no | unsure           (axis A)
  confidence REAL,
  delta_type TEXT NOT NULL,      -- exact_repeat|restatement|elaboration|new_detail|
                                 -- timing_update|severity_update|location_update|
                                 -- contradiction|delay_claim|branch|first_mention|unreviewed
  delta_note TEXT,
  method TEXT NOT NULL,          -- seeded|lexical|model|human
  created_at TEXT NOT NULL,
  superseded_by INTEGER REFERENCES assignment(assignment_id)
);
CREATE INDEX IF NOT EXISTS ix_assign_claim ON assignment(claim_id, superseded_by);
CREATE INDEX IF NOT EXISTS ix_assign_mention ON assignment(mention_id, superseded_by);

CREATE TABLE IF NOT EXISTS relationship (
  rel_id INTEGER PRIMARY KEY AUTOINCREMENT,
  from_claim TEXT NOT NULL REFERENCES canonical_claim(claim_id),
  to_claim TEXT NOT NULL REFERENCES canonical_claim(claim_id),
  rel_type TEXT NOT NULL,        -- precedes|follows|causes|triggers|depends_on|
                                 -- co_occurs_with|part_of|same_event_as|narrative_sequence
  asserted_by TEXT NOT NULL,     -- brandon | system
  evidence_mention TEXT REFERENCES mention(mention_id),
  run_id INTEGER REFERENCES run(run_id),
  note TEXT
);

-- ----------------------------------------------------- reality, kept apart
CREATE TABLE IF NOT EXISTS validation_evidence (
  ev_id INTEGER PRIMARY KEY AUTOINCREMENT,
  claim_id TEXT NOT NULL REFERENCES canonical_claim(claim_id),
  observed_on TEXT,              -- axis 3: when the real event happened
  source_url TEXT,
  summary TEXT,
  added_at TEXT NOT NULL,
  added_by TEXT
);
CREATE TABLE IF NOT EXISTS validation_state (
  state_id INTEGER PRIMARY KEY AUTOINCREMENT,
  claim_id TEXT NOT NULL REFERENCES canonical_claim(claim_id),
  state TEXT NOT NULL,           -- UNRESOLVED|NOT_YET_DUE|POTENTIAL_MATCH|PARTIAL_MATCH|
                                 -- STRONG_MATCH|CONTRADICTED|EXPIRED_WITHOUT_MATCH|
                                 -- UNFALSIFIABLE|SUPERSEDED
  decided_at TEXT NOT NULL,
  rationale TEXT,
  run_id INTEGER REFERENCES run(run_id)
);

-- ------------------------------------------------- HIS fulfilment assertions
-- "I told you this was coming and it just happened." That is still his speech,
-- not reality, so it cannot live in validation_evidence. Third object, third table.
CREATE TABLE IF NOT EXISTS fulfilment_assertion (
  fa_id INTEGER PRIMARY KEY AUTOINCREMENT,
  video_id TEXT NOT NULL REFERENCES video(video_id),
  segment_id TEXT REFERENCES segment(segment_id),
  start_s INTEGER NOT NULL,
  uttered_at TEXT,               -- when he made the fulfilment claim
  claim_id TEXT REFERENCES canonical_claim(claim_id),   -- which prophecy he says landed
  points_back_to TEXT,           -- free text: the earlier word he is invoking
  claimed_event_on TEXT,         -- when he says the real event happened
  real_event TEXT,               -- the news event he points at, in neutral words
  quote TEXT,
  cue TEXT,                      -- the phrase that flagged it
  strength TEXT,                 -- strong | weak: how much the cue itself asserts
  method TEXT NOT NULL,          -- rules | model | human
  run_id INTEGER REFERENCES run(run_id),
  reviewed INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_fa_claim ON fulfilment_assertion(claim_id);
"""

# ---------------------------------------------------------------- rules pass

PRAYER = [
    r"\bfather (?:i|we) (?:thank|pray|ask)", r"\bin jesus'? name\b", r"\bwe plead the blood\b",
    r"\bi plead the blood\b", r"\blord (?:i|we) (?:thank|ask|pray)\b", r"\bthank you (?:father|lord)\b",
    r"\bwe (?:call|declare|decree)\b.{0,30}\b(?:in the name of jesus)\b", r"\bamen\b",
    r"\bhallelujah\b", r"\bwe come (?:before|to) you\b",
]
WORSHIP = [r"\b(?:hallelujah|glory to god)\b.{0,40}\b(?:hallelujah|glory)\b",
           r"\bsing(?:ing)? (?:to|unto) (?:the lord|him)\b"]
PROMO = [
    r"\blike (?:our|the) video\b", r"\bsubscrib", r"\bthe algorithm\b", r"\bcomment (?:down )?below\b",
    r"\bshare (?:this|the) video\b", r"\bpatreon|paypal|cash ?app\b", r"\bhit the bell\b",
    r"\bput a smile on your face\b", r"\bwe'?ll see you (?:all )?next time\b", r"\bgod bless you all\b",
]
PREDICT = re.compile(
    r"\b(i saw|i see|the lord (?:showed|told|said|spoke)|he showed me|god (?:showed|told|said)"
    r"|is coming|are coming|will (?:be|come|happen|see|go|have|hit|fall|rise|crash|close)"
    r"|going to (?:be|come|happen|see|hit|fall|rise|crash|close)|there will|it will|they will"
    r"|shall be|in the vision|in the dream|what's coming|whats coming)\b", re.I)
DOMAIN = re.compile(
    r"\b(earthquake|tsunami|volcano|hurricane|tornado|flood|drought|famine|plague|virus|pandemic"
    r"|dollar|currency|bank|banks|inflation|recession|depression|crash|market|gold|silver|crypto"
    r"|tariff|trade|oil|gas|grid|blackout|power|water|food|grocery|shortage|war|missile|nuclear"
    r"|military|draft|invasion|china|russia|iran|israel|taiwan|ukraine|election|president|congress"
    r"|financial|finances|economy|economic|shaking|collapse|storm|judgment|persecution|famine"
    r"|martial law|riot|looting|internet|ai|chip|surveillance|mark of the beast|tribulation)\b", re.I)
RETROSPECT = re.compile(r"(?:you|lord) (?:showed|warned|told) (?:me|us)|things (?:that )?"
                        r"(?:you|he) (?:showed|warned)|what (?:you|he) showed me", re.I)
# home/family/personal material the user does not want in the corpus
MODAL = re.compile(r"\b(would|could|might|about to|going to|before it|when it (?:hits|comes)"
                   r"|watch for|keep an eye|gonna)\b", re.I)
NARRATIVE = re.compile(r"\b(when i was|years ago|i remember|my (?:wife|son|daughter|grandmother|mom)"
                       r"|growing up|back then)\b", re.I)

PRAYER_RE = [re.compile(p, re.I) for p in PRAYER]
WORSHIP_RE = [re.compile(p, re.I) for p in WORSHIP]
PROMO_RE = [re.compile(p, re.I) for p in PROMO]

TIMED_LINE = re.compile(r"^\[(\d{1,3}):(\d{2})\]\s*(.*)$")
ID_FROM_NAME = re.compile(r"\[([A-Za-z0-9_-]{11})\]")
STOPWORDS = set("""a an the and or but if then than that this these those of in on at to for with
by from as is are was were be been being it its he she they them his her their we you i me my our
your not no so very just like about into over under again more most some any all one two do does did
did doing have has had having will would can could should shall may might must there here what which
who whom when where why how said say says told tell going get got know think going lord god jesus
""".split())


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def connect(path):
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    con.execute("PRAGMA busy_timeout=30000")   # a long typing run holds the write lock
    return con


def migrate(con):
    """Additive column migrations. CREATE TABLE IF NOT EXISTS never alters an existing table,
    so a database made before a column existed needs the ALTER stated here."""
    have = {r["name"] for r in con.execute("PRAGMA table_info(canonical_claim)")}
    if "merged_into" not in have:
        con.execute("ALTER TABLE canonical_claim ADD COLUMN merged_into TEXT "
                    "REFERENCES canonical_claim(claim_id)")
        con.commit()
    have = {r["name"] for r in con.execute("PRAGMA table_info(mention)")}
    if "duplicate_of" not in have:
        con.execute("ALTER TABLE mention ADD COLUMN duplicate_of TEXT "
                    "REFERENCES mention(mention_id)")
        con.commit()


def new_run(con, kind, tool, prompt_version=None, note=None):
    cur = con.execute(
        "INSERT INTO run (kind, tool, prompt_version, started_at, note) VALUES (?,?,?,?,?)",
        (kind, tool, prompt_version, now(), note))
    con.commit()
    return cur.lastrowid


def latest_run(con, kind):
    row = con.execute("SELECT run_id FROM run WHERE kind=? ORDER BY run_id DESC LIMIT 1",
                      (kind,)).fetchone()
    return row["run_id"] if row else None


# --------------------------------------------------------------------- ingest

def read_cues(path: Path):
    cues = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line:
            continue
        m = TIMED_LINE.match(line)
        if m:
            cues.append((int(m.group(1)) * 60 + int(m.group(2)), m.group(3).strip()))
        elif cues:
            cues[-1] = (cues[-1][0], (cues[-1][1] + " " + line).strip())
    return cues


def segment_cues(cues, target_words=110, max_gap=8):
    """Passages of roughly target_words, broken at long pauses. Start times preserved."""
    out, buf, start, prev, n = [], [], None, None, 0
    for t, text in cues:
        if start is None:
            start = t
        if buf and (n >= target_words or (prev is not None and t - prev > max_gap)):
            out.append((start, prev, " ".join(buf)))
            buf, start, n = [], t, 0
        buf.append(text)
        n += len(text.split())
        prev = t
    if buf:
        out.append((start, prev, " ".join(buf)))
    return out


def cmd_ingest(args, con):
    indir = Path(args.indir).resolve()
    files = sorted(f for f in indir.glob("*.txt") if not f.name.startswith("."))
    if not files:
        sys.exit(f"no transcripts in {indir}")

    manifest = {}
    mpath = indir / "manifest.tsv"
    if mpath.exists():
        for line in mpath.read_text(encoding="utf-8").splitlines()[1:]:
            parts = line.split("\t")
            if len(parts) >= 4:
                rec = {"title": parts[1], "duration": parts[2], "url": parts[3]}
                # newer manifests carry the upload date, which saves a second yt-dlp pass
                if len(parts) >= 5 and len(parts[4]) == 8 and parts[4].isdigit():
                    d = parts[4]
                    rec["uploaded_on"] = f"{d[:4]}-{d[4:6]}-{d[6:]}"
                manifest[parts[0]] = rec

    added_v = added_s = skipped = 0
    for f in files:
        m = ID_FROM_NAME.search(f.name)
        if not m:
            continue
        vid = m.group(1)
        blob = f.read_bytes()
        sha = hashlib.sha256(blob).hexdigest()
        row = con.execute("SELECT transcript_sha256 FROM video WHERE video_id=?", (vid,)).fetchone()
        if row and row["transcript_sha256"] == sha:
            skipped += 1
            continue
        meta = manifest.get(vid, {})
        title = meta.get("title") or ID_FROM_NAME.sub("", f.stem).strip()
        dur = meta.get("duration")
        # a re-ingest must not drop a date already fetched by `dates`
        prior = con.execute("SELECT uploaded_on FROM video WHERE video_id=?", (vid,)).fetchone()
        uploaded = meta.get("uploaded_on") or (prior["uploaded_on"] if prior else None)
        con.execute(
            "INSERT OR REPLACE INTO video (video_id,title,url,duration_s,uploaded_on,"
            "transcript_sha256,fetched_at) VALUES (?,?,?,?,?,?,?)",
            (vid, title, meta.get("url") or f"https://youtu.be/{vid}",
             int(dur) if dur and dur.isdigit() else None, uploaded, sha, now()))
        # A corrected transcript re-segments the video. Mentions survive it: they carry
        # start_s, which is stable, so unlink them, rebuild, then re-link by time.
        con.execute("UPDATE mention SET segment_id=NULL WHERE video_id=?", (vid,))
        con.execute("DELETE FROM segment_fts WHERE segment_id IN "
                    "(SELECT segment_id FROM segment WHERE video_id=?)", (vid,))
        con.execute("DELETE FROM segment_type WHERE segment_id IN "
                    "(SELECT segment_id FROM segment WHERE video_id=?)", (vid,))
        con.execute("DELETE FROM segment WHERE video_id=?", (vid,))
        for start, end, text in segment_cues(read_cues(f)):
            sid = f"{vid}:{start}"
            con.execute(
                "INSERT OR REPLACE INTO segment (segment_id,video_id,start_s,end_s,word_count,text)"
                " VALUES (?,?,?,?,?,?)", (sid, vid, start, end, len(text.split()), text))
            con.execute("INSERT INTO segment_fts (segment_id,text) VALUES (?,?)", (sid, text))
            added_s += 1
        con.execute("""UPDATE mention SET segment_id = (
                         SELECT s.segment_id FROM segment s
                         WHERE s.video_id = mention.video_id AND s.start_s <= mention.start_s
                         ORDER BY s.start_s DESC LIMIT 1)
                       WHERE video_id = ?""", (vid,))
        added_v += 1
    con.commit()
    print(f"ingested {added_v} videos, {added_s} segments ({skipped} unchanged)")


def cmd_dates(args, con):
    """uttered_at is the anchor every relative date resolves against, so it is not optional."""
    rows = con.execute("SELECT video_id FROM video WHERE uploaded_on IS NULL").fetchall()
    if not rows:
        print("all videos already dated")
        return
    ids = [r["video_id"] for r in rows]
    print(f"fetching upload dates for {len(ids)} videos ...")
    done = 0
    for chunk in (ids[i:i + 40] for i in range(0, len(ids), 40)):
        cmd = [sys.executable, "-m", "yt_dlp", "--skip-download", "--no-warnings", "--ignore-errors",
               "--print", "%(id)s|%(upload_date)s"] + [f"https://youtu.be/{v}" for v in chunk]
        out = subprocess.run(cmd, capture_output=True, text=True).stdout
        for line in out.splitlines():
            if "|" not in line:
                continue
            vid, d = line.strip().split("|", 1)
            if len(d) == 8 and d.isdigit():
                con.execute("UPDATE video SET uploaded_on=? WHERE video_id=?",
                            (f"{d[:4]}-{d[4:6]}-{d[6:]}", vid))
                done += 1
        con.commit()
    print(f"dated {done} videos")


# ----------------------------------------------------------------- typing

def type_segment(text):
    low = text.lower()
    # Auto-captions sometimes loop a phrase for minutes, and sung refrains repeat by nature.
    # Either way there is nothing for an extractor to read, so keep them out of the pack.
    words = re.findall(r"[a-z']+", low)
    if len(words) > 30 and len(set(words)) / len(words) < 0.30:
        return "garbled", 0, 0.8, f"loop:{len(set(words))}/{len(words)}"
    prayer_hits = sum(1 for r in PRAYER_RE if r.search(low))
    worship_hits = sum(1 for r in WORSHIP_RE if r.search(low))
    promo_hits = sum(1 for r in PROMO_RE if r.search(low))
    predicts = bool(PREDICT.search(text))
    domain = len(set(m.group(0).lower() for m in DOMAIN.finditer(text)))

    if promo_hits >= 1 and not predicts:
        return "promo", 0, 0.8, f"promo:{promo_hits}"
    payload = int(predicts and (domain > 0 or RETROSPECT.search(text) is not None))
    if worship_hits >= 1 and prayer_hits >= 1:
        # prayer can carry a claim: "protect them because I saw X coming"
        return "worship", payload, 0.7, f"worship:{worship_hits}"
    if prayer_hits >= 2:
        return "prayer", payload, 0.75, f"prayer:{prayer_hits},payload:{payload}"
    if prayer_hits == 1 and not predicts:
        return "prayer", 0, 0.55, "prayer:1"
    if prayer_hits == 1 and payload:
        return "prayer", 1, 0.6, "prayer:1,payload:1"
    if NARRATIVE.search(text) and not predicts and domain == 0:
        return "testimony", 0, 0.5, "narrative"
    if predicts or domain:
        return "content", 1, 0.6 if domain else 0.5, f"predict:{int(predicts)},domain:{domain}"
    # Commentary with a forward modal still hides claims ("an uncovering of a scandal would
    # try to keep him at bay"). Keep the honest type, but send it to the extractor: a missed
    # claim is invisible forever, an extra segment only costs tokens.
    if MODAL.search(text):
        return "commentary", 1, 0.35, "modal"
    return "commentary", 0, 0.4, "none"


def cmd_type(args, con):
    run_id = new_run(con, "type", "rules-v1", note="regex segment typing")
    rows = con.execute("SELECT segment_id, text FROM segment").fetchall()
    counts = Counter()
    payload = 0
    for i, r in enumerate(rows, 1):
        ct, pay, conf, ev = type_segment(r["text"])
        counts[ct] += 1
        payload += pay if ct in ("prayer", "worship") else 0
        con.execute("INSERT OR REPLACE INTO segment_type (segment_id,run_id,content_type,"
                    "has_payload,confidence,evidence) VALUES (?,?,?,?,?,?)",
                    (r["segment_id"], run_id, ct, pay, conf, ev))
        if i % 5000 == 0:                      # a 50k-segment run is not all-or-nothing
            con.commit()
            print(f"  {i}/{len(rows)} ...", flush=True)
    con.commit()
    total = sum(counts.values())
    print(f"run {run_id}: typed {total} segments")
    for ct, n in counts.most_common():
        print(f"  {ct:<12} {n:>6}  {n*100//max(total,1):>3}%")
    print(f"  prayer/worship segments still carrying a claim: {payload}")


# ------------------------------------------------------------------ packing

PACK_INSTRUCTIONS = """Extract every distinct forward-looking claim in the passage.
Return JSON: {"mentions":[{...}]} with one object per atomic claim, fields:
claim_text (neutral paraphrase, one sentence), quote (<=15 words verbatim),
source_mode (VISION|DREAM|LORD_SAID|IMPRESSION|INTERPRETATION|PERSONAL_INFERENCE|
NEWS_COMMENTARY|QUOTING_SOMEONE_ELSE), certainty (definite|strong|tentative|speculative),
conditionality (unconditional|if_x|unless_x|prayer_may_prevent|prayer_may_delay|
prayer_may_reduce|multiple_paths|unclear), condition_text, topics[], entities[], locations[],
time_phrase (exactly as said, "" if none), window_start/window_end (ISO, resolved against
uttered_at), time_precision (exact_date|month|season|year|range|relative|none),
severity, magnitude, causes[] (only ones he states), consequences[] (only ones he states),
falsify_match (what observable event would count as this coming true),
falsify_miss (what would count as it failing).
Return {"mentions":[]} if the passage makes no forward-looking claim.
Never infer a cause he did not state. Never resolve a date he did not give."""


def cmd_pack(args, con):
    run = latest_run(con, "type")
    if run is None:
        sys.exit("run `type` first")
    q = """SELECT s.segment_id, s.video_id, s.start_s, s.text, v.uploaded_on, v.title
           FROM segment s JOIN segment_type t ON t.segment_id=s.segment_id AND t.run_id=?
           JOIN video v ON v.video_id=s.video_id
           WHERE t.content_type='content' OR t.has_payload=1
           ORDER BY v.uploaded_on, s.start_s"""
    rows = con.execute(q, (run,)).fetchall()
    if args.limit:
        rows = rows[:args.limit]
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / "extract.jsonl"
    with path.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps({
                "segment_id": r["segment_id"], "video_id": r["video_id"],
                "video_title": r["title"], "uttered_at": r["uploaded_on"],
                "start_s": r["start_s"], "text": r["text"],
                "instructions": PACK_INSTRUCTIONS,
            }, ensure_ascii=False) + "\n")
    print(f"{len(rows)} segments -> {path}")
    print(f"(of {con.execute('SELECT COUNT(*) c FROM segment').fetchone()['c']} total segments)")


# ------------------------------------------------------------------- loading

def cmd_load(args, con):
    data = json.loads(Path(args.file).read_text(encoding="utf-8"))
    mentions = data["mentions"] if isinstance(data, dict) else data
    run_id = new_run(con, "extract", args.tool, args.prompt_version, note=args.file)
    added = 0
    # A falsifier written after the outcome is known is worthless, so it is required at load
    # time or not trusted at all. Say plainly that it is unfalsifiable if it is.
    blank = [m for m in mentions if not (m.get("falsify_match") or "").strip()]
    if blank:
        sys.exit(f"  refused: {len(blank)} mentions carry no falsify_match, first at "
                 f"{blank[0]['video_id']}@{blank[0]['start_s']}. Write one before loading, "
                 f"even if it says the claim is unfalsifiable as stated.")
    # Fifteen words is the corpus-wide verbatim limit. Catching it here rather than in selftest
    # keeps the offending row out of the database entirely, instead of leaving a hand-edit to do
    # after the fact; the trim belongs in the extractor's paraphrase, not in a later UPDATE.
    longq = [m for m in mentions if len((m.get("quote") or "").split()) > 15]
    if longq:
        sys.exit(f"  refused: {len(longq)} quotes run past fifteen words, first at "
                 f"{longq[0]['video_id']}@{longq[0]['start_s']} "
                 f"({len(longq[0]['quote'].split())} words). Shorten the quote, not the claim.")
    for m in mentions:
        vid = m["video_id"]
        start = int(m["start_s"])
        seg = con.execute("SELECT segment_id FROM segment WHERE video_id=? AND start_s<=? "
                          "ORDER BY start_s DESC LIMIT 1", (vid, start)).fetchone()
        vrow = con.execute("SELECT uploaded_on FROM video WHERE video_id=?", (vid,)).fetchone()
        if vrow is None:
            print(f"  skip: video {vid} not ingested")
            continue
        # Keyed on content and extractor, NOT run_id: re-loading the same file is idempotent,
        # while a different tool or prompt version produces a separate row on purpose.
        mid = hashlib.sha256(
            f"{vid}|{start}|{m['claim_text']}|{args.tool}|{args.prompt_version}"
            .encode()).hexdigest()[:16]
        con.execute("DELETE FROM mention_fts WHERE mention_id=?", (mid,))
        con.execute("""INSERT OR REPLACE INTO mention (mention_id,run_id,video_id,segment_id,
            start_s,uttered_at,origin_date,claim_text,quote,content_type,source_mode,certainty,
            conditionality,condition_text,topics,entities,locations,time_phrase,window_start,
            window_end,time_precision,due_at,severity,magnitude,causes,consequences,
            falsify_match,falsify_miss,created_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
            mid, run_id, vid, seg["segment_id"] if seg else None, start,
            vrow["uploaded_on"], m.get("origin_date"), m["claim_text"], m.get("quote"),
            m.get("content_type"), m.get("source_mode"), m.get("certainty"),
            m.get("conditionality"), m.get("condition_text"),
            json.dumps(m.get("topics", [])), json.dumps(m.get("entities", [])),
            json.dumps(m.get("locations", [])), m.get("time_phrase"),
            m.get("window_start"), m.get("window_end"), m.get("time_precision"),
            m.get("due_at") or m.get("window_end"), m.get("severity"), m.get("magnitude"),
            json.dumps(m.get("causes", [])), json.dumps(m.get("consequences", [])),
            m.get("falsify_match"), m.get("falsify_miss"), now()))
        con.execute("INSERT INTO mention_fts (mention_id,claim_text,quote) VALUES (?,?,?)",
                    (mid, m["claim_text"], m.get("quote") or ""))
        added += 1
    con.commit()
    print(f"run {run_id}: loaded {added} mentions from {args.file} (tool={args.tool})")


def cmd_seed(args, con):
    claims = json.loads(Path(args.file).read_text(encoding="utf-8"))
    for c in claims:
        con.execute("INSERT OR REPLACE INTO canonical_claim (claim_id,label,domain,description,"
                    "seeded,created_at) VALUES (?,?,?,?,1,?)",
                    (c["claim_id"], c["label"], c.get("domain"), c.get("description"), now()))
        for a in c.get("aliases", []):
            con.execute("INSERT OR IGNORE INTO claim_alias (claim_id,alias) VALUES (?,?)",
                        (c["claim_id"], a.lower()))
    con.commit()
    print(f"seeded {len(claims)} canonical claims")


# ---------------------------------------------------------------- clustering

def tokens(text):
    return [w for w in re.findall(r"[a-z0-9]+", text.lower())
            if w not in STOPWORDS and len(w) > 2]


def cmd_cluster(args, con):
    """Lexical blocking + assignment. Auto-assigns only what is unambiguous; everything
    else lands as same_event='unsure' for a model or a human to adjudicate."""
    run_id = new_run(con, "cluster", "lexical-v1", note="tf-idf blocking over seeded claims")
    # a merged id keeps resolving for old exports but must never win new mentions
    claims = con.execute("SELECT claim_id,label,description FROM canonical_claim"
                         " WHERE merged_into IS NULL").fetchall()
    aliases = defaultdict(list)
    for r in con.execute("SELECT claim_id, alias FROM claim_alias"):
        aliases[r["claim_id"]].append(r["alias"])

    mentions = con.execute("SELECT mention_id, claim_text, quote, locations, uttered_at, "
                           "time_phrase, severity FROM mention ORDER BY uttered_at, start_s"
                           ).fetchall()
    if not mentions:
        sys.exit("no mentions loaded")

    docs = {c["claim_id"]: tokens(" ".join(filter(None, [c["label"], c["description"]] +
                                                  aliases[c["claim_id"]]))) for c in claims}
    df = Counter()
    for toks in docs.values():
        df.update(set(toks))
    n_docs = max(len(docs), 1)

    def score(mtoks, ctoks):
        mset, cset = Counter(mtoks), set(ctoks)
        if not mset or not cset:
            return 0.0
        s = 0.0
        for w, c in mset.items():
            if w in cset:
                s += (1 + math.log(c)) * math.log(1 + n_docs / (1 + df[w]))
        return s / math.sqrt(len(mset))

    # A re-run must not stack a second live assignment on a mention, and must never
    # overwrite an adjudication a model or a person made. Auto rows it supersedes; the
    # rest it leaves alone.
    live = defaultdict(list)
    for r in con.execute("SELECT assignment_id, mention_id, method FROM assignment "
                         "WHERE superseded_by IS NULL"):
        live[r["mention_id"]].append((r["assignment_id"], r["method"]))

    assigned = Counter()
    kept = 0
    seen_text = {}
    for m in mentions:
        prior_rows = live.get(m["mention_id"], [])
        if any(meth != "lexical" for _, meth in prior_rows):
            kept += 1
            continue
        mtoks = tokens(m["claim_text"])
        best, best_s = None, 0.0
        for cid, ctoks in docs.items():
            s = score(mtoks, ctoks)
            # an alias appearing verbatim is much stronger evidence than tf-idf overlap
            if any(a in m["claim_text"].lower() for a in aliases[cid]):
                s += 2.0
            if s > best_s:
                best, best_s = cid, s
        norm = re.sub(r"[^a-z0-9 ]", "", m["claim_text"].lower())
        if best is None or best_s < args.threshold:
            claim_id, same, delta, method, conf = None, "unsure", "unreviewed", "lexical", best_s
        else:
            prior = con.execute(
                "SELECT COUNT(*) c FROM assignment WHERE claim_id=? AND superseded_by IS NULL",
                (best,)).fetchone()["c"]
            same = "unsure"
            if norm in seen_text:
                delta = "exact_repeat"
            elif prior == 0:
                delta = "first_mention"
            else:
                delta = "unreviewed"
            claim_id, method, conf = best, "lexical", best_s
        seen_text[norm] = m["mention_id"]
        cur = con.execute("""INSERT INTO assignment (mention_id,claim_id,run_id,same_event,
                             confidence,delta_type,method,created_at) VALUES (?,?,?,?,?,?,?,?)""",
                          (m["mention_id"], claim_id, run_id, same, round(conf, 3), delta,
                           method, now()))
        for aid, _ in prior_rows:
            con.execute("UPDATE assignment SET superseded_by=? WHERE assignment_id=?",
                        (cur.lastrowid, aid))
        assigned[claim_id or "(unassigned)"] += 1
    con.commit()
    if kept:
        print(f"  {kept} mentions left untouched: they carry a reviewed assignment")
    print(f"run {run_id}: {len(mentions)} mentions assigned (threshold {args.threshold})")
    for cid, n in assigned.most_common(15):
        print(f"  {cid:<34} {n:>4}")



def cmd_review(args, con):
    """Load adjudications from a model or a human. Never edits an assignment: it writes a new
    one and marks the old superseded, so the earlier judgment stays auditable."""
    items = json.loads(Path(args.file).read_text(encoding="utf-8"))
    items = items["reviews"] if isinstance(items, dict) else items
    run_id = new_run(con, "cluster", args.tool, args.prompt_version, note=args.file)
    done = miss = unchanged = 0
    for it in items:
        mid = it.get("mention_id")
        if not mid:
            # One passage can yield several mentions, so video+start_s is not a key. Taking the
            # newest would quietly adjudicate a different claim than the one written up; an
            # ambiguous row is refused instead, with the ids needed to disambiguate it.
            cands = con.execute("SELECT mention_id, claim_text FROM mention "
                                "WHERE video_id=? AND start_s=? ORDER BY created_at DESC",
                                (it["video_id"], int(it["start_s"]))).fetchall()
            if not cands:
                print(f"  no mention at {it['video_id']}@{it['start_s']}")
                miss += 1
                continue
            if len(cands) > 1:
                want = (it.get("claim_text") or "").strip()[:60]
                cands = [r for r in cands if want and r["claim_text"].startswith(want)] or cands
            if len(cands) > 1:
                print(f"  ambiguous at {it['video_id']}@{it['start_s']}: "
                      f"{len(cands)} mentions share it, name one with mention_id")
                for r in cands:
                    print(f"      {r['mention_id']}  {r['claim_text'][:70]}")
                miss += 1
                continue
            mid = cands[0]["mention_id"]
        if it.get("duplicate_of"):
            # One utterance re-extracted by a second run. Both rows stay, because both are
            # real extractor output, but only one carries the claim: the other would count
            # the same telling twice inside one thread.
            con.execute("UPDATE mention SET duplicate_of=? WHERE mention_id=?",
                        (it["duplicate_of"], mid))
            it = dict(it, claim_id=None, same_event="no", delta_type="duplicate")
        old = con.execute("SELECT assignment_id, claim_id, same_event, delta_type, method "
                          "FROM assignment WHERE mention_id=? AND superseded_by IS NULL",
                          (mid,)).fetchall()
        # Replaying an older review file must not silently revert a newer decision. Identical
        # rows are a no-op; a genuine change is applied but announced, so reversion is visible.
        same = [o for o in old
                if (o["claim_id"] or "") == (it.get("claim_id") or "")
                and o["same_event"] == it.get("same_event", "yes")
                and o["delta_type"] == it["delta_type"]]
        if same and len(same) == len(old):
            unchanged += 1
            continue
        for o in old:
            if o["method"] != "lexical":
                # a row keyed by mention_id need not carry video_id, so this line must not
                # assume it: the announcement is here to make a reversion visible, not to fail
                where = (f"{it['video_id']}@{it['start_s']}" if it.get("video_id") else mid)
                print(f"  CHANGED {where}: "
                      f"{o['claim_id']}/{o['delta_type']} -> "
                      f"{it.get('claim_id')}/{it['delta_type']}")
        cur = con.execute("""INSERT INTO assignment (mention_id,claim_id,run_id,same_event,
                             confidence,delta_type,delta_note,method,created_at)
                             VALUES (?,?,?,?,?,?,?,?,?)""",
                          (mid, it.get("claim_id"), run_id, it.get("same_event", "yes"),
                           it.get("confidence", 1.0), it["delta_type"], it.get("note"),
                           args.tool, now()))
        for o in old:
            con.execute("UPDATE assignment SET superseded_by=? WHERE assignment_id=?",
                        (cur.lastrowid, o["assignment_id"]))
        done += 1
    con.commit()
    print(f"run {run_id}: {done} adjudications applied ({miss} unmatched, "
          f"{unchanged} already current), prior rows superseded")



def cmd_relate(args, con):
    """Load event-graph edges. asserted_by must say whether HE stated the link or we inferred it."""
    rels = json.loads(Path(args.file).read_text(encoding="utf-8"))
    rels = rels["relationships"] if isinstance(rels, dict) else rels
    run_id = new_run(con, "relate", args.tool, note=args.file)
    n = skipped = 0
    for r in rels:
        ev = None
        if r.get("evidence_video") and r.get("evidence_start_s") is not None:
            row = con.execute("SELECT mention_id FROM mention WHERE video_id=? AND start_s=? "
                              "ORDER BY created_at DESC LIMIT 1",
                              (r["evidence_video"], int(r["evidence_start_s"]))).fetchone()
            ev = row["mention_id"] if row else None
        if r["asserted_by"] == "brandon" and ev is None:
            print(f"  refused: {r['from_claim']} -> {r['to_claim']} claims he asserted it "
                  f"but names no mention as evidence")
            continue
        # re-running the same file must not stack duplicate edges
        dupe = con.execute("""SELECT rel_id FROM relationship WHERE from_claim=? AND to_claim=?
                              AND rel_type=? AND asserted_by=?
                              AND COALESCE(evidence_mention,'') = COALESCE(?,'')""",
                           (r["from_claim"], r["to_claim"], r["rel_type"], r["asserted_by"],
                            ev)).fetchone()
        if dupe:
            skipped += 1
            continue
        con.execute("""INSERT INTO relationship (from_claim,to_claim,rel_type,asserted_by,
                       evidence_mention,run_id,note) VALUES (?,?,?,?,?,?,?)""",
                    (r["from_claim"], r["to_claim"], r["rel_type"], r["asserted_by"], ev,
                     run_id, r.get("note")))
        n += 1
    con.commit()
    print(f"run {run_id}: {n} relationships loaded"
          + (f", {skipped} already present" if skipped else ""))


def cmd_merge(args, con):
    """Fold a duplicate canonical claim into the one that keeps the thread.

    Two ids for one event split its history in half, which is the one thing the claim graph
    exists to prevent. The merge moves every live assignment across as a NEW assignment row,
    supersedes the old one, and leaves the losing id in place pointing at the winner, so an
    old export that names the dead id can still be resolved. Nothing is deleted and no
    judgment is rewritten: same_event and delta_type travel unchanged."""
    pairs = json.loads(Path(args.file).read_text(encoding="utf-8"))
    pairs = pairs["merges"] if isinstance(pairs, dict) else pairs
    run_id = new_run(con, "cluster", args.tool, note=f"merge {args.file}")
    moved = folded = 0
    for p in pairs:
        keep, drop, note = p["keep"], p["drop"], p.get("note")
        rows = {r["claim_id"] for r in con.execute(
            "SELECT claim_id FROM canonical_claim WHERE claim_id IN (?,?)", (keep, drop))}
        if {keep, drop} - rows:
            print(f"  skipped {drop} -> {keep}: unknown claim id")
            continue
        if keep == drop:
            continue
        for a in con.execute("SELECT * FROM assignment WHERE claim_id=? AND superseded_by IS NULL",
                             (drop,)).fetchall():
            cur = con.execute("""INSERT INTO assignment (mention_id,claim_id,run_id,same_event,
                                 confidence,delta_type,delta_note,method,created_at)
                                 VALUES (?,?,?,?,?,?,?,?,?)""",
                              (a["mention_id"], keep, run_id, a["same_event"], a["confidence"],
                               a["delta_type"],
                               ((a["delta_note"] + " | ") if a["delta_note"] else "")
                               + f"moved from duplicate claim {drop}",
                               "merge", now()))
            con.execute("UPDATE assignment SET superseded_by=? WHERE assignment_id=?",
                        (cur.lastrowid, a["assignment_id"]))
            moved += 1
        # everything else that names the dead id follows it, minus edges that would self-loop
        # move aliases, tolerating the ones both ids already share
        con.execute("INSERT OR IGNORE INTO claim_alias (claim_id, alias)"
                    " SELECT ?, alias FROM claim_alias WHERE claim_id=?", (keep, drop))
        con.execute("DELETE FROM claim_alias WHERE claim_id=?", (drop,))
        con.execute("DELETE FROM relationship WHERE (from_claim=? AND to_claim=?)"
                    " OR (from_claim=? AND to_claim=?)", (drop, keep, keep, drop))
        con.execute("UPDATE relationship SET from_claim=? WHERE from_claim=?", (keep, drop))
        con.execute("UPDATE relationship SET to_claim=? WHERE to_claim=?", (keep, drop))
        for tbl in ("validation_evidence", "validation_state", "fulfilment_assertion"):
            con.execute(f"UPDATE {tbl} SET claim_id=? WHERE claim_id=?", (keep, drop))
        con.execute("INSERT OR IGNORE INTO claim_alias (claim_id, alias) VALUES (?,?)",
                    (keep, drop.replace("-", " ")))
        con.execute("UPDATE canonical_claim SET merged_into=? WHERE claim_id=?", (keep, drop))
        print(f"  {drop} -> {keep}" + (f"  ({note})" if note else ""))
        folded += 1
    con.commit()
    print(f"run {run_id}: {folded} claims folded, {moved} assignments moved")


def cmd_evidence(args, con):
    """Record what actually happened, and optionally a verdict. Reality lands here and
    nowhere else: no row in this command can touch a mention or a fulfilment assertion."""
    items = json.loads(Path(args.file).read_text(encoding="utf-8"))
    items = items["evidence"] if isinstance(items, dict) else items
    run_id = new_run(con, "validate", args.tool, note=args.file)
    ev = st = 0
    for it in items:
        dupe = con.execute("SELECT ev_id FROM validation_evidence WHERE claim_id=? AND "
                           "COALESCE(source_url,'')=COALESCE(?,'') AND COALESCE(summary,'')=?",
                           (it["claim_id"], it.get("source_url"), it.get("summary", ""))).fetchone()
        if not dupe:
            con.execute("""INSERT INTO validation_evidence (claim_id,observed_on,source_url,
                           summary,added_at,added_by) VALUES (?,?,?,?,?,?)""",
                        (it["claim_id"], it.get("observed_on"), it.get("source_url"),
                         it.get("summary"), now(), args.tool))
            ev += 1
        if it.get("state"):
            con.execute("""INSERT INTO validation_state (claim_id,state,decided_at,rationale,run_id)
                           VALUES (?,?,?,?,?)""",
                        (it["claim_id"], it["state"], now(), it.get("rationale"), run_id))
            st += 1
    con.commit()
    print(f"run {run_id}: {ev} evidence rows, {st} verdicts recorded")


def cmd_validate(args, con):
    """Mechanical state pass. Uses only the claim's own fields and today's date, never an
    outcome, so running it cannot contaminate the record with hindsight."""
    run_id = new_run(con, "validate", "rules-v1", note="mechanical due/falsifiability pass")
    today = date.today().isoformat()
    rows = con.execute("""
        SELECT a.claim_id, MIN(m.due_at) due, MAX(m.falsify_match) fm,
               GROUP_CONCAT(DISTINCT m.conditionality) conds,
               MAX(CASE WHEN m.conditionality = 'unconditional' THEN 1 ELSE 0 END) has_uncond
        FROM assignment a JOIN mention m ON m.mention_id=a.mention_id
        WHERE a.claim_id IS NOT NULL AND a.superseded_by IS NULL AND a.same_event IN ('yes','unsure')
          AND a.delta_type != 'unreviewed'
        GROUP BY a.claim_id""").fetchall()
    # A claim judged against real evidence outranks a rule. Without this guard the mechanical
    # pass relabels a recorded miss as UNFALSIFIABLE, which is the exact laundering the
    # separate-tables design exists to prevent.
    judged = {r["claim_id"] for r in con.execute(
        "SELECT DISTINCT claim_id FROM validation_evidence")}
    counts = Counter()
    held = 0
    for r in rows:
        if r["claim_id"] in judged:
            held += 1
            continue
        conds = (r["conds"] or "").split(",")
        prayer_cond = any(c.startswith("prayer_may") for c in conds)
        unfalsifiable = (r["fm"] or "").lower().startswith("unfalsifiable")
        if unfalsifiable:
            state, why = "UNFALSIFIABLE", "no observable criterion could distinguish outcomes"
        elif prayer_cond and (r["due"] is None or not r["has_uncond"]):
            # A prayer caveat only excuses a claim that had nothing checkable anyway. When a
            # hard date exists and at least one telling was unconditional, the caveat is a
            # footnote, not a get-out: otherwise one hedged retelling launders a dated claim.
            state, why = "UNFALSIFIABLE", "conditional on prayer: a non-event is attributed to intercession"
        elif r["due"] is None:
            state, why = "UNRESOLVED", "no due date given, cannot expire"
        elif r["due"] >= today:
            state, why = "NOT_YET_DUE", f"due {r['due']}"
        else:
            state, why = "UNRESOLVED", f"due {r['due']} has passed, needs external evidence"
        con.execute("INSERT INTO validation_state (claim_id,state,decided_at,rationale,run_id)"
                    " VALUES (?,?,?,?,?)", (r["claim_id"], state, now(), why, run_id))
        counts[state] += 1
    con.commit()
    print(f"run {run_id}: {sum(counts.values())} claims stated (no outcomes consulted)")
    for st, n in counts.most_common():
        print(f"  {st:<22} {n}")
    if held:
        print(f"  {held} claims left alone: already judged against real evidence")


FULFIL_CUE = re.compile(
    r"\b(i (?:told|warned) (?:you|y'?all)|like i (?:said|told you)|i('| ha)ve been (?:telling|saying)"
    r"|remember (?:when|what) i (?:said|told)|just like (?:i|the lord) (?:saw|showed|said)"
    r"|came to pass|come to pass|it happened|it'?s happening (?:now|right now)"
    r"|(?:we'?re|you'?re) seeing (?:it|this) (?:now|today)|that'?s what i saw"
    r"|this is (?:exactly )?what i (?:saw|warned|told)|right on time"
    r"|(?:the word|the prophecy) (?:i gave|came)|what i prophesied|i prophesied)\b", re.I)


def cmd_pick(args, con):
    """Queue passages for a reading pass: content-typed, matching a topic, carrying a forward
    cue, and not already extracted. This is the query the extractor runs before every batch."""
    run = latest_run(con, "type")
    likes = args.like or []
    clause = " OR ".join(["s.text LIKE ?"] * len(likes)) or "1=1"
    params = [run] + [f"%{t}%" for t in likes]
    since, until = args.since or "0000", args.until or "9999"
    rows = con.execute(f"""
        SELECT s.video_id, s.start_s, s.text, v.uploaded_on, v.title
        FROM segment s JOIN segment_type t ON t.segment_id=s.segment_id AND t.run_id=?
        JOIN video v ON v.video_id=s.video_id
        WHERE (t.content_type='content' OR t.has_payload=1)
          AND v.uploaded_on BETWEEN ? AND ?
          AND ({clause})
        ORDER BY v.uploaded_on DESC, s.start_s""",
        [run, since, until] + [f"%{t}%" for t in likes]).fetchall()
    done = {(r["video_id"], r["start_s"]) for r in con.execute(
        "SELECT video_id, start_s FROM mention")}
    # one definition of "forward-looking" for the whole tool: PREDICT, the same regex the
    # typing pass and tier_of use. A second local regex here made tier 4 passages survive
    # a cue filter that was supposed to exclude them.
    hits = [r for r in rows
            if (r["video_id"], r["start_s"]) not in done
            and (args.loose or PREDICT.search(r["text"]))]
    if args.tier:
        hits = [r for r in hits if tier_of(r["text"]) == args.tier]
    if args.focus:
        want = set(args.focus.split(","))
        queue = {r["segment_id"] for r in focus_queue(con)}
        seen = {r[0] for r in con.execute("SELECT DISTINCT segment_id FROM mention "
                                          "WHERE segment_id IS NOT NULL")}
        rows = [r for r in con.execute(f"""
            SELECT s.segment_id, s.video_id, s.start_s, s.text, v.uploaded_on, v.title
            FROM segment s JOIN video v ON v.video_id=s.video_id
            WHERE v.uploaded_on BETWEEN ? AND ? ORDER BY v.uploaded_on DESC, s.start_s""",
            [since, until]) if r["segment_id"] in queue]
        hits = [r for r in rows if r["segment_id"] not in seen
                and want & set(focus_of(r["text"]))]
    print(f"{len(hits)} unextracted passages across {len({h['video_id'] for h in hits})} videos"
          f"  (of {len(rows)} matching"
          + (f", tier {args.tier} only" if args.tier else "")
          + (f", focus {args.focus}" if args.focus else "") + ")")
    for r in hits[:args.limit]:
        tag = f" | {','.join(focus_of(r['text']))}" if args.focus else ""
        print(f"\n--- {r['uploaded_on']} | {r['video_id']} @ {r['start_s']} | {r['title'][:44]}{tag}")
        print("   ", " ".join(r["text"].split())[:args.chars])


# "came to pass" asserts fulfilment. "I told you" is usually just a discourse marker.
STRONG_CUE = re.compile(r"came to pass|come to pass|that'?s what i saw|this is (?:exactly )?what i"
                        r"|i prophesied|what i prophesied|right on time|it'?s happening"
                        r"|seeing (?:it|this) (?:now|today)|just like (?:i|the lord)"
                        r"|i warned", re.I)

# "come to pass" is the one cue in the list that runs three ways. "It came to pass" asserts a
# word landed. "It shall come to pass in the last days" is Joel quoted through Acts, or a
# promise about the future. "It never came to pass" concedes a miss. Only the first is a
# fulfilment assertion, and deciding strength from the cue string alone made all three strong:
# of 114 unlinked "come to pass" rows, 113 were promises, scripture or admitted misses that no
# reader could ever attach to a claim. Tense and negation are read from the surrounding window.
CTP_ASSERTS = re.compile(r"\b(?:came to pass|(?:has|have|had|already)\s+come to pass)\b", re.I)
CTP_NEGATED = re.compile(r"\b(?:not|never|without|no)\b[^.?!]{0,45}\bcome to pass\b"
                         r"|n'?t\b[^.?!]{0,45}\bcome to pass\b", re.I)


def cue_strength(cue, window):
    """Strong means he asserts an earlier word landed; weak means a discourse marker. The
    window is the surrounding text, because tense lives outside the cue string."""
    if not STRONG_CUE.search(cue):
        return "weak"
    if "come to pass" in cue.lower():
        if not CTP_ASSERTS.search(window) or CTP_NEGATED.search(window):
            return "weak"
    return "strong"


def cmd_scan(args, con):
    """Find where he asserts an earlier word has landed. These are candidates only: a cue
    match is not a fulfilment, it is a place a reader must look."""
    run_id = new_run(con, "scan", "rules-v1", note="fulfilment cue scan")
    rows = con.execute("""SELECT s.segment_id, s.video_id, s.start_s, s.text, v.uploaded_on, v.title
                          FROM segment s JOIN video v ON v.video_id=s.video_id""").fetchall()
    found = 0
    # Incremental: a segment that already carries any fulfilment row was scanned before, and
    # its rows may since have been weakened, linked or deduplicated by hand. Deleting and
    # reinserting undid all of that (680 resolved rows came back on 29 Oct 2026).
    scanned = {r[0] for r in con.execute(
        "SELECT DISTINCT segment_id FROM fulfilment_assertion WHERE segment_id IS NOT NULL")}
    for r in rows:
        if r["segment_id"] in scanned:
            continue
        m = FULFIL_CUE.search(r["text"])
        if not m:
            continue
        words = r["text"].split()
        i = max(0, len(" ".join(words[:0])) )
        idx = r["text"].lower().find(m.group(0).lower())
        quote = " ".join(r["text"][max(0, idx - 60): idx + 120].split())[:180]
        strength = cue_strength(m.group(0), quote)
        con.execute("""INSERT INTO fulfilment_assertion (video_id,segment_id,start_s,uttered_at,
                       quote,cue,strength,method,run_id,created_at)
                       VALUES (?,?,?,?,?,?,?,?,?,?)""",
                    (r["video_id"], r["segment_id"], r["start_s"], r["uploaded_on"],
                     quote, m.group(0).lower(), strength, "rules", run_id, now()))
        found += 1
    con.commit()
    strong = con.execute("SELECT COUNT(*) FROM fulfilment_assertion WHERE run_id=? "
                         "AND strength='strong'", (run_id,)).fetchone()[0]
    print(f"run {run_id}: {found} fulfilment-claim candidates across "
          f"{len(set(r['video_id'] for r in rows))} videos "
          f"({strong} strong, {found - strong} weak discourse markers)")
    top = con.execute("""SELECT cue, COUNT(*) n FROM fulfilment_assertion WHERE run_id=?
                         GROUP BY cue ORDER BY n DESC LIMIT 8""", (run_id,)).fetchall()
    for t in top:
        print(f"  {t['n']:>5}  \"{t['cue']}\"")
    print("\nreview them with:  python prophecy.py fulfilled --unreviewed")


def cmd_fulfil(args, con):
    """Attach a fulfilment assertion to the claim it says landed, and to the real-world event
    he points at. Marking one reviewed protects it from being wiped by the next scan."""
    items = json.loads(Path(args.file).read_text(encoding="utf-8"))
    items = items["links"] if isinstance(items, dict) else items
    run_id = new_run(con, "fulfil", args.tool, note=args.file)
    linked = miss = 0
    for it in items:
        # fa_id is exact; video+start_s is kept for hand-written files but is not a key,
        # because one segment can carry several cues.
        if it.get("fa_id"):
            row = con.execute("SELECT fa_id FROM fulfilment_assertion WHERE fa_id=?",
                              (int(it["fa_id"]),)).fetchone()
        else:
            row = con.execute("""SELECT fa_id FROM fulfilment_assertion
                                 WHERE video_id=? AND start_s=? ORDER BY fa_id DESC LIMIT 1""",
                              (it["video_id"], int(it["start_s"]))).fetchone()
        if not row:
            print(f"  no assertion at {it.get('fa_id') or ''}"
                  f"{it.get('video_id','')}@{it.get('start_s','')}")
            miss += 1
            continue
        # A reader may also overturn the strength the rules pass guessed. STRONG_CUE fires on
        # scripture narration and on ordinary discourse ("just like I said" mid-teaching), and
        # those are not assertions that a word landed. Demoting one here is a judgment, stamped
        # with this run, and it supersedes the heuristic rather than hiding it.
        if it.get("strength"):
            con.execute("UPDATE fulfilment_assertion SET strength=? WHERE fa_id=?",
                        (it["strength"], row["fa_id"]))
        con.execute("""UPDATE fulfilment_assertion SET claim_id=?, points_back_to=?,
                       claimed_event_on=?, real_event=?, method=?, run_id=?, reviewed=1
                       WHERE fa_id=?""",
                    (it.get("claim_id"), it.get("points_back_to"), it.get("claimed_event_on"),
                     it.get("real_event"), args.tool, run_id, row["fa_id"]))
        linked += 1
    con.commit()
    print(f"run {run_id}: {linked} fulfilment assertions linked ({miss} unmatched)")
    # Both halves must filter on strength, or demoting a false positive to weak leaves the
    # numerator counting rows the denominator has dropped, and the tally reads over 100%.
    total = con.execute("SELECT COUNT(*) FROM fulfilment_assertion WHERE strength='strong'").fetchone()[0]
    done = con.execute("SELECT COUNT(*) FROM fulfilment_assertion WHERE strength='strong'"
                       " AND claim_id IS NOT NULL").fetchone()[0]
    print(f"  {done} of {total} strong assertions now attached to a claim")


# Tiering the queue. Reading 42,000 passages of speech is not the goal; extracting every
# passage that carries a checkable claim is. Tier 1 is the only tier that can ever be scored.
HAS_DATE = re.compile(r"\b20[2-4]\d\b|\b(?:january|february|march|april|may|june|july|august"
                      r"|september|october|november|december)\b|\bnext (?:year|month|week)\b"
                      r"|\bwithin \w+ (?:days|weeks|months|years)\b|\bby the end of\b", re.I)
HAS_NUM = re.compile(r"\$\s?\d|\b\d[\d,.]*\s*(?:trillion|billion|million|thousand|percent)\b"
                     r"|\bmagnitude\b|\b\d\.\d\b", re.I)
HAS_PLACE = re.compile(r"\b(?:america|china|russia|iran|israel|taiwan|ukraine|canada|europe|japan"
                       r"|gaza|texas|california|new york|missouri|kentucky|tennessee|okinawa"
                       r"|hawaii|cuba|venezuela|britain|germany|poland|turkey|saudi)\b", re.I)


# The focus queue: tier 3 passages (forward cue, no date, number or place) that touch economics,
# politics or health. Tiers 1 and 2 are read in full; inside tier 3 these three subjects are read
# in full too. The patterns avoid the words his ministry uses in another sense: "oil" is anointing,
# "gold" is the streets of heaven, "heal" is prayer, "crash" is as often a plane as a market.
FOCUS = {
    "economics": re.compile(
        r"\b(?:econom\w*|recession|depression|inflation\w*|deflation|dollar\w*|currenc\w*"
        r"|stock market|stocks|wall street|dow jones|the dow|market crash|banks?|banking|bank run"
        r"|federal reserve|the fed|interest rates?|debt|tariff\w*|trade war|gas prices?|food prices?"
        r"|prices? (?:of|go|going|will|rise|skyrocket)\w*|oil prices?|price of (?:oil|gas|gold|silver|food)"
        r"|crude|barrels?|gold and silver|silver and gold|bitcoin|crypto\w*|stablecoin\w*|housing market"
        r"|mortgage\w*|real estate|unemployment|layoffs?|jobs report|shortages?|supply chain\w*"
        r"|food supply|grocer\w*|wealth transfer|bubble|cbdc|digital currency|brics|bankrupt\w*)\b", re.I),
    "politics": re.compile(
        r"\b(?:elections?|midterms?|ballots?|voters?|voting|congress\w*|senat\w*|democrats?|republicans?"
        r"|red wave|blue wave|trump|vance|biden|kamala|harris|newsom|desantis|rubio|mamdani|obama"
        r"|presiden\w*|impeach\w*|supreme court|governors?|white house|administration|legislation"
        r"|executive orders?|deep state|government shutdown|shutdown|prime minister|parliament"
        r"|netanyahu|putin|zelensky|xi jinping|starmer|carney|third term|insurrection|indict\w*)\b", re.I),
    "health": re.compile(
        r"\b(?:virus\w*|pandemic\w*|epidemic\w*|plagues?|vaccin\w*|disease\w*|outbreaks?|cancer"
        r"|hospitals?|illness\w*|sickness|bird flu|h5n1|flu|measles|covid\w*|ebola|marburg|cdc"
        r"|world health|rfk|autism|pharma\w*|health ?care|public health|bioweapon\w*|pathogen\w*"
        r"|lockdowns?|quarantin\w*|mpox|monkeypox|polio|tuberculosis|antibiotic\w*|fda)\b", re.I),
}


def focus_of(text):
    """The focus subjects a passage touches, or an empty list."""
    return [k for k, rx in FOCUS.items() if rx.search(text)]


def focus_queue(con):
    """Every tier 3 focus passage worth one reading: representatives of a near-duplicate group,
    plus passages never grouped. Returns (segment_id, video_id, start_s, text, uploaded_on, title)."""
    run = latest_run(con, "type")
    dup = {r[0] for r in con.execute(
        "SELECT segment_id FROM passage_group WHERE is_representative=0")} \
        if con.execute("SELECT 1 FROM sqlite_master WHERE name='passage_group'").fetchone() else set()
    rows = con.execute("""SELECT s.segment_id, s.video_id, s.start_s, s.text, v.uploaded_on, v.title
                          FROM segment s JOIN segment_type t ON t.segment_id=s.segment_id AND t.run_id=?
                          JOIN video v ON v.video_id=s.video_id
                          WHERE t.content_type='content' OR t.has_payload=1
                          ORDER BY v.uploaded_on DESC, s.start_s""", (run,)).fetchall()
    return [r for r in rows
            if r["segment_id"] not in dup and tier_of(r["text"]) == 3 and focus_of(r["text"])]


def tier_of(text):
    if not PREDICT.search(text):
        return 4
    if HAS_DATE.search(text):
        return 1
    if HAS_NUM.search(text) or HAS_PLACE.search(text):
        return 2
    return 3


def _shingles(text, k=4):
    w = re.findall(r"[a-z']+", text.lower())
    return {hash(" ".join(w[i:i + k])) for i in range(max(0, len(w) - k + 1))}


def cmd_dedupe(args, con):
    """Group near-identical passages. He re-tells the same visitation constantly, so the raw
    queue counts the same content many times. Reading one passage per group is enough; the
    duplicates stay in the corpus and stay searchable."""
    con.executescript("""
      CREATE TABLE IF NOT EXISTS passage_group (
        segment_id TEXT PRIMARY KEY REFERENCES segment(segment_id),
        group_id TEXT NOT NULL,
        is_representative INTEGER NOT NULL,
        run_id INTEGER REFERENCES run(run_id));
      CREATE INDEX IF NOT EXISTS ix_pg_group ON passage_group(group_id);""")
    run_id = new_run(con, "dedupe", "minhash-v1", note=f"threshold {args.threshold}")
    type_run = latest_run(con, "type")
    rows = con.execute("""SELECT s.segment_id, s.text, s.word_count, v.uploaded_on
                          FROM segment s JOIN segment_type t ON t.segment_id=s.segment_id
                             AND t.run_id=? JOIN video v ON v.video_id=s.video_id
                          WHERE (t.content_type='content' OR t.has_payload=1)
                          ORDER BY v.uploaded_on, s.segment_id""", (type_run,)).fetchall()
    print(f"hashing {len(rows):,} queued passages ...")

    K, BANDS = 16, 4
    seeds = [0x9E3779B1 * (i + 1) & 0xFFFFFFFF for i in range(K)]
    sigs, shing = {}, {}
    for r in rows:
        sh = _shingles(r["text"])
        if len(sh) < 8:
            continue
        shing[r["segment_id"]] = sh
        sigs[r["segment_id"]] = tuple(min((h ^ s) & 0xFFFFFFFF for h in sh) for s in seeds)

    buckets = defaultdict(list)
    per = K // BANDS
    for sid, sig in sigs.items():
        for b in range(BANDS):
            buckets[(b, sig[b * per:(b + 1) * per])].append(sid)

    parent = {sid: sid for sid in sigs}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    pairs = 0
    for members in buckets.values():
        if len(members) < 2 or len(members) > 60:      # a huge bucket is noise, not a match
            continue
        base = members[0]
        for other in members[1:]:
            a, b = shing[base], shing[other]
            j = len(a & b) / max(len(a | b), 1)
            if j >= args.threshold:
                ra, rb = find(base), find(other)
                if ra != rb:
                    parent[rb] = ra
                    pairs += 1

    groups = defaultdict(list)
    for sid in sigs:
        groups[find(sid)].append(sid)
    order = {r["segment_id"]: i for i, r in enumerate(rows)}
    con.execute("DELETE FROM passage_group")
    dupes = 0
    for gid, members in groups.items():
        members.sort(key=lambda s: order[s])           # earliest telling is the representative
        for i, sid in enumerate(members):
            con.execute("""INSERT OR REPLACE INTO passage_group
                           (segment_id, group_id, is_representative, run_id)
                           VALUES (?,?,?,?)""", (sid, gid, 1 if i == 0 else 0, run_id))
        dupes += len(members) - 1
    con.commit()
    uniq = len(groups)
    print(f"run {run_id}: {len(sigs):,} passages -> {uniq:,} unique groups "
          f"({dupes:,} near-duplicates, {dupes * 100 // max(len(sigs), 1)}% of the queue)")
    big = sorted(groups.values(), key=len, reverse=True)[:3]
    for members in big:
        if len(members) > 1:
            print(f"  a group of {len(members)} retellings, first at {members[0]}")


def cmd_autolink(args, con):
    """Attach fulfilment assertions to claims by alias match, at scale. Only confident hits
    are attached, they are stamped method='lexical' so they never pass for an adjudicated
    link, and reviewed stays 0 so `todo` keeps counting them."""
    run_id = new_run(con, "fulfil", "lexical-v1", note="alias autolink over fulfilment assertions")
    aliases = defaultdict(list)
    for r in con.execute("SELECT claim_id, alias FROM claim_alias"):
        if len(r["alias"]) >= 5:            # short aliases match everything
            aliases[r["claim_id"]].append(r["alias"].lower())
    labels = {r["claim_id"]: r["label"].lower()
              for r in con.execute("SELECT claim_id, label FROM canonical_claim"
                                   " WHERE merged_into IS NULL")}

    # match on the whole passage, not the cue window: the topic words usually sit either side
    sql = ("SELECT f.fa_id, COALESCE(s.text, f.quote) AS quote FROM fulfilment_assertion f "
           "LEFT JOIN segment s ON s.segment_id = f.segment_id "
           "WHERE f.claim_id IS NULL AND f.reviewed=0")
    rows = (con.execute(sql).fetchall() if args.all
            else con.execute(sql + " AND f.strength=?", ("strong",)).fetchall())
    linked = ambiguous = 0
    per_claim = Counter()
    for r in rows:
        low = " " + re.sub(r"[^a-z0-9 ]", " ", (r["quote"] or "").lower()) + " "
        low = re.sub(r"\s+", " ", low)
        hits = []
        for cid, als in aliases.items():
            score = sum(2 for a in als if f" {a} " in low)
            if len(labels[cid]) > 8 and f" {labels[cid]} " in low:
                score += 3
            if score:
                hits.append((score, cid))
        hits.sort(reverse=True)
        # one clear winner only: a tie means the quote is generic, so leave it for a reader
        if hits and hits[0][0] >= args.min_score and (len(hits) == 1 or hits[0][0] > hits[1][0]):
            con.execute("""UPDATE fulfilment_assertion SET claim_id=?, method='lexical',
                           run_id=? WHERE fa_id=?""", (hits[0][1], run_id, r["fa_id"]))
            per_claim[hits[0][1]] += 1
            linked += 1
        elif hits:
            ambiguous += 1
    con.commit()
    print(f"run {run_id}: {linked} assertions auto-linked, {ambiguous} ambiguous, "
          f"{len(rows) - linked - ambiguous} no match")
    for cid, n in per_claim.most_common(10):
        print(f"  {cid:<30} {n}")
    print("  (all stamped method=lexical and left unreviewed: they are candidates, not judgments)")


def cmd_fulfilled(args, con):
    """What he says has already come true, kept strictly apart from what we verified."""
    clauses, params = [], []
    if args.unreviewed:
        clauses.append("f.reviewed=0")
    if args.claim_id:
        clauses.append("f.claim_id=?"); params.append(args.claim_id)
    if args.strong:
        clauses.append("f.strength='strong'")
    where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
    params = tuple(params)
    rows = con.execute(f"""SELECT f.*, v.title FROM fulfilment_assertion f
                           JOIN video v ON v.video_id=f.video_id {where}
                           ORDER BY f.uttered_at DESC, f.start_s""", params).fetchall()
    print(f"\n{len(rows)} fulfilment assertions"
          + (" awaiting review" if args.unreviewed else ""))
    print("(these are HIS claims that a word landed, not our verification)\n")
    for r in rows[:args.limit]:
        state = ""
        if r["claim_id"]:
            st = con.execute("SELECT state FROM validation_state WHERE claim_id=? "
                             "ORDER BY state_id DESC LIMIT 1", (r["claim_id"],)).fetchone()
            state = f" | our state: {st['state']}" if st else " | our state: none"
        print(f"  {r['uttered_at'] or '????-??-??'}  {fmt_ts(r['start_s']):>7}  "
              f"[{r['strength']}] cue=\"{r['cue']}\"{state}")
        print(f"      claim: {r['claim_id'] or '(unassigned)'}   "
              f"event date he gives: {r['claimed_event_on'] or '(none)'}")
        print(f"      {r['quote'][:150]}")
        print(f"      https://youtu.be/{r['video_id']}?t={r['start_s']}")
    if len(rows) > args.limit:
        print(f"\n  ... {len(rows) - args.limit} more (raise --limit)")



def cmd_todo(args, con):
    """What still needs judgment, and how far the corpus is from fully read. Unreviewed
    lexical guesses are excluded from validation, so this is where they must not hide."""
    rows = con.execute("""
        SELECT a.claim_id, a.method, a.same_event, a.delta_type,
               m.video_id, m.start_s, m.uttered_at, substr(m.claim_text,1,88) t
        FROM assignment a JOIN mention m ON m.mention_id=a.mention_id
        WHERE a.superseded_by IS NULL
          AND (a.delta_type='unreviewed' OR a.same_event='unsure')
        ORDER BY m.uttered_at DESC""").fetchall()
    # An extractor that says 'unsure' has done its job; hiding that behind a method filter
    # would let a deliberate flag sit unanswered forever, which is the one thing this
    # command exists to prevent.
    # 'unsure' plus contradiction or branch is the terminal state the design asks for, not a
    # backlog: two tellings that disagree are meant to stay side by side. Everything else
    # marked unsure is someone saying they could not tell, which is work.
    parked = [r for r in rows if r["same_event"] == "unsure"
              and r["delta_type"] in ("contradiction", "branch")]
    rows = [r for r in rows if r not in parked]
    lex = sum(1 for r in rows if r["method"] == "lexical")
    print(f"{len(rows)} assignments awaiting judgment "
          f"({lex} lexical guesses, {len(rows) - lex} flagged unsure by an extractor); "
          f"{len(parked)} parked as an unresolved contradiction or branch, which is deliberate\n")
    for r in rows[:args.limit]:
        print(f"  {r['uttered_at']}  {r['video_id']}@{r['start_s']:<6} -> "
              f"{r['claim_id'] or '(unassigned)'}   [{r['method']}/{r['delta_type']}]")
        print(f"      {r['t']}...")
    unlinked = con.execute("SELECT COUNT(*) FROM fulfilment_assertion WHERE strength='strong' "
                           "AND claim_id IS NULL").fetchone()[0]
    total = con.execute("SELECT COUNT(*) FROM segment_type WHERE run_id=(SELECT MAX(run_id) "
                        "FROM run WHERE kind='type') AND (content_type='content' OR has_payload=1)"
                        ).fetchone()[0]
    got = con.execute("SELECT COUNT(DISTINCT segment_id) FROM mention "
                      "WHERE segment_id IS NOT NULL").fetchone()[0]
    due = con.execute("""SELECT COUNT(*) FROM (
        SELECT a.claim_id FROM assignment a JOIN mention m ON m.mention_id=a.mention_id
        WHERE a.superseded_by IS NULL AND a.delta_type!='unreviewed' AND m.due_at IS NOT NULL
          AND a.claim_id IS NOT NULL
        GROUP BY a.claim_id
        HAVING MIN(m.due_at) < date('now')
           AND (SELECT COUNT(*) FROM validation_evidence e WHERE e.claim_id=a.claim_id)=0)"""
        ).fetchone()[0]
    type_run = latest_run(con, "type")
    rows2 = con.execute("""SELECT s.segment_id, s.text FROM segment s
                           JOIN segment_type t ON t.segment_id=s.segment_id AND t.run_id=?
                           WHERE t.content_type='content' OR t.has_payload=1""",
                        (type_run,)).fetchall()
    seen = {r[0] for r in con.execute("SELECT DISTINCT segment_id FROM mention "
                                      "WHERE segment_id IS NOT NULL")}
    tiers = defaultdict(lambda: [0, 0])
    for r in rows2:
        t = tier_of(r["text"])
        tiers[t][0] += 1
        if r["segment_id"] in seen:
            tiers[t][1] += 1
    names = {1: "dated claims (scoreable)", 2: "claim with a number or place",
             3: "claim with neither", 4: "no forward cue at all"}
    print("\n  extraction coverage by tier")
    for t in sorted(tiers):
        n, d = tiers[t]
        print(f"    tier {t}  {names[t]:<30} {d:>4} of {n:>6,} read  ({d * 100 / max(n, 1):.1f}%)")
    fq = focus_queue(con)
    by = defaultdict(lambda: [0, 0])
    for r in fq:
        for k in focus_of(r["text"]):
            by[k][0] += 1
            by[k][1] += r["segment_id"] in seen
    fread = sum(r["segment_id"] in seen for r in fq)
    print(f"    focus   tier 3 econ/politics/health    {fread:>4} of {len(fq):>6,} read"
          f"  ({fread * 100 / max(len(fq), 1):.1f}%)  "
          + ", ".join(f"{k} {d}/{n}" for k, (n, d) in sorted(by.items())))
    print(f"\n  strong fulfilment assertions not yet linked  : {unlinked:,}")
    print(f"  past-due claims with no evidence recorded    : {due}")


def cmd_search(args, con):
    """Full-text over the raw corpus. Answers 'everything he has ever said about X' before
    any extraction has run, which is also how you find what still needs extracting."""
    run = latest_run(con, "type")
    rows = con.execute(f"""
        SELECT s.segment_id, s.video_id, s.start_s, v.title, v.uploaded_on,
               t.content_type, t.has_payload,
               snippet(segment_fts, 1, '>>', '<<', ' ... ', 14) AS snip,
               EXISTS(SELECT 1 FROM mention m WHERE m.segment_id=s.segment_id) AS extracted
        FROM segment_fts f
        JOIN segment s ON s.segment_id = f.segment_id
        JOIN video v ON v.video_id = s.video_id
        LEFT JOIN segment_type t ON t.segment_id = s.segment_id AND t.run_id = ?
        WHERE segment_fts MATCH ?
        ORDER BY v.uploaded_on, s.start_s""", (run, args.query)).fetchall()
    if args.type:
        rows = [r for r in rows if r["content_type"] == args.type]
    vids = {r["video_id"] for r in rows}
    dates = sorted(r["uploaded_on"] for r in rows if r["uploaded_on"])
    print(f"\n\"{args.query}\": {len(rows)} passages across {len(vids)} videos"
          + (f", {dates[0]} to {dates[-1]}" if dates else ""))
    print(f"{sum(1 for r in rows if r['extracted'])} already have an extracted mention\n")
    for r in rows[:args.limit]:
        mark = "*" if r["extracted"] else " "
        kind = (r["content_type"] or "?")[:10]
        print(f" {mark} {r['uploaded_on'] or '????-??-??'}  {fmt_ts(r['start_s']):>7}  {kind:<10}"
              f" {r['title'][:44]}")
        print(f"     {r['snip'][:150]}")
        print(f"     https://youtu.be/{r['video_id']}?t={r['start_s']}")
    if len(rows) > args.limit:
        print(f"\n  ... {len(rows) - args.limit} more (raise --limit)")


def cmd_graph(args, con):
    rows = con.execute("""SELECT r.*, c1.label l1, c2.label l2 FROM relationship r
                          JOIN canonical_claim c1 ON c1.claim_id=r.from_claim
                          JOIN canonical_claim c2 ON c2.claim_id=r.to_claim
                          ORDER BY r.asserted_by, r.from_claim""").fetchall()
    print(f"\n{len(rows)} edges\n")
    for r in rows:
        tag = "HE STATES" if r["asserted_by"] == "brandon" else "we infer "
        print(f"  [{tag}] {r['l1']}")
        print(f"      --{r['rel_type']}-->  {r['l2']}")
        if r["note"]:
            print(f"      {r['note']}")


# -------------------------------------------------------------------- views

def fmt_ts(s):
    return f"{int(s)//60}:{int(s)%60:02d}"


def cmd_thread(args, con):
    c = con.execute("SELECT * FROM canonical_claim WHERE claim_id=?", (args.claim_id,)).fetchone()
    if not c:
        sys.exit(f"no such claim: {args.claim_id}")
    if c["merged_into"]:
        print(f"  {args.claim_id} was folded into {c['merged_into']}; showing that thread")
        args.claim_id = c["merged_into"]
        c = con.execute("SELECT * FROM canonical_claim WHERE claim_id=?",
                        (args.claim_id,)).fetchone()
    rows = con.execute("""
        SELECT m.*, a.delta_type, a.same_event, a.confidence, v.title, v.uploaded_on
        FROM assignment a JOIN mention m ON m.mention_id=a.mention_id
        JOIN video v ON v.video_id=m.video_id
        WHERE a.claim_id=? AND a.superseded_by IS NULL
        ORDER BY v.uploaded_on, m.start_s""", (args.claim_id,)).fetchall()
    print(f"\n{c['label'].upper()}   [{c['claim_id']}]   domain={c['domain']}")
    print(f"{c['description'] or ''}\n")
    if not rows:
        print("  no mentions assigned yet")
        return
    print(f"first mentioned : {rows[0]['uploaded_on']}  {rows[0]['title'][:50]}  {fmt_ts(rows[0]['start_s'])}")
    print(f"mentions        : {len(rows)} across {len({r['video_id'] for r in rows})} videos\n")
    print("EVOLUTION")
    for r in rows:
        when = r["time_phrase"] or "(no time given)"
        print(f"  {r['uploaded_on']}  {fmt_ts(r['start_s']):>6}  [{r['delta_type']}]")
        print(f"      {r['claim_text']}")
        print(f"      when={when} | mode={r['source_mode']} | cond={r['conditionality']}"
              f" | certainty={r['certainty']}")
        if r["quote"]:
            print(f"      \"{r['quote']}\"")
        print(f"      https://youtu.be/{r['video_id']}?t={r['start_s']}")
    fa = con.execute("SELECT COUNT(*) n FROM fulfilment_assertion WHERE claim_id=?",
                     (args.claim_id,)).fetchone()["n"]
    if fa:
        print(f"\nHE CLAIMS FULFILLED : {fa} assertions "
              f"(python prophecy.py fulfilled --claim-id {args.claim_id})")

    evs = con.execute("SELECT observed_on, summary, source_url FROM validation_evidence "
                      "WHERE claim_id=? ORDER BY observed_on", (args.claim_id,)).fetchall()
    if evs:
        print("\nWHAT ACTUALLY HAPPENED (its own table; nothing here edits his words)")
        for e in evs:
            print(f"  {e['observed_on'] or '????-??-??'}  {(e['summary'] or '')[:140]}")
            print(f"      {e['source_url']}")

    states = con.execute("SELECT state, decided_at, rationale FROM validation_state "
                         "WHERE claim_id=? ORDER BY state_id DESC LIMIT 1",
                         (args.claim_id,)).fetchone()
    print(f"\nOUR VERDICT     : {states['state'] if states else 'UNRESOLVED (no state recorded)'}")
    if states and states["rationale"]:
        import textwrap
        for line in textwrap.wrap(states["rationale"], 90):
            print(f"  {line}")


def cmd_timeline(args, con):
    where, params = "", []
    if args.year:
        where = "AND (m.window_start LIKE ? OR m.window_end LIKE ? OR m.time_phrase LIKE ?)"
        params = [f"{args.year}%", f"{args.year}%", f"%{args.year}%"]
    rows = con.execute(f"""
        SELECT m.*, v.uploaded_on, v.title, a.claim_id
        FROM mention m JOIN video v ON v.video_id=m.video_id
        LEFT JOIN assignment a ON a.mention_id=m.mention_id AND a.superseded_by IS NULL
        WHERE (m.time_precision IS NOT NULL AND m.time_precision!='none') {where}
        ORDER BY COALESCE(m.window_start,'9999'), v.uploaded_on""", params).fetchall()
    print(f"\n{len(rows)} dated claims" + (f" mentioning {args.year}" if args.year else ""))
    for r in rows:
        topics = ", ".join(json.loads(r["topics"] or "[]")[:3])
        print(f"\n  {r['window_start'] or r['time_phrase']:<24} {topics}")
        print(f"    {r['claim_text']}")
        print(f"    said {r['uploaded_on']} · https://youtu.be/{r['video_id']}?t={r['start_s']}"
              f" · cond={r['conditionality']}")


def cmd_stats(args, con):
    q = lambda s: con.execute(s).fetchone()[0]
    print(f"videos            {q('SELECT COUNT(*) FROM video')}")
    print(f"  dated           {q('SELECT COUNT(*) FROM video WHERE uploaded_on IS NOT NULL')}")
    print(f"segments          {q('SELECT COUNT(*) FROM segment')}")
    print(f"  words           {q('SELECT COALESCE(SUM(word_count),0) FROM segment'):,}")
    run = latest_run(con, "type")
    if run:
        print(f"segment types (run {run})")
        for r in con.execute("SELECT content_type, COUNT(*) n, SUM(has_payload) p FROM segment_type"
                             " WHERE run_id=? GROUP BY content_type ORDER BY n DESC", (run,)):
            print(f"  {r['content_type']:<12} {r['n']:>6}   payload={r['p']}")
    print(f"mentions          {q('SELECT COUNT(*) FROM mention')}")
    print(f"canonical claims  {q('SELECT COUNT(*) FROM canonical_claim WHERE merged_into IS NULL')}"
          f"   (+{q('SELECT COUNT(*) FROM canonical_claim WHERE merged_into IS NOT NULL')} folded"
          " as duplicates)")
    print(f"assignments       {q('SELECT COUNT(*) FROM assignment WHERE superseded_by IS NULL')}")
    print(f"  unassigned      {q('SELECT COUNT(*) FROM assignment WHERE claim_id IS NULL AND superseded_by IS NULL')}")
    need = con.execute("SELECT COUNT(*) FROM assignment WHERE same_event='unsure'"
                       " AND superseded_by IS NULL").fetchone()[0]
    print(f"  needing review  {need}")
    print(f"relationships     {q('SELECT COUNT(*) FROM relationship')}")
    print(f"validation rows   {q('SELECT COUNT(*) FROM validation_evidence')}")


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", default=DB_DEFAULT)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init")
    p = sub.add_parser("ingest"); p.add_argument("indir")
    sub.add_parser("dates")
    sub.add_parser("type")
    p = sub.add_parser("pack"); p.add_argument("-o", "--outdir", default="packs"); p.add_argument("--limit", type=int)
    p = sub.add_parser("load"); p.add_argument("file"); p.add_argument("--tool", default="manual"); p.add_argument("--prompt-version", default="v1")
    p = sub.add_parser("seed"); p.add_argument("file")
    p = sub.add_parser("cluster"); p.add_argument("--threshold", type=float, default=1.2)
    p = sub.add_parser("review"); p.add_argument("file"); p.add_argument("--tool", default="claude-opus-5"); p.add_argument("--prompt-version", default="v1")
    p = sub.add_parser("relate"); p.add_argument("file"); p.add_argument("--tool", default="claude-opus-5")
    p = sub.add_parser("merge"); p.add_argument("file"); p.add_argument("--tool", default="claude-opus-5")
    sub.add_parser("validate")
    p = sub.add_parser("search"); p.add_argument("query"); p.add_argument("--limit", type=int, default=15); p.add_argument("--type")
    p = sub.add_parser("evidence"); p.add_argument("file"); p.add_argument("--tool", default="claude-opus-5+web")
    p = sub.add_parser("pick"); p.add_argument("--like", action="append"); p.add_argument("--since"); p.add_argument("--until"); p.add_argument("--limit", type=int, default=15); p.add_argument("--chars", type=int, default=380); p.add_argument("--loose", action="store_true"); p.add_argument("--tier", type=int); p.add_argument("--focus", help="economics,politics,health: the tier 3 focus queue")
    p = sub.add_parser("fulfil"); p.add_argument("file"); p.add_argument("--tool", default="claude-opus-5")
    p = sub.add_parser("autolink"); p.add_argument("--min-score", type=int, default=4); p.add_argument("--all", action="store_true")
    p = sub.add_parser("dedupe"); p.add_argument("--threshold", type=float, default=0.55)
    p = sub.add_parser("todo"); p.add_argument("--limit", type=int, default=12)
    sub.add_parser("scan")
    p = sub.add_parser("fulfilled"); p.add_argument("--unreviewed", action="store_true"); p.add_argument("--claim-id"); p.add_argument("--strong", action="store_true"); p.add_argument("--limit", type=int, default=20)
    sub.add_parser("graph")
    p = sub.add_parser("thread"); p.add_argument("claim_id")
    p = sub.add_parser("timeline"); p.add_argument("--year")
    sub.add_parser("stats")

    args = ap.parse_args()
    con = connect(args.db)
    if args.cmd == "init":
        con.executescript(SCHEMA)
        con.commit()
        print(f"schema ready in {args.db}")
        return
    con.executescript(SCHEMA)   # idempotent, keeps an existing db in step
    migrate(con)
    {"ingest": cmd_ingest, "dates": cmd_dates, "type": cmd_type, "pack": cmd_pack,
     "load": cmd_load, "seed": cmd_seed, "cluster": cmd_cluster, "review": cmd_review,
     "merge": cmd_merge,
     "relate": cmd_relate, "validate": cmd_validate, "graph": cmd_graph, "thread": cmd_thread,
     "search": cmd_search, "scan": cmd_scan, "todo": cmd_todo, "fulfilled": cmd_fulfilled, "fulfil": cmd_fulfil,
     "autolink": cmd_autolink, "dedupe": cmd_dedupe,
     "evidence": cmd_evidence, "pick": cmd_pick,
     "timeline": cmd_timeline, "stats": cmd_stats}[args.cmd](args, con)


if __name__ == "__main__":
    main()

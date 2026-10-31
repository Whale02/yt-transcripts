#!/usr/bin/env python3
"""Turn raw transcripts into a searchable, auditable claim table.

  python classify.py lastdays/                  # writes claims.tsv, timeline.tsv, report.md
  python classify.py lastdays/ --now 2026       # what counts as a future date

Pipeline: strip non-speech and filler, cut into passages, tag each passage with
topic categories, pull out date expressions (marked past / future / relative),
places and quantities, and say whether the passage predicts an event.

This is a keyword pass. It is a fast, free index over a lot of audio, not a
reader. The `terms` column shows exactly which words fired, so a wrong tag is
visible and fixable in the tables below rather than mysterious.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------- categories
# A term with a space is a phrase and scores 3. A single word scores 1.
# A category needs 2 points to be applied, so one ambiguous word is never enough.

CATEGORIES = {
    "economy_markets": [
        "economy", "economic", "recession", "depression", "stock market", "stocks",
        "wall street", "market crash", "financial crash", "financial collapse",
        "inflation", "hyperinflation", "deflation", "prices", "price of",
        "unemployment", "layoffs", "jobs", "wages", "housing market", "real estate",
        "mortgage", "rent", "gold", "silver", "oil", "gas prices", "gasoline",
        "investment", "investors", "retirement", "401k", "pension", "savings",
        "debt", "loans", "interest rates", "businesses", "bankrupt", "bankruptcy",
        "trade war", "tariffs", "supply chain", "great depression",
    ],
    "money_system": [
        "dollar", "dollars", "currency", "cash", "banking", "banks", "the bank",
        "federal reserve", "treasury", "digital currency", "digital dollar", "cbdc",
        "crypto", "bitcoin", "cashless", "mark of the beast", "buying and selling",
        "atm", "bank account", "bank accounts", "bank holiday", "banks close",
        "devalue", "devaluation", "worthless", "petrodollar", "financial reset",
        "new currency", "new financial system", "digital platform",
    ],
    "politics_government": [
        "president", "presidential", "election", "elections", "vote", "voting",
        "government", "congress", "senate", "legislation", "administration",
        "white house", "supreme court", "governor", "martial law", "executive order",
        "impeach", "assassination", "assassinate", "regime", "coup", "constitution",
        "our rights", "freedom of speech", "politician", "politicians",
    ],
    "war_conflict": [
        "war", "world war", "world war three", "military", "army", "soldiers",
        "troops", "invasion", "invade", "bombs", "bombing", "missile", "missiles",
        "nuclear", "nuke", "weapons", "airstrike", "warships", "navy", "submarine",
        "emp", "terrorist", "terrorism", "boots on the ground", "enemy",
    ],
    "health_disease": [
        "plague", "pandemic", "virus", "viral", "disease", "outbreak", "infection",
        "infected", "hospital", "hospitals", "doctors", "medicine", "medical",
        "vaccine", "vaccines", "quarantine", "lockdown", "death toll", "cancer",
        "the flu", "bird flu", "covid", "ebola", "antibiotics", "sickness",
    ],
    "disaster_natural": [
        "earthquake", "earthquakes", "tsunami", "tidal wave", "volcano", "eruption",
        "hurricane", "tornado", "tornadoes", "flood", "flooding", "wildfire",
        "drought", "famine", "heat wave", "blizzard", "sinkhole", "landslide",
        "asteroid", "meteor", "solar flare", "fault line", "new madrid",
        "san andreas", "cascadia", "yellowstone", "natural disaster",
    ],
    "infrastructure_utilities": [
        "power grid", "the grid", "electricity", "blackout", "power outage",
        "transformer", "substation", "water supply", "pipeline", "internet goes",
        "cell phones", "communication", "satellites", "trucking", "truckers",
        "railroad", "airports", "highways", "refinery", "fuel supply",
    ],
    "food_water_supply": [
        "food", "groceries", "grocery store", "grocery stores", "empty shelves",
        "shortage", "shortages", "hunger", "starve", "starvation", "crops",
        "harvest fails", "farmers", "farming", "livestock", "wheat", "corn",
        "seeds", "clean water", "drinking water", "canned", "pantry", "stockpile",
        "food supply", "store food",
    ],
    "civil_unrest_crime": [
        "riots", "rioting", "looting", "looters", "violence", "crime", "gangs",
        "murder", "shooting", "protests", "unrest", "chaos", "anarchy", "curfew",
        "camps", "roundup", "arrested", "persecution", "refugees", "martial",
    ],
    "technology_surveillance": [
        "artificial intelligence", "robots", "computers", "the chip", "implant",
        "surveillance", "cameras", "tracking", "digital id", "biometric",
        "facial recognition", "the network", "drones", "your phone", "technology",
    ],
    "spiritual_church": [
        "god", "jesus", "the lord", "holy spirit", "christ", "church", "churches",
        "pastor", "pastors", "revival", "pray", "prayer", "repent", "repentance",
        "sin", "judgment", "tribulation", "rapture", "antichrist", "the beast",
        "angel", "angels", "heaven", "hell", "prophecy", "prophet", "vision",
        "dream", "scripture", "bible", "faith", "believers", "salvation", "souls",
    ],
    "preparedness_instruction": [
        "prepare", "be prepared", "get ready", "stock up", "store up", "buy now",
        "get out of debt", "debt free", "pay off", "warn people", "tell people",
        "supplies", "generator", "plant a garden", "protect your family",
        "have on hand", "do not wait", "get out of the city",
    ],
}

FALLBACK = "trend_other"

# These saturate religious speech, so they must not outrank a domain topic.
WEIGHT = {"spiritual_church": 0.25, "preparedness_instruction": 0.6}

PHRASES = {c: [t for t in terms if " " in t] for c, terms in CATEGORIES.items()}
WORDS = {c: [t for t in terms if " " not in t] for c, terms in CATEGORIES.items()}

# ------------------------------------------------------------------- signals

PREDICT_CUE = re.compile(
    r"\b(i saw|i see|the lord (?:showed|told|said|spoke)|he showed me|god (?:showed|told|said)"
    r"|is coming|are coming|will (?:be|come|happen|see|go|have|hit|fall|rise|crash|close)"
    r"|going to (?:be|come|happen|see|go|have|hit|fall|rise|crash|close)"
    r"|there will|it will|they will|you will|shall be|in the vision|in the dream)\b", re.I)

MONTHS = ("january february march april may june july august september october "
          "november december").split()
MONTH_RE = "|".join(MONTHS)

YEAR = re.compile(r"\b(?:19|20)\d{2}\b")
# "may", "march" and "fall" are also ordinary words, so a month counts only with
# a day number, a year, or a preposition in front of it.
MONTH_DATE = re.compile(
    r"\b(?:(?:in|by|on|of|during|until|before|after|around|since)\s+)?(?:" + MONTH_RE + r")"
    r"(?:\s+(?:the\s+)?\d{1,2}(?:st|nd|rd|th)?)?(?:[, ]+((?:19|20)\d{2}))?\b", re.I)
RELATIVE = re.compile(
    r"\b(?:(?:within|in|after|over)\s+(?:the\s+next\s+)?"
    r"(?:a|one|two|three|four|five|six|seven|eight|nine|ten|\d+)\s+"
    r"(?:day|days|week|weeks|month|months|year|years|decade|decades)"
    r"|next\s+(?:year|month|week|spring|summer|fall|winter)"
    r"|(?:by|before)\s+the\s+end\s+of\s+(?:this|next)\s+year"
    r"|(?:spring|summer|fall|winter)\s+of\s+(?:19|20)\d{2})\b", re.I)
SEASONAL = re.compile(
    r"\b(?:passover|rosh hashanah|yom kippur|feast of trumpets|hanukkah|christmas|"
    r"easter|election day|midterms?|inauguration)\b", re.I)

QUANTITY = re.compile(
    r"(\$\s?\d[\d,.]*(?:\s*(?:trillion|billion|million|thousand))?"
    r"|\b\d[\d,.]*\s*(?:trillion|billion|million|thousand)\b"
    r"|\b\d{1,3}(?:\.\d+)?\s*(?:percent|%)"
    r"|\b\d{1,3}\s*cents?\b)", re.I)

PLACES = sorted({
    "america", "united states", "china", "russia", "iran", "israel", "ukraine",
    "north korea", "south korea", "taiwan", "japan", "india", "pakistan",
    "afghanistan", "iraq", "syria", "lebanon", "turkey", "egypt", "saudi arabia",
    "yemen", "venezuela", "mexico", "canada", "brazil", "europe", "england",
    "britain", "france", "germany", "italy", "spain", "africa", "nigeria",
    "australia", "middle east", "jerusalem", "tel aviv", "moscow", "beijing",
    "tehran", "washington", "new york", "california", "texas", "florida", "ohio",
    "kentucky", "tennessee", "missouri", "arkansas", "oklahoma", "kansas",
    "nebraska", "iowa", "michigan", "illinois", "chicago", "los angeles",
    "san francisco", "seattle", "houston", "dallas", "atlanta", "miami", "boston",
    "philadelphia", "detroit", "denver", "phoenix", "las vegas", "gulf coast",
    "east coast", "west coast", "midwest",
}, key=len, reverse=True)

NONSPEECH = re.compile(r"[\[(](?:music|applause|laughter|inaudible|unintelligible|silence|"
                       r"foreign|__|singing|instrumental|noise|crosstalk)[^\])]*[\])]", re.I)
BRACKETED = re.compile(r"[\[(][^\])]{0,40}[\])]")
FILLER_ONLY = re.compile(r"^(?:(?:uh|um|uhh|umm|mhm|hmm|ah|oh|yeah|okay|ok|so|and|but|"
                         r"you know|i mean|right)[\s,.]*)+$", re.I)
STUTTER = re.compile(r"\b(\w+)(\s+\1\b){1,}", re.I)
CHEVRON = re.compile(r"^>+\s*")
TIMED_LINE = re.compile(r"^\[(\d{1,3}):(\d{2})\]\s*(.*)$")
ID_FROM_NAME = re.compile(r"\[([A-Za-z0-9_-]{11})\]")


def load(path: Path):
    """[(seconds|None, text)] with non-speech and filler removed."""
    cues = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line:
            continue
        t = None
        m = TIMED_LINE.match(line)
        if m:
            t = int(m.group(1)) * 60 + int(m.group(2))
            line = m.group(3)
        line = CHEVRON.sub("", line)
        line = NONSPEECH.sub(" ", line)
        line = BRACKETED.sub(" ", line)
        line = STUTTER.sub(r"\1", line)
        line = re.sub(r"\s+", " ", line).strip(" -")
        if not line or FILLER_ONLY.match(line):
            continue
        cues.append((t, line))
    return cues


def passages(cues, target_words=90):
    """Group cues into passages of roughly target_words, breaking on long pauses."""
    out, buf, start, prev_t, n = [], [], None, None, 0
    for t, text in cues:
        if start is None:
            start = t
        gap = (t - prev_t) if (t is not None and prev_t is not None) else 0
        if buf and (n >= target_words or gap > 6):
            out.append((start, " ".join(buf)))
            buf, start, n = [], t, 0
        buf.append(text)
        n += len(text.split())
        prev_t = t
    if buf:
        out.append((start, " ".join(buf)))
    return out


def tag(text):
    """(weighted scores, matched terms per category)."""
    low = " " + re.sub(r"[^a-z0-9$%]", " ", text.lower()) + " "
    low = re.sub(r"\s+", " ", low)
    scores, terms = Counter(), defaultdict(list)
    for cat, phrases in PHRASES.items():
        pts = 0
        # repetition is signal: a passage really about the dollar says "dollar"
        # several times. Capped so one word cannot run away with the passage.
        for p in phrases:
            n = min(low.count(f" {p} "), 2)
            if n:
                pts += 3 * n
                terms[cat].append(p if n == 1 else f"{p}x{n}")
        for w in WORDS[cat]:
            n = min(low.count(f" {w} "), 3)
            if n:
                pts += n
                terms[cat].append(w if n == 1 else f"{w}x{n}")
        if pts:
            scores[cat] = pts * WEIGHT.get(cat, 1.0)
    return scores, terms


def dates_in(text, now_year):
    """[(expression, kind)] where kind is future / past / relative / seasonal."""
    out, seen = [], set()

    def add(expr, kind):
        key = (expr.lower(), kind)
        if key not in seen:
            seen.add(key)
            out.append((expr, kind))

    for m in YEAR.finditer(text):
        y = int(m.group(0))
        add(m.group(0), "future" if y >= now_year else "past")
    for m in MONTH_DATE.finditer(text):
        expr, year = m.group(0).strip(), m.group(1)
        if year:
            add(expr, "future" if int(year) >= now_year else "past")
        elif re.match(r"^(in|by|on|of|during|until|before|after|around|since)\b", expr, re.I) \
                or re.search(r"\d", expr):
            add(expr, "relative")
    for m in RELATIVE.finditer(text):
        add(m.group(0).strip(), "relative")
    for m in SEASONAL.finditer(text):
        add(m.group(0).strip(), "seasonal")
    return out


def places_in(text):
    low = " " + re.sub(r"[^a-z ]", " ", text.lower()) + " "
    low = re.sub(r"\s+", " ", low)
    return [p for p in PLACES if f" {p} " in low]


def analyse(path: Path, min_score: float, now_year: int):
    m = ID_FROM_NAME.search(path.name)
    vid = m.group(1) if m else ""
    title = ID_FROM_NAME.sub("", path.stem).strip()
    rows = []
    for start, text in passages(load(path)):
        if len(text.split()) < 12:
            continue
        scores, terms = tag(text)
        dates = dates_in(text, now_year)
        forward = [d for d, k in dates if k in ("future", "relative", "seasonal")]
        past = [d for d, k in dates if k == "past"]
        is_event = bool(PREDICT_CUE.search(text))
        top = [c for c, sc in scores.most_common() if sc >= min_score]
        primary = top[0] if top else FALLBACK
        if is_event:
            bucket = "event_with_date" if forward else "event_no_date"
        else:
            bucket = "context"
        rows.append({
            "video_id": vid,
            "title": title,
            "t": start if start is not None else "",
            "url": f"https://youtu.be/{vid}?t={start}" if vid and start is not None else "",
            "primary": primary,
            "categories": ",".join(top[:4]) or FALLBACK,
            "bucket": bucket,
            "when": "; ".join(forward[:5]),
            "when_past": "; ".join(past[:3]),
            "places": ",".join(places_in(text)[:6]),
            "quantities": "; ".join(dict.fromkeys(q.strip() for q in QUANTITY.findall(text)))[:120],
            "terms": ",".join(terms.get(primary, [])[:8]),
            "text": text,
        })
    return rows


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("indir", help="directory of .txt transcripts (download them with --timestamps)")
    ap.add_argument("-o", "--outdir", help="output directory (default: indir)")
    ap.add_argument("--min-score", type=float, default=2.0,
                    help="weighted points needed to apply a category (default 2)")
    ap.add_argument("--now", type=int, default=dt.date.today().year,
                    help="years at or after this count as forecasts (default: this year)")
    args = ap.parse_args()

    indir = Path(args.indir).expanduser().resolve()
    outdir = Path(args.outdir).expanduser().resolve() if args.outdir else indir
    outdir.mkdir(parents=True, exist_ok=True)

    files = sorted(f for f in indir.glob("*.txt") if not f.name.startswith("."))
    if not files:
        sys.exit(f"no .txt transcripts in {indir}")

    rows = []
    for f in files:
        r = analyse(f, args.min_score, args.now)
        rows.extend(r)
        print(f"  {f.name[:66]:<66} {len(r):>4} passages")

    cols = ["video_id", "title", "t", "url", "primary", "categories", "bucket",
            "when", "when_past", "places", "quantities", "terms", "text"]
    with (outdir / "claims.tsv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    dated = [r for r in rows if r["bucket"] == "event_with_date"]
    dated.sort(key=lambda r: (r["when"], r["video_id"], r["t"] or 0))
    with (outdir / "timeline.tsv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(dated)

    by_cat = defaultdict(list)
    for r in rows:
        by_cat[r["primary"]].append(r)
    lines = ["# Transcript topic breakdown", "",
             f"{len(files)} videos, {len(rows)} passages, {len(dated)} dated forecasts, "
             f"{sum(1 for r in rows if r['bucket'] == 'event_no_date')} undated forecasts.", "",
             "| category | passages | dated | share |", "|---|---:|---:|---:|"]
    for cat, rs in sorted(by_cat.items(), key=lambda kv: -len(kv[1])):
        d = sum(1 for r in rs if r["bucket"] == "event_with_date")
        lines.append(f"| {cat} | {len(rs)} | {d} | {len(rs) * 100 // len(rows)}% |")
    years = Counter(y for r in rows for y in re.findall(r"\b(20[2-5]\d)\b", r["when"]))
    if years:
        lines += ["", "## Forecast years named", "", "| year | passages |", "|---|---:|"]
        lines += [f"| {y} | {n} |" for y, n in sorted(years.items())]
    places = Counter(p for r in rows for p in r["places"].split(",") if p)
    if places:
        lines += ["", "## Places named", "", "| place | passages |", "|---|---:|"]
        lines += [f"| {p} | {n} |" for p, n in places.most_common(15)]
    (outdir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"\n{len(rows)} passages -> {outdir / 'claims.tsv'}")
    print(f"{len(dated)} dated forecasts -> {outdir / 'timeline.tsv'}")
    print(f"summary -> {outdir / 'report.md'}")


if __name__ == "__main__":
    main()

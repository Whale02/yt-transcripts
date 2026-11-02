#!/usr/bin/env python3
"""Batch-download YouTube transcripts as plain text. No API key, no paid service.

Fetches the caption track with yt-dlp (manual subs if the uploader wrote them,
auto-generated otherwise), then converts the .vtt into readable text.

  python yt_transcripts.py URL [URL ...]
  python yt_transcripts.py -f urls.txt -o out/
  python yt_transcripts.py "https://www.youtube.com/@channel/videos" --limit 50

A playlist, channel or @handle URL expands to every video on it. Re-running
skips videos already in the archive file, so an interrupted batch resumes.
"""

from __future__ import annotations

import argparse
import csv
import html
import re
import subprocess
import sys
from pathlib import Path

TAG = re.compile(r"<[^>]+>")
CUE_TIME = re.compile(r"(\d{2}:\d{2}:\d{2}\.\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}\.\d{3})")
ID_FROM_NAME = re.compile(r"\[([A-Za-z0-9_-]{11})\]")


def run_ytdlp(urls, outdir, langs, limit, cookies_browser, sleep):
    """Pull caption files only. Returns yt-dlp's exit code."""
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--skip-download",
        "--write-subs", "--write-auto-subs",
        "--sub-langs", langs,
        "--sub-format", "vtt/best",
        "--convert-subs", "vtt",
        "--ignore-errors",
        "--no-warnings",
        "--no-progress",
        "--sleep-requests", str(sleep),
        "--download-archive", str(outdir / ".archive.txt"),
        # without this, --skip-download means nothing is ever recorded and every
        # re-run re-fetches the whole channel
        "--force-write-archive",
        "--print-to-file",
        "%(id)s\t%(title)s\t%(duration)s\t%(webpage_url)s\t%(upload_date)s",
        str(outdir / "manifest.tsv"),
        "-o", str(outdir / "%(title).120B [%(id)s].%(ext)s"),
    ]
    if limit:
        cmd += ["--playlist-end", str(limit)]
    if cookies_browser:
        cmd += ["--cookies-from-browser", cookies_browser]
    cmd += list(urls)
    print("  " + " ".join(cmd[2:6]) + " ...", file=sys.stderr)
    return subprocess.call(cmd)


def pick_one_per_video(vtts, keep_extras):
    """One caption file per video. Prefers the original track over auto-translations
    (yt-dlp names those en-de, en-fr, ...). Extras are deleted unless --keep-vtt."""
    def rank(path):
        suffix = path.stem.rsplit(".", 1)[-1].lower() if "." in path.stem else ""
        for i, want in enumerate(("", "en-orig", "en", "en-us", "en-gb", "en-en")):
            if suffix == want:
                return i
        return 99

    groups = {}
    for v in vtts:
        m = ID_FROM_NAME.search(v.name)
        groups.setdefault(m.group(1) if m else v.name, []).append(v)

    chosen = []
    for _, files in sorted(groups.items()):
        files.sort(key=rank)
        chosen.append(files[0])
        for extra in files[1:]:
            if not keep_extras:
                extra.unlink()
    return chosen


def parse_vtt(path: Path):
    """[(start_seconds, text_line)] with the rolling auto-caption repeats removed."""
    out, last, start = [], None, 0.0
    cue_start = None
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        m = CUE_TIME.search(line)
        if m:
            h, mnt, s = m.group(1).split(":")
            cue_start = int(h) * 3600 + int(mnt) * 60 + float(s)
            continue
        if not line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE", "STYLE")):
            continue
        if line.isdigit():          # sequence number in srt-ish files
            continue
        text = html.unescape(TAG.sub("", line)).strip()
        if not text or text == last:
            continue
        last = text
        out.append((cue_start if cue_start is not None else start, text))
    return out


def write_text(cues, dest: Path, timestamps: bool):
    if timestamps:
        body = "\n".join(f"[{int(t)//60:02d}:{int(t)%60:02d}] {x}" for t, x in cues)
    else:
        # reflow into paragraphs: break where the gap between cues is > 4s
        chunks, buf, prev = [], [], None
        for t, x in cues:
            if prev is not None and t - prev > 4.0 and buf:
                chunks.append(" ".join(buf))
                buf = []
            buf.append(x)
            prev = t
        if buf:
            chunks.append(" ".join(buf))
        body = "\n\n".join(chunks)
    dest.write_text(body + "\n", encoding="utf-8")
    return len(body)


def main():
    # Windows consoles default to cp1252 and choke on CJK / fullwidth video titles.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls", nargs="*", help="video / playlist / channel URLs")
    ap.add_argument("-f", "--file", help="text file with one URL per line (# comments ok)")
    ap.add_argument("-o", "--outdir", default="transcripts", help="output directory (default: transcripts)")
    ap.add_argument("-l", "--langs", default="en-orig,en,en-US,en-GB",
                    help='sub languages, yt-dlp syntax (default English; try "zh-Hans,zh", or "en.*" to also pull auto-translations)')
    ap.add_argument("--limit", type=int, help="max videos per playlist/channel")
    ap.add_argument("--timestamps", action="store_true", help="prefix each line with [mm:ss]")
    ap.add_argument("--keep-vtt", action="store_true", help="keep the raw .vtt files")
    ap.add_argument("--cookies-browser", help="e.g. chrome, edge, firefox — for age-gated or bot-checked videos")
    ap.add_argument("--sleep", type=float, default=1.0, help="seconds between requests (default 1)")
    args = ap.parse_args()

    urls = list(args.urls)
    if args.file:
        for line in Path(args.file).read_text(encoding="utf-8").splitlines():
            line = line.split("#")[0].strip()
            if line:
                urls.append(line)
    if not urls:
        ap.error("give at least one URL, or -f urls.txt")

    outdir = Path(args.outdir).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print(f"→ {outdir}", file=sys.stderr)

    rc = run_ytdlp(urls, outdir, args.langs, args.limit, args.cookies_browser, args.sleep)

    vtts = pick_one_per_video(sorted(outdir.glob("*.vtt")), args.keep_vtt)
    written = 0
    for vtt in vtts:
        cues = parse_vtt(vtt)
        if not cues:
            print(f"  empty: {vtt.name}", file=sys.stderr)
            continue
        stem = re.sub(r"\.[A-Za-z0-9_-]+$", "", vtt.stem)   # drop the .en / .en-orig lang suffix
        dest = outdir / f"{stem}.txt"
        n = write_text(cues, dest, args.timestamps)
        written += 1
        print(f"  {dest.name}  ({n:,} chars)")
        if not args.keep_vtt:
            vtt.unlink()

    manifest = outdir / "manifest.tsv"
    if manifest.exists():
        rows = [r for r in csv.reader(manifest.read_text(encoding="utf-8").splitlines(), delimiter="\t") if r]
        seen, uniq = set(), []
        for r in rows:
            if r[0] not in seen:
                seen.add(r[0])
                uniq.append(r)
        with manifest.open("w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(["id", "title", "duration_s", "url", "upload_date"])
            w.writerows(uniq)

    have = len(list(outdir.glob("*.txt")))
    print(f"\n{written} new, {have} total transcripts in {outdir}", file=sys.stderr)
    if rc != 0:
        print("yt-dlp reported errors on some videos (see above); the rest still downloaded.", file=sys.stderr)
    return 1 if rc != 0 else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Try the YouTube public transcript endpoint when yt-dlp video metadata is bot-gated.

Usage:
  python scripts/fetch_missing_captions.py VIDEO_ID:corpus VIDEO_ID:corpus-streams
Only write raw transcript files if full, timestamped captions are returned.
"""
import csv
import re
import sys
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

ROOT=Path(__file__).resolve().parents[1]
ID=re.compile(r"^[A-Za-z0-9_-]{11}$")

def main():
    api=YouTubeTranscriptApi()
    fetched=0
    blocked=[]
    for pair in sys.argv[1:]:
        vid,folder=(pair.split(":",1)+["corpus"])[:2] if ":" in pair else (pair,"corpus")
        if not ID.fullmatch(vid) or folder not in ("corpus","corpus-streams"):
            raise ValueError(f"Invalid video id/collection: {pair}")
        directory=ROOT/folder
        if any(vid in p.name for p in directory.glob("*.txt")):
            print(f"Already exists: {vid}")
            continue
        try:
            captions=api.fetch(vid,languages=("en","en-US","en-GB"))
            data=list(captions)
            if len(data)<3:
                raise RuntimeError("No captioned speech available")
            body="\n".join(
                f"[{int(c.start)//60:02d}:{int(c.start)%60:02d}] {c.text.replace(chr(10),' ').strip()}"
                for c in data if c.text.strip()
            )
            if len(body)<120:
                raise RuntimeError("Too little transcript content")
            name=f"New Last Days upload [{vid}].txt"
            (directory/name).write_text(body+"\n",encoding="utf-8")
            manifest=directory/"manifest.tsv"
            existing=manifest.read_text(encoding="utf-8-sig",errors="replace") if manifest.exists() else ""
            if not re.search(r"(?m)^"+re.escape(vid)+r"\t",existing):
                with manifest.open("a",encoding="utf-8") as f:
                    f.write(f"{vid}\tNew Last Days upload\t\t"
                            f"https://www.youtube.com/watch?v={vid}\t\n")
            print(f"SUCCESS: {vid} -> {folder}/{name}, {len(data)} caption cues")
            fetched+=1
        except Exception as ex:
            blocked.append((vid,str(ex)))
            print(f"FAILED: {vid}: {type(ex).__name__}: {str(ex)[:300]}",file=sys.stderr)
    print(f"Captured {fetched}; inaccessible: {len(blocked)}")
    if blocked:
        return 1
    return 0

if __name__=="__main__":
    sys.exit(main())

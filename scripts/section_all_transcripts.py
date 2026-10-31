#!/usr/bin/env python3
"""Generate source-preserving, sectioned markdown for all Biggs transcripts.

Chinese section outlines and English key points are source-grounded extractive aids, not fact checks.
Run from any directory: python3 scripts/section_all_transcripts.py
"""
import csv
import math
import re
from pathlib import Path
from transcript_keypoints import selected_passages, overview, keypoint_markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "exports" / "all-videos"
ID = re.compile(r"\[([A-Za-z0-9_-]{11})\]\.txt$")
TIME = re.compile(r"^\[(?:(\d+):)?(\d+):(\d{2})\]")
TONGUES = re.compile(
    r"^\[(?:\d+:)?\d+:\d{2}\]\s*(?:(?:speech\.\s*)?foreign speech(?:[.\s]*foreign speech)*[.\s]*|\[?speaking in tongues\]?[.\s]*|\[?unintelligible prayer\]?[.\s]*)$",
    re.I,
)
CATEGORIES = [
    ("美国选举与投票", r"\b(election|midterms?|ballots?|vot(?:e|ing|er|es)|polling station|senate|congress)\b"),
    ("特朗普与白宫", r"\b(trump|white house|mar.a.lago|barron|first lady)\b"),
    ("政党与政治人物", r"\b(democrat|republican|harris|pelosi|newsom|biden|booker|aoc|governor)\b"),
    ("经济、银行与市场", r"\b(econom\w*|financial|bank|stock|market|interest rates?|recession|dollars?|inflation|crypto\w*|bitcoin|silver|gold)\b"),
    ("战争与国际事务", r"\b(war|military|iran|israel|hamas|russia|ukraine|china|taiwan|north korea|nato|nuclear|missiles?)\b"),
    ("治安、袭击与安全", r"\b(attacks?|terrorists?|shoot\w*|bomb|gun|assassinat\w*|security|explosions?|threat|police|fbi)\b"),
    ("疾病、医疗与药品", r"\b(virus|plague|medicine|medications?|diabet\w*|heart disease|health|hospital|pandemic|vaccin\w*)\b"),
    ("地震、风暴与灾害", r"\b(earthquakes?|storms?|hurricanes?|tornado\w*|floods?|tsunami|volcano|fires?|drought|weather)\b"),
    ("物资、能源与供应链", r"\b(supply chains?|shortages?|grocery|food|water|oil|gas|fuel|trucks?|walmart|shelv\w*|electric grid)\b"),
    ("AI、科技与监控", r"\b(artificial intelligence|ai|technology|robots?|drones?|internet|starlink|surveillance|facial recognition|digital|computers?)\b"),
    ("教会、复兴与信仰", r"\b(church(?:es)?|revival|pastor|jesus|holy spirit|god|christ|bible|angel|heaven|satan|spiritual)\b"),
    ("祷告、敬拜与现场互动", r"\b(pray\w*|lord|worship|praise|hallelujah|amen|thank you|sing|brother|sister|family)\b"),
    ("预言、梦境与异象", r"\b(vision|prophe\w*|dream|i saw|i see|the lord showed|i heard|the lord said|coming)\b"),
    ("个人故事与访谈", r"\b(i remember|my wife|my son|when i was|interview|testimony|tell you a story)\b"),
]
PLACES = [
    ("Texas", "texas"), ("California", "california"), ("New York", "new york"),
    ("Florida", "florida"), ("Oklahoma", "oklahoma"), ("Las Vegas", "las vegas"),
    ("New Orleans", "new orleans"), ("Canada", "canada"), ("Europe", "europe"),
    ("France", "france"), ("Berlin", "berlin"), ("Vatican", "vatican"),
    ("China", "china"), ("Russia", "russia"), ("Ukraine", "ukraine"),
    ("Israel", "israel"), ("Iran", "iran"), ("Cuba", "cuba"),
]
CATEGORIES = [(n, re.compile(p, re.I)) for n, p in CATEGORIES]
PLACES = [(n, re.compile(r"\b" + re.escape(p) + r"\b", re.I)) for n, p in PLACES]

def seconds(line):
    m = TIME.match(line)
    return (3600*int(m[1] or 0) + 60*int(m[2]) + int(m[3])) if m else None

def clock(t):
    return f"{t//60:02d}:{t%60:02d}"

def manifest_dates(folder):
    path = folder / "manifest.tsv"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8-sig", newline="", errors="replace") as f:
        return {r["id"]:r["upload_date"] for r in csv.DictReader(f, delimiter="\t")
                if r.get("id") and r["id"] != "id" and r.get("upload_date")}

def summarize(lines):
    text = "\n".join(lines)
    hits = sorted(((name, len(rx.findall(text))) for name,rx in CATEGORIES), key=lambda x:x[1], reverse=True)
    topics = [n for n,c in hits if c>=2][:3] or ["现场讲话（无可靠自动分类）"]
    locations = sorted(((name,len(rx.findall(text))) for name,rx in PLACES), key=lambda x:x[1], reverse=True)
    locations = [n for n,c in locations if c>=2][:4]
    detail = "本段涉及：" + "、".join(topics) + "。"
    if locations: detail += " 提到的地点：" + "、".join(locations) + "。"
    detail += " 本摘要为关键词辅助导航，事件和论断请核对以下原文。"
    return "、".join(topics[:2]), detail

def chapters(lines):
    stamps = [v for line in lines if (v:=seconds(line)) is not None]
    if not stamps: return [(0,0,lines)]
    duration = max(stamps)
    interval = max(240, min(1080, math.ceil((duration+1)/12/60)*60))
    result, part, bucket, previous = [],[],0,0
    for line in lines:
        t=seconds(line)
        if t is not None: previous=t
        next_bucket=previous//interval
        if part and bucket!=next_bucket:
            result.append((bucket*interval, min((bucket+1)*interval-1,duration),part))
            part=[]
        part.append(line)
        bucket=next_bucket
    if part: result.append((bucket*interval,duration,part))
    return result

def transform(video_id, title, source, date):
    raw=source.read_text(encoding="utf-8-sig",errors="replace")
    lines=raw.splitlines()
    edited=[]
    removed=0
    for line in lines:
        if TONGUES.fullmatch(line.strip()):
            m=TIME.match(line)
            edited.append(m.group(0)+" [已省略：字幕明确标注的 speaking in tongues / foreign speech]")
            removed+=1
        else:
            edited.append(line)
    grouped=chapters(edited)
    src=source.relative_to(ROOT).as_posix()
    rows=[
        f"# {title}","",
        f"**视频**: https://www.youtube.com/watch?v={video_id}",
        f"**原始转录**: https://github.com/Whale02/yt-transcripts/blob/master/{src}",
        f"**上传日期**: {date or '原始 manifest 未提供'}",
        f"**源字幕行数**: {len(lines)}；**章节数**: {len(grouped)}；**明确省略行数**: {removed}","",
        "**保留原则**：全部英文正常讲话、原始时间戳、新闻引用、祷告、唱诗、重复和口语错误均保留。仅明确标注为 speaking in tongues/foreign speech 的字幕行被替换为带时间戳占位符。自动字幕无法辨认的方言可能被错误转写成英文，为避免误删，仍保留。中文章节标题是自动主题分类；Section 内容概述和 Key Points 是按时段提取的实际发言，不是经过逐段人工语义总结。任何预言都尚未在此核验。","",
        "## 章节目录","",
    ]
    summaries=[]
    for i,(start,end,part) in enumerate(grouped,1):
        label,tags=summarize(part)
        header=f"{i:02d}. {clock(start)}–{clock(end)} · {label}"
        keypoints=selected_passages(part,4)
        summaries.append((header,overview(label,keypoints),keypoints))
        rows.append(f"- [{header}](#section-{i:02d})")
    rows.extend(["","## 全片概述与 Key Points","",
        f"全片共 {len(grouped)} 节。以下按时间覆盖全片，摘取能够回溯到原字幕的代表性发言；属于自动抽取的内容索引，没有人工语义审核，也不能据此认定预言准确。",""])
    representative=[points[0] for _,_,points in summaries if points]
    if representative:
        indices=sorted({round(i*(len(representative)-1)/max(1,min(len(representative),6)-1))
                        for i in range(min(6,len(representative)))})
        rows.extend(keypoint_markdown(video_id,[representative[k] for k in indices]))
    else:
        rows.append("- 当前视频缺少足够明确的字幕段落。")
    for i,(_,_,part) in enumerate(grouped,1):
        header,section_overview,keypoints=summaries[i-1]
        rows.extend(["",f'<a id="section-{i:02d}"></a>',f"## {header}","",
                     f"**Section 内容概述**：{section_overview}","",
                     "### Key Points / 关键要点","",
                     *keypoint_markdown(video_id,keypoints),"",
                     "### 完整英文 Transcript","",
                     "~~~text",*part,"~~~"])
    (OUT/f"{video_id}.md").write_text("\n".join(rows)+"\n",encoding="utf-8")
    return len(grouped),removed

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    videos={}
    for folder in (ROOT/"corpus", ROOT/"corpus-streams"):
        dates=manifest_dates(folder)
        for source in sorted(folder.glob("*.txt")):
            m=ID.search(source.name)
            if not m: continue
            vid=m.group(1)
            if vid not in videos or source.stat().st_size > videos[vid][0].stat().st_size:
                videos[vid]=(source,source.name[:m.start()].strip() or vid,dates.get(vid,""))
    index=[]
    omitted=0
    for vid,(src,title,date) in sorted(videos.items()):
        count,removed=transform(vid,title,src,date)
        omitted+=removed
        index.append((date,title,vid,count))
    for old in OUT.glob("*.md"):
        if old.name!="INDEX.md" and old.stem not in videos: old.unlink()
    index.sort(key=lambda row:(row[0],row[1]),reverse=True)
    rows=["# Brandon Biggs · 全部视频分章节 Transcript","",
          f"共 **{len(index)}** 条独立视频；明确 speaking-in-tongues 省略标记 {omitted} 处。","",
          "每条视频均有全片概述、各章节内容概述和带原视频时间戳的 Key Points。概要由规则生成，关键要点从原文提取，未作人工深度语义审核，也未核验具体预言。","",
          "| 上传日期 | 视频 / 完整 Transcript | 章节数 |","|---|---|---:|"]
    for date,title,vid,count in index:
        name=title.replace("|","\\|").replace("[","(").replace("]",")")
        date=(date[:4]+"-"+date[4:6]+"-"+date[6:8]) if len(date)==8 else "未提供"
        rows.append(f"| {date} | [{name}]({vid}.md) | {count} |")
    (OUT/"INDEX.md").write_text("\n".join(rows)+"\n",encoding="utf-8")
    print(f"Generated {len(index)} transcript files, plus INDEX.md. Explicit tongue-caption omissions: {omitted}.")

if __name__=="__main__":
    main()

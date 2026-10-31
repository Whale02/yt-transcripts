#!/usr/bin/env python3
"""Grounded extractive key points for time-coded conversational transcripts.

No language model, external APIs, or invented facts: excerpts are contiguous
source text, so users can check each selected passage in the raw transcript.
"""
import math
import re
from collections import Counter

STAMP = re.compile(r"^\[(?:(\d+):)?(\d+):(\d{2})\]\s*(.*)$")
TOKENS = re.compile(r"[a-z][a-z'-]{2,}",re.I)
STOP = set("""the a and for of has have they them their into what when where while with without this that these those there then being been from about you your are was were will shall would could should did does doing just know like really going gonna theyre thats because right thing things here there something someone everybody everything whenever yall ourselves themselves out over under again more less too much very how why who whose said says say see seeing saw got get come coming people one two three we us our i me my mine am its it is at on in to an or as by be if not no yes so but do can he she his her hers they be done make made go goes he we them a lot all had has around through from after before them thank good bad okay well sure back down also look looking today tonight tomorrow yesterday yeah oh um uh yeah Lord lord god jesus holy spirit""".split())
CUES = [
    (re.compile(r"\bi saw\b|\bi see\b|\bvision\b|\bi heard\b|\bthe lord showed\b|\bgod showed\b",re.I),2.2),
    (re.compile(r"\bi believe\b|\bi think\b|\bwill happen\b|\bgoing to\b|\bthere will\b|\bis coming\b",re.I),1.0),
    (re.compile(r"\b(?:election|midterm|trump|senate|congress|president|governor|democrat|republican|harris|musk)\b",re.I),1.0),
    (re.compile(r"\b(?:attack|bomb|shooting|earthquake|pandemic|plague|war|iran|russia|china|israel|virus|shortage)\b",re.I),1.0),
    (re.compile(r"\b(?:202[4-9]|2030|friday|monday|tuesday|wednesday|thursday|saturday|sunday|january|february|march|april|may|june|july|august|september|october|november|december)\b",re.I),0.8),
]
PRAYER = re.compile(r"\b(?:father i thank|thank you lord|we praise you|hallelujah|give you the glory|in jesus name|amen amen)\b",re.I)
PROMO = re.compile(r"\b(?:like and subscribe|subscribe to the channel|hit that like button|super chat|share this video)\b",re.I)
NONCONTENT = re.compile(r"^(\[已省略|Foreign speech|Speech\. Foreign speech)",re.I)

def timestamp(s):
    m=STAMP.match(s)
    if not m: return None
    return 3600*int(m[1] or 0)+60*int(m[2])+int(m[3])

def create_clips(lines, min_words=12, max_words=55, max_seconds=28):
    """Combine consecutive subtitle fragments into readable passages with timestamp."""
    segments=[]
    words=[]
    first_t=last_t=None
    for line in lines:
        m=STAMP.match(line)
        if not m: continue
        t=timestamp(line)
        body=m.group(4).replace(">>","").strip()
        if NONCONTENT.search(body): continue
        if not body: continue
        if first_t is None: first_t=t
        last_t=t
        words.append(body)
        joined=" ".join(words)
        count=len(joined.split())
        sentence_end = bool(re.search(r'[.?!]["”\']?$',body))
        if (count>=min_words and sentence_end) or count>=max_words or t-first_t>=max_seconds:
            if count>=min_words:
                segments.append((first_t,joined))
            words=[]
            first_t=last_t=None
    if words and (sum(len(x.split()) for x in words)>=min_words):
        segments.append((first_t," ".join(words)))
    return segments

def selected_passages(lines, n=4):
    clips=create_clips(lines)
    if not clips: return []
    if len(clips)<=n: return clips
    counts=Counter()
    wordsets=[]
    for t,txt in clips:
        tokens=set(w.lower().strip("-'") for w in TOKENS.findall(txt))
        tokens={w for w in tokens if w not in STOP and len(w)>3}
        wordsets.append(tokens)
        counts.update(tokens)
    # Important passages have specific facts, diversity, and attributed language.
    scores=[]
    for i,(t,txt) in enumerate(clips):
        unique=wordsets[i]
        novelty=sum(1/math.sqrt(counts[w]) for w in unique)
        cue=sum(weight for pat,weight in CUES if pat.search(txt))
        nums=0.8 if re.search(r"\b\d{2,4}\b",txt) else 0
        penalty=(2.4 if PRAYER.search(txt) else 0)+(1.0 if PROMO.search(txt) else 0)
        scores.append((novelty/max(4,math.sqrt(len(unique)))+cue+nums-penalty,i))
    # Greedy MMR: discourage close timestamps or repeating the same words.
    chosen=[]
    for j in range(n):
        candidates=[]
        for score,i in scores:
            if i in chosen: continue
            overlap=0.0
            for k in chosen:
                union=len(wordsets[i] | wordsets[k])
                overlap=max(overlap,len(wordsets[i] & wordsets[k]) / max(1,union))
            time_gap=min(abs(clips[i][0]-clips[k][0]) for k in chosen) if chosen else 10**9
            proximity=1.8 if time_gap<55 else (0.7 if time_gap<110 else 0)
            candidates.append((score-3*overlap-proximity,i))
        if not candidates: break
        chosen.append(max(candidates)[1])
    return sorted((clips[k] for k in chosen),key=lambda x:x[0])

def overview(topic_label, keypoints):
    if not keypoints:
        return f"本节讨论主题：{topic_label}。本节原文没有足够长的完整字幕片段可供可靠提取。"
    labels=[]
    sample=" ".join(p for _,p in keypoints)
    if re.search(r"\bi saw\b|\bi see\b|\bvision\b",sample,re.I):
        labels.append("异象或所见")
    if re.search(r"\bi believe\b|\bi think\b",sample,re.I):
        labels.append("个人判断")
    if re.search(r"\bsaid\b|\bnews\b|\breport\b|\bvideo\b",sample,re.I):
        labels.append("引用或评论")
    if re.search(r"\bpray\b|\blord\b|\bjesus\b",sample,re.I):
        labels.append("祷告及宗教表达")
    detail="、".join(labels) if labels else "具体发言"
    return f"本节围绕{topic_label}展开，包含{detail}。下列要点选自这一时段的连续原话，并附可回听的时间戳；仅代表讲话内容，尚未核验事实。"

def point_caption(text):
    if re.search(r"\bi saw\b|\bi see\b|\bvision\b",text,re.I):
        return "他描述所见"
    if re.search(r"\bi believe\b|\bi think\b|\bprobably\b",text,re.I):
        return "他表达判断"
    if re.search(r"\bi heard\b|\blord said\b|\bthe lord told\b",text,re.I):
        return "他转述所听到的话"
    if re.search(r"\bpray\b|\bthank you lord\b|\bin jesus name\b",text,re.I):
        return "他进行祷告"
    if re.search(r"\bnews\b|\barticle\b|\bmedia\b|\breport\b",text,re.I):
        return "他讨论新闻或报道"
    return "本段原话"

def keypoint_markdown(video_id, keypoints):
    if not keypoints:
        return ["- 本节没有足够清晰的字幕可自动提取关键发言。"]
    result=[]
    for time,phrase in keypoints:
        stamp=f"{time//60:02d}:{time%60:02d}"
        excerpt=phrase.replace("|","\\|").replace("\n"," ").strip()
        # Quotation is extractive, not model-written or fact-checked.
        result.append(f"- **[{stamp}](https://www.youtube.com/watch?v={video_id}&t={time}s) · {point_caption(excerpt)}**：{excerpt}")
    return result

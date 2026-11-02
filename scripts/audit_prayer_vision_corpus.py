#!/usr/bin/env python3
"""Corpus-level reconnaissance of prayer-change claims and repeated 2026 midterm visions.

Evidence discovery only: patterns select candidates for human verification. Counts are
mentions / recordings, never probabilities of future events or prayer efficacy.
"""
from collections import Counter
from bisect import bisect_left, bisect_right
from pathlib import Path
import csv, json, re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'exports' / 'research'
OUT.mkdir(parents=True, exist_ok=True)
STAMP = re.compile(r'^\[(?:(\d+):)?(\d+):(\d{2})\]\s*(.*)')
VID = re.compile(r'\[([A-Za-z0-9_-]{11})\]\.txt$')

def sec(m):
    return int(m[1] or 0)*3600+int(m[2])*60+int(m[3])

def fmt(t):
    return f'{t//3600}:{t//60%60:02}:{t%60:02}' if t>=3600 else f'{t//60}:{t%60:02}'

def read_dates():
    dates={}
    for p in [ROOT/'corpus'/'manifest.tsv',ROOT/'corpus-streams'/'manifest.tsv']:
        if not p.exists():continue
        with p.open(encoding='utf8', errors='replace') as f:
            for d in csv.DictReader(f, delimiter='\t'):
                v=d.get('id','');dt=d.get('upload_date','')
                if re.fullmatch(r'\d{8}', dt or ''): dates[v]=f'{dt[:4]}-{dt[4:6]}-{dt[6:]}'
    idx=ROOT/'exports'/'all-videos'/'INDEX.md'
    if idx.exists():
        for line in idx.read_text(encoding='utf8').splitlines():
            m=re.search(r'\|\s*(\d{4}-\d\d-\d\d)\s*\|.*?\(([A-Za-z0-9_-]{11})\.md\)',line)
            if m:dates[m[2]]=m[1]
    return dates

def context(segments, times, at, radius=75):
    lo=bisect_left(times,at-radius)
    hi=bisect_right(times,at+radius)
    return ' '.join(x[1] for x in segments[lo:hi])

# These are ONLY keyword retrieval gates, not automatically adjudicated truth labels.
prayer_change = {
    'explicit_averted': re.compile(r'(?:we|you|they|god|prayer).{0,60}(?:stopped|averted|prevented|saved|delayed|shifted|changed|held.{0,14}back)|(?:stopped|averted|prevented|saved|delayed|shifted|changed|held.{0,14}back).{0,75}(?:pray|prayer|interced)',re.I),
    'prayed_away': re.compile(r'\bprayed? (?:it|them|this|that) (?:away|out)\b|\bprayer (?:averted|prevented|stopped|changed|shifted)\b',re.I),
    'before_after': re.compile(r'\b(?:it|this|that|the (?:attack|storm|event)) (?:didn.t happen|was cancelled|didn.t come|never happened)\b.{0,95}\b(?:prayed|prayer|intercession)',re.I),
    'claim_fallibility': re.compile(r'\bi (?:missed|was wrong|got it wrong)\b|\b(?:vision|prophecy) (?:was|is) (?:wrong|off|delayed)\b',re.I)
}
out=[]
summ=Counter()
for folder in ('corpus','corpus-streams'):
    for path in (ROOT/folder).glob('*.txt'):
        m=VID.search(path.name)
        if not m:continue
        id=m[1]
        segments=[]
        for line in path.read_text(encoding='utf8',errors='replace').splitlines():
            mt=STAMP.match(line)
            if mt and mt[4].strip():segments.append((sec(mt),mt[4].strip()))
        if not segments:continue
        out.append(dict(id=id,title=path.stem.rsplit(' [',1)[0],path=str(path.relative_to(ROOT)),segments=segments))
        summ['transcript_files']+=1

dates=read_dates()
# Deduplicate videos if same video ID present in two folders.
byid={item['id']:item for item in out}
summ['unique_ids']=len(byid)

midterm=[]
prayer=[]
for obj in byid.values():
    id=obj['id']; segments=obj['segments'];date=dates.get(id)
    times=[x[0] for x in segments]
    for t,line in segments:
        if re.search(r'\bsenate\b',line,re.I) and (date is None or date>='2025-01-01'):
            c=context(segments,times,t,65)
            senator=re.search(r'(?:lose|lost|losing).{0,35}senate|senate.{0,55}(?:flips? blue|flipped blue|going blue|go blue|blue|lose|lost)|senate.{0,35}to (?:the )?democrat',c,re.I)
            house=re.search(r'(?:keep|win|winning|maintain|retain|holding).{0,35}house|house.{0,55}(?:red|republican|keep|win|maintain|retain)',c,re.I)
            if senator and house:
                midterm.append(dict(id=id,date=date,at=t,url=f'https://www.youtube.com/watch?v={id}&t={t}s',snippet=c[:900],label='candidate_R_House_D_Senate'))
        if not re.search(r'pray|intercess|avert|stopp|prevent|chang|shift|delay|held|missed|wrong',line,re.I):
            continue
        for name,pat in prayer_change.items():
            s=context(segments,times,t,16)
            if pat.search(s):
                prayer.append(dict(category=name,id=id,date=date,at=t,url=f'https://www.youtube.com/watch?v={id}&t={t}s',excerpt=s[:720]))
# De-dupe overlapping hits in 90-second neighborhoods within each video.
def dedupe(items,categorykey):
    keep=[];latest={}
    for item in sorted(items,key=lambda x:(x['id'],x.get(categorykey,''),x['at'])):
        key=(item['id'],item.get(categorykey,''))
        if item['at']-latest.get(key,-99999)<85:continue
        latest[key]=item['at'];keep.append(item)
    return keep

midterm=dedupe(midterm,'label')
prayer=dedupe(prayer,'category')
bycategory=Counter(x['category'] for x in prayer)
midterm_videos={x['id'] for x in midterm}
dated=sorted(midterm,key=lambda x:(x['date'] or '9999',x['id'],x['at']))
for x in dated: x['snippet']=x['snippet'][:680]
for x in prayer: x['excerpt']=x['excerpt'][:580]
# Prioritize cases with event names where explicit-change statements have object to investigate.
casewords=re.compile(r'\b(?:coachella|assassinat|trump|hurricane|storm|earthquake|plague|virus|vaccine|israel|iran|canada|election|midterm|senate|house|volcano|attack|shooting|terror|france|japan|new orleans|war|october|june|november|december|202\d)\b',re.I)
named=[x for x in prayer if casewords.search(x['excerpt']) and x['category']!='claim_fallibility']
report={
 'method':'Simple regular expression candidate retrieval of original English timestamped subtitle lines, using 16s or 65s context. Not a comprehensive semantic classification; not yet human adjudicated.',
 'scope':dict(transcript_files=summ['transcript_files'],unique_videos=summ['unique_ids'],with_dated_midterm_candidates=len(midterm_videos),candidate_midterm_passages=len(midterm),prayer_change_candidate_passages=len(prayer),prayer_categories=dict(bycategory),named_prayer_candidate_passages=len(named)),
 'notes':['A repeated clip may represent a replay, not a new vision.','Falsification requires tracing earliest statement and independent event evidence.','Do not infer changes in reality from any prayer/change language.','Missing upload dates are null, not assigned by intuition.'],
 'midterm_candidates':dated[:450],
 'named_prayer_change_candidates':sorted(named,key=lambda x:(x['date'] or '9999',x['id'],x['at']))[:900],
 'all_prayer_change_candidates':sorted(prayer,key=lambda x:(x['date'] or '9999',x['id'],x['at']))[:1200]
}
p=OUT/'full-corpus-prayer-vision-candidate-audit-2026-11-02.json'
p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report['scope'],indent=2))
print('wrote',p)

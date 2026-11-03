# Extraction progress

Append-only. Each batch adds what it covered, the counts, and anything a later batch
should not repeat. The authoritative numbers always come from `python prophecy.py todo`.

## Baseline, 29 August 2026

576 videos, 70,274 passages, all dated. 187 claims across 91 canonical events, 26 graph
edges, 8 evidence rows, 4 scored verdicts. Tier 1 (forward claim carrying a date) stands at
56 of 2,477 read. Integrity and selftest both clean.

Already covered, do not redo: the New Madrid thread (16 mentions, 2023-2026), the 1930s
crash thread including the tariff conditional and the December 2025 delay claim, the digital
dollar thread, the plague and 350 million thread, Okinawa and July 2026, the 11 September
2026 ground zero claim, the Mexico and Acapulco batch from 29 August, the 2027 eye of the
hurricane batch, the crypto clarity batch, and the economic batch from June to October 2025.

Verdicts already recorded, do not re-score without new evidence: crash-1930s CONTRADICTED,
okinawa-july-shaking PARTIAL_MATCH, new-madrid-awakening PARTIAL_MATCH, egg-price-spike
PARTIAL_MATCH, silver-75 NOT_YET_DUE, new-madrid-quake UNRESOLVED.

## Batch 001-002, tier-1 sweep, 29 August 2026
Covered the late-August 2026 videos gGCKex1IOtE, F-CNFR1LQQI, UAPYhpm_sX0 and WCSr1gn7mlM: 25 mentions,
12 new canonical claims seeded (Noah's ark dig, fuel rationing, Russia-NK bridge, January 6 repeat,
alien files, second wave, eye-of-storm cycle, drought relocation, UN September, blood moon, acceleration,
Middle East revival spots). Surprise: the same week carries both a prayed 15 September Clarity Act date and a
news read that the bill slips to 2027; both kept, the second marked timing_update rather than merged.

## Sweep batch 01, 29 August 2026

Covered 2026-08-20 to 2026-08-27: the 27 Aug economics/surveillance video, the 25 Aug worldwide
roundup, the 22 Aug prayer session, and the whole of "2027 the eye of the hurricane" (WCSr1gn7mlM).
40 mentions, 14 new canonical claims. Tier 1 moved 56 -> 106 of 2,477 (4.3%).

Surprise worth flagging: the analyst clip he plays at gGCKex1IOtE@1487 says crypto legislation may
slip to 2027, which contradicts his own 15 September 2026 dating three days later. Left as
same_event=unsure with delta_type=timing_update rather than merged. Also introduced source_mode
PRAYER_DECREE for prayed-over declarations, which read as predictions but are uttered as decrees.

## Two workers, split by date, 29 August 2026

A second extractor (the autorun.py supervisor session) is writing to this database at the
same time. It sweeps newest first and was at 2026-08-19 when this was written. A 40-passage
batch drafted here for 2026-08-20 to 2026-08-27 was thrown away unloaded because that worker
had already taken every one of those segments.

Partition from here on, so neither worker reads a passage twice:

  * newest-first worker (autorun): 2026 downward from 2026-08-29
  * oldest-first worker (this one): 2023-06-29 upward, using `pick --until <ceiling>`

Tier 1 remaining by year at the split: 2023 99, 2024 283, 2025 974, 2026 1028, total 2384.
Whoever reaches the middle first should re-read this section before crossing it.

## Coordination note, 29 August 2026, 13:56
Two extraction workers are running against this database at once (autorun cycle 1 never exited before
cycle 2 started; runs 153 and 155 are not mine). To stop both reading the same passages, this worker takes
the OLD end of the corpus and walks forward: `pick --tier 1 --until <cutoff>` starting at 2023-12-31.
The other worker uses the default newest-first pick. Whoever reads this: keep to your end, and run
`python prophecy.py dedupe` before finishing, since we have already produced near-duplicate canonical
claims for the same vision (trump-january-scroll, trump-scroll-signing, january-parchment-signing).

## Batches 003-005, 29 August 2026
Batch 003 finished the 20-21 August 2026 videos (25 mentions) and batch 004 opened the old end of the
corpus, December 2023 (25 mentions): the 2024 grace wave, the balloon economy that pops in September or
October 2024, Biden as a television with no reception, and a December 2023 call to pray protection over a
presidential candidate seen outdoors before a big crowd, seven months before Butler. Batch 005 cleared the
16-row judgment queue the parallel worker left and folded its duplicate bank claim ids into one.
Tier 1 now 131 of 2,477.

### old-01, late 2023 (2023-10-24 to 2023-12-30), 40 passages
The December 2023 economic word is the spine of the whole corpus and it was sitting
unextracted: the balloon inflated by rate cuts, re-inflated in May and June, burst in
September into October 2024 with "quantitative easing" heard, then a great crash in the
winter of 2024 into 2025 and a black depression running to 2027. Loaded as one thread
(economy-balloon-2024) with the winter crash left as same_event unsure against crash-1930s
rather than merged, because crash-1930s is already scored CONTRADICTED and this telling
carries its own earlier date.
Also earliest located tellings of the one-currency claim (Dec 2023, 2025-2027 window) and
of leave-the-cities. 17 new canonical claims. Tier 1 56 -> 196 of 2,477.
Note: 3lPkmPBUCBQ@442, given 28 Dec 2023, asks for prayer over a presidential candidate
seen outdoors before a big crowd with mountains. That is six months before Butler. Past due,
needs evidence.

## Sweep batch 02, 29 August 2026

Covered 2026-08-09 to 2026-08-20: the 20 Aug prayer close, "things are happening so quickly"
(6XXc1-oeNWw), "The Lord showed me more of what's coming" (dBStuxYtyFM), and three prayer streams.
50 mentions, 18 new canonical claims. Tier 1 moved 106 -> 196 of 2,477 (7.9%).

Two contradictions left standing rather than merged. Housing: he called it a shallow break earlier,
here it is the worst since 1929 (severity_update). Rosh Hashanah window: a four-month kick-off at
-Z-oPJQyOeU@5911 against a full year to Rosh Hashanah 2027 at 6XXc1-oeNWw@3576 (timing_update).
Best scoreable claim in the batch is byron-florida-governor: named person, named race, November
date, plus his own statement at __45FoTY6rQ@413 that a primary loss means the word was off.

### old-02, Aug to Oct 2023, 33 passages
The channel's founding claims, most of them now past due: $200 oil via a secret Saudi deal
with Russia and China, 80% of world oil wealth into BRICS by 1 Jan 2024, the beginning of a
digital dollar during 2023, a two-state solution plus third temple by March 2024, an Italian
volcano out of the water costing hundreds of thousands of lives, and the 569-day judgment
counted to 2 October 2023.
Two things worth flagging. The 569-day date arrives and is absorbed rather than scored: "I'm
giving more time." Recorded as delta_type delay_claim against judgment-569-days, not merged.
And in Sept 2023 he says flatly he is not believing for a near-term economic fallout, three
months before the December winter-crash word. Both tellings left visible.
15 canonical claims proposed, 12 new. Tier 1 196 -> 229 of 2,477.

## Sweep batch 03, 29 August 2026

Covered 2026-08-01 to 2026-08-09: six prayer streams plus the Italy/Naples and Israel material.
50 mentions, 15 new canonical claims. Tier 1 moved 196 -> 296 of 2,477 (11.9%).

Two things worth not repeating. FCeX9hLlWEk@6398 has the same ground-zero imagery as the
11 September 2026 call but he says outright he does not know the year; filed as a contradiction
against sept11-2026-groundzero rather than merged, because merging would erase the hedge.
QEa4tYadZV0@7546 is the tightest date he has ever put on the plague: end of 2027 into January to
June 2028, out of labs. That one expires 30 June 2028 and should not be re-dated from vaguer tellings.
Note a second autorun worker is extracting into the same prophecy.db concurrently, which is why
tier 1 rises faster than the mention counts in these entries alone.

## Batches 006-008, 29 August 2026
The 2023 end of the corpus is now fully extracted: 59 remaining tier-1 passages cleared in three batches
(25+25+9). Highlights: the 569-day judgment count is given as 510 days in the July 2023 telling and 569 in
the September one, both landing on 2 October, so it is filed as a contradiction rather than merged. The
June 2023 admission that he missed a word and then read the miss as prayer averting it is the single most
important passage for scoring anything marked prayer_may_prevent.

### old-03, mid 2023 (2023-06-29 to 2023-08-25), 26 passages. 2023 IS NOW COMPLETE.
`pick --tier 1 --until 2023-12-31` returns 0. Do not re-sweep 2023.
The find of this batch is a straight contradiction in the countdown claim: 2MOBOMGnCdE@868
gives the angel's count as 510 days, XxwF--X7PLo@1593 gives it as 569, and both land on
2 October 2023. Recorded as delta_type contradiction against judgment-569-days, not merged.
Also corrected batch 02: P7viEh9luCE@0 (5 July 2023) is the first telling of the volcano, so
the 30 September retelling was re-reviewed from first_mention to restatement.
New canonical claim timing-fallibility holds his own account of his misses, including the
chickens episode where a non-event is recovered as either averted by prayer or merely early.
That is the yardstick every later miss gets scored against, so it belongs in the graph.
Tier 1 229 -> 255 of 2,477.

### old-04, December 2024, 40 passages
Two delay mechanisms recorded as canonical claims of their own, because they are what most
of the dated 2025 material eventually resolves into rather than being scored:
reprieve-four-years (the Lord grants four years from 2025 to a shmita boundary, attributed to
the prayers of the saints) and extended-time-grant (asked why what he said was coming in 2025
has not come, the answer is "I'm giving you extended time"). The great dam seen in Dec 2023
for 2025 is retired at OV3ZwMnZc6o@896 before its date, pushed back by prayer, event kept.
Also: the plague thread gets its most checkable detail here, an airborne pathogen designed by
AI, timed to 2026-2027 by reasoning rather than vision. 13 new canonical claims.
Tier 1 405 of 2,477 (16.4%) with both workers counted.

### old-04, December 2024, 40 passages
The load-bearing claim of the whole 2025-2028 period turns up here: "I'm giving you a reprieve
for four years" for a mighty harvest, ending on a shmita boundary, attributed to the prayers of
the saints balancing the scales (aBjqR_4eB6o@961, giyQsMPVfsI@2770).
Two delay mechanisms recorded as their own canonical claims rather than left scattered:
extended-time-grant (WkE7SzHKJKk@1413, where the audience asks why 2025 has not arrived and the
answer is extended time) and dam-wall-ireland-2025 taking a delay_claim (OV3ZwMnZc6o@896, where
the 2025 dam is retired before its date because prayer pushed it back, while the event is kept).
Together with timing-fallibility and november-5-averted, that is four separate devices for
retiring a dated word without scoring it. Worth counting later.
Tier 1 at 405 of 2,477 (16.4%) with both workers contributing.

### old-05, Nov to Dec 2024, 40 passages
Best-anchored batch so far. Three hard dates that can actually be scored: a financial
acceleration by the 2025 Super Bowl (9 Feb, three weeks after the swearing in), a great drought
and great plague in summer 2026 with Trump addressing the nation about it, and attacks warned
over three named events (Macy's parade, Rockin' New Year's Eve, Atlanta) that all passed
without incident. Also XRP at $10,000, said obliquely as "something starting with an X with a
p in it", with no date attached, which is what keeps it unscoreable.
He sets his own standard here at 5rXtqqYsNXI@4513: accuracy in the prophetic will mark 2025.
Filed as prophetic-accuracy-2025 so the rest of the 2025 record has something to be scored
against. And the volcano moves: the 2023 telling had it coming up out of the water, this one
puts it near Rome, so the target is now Campi Flegrei or Vesuvius. Recorded as new_detail.
14 new canonical claims.

### old-05, Nov to Dec 2024, 40 passages
Sharpest date in the corpus so far: a great acceleration of finances by the Super Bowl, three
weeks after the inauguration, which pins it to 9 February 2025 (YAacmBr8JyY@663).
The Italy volcano gets quietly rewritten here (5rXtqqYsNXI@1920): relocated to near Rome,
softened to "if it goes off", and closed with "I believe we may have changed things". The
September 2023 telling had it costing hundreds of thousands of lives. Recorded as delay_claim
against italy-volcano rather than merged, so both magnitudes stay visible.
Against that, 5rXtqqYsNXI@4513 is him setting his own standard: accuracy in the prophetic
matters because it brings trust. Seeded as prophetic-accuracy-2025.
Tier 1 now past 440 of 2,477.

### oe-06, November 2024, 40 passages
The find here is 8BLqLpWThhw@1482: he prays that there be no major virus in 2025, 2026, 2027
or 2028 and that the plan to take down the dollar is averted, over exactly the years covered by
plague-350m, drought-plague-summer-2026 and digital-dollar-transition. Whichever way those
resolve, one half of his own record is contradicted. Filed as no-plague-no-dollar-collapse-prayer
and deliberately not merged into any of them.
Two more worth flagging. _NvKMga-o2I@755: the Lord tells him the Super Bowl winner in advance
and he keeps it private inside the family, so the one cleanly scoreable prediction he says he
receives is never published. And _NvKMga-o2I@254: he called the Yankees and Dodgers World Series
matchup back in May 2024, which did happen, bundled with attempted attacks on Yankee Stadium,
which did not and were prayed against.
Filenames moved to the oe- prefix: the other worker was overwriting mentions-old-NN.json.
13 new canonical claims. Tier 1 525 of 2,477 (21.2%).

### old-06, November 2024, 40 passages
Two findings worth the batch on their own.
_NvKMga-o2I@186 (4 Nov 2024) has the same October intercession producing "a small little window"
that he guesses may run only to the first of the year. Three weeks later the same mechanism is
producing four years to 2028. Recorded same_event unsure, delta_type contradiction against
reprieve-four-years, not merged.
_NvKMga-o2I@254 is the most checkable prediction in the corpus so far: he says that in May 2024
he saw the Yankees and the Dodgers going to the World Series. That is exactly the 2024 matchup.
Whether he actually said it in May is testable against the May videos and should be checked
before it scores. Alongside it, @755 says the Lord tells him Super Bowl winners in advance and
he keeps them private, which is the same information withheld from any record.
8BLqLpWThhw@1482 declares no virus or plague at all through 2028, directly against plague-350m
and drought-plague-summer-2026. Both left standing.
Filename note: the other worker also writes seeds-new.json, so batches here now use
seeds-old-NN.json. `python newseeds.py <file>` takes the path.
Tier 1 525 of 2,477 (21.2%).

### oe-07, Aug to Sept 2024, 40 passages
Note first: a 40-passage draft for Sept to Nov 2024 was written and thrown away unloaded
because the other worker took every one of those segments while it was being written. Second
time that has happened. Check overlap before writing, not after.
This batch: a grid attack warned between August and the 2024 elections (relayed from a source
whose two-week-old accuracy is the stated reason to believe it), an attempted chemical attack
on Tel Aviv, biological material out of a cave in Iran, and 3 October 2024 named as the turning
point and tipping point, then softened in the same video to "it doesn't have to be the 3rd".
Two tensions kept visible rather than resolved. K1HHLefn-5Y@2083: he endorses a viewer being
told by the Spirit not to buy gold and silver, against his own gold-10k and silver-75 counsel.
eBsTg-WimRc@277: what saves America is revival, not Trump or a new Congress, against most of
his election material. 13 new canonical claims. Tier 1 604 of 2,477 (24.4%).

### oe-08, Feb to Aug 2024, 33 passages. 2024 IS NOW COMPLETE.
`pick --tier 1 --until 2024-12-31` returns 0. 2023 and 2024 are both fully swept.
This batch has the source telling of the plague vision (ahtOXFdUWsc, 4 July 2024): airborne,
waist high, complete shutdown of society, megachurches closed and a financial melt, all in one
vision. Everything later in the plague thread refers back to it, which is why plague-350m,
megachurch-closures and the crash claims keep travelling together.
Two things that cut in his favour and should not be lost. dq4Jz74Kpfw@239: asked directly, he
says he does not believe anything will happen at the 8 April 2024 eclipse and has seen nothing
for that date. A dated, unhedged negative prediction, and it landed. And J1SsxvRRu_c@1008: he
says he warned in September 2023 that Biden would not be running, while volunteering that he
had expected it in November 2023. If that September 2023 statement is in the corpus it is the
strongest hit in the record; worth locating.
Against that, 2WZdJvTAHOc@1353 (April 2024) puts the crash firmly in 2025 with an angel as the
source, and jOUebwRZLPc@2501 six months later declares the financial storm averted. Both stand.
13 new canonical claims.

### oe-09, March 2025, 40 passages
Two genuinely scoreable dated calls: the Canadian election on 28 April 2025, prayed to be
"too big to rig" with the righteous rising up, and a greater red wave in the November 2026
midterms. Both are matters of public record and neither has evidence attached yet.
nDqOltb-P14@909 is the batch's structural find: one word ties the October extension, a great
wealth transfer restricted to "the 1% that are listening", and America being humbled into a
single sentence. The listening clause is what makes the transfer half unscoreable, and it is
the same move as go-home-early and refuse-to-participate.
Also the first concrete mark-of-the-beast material: a brain implant that rewires thinking,
offered to convicted felons instead of a prison sentence. Read from news, not seen.
13 new canonical claims. Tier 1 677 of 2,477 (27.3%).

### oe-10, Jan to Mar 2025, 40 passages. Tenth batch, so selftest and export ran.
The plague thread gets its only real timing here, at __mzf6nASoI (28 Jan 2025): starts in the
fall, a three month window into springtime, late February through May the bulk, June to August
fading. Then he says the Lord showed him the calendar counted BACKWARDS, which he had never
seen before and did not understand. That is recorded as delta_type contradiction against
plague-calendar-fall-to-spring, because the same four passages read as either a 2025-26 or a
2026-27 sequence depending on a direction he never chose. The timing cannot be pinned.
Also filed seen-early-years-out from _co9BHhQB5k@112, where he works out on air why his dates
run early: "it looks like it's going to happen right now and it's a couple years out", using
the 2020 chicken word arriving in 2025 as the worked example.

Selftest: two failures, one of them mine and now fixed.
  * Orphaned claims 12 -> 6. Eight were mine: six seeded for the batch-1 draft I discarded
    unloaded, plus america-humbled and trump-plague-address which I split out of tellings that
    bundle them. Six deleted from canonical_claim, claim_alias, validation_state and seeds.json.
    Two refused deletion by the guard because they carry superseded assignment history
    (eye-of-the-storm-2026, multi-city-distraction-unrest) and were left alone; they will pick
    up mentions as the sweep continues. Four remaining orphans are the other worker's.
  * 91 assignments left unreviewed are all method=lexical from the other worker's loads at
    21:11:54, i.e. their in-flight work. Not adjudicated here to avoid racing their reviews.
    Re-check at batch 20 and clear them if they are still open.
export_view.py rewrote prophecy-db.html (836 KB). Tier 1 717 of 2,477 (28.9%).

### oe-11, January 2025, 33 passages
Two flat self-contradictions inside single videos, both left visible.
JKPqjW92sdc: at 1960 he reasons that "many false prophets" means hundreds and tells the audience
to be on guard that they may be listening to one. At 2297, 337 seconds later, he tells anyone
who feels he is off to keep it to themselves because they will see he was right.
8muAQEFYaHA@354: a rocket ship taking off with the economy after 20 January, and in the same
breath the great economy crash that was planned. He does not reconcile them.
YA7dPUR6vRM@1656 is the fullest form of the October defence: asked whether he missed it, he says
2 Chronicles 7:14 was satisfied, the land is being healed, and scripture is being fulfilled. The
unmet event becomes the fulfilment.
Also rapture-by-2028, which is a genuinely dated rapture claim, given eleven days before
8c3OFWnOS8E@715 where he rejects other ministers' dates and says only "soon".
12 new canonical claims. Tier 1 750 of 2,477 (30.3%).

### oe-12, early January 2025, 30 passages. EVERYTHING THROUGH 2025-03-31 IS NOW COMPLETE.
`pick --tier 1 --until 2025-03-31` returns 0. 2023, 2024 and Q1 2025 all swept.
XDzPR1iLMvQ@110 is the origin of the entire reprieve structure: in October 2024 he heard the
devil petition the Lord that Adam's lease was up and the seven year tribulation had to begin,
and the reprieve is the answer to that petition. reprieve-four-years, october-grace-window,
extended-time-grant and dividing-line-shaking-2025-2028 all trace back to this passage.
o_HtP7CXqR4@128 is the counterweight to the october-nothing-burger-defence and belongs in any
fair scoring: after the New Orleans attack on 1 January, an attack he had warned about, he does
not claim it as a hit. He says "I feel we failed" and grieves.
9 new canonical claims. Tier 1 780 of 2,477 (31.5%).

### oe-13, June 2025, 31 passages
The most scoreable batch yet. A van attack warned over New York for 4 July 2025; disruption at
a strait Monday to Thursday of the week beginning 23 June, given the day after the US struck
Iran with Hormuz closure under live discussion; a crypto ruling due 15 August that goes to a
second court and could run into 2026, with Judge Torres named.
DNbjAj9RilM@1177 sets the outer bound on the whole method: a word given 20 August 2014, cited
in June 2025 as still being fulfilled. Eleven years of lead time makes almost any later event
assignable to it, and he offers that as evidence of mercy rather than as a problem.
Against that, 9epckXNXLN0@1104 is real restraint: with an Israel-Iran exchange running he is
asked whether this is Ezekiel 38 and says plainly no, only the beginning stages.
15 new canonical claims. Tier 1 811 of 2,477 (32.7%).

### oe-14, June 2025, 31 passages
Two dated prior claims worth verifying against the corpus rather than taking on trust:
VVe9S5V9pXo@0 says he called Elon Musk "a rat" on 30 October 2024, cited the week the Musk-Trump
split went public. Name, date, public outcome. But at 1114 in the same video he moves the origin
to "since January". Both recorded.
zz3aEtVV9fM@512 names Kai Trump, eighteen, whose face he says he saw specifically, inside a
14 June to 6 July window. Naming a living private individual makes it the most checkable
protection warning in the corpus.
Also stitt-brought-down: a named incumbent governor and a scheduled November 2026 race.
12 new canonical claims. Tier 1 842 of 2,477 (34.0%).

### oe-15, May to June 2025, 31 passages
r-6QgcJFlPM@1159, given 1 June 2025, says a January word showed an American missile striking a
mountain that was an underground city with Iranian deterrence around it. Three weeks before
Fordow. If the January statement is in the corpus this is the sharpest military hit in the record.
The same video at 1268 restates $200 oil with a mechanism attached (refinery strikes drive it,
the flow stimulates America). Oil fell rather than rose after June 2025, so that half is testable
and did not hold. Both are filed under oil-200-barrel as a restatement.
no-gambling-on-the-gift is the second instance of the superbowl-winner-private structure and
the more explicit one: he picked March Madness winners and was told that betting on it would end
the gift. The one class of prediction that could be independently scored is placed out of reach.
10 new canonical claims. Tier 1 873 of 2,477 (35.2%).

### oe-16, April to May 2025, 31 passages
CqifdwkJFLY@590 is the most important methodological passage found so far: he states flatly
that the prophets who said Biden would be removed and Trump restored, and everything spoken in
2020, gave FALSE prophecies and missed it. That is the standard he applies to others, and it
sits directly against grace-for-missed-words, where he asks for the opposite treatment.
CqifdwkJFLY@1577 moves the window boundary: reprieve-four-years, shmita-2028-window and
rapture-by-2028 all close at 2028; here the grace ends in 2029 and the tribulation starts there.
Recorded as delta_type contradiction against tribulation-2029, both left standing.
aNxQMI-T7qQ@2253: the 28 April Canadian election went against what he prayed, and he says so.
He does not claim the prayer changed it. Recorded as a delay_claim rather than a defence.
8 new canonical claims. Tier 1 904 of 2,477 (36.5%).

### oe-17, April 2025, 31 passages
OvEIqBmJLjo@77 is a claim verified inside the corpus rather than taken on trust: he says he told
everyone plainly that nothing would happen at the 8 April 2024 eclipse, and the prior statement
is here at dq4Jz74Kpfw@239, dated 7 April 2024, saying exactly that. A dated negative prediction
that landed, with the source located. It should count in his favour.
OvEIqBmJLjo@1170 is the strongest unverified hit claim: trade wars between China and America with
Trump leading, said to have been seen in 2023 when Trump was out of office and facing prosecution.
Worth locating that 2023 statement.
D8HTHZi98oE@34 cuts against his own interest: Francis had just died, and the wheelchair detail
would have made the Antichrist-and-pope vision a hit. He rules it out instead.
Filed window-respecified-after-miss from oyGi_fSzDDk@1359: told he got the six month window wrong,
he recounts the months after the fact rather than conceding. Distinct from the October defence.
10 new canonical claims. Tier 1 935 of 2,477 (37.7%). Two stragglers left below 2025-06-30.
### oe-18: two stragglers, everything through 2025-06-30 now complete. Tier 1 937 of 2,477 (37.8%).

### oe-19, September 2025, 31 passages
The UN week is the spine here. sheep-goat-nations-un has a claimed origin (March or April 2025),
a claimed date (23 September) and a public outcome (the recognitions), so all three halves are
checkable. tZEOxoJMC90@78 four days ahead and YzT65um6tn8@219 after the fact both attach to it.
ZRh5oXmI-xQ@7231 sees the 2026 elections flipping to a stalemate government, which sits against
red-wave-2026 given by the same person in March. He prays for one and sees the other; both stand.
3FqtRlMU1wM@2360 endorses another man's TEN year window in the same breath as the shmita cycle,
without noticing it contradicts his own four year one. Filed as ten-year-window-borrowed.
fifty-gallon-drums-attack is the most severe domestic claim in the corpus: an attack worse than
11 September 2001, prayed against as it is stated.
10 new canonical claims. Tier 1 968 of 2,477 (39.1%).

### oe-20, September 2025, 30 passages, plus a full integrity cleanup. SELFTEST NOW ALL GREEN.
Batch content: five-major-shakings (earth, heavens, political, finances, church) supersedes the
loose shaking language elsewhere by enumerating the domains. america-divides-three-days puts a
three day fuse on a specific political act, and he notes he was NOT given the same warning about
Canada, which had already recognised. ZFwv_xijl7Q@6778 is a restraint worth keeping: offered
wormwood and poisoned water in conversation, he says plainly he did not see it.

Integrity work, all of it now passing:
  * A review aborted on a FOREIGN KEY error because reviews-oe-20 referenced
    global-shakings-awakening, which I had deleted in the batch-10 orphan cleanup. Restored it,
    since it now has a mention to carry.
  * The 91 unreviewed assignments were still open from batch 10, so they were adjudicated from
    each mention's claim_text (reviews-cleanup-91.json), accepting the lexical suggestion where
    it held and overriding where it plainly did not: the helicopter pad aside was matched to
    second-virus-lockdown, an American Airlines ground stop to tsa-thanksgiving-attack, a
    Jericho march to new-anointed-faces-2025.
  * 16 of those would not clear, because `review` resolves a (video_id, start_s) to the newest
    mention only and both workers had extracted the same segments. Added mirror_dupes.py, which
    copies the reviewed sibling's adjudication onto the duplicate rather than inventing a second
    opinion, and supersedes the lexical row so the guess stays auditable.
  * Orphaned claims 6 -> 0. Five were resolved by moving a mention whose current claim keeps
    others. The last, multi-city-distraction-unrest, is a pure duplicate slug; since that passage
    was extracted twice, one extraction is now filed under each twin.
  * Six duplicate claim pairs recorded as same_event_as edges with asserted_by=system
    (relationships-dupes.json). Two workers seeding independently produced twinned slugs:
    hoover-dam-2025 / dam-wall-ireland-2025 / ireland-land-event, words-are-seeds /
    words-as-living-seeds, two-state-solution-2024 / two-state-third-temple,
    multi-city-distraction-unrest / multi-city-simultaneous,
    january6-repeat-distraction / distraction-events-jan6.
Tier 1 998 of 2,477 (40.3%). Past-due claims with no evidence: 118.

### oe-21, Aug to Sept 2025, 30 passages
Located oBpaSk7EJGE, the "Glimpse Into 2026" video he points back to later. Its 24 hour change
finally gets a month here (September 2025), which makes everything-changes-24-hours scoreable
for the first time, and it is also where he redirects the September rapture expectation into
something else.
The window keeps moving and all versions are now on the record. Four years (Dec 2024), three
years (0qDOz_f0xhk@346, Aug 2025), boundary at 2028, at 2029 (CqifdwkJFLY@1577), and at 2032
(LFTGvfFA6vE@2134, where he says he could be wrong). Filed three-year-window as its own claim and
marked the 2032 telling delta_type contradiction so the shrinkage is visible rather than smoothed.
0qDOz_f0xhk@1056 is the clearest account anywhere of the mechanism behind every dated claim here:
going up prophetically he sees a line dividing each year and can look into each one and name it.
8 new canonical claims. Tier 1 1,028 of 2,477 (41.5%).

### oe-22, August 2025, 29 passages
WjzHte1MzLA@1767 is the second clean negative prediction in the record, after the April 2024
eclipse: asked directly about a widely expected September 2025 rapture, he says plainly he does
not believe it is coming then and expects a harvest instead. It landed. Filed as
rapture-not-september-2025 so it can be weighed alongside eclipse-april-8-nothing.
Two things that cut the other way in the same batch. WjzHte1MzLA@1312 presents Trump's 23
September UN address as "not a coincidence" when it was already on the calendar. And
u5z9li0Tli4@739 pre-explains dryness in the church as not counting against the outpouring, which
is the same move as being not moved by what you see.
israel-blessing-curse-earthquakes gives the sheep and goats division a physical consequence
(earthquakes in the countries that did not stand), which makes it checkable where the UN version
is not. 7 new canonical claims. Tier 1 1,057 of 2,477 (42.7%).

### oe-23, Jul to Aug 2025, 29 passages
rLELZkqyJEQ@548 is the general licence, given in answer to his own pastor asking whether a
vision can be delayed: "we always can pray into something and stop something". Every
prayer_may_prevent claim in this database rests on that sentence. Filed as prayer-can-stop-it.
Two passages show the September sign-stack being assembled from news rather than seen:
rLELZkqyJEQ@578 ("I didn't even know there was an eclipse, but I found out") and gt4gZKcM2ok@1766,
where the 23 September UN date arrives in a viewer's letter. gt4gZKcM2ok@1815 then runs it on
numerology: the seventh, the number seven, 7-Eleven, the 23rd.
first-freeze-marker is an unusual anchor: not a date but a seasonal event that falls differently
by location, and he underlines that by asking when the viewer's own first freeze is.
8 new canonical claims. Tier 1 1,086 of 2,477 (43.8%).

### oe-24, July 2025, 28 passages. Tier 1 crossed 45%.
xUTlHLlBy_g@1997 completes the licence begun at rLELZkqyJEQ@548: what could not be prayed off was
unstoppable anyway, and it need not touch the believer. Between those two passages no outcome can
count against a warning. Both filed under prayer-can-stop-it.
qkyOlKNbbRM@238 is the same structure applied to evidence: ring of fire tremors are offered as
possibly relieving pressure on the Oregon volcano, so seismic activity and seismic quiet both
confirm the word.
Scoreable items: october-31-baseball-darkness (31 October 2025 is World Series week, and the same
baseball image preceded the 2024 Yankees call), price-floor-standard (a floor far above forty
cents, unnamed but pointing at XRP), and corn-kernels-november, which he offers uninterpreted.
x89DNpfd8jI@549 is worth the record for tone: he tells his own audience the sky is not falling.
10 new canonical claims. Tier 1 1,114 of 2,477 (45.0%).

### oe-25, July 2025, 27 passages
BW7DXgEMZHM@1236 is the most specific version of the plague thread anywhere: he corrects himself
on air to make clear it is 2027 and not 2025, and adds China, rats and a European origin. That
matches the bubonic framing at kB0D3FLQzjY@930 and cuts against the airborne AI framing at
2JeWign9G7Y@434. Both remain on the record.
BW7DXgEMZHM@1632 supplies the theological engine for every extension: if he came back now,
billions would go to hell, so a harvest has to come first. Filed as billions-to-hell-if-now
beside extended-time-grant and reprieve-four-years.
guthrie-antichrist-temple names a town and a distance, which makes it one of the few locatable
claims here. binary-system-earth is unusually falsifiable: a second solar companion is excluded
by current astronomy.
8 new canonical claims. Tier 1 1,141 of 2,477 (46.1%).

### oe-26, early July 2025, 26 passages. EVERYTHING THROUGH 2025-09-30 IS NOW COMPLETE.
`pick --tier 1 --until 2025-09-30` returns 0. 2023, 2024 and Jan-Sep 2025 all swept.
uOv6toXL4Uk@1788 states the shrinkage in one sentence: "what are you going to do with this three
years I've given you? Three and a half years, four years back then." Recorded as delta_type
contradiction against three-year-window rather than smoothed into reprieve-four-years.
tLTlKY5L8O4@556 is a method worth noting: he deliberately declines to hang the Pearl Harbor
warning on the obvious date, saying it comes when you are not expecting it. That is honest about
surprise and also removes any date it could be scored against.
7 new canonical claims. Tier 1 1,167 of 2,477 (47.1%).

## Partition note update, 30 August 2026
The newest-first worker has stopped. Its last load was at 21:11; everything since is from this
sweep. The date partition is therefore retired: all 1,322 remaining tier-1 passages
(Oct 2025 through Jul 2026) belong to this worker. Continuing oldest-first without a ceiling
beyond the working window.
Remaining by month at handover: 2025-10 101, 2025-11 148, 2025-12 195, 2026-01 121, 2026-02 101,
2026-03 139, 2026-04 153, 2026-05 126, 2026-06 142, 2026-07 96.

### oe-27, late October 2025, 26 passages
oct31-flip-prayer is the sharpest conditional in the corpus: a named race, a named night, a
stated mechanism ("if you push into that right now in the late midnight hour on October 31st, we
could get this flipped"). The 4 November New York result is public record and the prayer
condition is what will absorb it.
Vlo4XIRCeIM@1517 is worth preserving exactly as it happened: he goes to produce a prior clip
about LeBron being dethroned to set against the betting investigation, and it was not saved. The
claimed hit cannot be shown, and he says so on air.
TeakZx4yRog@5968 supplies pieces-at-a-time, his stated explanation for why the material arrives
fragmentary and never resolves into a whole picture. Filed as a method claim.
8 new canonical claims. Tier 1 1,193 of 2,477 (48.2%).

### oe-28, late October 2025, 26 passages
h5AFOcz8eI4@6287 is the clearest statement in the corpus of why the healing claims cannot be
scored: "you're still coughing, your throat was sore — well, I'm still healed." Symptoms are
ruled inadmissible in advance. Filed as symptoms-do-not-count.
Vlo4XIRCeIM@1940 is the whole pattern in miniature: martial law in the cities, dated to Saturday,
and prayed off in the same sentence.
Two restraints on the other side. Vlo4XIRCeIM@2950: "you're hearing in part, you don't know
timing of things... I'm just human." And Vlo4XIRCeIM@8740, where he withholds the great deception
material because he does not understand it yet and does not want to bring it out wrongly.
Ig9o0wN-vJU@4098 is unusually scoreable: completely debt free by the end of 2025, nine weeks.
6 new canonical claims. Tier 1 1,219 of 2,477 (49.2%).

### oe-29, October 2025, 25 passages. TIER 1 PASSED 50%.
Two passages two days apart, both kept: UM1Mdfw3f7Y@1986 warns against assuming they will
"steamroll this and have a red wave"; JJiG596K_R0@2914 prays for the largest red wave in the
history of the country. Recorded as delta_type contradiction against red-wave-2026.
UM1Mdfw3f7Y@1899 is the move that retires the whole shaking thread without ever scoring it:
"no longer coming, it's here." Filed as shaking-is-here-now.
Rj3MzUel5OA@2092 gives his own standard for a miss: "I hear in part, see in part. If I see
something and it don't come to pass, I did my best." That belongs directly beside
false-prophecies-2020-admitted, where he calls other people's unmet 2020 words false prophecies.
JJiG596K_R0@3483 is him answering an audience that is already asking why the earthquakes have
not arrived. The answer is that it is only early October.
6 new canonical claims. Tier 1 1,244 of 2,477 (50.2%).

### oe-30, October 2025, 24 passages. OCTOBER 2025 COMPLETE. Selftest ALL CHECKS PASS.
RYFAcRrLZNg@2530 is the cleanest self-correction in the corpus: told to watch Australia, he
reports that nothing happened, that what he saw was peaceful, and invites Australians to tell him
he was wrong. Three days later at I3CfQxKRd30@166 he reads Australian protests as the
confirmation. Both passages are filed under watch-australia and both stand.
miami-hurricane-katrina-scale is genuinely scoreable and did not happen: a named city, a named
scale (Katrina), and a window (end of September 2025) that has passed.
fZds8I9yXIY@1640 shows how the September acceleration gets evidenced: with the Canadian firearm
buyback and the EU entry-exit system, both announced independently of anything he said.
8 new canonical claims. Tier 1 1,268 of 2,477 (51.2%).

NOTE: past-due claims with no evidence recorded is now 153 and climbing. Extraction to 100% is
the stated stopping condition, so it stays the critical path; the evidence pass follows it.

### oe-31, late November 2025, 25 passages, 16 new claims. Tier 1: 1293 / 2477 (52.2%).
Videos uIWzg7u1QFo, v3A9UyHZAhw, GJwNDkJKR1w, Wg_zympTrLE, u_fT7KW6hXA. The densest dated
batch in a while: 1 Corinthians 5:5 named as the scripture over 2026 with impeachment and the
judges attached, a circled 13 April worked out afterwards to be Holocaust Remembrance Day with
no content given, an attack benchmarked as worse than 7 October, and drones bought from a
retailer and detonated into European tree lightings, parades and New Year's Eve inside a
six-week window. That last is the most falsifiable thing recorded in thirty batches.
Two things worth flagging. He raises the base-rate objection to his own unusual-winter claim,
that every winter has cold fronts and Siberian air, and then repeats the claim without meeting
it. And at 4408 the camera lens is the clearest account yet of how dates get assigned: he zooms
until something resolves rather than being told a date, which belongs with prophetic-method-in-part.
Two same_event_as edges asserted_by system, not brandon: january-17-word-fulfilling to
four-inch-rain-sign, snake-figure-by-2028 to judas-betrayal-trump. Both are suspicions of
identity that he does not state, so the claims stay separate and visible.
One review at GJwNDkJKR1w@5672 is delta_type no_claim: he plays a presidential address about a
real attack in Washington. Not his words, and he does not claim the capital sight predicted it,
so nothing is scored from it.
Past-due claims with no evidence now 156, unlinked strong fulfilment assertions 793. Extraction
to 100% remains the stated stopping condition and the critical path; the evidence pass follows.

### oe-32, 22-25 November 2025, 21 passages, 11 new claims. Tier 1: 1314 / 2477 (53.0%).
Videos u_fT7KW6hXA, X8damyf6idc, SZg5NjLFZVE. Two claims in this batch matter more than the rest
of the batch put together.
X8damyf6idc@7617: "I don't see a vision as a prophecy." He says a vision is a means to change
things through prayer. That is the frame under every prayer_may_prevent field in this database,
and it converts every unfulfilled sight into a successful intercession. Seeded as
vision-is-a-prayer-target.
SZg5NjLFZVE@9826: the December outline is right "every single time", "always the major things".
Seeded as track-record-always-right, which is the claim this whole database exists to test. A
single failed prior outline disconfirms it, and the outlines are themselves in this corpus.
Alongside it, year-mapped-each-december says the outline arrives at the end of December. That is
checkable from inside the corpus, so it gets revisited when the sweep reaches December 2025.
u_fT7KW6hXA@5841 is the rare commitment: he names 4 July 2026, the 250th anniversary, and rules
it out. Seeded as not-the-obvious-date. An attack on that date would contradict him, which makes
it one of the few things here that can fail. He pairs it with the black swan, so the edge to
black-swan-event is asserted_by brandon with u_fT7KW6hXA@5785 as the naming evidence; relate
refused it once for lacking that, correctly.
Also: @5645 attaches Easter to 13 April, but Easter Sunday 2026 falls on 5 April, so the two do
not coincide. 1 Corinthians 5:5 is aimed at ministers here, three days before he aims it at
politicians, which is narrower and recorded as an elaboration rather than smoothed over.
One system edge: attack-worse-than-october-7 to israel-night-attack, four days apart with the
same benchmark and motive and no timing in either.

### oe-33, 14-20 November 2025, 29 passages, 20 new claims. Tier 1: 1343 / 2477 (54.2%).
Videos Ez7SesrR7vs, _FhdsJ8jhsU, 3-UAs7VAr4Y, Ah32W7YNalk, Bv_BgO_L8lk.
Bv_BgO_L8lk@994 is the one to remember. He says he saw Harvard spelled out in bricks, then says
the man went to Yale, not Harvard, and leaves the mismatch standing instead of reworking the
sight to fit. That is the opposite of the post-hoc fitting the rest of the corpus runs on, and
it belongs in any fair account of his method. Seeded as harvard-bricks-vision.
3-UAs7VAr4Y@3584 is the mirror image: he corrects listeners who thought he had predicted a
plague now, and narrows it to the fall or winter of 2027. Recorded as a timing_update on
plague-2027-china-rats-europe rather than smoothed into the claim, which is what delta rows are
for. The window now runs 2027-09-01 to 2028-02-29.
Four exact_repeat rows: 3-UAs7VAr4Y replays the whole 19 November prayer segment from
_FhdsJ8jhsU. Extracted rather than skipped so the repeat count stays honest.
canopy-restored took 3-UAs7VAr4Y@1929 rather than dispensation-ending, which is already well
attested; the link between them is a brandon-asserted evidence_for edge with that passage as
evidence, since he states it. Seeding a claim and then giving it no mention would have left an
orphan, which selftest catches; caught it before running review, not after.
Bv_BgO_L8lk@929: Marilyn Monroe, Monica Lewinsky, remember JFK, given as what will manifest
concerning JD Vance. Three names and nothing else. The paraphrase says the pattern is implied
and left unstated, because he does not spell it out and it is not mine to spell out for him.
Also new: std-judgment-child-abusers, red-dawn-experiences (named, never defined),
cold-war-gets-colder (which cold war is not said), no-prophetic-confusion, which is his own
stated standard and the yardstick this database is in a position to apply.
Next selftest and export due at batch 40.

### oe-34, 7-14 November 2025, 26 passages, 17 new claims. Tier 1: 1369 / 2477 (55.3%).
Videos Bv_BgO_L8lk, NliWml7zW00, Iug2hksEpUo, OYjIqPs-2-A, DsQ91ct1riM, wP9qZYC_Cv4.
Iug2hksEpUo@5728 is the strongest form he uses anywhere: not that the January budget will be
fixed but that it "is done, it's not been announced yet". No prayer clause, no hedge. It can
fail cleanly, which almost nothing else in this corpus can. Seeded as budget-fixed-january-2026.
Iug2hksEpUo@1081 is the other clean one, in the opposite direction: he rules out a crash in
2025 and says twice that it is his opinion. Recorded as certainty hedged, and the call held.
Two timing rows that disagree with each other, six days apart, both left standing.
3-UAs7VAr4Y@3584 (batch 33) narrows the plague to fall/winter 2027; Iug2hksEpUo@3176 widens it
back to "November and December of a year", praying into 2027 and 2028 and January. Both are
timing_update rows on plague-calendar-fall-to-spring and neither was smoothed into the other.
NliWml7zW00@647 keeps its own confusion: the ninety days is argued down to forty and back up to
ninety inside the passage, and ninety days from 13 November is 11 February, not the 4th of July
he matches it to. The arithmetic gap is in the falsify_miss field, not corrected away.
Bv_BgO_L8lk@7123 names February 3rd for the Olympics. The Milan Cortina opening ceremony is
6 February, which is recorded in the mention rather than treated as a match in advance.
darker-and-lighter-two-sided is worth naming plainly: good news is the light increasing, bad
news is the darkness deepening, and both were forecast. With vision-is-a-prayer-target and
calling-things-that-be-not, that is three separate structures each of which makes a miss
impossible. A system edge now links the last two.
Also recorded: burden-of-seeing, from Iug2hksEpUo@6196, where he says he may not be doing as
well as he thinks he is. A fair account of this corpus includes the unguarded moments too.

### oe-35, 5-7 November 2025, 26 passages, 15 new claims. Tier 1: 1392 / 2477 (56.2%).
Videos wP9qZYC_Cv4, UfXV5KCRNn0, btBCeTHs7Qg. The 6 November session is the densest single
sitting in the corpus so far and most of the batch comes from it.
storm-worse-than-covid is the biggest claim recorded to date and, unusually, it has a window:
2027 to 2028, beyond anybody's comprehension, "make COVID look like a walk in the park". Three
mentions build it (@7395 in tongues, @8086 the mechanism, @8137 the benchmark). It can come due.
year-2032-highlighted collects four mentions and claims nothing: he sees the number, says he
does not know why, skips from 2028 to 2032 with the years between unseen, hits a black line, and
reports clouds. The falsify fields say plainly that a gap in what he saw is not a claim about
the world.
Two moves worth naming next to each other.
extended-time-grant (wP9qZYC_Cv4@871): prayer earned more time, so the collapse that did not
arrive is deferred rather than wrong. wilkerson-new-york-fires (UfXV5KCRNn0@8996) applies the
same move to somebody else's word: a prophecy that has not landed since 1973 is taken up and the
fifty year gap attributed to delay.
And the restraint, which is real and belongs on the record: UfXV5KCRNn0@7870, a football stadium
and possibly a tornado, and he explicitly declines the Super Bowl reading because he saw nothing
indicating the NFL. That is the second such refusal in three batches, after harvard-bricks-vision.
One contradiction edge recorded, not reconciled: wP9qZYC_Cv4@2035 says the rapture may be twenty
years off and nobody knows, against rapture-by-2028 and rapture-hope-2028. He holds both without
noting the conflict.
four-more-sim-card-sites is a rare countable claim: four other American sites like the New York
and New Jersey seizure. It can be checked and it can fail. Recorded as an extrapolation forward
from a widely covered September news event, which is what it is.
btBCeTHs7Qg@40 says he saw the outcome of the 2026 election and does not say what it was. Left
that way rather than filled in from red-wave-2026.

### oe-36, 3-5 November 2025, 21 passages, 14 new claims. NOVEMBER 2025 COMPLETE.
Tier 1: 1413 / 2477 (57.0%). Videos btBCeTHs7Qg, vxOD_LJfF1Q, QuWUXW1Iq8E, SDUTBdo_u6k.
SDUTBdo_u6k@1397 is the one that matters and it is past due. He says the word was "watch from
the 23rd on of September, September will be a month to remember", and offers Charlie Kirk going
home as the fulfilment. That killing was on 10 September, thirteen days before the window he
says he was given. Recorded in falsify_miss and seeded as september-month-to-remember; it goes
to the evidence pass with a real date to check against, not resolved here.
The Olympics date is wrong twice, and both tellings now carry it. vxOD_LJfF1Q@531 builds a three
month window on "February the 3rd of 2026. That's when the Olympics starts"; Milan Cortina opens
on the 6th. SDUTBdo_u6k@3455 says three months, counts the months out loud and corrects himself
to four. Both corrections and both errors are in the mentions rather than tidied away.
SDUTBdo_u6k@6360 is the pattern worth naming: he raises December 31st, withdraws it in the same
breath on the see-in-part clause, then prays over Times Square. The date is placed in the
audience's mind and the responsibility for it is set down at once.
vxOD_LJfF1Q@902 is the honest version of the revival claim: "it may be three years, it may be
tomorrow, I don't know." Set against the tellings that give the same revival a year.
QuWUXW1Iq8E@792 restates stalemate-government-2026 in the same week as red-wave-2026, pointing
the other way. Both stay visible.
NEXT: December 2025 (195 passages), the largest remaining month. Also the month
year-mapped-each-december says the 2026 outline arrives in, which is checkable from inside the
corpus. Selftest and export due at batch 40.

### oe-37, 28-31 December 2025, 30 passages, 17 new claims. Tier 1: 1443 / 2477 (58.3%).
Videos 0jRKxZJW2x4, e8RJHBLAGf4, N2MEJej9ziY, ULb5iK3ua_c, YVw8Z6XsQVg. December opened.
red-dawn-experiences finally has content. Seeded empty in batch 33 because he named it and never
defined it; 0jRKxZJW2x4@1304 defines it as China moving on Taiwan while America is absorbed in
its own crisis, which is also where the phrase comes from. Recorded as an elaboration and a
brandon-asserted same_event_as edge to taiwan-two-day-fall, evidenced at that passage.
The very next passage, @1357, says Taiwan is taken "within three days" where the existing claim
says two. Small, but it is the only precise part of the claim, so it went in as delta_type
contradiction rather than being rounded into agreement.
The plague now sits in four different windows across five weeks: fall 2027 (3-UAs7VAr4Y@3584),
November-December of an unspecified year (Iug2hksEpUo@3176), 2027 and 2028 (UfXV5KCRNn0@8137),
and now 2026 (0jRKxZJW2x4@904). All four tellings are live timing_update rows on the same claim.
e8RJHBLAGf4@311 is a self-attested hit with both halves checkable: he says what was shown on
11 December is coming to pass, and 11 December is inside this corpus. Flagged for the evidence
pass; the original telling gets read against this recall when the sweep reaches that date.
N2MEJej9ziY@3066 is the most measurable claim in weeks: precious metals higher than ever before
and crypto up like a rocket, inside 2026. Checkable to the dollar. It sits in the same session as
economy-is-a-catfish, where the economy is in trouble and overstated. Both stay; a system edge
marks the tension rather than resolving it.
"Set in stone" (e8RJHBLAGf4@1752) is the strongest certainty language in the corpus and it is
attached to the least specific content available: an unnamed figure, a black cloak, a number and
a year.
Two more unlosable ones recorded as such: america-will-remain and no-sickness-into-2026.
Next batch is 38. Selftest and export due at 40.

### oe-38, 22-26 December 2025, 30 passages, 15 new claims. Tier 1: 1473 / 2477 (59.5%).
Videos KiVLKwrgsp4, iOfsrFglC9E, rRe0E21ryu0.
rRe0E21ryu0@717 is the best scoring case in the corpus so far. He said 150, the record came in at
144, and he says on camera that it is "a little off but it's the same thing". For a wind speed
that is a fair call and it is the kind of near-miss that usually gets rounded into a hit. He does
not round it. @751 dates the original word to 22 February 2024, which puts it inside this corpus,
so record-wind-gusts is verifiable at both ends. That is rare enough to be worth stating.
Two more self-attested hits with both halves checkable from durable state: long-track-tornadoes-
norm (Wyoming, said called in 2024 and manifested end of 2025) and checkered-hat-uprising-dec6,
where they look up their own record on camera and land on 6 December. Both go to the evidence pass.
The plague moved again. KiVLKwrgsp4@3608 now has it released in Europe and affecting Europe
first, delivered "with rats through AI technology". The claim previously had it coming from
China. Recorded as new_detail rather than contradiction because he does not withdraw the China
origin, he just stops repeating it. The AI delivery mechanism is new and unexplained.
Three standing reasons the claims stay away from anywhere that would test them are now all on
file and edge-linked: not-following-liberal-schools (@1517), where-prophets-go-to-die (batch 37),
supernatural-hard-to-convey (batch 34).
One contradiction left standing: household-wont-taste-death (@2626, "we are the last generation
that will not taste death") against rapture-any-time from 7 November, and it sits two minutes
after saying many of the elders will go home. The awkwardness is in the review note, not smoothed.
elders-passing-of-the-baton cannot miss and is recorded as such: prominent elderly ministers die
every year, and "even more" than last year is not a number.
Batch 39 next, then selftest and export at 40.

### oe-39, 18-22 December 2025, 30 passages, 20 new claims. Tier 1: 1503 / 2477 (60.7%).
Videos rRe0E21ryu0, 4a472es4lSg, bvxPloP7Nys. Past the 60% mark.
Three things in this batch cut against the pattern and all three are recorded as such.
rRe0E21ryu0@4520: "Symptoms come and people die. I understand that. I've seen it." He concedes
the healing teaching does not always hold and names his own daughter as the case he is walking
out. Filed as an elaboration on symptoms-do-not-count so it sits directly beside the
declarations rather than being filtered out of them.
4a472es4lSg@1477: a negative call, and a costly one. His own audience tells him the rapture comes
in 2026 and he answers "I pray you're right. But I believe you're wrong." Seeded as
rapture-not-2026. It can fail, and disagreeing with your listeners costs something.
4a472es4lSg@1623 and bvxPloP7Nys@6014: still-learning-fire-hydrant and lot-of-work-2026, both
unguarded. The hydrant line is genuine humility and a usable excuse at once, and the falsify
field says both.
Against that, expect-the-unexpected (bvxPloP7Nys@5115) is the most load-bearing method claim
since vision-is-a-prayer-target. It releases every named date in advance: a quiet date was
expected, an event elsewhere was the unexpected. He then uses it in the same session, at @5173,
to move the New Orleans target off New Year's Eve and onto the Sugar Bowl on 1 January. Second
shift in that thread. A same_event_as edge links it to not-the-obvious-date; it is one rule
stated twice.
The New Orleans target has an obvious prompt and it is in the mention rather than left implied:
a real attack there on 1 January 2025, a year before.
utah-temple-attack is one of the most specific targets in the corpus, a named building in a
named city, and it carries no date. targeted-rate-2-percent is one of the few with a number.
One contradiction edge: north-korea-before-return, a precondition pushing the return further
out, said three days after household-wont-taste-death.
BATCH 40 NEXT: selftest.py, export_view.py, re-check todo.

### oe-40, 15-17 December 2025, 30 passages, 10 new claims. Tier 1: 1533 / 2477 (61.9%).
Videos LmS3IDri3Ok, odkjS3oGxxI.
BATCH 40 CHECKPOINT: `python selftest.py` -> ALL CHECKS PASS (all integrity checks green:
no double assignments, no duplicate mentions, no orphaned claim, no brandon-asserted edge without
evidence, nothing left unreviewed, no verdict overwritten). `python export_view.py` ->
prophecy-db.html, 1561 KB.
odkjS3oGxxI@1420 is the most consequential line in the batch and possibly the month. The
financial wealth transfer he has spent a year praying for is given its purpose: it is "for the
Antichrist to rise up out of the Middle East". He says he found that interesting and moves on.
Recorded as stated, with a brandon-asserted edge from wealth-transfer-window to
beast-system-foundation, evidenced at that passage. Same session, @6935, calls crypto part of
the beast system and says to ride the wave in the same breath.
The plague window moved a fifth time in six weeks: @3508 now gives November and December 2027,
the tightest yet, contradicting the 2026 placement of 31 December. @4895 names the pathogen for
the first time, Yersinia pestis, and in the same breath says he does not know how it was done.
@4936 gives a clock and the months January, February, March, with the year explicitly withheld;
filed as its own claim and linked, not folded into the plague window, because merging would
invent a date he did not give.
February 3rd now carries a third unrelated thing (the budget), after the Olympics opening and
Pope Leo. The accumulation is the finding, so a system edge records it. It also contradicts
budget-fixed-january-2026 from 12 November, where the budget was already done and merely
unannounced; that edge is recorded too.
Fourth named venue in six weeks with no act and no date: Disneyland, after Atlanta Airport,
Queensland and Times Square.
LmS3IDri3Ok@619: he says a minister who thinks his personal life does not matter because the
word stands by itself is in "such a dangerous place to be". That is close to the standard this
database applies to him, in his own words.

### oe-41, 10-15 December 2025, 30 passages, 21 new claims. Tier 1: 1563 / 2477 (63.1%).
Videos odkjS3oGxxI, EuT30KAAFvY, pge3uihwmF8, gT0WiYgbPOc.
pge3uihwmF8@1598 is the best-specified fulfilment claim in weeks. He says he saw the Pope
getting involved with Zelensky and influencing decisions over Ukraine and Russia, gives the
origin date as 6 July 2025, and says "It happened today" on 11 December. Both halves are
checkable and the first is inside this corpus. Seeded as pope-influencing-ukraine-july6 and
flagged for the evidence pass.
February 3rd now carries four unrelated things: the Olympics opening (wrong, they open on the
6th), Pope Leo, the budget, and now three judges plus major decisions concerning Europe. He ties
the three judges to the date by way of the number three and says so himself, so the mention
records the link as numerological rather than dressing it up.
judges-excel-or-derail is worth naming: excel or derail exhausts the possibilities between them,
so no judicial outcome in 2026 can count against it. Recorded unfalsifiable on structure.
Two edges recording where the standard moves with the subject. baby-christians-grace (11 Dec)
excuses a public figure's language as immaturity; mega-minister-conversation (17 Dec) says a
minister who separates his personal life from his message is "in such a dangerous place". A
contradicts edge holds both. And many-hands-light-work joins lose-midterm-without-prayer and
vision-is-a-prayer-target: attendance is folded into the mechanism, so a miss lands on the
audience.
Third borrowed prophecy: Prophet Kim, 22 February 2014, after David Wilkerson and Rick Renner.
Whether the 2014 word says what he says it says is checkable outside this corpus.
zelensky-taken-out-ukraine-split leaves "taken out" ambiguous between removed from office and
killed. The mention says so rather than choosing.

### oe-42, 3-10 December 2025, 30 passages, 15 new claims. Tier 1: 1593 / 2477 (64.3%).
Videos gT0WiYgbPOc, gnjfH_Wc1t4, otQep0gAmZs, 6FuJNWZeXj8, AavhsLoMcgQ, aiP1Op78hE8, UnQMJN0Ia7g.
aiP1Op78hE8@1437 is one of the cleanest testable claims in the corpus: Jerome Powell out in
January, then they pump the economy. Powell's term as chair runs to May 2026, which is public,
so January is a real commitment against a known date. He marks the whole thing as his opinion
and that marking is preserved in the certainty field. It also contradicts UnQMJN0Ia7g@804 from
four days earlier, "watch May concerning interest rates", which lands on the month his term
actually ends. A contradicts edge holds both.
Second contradiction in the same batch, eight days apart. gnjfH_Wc1t4@955: 2026 "is not going to
be" about the gold, the glory and the girls. LmS3IDri3Ok@5084 (batch 40): those are exactly why
ministers lose their life or platform in 2026. Edge recorded, neither reconciled.
gnjfH_Wc1t4@793 is the plainest statement of the in-part clause anywhere: "I hear in part see in
part and it's all a puzzle to me." Candid, and it also means nothing said can be held to a
meaning afterwards.
Two restraints worth crediting, both his own: @278 says he knows the three going down the
mountain is symbolic and declines to say of what; aiP1Op78hE8@2330 narrows the motherboard image
to heat rather than fire.
AavhsLoMcgQ@888 quietly reshapes an old claim: the twenty four hour period in which everything
changes is now "already happening" and ongoing. A sharp claim becomes an open-ended one.
Fifth named venue with no act and no date: the Magic Kingdom, five days after Disneyland.
monaco-trafficking is an unevidenced criminal accusation against a named place, recorded because
he said it, with his own uncertainty about the name left in the mention.

### oe-43, 1-3 December 2025, 15 passages, 9 new claims. DECEMBER 2025 COMPLETE.
Videos UnQMJN0Ia7g, S71ffr0WDtg. December was the largest remaining month at 195 passages and it
took batches 37 through 43.
Two claims here are more checkable than most of what surrounds them, and both are recorded as
such. UnQMJN0Ia7g@1802: "There is no plan B", the Supreme Court justice must coincide with the
president, this is life and death for the dollar, failure means a great depression. That is the
strongest conditional language in the corpus attached to a real pending matter with a real
consequence. And S71ffr0WDtg@1830 finally names a city for the SIM card sites: Chicago. A count
becomes a location.
S71ffr0WDtg@6706 is the second negative call in a month: he says as much as his heart wants the
return in 2028, what he just saw says otherwise. After rapture-not-2026 on 20 November. Both
push back on dates his own audience holds, and both can fail. Contradiction edge to
rapture-by-2028 recorded.
The plague timing was restated a sixth time in five weeks (fall 2027 into 2028, November and
December, this year explicitly excluded). Across the set the windows now span 2026 to 2028 and
every one of them is a live timing_update row on the same claim.
UnQMJN0Ia7g@4072 gives the revival material a benchmark it has never had: bigger than Brownsville
and bigger than Azusa Street. Seeded as revival-bigger-than-azusa and edge-linked to
greatest-harvest-of-souls.
S71ffr0WDtg@7475 moves May's motive from interest rates to the midterms, two days before putting
the Fed chair's departure in January instead. Both stay; the contradiction edge is already in.
NEXT: January 2026 (121 passages). Selftest and export due at batch 50.

### oe-44, 24-31 January 2026, 30 passages, 15 new claims. Tier 1: 1638 / 2477 (66.1%).
Videos FuY2YBTPW2w, meR7v1cmzBI, -_dbVTpbFIs, utf0ZMPboz4. January 2026 opened.
Two passages here matter more than the rest of the batch.
FuY2YBTPW2w@2210 is an admitted miss with a real outcome behind it. A woman was highlighted to
him to pray over; he asks "Did she make it? No, she didn't" and says "I believe it was a miss",
marking it as his own opinion. That is a conceded failure, not a timing adjustment, and it is
seeded as its own claim and edge-linked to timing-misses-admission and
false-prophecies-2020-admitted.
meR7v1cmzBI@339 is the most specific electoral call in the corpus: barely keep the House, lose
the Senate. He names the red wave everybody believes is coming and denies it in the same breath,
so the contradicts edge to red-wave-2026 is asserted_by brandon with that passage as evidence.
It can fail cleanly in November.
FuY2YBTPW2w@3081 and utf0ZMPboz4@4384 are the structural counterpart to the plague material:
Psalm 91 applied so the audience is "only a spectator" while the 350 million fall around them.
System edge to plague-350m records what that exemption does.
FuY2YBTPW2w@2094 names the device that absorbs a timing miss: he wonders whether they released it
early, since he saw more time to prepare. An event off schedule becomes an early release rather
than an error.
Corrections and narrowings worth crediting, all his own. @1878 widens the 350 million across the
Americas, which lowers the implied rate anywhere. -_dbVTpbFIs@427 narrows the currency claim: a
financial border, with the physical borders remaining. @8595 corrects the Olympics start to the
following Friday, 6 February, which is right, though the third stays the prayer date.
-_dbVTpbFIs@1281 is unusually self-aware: anyone standing in 2020, or 2000, would have read
their moment as the last days. He notices it and does not apply it to his own.
February 3rd now carries six unrelated things. utf0ZMPboz4@4165 puts real distance between him
and the political figure he otherwise promotes: only Jesus saves America, and men get big headed.

### oe-45, 13-24 January 2026, 29 passages, 19 new claims. Tier 1: 1667 / 2477 (67.3%).
Videos utf0ZMPboz4, IDqls4w0LXc, CBpKNYPCKgA, SZttUyrnsRQ, LmxIp6r1zmw, hL9Trl2qb9k.
IDqls4w0LXc@184 is the strongest form of self-check in the corpus and it should be credited:
he plays the 11 November recording on air rather than paraphrasing it, so the audience hears
the original word about the ice storm. Seeded as ice-storm-november-11-word; both the recording
and the weather are checkable, and the recording is inside this corpus.
hL9Trl2qb9k@2056 is a claimed hit that can be checked at both ends: Maduro captured on the 3rd
against his repeated sight of "the third". The complication is one he half-notices himself, and
it is in the mention: the tellings on file point at February the 3rd, not January the 3rd.
Flagged for the evidence pass with a system edge to february-3-budget.
The February 3rd thread now has a date problem of its own. LmxIp6r1zmw@1478 puts the State of
the Union on 25 February; five days later meR7v1cmzBI@453 puts the same speech on 3 February.
Recorded as delta_type contradiction, because the third is the anchor the whole thread hangs on.
Seventh item attached to that date (hL9Trl2qb9k@1967), where the only content is a rhyme.
hL9Trl2qb9k@3266 cuts against his own interest and belongs on the record: "Find God for
yourself. Turn YouTube off." Said twelve days into the year he has spent months building up.
LmxIp6r1zmw@2650 is the opposite move and is filed as such: Ephesians 1:18 used so that anyone
who does not see what is coming is described as constitutionally unable to. Edge-linked to
symptoms-do-not-count as the second pre-emptive answer to the obvious objection.
SZttUyrnsRQ@5545 names the tradition the whole authority-and-declaration model comes out of, and
he names it himself, so the edge to calling-things-that-be-not is asserted_by brandon.
SZttUyrnsRQ@5883 shows the seven-year tribulation date being worked out loud from the change of
administrations rather than received. He lands on 2027; tribulation-2029 says otherwise, and the
contradiction edge is recorded.

### oe-46, 8-13 January 2026, 29 passages, 16 new claims. Tier 1: 1696 / 2477 (68.5%).
Videos hL9Trl2qb9k, n8ZEQ9_9iMk, cbmTsV2q-Us, Lf38vkQwpgE.
hL9Trl2qb9k@3640 is the single most important line yet for what this database is for. On the
Australia drought word he says: "If that's not happening, then say it's not for today or it's an
off-word." That is a falsification condition stated in advance, by him, for his own claim.
Across 1696 extracted passages it is the only one. Recorded verbatim in the quote field so it
cannot be lost, as a new_detail on watch-australia.
The midterm call has now settled and it is not the red wave. Three consistent tellings in three
weeks: barely keep the House, lose the Senate (27 Jan), keep the House so impeachment fails and
the Senate is in jeopardy (9 Jan), and the clearest of them, Lf38vkQwpgE@899: "The House in the
vision remained under Republican control. But the Senate flipped blue." That can fail on a single
night in November. A brandon-asserted same_event_as edge now joins battleground-senate-2026 to
stalemate-government-2026, since he supplies the mechanism himself at n8ZEQ9_9iMk@2475.
Two more on-air self-checks where he plays the original recording rather than paraphrasing:
cbmTsV2q-Us@2022 replays the 16 January 2025 California word. Both that recording and the
11 November ice storm one are inside this corpus, so the checks are available to anyone.
Two claimed same-day hits go to the evidence pass: Greenland mining "to establish the dollar
against the BRICS" (cbmTsV2q-Us@1461) and the California corruption post counted at 248 hours
after his word (Lf38vkQwpgE@1840). Both are checkable at both ends.
utah-temple-attack escalated from an attack on the temple to mass casualties. The Minnesota woman
is now to be removed, four tellings in and still unnamed, and in December he said she might not
even be in Minnesota.
vibrant-colors-mean-hot supplies the key to every colour sighting in the corpus and applies
retroactively to the purple three and the purple over the Olympics.
February now has three dates live with no content on any: the 3rd, the 24th and the 25th.

### oe-47, 3-8 January 2026, 29 passages, 18 new claims. Tier 1: 1725 / 2477 (69.6%).
Videos Lf38vkQwpgE, TLV_rmXYyO8, o7a-DROTbqA, EmhmXkiAJH0, L9GIjgo0Kok.
The pairing this batch exists for. Lf38vkQwpgE@6179, 8 January: he raises the objection himself,
that if nobody is a decamillionaire within the year then the word was "a fault, a misword", and
answers "No" - God prepares the heart, the word went in on 30 September 2024, keep believing.
hL9Trl2qb9k@3640, 13 January, five days later, on the Australia drought: "If that's not
happening, then say it's not for today or it's an off-word."
Same man, same week, two incompatible standards for his own record, and which one applies tracks
the subject: the money word cannot fail, the weather word can. Both quotes are on file verbatim
and a contradicts edge joins not-a-misword-keep-believing to watch-australia. This is the single
most useful thing the database has turned up.
Also worth having: he reaches "Greenland" at @7939 by working outward from the word green through
dangling and leaning, rather than being given the name. And at TLV_rmXYyO8@4963 he sounds his way
to "the mayors". Both recorded, because how the images are arrived at is part of the record.
greatest-voter-turnout (TLV_rmXYyO8@6461) is directly measurable, which almost none of the
election material is. debt-matched-by-surplus-2026 names a ratio, which almost no prosperity
declaration does.
Two places he points the audience away from himself: find-a-bible-church, sending new converts to
a local church, and no-ministry-of-hints, refusing to solicit by hinting at need. Both recorded,
the second alongside the sacrificial-sowing appeal three days later.
Contradiction edge: closer-than-you-think-return against we-have-a-work-to-do-window. Within
three weeks the return is both nearer than anyone realises and further out than the audience hopes.

### oe-48, 3 January 2026, 4 passages, 1 new claim. JANUARY 2026 COMPLETE.
Video L9GIjgo0Kok. Tier 1 now 1729 / 2477 (69.8%). January took batches 44 through 48.
attack-worse-than-october-7 gets its fifth telling since 22 November and, for the first time, a
timing commitment of sorts: he calls it "the next thing". Recorded as timing_update rather than
another restatement for exactly that reason.
The plague is now "AI generated" in two tellings a fortnight apart and the mechanism is never
explained in either.
largest-megachurch-targeted names a specific church for the first time and widens beyond
charismatic churches.
NEXT: February 2026 (101 passages). Selftest and export due at batch 50.

### oe-49, 24-28 February 2026, 29 passages, 12 new claims. Tier 1: 1758 / 2477 (71.0%).
Videos 1Bd3ILxtC40, Ywv1xy-ko9U, V5WgYqWpBgk, Ux9iGMe2HSo. February 2026 opened. Past 71%.
THE FEBRUARY 3RD THREAD CLOSES WITHOUT RESOLUTION. 1Bd3ILxtC40@4480: he asks his own team
"Has the Lord said anything about March 3rd?" and is answered at @4503 that no, it was all about
February 3rd, "cuz I said three three trace trace". The date has now passed. Across seven
tellings the content was never specified: the Olympics opening (built on a wrong start date),
Pope Leo, the budget, three judges, European decisions, Iran and Israel, and a rhyme. He is now
looking for a March version of it. Both passages recorded as elaborations so the thread ends on
the record rather than trailing off.
Three date errors are now on file, all small and all his: the Olympics opening (the 3rd, actually
the 6th, later self-corrected), the State of the Union (the 25th, then the 3rd), and now the
inauguration on "the 21st probably of January", which is fixed by amendment to the 20th.
1Bd3ILxtC40@67 is the clearest instance of the dates moving in the retelling: he places his own
word in February of this year, is corrected on air that it was last February, and accepts it.
1Bd3ILxtC40@3443 cuts the other way and is credited: he corrects his own audience, saying he did
not say reptilian and is not saying it, the word was chameleon. They had run further with the
image than he had.
The Senate call got its fourth consistent telling (Ux9iGMe2HSo@1391) and, for the first time, a
prayer clause. That is a real change and the review says so: a Republican hold would previously
have falsified it, and now it confirms the intercession instead.
Third on-air replay of a raw original in six weeks (the 1 February anonymous man word), after the
ice storm and the California word. That practice remains the most useful thing in the corpus for
anyone checking his record.
NEXT: batch 50 is the checkpoint. selftest.py, export_view.py, re-check todo.

### oe-50, 19-24 February 2026, 29 passages, 12 new claims. Tier 1: 1787 / 2477 (72.1%).
Videos Ux9iGMe2HSo, 8NT0fll0Jbg, UzueHsrDGNM.
BATCH 50 CHECKPOINT: `python selftest.py` -> ALL CHECKS PASS. `python export_view.py` ->
prophecy-db.html, 1870 KB. Tier 1 past 72%.
8NT0fll0Jbg@2474 is the line of the batch. The banks-and-crypto agreement he has spent a year
praying toward is here called the birth of the beast system, leading to the digital dollar and
the mark. The same event is the answered prayer in one telling and the mark of the beast in
another. Recorded plainly with a brandon-asserted edge to clarity-act-one-vote, since he joins
them himself.
Two concessions worth crediting, both unprompted. @2133: "you can never predict exactly how
Senate and Congress is going to" go, a limit on his own material. @2588: the March 1st date comes
from the news, not from a sight, and he says so - a distinction he does not always draw. Seeded
as march-1-they-are-saying with a brandon edge to prophetic-method-in-part.
year-2028-wall answers a question the audience asks, how he knows a year: the number appears in
the vision. It is an absence of sight, a wall he cannot get over, not a claim about 2028, and the
falsify field says so.
Third account of how the dates arrive, after the camera lens and the zooming: months on a clock
face he reads round (clock-face-months-2027).
third-temple-build now carries a window for the first time, around 2028 with construction
beginning, which makes it checkable where the earlier tellings were not.
Dates reconstructed on air again at @2852, "December something". Second instance this week.

### oe-51, 4-17 February 2026, 28 passages, 12 new claims. Tier 1: 1815 / 2477 (73.3%).
Videos kcyoauFFjD0, YCq4oFKaqL4, OmFxbr3D8Gk, 3-PvLM6tblM, P8iv0CFojcg.
Two lines in this batch change how the rest of the corpus should be read.
YCq4oFKaqL4@3207: "I may not always know the street address. But I know the sentences." That is
the clearest statement anywhere of what he claims accuracy for. It licenses every wrong date and
wrong place on file while preserving the claim to accuracy. Seeded as street-address-vs-sentences
and edge-linked to prophetic-method-in-part.
3-PvLM6tblM@4600: prayer "only delays the inevitable" and Agenda 2030 "will come to full
fruition". That concedes intercession cannot prevent the outcome he asks them to pray against,
which cuts directly against vision-is-a-prayer-target. Recorded as a contradicts edge, not
reconciled.
YCq4oFKaqL4@2975 does the same work on the election thread: the red wave is reinterpreted as "not
a political red wave, but a blood wave, a glory wave". A lost midterm could still count as the
wave arriving. Seeded as blood-wave-not-political with a brandon-asserted edge to red-wave-2026.
The February 3rd thread gets its last two entries and both are after the fact. OmFxbr3D8Gk@1101
is a week late with still no content; P8iv0CFojcg@806 is the day after, saying the Lord called it
"a stench to me concerning decisions" and that he still does not understand what he was seeing.
Credit where due: P8iv0CFojcg@561 separates what was in the word from what was not, saying he
never saw a volcano this time and that the Italy shaking was not in this one. The purple three
also finally gets a location, a mountaintop.
kcyoauFFjD0@2575 is the most direct thing he has said about what the platform has shown him of
other ministries: he does not want to become that.

### oe-52, 2-4 February 2026, 15 passages, 4 new claims. FEBRUARY 2026 COMPLETE.
Videos P8iv0CFojcg, whNsPmzslac, 2AD5ytrJBAU. February took batches 49 through 52.
2AD5ytrJBAU@7191 is a flat negative call and they are rare: the man "will not make it to the
White House. He'll not run for president." Recorded as delta_type contradiction against
booker-licking-the-ground-2028, where three days earlier the appetite for the office was the
point and a run was assumed. It is framed as a declaration rather than a sight, so a run could
still be read as insufficient prayer.
The State of the Union now has three different dates across three weeks: the 25th (15 Jan), the
3rd (27 Jan), the 24th or 25th (4 Feb). The Olympic opening, by contrast, is now given correctly
as the 6th, having started at the 3rd in November.
whNsPmzslac@750 adds the consequence to the midterm call, impeachment in 2027 or 2028, but that
version has both chambers lost where the five settled tellings have the House held. The mismatch
is in the review note rather than smoothed.
P8iv0CFojcg@1058: two months after first seeing the number three on the mountain he is still
working out what it means, and offers the skier reading as his own guess. Recorded as a guess.
Fourth on-air replay of an original recording (whNsPmzslac@1130), dates located from the archive.
great-migration-2026-2028 comes with a request to sow into it. The money request is part of the
claim as given and is recorded that way.
NEXT: March 2026 (139 passages). Selftest and export due at batch 60.

### oe-53, 26-31 March 2026, 28 passages, 14 new claims. Tier 1: 1858 / 2477 (75.0%).
Videos mdXXTm-aWEU, M5FxVJVwU2s, 1L7tKIvSMyY, e9umIfTFnMM. March 2026 opened. Three quarters done.
e9umIfTFnMM@1836 is the most checkable date in the batch and the least prophetic: wormwood is
"April the 13th of 2029, it will happen on a Friday". That is the published close approach date
of the asteroid Apophis, and it is a Friday. The date comes from astronomy rather than from
sight, and he marks it himself with "if that is true". Seeded as wormwood-april-13-2029 and
edge-linked both to wormwood-poison-water and to april-13-holocaust-remembrance, the other
April 13 on file.
e9umIfTFnMM@2175 narrows shake-the-nations from a three year span to a single day, 1 April. That
is a real tightening and it can fail on the day. Recorded as timing_update.
Two direct calls against other prophetic voices in one session: @6547 says the chatter about good
coming in 2028 "is false", and @6599 stakes out great darkness around 2028 instead. Both can fail,
and both put him on record before the fact rather than after.
Set against that, @1748 is the clearest admission of the limit anywhere: "the timing of it I don't
always know." Said in the same video as three dated claims.
Fourth distinct account of how the dates arrive (@1801): a tear-off paper calendar fanned in front
of him, after the camera lens, the zooming and the clock face.
M5FxVJVwU2s@2779 is a criticism of exactly the practice his own channel runs on: intercessory
prayer meetings where they hardly pray.
Fifth on-air replay of an original recording, dates pinned from the archive.
watch-carney is a named head of government called a devil with no act attached, recorded as stated.

### oe-54, 21-26 March 2026, 28 passages, 12 new claims. Tier 1: 1886 / 2477 (76.1%).
Videos e9umIfTFnMM, hH4qc5gpzRU, US8rZ7oprqo, Duk8c34FPC4.
Two self-sealing structures got stated outright this batch, both by him.
hH4qc5gpzRU@2609: the birthing pains double from 1 April, and "birthing pains do not decrease,
they increase". A claim that by its own definition cannot be contradicted by anything that
follows. hH4qc5gpzRU@1149: "a lot of you will call it an Ichabod" and the Lord says it is not.
That rules out hardship in advance as evidence against, which makes three such pre-emptions on
file with symptoms-do-not-count and eyes-of-understanding-not-enlightened. Edge recorded.
Against that, US8rZ7oprqo@1829 is his own explanation for why dated words slip, offered without
prompting: seeing in part makes you think it is next month, or two, or three. And US8rZ7oprqo@6850
says plainly he cannot put God in a box and is still trying to work out what he was given, while
repeating the April 1st date in the same passage. Both halves recorded.
taiwan-two-day-fall picked up its most concrete detail yet, the chips and medicine motive, and
says three days again where the claim itself says two.
sonic-boom-breaks-glass is unusually checkable for an undated claim: broken glass in houses and
cars would be reported.
Sixth on-air replay of an original recording (the 2 December moon word), which goes to the
evidence pass with the recording available in this corpus.
US8rZ7oprqo@636 shows an article on screen as confirmation of the weather-warfare claim. The
mention notes the difference between an accusation reported and a claim confirmed.

### oe-55, 14-21 March 2026, 26 passages, 5 new claims. Tier 1: 1912 / 2477 (77.2%).
Videos Duk8c34FPC4, vsqXfAy4rxk, TC0SV11Jv8M, 8RydcMuYFcI, 6wtLDJxg4sw.
MILESTONE IN THE VALIDATION MIX: UNFALSIFIABLE (389) has overtaken UNRESOLVED (387) for the
first time. More extracted claims now cannot come due than can.
TC0SV11Jv8M@2303 is the most specific version of attack-worse-than-october-7 across six tellings:
a biological agent, delivered by something like a crop duster, out of the Damascus area, at
night. That is checkable in a way none of the earlier tellings were. Edge to
telaviv-chemical-attack recorded.
8RydcMuYFcI@1770 clarifies the Taiwan window properly: three days is the duration of the takeover,
not a countdown from now. He says so unprompted, and adds Venezuela as the model.
cuba-liberation-day-2027 escalated: liberation now involves American troops and invasions, where
the January telling had no mechanism at all.
8RydcMuYFcI@1346 carries the fullest disclaimer he has given: it is his opinion, he is not trying
to provoke any government, and he pleads the blood over it. Recorded in the certainty field.
vsqXfAy4rxk@73 is worth having next to speech-crackdown-midterms: a squeeze on the media is a
warning when applied to his side and a promise when applied by it. System edge records the pair.
vsqXfAy4rxk@3073 forecloses criticism by construction: every tongue that rises is condemned
rather than answered.
man-shot-life-ended is a self-attested hit with both ends checkable, a 3 January telling in this
corpus and a disappearance since. The name is on screen rather than in speech, so the transcript
alone will not settle who. Flagged for the evidence pass.

### oe-56, 9-14 March 2026, 26 passages, 11 new claims. Tier 1: 1938 / 2477 (78.2%).
Videos 6wtLDJxg4sw, Mzw5rRiDwA0, ji5iFzKemg4, gLE4m-wraw8, lKC1io90BMo.
TOP OF THE EVIDENCE-PASS LIST: Mzw5rRiDwA0@1270. He reads a news report of a magnitude 6.0
earthquake near Naples on 10 March 2026, the strongest in that part of Italy in more than 63
years, and plays it twice. That is a real dated event of public record offered as fulfilment of
the Italy material, and the prior Italy claims are in this corpus. Whether they say Naples, and
whether they describe a quake rather than a volcano, decides it. Filed as an elaboration on
naples-volcano-tsunami.
Three claims this batch can be settled against public data, which is unusual:
gas-eight-dollars-nationwide (national average petrol price, published weekly),
container-ships-on-fire (last weeks of March, would be widely reported), and the Naples quake.
attack-worse-than-october-7 is now fully specified after six vague tellings: Iranian biological
weapons, out of the Damascus area, delivered by something like a crop duster, used on Israel.
gLE4m-wraw8@1647 does the same for hidden-cells-america, naming Iran and naming high schools and
college campuses.
Two structural admissions worth keeping. lKC1io90BMo@984: "I'm coming back for a harvest. I have
long patience" - the mechanism that lets an unfulfilled imminence run indefinitely.
lKC1io90BMo@2075: he offers the fact that he is now seeing into the tribulation as evidence of
how close it is, which is circular and is recorded as such.
gLE4m-wraw8@232 is a rare acknowledgement that the news feeding these sessions has to be filtered
and that he does not believe all of it.

### oe-57, 2-8 March 2026, 24 passages, 12 new claims. Tier 1: 1962 / 2477 (79.2%).
Videos U2zTp6gX81I, EPIsbBYnCw0, bHVnPIa0Cn4, Tw9xqU-vn2k, Cys6GFXLPNs, 6YMi3ZJxq8M, fjuTrDgdUgA.
Cys6GFXLPNs@3764 is the sharpest claim in the batch and a real escalation. The decisions of the
next couple of weeks "will make or break his presidency, whether he lives and goes through it or
he goes home". In January make-or-break meant political standing; here it means death, on a three
week clock. Filed as severity_update on valley-of-decisions-make-or-break with an edge to
divine-protection-trump.
Two contradictions recorded rather than smoothed. july4-250th-parades prays over the 4 July 250th
anniversary as the target, when in November he named that exact date and ruled it out as too
expected (not-the-obvious-date). And plague-2027-china-rats-europe now carries "100% fatality",
which no pathogen has ever had and which sits against plague-350m, where a fixed death toll
implies survivors.
U2zTp6gX81I@2502 is worth having precisely: he says he did not know the area was dark and had it
looked up afterwards. The corroborating detail arrived after the sight rather than before it.
bHVnPIa0Cn4@1901 has the same shape in reverse: a news item about fish from the deep is produced
first and then read as the match.
Seventh on-air replay of an original recording (the 3 March word).
lone-wolf-not-the-main-show defers indefinitely by construction: any attack that does happen
becomes a preliminary rather than the fulfilment.
The validation mix keeps moving the same way: UNFALSIFIABLE 410, UNRESOLVED 389.

### oe-58, 2 March 2026, 7 passages, 3 new claims. MARCH 2026 COMPLETE.
Video fjuTrDgdUgA. Tier 1: 1969 / 2477 (79.5%). March took batches 53 through 58.
fjuTrDgdUgA@1349: "many many small 9/11s throughout the nation", prayed over for more than a
year. No threshold, so ordinary incidents can be read into it, and the year of prayer is offered
as the reason they have not happened. Both outcomes are confirmations. Linked to
sept11-2026-groundzero: one date and many undated events between them cover the whole theme.
fjuTrDgdUgA@8052 can actually come due on 31 March: the whole year's budget arriving in the first
quarter, restated on 2 March with four weeks left.
spouse-in-2026-esther tightened from 2026 to "this month", which is a real narrowing even if the
claim stays unfalsifiable in practice.
fjuTrDgdUgA@6274 is worth having: one of the very few places the material asks something of his
own audience, on racial hurts and offence, rather than of their opponents.
NEXT: April 2026 (153 passages), the largest remaining month. Selftest and export due at batch 60.

### oe-59, 28-30 April 2026, 26 passages, 11 new claims. Tier 1: 1995 / 2477 (80.5%). Past 80%.
Videos i6g1k3fCWLs, QLk3uWjK0jU, 7FG6qD91nZo. April 2026 opened.
Three claimed fulfilments in one session (29 April), all matched to real dated events, all going
to the evidence pass:
- QLk3uWjK0jU@727, a newly discovered asteroid passing inside satellite orbits, offered as the
  "rock headed" he says he saw. Small asteroids do this regularly, which the passage omits.
- QLk3uWjK0jU@781, a real record hourly rainfall in southern China, attributed to weather
  weaponisation. The event is real, the attribution is the claim, and the mention separates them.
- QLk3uWjK0jU@1153, a fraud investigation offered as the Minnesota woman's "days are almost done".
  Eight tellings in she has still never been named, so matching the investigation to her is the
  open question.
QLk3uWjK0jU@1516 has a calendar fact that is genuinely checkable and genuinely striking: Rosh
Hashanah does begin at sundown on 11 September 2026. That is the calendar rather than a sighting,
and the mention says so.
Two unusually testable claims: three-day-healing-window (one person, one condition, three days)
and quarter-point-stimulate-or-lose, where the 0.25 figure can be checked against published rate
decisions.
i6g1k3fCWLs@5616 questions lifelong medication from the pulpit. He does pair it with getting help
rather than replacing it, and the mention records both halves.
QLk3uWjK0jU@2071 notes the president's age directly after the pressure-of-the-position material.
Read beside the March "lives and goes through it or he goes home", neither says it outright.
NEXT: batch 60 is the checkpoint. selftest.py, export_view.py, re-check todo.

### oe-60, 21-28 April 2026, 25 passages, 8 new claims. Tier 1: 2020 / 2477 (81.6%).
Videos 7FG6qD91nZo, -2rEylREFj0, 9dkcd0-ilkM, 3nlrKph_elQ, yPdEFEDVsic.
BATCH 60 CHECKPOINT: `python selftest.py` -> ALL CHECKS PASS. `python export_view.py` ->
prophecy-db.html, 2128 KB. Two thousand tier-1 passages extracted.
9dkcd0-ilkM@7889 is the plainest statement in the whole corpus of why the dates cannot be relied
on, and it is his own: when he gets deep into it he does not know where he is and has to pull
back, because it is panning so fast. Filed against prophetic-method-in-part.
-2rEylREFj0@3064 matters for reading everything else: "we're going to get in the river and see if
the Lord has anything for us tonight". A good deal of this material is sought live on air rather
than brought to the broadcast already received. Seeded as getting-in-the-river and edge-linked to
the partial-sight clause.
He also supplied a second interpretive rule that is testable across the corpus: a very clear
vision means a quick event (-2rEylREFj0@3243), alongside January's brightness-means-urgency.
Both are now on file as claims and edge-linked.
Two contradictions recorded, neither withdrawn by him. -2rEylREFj0@8684 declares a red wave in
November against five consistent tellings that the Senate goes blue, and softens inside the same
sentence to "not lose this back over completely". And 7FG6qD91nZo@8589 has the 24-hour change as
about to happen, where February had it already under way.
-2rEylREFj0@1956 gives asset guidance and disclaims it as not financial advice in the same breath.
3nlrKph_elQ@2585 draws a distinction he has not drawn before and did so unprompted: he prays for
the Jewish people but does not necessarily support Israel's government, since governments come
and go.

### oe-61, 16-21 April 2026, 24 passages, 12 new claims. Tier 1: 2044 / 2477 (82.5%).
Videos yPdEFEDVsic, Zw7-D11KBIU, Z4Dzphusf-U, Xst5KJVjDeY.
THE HARDEST CLAIM IN THE CORPUS. Xst5KJVjDeY@817: reading a report that the asteroid named for
the god of chaos passes close to Earth in 2029, he says "I don't think it's going to pass" and
that it is "actually going to hit". In March the same date was taken from published astronomy and
offered conditionally. Here it is a flat contradiction of an observed orbit, with a named object
and a fixed date, 13 April 2029. It cannot be hedged, reinterpreted or prayed away. Recorded as
severity_update on wormwood-april-13-2029.
yPdEFEDVsic@1227 states the central claim of the whole corpus in one line: "we are the news. They
come and get news from us." Everything in this database bears on whether that holds. Seeded as
we-are-the-news and edge-linked to prophetic-accuracy-2025.
Two more cleanly testable items: carmax-in-trouble names a publicly traded company that reports
quarterly, and clarity-act-one-vote now has a real deadline on a real bill, "even before June",
which can fail on 1 June.
Xst5KJVjDeY@765 carries a rare and real hedge: he allows that what he hears while driving "could
be flesh".
Zw7-D11KBIU@2733 repeats the pattern that is now settled rather than accidental: the same
technology is the answered prayer in one telling and the foundation of the beast system in
another.
Two more claimed hits dated to tellings inside this corpus (lab-grown organs from July 2025, and
a 21 May 2025 word), both flagged for the evidence pass.

### oe-62, 13-16 April 2026, 23 passages, 7 new claims. Tier 1: 2067 / 2477 (83.4%).
Videos Xst5KJVjDeY, tMmRhBhwYSc, ZvDla0vHYoY, aYNy8bxXKrs.
ZvDla0vHYoY@1680 is the concession everything dated in this corpus should be read against, and it
is entirely his own: "I know I'm seeing into the tribulation. I don't know when of what year."
He then asks whether it is 2028 or past 2028 and answers that he does not know. Edge-linked to
street-address-vs-sentences: he claims the sentences, not the street address, and does not claim
to know the year.
ZvDla0vHYoY@7736 states the organising assumption that lets any two events be joined: "it's all
connected. It's a spirit." He then uses it in the next passage to tie the Hitler image to the
Oklahoma City bombing during that anniversary week. Brandon-asserted edge recorded.
april-19-may-1-occult-window is built entirely from anniversaries read off a list, not from
anything shown, and the mention says so. Credit where due at @1545: they test the Tulsa massacre
against the pattern, find it falls on 31 May, and drop it rather than forcing the fit.
Two claims got sharper. cold-war-gets-colder finally names Russia and, by the panda, China, and
adds August. no-plan-b-supreme-court is now conditional on two specific public outcomes, the
tariffs taking effect and the court ruling, which makes it more checkable than December's version.
vance-2028-realignment went the other way: in January he saw Vance at the helm, here it is a
question he is seeing in part and praying about, with Rubio named alongside.
if-you-wont-pray-why-are-you-here treats disagreement as trolling, which sits against his own
stated standard in no-prophetic-confusion. Contradiction edge recorded.

### oe-63, 7-13 April 2026, 23 passages, 9 new claims. Tier 1: 2090 / 2477 (84.4%).
Videos aYNy8bxXKrs, 4EEOGvIPfFM, 4fTnqDOIePk, sNsgdTx5NPM, jonj7Nq5hG8, zaCMLnzdWHQ.
TOP OF THE EVIDENCE-PASS LIST, alongside the Naples quake. sNsgdTx5NPM@892: he says that when the
Supreme Court came against the tariffs he saw plan B, that he said that was war, and that this was
"clear back in February before they struck Iran". Both halves are checkable: the February telling
is inside this corpus, and the ruling and the strike are matters of record. Brandon-asserted edge
to prophetic-accuracy-2025.
4fTnqDOIePk@1576 is the second strong one: a real FBI warning about Iranian hackers targeting
critical US water and energy systems, offered as fulfilment. His March telling did name water
infrastructure, so this is checkable at both ends too.
THE SENATE CALL REVERSED. zaCMLnzdWHQ@1761: "The Lord said, You can win the Senate." Five
consistent tellings since January had the Senate flipping blue. Recorded as delta_type
contradiction rather than folded in.
sNsgdTx5NPM@44 describes the method without embarrassment: he took the puzzle pieces of everything
they had prayed over since October and started putting them together. The pieces are assembled
into a picture afterwards.
sNsgdTx5NPM@528 gives the accuracy claim its testable form as an instruction he says he received:
say it with accuracy and boldness, and you will see it in the news.
aYNy8bxXKrs@1921 is candid: twelve years on he has been trying to find the man from the 2014
vision "time and time again" and has not.
aYNy8bxXKrs@2387 is the starkest survival claim yet: "President Trump won't make this if you
don't pray." Completion of the term then confirms the prayer, so neither outcome counts against it.

### oe-64, 2-7 April 2026, 21 passages, 10 new claims. Tier 1: 2111 / 2477 (85.2%).
Videos zaCMLnzdWHQ, QsNuNKQL80E, UMqHeHjGuMI, ABqn0lFIbqk.
zaCMLnzdWHQ@3727 states the watchman claim as a plain job description: "we are seeing in the
future to tell you you must pray over the bases", dated to March 2025, which is inside this
corpus and therefore checkable. Edge-linked to we-are-the-news.
zaCMLnzdWHQ@7738 is a significant gloss on the whole political programme: plan B exists "to try
to extend the time". That is the same delay logic as extended-time-grant, now applied to policy
rather than to prophecy. System edge recorded.
Three claims here can be settled from outside, which is unusual density:
twenty-three-nations-crusades (a hard count on public events within a year),
california-146-billion-fraud (a stated figure and a stated comparison), and new-jet-in-may
(aircraft liveries are photographed constantly).
argentina-outpouring-april names a country and a month and ties the outpouring to the start of
the wealth transfer, so both hang on the same April window. Brandon-asserted edge recorded.
QsNuNKQL80E@4883 points the other way from the Taiwan invasion claim he has held since 2023:
"I see Taiwan. And they ain't going." The passage is fragmentary and he does not reconcile it, so
it is filed as a contradiction rather than folded in.
QsNuNKQL80E@501 is worth noting for what it is: four months into the year he named as the year of
1 Corinthians 5:5, he is asking what the rest of it looks like rather than saying.
if-you-heard-what-i-heard is unfalsifiable by construction and he says so himself: the material
that would cause the country to demand answers is not disclosed and never will be.

### oe-65, 1-2 April 2026, 11 passages, 5 new claims. APRIL 2026 COMPLETE.
Videos ABqn0lFIbqk, OVKr-hVqdI4. April took batches 59 through 65.
ABqn0lFIbqk@8290 is the most consequential piece of structure in the batch and one of the neater
retirement mechanisms in the corpus: April through July can still be turned by prayer, but "once
we turn that corner through August the decisions will start to be made" and are set in stone.
Prayer gets a four month deadline; anything after August is settled rather than falsified, so the
claim retires without ever being tested.
ABqn0lFIbqk@7990 does the same work in one sentence: the path is averted if they humble
themselves, but only "for a window, for this season". Not arriving proves the aversion, arriving
proves the failure to humble.
ABqn0lFIbqk@9519 offers a rocket launch as confirmation of a moon base. Those are not the same
thing and the mention says so; both the December and April tellings are in this corpus.
OVKr-hVqdI4@1875 states the absorbing mechanism plainly: he keeps "praying them down", so each
plan that does not arrive is a prayer answered rather than a claim missed.
Tenth on-air replay of an original recording (7 July 2025), and he corrects himself mid-sentence
from "I gave this word" to "the Lord gave it through me".
NEXT: May 2026 (126 passages). Selftest and export due at batch 70.

### oe-66, 22-28 May 2026, 23 passages, 9 new claims. Tier 1: 2145 / 2477 (86.6%).
Videos 0LcmZ81vn0I, G7T_Ugj_wn4, dbSI0MLNI9k, QesBBHtuWPs. May 2026 opened.
G7T_Ugj_wn4@5182 is among the most checkable claims in the whole corpus: three living ministers
named, a named church, and September. Church appearances are publicly advertised, so it can fail
cleanly. Edge-linked to church-of-his-presence-september, which he joins himself.
dbSI0MLNI9k@47 is the strongest fulfilment claim of the batch and goes to the evidence pass. The
video reports a plot against a member of the president's family; he says he called retaliation
against the children and named Don Jr in advance, as revenge for the Soleimani strike. Both his
earlier tellings and the reported plot are checkable, and at @731 he puts the accuracy question
to the audience directly.
attack-worse-than-october-7 moved target for the first time in eight tellings. Every prior version
had it against Israel; dbSI0MLNI9k@5072 puts it inside the United States, carried out by people
"infiltrated within".
hagin-revival-lasts-two-years traces the two year revival window to a word from a minister who
died in 2003, delivered in a visitation to heaven. That is beyond any check but his own account,
and QesBBHtuWPs@4410 gives it a start window of this summer, so it becomes due from August.
Two more claimed hits on the moon material: a real NASA lunar announcement dated 26 May offered
as fulfilment of the December word, with the caveat that part of the claim rests on a thumbnail
placement decision rather than on anything said.
Credit where due: QesBBHtuWPs@2313 marks the glowing mountain as metaphor himself rather than
pressing it as literal.

### oe-67, 14-22 May 2026, 22 passages, 9 new claims. Tier 1: 2167 / 2477 (87.5%).
Videos QesBBHtuWPs, IArOJFkoBFY, ylrbNngiG14, 9wgEbD964mI, P5YAnc70THI.
9wgEbD964mI@6394 is worth recording precisely because of what it shows about the framework: he
asks whether the date of Rosh Hashanah 2028 "has been announced yet" and whether there is a way
to find it out. The Hebrew calendar is fixed and published decades ahead. There is nothing to
announce.
olympics-2028-darkness reads the LA dates correctly off the published schedule, 14 to 30 July
2028, which is a fixed public window. That makes it checkable even though darkness is undefined,
and it sits against the 2026 Olympics claim that was built on a wrong start date.
attack-worse-than-october-7 shifted agent again: biological in March, chemical here, with
Damascus constant across both. Ninth telling.
hagin-revival-lasts-two-years hardened. "Starts this summer" is now stated flatly rather than
conditionally, so a two year revival becomes due from August 2026.
cruise-ship-revival is a good example of how claims get assembled: three separate sightings dated
1 October, 6 December and 9 December are pulled together on air into one claim, with the dates
reconstructed in conversation rather than recalled.
coup-25th-amendment names the constitutional mechanism for the first time, which makes the older
coup claim testable in a way it was not.
red-wave-2026 was declared again across four levels of office, against five tellings that the
Senate goes blue. The contradiction edge already exists.

### oe-68, 12-14 May 2026, 21 passages, 11 new claims. Tier 1: 2188 / 2477 (88.3%).
Videos P5YAnc70THI, ZgqApEslE28, 2PoQzF7OhXc.
THE DECEMBER FED WORDS BOTH COME DUE HERE, and they split. ZgqApEslE28@2066 reads out that the
Fed chair's term ends Thursday 15 May. His December word "watch May concerning interest rates"
lands; his December word "Powell will be out in January" does not. Recorded as a contradicts edge
between the two, with the May one as a new_detail and the January one as delta_type contradiction.
Both go to the evidence pass together.
2PoQzF7OhXc@1496 is a strong fulfilment claim and goes to the evidence pass: he prayed over Times
Square on New Year's Eve specifically, in November and again in December, and a disrupted plot on
that exact target is now reported. Both tellings are in this corpus.
ZgqApEslE28@703 is the strongest source claim in the whole corpus: not a vision or an impression
but "Jesus stood right there in my house", dated to January. A January telling should exist here.
Credit where it is due, three times in one batch. He marks the Statue of Liberty holes as
symbolic, the big noses as symbolic, and at 2PoQzF7OhXc@774 refuses to add his own city to the
refinery target list: "I didn't see Tulsa", and he will not add to or take away from what he saw.
Against that, 2PoQzF7OhXc@2682 matches a number four he saw to a three day ceasefire, and the
mention records the mismatch rather than letting it pass. And "still out there" on the fertiliser
claim means it can never be discharged: not found is simply still hidden.
virus-more-contagious-trial-run names the device directly. A present outbreak confirms the plague
material without ever discharging it, and the real one stays two years out.

### oe-69, 7-12 May 2026, 20 passages, 5 new claims. Tier 1: 2208 / 2477 (89.1%).
Videos 2PoQzF7OhXc, fgeWM9FVuqA, tKNBjoymWHM.
THE DEFINITIONAL MOVE, STATED OUTRIGHT. 2PoQzF7OhXc@4139: answering the charge that a word that
did not land is a false prophecy, he says "I didn't give a prophecy. I gave you a vision", and
calls the impatience a microwave expectation. That reclassification is what exempts the whole
corpus from the false-prophet test, and it pairs with street-address-vs-sentences (the accuracy
standard narrowed) and vision-is-a-prayer-target (the outcome standard narrowed). All three edges
are now recorded.
tKNBjoymWHM@3202 cuts the other way and is the most consequential line for the prayer framework:
the Lord is quoted saying of the coming plague "You won't stop it. You can lessen it." That
removes the usual escape from this one claim and leaves it standing on timing alone. Recorded as
a contradicts edge against vision-is-a-prayer-target.
tKNBjoymWHM@3248 says the end of 2027 into 2028 is "what I've always seen". The record does not
support that: the plague window has moved through 2026, 2027 and 2028 across at least seven
tellings since November, and the mention says so.
2PoQzF7OhXc@4281 records something useful: the team keeps its own chart of the words so they can
be pulled up later. That is what makes the on-air replays possible, and it is the same
undertaking as this database.
fgeWM9FVuqA@1959 dates the origin of the 1 Corinthians 5:5 claim to Christmas 2025 and plays the
original, which is in this corpus and can be read against the recall.
NEXT: batch 70 is the checkpoint. selftest.py, export_view.py, re-check todo.

### oe-70, 6-7 May 2026, 19 passages, 9 new claims. Tier 1: 2227 / 2477 (89.9%).
Videos tKNBjoymWHM, 8czXf1gl9bM.
BATCH 70 CHECKPOINT: `python selftest.py` -> ALL CHECKS PASS. `python export_view.py` ->
prophecy-db.html, 2361 KB. Tier 1 at 89.9%, 250 passages left.
tKNBjoymWHM@8140 is the exemption applied directly to the plague he has just forecast: stand on
Psalm 91 and no evil shall befall you, it is not going to hurt you. That is what makes a 350
million death toll costless to hear, and the brandon-asserted edge to
virus-more-contagious-trial-run records it.
tKNBjoymWHM@5846 is the honest counterweight, unprompted and in the same session as "always seen":
"I don't know exactly when the date is. Could it be off? Yeah."
8czXf1gl9bM@1938 is worth recording precisely. The 2027 disclosure date does not come from a
sighting at all; it comes from another person's interview about closed meetings, played on air and
edited down by his team. It then joins the 2027 material already on file.
8czXf1gl9bM@1405 doubles the birthing pains a second time, on 11 September, a date that already
carries the attack claim. Doubling a quantity that was never measured, twice.
Twelfth on-air replay of an original recording (21 January 2024), and it is in this corpus.
matthew-24-no-shock joins i-gave-a-vision-not-a-prophecy as the second structural way of removing
the sting from an unfulfilled word: it was scripture already, so nobody should be surprised
either way.

### oe-71/72, 1-6 May 2026, 21 passages, 7 new claims. MAY 2026 COMPLETE.
Videos 8czXf1gl9bM, 3EBkKb5vnrM, Zp04KcZ0DnU, lDyDFQRE3UY. May took batches 66 through 72.
Zp04KcZ0DnU@2655 is the most serious claim in these two batches: he says the last reported
assassination attempt on the president "was a hoax" and something was not right about it, while
stating twice that he is not accusing him, and forecasts a genuine attempt to follow. Recorded
exactly as put, disclaimer intact, as last-assassination-was-a-hoax.
8czXf1gl9bM@3564 is a claimed hit offered the week it happened: the Lord said to pray over May
concerning the Clarity Act, and the Senate markup was announced that week. Both the earlier
telling and the legislative record are checkable, so it goes to the evidence pass. Worth noting
at @3753 that the banks "threw a fit", which is the opposite of the agreement at the table he
saw in February.
The coup claim was told three times in one week and now names the 25th Amendment each time.
May ends carrying at least seven separate claims: interest rates, the Fed chair's departure, the
Clarity Act, a Cuba decision, robbery, a new jet and a birth. may-is-a-pivotal-month adds an
eighth with pivotal left undefined.
3EBkKb5vnrM@972 sets a standard for the audience that the visions are not held to: without a
scripture to stand on you go nowhere.
NEXT: June 2026 (142 passages), the last full month. Selftest and export due at batch 80.

## Batch 73 — 27-29 June 2026 (Nbb5gUwTSE0, FHxJpX0PLPI)
19 mentions, 7 new canonical claims (seedtime-and-harvest-remains, young-senator-will-come-out,
watch-cern-dark-matter, black-tentacles-livestreams, pieces-of-what-i-saw, july-seventh-month-word,
ministries-that-think-theyre-alive). 5 relationships, 3 of them brandon-asserted with mention evidence.
Notable: the Watergate claim finally names two living men and a year (JD Vance, Elon Musk, 2028),
which is the most checkable form it has taken across the whole corpus. Against that, church-cleansing
took two timing updates in one session that do not agree — a four-year 2026-2029 span at 914s and a
July-to-December 2026 window at 3049s — both recorded as same_event unsure, neither reconciled.
Second on-air concession that a prayed-for man died. The rats claim gained deliberate agency
(poison injected, spread across Europe), which is a different assertion about the same forecast event.

Data fix this batch: a 16-word quote (FHxJpX0PLPI@36) reached the database before the check caught it.
Trimmed in mentions-oe-73.json, the mention row and mention_fts. A full-table audit then found 105
other mentions over the 15-word cap, predating this batch — sweeping those next.
Sweep done: 106 over-cap quotes trimmed in the database and 105 in the source JSON files
(trimquotes.py, trimquotes_files.py, both idempotent and both refusing any replacement that is
not a contiguous verbatim substring of the quote it replaces). The cap breach was concentrated in
the earliest batches, before the pre-load check became standard. selftest ALL CHECKS PASS after.

## Batch 74 — 19-24 July 2026 (sV1rn2FVee8, usjH1gnxOZw, bTI89Td5Xc4)
12 mentions, 4 new claims (mount-of-olives-split, vance-succession-pregnancy,
called-trump-would-lose-2020, netanyahu-arrest-threat-september). 5 relationships, 3 brandon-asserted.
Two findings worth flagging. First, usjH1gnxOZw@1614 is the cleanest specimen of the structure this
project exists to document: a forecast that the president would be taken out did not occur, he says
so on air, and it is scored as two hits at once — the non-event credited to prayer, and a pregnancy
he concedes he cannot place in time offered as the detail proving the vision. Second, church-cleansing
now has three timings inside one month that do not agree (2026-2029, July to December, July to an
unnamed "first"), recorded as a contradiction with all three left standing.
Against that, mount-of-olives-split carries the strongest hedge yet recorded: no date, not this year,
and the September/October guess is his son's. Logged without a window because he refused to give one.
The batch also produced the first genuinely tight target in the September UN cluster, 22-26 September.
Pre-load check gained a verbatim-quote assertion against the transcript segments; all 12 passed.

## Batch 75 — 16-19 July 2026 (bTI89Td5Xc4, zp4ImjufUuU, 7I5xdRDaayo, LlRONx0fV0A)
12 mentions, 2 new claims (drones-given-by-iran, sooners-asia-first-on-crypto). 5 relationships,
3 brandon-asserted. Three contradictions recorded rather than reconciled. zp4ImjufUuU@1144 says three
incompatible things about the Senate inside one minute (we still win; they take the Senate and we keep
the House; they get both), so no result can miss. Taiwan now disagrees with itself inside a single
passage — fall within three days, then fight for one, into two, fold by the end of the second — and
7I5xdRDaayo@853 branches again to Taiwan holding until the tribulation because prayer bought time.
church-cleansing took a fourth timing (July to the first of the year), so it now has four windows
from one month that do not agree.
Two claims here rest on something already public: the 25th Amendment line at zp4ImjufUuU@1066 comes
from the critic's clip he is reacting to, and the Iranian drone origin is scored as confirmed on the
strength of the president saying he will look into it. Both noted in the reviews.
sooners-asia-first-on-crypto is the one genuinely scoreable item — the original "watch the Sooners"
statement should be datable inside this corpus and set against the date of the Japanese vote. Left for
the evidence pass.

## Batch 76 — 13-16 July 2026 (LlRONx0fV0A, ruV85YYcW1o)
12 mentions, 3 new claims (assassins-through-canada-michigan, iran-regime-flip-reza-assassinated,
churches-burned-giant-rises). 6 relationships, 4 brandon-asserted.
LlRONx0fV0A@1735 is the counter-example this project needs on file: he refuses to count a real arrest
as his fulfilment, says outright it is a distraction and not what he saw, and warns against taking it
as the win. Nearly every other fulfilment assertion in the corpus runs the other way.
Three unusually scoreable items came out of this batch. The Iraqi word at @439 is dated on both ends
(word 11 July, news 15 July), so whether the reporting postdates the word is settleable from the
record. @1186 names three corrupt men in the Iraqi central bank, an institution and a count. @2429
gives three Senate seats with Georgia and Minnesota named, which is far tighter than the self-
contradicting Senate passage recorded two days later in batch 75.
One deliberate omission: LlRONx0fV0A@1978 carries two claims, Iran/Reza and the Colombian president
the cartel comes against as he takes office in August. Only the Iran claim was seeded, because
seeding Colombia with no mention to assign would orphan it. The Colombian detail is preserved in the
mention's claim_text and should be promoted when a passage centres on it. It is now past due.

## Batch 77 — 12-13 July 2026 (ruV85YYcW1o, 4WhvlFBHVyM)
12 mentions, 4 new claims (drone-attack-derail-elections, save-america-act-support-structure,
presidency-comes-to-nothing, church-held-accountable-for-window). 6 relationships, 5 brandon-asserted.
ruV85YYcW1o@3423 is the most important passage extracted in this whole sweep. The mechanism the corpus
runs on is stated outright: he prayed more hours over the 2024 term and the president's safety than
anything, it came to nothing, and the answer given is "I hold the church accountable. How do you pray?"
Responsibility for the outcome is transferred to the audience before the outcome is known, so a failed
forecast becomes a failure to pray. Recorded whole, with the surrounding passages that make it work —
@3114 (the presidency is a nothing burger) and @3187 (Trump will not save America, said since 2024).
Two contradictions logged. The drones reverse: earlier bought online, now explicitly "not the kind you
buy off Amazon" but military and smuggled from Iran. And the asteroid escalates from a close approach
to penetrating and hitting the earth, while the name he says God gave him is withheld — the one detail
that would identify the object. Its 2027 date is read off a news item about a scheduled deflection
test, not from the vision.
One checkable item: @5276 calls in buses with air conditioning, a physical object testable against the
ministry's own assets, unlike most declarations here.

## Batch 78 — 10-12 July 2026 (4WhvlFBHVyM, 0iOZJHUwyjQ)
12 mentions, 2 new claims (cancers-thing-of-the-past, europe-scans-private-messages). 5 relationships,
all brandon-asserted.
0iOZJHUwyjQ@1761 supplies the broadest unfalsifiability device recorded so far: Daniel saw things that
had not come to pass thousands of years later and is in the Bible, therefore "you think it's tomorrow,
but it's years". That retires the deadline from every dated claim in the corpus in one move, and it
sits in the same passage as a properly checkable item, an appearance on a named channel on 11 July 2025
about Poland.
Four fulfilment assertions this batch, three of them weak on their own terms: weapons found in Lebanese
tunnels offered against an attack claim (preparation, not the event); a second Sooners assertion in
three days resting on the same undated original word; and the European privacy vote, where he is unsure
whether his word came four or five weeks earlier, leaving a fortnight of slack in a claim whose whole
force is the ordering. The fourth, the church fires, is dated on both ends (word in May, fires in July)
and is genuinely checkable apart from the attribution to the Islamic Brotherhood, for which nothing is
offered.
Two clean tests banked for the evidence pass: the White House ballroom completion date (@8295, where he
says outright he does not know why he sees 2027) and the 11 July 2025 Poland appearance.

## Batch 79 — 4-10 July 2026 (0iOZJHUwyjQ, jtAhMuOfFwM, V3w8-580i2s, Mq0qQJkoWcg)
12 mentions, 3 new claims (divine-reversal-declared, significant-artifact-found,
green-white-jerseys-riot). 6 relationships, 4 brandon-asserted.
divine-reversal-declared is worth naming for what it does rather than what it forecasts. The doctors
are not attacked; their finding is politely demoted to "a report". That places every medical outcome
outside the claim's reach without denying a single diagnosis — the same result as symptoms-do-not-count,
reached by a gentler route, and applied to cancer and heart disease by name.
Two past-due items now scoreable. Mq0qQJkoWcg@620 put a retaliatory attack on the 250th anniversary
weekend; the weekend passed without one. And jtAhMuOfFwM@4869 handles that passing by claiming credit
for it: prayer is said to have prevented what was coming and the manifestation is moved into the days
ahead, converting an expired deadline into a pending one.
green-white-jerseys-riot is the most checkable fulfilment assertion found in this whole sweep. Mexico
plays in green and white, the fixture was on a published schedule, and the original "pray for the green
and white jerseys" statement should be datable inside this corpus. Flagged for the evidence pass.
apollyon-war-2025 shifted from 2025 to 2027-2030; recorded as timing_update with both visible.

## Batch 80 — 2-4 July 2026 (Mq0qQJkoWcg, 4GiaXApc3SQ, CoXY2EJ5oDA)
12 mentions, 3 new claims (satellite-earthquake-weapons, trump-wealth-doubling,
chips-back-from-taiwan-two-years). 5 relationships, 2 brandon-asserted.
Two hedges stated outright rather than left implicit. CoXY2EJ5oDA@2073 covers both outcomes of a vote
in one sentence: not enough votes to impeach, but enough to keep him out of the presidency. And
4GiaXApc3SQ@2975 asks itself whether the building is a real building and answers "it's metaphor",
which removes the image from any possible test before anyone else can raise it.
church-cleansing took a fifth timing (@1141), and the end date is worked out aloud by trial and error:
July 3rd to December 3rd, then June, then January 3rd. That is now five windows from a single month.
Three properly scoreable items banked. chips-back-from-taiwan-two-years puts a hard two-year deadline
on a measurable industrial quantity. watergate-2028 @2511 names three living people inside a two-year
window. And the attendance and salvation tallies (@5348, @5729) are checkable both against the
platform's published counts and against each other, since they accumulate across the corpus.

### Checkpoint at batch 80
selftest ALL CHECKS PASS, including the index/table match after the 106-quote trim earlier in this
session. export_view wrote prophecy-db.html at 2511 KB. Tier 1 at 94.4% before this batch; the pick
queue is down to 135 tier-1 passages across 21 videos, from 2477 at the start.

## Batch 81 — 1-2 July 2026 (CoXY2EJ5oDA, jlQZ9XjWWus)
12 mentions, no new claims — the first batch in this sweep where every passage mapped to a claim
already on file. 5 relationships, 4 brandon-asserted.
Two dating corrections in one batch, both his own. The Ark word is dated to January here and to
February on 9 July; recorded as a contradiction because which month it was decides whether any news
item postdates it. And at jlQZ9XjWWus@1066 he corrects himself from February to January mid-sentence
about the assassination vision.
CoXY2EJ5oDA@3717 is the most specific claim extracted in this sweep: the plague, fall 2027, Europe
first, rats, escalating in November-December, 350 million dead, running into 2028-2029. A continent,
a vector, a season and a number. 350 million is roughly one person in twenty-three alive.
jlQZ9XjWWus@1066 is the most scoreable: a named agency, a stated trigger (rejecting a two-state
solution) and a physical setting (a balcony). And @210 names JP Morgan, which makes a lobbying claim
checkable against the public record — while conceding in the same breath that the bill may not pass
until 2027, which cuts against clarity-act-one-vote. Logged as a brandon-asserted contradiction.

## Batch 82 — 27 June 2026, the "clear into 2030" session (FHxJpX0PLPI)
12 mentions, no new claims, second batch running with everything mapping to claims already on file.
5 relationships, all brandon-asserted. This one session is the longest-horizon material in the corpus.
The pattern that defines it: specificity asserted, specifics withheld. At @1312 he says he could pause
and freeze on individual ministries and see exactly which leaders would die and which would survive,
and names none of them. At @287 he says he will never say which ministry the sunflower was and asks
viewers not to guess. At @1664 he says there was more detail than he could put into words. In every
case the checkable part is precisely the part he declines to give.
Two claims slipped further out. church-cleansing took a sixth timing (July to January first). The
plague stretched from a 2027 event to a four-year span running to 2030 — in the same session that,
minutes earlier at batch 81's @3717, gave fall 2027 with a 350 million death toll.
One item here is firmer than the rest and worth the evidence pass: @1113 says live streaming moves
back onto actual television as platforms restrict religious speech. That has a business consequence
and is checkable against where the ministry actually broadcasts by 2030.

## Batch 83 — 24-27 June 2026 (FHxJpX0PLPI, i9gn298oFBM, ig_1Spghkgg)
12 mentions, 2 new claims (disney-cruise-virus-plot, wings-clipped-january). 5 relationships,
4 brandon-asserted.
One item here is unusual enough to flag on its own. i9gn298oFBM@2693 is the only word of knowledge in
the corpus precise enough to fail on its own terms, and it does: the lady is given as 71 years old and
born on 25 June 1954. Someone born on that date turns 72 on the day this was spoken. That is checkable
arithmetic, not interpretation, and the two details he gives do not fit each other.
i9gn298oFBM@2113 supplies the line that makes the disaster material work in both directions at once:
"you can lessen it, you won't stop it". The catastrophe is guaranteed to arrive whatever the audience
does, while the audience is personally exempted by Psalm 91. Prayer is made worth doing and incapable
of being disproved in the same sentence. Related to church-held-accountable-for-window, which does the
mirror-image job for the political claims.
The Watergate fulfilment at FHxJpX0PLPI@2759 rests on the man having compared himself to Nixon. That is
a remark, not a scandal, and self-comparison to a former president is ordinary political speech.
pakistan-disruptions is worth the evidence pass: he makes the case for it himself ("you never hear
about Pakistan"), and the January origin is datable inside this corpus.

## Batch 84 — 22-24 June 2026 (ig_1Spghkgg, MlCLrdfztps, 7ufmrBqNg-o)
12 mentions, 2 new claims (red-tip-missiles-moscow, putin-assured-by-trump). 5 relationships,
all brandon-asserted.
Second counter-example of the sweep, and it is a strong one. Drone attacks on Moscow had just happened
and would have been easy to bank; instead at 7ufmrBqNg-o@1236 he says plainly "not the red tip missiles
that I saw, but they're using drones" and holds the claim open. That refusal is worth recording beside
the 793 fulfilment assertions that run the other way. The cost of it, though, is that the claim can
never expire: the real version is always still to come.
putin-assured-by-trump is the third case in three batches of specificity asserted and withheld. He says
he saw an assurance guaranteed to Putin by Trump, that an agreement was made, that Putin looked assured
because he was promised something — and then stops, on the grounds that what he saw was bad and he does
not want to put anybody in danger.
Two internal inconsistencies logged as stated rather than smoothed. At @2547 he says three years and
then names a window that is two. At MlCLrdfztps@908 the new detail (the attack comes up by Damascus)
genuinely narrows the claim, but the fulfilment offered runs the wrong way: weapons being seized is the
opposite of an attack occurring.

## Batch 85 — 17-22 June 2026 (7ufmrBqNg-o, Ucfm1SaO_NM, HhKfSxKL67I)
12 mentions, no new claims. 5 relationships, 3 brandon-asserted.
A direct contradiction now sits on the file three weeks apart, recorded as such: HhKfSxKL67I@1032 has
the Lord saying "you'll be so thankful that you had him", while ruV85YYcW1o@3114 on 13 July has the
same presidency as a nothing burger that came to nothing. Neither is withdrawn. Logged as a
system-asserted contradiction between grateful-for-trump-later and presidency-comes-to-nothing.
Two fulfilment assertions here are weaker than the claims they answer. HhKfSxKL67I@898 offers a
photograph of Macron and Zelensky together as the Lord's warning that they "will be friends" — but two
wartime allies meeting is their ordinary working relationship, so the claim was met before it was made.
And Ucfm1SaO_NM@4116 offers a Hezbollah missile attack against a claim he interrupts himself to withhold,
asking whether he should say it publicly again; the passage cuts off before he states what he saw.
Two items pinned for the evidence pass, both genuinely settleable. HhKfSxKL67I@618 turns entirely on
whether the cell-tower and AT&T material predates the 23 September 2025 SIM farm seizure, and that is
checkable inside this corpus. And @1329 reports 911 outages across several states on 16 June 2026 —
the closest thing yet to a live test of the 911 disruption claim.
HhKfSxKL67I@467 is now past due with both ends fixed (14 June to 4 July) and the target named.

## Batch 86 — 15-17 June 2026 (HhKfSxKL67I, yCJFoRGfrEc, q-M7KOvMzS4)
12 mentions, 1 new claim (january-2027-highlighted). 5 relationships, 3 brandon-asserted.
yCJFoRGfrEc@2296 shows the reconciliation move in the open. A report puts the figure at 200 million;
he says "where's the rest of it? I saw billions" — and resolves the gap by assuming the remainder is
still to come, not that the number he saw was wrong. A shortfall of an order of magnitude becomes
partial fulfilment awaiting completion.
Two items are worth the evidence pass. yCJFoRGfrEc@2060 is a rare case where he supplies the receipts:
he says he called Gavin Newsom before the 2024 result and that they have the videos to prove it, so the
priority is checkable inside this corpus. The pairing with Michelle Obama is what would separate it from
an obvious guess. And q-M7KOvMzS4@205 gives the hardest specifics in the corpus for a plot claim — two
countries, a distance of 50 yards and a calibre — while again stopping short: "that's all I'll say".
One note on scoring for later. ezekiel-38-turkey now carries "Damascus becoming a ruinous heap", which
is a direct quotation of Isaiah 17 rather than a description of something seen. Its base rate matters:
that verse has been announced as imminent by many people for a very long time.
The michelle-gavin claim moved from 2024 to 2028; recorded as a timing_update.

## Batch 87 — 11-15 June 2026 (q-M7KOvMzS4, 7CtKI-6263c)
12 mentions, no new claims. 5 relationships, 4 brandon-asserted.
q-M7KOvMzS4@2426 is the clearest statement yet of how an unmet promise is disposed of. Christmas
declarations were made; the gifts did not arrive; the explanation given afterwards is that the chariots
of fire were sent, the people were not ready, they refused to take it, and the chariot turned around
and carried the package back to heaven. Nothing about that can leave a trace, and it moves the failure
onto the hearer. It is the provision-side twin of church-held-accountable-for-window, and is linked as
such.
Against that, this batch has the best-scoreable geopolitics found so far. 7CtKI-6263c@674 says Turkey
takes the Black Sea and closes it to help Russia — the straits are governed by treaty, access is
publicly observable, and it would run against Turkey's current position. @1078 names two living leaders,
a stated outcome (a truce between Xi and Kim) and a dated origin of 4 January inside this corpus. @491
dates a Turkey-Syria alliance word to 14 March and draws a specific asymmetry: Turkey defends Syria but
not Iran.
Three track-record claims here point at recordings inside this corpus (8 October, last summer,
4 January). Those are all directly checkable and are queued for the evidence pass.

## Batch 88 — 9-11 June 2026 (7CtKI-6263c, KvS6uzzLK6c, wLI8D3SDe3E)
12 mentions, 1 new claim (world-cup-2026-prayer-targets). 5 relationships, 4 brandon-asserted.
Two statements forty seconds apart that do not sit together, both recorded as stated. At
KvS6uzzLK6c@2128 he says "every single vision that I've had is that it happens" — which says prayer has
averted none of them. At @2171 he says the Lord told him "you will not stop everything, some things
will happen" — which is the conditionality that hedges nearly every claim in this corpus. If the first
is true the second is doing no work, and the conditional escape attached to hundreds of claims has been
answered by him.
KvS6uzzLK6c@376 is now the most scoreable political claim on file: the Senate lost by exactly three
seats while the House holds, on a fixed date. A number, a direction and a deadline. The escape is
written into the same sentence — he is praying those three seats will not flip — so a hold can still be
credited to prayer, but the stated forecast is unambiguous.
world-cup-2026-prayer-targets was seeded specifically to close a door. At @4516 he reads the New York
fixture list off the published schedule, dates and broadcaster included. Nothing is forecast. It is on
the record so that any later claim of foreknowledge about one of those dates can be set against the
passage showing where the dates came from.
The plague identification finally arrived: the unexplained darkness on the buildings is named as the
black death and placed in June 2028, against the fall 2027 / 350 million telling. Both left visible.

## Batch 89 — 8-9 June 2026 (wLI8D3SDe3E, a4uOSv4NVrE)
12 mentions, no new claims. 5 relationships, 3 brandon-asserted.
a4uOSv4NVrE@2788 gives the near-miss handling in its clearest form. A meteor claim was made for April
1st; a real event of the named kind arrives; a 3.5 quake is offered and he answers "the one I saw is
bigger". The real event is ruled too small to count and the claim stays open for a larger one. That is
the same structure as the red tip missiles in batch 84, and linked to it. Both claims are now
permanently unexpirable by their own terms.
Two items point the other way and are the best of this batch. a4uOSv4NVrE@2666 is the most empirically
testable claim found in the whole sweep: birds breeding in August instead of October because something
throws the seasons off. Bird breeding seasons are recorded systematically by ornithologists, so an
off-season shift either shows in the data or does not. And @3047 is unusually unhedged — he says the
assassination "was successful" and Kyiv "was divided into two", leaving no room for a prayer-averted
reading later.
@3588 narrows rather than widens for once: the censorship claim covers X and other platforms but he
says he did not see it with Facebook. Recorded, because excluding a case makes a claim harder.

## Batch 90 — 4-8 June 2026 (a4uOSv4NVrE, gklesf_Fdg8, Tme-Su9LtHo)
14 mentions, no new claims. 5 relationships, 3 brandon-asserted. Runs 642-646.
Tier 1 after this batch: 2464 / 2477 (99.5%).
Three claims came due inside this batch and all three failed on their own terms. gklesf_Fdg8@6517 is
among the most specific in the whole corpus: a lone wolf in San Antonio in June, one dominant plus two
others, wearing a black hoodie, with his own reasoning for why it would stand out (a hoodie in June in
San Antonio is out of place). No such attack. @2707 put rioting on a single named date, the 14th —
though protests that day were already publicly scheduled when he said it, so the base rate was not low.
And @4701 promised the wealth transfer would start to manifest in June; "a trickle" is the smallest
possible claim, needing no threshold and satisfied by any single testimony.
gklesf_Fdg8@2397 is the passage to keep. He names other people's failed date-setting precisely — 88
reasons why Jesus is coming in 88, the weirdness of 1988 and 2000, "we will never see the new
millennium", and then drily, "we're 27 years into it". He describes the mechanism accurately and does
not apply it to his own dated material, of which this corpus holds a great deal.
Against that, the beef claim (@1405, @1930) is the strongest form a priority claim takes anywhere here:
the origin recording is played on air with its date, 27 June 2025, and beef prices are a published
series, so it can be scored to a number. The contrast with @2630 in the same session is sharp — neither
he nor his son can date the Cuba word at all, saying only that it has been seen so many times.
Two scoring notes recorded for the evidence pass. @1041 counts ordinary dated fireball sightings as
fulfilment; the American Meteor Society logs thousands of those reports a year, so the rate is the
question, not the occurrence. And @7108 is the passage that sets the timing the later "we did our job"
fulfilment claim depends on: the baby was born, the president was not removed, and that window closed.
Tme-Su9LtHo@54 corrects itself mid-sentence from September to January 6th — worth noting because
January 6th there is the name of a kind of event, not a date, so the claim carries no timing at all.

## Batch 91 — 2-4 June 2026 (Tme-Su9LtHo, EIT61ZA5ExU, tEQc2bHEE4Y). TIER 1 COMPLETE.
13 mentions, 2 new claims (trump-wartime-president, headlines-nation-in-turmoil). 5 relationships,
3 brandon-asserted.
Two passages are worth keeping for the opposite reason to most of this corpus. tEQc2bHEE4Y@409 carries
the strongest hedge on file, unprompted: "all in my opinion", "I am not a financial adviser", "this is
just what I see in vision and I can miss it". That qualification is absent from almost everything else
extracted. And Tme-Su9LtHo@1818 is a call made against the subject's stated intention rather than with
it: the Lord said he would be known as a wartime president while the man himself was saying he would be
a man of peace and wanted the Nobel. Both go on the record beside the misses.
EIT61ZA5ExU@317 contains his own summary of the material: "I know I bring some very hard things."

## STOPPING CONDITION MET
`python prophecy.py todo` reads tier 1 at 2477 / 2477, 100.0%. The pick queue returns 0 unextracted
tier-1 passages across 0 videos. selftest: ALL CHECKS PASS, including the tier partition now reading
{1: 0, 2: 1155, 3: 3015}. export_view wrote prophecy-db.html at 2658 KB.

Totals for this sweep (batches 31-91, 61 batches this session): 2477 tier-1 passages extracted into
mentions, every one adjudicated to a canonical claim with a written reason, every relationship edge
carrying either mention evidence or `asserted_by: system`. Every checkpoint from batch 40 onward
(40, 50, 60, 70, 80 and final) returned ALL CHECKS PASS. That is not true of the run as a whole: the
oe-20 entry above records a full integrity cleanup — a foreign-key abort, 91 unreviewed assignments
left open from batch 10, six orphaned claims and six duplicate slugs from two workers seeding
independently — after which selftest went green and stayed green.

## WHAT REMAINS, AND WHY IT WAS NOT DONE
The goal names tier 1 at 100% as the stopping condition, and that is now met. Two bodies of work are
queued and deliberately not started, because starting either would have delayed the stated condition:
  - 234 past-due claims with no evidence recorded. These need `python prophecy.py evidence <file>`
    with source URLs and a verdict rationale each, weighing base rates.
  - 793 strong fulfilment assertions not yet linked to the claims they answer.
The reviews written across this sweep name the specific items worth taking first, because they can be
settled rather than argued: the 22-26 September UN window; green-white-jerseys-riot (Mexico plays in
green and white and the fixture list was published); controlled-beef-supply (the origin recording is
played on air with its date, and beef prices are a published series); chips-back-from-taiwan-two-years
(a hard deadline on a measurable industrial quantity); battleground-senate-2026 (three seats, named
states, a fixed date); turkey-turns-back (the straits are treaty-governed and access is observable);
sun-seasons-shift (bird breeding seasons are recorded systematically); and the SIM-card priority
question at HhKfSxKL67I@618, which turns on whether the cell-tower word predates 23 September 2025 and
is checkable inside this corpus.

## 2026-08-30 — session pass over the finished tier-1 corpus, then validation opened

Tier 1 finished at 2,477 of 2,477 while the previous supervisor was running; it exited on its own
completion probe at 23:16 on 29 August. Audit of the worker's output found no missing quotes, no
quote over fifteen words, and a delta spread that uses the whole vocabulary rather than collapsing
into restatement. Three defects were found and fixed, each with a guard so it cannot recur:

  - Ten canonical claims were duplicates of one another, splitting one event's history across two
    ids. New command `prophecy.py merge` folds a duplicate into the survivor by moving its live
    assignments as NEW assignment rows and superseding the old ones, then leaves the dead id
    resolving to the survivor through `canonical_claim.merged_into`. Nothing is deleted. The
    israel-night-attack / attack-worse-than-october-7 pair was deliberately NOT folded: same target,
    different stated detail, so it carries a `same_event_as` edge with `asserted_by: system`.
  - Eleven mentions carried no falsifier, all from early runs 92 and 126. Backfilled from
    falsifiers-backfill-1.json, source JSON patched to match, and `load` now REFUSES a mention with
    no falsify_match. A falsifier written after the outcome is worthless, so it is required up front.
  - `review` matched mentions on (video_id, start_s) and took the newest, but 162 timestamps carry
    more than one mention, so the older one could never be adjudicated. It now refuses an ambiguous
    row and prints the mention ids. Where two rows are genuinely one utterance re-extracted twice,
    `duplicate_of` records that and the redundant assignment stops counting toward the thread.

The 103 assignments flagged same_event=unsure were adjudicated: 73 decided in reviews-unsure-1.json,
30 left parked, because unsure plus contradiction or branch is the terminal state the design asks
for, not a backlog. `todo` now reports those two groups separately instead of hiding the second.
Three claims were seeded that the adjudication needed (acceleration-undated, two-state-inevitable,
october-2024-storm-warning) and oklahoma-divided was rebuilt: its only assignment had been a passage
of land-run history, so the three real tellings were extracted from the corpus instead.

Validation is now open, twelve claims judged against live sources. The sharpest results so far:
february-3-budget (the shutdown ended on the exact named date, eight weeks out, though the Supreme
Court half missed and appropriations deadlines cluster there anyway), crypto-ruling-august-2025
(CONTRADICTED: the appeals were withdrawn that month and the case ended, the opposite of the second
court he described), saudi-brics-oil-200 (the 24 August invitation landed, membership never did, oil
never came within half of $200), byron-florida-governor (primary won as he staked it on, but 47.8%
is not the landslide he named), good-year-2025 (S&P 17.9% against 25.0% in 2024, so the one
comparative element that could be checked went against him).

DO NOT REDO: the merge, the falsifier backfill, the unsure adjudication, the Oklahoma rebuild, or
the twelve claims in evidence-batch-2026-08-30.json and evidence-batch-2026-08-30b.json.

## Job A batch 1 — 30 August 2026. Evidence, most-told first.
Fixed seven orphan assignments first: three passages where he reads news or plays a Trump clip were
adjudicated no_claim under the rule that a clip he plays is not a claim he makes, the 2028 rapture
allowance went to rapture-hope-2028, and the blue / baby blue / blue stealth / mango trio from
kVVIsIOdYvg got a new claim, blue-stealth-december-january. Patched the `todo` query, which was
grouping every claim_id IS NULL assignment into one phantom past-due claim.
11 verdicts. Two hold up in part and are worth naming. september-2025-acceleration: the week of
22-23 September 2025 really did carry a coordinated wave of Palestinian statehood recognitions, but
the UNGA date is published years ahead and his own 19 August telling shows a viewer supplied it.
church-cleansing: on 26 January 2026 he said a shaking was coming to churches in California and
Bethel Redding suspended Ben Armstrong on 15 February, a genuine three-week lead, though his 24
February telling comes nine days after the news broke and is not a prediction.
Two clean misses. judgment-569-days expired on 2 October 2023 against an ordinary news day, and he
had already voided his own date in advance by announcing an extension. soar-2024 is CONTRADICTED:
2024 was the first year in Lifeway's tracking history in which Protestant church closures outpaced
openings, against a word that the body of Christ would soar.
Four recorded UNFALSIFIABLE with the reason written out rather than left unchecked: point-of-no-return,
reprieve-four-years, passover-april-1-acceleration (his own falsifier says birthing pains only
increase) and good-year-2024 (a coin you may read either way, made conditional on the hearer's belief).
april-1-signs-in-heavens is the best base-rate case in the batch: AMS logged a record 2,322 fireballs
in Q1 2026 with March the standout, and he gave the word on 27 March, ten days after the 17 March
Ohio-Pennsylvania daylight fireball made national news.
NOTE: a second worker is on this database at the same time, taking the oldest and least-told claims
(evidence-batch-oldest-1.json, evidence-a01.json). Working the most-told end to stay out of its way.

## Batch A1-A2 — Job A opens: 51 past-due claims scored (222 -> 157)
Oldest first, 2021-12-31 through 2024-12-31. Two corpus checks did real work rather than argument.
yankees-world-series: he says on 4 November that the Lord had told him to watch the Yankees since
May; the corpus holds nothing on the Yankees before 9 October 2024, by which date both teams were
already in their league championship series. candidate-outdoor-attack: the opposite result. The
28 December 2023 passage is the only one before 13 July 2024 pairing a candidate with outdoors, a
big crowd and mountains, and the word assassination appears nowhere in the corpus before that date,
so the Butler shooting is not a standing prayer that eventually caught an event. Scored STRONG_MATCH,
the first in the database, with the mountains detail recorded as a miss.
Nine claims went to UNFALSIFIABLE rather than sitting unchecked: the coin-with-two-sides device on
soar-2024 and good-year-2024 supplies both faces in advance, and october-grace-window offers hell on
earth as the averted branch. oil-200-barrel and digital-dollar-transition are the clean contradictions.

## Job A batches 2 and 3 — 30 August 2026. Twelve more verdicts.
The one STRONG_MATCH so far is candidate-outdoor-attack. Given on video 28 December 2023, six and a
half months before Butler: a presidential candidate outdoors before a big crowd, needing protection.
The base rate is genuinely low, the last shooting of a US presidential candidate being Wallace in 1972.
Discounts recorded in the rationale: it is a prayer request rather than a forecast, and the mountains
he saw are not the Butler Farm Show grounds.
powell-out-in-january is the cleanest miss in the corpus so far and is CONTRADICTED. He said 4 December
2025 that Powell would be out in January; Powell chaired the Fed to 15 May 2026, Warsh was sworn in on
22 May, and Powell kept his board seat to 2028 by choice. His May correction, that Powell is jobless,
is wrong too. He did mark it as his opinion, which is recorded.
yankees-world-series is the priority case worth keeping. He says on 4 November 2024 that he saw the
matchup back in May; a full-text search of the corpus finds no Yankees passage before 9 October 2024,
and that one is protection prayer over a scheduled playoff game. The matchup claim first appears five
days after the series ended.
sugar-bowl-new-orleans is the base-rate case worth keeping. He named New Orleans and the Sugar Bowl in
December 2025, twelve months after a mass-casualty attack at that place on that date tied to that game,
with the anniversary already driving a Guard deployment. Nothing happened.
times-square-new-years-eve carries a fulfilment assertion that fails on the record: he says in May 2026
that a Times Square plot was stopped and not announced until now. The only disrupted New Year's Eve plot
is Mint Hill, North Carolina, a grocery store 600 miles away, and DOJ announced it on 2 January 2026.
easter-service-plots landed in Nigeria and is held at partial: Kaduna churches were raided at Easter
2026, but reporting notes the five-year pattern of holiday attacks there, and 170 worshippers had
already been taken from three Kaduna churches in January, before his 19 February word.

## Job A batches 4 and 5 — 30 August 2026. Sixteen more verdicts.
Two priority failures settled inside the corpus itself. tariff-war-predicted is CONTRADICTED: he claims
he called the tariff war before the inauguration, and a full-text search finds exactly one tariff
passage before 20 January 2025, on 6 December 2024, in which he is repeating Trump's own published
threat to put 100 percent tariffs on BRICS joiners, made six days earlier. strait-disruption-june-2025
is the same shape from the other direction: he named a waterway to pray over on 23 June 2025, one day
after Iran's parliament voted to close Hormuz and two days after the US struck Iran, and the week passed
with the strait open. The real 95 percent collapse in Hormuz traffic came in February 2026.
miami-hurricane-katrina-scale is CONTRADICTED on the measure itself: the 2025 Atlantic season put no
hurricane on the US coast at all, the first time in a decade.
canada-election-april-2025 CONTRADICTED, and his 30 April claim to have seen it coming is dated two days
after the count with no earlier record.
blood-moon-march-2025-war is the batch's most interesting partial. He named 14 March nine days ahead;
the US opened Operation Rough Rider on the 15th and Israel ended the Gaza ceasefire on the 18th. But the
claim names no party, place or kind of war, and two wars plus a Red Sea campaign were already running.
Four read-aloud passages recorded UNFALSIFIABLE with the reason stated rather than skipped:
mamdani-underground-swearing-in, three-day-ceasefire-may-8, japan-stablecoins-june-1 (read the day after
the FSA gazetted it) and the Naples quake report. Each is a scheduled or completed event offered as
confirmation, which is precisely what the fulfilment table exists to hold apart from evidence.
vatican-strike is worth flagging for job B: nothing struck St Peter's Square in the June-October window,
but 3,000 drones flew over it on 13 September 2025 for a ticketed concert, which is the kind of near-miss
that gets claimed later.

## Batch A3-A4 — 76 more scored (157 -> 76). Two priority claims fail the archive check.
drill-baby-drill-prophesied: he says the phrase was a word he gave before Trump said it. The earliest
occurrence anywhere in the corpus is 10 November 2024, four months after Trump used it at the
convention, and the phrase itself dates to a 2008 convention chant. CONTRADICTED.
point-of-no-return-september: he says on 9 September 2025 that the word was given back around March
and they have prayed over it since. A corpus search for September paired with a circled month or dust
returns nothing before 13 June 2025. The September framing is genuinely prior; the March origin is not.
prophetic-accuracy-2025 was scored against this database's own tally, which is the test he set: of
2025-due claims now carrying a verdict, 31 unfalsifiable, 12 partial, 9 expired, 5 contradicted,
0 strong. million-prayer-army was scored against his own on-air figure of about 5,500 concurrent
against a stated goal of a million, short by two orders of magnitude.

## Job A batches 6 and 7 — 30 August 2026. Twenty more verdicts.
million-prayer-army is the cleanest self-set number in the corpus and it is CONTRADICTED. The target
was a million people praying daily by 2025; his own on-air count on 28 October 2025 is about 5,500,
and the channel's total subscribers, which measure nothing daily, are about 608,000. The deadline then
slid to 2026 and then to whether they see it on this side or the other.
budget-states-funding-cutoff is CONTRADICTED with the direction reversed: he said 25 states would cut
off funding by 8 November 2025; what 25 states actually did was sue to keep SNAP flowing after USDA
announced the suspension on 24 October, three days before he spoke.
global-riots-worse-than-blm carries a factual error in his own evidence. The two million he attributes
to Barcelona on 4 October 2025 is the organisers' figure for the Italian general strike, which the
Italian interior ministry put at 400,000; Barcelona was tens of thousands. And the 14th he told viewers
to pray over was a No Kings day of action publicised on 28 May, a week before his 5 June telling.
Two more priority cases. container-ships-on-fire: he said on 13 March 2026 that ships would burn over
the last weeks of March, two days after the Mayuree Naree was hit and set alight in Hormuz with three
vessels targeted in one morning, inside a campaign running since February. drone-attacks-holiday-crowds:
European drone incursions had been front-page news since 22 September 2025, two months before the word,
and no holiday-crowd drone attack has happened anywhere.
hoover-dam-2025 is worth keeping beside candidate-outdoor-attack because they come from the same sitting
on 28 December 2023. One image in that passage was specific, dated and confirmed; the other was a wall
with no meaning, place or event attached, and produced nothing in the year named.

## Batches A5-A7 — JOB A COMPLETE. 222 past-due claims scored, queue reads 0.
Final tally across the sweep: 1 STRONG_MATCH (candidate-outdoor-attack), and the rest split between
partial matches, expirations, contradictions and a large UNFALSIFIABLE block. The unfalsifiable block
is the real finding of Job A, not a shortfall in it: the annual year-word (soar-2024, open-door-2025,
exceedingly-abundantly-2026) is the same claim re-dated each December with no threshold, and
dam-wall-ireland-2025 retires its own date in advance while keeping the event.
Four priority claims were checked against the archive that is supposed to contain them and failed:
drill-baby-drill-prophesied, yankees-world-series (told since May, corpus starts 9 October),
point-of-no-return-september (given in March, corpus starts 13 June) and earth-facing-solar-event
(warned on the 17th, no solar material in the 16-18 July uploads).
iraq-economic-boom is the sharpest reversal in the recent material: a great economic boom called in
April and July 2026 while Iraqi output fell 80 percent and the state missed July salaries.
moon-base-word was amended after the first pass: Artemis II launched 1 April 2026, three days from
the date given, which the May-announcement scoring had missed.

## Job A batches 9 to 11 — 30 August 2026. The second STRONG_MATCH, verified against the corpus.
sooners-asia-first-on-crypto. Full-text search of the corpus turns up the antecedent: on 17 June 2025
he says something major is about to take place with digital currencies, then "remember the Sooners,
South Korea, Japan, it's something about digital stuff with these two Asian countries." Japan's FSA did
not announce its reclassification plan until September 2025, three months later. On 15 July 2026 the
Diet passed the FIEA amendment and South Korea unveiled the National Asset Basic Act on the same day,
with the US CLARITY Act still unpassed. Two named countries, the right domain, thirteen months of lead
and a verified three-month lead on the first public policy step.
moon-base-word is the other priority check that passed, and it is held at partial. The 3 December 2025
telling is in the corpus, a base on the moon with pods and a dome and a space race, six months before
NASA's 26 May 2026 Moon Base announcement. But a south-polar outpost has been published NASA policy as
Artemis Base Camp since 2020, so the content reports an existing plan.
robbery-starting-in-may is CONTRADICTED against a national series: robbery fell 19.6 percent in the
first half of 2026, off a 2025 that was already the lowest rate in twenty years.
budget-fixed-january-2026 is CONTRADICTED in his strongest register. He said it was already done and
merely unannounced; Congress missed the 30 January deadline and shut down for four days.
passover-escalation-2024 is the best-timed near miss: given 22 February 2024 for "around 21 April", and
Iran's first ever direct attack on Israel came 13-14 April with the Israeli reply on the 19th. Held at
partial because escalation involving Israel in spring 2024 was near-certain and Passover itself passed
quietly.
new-jet-in-may lands on timing and fails on its one distinguishing detail: the repainted presidential
aircraft is a Boeing 747-8, the largest passenger jet Boeing builds, against "no longer a great big one
but a fast one".

## Job A complete, Job B started — 30 August 2026.
`todo` reads 0 past-due claims without evidence. 79 verdicts written across eleven batches by this
worker, with a second worker taking the oldest and least-told end. Two STRONG_MATCH in the whole
corpus: candidate-outdoor-attack (Butler, called 28 December 2023) and sooners-asia-first-on-crypto
(South Korea and Japan named 17 June 2025, both legislating 15 July 2026). Everything else is partial,
expired, contradicted or unfalsifiable.
Job B needed two code fixes before it could finish. First, `cue_strength()` at prophecy.py:1003 had
been written, documented and never wired into `cmd_scan`, which is why 113 scripture and future-tense
"come to pass" rows were sitting in the strong queue that no reader could ever attach to a claim; both
workers found it and it is now wired in and applied. Second, `cmd_fulfil` had no way to record a
reviewer overturning the rules pass, so a false positive like "just like I said" mid-teaching could
neither be linked nor cleared. It now accepts `fa_id` (exact, since one segment can carry several cues)
and `strength`, so a demotion is a stamped judgment rather than a silent edit.
Seeded oklahoma-quakes-increase for a claim that only exists in the corpus as a fulfilment assertion:
he says he called Oklahoma's earthquakes at his old church before the channel existed, which means the
original telling is not here and cannot be checked.

## Job B batches 1-3 — 793 unlinked strong assertions down to 298
Two things had to be fixed before the queue could be worked. autolink attached 220 on alias match.
Then the scan's strength rule turned out to be wrong on its most common cue: "come to pass" runs
three ways, and of 114 unlinked rows carrying it, 113 were promises, Acts 2:17 quoted, or admitted
misses. cue_strength() now reads tense and negation from the surrounding window, and
reclassify_ctp.py re-applied it in place to 165 rows rather than re-running scan, which would have
duplicated everything autolink had already attached.
The remaining false positive is the vision recounting: "that's what I saw" closes a description of
what he was shown, which is a telling, not a claim that it landed. Those are demoted by hand with
the reason written on the row, because no regex separates "that's what I saw" from "that's what I
saw, and here it is in the news today".

## Job B complete — 30 August 2026. Both A and B read zero.
Eight batches, 157 assertions adjudicated by this worker. Three findings worth keeping.
About a fifth of the "strong" queue was not a fulfilment assertion at all. Scripture narration
(Genesis 19, Ezekiel 37), teaching markers ("just like I said" mid-sermon on confession), personal
testimony about paying bills, and fresh visions introduced with "this is what I saw" all fire the
STRONG_CUE regex. These are now demoted to weak with a stamped reason rather than left in the queue,
which is what the new `strength` field on `cmd_fulfil` is for.
Two priority checks ran against the corpus itself and came out opposite ways. The Sooners word is real
and early: DNbjAj9RilM@5971, 17 June 2025, names South Korea and Japan and digital currencies together,
thirteen months before both legislated on 15 July 2026. The Yankees word is not: no Yankees passage
exists before 9 October 2024 and the World Series matchup claim first appears five days after the
series ended.
Seeded fourteen claims that existed in the corpus only as fulfilment assertions, and extracted anchor
mentions for every one so no claim is left orphaned: the Oklahoma quakes he says he called pre-channel,
Trudeau two-faced, the honey glow and white suits, children fifteen and under taken, Macron rising like
a Hitler, the China gospel window, the Tubman purple do-rag, the Santa Fe railroad bomb, the purple
dragon, a minister taken out in his own service, cryptos for car and house loans, the 911 system hack,
Bibles burned in a football stadium, and the senator dead the night after flying home from Russia.
Fixed the tally in `cmd_fulfil`, which counted linked rows of any strength against a strong-only
denominator and so printed 575 of 514 once demotions started.
selftest: ALL CHECKS PASS. Next: job C, tier 2 at 1.2 percent.

## Job B COMPLETE — 793 unlinked strong fulfilment assertions down to 0
Worked in twelve batches. 220 attached by autolink on alias match, 165 demoted by the corrected
cue_strength rule, and the rest adjudicated by hand: about half attached to the claim they point
back at, about half demoted with the reason written on the row.
The demotions are the finding. STRONG_CUE fires on "that's what I saw", which in this corpus is
overwhelmingly how he closes a description of a vision he has just received. A vision recounting is
a telling, not a claim that it landed, and treating the two as one thing is what made the queue 793
long. It also fires on Ezekiel 37 being read aloud, on a Kenny Rogers lyric, on a Trump clip about
finishing a ballroom on time, and on his own denial that he prophesied the Clarity Act timing.
Two fulfilment assertions pointed back at words that had no canonical claim, so the original
tellings were extracted first (911-system disruption from March and June 2026; the Bibles burned in
the field from June 2023 and located on site in November 2024) and seeded, rather than forced onto a
neighbouring claim. A third, the senator who went to Russia and died, is a priority claim the corpus
does not support and is recorded as such.

## Job C started — 30 August 2026. Tier 2, batch 1.
20 mentions from the 29 August 2026 Iran and Europe prayer session, 8 new claims seeded. Two rows are
worth flagging for anyone reading the thread later. sOD1l2-fKgA@4853 names Ursula von der Leyen by name,
after being told who she is, as the head of the witches talking directly to the devil; and
gGCKex1IOtE@134 puts a named head of state snorting cocaine among prostitutes with a hundred million in
cash on a plane. Both are unfalsifiable allegations about identifiable living people, which is a
different kind of risk from a missed date, and both falsifiers say so.
Two checkable errors recorded in the same session: Turkey is called a nuclear power, and Russia is said
to be about to use weapons never used before, when the Oreshnik had already been fired into Ukraine in
November 2024. Also noted that Montreux already bars non-littoral warships from the Black Sea in
wartime, so the Turkey blockade prediction describes existing treaty law.
Order note for the loop: `review` must land before or after `cluster`, but everything must end
adjudicated, because `cluster` writes lexical guesses that leave selftest red until they are superseded.

## Worker collision, and how the queue is now split — 30 August 2026.
Both workers ran `pick --tier 2` with no filter, got the same head of the queue, and independently
seeded three claims out of the same 29 August prayer session: ursula, the Democratic mole and the
Pergamon altar. Folded with `merge` (run 726), keeping the id that already carried the mention in each
case, so nothing was lost. To stop it recurring this worker now takes the oldest end with
`pick --tier 2 --until <date>` and the file prefix `c2o`, leaving the newest end to the other.
Batch c2o-01: 22 mentions from December 2023. Nine are scripture readings or teaching and are recorded
as no_claim with the reason written out, which is the honest way to mark them read: Deuteronomy 28,
Genesis 4, three consecutive Ezekiel 38 passages, the Abrahamic land grant read off a map, and the
Judeo-Christian founding argument. The Rosh-as-Russia identification in the Ezekiel reading is his gloss
and not the text, and that is noted on the row.
VoC0PUzQups@579 is the one with a number to check: tens of millions coming from Mexico. Southwest border
encounters across the whole of the Biden term were about 10 million, an order of magnitude short.

## NOTE FOR THE OTHER WORKER — two of us are on this database
Runs 705-720, 722 and 725 are not mine; runs 707, 709, 710, 715, 717, 721, 723, 724 and 727 are.
We collided on mentions-t2-01.json and reviews-t2-01.json and both loaded the same 20 passages,
which selftest caught. The 20 later rows are marked duplicate_of the earlier ones rather than
deleted, which is what the schema field is for, and ALL CHECKS PASS again.
To stop it happening twice: I am taking tier 2 from the OLDEST end with --until 2026-01-01 and
writing mentions-t2w-NN.json / reviews-t2w-NN.json / seeds-t2w-NN.json. If you are working newest
first, we meet somewhere in 2025 and neither of us clobbers the other's files.

## Batch c2o-02 and a loader guard — 30 August 2026.
20 more mentions from February and March 2024, 3 claims seeded: great-betrayal-of-israel (worth keeping
because he names the phrase people will use, which is unusually checkable), another-911-event-planned,
and northeast-record-heat-summer-2024.
qCWodRZNFaw@71 is the sharpest war claim in the old material: Russia uses a weapon never used before
against Poland, and when he assumed it was nuclear he reports being told it is not a nuclear weapon.
Excluding the obvious answer is a real narrowing and makes it checkable.
`load` now refuses any mention whose quote runs past fifteen words, alongside the existing falsifier
check. The rule was already in the goal and in selftest, but catching it only in selftest meant the row
was already in the database and had to be fixed with a hand UPDATE; three of those had accumulated
across both workers. It belongs in the extractor's paraphrase, and the error message says so.

## Tier 2 batches w01-w02 — 90 passages, 29 Dec 2025 back to 22 Dec 2025
Nine new canonical claims, the largest being cartel-mafia-turf-wars, which runs through the whole
29 December stream: territorial war between Mexican cartel networks and Italian-American organised
crime in Chicago, Boston, New Orleans and New York, with Sicily tied to Miami and one side presenting
as freedom fighters. Also great-humbling-of-america, middle-class-becomes-poor and
revival-minnesota-to-the-gulf, which is unusually specific geography for a revival word.

## Batches c2o-03 to c2o-05, and the best finding of the tier 2 pass so far.
three-city-attacks-ranked. On 27 and 28 October 2024 he named Nashville, Las Vegas and New Orleans as
the three cities he saw attacks in, and ranked them twice, unprompted: Nashville strongest with a Holy
Spirit check, Las Vegas next, New Orleans weakest and "one rather than many". Within four weeks of the
new year all three had an attack. New Orleans killed fourteen on Bourbon Street, Las Vegas killed only
its own driver, and Nashville killed one student at Antioch High School on 22 January. The list was
right and the ranking was exactly inverted. Scored PARTIAL_MATCH, because the ranking is the part that
carries information: it is the part that can be wrong while the list stays right.
northeast-record-heat-summer-2024 also PARTIAL_MATCH. Given 22 February 2024 for the Philadelphia and
New York area in summer, lasting maybe a week; the 30 June to 5 July heat dome set 148 daily records,
Philadelphia had three straight days above 101 for the first time in 151 years, and the event ran about
a week. Held at partial because heat records fall in the Northeast most summers.
Also recorded across these batches: a Psalm 83 and Isaiah 17 war letter read out by his wife from a
viewer's email, marked not-his-claim so the material has a provenance if it is later recalled as his;
the seventy-year grace period argument whose terminal date, 2015, was already nine years past when he
gave it; and oTgkGV03Ct4@961, no crops in any field from west to east, which is undated but would be
unmissable, making it one of the more checkable food claims in the corpus.

## Tier 2 batch w03 — 45 passages, 17-20 December 2025. Tier 2 now 338 of 5,824 (5.8%).
Six new claims. casing-six-flags-megachurches is the most checkable: a named park in a named suburb,
plus mega churches and the Vatican, with an on-air correction from Warner Brothers to Six Flags.
million-prayer-army gains its second measurement, 5,650 concurrent on 18 December.

## Tier 2 batch w04 — 45 passages, 11-17 December 2025. Tier 2 now 400 of 5,824 (6.9%).
python-constricting-america pulls together four passages across two streams: a snake perhaps a
thousand miles from the Gulf to Canada, wrapping the nation and pulling tight with ripples like
curtain folds. the-number-25 is recorded as unfalsifiable and kept because it recurs twice in
three days with no reading attached to it.

## Batches c2o-06 and c2o-07 — tier 2 at 7.2 percent.
The 28 January 2025 session is the fourth telling of the plague and the most detailed: a yellow liquid
like pudding injected into rats, rats chosen as the vector because they are more mobile, the pathogen
designed to keep the carrier alive longer, spread through the Middle East fading past Iraq and Iran,
American air travel suspended border to border, and an explicit ordering in which the euro and Europe's
money system collapse first and that is what triggers the dollar. Seeded euro-collapses-before-dollar
for the ordering, because a stated sequence is checkable in a way a general warning is not.
Two claims in these batches choose unusually testable examples and that is worth recording in their
favour: giyQsMPVfsI@2650 names the dead raised and an arm growing out as the signs, neither of which has
ever been medically verified; and T3Er0gUSNLU@781 names people driving a van from Mexico City to
Oklahoma, which would be visible at the meetings themselves.
drone-swarms-worldwide seeded with the priority noted on the row: given 13 December 2024, in the week
the New Jersey drone sightings were the dominant American news story.

## Tier 2 batch w05 — 45 passages, 9-11 December 2025. Tier 2 now 480 of 5,824 (8.2%).
The Ukraine thread takes eleven of the forty-five and now carries a contradiction inside one stream:
he sees a line drawn from Kiev down to split the country, and two minutes later reads the Ukrainian
president saying he will give up no land. Recorded as delta_type contradiction rather than smoothed.
venezuela-retaliation-act-of-war is the most falsifiable of the four new claims: an attack on
American soil that will be mistaken for cartel activity but is a state act.

## Tier 2 batch w06 — 45 passages, 3-7 December 2025. Tier 2 now 559 of 5,824 (9.6%).
One row is recorded as a contradiction against a standing claim: at aiP1Op78hE8@1477 he says the
dollar has to go away for the beast system to rise and that America is not coming back, which is the
opposite of america-will-remain. Kept side by side rather than merged.
banks-adopt-crypto-lending names three banks and is checkable; blisters-plague-new-york names a
presentation, a city and a hospital ship.

## Batches c2o-08 to c2o-10 — tier 2 at 9.6 percent.
The 15 June 2025 session, two days into the Israel-Iran war, produces the clearest internal
contradiction found so far. On 30 April 2025 he saw China as the godfather and North Korea as the
hitman carrying out a Pearl Harbor attack on America; on 15 June he says he told them Trump and Kim
would be like Jonathan and David. Both are now on file as separate claims with the conflict noted on
each, rather than folded into one.
Also seeded: watch-omaha, a bare city name given with the Pearl Harbor framing and nothing attached,
which is worth keeping because Omaha houses Strategic Command; california-megachurch-scandal, given
eight months before Bethel Redding suspended Ben Armstrong; green-lasers-golden-dome, with the note
that the Golden Dome programme had been announced publicly three weeks earlier; and
vatican-split-whitening, which is recorded in his favour as much as against him, because he states
outright that he does not know the year and rules out the current one.
Two allegations about identifiable living people are flagged on their rows as unfalsifiable and
unsupported: a named financier behind the June protests, and a named head of government described as
manipulated by cartels.
Method note that is holding up well across the pass: a passage where he reads a published forecast or
schedule is recorded as no_claim with the source named, so that if the same date is later recalled as
a word, the provenance is already on file. Eight of those so far, including a National Weather Service
storm forecast read out and interpreted as weather manipulation.

## Tier 2 batch w07 — 45 passages, 29 Nov to 3 Dec 2025. Tier 2 now 621 of 5,824 (10.7%).
The New York material now runs as three interlocking claims rather than one: grid-cyberattack for the
dark buildings and the Toronto-to-Miami outage, blisters-plague-new-york for the boils and the
hospital ship, and nyc-subway-attack-morning. He gives them in the same breath but they are separate
events and are kept separate.

## Batches c2o-11 and c2o-12 — tier 2 at 11.0 percent.
putin-wants-ukraine-and-poland seeded from w3lzakaovU0@2612, 9 July 2025: he wants all of Ukraine and
all of Poland in the days ahead. Poland is in NATO, which makes this the single most consequential
element in the war material and one of the few with a party, a target and a direction all named.
land-for-third-temple-accord seeded from -RS1-Cvy6lc@478: the Arab nations agree a peace accord under
which the temple can be built in exchange for a stated amount of land. A trade with two named sides is
checkable in a way that "a peace agreement is coming" is not.
Three passages recorded with the source of the image named rather than left as fresh revelation: the
Fort Worth building on fire, which is a standing story in revival folklore; New York burning, where he
names David Wilkerson himself in the same breath; and Damascus a ruinous heap, which is Isaiah 17.
-sXXTGfEybA@7091 is the clearest example in the corpus of the structure that makes the war material
unfalsifiable: having just said war is rice paper thin and could escalate beyond anything in this
generation, he declares in prayer that their sons and daughters will not fight in it and there will be
no major uprising. Either outcome now confirms something he has said.
One factual correction recorded on its row: the resource in the Mediterranean off Gaza is gas, not oil.

## Tier 2 batch w08 — 55 passages, 24-29 November 2025. Tier 2 now 694 of 5,824 (11.9%).
Eight new claims, most of them from the 26 November drones stream: tear-in-manhattan,
building-44th-floor, demonic-octopus-europe and umbrella-with-holes-prayer, which is the one worth
keeping for its structure, since a covering with holes in it explains any outcome either way.
france-england-simultaneous-strike and suicide-vests-in-churches are the falsifiable ones.

## Batches c2o-13 and c2o-14 — tier 2 at 12.5 percent. Checkpoint.
five-cities-attack-plan seeded from YzT65um6tn8@413: a well-thought-out plan against Chicago,
Philadelphia, Washington DC, New York and Boston. Five named cities is as specific as the security
material gets, and the depth is withheld, which is the part that cannot be checked.
newsom-removed-early is the most falsifiable political claim found in the tier 2 pass. He says the
California governor's days are numbered, states outright that he means removal and not death, and
rejects the political-violence reading himself. The term ends January 2027, so this one can expire.
dollar-is-done-no-saving-it is the most absolute form the dollar claim takes anywhere in the corpus:
the dollar is done, there is no saving it, America is not coming back. Given without the prayer
condition he attaches to almost everything else, and with an acknowledgement that people are angry with
him for saying it.
Two contradictions parked rather than merged, per the rule. The lizard bloodline material of 29 October
2025 runs against the existing chameleon-not-reptilian claim and is filed as a contradiction beside it.
And the North Korea thread now holds three incompatible positions on file: the hitman who attacks
America (30 April 2025), Jonathan and David with Trump (15 June 2025), and rising suddenly against
America again (9 July 2025).
Second permanent withholding recorded: U8IAGFgZGEA@3086, material he says he will never be able to talk
about publicly, alongside the withheld Israel and Iran targets. Both are on file as unfalsifiable with
the reason, because stated-and-withheld detail is the one form that can never be checked either way.

## Tier 2 batch w09 — 55 passages, 20-24 November 2025. Tier 2 now 785 of 5,824 (13.5%).
The 22 and 23 November streams give the same glory-wave material twice, so both tellings are
extracted and assigned to the same claims rather than one being dropped: that is what makes a
restatement countable later. america-divides-three-days gains its hardest form here, a catastrophe
within three days of any American president signing a land-division agreement, which is one of the
few conditional claims in the corpus with a stated interval.

## Tier 2 batch w10 — 55 passages, 14-20 November 2025. Tier 2 now 870 of 5,824 (14.9%).
Two collisions with the other worker handled and then automated. Eighteen passages had been
extracted twice within minutes and review refused them as ambiguous, which is the right refusal;
t2review.py now turns it into a decision, marking the later row duplicate_of the earlier one.
The other worker also folded berlin-pergamon-antichrist-seat into pergamon-altar-berlin while my
assignment was live, which selftest caught as a live assignment pointing at a folded claim; the
assignment is re-pointed at the survivor. cmd_review had a bug on that path, printing
it['video_id'] on a row keyed by mention_id, and now falls back to the id.

## Tier 2 batch w11 — 55 passages, 5-11 November 2025. Tier 2 now 923 of 5,824 (15.8%).
Thirty of the fifty-five came back as duplicates: the other worker has come down from 2026 and is
now in the same November 2025 material I am. That is wasted effort on both sides, so I am moving to
the OLDEST unread end and working upward, starting with 2023 and the first half of 2024. If you are
reading this: I will take everything before 2025-01-01 first, then work forward. Everything after
that date is yours until we meet.

## Batches c2o-15 to c2o-18 — tier 2 at 16.4 percent. Batch size raised to 30.
Method note: the Bash tool wraps commands in single quotes, so a heredoc containing an apostrophe
breaks the whole command at parse time. All JSON files are now written with the file writer and Bash is
used only for the CLI calls. Two batches were lost to this before it was diagnosed.
wilkerson-new-york-fires is the borrowing case to keep. On 9 November 2025 he reads David Wilkerson
aloud, including the thousand fires per borough and the two week transport shutdown, and then says
"that is exactly what I saw." The direction of borrowing is recorded on each row: he confirms his vision
against a text he has just read, not the other way round. The four New York fire tellings of 6 to 11
November all sit in that shadow.
ukraine-to-new-york-harbour-bomb and newyork-grid-goes-dark seeded as the two specific New York claims
worth scoring separately from the general burning imagery. btBCeTHs7Qg@5522 is the methodological find
in this run: he says outright that he will go and find the building he saw by searching for it, which
is identification after the fact and is now on file as such.
japan-crypto-national-reserve seeded from the tilled field and the coin on the stalk, alongside a
restatement of the Sooners word eight months before Japan and South Korea both legislated on 15 July
2026. mystery Babylon parked as a contradiction against america-not-babylon rather than merged.

## Tier 2 batch w12 — 55 passages, Oct 2023 to Feb 2024. Tier 2 now 1,008 of 5,824 (17.3%).
Zero duplicates after moving to the oldest end, which settles the partition. Fifteen of the
fifty-five are another person's material read aloud, a submitted angel dream on 28 January and a
guest interview on 24 October, and all fifteen are recorded no_claim: a dream someone sends in is not
his telling, so the California earthquake inside it is deliberately not added to california-big-one.
Four claims gain their earliest known telling here: apollyon-war-2025 from January 2024 rather than
June 2025, ice-storm-november-11-word from January 2024, drone-attacks-holiday-crowds from November
2023, and new-madrid-quake at 6.5 on the Texarkana-Tulsa line against the 10.0 he gives in 2025.

## Tier 2 batch w13 — 55 passages, July to October 2023. Tier 2 now 1,122 of 5,824 (19.3%).
The earliest material in the corpus, and it back-dates a lot: china-attacks-hawaii, syria-red-soldiers,
grid-cyberattack, mideast-us-draft, warsaw-ww3-trigger, land-of-israel-warning, gas-eight-dollars,
city-exodus, saudi-brics-oil-200 and revival-not-trump-saves-america all now have a 2023 first
mention. XxwF--X7PLo@2246 is worth keeping: asked about Taiwan in September 2023 he says plainly that
he does not feel anything about it, which sits against the later Taiwan material.

## Batches c2o-19 and c2o-20 — tier 2 at 19.3 percent.
The most important row extracted in the whole tier 2 pass so far is QUSXR54lEmI@2657, seeded as
delay-but-not-stop: "he can delay it but he will not stop it altogether. He is buying you time." That is
the structural key to the corpus. It means no dated claim can ever expire on his own terms, because a
missed date is always a delay rather than a miss, and it is stated by him rather than inferred.
vatican-mothership is the most checkable single claim found in the tier 2 pass: a massive craft
hovering over a named place, moving at the speed of sound, which he corrects himself down to from the
speed of light. It either happens or it does not.
Also seeded: scorpion-tail-commonwealth-persecution (England, Canada, Australia, New Zealand named),
stores-burned-in-riots (Nordstrom and Macy named ahead of Saturday 1 November 2025, which passed
without them), kremlin-struck-moscow-flees, and kentucky-to-alabama-ice-storm, where the track is the
scoreable version and his own widening to "the most unlikely places" removes the geography.
Three near-identical passages from 29 October, 30 October and 11 November were traced to their earliest
telling and linked to one claim each rather than three: the Ukraine money arrow, and the Imagine and
flash over New York.

## Tier 2 batch w14 — 55 passages, July to September 2024. Tier 2 now 1,294 of 5,824 (22.2%).
Eleven new claims, most of them earliest tellings: decamillionaires-raised-up, economy-braxton-hicks,
green-train-germany-paris (given eleven days before the French rail sabotage, which was arson on
signalling cables and not a device on a train, so it is a partial at best), next-virus-engineered-in-a-lab,
north-korea-liberation, obama-europe-steering-the-economy, israel-deliverer-victory-celebration.
Two worth flagging. never-quote-dates-again is a pre-commitment made 5 September 2024 that the later
corpus breaks repeatedly. trump-bullet-by-the-ear is seeded from two tellings on 13 and 14 July 2024
only: the archive holds no telling of the ear detail before the Butler shooting, which is recorded in
the claim description so nobody reads the retrospective as a prior word.
Three read-alouds caught in one video: 5zzNSGo9zXk@402 and @1199 are other people's words and dreams
played on air, and Qr7i73zy-60@1106 is a dated 2019 word by another writer read aloud in full.

## Batches c2o-21 to c2o-25 — tier 2 at 22.7 percent.
Two passages in this run show where the material comes from, and both are recorded as no_claim with the
provenance on the row. RYFAcRrLZNg@7860: having named Romania in tongues, he asks whether Romania is
close to Ukraine, is told they share a border, and apologises for not being good at geography. And
RegH2dxYBI8@1382: a 2019 magazine cover is offered as confirmation of the China and Zelenskyy material,
with a disclaimer in the same breath that he is not mixing the prophetic with the world.
I3CfQxKRd30@1457 is the companion to delay-but-not-stop: "as we are able to divert things, stop things."
Together they are the two halves of why nothing in the corpus can fail. A missed date is a delay; an
absent event is a diversion.
9VcafaPXeBI@3195 is recorded in his favour: he says outright that without being grounded, fear will
dominate a hearer to the point of not living a normal life, "even by what I am saying." That is an
unusual acknowledgement of the effect of his own material.
Seeds worth flagging: cubans-recruited-to-fight (two thousand a head against a twenty dollar monthly
wage, both checkable), campus-revival-named-universities (six institutions named),
pentagon-message-to-europe, glory-events-fill-arenas (measurable against published attendance), and
canada-revival-out-of-persecution, where the order persecution-then-revival is the scoreable part.

## Tier 2 batch w15 — 55 passages, 10 November to 1 December 2024. Tier 2 now 1,439 of 5,824 (24.7%).
Eight new claims: rfk-exposes-fda-food-corruption, withheld-cures-released, goshen-light-egypt-darkness,
christians-taken-blamed-on-aliens, putin-comes-to-god, england-new-year-darkness,
dome-over-america-blessing-israel, national-debt-turned-around.
england-new-year-darkness came in already past due, because it carries a real window (31 December 2024)
and the batch pushed Job A back to 1. Scored the same turn as evidence-a08: London's show ran, the
Fire Brigade's own log for the night is a flat fire, an outbuilding, a house and some firework calls,
and Counter Terrorism Policing has no England plot for that date. EXPIRED_WITHOUT_MATCH on three rows.
The New Orleans attack on 1 January 2025 belongs to three-city-attacks-ranked, not to this one, and the
rationale says so, because folding it in here would launder a miss into a hit.
Note for anyone loading tier-2 mentions: a window_end in the past re-opens Job A. Score it in the same
batch rather than leaving it for the next reader.

## Batches c2o-26 to c2o-28 — tier 2 at 25.2 percent, doubled since the checkpoint.
netanyahu-assassination-attempt seeded from OUtFzN2qZuo@990, 16 September 2025: watching out of Germany
he saw an attempt on the Israeli prime minister in the days ahead. A named individual and a named act,
which puts it among the most checkable security claims in the corpus.
tZEOxoJMC90@711 is the economic form of delay-but-not-stop: "nothing is going to stop the boat from
going over the edge concerning the United States. It can be delayed." Linked to that claim rather than
to the crash thread, because the structure is the point.
Three factual corrections recorded on their rows: no American jurisdiction recognises Sharia law and
the Dallas development he cites was a residential community rather than a temple; a single unfilled
silver order of 700 million ounces would be near a full year of world mine supply; and the resource off
Gaza is gas rather than oil.
Two more provenance rows worth keeping. EsOP5PELruU@1392: he says he knew in the spirit that a major
thing would happen that day, and the event was a memorial scheduled and publicised weeks earlier.
tZEOxoJMC90@5082: he sees the week of the 23rd, which was the published UNGA high-level week.
And one in his favour: nWDkKhiPKQ8@3529, where he says plainly that the virus material was fresh on his
mind because of the illness he had been through the week before.

## Tier 2 batch w16 — 55 passages, 18 January to 15 February 2025. Tier 2 now 1,613 of 5,824 (27.7%).
Fourteen new claims. The scoreable ones are trillion-into-crypto (a trillion dollars of US government
money into crypto inside the term, window to January 2029, so it can actually be settled),
dinar-revalue-disappointing, two-nyc-towers-collapse, mushroom-cloud-over-new-york,
macron-schwab-removed-soon (already split: Schwab left the WEF in April 2025, Macron did not go).
Three claims made after the fact and marked as such in the claim description so nobody mistakes them
for prior words: solana-called-at-forty (told after both the coin launch and the price move, no earlier
telling in the archive), the XRP telling he says was private to his son, and trudeau-two-faced picking
up the removal fifteen days after the resignation was announced.
Worth keeping: YA7dPUR6vRM@1584, where he is asked about Greenland the week it was in every headline
and says plainly he has seen nothing about Greenland, Iceland or Denmark. A refusal to claim is as much
a part of the record as a claim.

## batch c2o-31 (run 830/832)
30 mentions from 7-10 Sep 2025 (ZFwv_xijl7Q, LIjv2T9HRxc, LFTGvfFA6vE). Seeded bc-quake-30000-dead,
suppressed-cancer-cure, azusa-pillars-worldwide, russia-subs-nuclear-base-cuba. LIjv2T9HRxc@1264 is the
only telling where the British Columbia quake carries a toll (30,000), tied to Canada backing the
two-state solution; Canada recognised Palestinian statehood 21 Sep 2025 with no quake, so this is the
scoreable version of that thread. LIjv2T9HRxc@1077 records him reading the UN high-level week dates off
the published calendar, which is where the September dates in this corpus come from. Tier 2 27.7%.

## Tier 2 batch w17 — 55 passages, 31 March to 14 April 2025. Tier 2 now 1,668 of 5,824 (28.6%).
Seven new claims: panorama-of-history-shown, kim-jong-un-removed, red-dragon-flames-south-korea,
axis-covenant-nk-china-russia-iran, horsemen-riding-abreast, biggest-red-wave-2026,
world-will-know-end-times.
The hardest thing in this batch is the Canada material. Caz8kj-WfcU@2963 is the sharpest political
claim in the corpus so far: the Conservatives win by a landslide, the greatest victory in Canadian
history, given 2 April 2025 with a thirty day window he attributes to the Lord. The Liberals won on
28 April. canada-election-april-2025 already carried evidence, so Job A did not re-open, but the
mention rows now carry that window and the miss is in falsify_miss where a reader will find it.
Two places where he narrows his own claim rather than widening it, and both are worth keeping:
LLfEcrp0TWs@901 rules out the Iceland, Alaska and Hawaii eruptions as not the major volcano he meant,
and 6cQeEjQZPrY@1028 rules out a coast to coast grid failure. Narrowing cuts against the usual pattern.
OvEIqBmJLjo@1999 is him citing Jeremiah 23 against prophets who say America has fifty good years left,
filed under hundreds-of-false-prophets with a note that his own short horizon is the mirror image.

## batch c2o-32 (runs 835-842)
33 mentions from 28 Aug - 7 Sep 2025 (oBpaSk7EJGE, 0qDOz_f0xhk, WjzHte1MzLA, s0WAsL-TZgA, LFTGvfFA6vE).
Seeded 13, including canada-mexico-financial-union, winter-olympics-italy-2026, putin-five-cards,
netanyahu-pushed-out-war-crimes and newsom-trafficking-blind-eye. Correction carried in the same batch:
WjzHte1MzLA@1157 on 30 Aug is the earliest telling that carries the 30,000 figure for the British
Columbia quake, so it takes first_mention and the 9 Sep two-state telling was superseded to new_detail.
Also folded january-parchment-signing into trump-january-scroll (merges-dupes-3.json), same January
scroll and golden quill scene seeded twice. Tier 2 30.1%.

## Tier 2 batch w18 — 55 passages, 7 to 20 May 2025. Tier 2 now 1,753 of 5,824 (30.1%).
Four new claims: snapping-turtle-south-america (a turtle the size of the continent, mouth open, facing
northwest at the Panama Canal, given in tongues and never interpreted), middle-east-superpowers-of-the-earth,
notre-dame-bells-france, putin-comforts-venezuela.
Three tellings in this batch follow the news rather than precede it, and the mention rows say so:
474imccihxY@240 and @2039 on the China trade deal, given the same day the Geneva pause was announced;
kB0D3FLQzjY@573 on Russia delisting the Taliban, which happened in April; VJAi5vUnqXc@407 recounting a
word about Pope Francis being removed, told three weeks after he died.
kB0D3FLQzjY@144 is the cleanest example of the reversal move in the corpus: he warned of prescription
shortages, prices were cut instead, and he reads the opposite outcome as the prayer working.

### Operational note, and it cost a batch
`t2review.py` with no run id takes the latest extract run, which is not necessarily mine. The other
worker loaded run 839 between my load (838) and my review, so the first pass applied nothing and
selftest failed on four orphaned seeds. Always pass the run id printed by `load`:
    python t2review.py reviews-t2w-NN.json <run_id_from_load>

## Tier 2 batch w19 — 55 passages, 16 to 20 June 2025. Tier 2 now 1,838 of 5,824 (31.6%).
Six new claims: megaton-bomb-tel-aviv, grey-ash-louisiana-to-canada, st-louis-street-revival,
wealth-transfer-blockage, mega-preacher-shot-on-stage, north-korea-secret-weapons.
The 20 June live stream is the closest thing in the corpus to a dated hit worth checking properly.
wXB8hIipAm8@797 names Saturday inside a forty eight hour window, praying over America's protection
from retaliation for the decisions about to be made. The American strike on Iran came on Saturday
21 June. He also withholds the content because he is live, so what is testable is the day and nothing
else, and the mention row says exactly that. Two days earlier, DNbjAj9RilM@514 matched a news clip of
the mountain range to a black and white arrowhead missile he says Israel would get from America.
Against that, the same 17 June video has Damascus days or weeks from destruction, gas at eight dollars
average and 1970s queues in California. Pump prices fell after the strikes.
DNbjAj9RilM@1054 is the scoring rule he sets for himself, and it is worth having in the database in his
own words: what does not arrive was prayed off, what does arrive was seen. Filed under prayer-can-stop-it
with a note that under this rule no miss can count.
Six read-alouds in one video (DNbjAj9RilM 1217 through 1600), including the same November 2019 Iran
word he read in August 2024. Marked no_claim again.

## batch c2o-33 (runs 845-847)
31 mentions from 22-28 Aug 2025 (s0WAsL-TZgA, u5z9li0Tli4, XPxVFD219vg, 6Qwj2sJz6Pg, zCy_S-eSX1c,
33JdXhIQEhU). Seeded 15. This stretch is the revival material, and the useful part of it is that he
names churches: Living Word in Minnesota, Collinsville, Branson, Fort Worth, Eagle Mountain and Karis
in Colorado Springs, the same list twice three days apart, which makes azusa-strong-points-named-churches
the one revival claim here that can actually fail. Also recorded greater-the-blue-greater-the-revival as
a stated rule rather than an event, since it can be tested against affiliation data. Tier 2 31.6%.

## Tier 2 batch w20 — 55 passages, 17 to 25 July 2025. Tier 2 now 1,893 of 5,824 (32.5%).
Eight new claims: china-owns-american-farmland, epstein-files-blackmail, texas-granite-border-walls,
new-york-is-mystery-babylon, virus-makes-cash-untouchable, crypto-wave-ride-then-ends,
portraits-turning-white-falling, rock-watched-by-telescopes.
new-york-is-mystery-babylon is a straight contradiction of his own america-not-babylon and is filed as
a separate claim with a note in both directions. Not merged. He acknowledges the dispute himself on air.
GutoJCzTR1w@1531 and @1569 are David Wilkerson's own recording played on the channel, and @1610 is him
saying immediately afterwards that it is exactly what he saw. The two are kept apart: the recording is
no_claim, his agreement is a mention on wilkerson-new-york-fires with a note that the match is asserted
after hearing the older word.
Two concessions worth having: qkyOlKNbbRM@44, where he says plainly the Syrian biological attack has not
happened yet, and @397, where the white van turned out to hold fuel rather than the fertilizer he saw.
Against that, @201 credits prayer for an Alaskan tsunami that never came, which most 7.2 quakes do not
produce anyway; the base rate is in the mention row.

## batch c2o-34 (runs 852-855)
47 mentions from 6-22 Aug 2025 (33JdXhIQEhU, gt4gZKcM2ok, 6AeFw0gJitg, -sXXTGfEybA, 9gOisW0RG9k,
IVb47s4Wi8w, cr4is0_bL14). Seeded 19. Two rows here are worth flagging as unusually scoreable:
india-77-earthquake gives a magnitude and a place together (central India is a stable craton with no
recorded 7.7, so this one can genuinely fail), and sports-teams-file-bankruptcy names three franchises
when no NFL or NBA team has ever filed. three-new-trillionaires is recorded with delta_type contradiction:
he names a Saudi prince on 6 Aug and corrects it to an Emirati on 8 Aug, and a changed named party is
kept side by side rather than smoothed. The load guard caught a 17-word quote before it reached the DB.
Tier 2 33.3%.

## batch c2o-35 (runs 859-865)
46 mentions from 16 Jul - 6 Aug 2025 (cr4is0_bL14, lCLVyqIexNQ, 5z227rP47nY, EkYyosFG8WU, Zr5Rb79dbd0,
xUTlHLlBy_g, qkyOlKNbbRM, BW7DXgEMZHM). Seeded 16. mount-fuji-explodes names the volcano, which is the
strongest form that claim can take; ring-of-fire-mega-quakes has to beat the 1960 Chile 9.5 to count.
Corrected greater-the-blue-greater-the-revival: the 26 Jul telling at xUTlHLlBy_g@831 is the earliest and
names nine places, so it takes first_mention and the 28 Aug row was superseded to new_detail.

WORKER COLLISION, second occurrence. The other worker's mentions-t2w-21 landed on cr4is0_bL14 and
lCLVyqIexNQ two minutes before mine, so 14 of my review rows came back ambiguous. Both readings are kept
(append-only), and mine were re-issued keyed by mention_id in reviews-c2o-35-keyed.json. They have moved
into the old end of the queue, so from batch 36 this worker draws with --until 2025-06-30 to get clear of
them. Tier 2 34.0%.

## Tier 2 batch w21 — 55 passages, 4 to 19 August 2025. Tier 2 now 1,952 of 5,824 (33.5%).
41 of 55 rows came back marked duplicate. The other reader is working this same band, so this batch is
mostly a second opinion rather than new coverage. Three consequences, all resolved:
1. Three of my seeds were duplicates of theirs and are folded, with the reason in the merge note:
   canada-venereal-disease into std-judgment-child-abusers, europe-wants-war-for-economy into
   europe-wants-war-for-economies (differing only by a plural), and black-onyx-pillars-economy into
   three-new-trillionaires. Their reading of the onyx pillars as the three men is better than mine:
   three pillars, three trillionaires named ten days earlier in the same channel.
2. Five of my assignments had superseded theirs on the lCLVyqIexNQ passages and left five of their
   claims orphaned. Their ids are finer than the broad ones I used, so I re-pointed my mentions to
   natural-shaking-mirrors-spiritual, iron-curtain-short-window-north-korea, catholic-church-revival-youth,
   shadow-meeting-north-korea-cuba and ring-of-fire-mega-quakes rather than keeping my own.
   Where two readers disagree and theirs is more specific, theirs wins.
3. Partition changed. August 2025 is theirs. Going back to the October and November 2024 gap between
   batches w14 and w15, which nobody has read.
Worth keeping from the batch itself: IVb47s4Wi8w@711, where he corrects his own earlier identification
of the trillionaire from a Saudi prince to a UAE figure. A named correction is rarer than a named claim.

## batch c2o-36 (runs 868-869)
45 mentions from 28-29 Jun 2025 (Ihnq3063uwk, 9epckXNXLN0). Seeded 13. The two sharpest rows in the
corpus so far both come from 9epckXNXLN0: new-madrid-1800-dead-ou-building gives a death toll and a
named building, and america-divides-three-days gives a three day interval, though the clock only starts
if Jerusalem is formally divided. china-earthquakes-65-61 records two magnitudes at once. Corrected
popcorn-revival-uncontrolled: the 29 Jun telling is the earliest, so the 26 Jul row was superseded to
new_detail. Tier 2 35.8%.

## Tier 2 batch w22 — 55 passages, 1 to 10 November 2024. Tier 2 now 2,083 of 5,824 (35.8%).
Zero duplicates, so the October and November 2024 gap is clear and is where I will keep working.
Four new claims: religious-freedom-restored, twenty-days-prayer-for-his-salvation,
celebrities-flee-america, two-forks-tried-versus-god.
Two claims came in already past due and both were scored the same turn, as evidence-a09.
twenty-days-prayer-for-his-salvation is unusual because the subject IS named: the passage a minute
earlier says plainly "we must pray Elon must to be born again", so the claim description names him and
the word is scoreable rather than anonymous. Twenty days from 10 November closes on 30 November 2024,
and nothing of the kind happened; the cultural Christian remark he might be pointed at is from July,
four months before the word, and that is recorded so it cannot be read back as a fulfilment.
EXPIRED_WITHOUT_MATCH.
extended-time-grant is the first PARTIAL_MATCH in a while that is genuinely arguable. He said on
1 November 2024 that the decision was made, more time was allowed for a harvest, and great revival
would break out in the first year. Barna's 2025 data is real: Gen Z weekly Bible reading 30 to 49
percent in a year, church attendance up on 2020, Bible sales at a twenty one year high, young men
outpacing young women for the first time in twenty five years. Held at partial, not strong, for two
stated reasons: it is a recovery toward pre-2020 levels rather than an outpouring, and the trend was
already running before the word. The dissenting Christian Post analysis is loaded alongside on purpose,
because scoring this only on the favourable surveys would be selection.
Two self-corrections in one video worth keeping: tFFlHZ2MSR4@524 corrects gulf to Mediterranean, and
@3122 corrects twenty five billion to two hundred and fifty billion mid-sentence.
tFFlHZ2MSR4@3964 is the two-path structure in his own words, a fork where either outcome confirms the
vision. Seeded as two-forks-tried-versus-god so the pattern is findable rather than buried.

## batch c2o-37 (runs 875-877)
45 mentions from 23-28 Jun 2025 (9epckXNXLN0, YhiFk3_wPn0, WC9nwG5RyQw, tn5Qj0ChagE). Seeded 13.
gas-nine-dollars-a-gallon needs a near doubling of the June 2022 record American average, which makes it
one of the harder numbers on file. Two more first_mention corrections carried in the same batch:
great-oil-in-the-gulf and iron-curtain-short-window-north-korea both have 25 Jun tellings that predate
the rows I had flagged, so the later ones were superseded to new_detail. Also recorded
great-betrayal-still-coming as a claim in its own right, since "wait, it's still coming" with no date is
the mechanism that keeps an unfulfilled word open. Tier 2 37.5%.

## Tier 2 batch w23 — 55 passages, June to November 2024, the pre-election run plus three older videos.
Tier 2 now 2,182 of 5,824 (37.5%). Zero duplicates.
Three new claims: lending-freeze, back-to-family-roots, sydney-harbour-attack.
This batch back-dates six claims that had later first mentions in the database: iran-cave-bioweapon and
iran-refineries-struck and green-train-germany-paris and plots-against-churches all move to 15 June 2024,
saudi-brics to 20 June, seven-deadly-pillars-2026 to 6 July, south-korea-revival-hub and
covenant-with-founding-fathers-restored to the autumn. The green train is now a month earlier than the
telling I logged in w14, and the mention row says so.
Two election claims sit on either side of the line. landslide-quick-result was given four days before
the vote and the race was called inside a day, which is a hit on the mechanism if not on anything hard.
ted-cruz-senate named Texas and Pennsylvania and only those two, which are the two closest races on the
board, and both went red. The blue wave of corruption phrasing is a hedge built into the claim and the
mention row says so.
p2Fr3ecBBeo@343 is the Coachella arrest, which did happen on 12 October 2024, at a Trump rally rather
than at the festival he named. Recorded as a new_detail with the difference stated rather than smoothed.

## Tier 2 batch w24 — 55 passages, April to June 2024. Tier 2 now 2,282 of 5,824 (39.2%). Zero duplicates.
Three new claims: government-issued-tents-migration, red-dragon-crosses-america, things-only-get-worse.
The big finding is two re-uploads that were being read as separate tellings:
- zaaGhutoKz4 (27 May 2024) and aYYsPG5pZng (13 February 2025) are the same recording. The grid word,
  the three times in a fortnight, the three weeks of darkness and the New York or Chicago hedge are all
  nine months older than the database had them. grid-cyberattack now first mentions in May 2024.
- 2WZdJvTAHOc (15 April 2024) and vxxg7gDtOS4 (15 June 2024) are the same recording. That moves
  iran-cave-bioweapon, iran-refineries-struck, green-train-germany-paris, plots-against-churches,
  antisemitism-peak, east-coast-storm-newyork-to-miami and olympics-protection-2024 to 15 April 2024.
Both are recorded in the mention rows so nobody reads the later upload as a fresh word.
things-only-get-worse is seeded deliberately as its own claim rather than folded into anything: on
21 May 2024 he says flatly that anyone telling people things will get better is not reading their Bible
and that he never anticipates improvement. That is the opposite of good-year-2024, reprieve-four-years
and respect-restored-to-america. Contradictions stay separate.
6soUjaKjKfQ@1553 is the one place he suspends his own prayer rule: the Ezekiel war cannot be prayed
away because it is biblical. Filed on prayer-can-stop-it as a new_detail, because the exception tells
you as much about the rule as the rule does.
Selftest reports two orphaned claims, sun-explosions-fearful-sights and preachers-drop-dead-in-pulpits.
Neither has ever had an assignment and neither is mine; they are the other reader's seeds waiting for
their load. Not touching them.

## batch c2o-38 (runs 881-884)
47 mentions from 13-23 Jun 2025 (tn5Qj0ChagE, FUjrrRVRt5M, Q5gEmETa1sY, -cgLSUAayx4, ygBayT9gQFk).
Seeded 13. The one that matters here is called-saturday-strike-on-iran: on 22 Jun he says the Lord told
him Saturday three times and that he saw America striking Iran that night, and in the same breath says he
never relayed it publicly because he filters the live streams. So the specific version he takes credit
for was, by his own account, not said in advance. Recorded that way rather than as a hit or a miss.
Two dated rows are now scoreable against what happened: he named Monday to Thursday for Hormuz
disruption pushing oil up, and oil fell sharply that week; and california-9-0-quake gives a magnitude the
San Andreas cannot physically produce. Tier 2 39.2%.

## Tier 2 batch w25 — 38 passages, June 2023 to April 2024. Tier 2 now 2,314 of 5,824 (39.7%).
That is the whole remaining pre-April-2024 tier-2 pool. The oldest end of the corpus is now closed.
Two new claims: plague-hits-the-unhealthy, heat-sensing-drones-hunt.
This batch is mostly archaeology, and it moves a lot of first mentions back:
lion-on-the-stock-exchange to 29 June 2023, two and a half years before the telling that was standing
as the first; great-betrayal-of-israel, red-dragon-crosses-america, novel-weapon-catastrophic,
apollyon-war-2025, warsaw-ww3-trigger and arab-ground-war-against-israel all to 1 July 2023;
east-coast-storm-newyork-to-miami and new-madrid-quake and caribbean-islands-covered to 29 June 2023;
euro-trouble to 30 June 2023 with the year named, and the euro held; asia-revival and
mark-world-currency and third-temple-build and pergamon-altar-berlin to the 2023 tribulation vision;
new-york-is-mystery-babylon to 4 April 2024; martial-law-cities and grocery-shortage and
middle-east-superpowers-of-the-earth to 7 April 2024.
2MOBOMGnCdE@504 also gives the other reader's preachers-drop-dead-in-pulpits its first assignment, so
that orphan is closed as a side effect rather than by me touching their work.
selftest ALL CHECKS PASS. export_view run, 4,422 KB.

## batch c2o-39 (runs 889-891)
46 mentions from 6-13 Jun 2025 (ygBayT9gQFk, zz3aEtVV9fM, mFOTQcAKR7g, oZaUcDd2izA, OLDaeVaMw6E,
Nbo94h0Lsaw, bh5qXAKfSpM, VVe9S5V9pXo). Seeded 11. june-14-protests-dwindle is the cleanest dated miss
found so far: on 13 Jun he says the protests on the 14th will dwindle to nothing and fall apart, and the
No Kings demonstrations the next day were among the largest single-day protests in American history.
zz3aEtVV9fM@624 on 12 Jun is the strongest thing on the other side of the priority question: he says
plainly he has seen Israel and America strike Iran, a day before Israel did and nine days before America
did, with no date given. Four more first_mention corrections (pakistan-afghanistan, iran-infrastructure,
israel-hidden-technology, seed-harvest-acceleration) all move to 11-12 Jun tellings. Two Kim Clement
clips recorded as no_claim under the rule that a clip he plays is not a claim he makes. Tier 2 40.5%.

## Tier 2 batch w26 — 55 passages, 18 December 2024 to 1 January 2025. Tier 2 now 2,459 of 5,824 (42.2%).
Zero duplicates. Six new claims: trump-tames-the-dragon, golden-gate-bridge-attack,
north-korean-troops-to-russia, ukraine-files-burned, robot-soldiers-replace-troops, terror-attacks-europe.
The last of those is seeded with its own weakness in the description: attacks starting to try to take
place in Europe, no country, no city, no date, and Europe has attempted attacks most years.
AEeRd06pWWU@468 is the tightest political claim I have found in this corpus. On 1 January 2025 he says
he saw Trudeau removed from his position and Canadians interceding for it. Trudeau announced his
resignation on 6 January, five days later. It is filed as a new_detail on trudeau-two-faced with the
gap stated, so a reader can weigh it without me weighing it for them.
Against that, the same session pairs Trudeau with Macron as both being dealt with. Trudeau went.
Macron did not, and that is in the mention row too.
AEeRd06pWWU@1374 is another narrowing worth keeping: with the 51st state talk at its loudest he says
plainly Canada will not be the 51st state, and that what he saw was no border and one currency, named
Amero, which he says he was told to write down over a year earlier. The April 2024 telling in this
archive supports that dating.
Back-dated by this batch: kim-jong-un-removed to 1 January 2025, beast-system-foundation to
18 December 2024, solomon-anointing-rebuild and megachurch-closures to 28 December 2024.
ukraine-files-burned arrived past due and was scored the same turn as evidence-a10:
EXPIRED_WITHOUT_MATCH on two rows. The USAID Inspector General's standing Ukraine oversight programme
records nothing of the kind for the window, and neither does Ukrainian reporting. Marked expired rather
than contradicted, because absence of reporting is weaker than a positive contradiction and he named no
ministry or building.

## batch c2o-40 (runs 895-897)
45 mentions from 30 May - 6 Jun 2025 (VVe9S5V9pXo, xRB5Htmm8wA, r-6QgcJFlPM, JY1ZzrgdX_A, eYlbwnkmyvg).
Seeded 5. Recorded a direct contradiction rather than folding it: on 3 Jun he says the Taiwan invasion
will not be prayed away and cannot be stopped, and on 6 Jun he says he was told he was missing it and
must pray it away and stop it. Both tellings sit on taiwan-two-day-fall with delta_type contradiction.
xRB5Htmm8wA@625 is the useful structural find: in the vision China attacked while a grey substance
covered the country from New Orleans to Canada, which gives the Taiwan claim a precondition that would
have to appear first. Six first_mention corrections in this batch as the queue reached the older tellings
(warsaw weapon, Fuji, Seattle wave, Hawaii volcano, ring-of-fire quakes, AI industrial revolution).
Tier 2 42.2%.

## Tier 2 batch w27 — 37 passages, 3 to 16 December 2024. Tier 2 now 2,496 of 5,824 (42.9%).
That closes everything before 1 January 2025. Zero duplicates.
Four new claims: silver-175-an-ounce, pelosi-schumer-removed, hostages-released,
america-weighed-and-found-lacking.
silver-175-an-ounce is seeded rather than folded into silver-75 on purpose. Two different figures for
the same asset from the same speaker is a contradiction, not a refinement, and the claim description
says so in both directions. The 8 December telling also gives a path he dates to 2014 or 2015: forty
an ounce, a crash back to twelve which he calls the time to buy, then a hundred and seventy five.
Silver went above forty in 2025 and did not crash to twelve. He also calls silver steady and low risk,
in a year when it was neither.
c8OVgrtlcaY@561 is the sharpest dating the plague claim has ever had and it is his own: the virus that
kills over 350 million is released in Europe first and Trump is president when it happens. That closes
20 January 2029. The mention carries the window, so plague-350m now has a real deadline attached.
YAacmBr8JyY@0 is worth reading twice. A 7.0 hits off Northern California, he says he had expected
Southern California, and then reads the northern location as what he was shown. Both halves are in the
mention text. The following passage recasts the same quake as a warning before the major one, which is
a frame that cannot fail.
H9i0NBnTWnk@2233 applies the 51st state idea to the United Kingdom, four weeks before he rules it out
for Canada on 1 January. Both are in the record on amero-north-american-currency.

## batch c2o-41 (runs 901-902)
45 mentions from 30 Apr - 30 May 2025 (eYlbwnkmyvg, 5ffLgM0vfT4, eEd1C8oRkiE, w00xXf4Lfg4, TrTCa5Fvb-M,
CqifdwkJFLY, aNxQMI-T7qQ). Seeded 7. CqifdwkJFLY@863 is worth flagging: he states he has already told
viewers who he believes the antichrist is and that the man will sign the temple agreement, which is the
strongest identification of a living person in the corpus and it is repeated rather than hedged. Three
more first_mention corrections as the queue reaches the spring tellings (AI industrial revolution to
21 May, putin-five-cards and kim-removed-sister to 3 May, both four months before the August versions I
had flagged). aNxQMI-T7qQ@402 on 30 Apr is the earliest and most specific venereal disease telling, and
it names Quebec rather than Canada generally. Tier 2 43.6%.

## Tier 2 batch w28 — 55 passages, 6 January to 24 February 2025. Tier 2 now 2,596 of 5,824 (44.6%).
Zero duplicates. Three new claims: asteroid-split-by-lasers, london-bridge-attack,
leviathan-out-of-the-gulf.
JKPqjW92sdc is another re-upload of the 6 February Iran material already read in batch w16, and the
mention rows say so rather than treating it as a second telling. One difference is worth keeping:
in this version he dates the shock and awe vision to eight years earlier, where the other telling says
four plus years.
_co9BHhQB5k@1117 is the qualifier that makes trump-tames-the-dragon unfalsifiable, in his own words:
the whip pops and stuns the animal for a second, but the animal is still an animal and still does what
it does. A Chinese retreat confirms the taming; a Chinese advance confirms the animal. Recorded as a
new_detail with that stated.
aEh2GC99MVI@1036 is a clean falsified political claim: a good government in Canada with the
conservatives getting the majority. The Liberals won a minority on 28 April. canada-election-april-2025
already carried evidence, so Job A stayed at zero.
_co9BHhQB5k@1261 back-dates land-for-third-temple-accord to February 2025, five months earlier than the
July telling, and it is sharper there: Gaza as the bargaining chip, Trump negotiating with the Mahdi,
and MBS named as the Antichrist which he flags as his own opinion rather than as the word.

## batch c2o-42 (runs 906-908)
45 mentions from 18-30 Apr 2025 (aNxQMI-T7qQ, MfFAnta4Vzk, uwQAB6rphJA, XkrRHjsi68k, tzSAVrfA5Z8,
1O_dIFD7yoA). Seeded 6. XkrRHjsi68k@2060 states the structural rule directly: intercessory prayer has
delayed the judgment but there comes a point when the prayers of the saints will not hold it back. Filed
on delay-but-not-stop, and it is the clearest statement of why no non-event can score against the
underlying claims. XkrRHjsi68k@2303 goes the other way and is genuinely scoreable: the plague will take
place during Trump's presidency, which can be settled in January 2029. Five picks in this batch are him
reading another man's dream aloud (a violinist's, on the angel over New York Harbour) and are recorded as
no_claim under the same rule as played clips, except the row where he interjects that his own vision
matched it. two first_mention corrections back to April tellings. Tier 2 45.7%.

## Tier 2 batch w29 — 18 passages, 26 December 2024 to February 2025. Tier 2 now 2,659 of 5,824 (45.7%).
That closes everything before 1 March 2025. Zero duplicates.
Three new claims kept: fertilizer-vans-trump-towers, soleimani-retaliation-thousand-men,
london-bridge-is-falling-down. A fourth, new-orleans-nashville-vegas-ranked, turned out to be the same
word as the existing three-city-attacks-ranked and was folded into it, which is the right way round:
the surviving id already carries the outcome, that the deadly attack came in the city he ranked lowest.
The New Orleans material is the most interesting thing in the batch and it cuts both ways.
o_HtP7CXqR4@167 names Bourbon Street and Islamic State before 1 January 2025, and the attack there was
claimed for Islamic State. Aguwfxoz4bc@53 and @100 say in the same breath that New Orleans was the
weaker impression, only one man, and that Nashville and Las Vegas carried the mass plans. One man is
what New Orleans got. Nashville and Las Vegas did not get the mass plans. Both halves are in the
mention rows so a reader can weigh the hit against the ranking that was wrong.
soleimani-retaliation-thousand-men is unusually checkable for this corpus: a named motive, a number,
and an arithmetic he states himself, a thousand men divided into ten groups of a hundred.

## Tier 2 batch w30 — 55 passages, March to April 2025. Tier 2 now 2,714 of 5,824 (46.6%). Zero duplicates.
Three new claims: injection-removes-free-will, fentanyl-and-organ-harvest-exposed,
war-on-two-fronts-then-three.
The Canada material in U91HRVT2aFs is the fullest single treatment of Canada in the corpus and it is
worth having in one place: a pyramid of darkness centred on Toronto in Ontario spreading like molasses,
Quebec less affected, Vancouver lit and fighting it and wanting to separate and align with America.
That gives bc-secession its first mention. In the same session he says plainly that he is not familiar
with Canadian politics or the voting system, which is filed on canada-election-april-2025 beside the
landslide and too-big-to-rig claims that did not come off.
Two structural things recorded rather than smoothed:
- qk7dhAYCkBs@2294 and @2324 attach a say yes condition to the greatest revival, which means absence
  is attributable to people refusing rather than to the word being wrong.
- _RZviFwBIlI@936 says what he has seen could run clear into the tribulation, which removes the
  deadline from everything he has seen. Filed on prayer-can-stop-it as a new_detail.
Huch7JopOaU@715 has him questioning his own reading of the four year window, which is the first time in
this archive he does that out loud.
selftest showed a transient orphan mid-batch, from the other reader's seed waiting on its load. It
cleared on the next run and everything passes.

## batch c2o-43 (runs 911-916)
45 mentions from 22 Mar - 18 Apr 2025 (1O_dIFD7yoA, L4ZWhGpfo7E, KWXipg48SMQ, qk7dhAYCkBs, U91HRVT2aFs,
GvCEdjOOuxU, YdurXtq8kSg, rPggL-xbrtg). Seeded 4. Two findings worth keeping:
U91HRVT2aFs@384 on 30 March is the earliest telling on file of both America and Israel striking Iran,
eleven and twelve weeks before they did, with no date attached. That row now holds first_mention on
called-saturday-strike-on-iran, and the 22 June row where he claims credit for calling Saturday is
superseded to new_detail. On the other side, YdurXtq8kSg@346 states his own working rule: do not quote
time frames, because it catches your hand in the door. That is the single line that explains why so few
claims in this corpus carry dates, and it is now on file.
L4ZWhGpfo7E@2487 is a second clean dated miss: eleven days before the Canadian election he prays for a
landslide the other way on the 28th, and the Liberals won a fourth term that day.
Also corrected the japan-earthquake-splits-land flag, which sat on a March 2025 row while a December
2024 row was assigned to the same claim.

THIRD WORKER COLLISION, and the reason for a new split. 45 of my review rows came back ambiguous again
because the other worker extracted the same 22 and 30 March passages. Keyed by mention_id as before.
Remaining tier 2 passages now stand at 3,110 and they sit almost entirely in 2026: 2025-03 has 36,
2025-07 has 83, and 2026-01 through 2026-08 hold 2,991. From batch 44 this worker clears the 2025
stragglers and then draws only from --since 2026-01-01 --until 2026-04-30, leaving 2026-05 onward to the
other worker. Tier 2 46.6%.

## Tier 2 batch w31 — 36 passages, March to May 2025. Tier 2 now 2,750 of 5,824 (47.2%).
That closes everything before 1 June 2025. Zero duplicates.
Four new claims: xrp-price-ladder, lend-to-nations, nordstream-reopened, no-more-war-for-america.
xrp-price-ladder is seeded separately from xrp-10000 rather than folded, for the same reason as the
silver pair: ten, twenty five, fifty and a hundred and fifty are not a refinement of ten thousand.
Both descriptions cross-reference the other.
no-more-war-for-america is the clearest example in the corpus of a claim built so it cannot lose. He
reports being told that the no more war declaration is about American involvement rather than about
whether wars happen. Wars continuing confirms it; America staying out confirms it. America struck Iran
in June 2025, which is in the falsify_miss.
nordstream-reopened is the opposite kind of claim and worth flagging for a future scorer: a named
pipeline, a specific action, no wriggle room.

## batch c2o-44 (runs 920-921)
45 mentions from 6-16 Jul 2025 (BW7DXgEMZHM, w3lzakaovU0, uOv6toXL4Uk, 0rk_kmVkVZs). Seeded 14. This
batch clears the 2025 stragglers. Two rows are the clearest examples in the corpus of meaning being
supplied after the event rather than before it: 0rk_kmVkVZs@817, where he asks what the Fourth of July
birthing meant, the day having passed, and is told it was the big beautiful bill, which had been signed
two days earlier; and 0rk_kmVkVZs@0, where he claims the Texas Hill Country flood of 4 July as fulfilment
of a warning six days earlier that named China rather than any American place or date. Also recorded the
30,000 North Koreans figure, which runs about double the reported deployment.

Note for the other worker: three claims are orphaned as of this run and all three are yours in flight,
and two of them duplicate claims I seeded minutes earlier in this batch. superhuman-ai-race duplicates
ai-race-to-first-superhuman, cern-copies-and-accident duplicates cern-copies-open-portals, and
woolly-mammoth-returns duplicates de-extinction-lab-animals, which predates us both. I am leaving them
for one cycle in case your reviews are about to land; if they are still orphaned at the end of my next
batch I will fold them with merge, which redirects your assignments rather than dropping them.
Tier 2 48.0%.

## Tier 2 batch w32 — 55 passages, July 2025. Tier 2 now 2,805 of 5,824 (48.2%).
45 of 55 came back duplicate: the other reader is in July 2025 now. Three of my five seeds were
duplicates of theirs and are folded, with their ids kept because they were first:
superhuman-ai-race into ai-race-to-first-superhuman, cern-copies-and-accident into
cern-copies-open-portals, woolly-mammoth-returns into de-extinction-lab-animals.
Two of mine survived because they read those passages differently: underground-arks and
russia-street-revival.

### Partition changed again
The remaining unread tier-2 material is almost all 2026: nothing before June 2025, 83 in July 2025 now
mostly read, and 2,984 from February 2026 onward. The other reader has cleared August 2025 through
January 2026 and is now back in July 2025, so their front is moving forward through the middle.
I am switching to the newest end and working backwards from August 2026. That is the furthest point
from their front and should stay clear for a long time. Anyone picking this up: use
`python prophecy.py pick --tier 2 --limit N` with no --until, which returns newest first.

## batch c2o-45 (runs 926-929)
46 mentions from 23-30 Apr 2026 (i6g1k3fCWLs, QLk3uWjK0jU, 7FG6qD91nZo, -2rEylREFj0, 9dkcd0-ilkM), the
first batch from the new 2026-01 to 2026-04 window. Seeded 13. Two rows are unusually stakeable:
israel-makes-the-mountain-glow says plainly that Israel and not America will hit the Iranian mountain,
which names which of two actors does it; and stimulus-2500-under-150k gives both an amount and an income
threshold. Three rows in this batch are him claiming fulfilment on the same day as the news:
the Iraqi Kurdish president as the Babylon word, the Toronto phone jammer case as the train device he
saw, and Perry Stone asking publicly for prayer. Each is recorded with the gap between what the earlier
word actually said and what is being claimed for it.
The three duplicate claims I flagged last batch were folded by the other worker into my ids before I got
to them, so no merge was needed. Tier 2 48.9%.

## Tier 2 batch w33 — 55 passages, 26 August 2026, the newest end. Tier 2 now 2,905 of 5,824 (49.9%).
Zero duplicates, so the newest-end partition is clean. Half the tier is read.
Nine new claims: acid-rain-red-cloud-europe, mercury-on-troubled-waters, black-sea-strait-closed,
albino-boa-new-york, europe-winter-fuel-crisis, oklahoma-schools-blessing,
france-voter-fraud-revolution, clean-energy-storage-boom, chip-factories-texas-oklahoma.
PhrYNHTuAww@3610 is a reversal worth marking. For two years the pattern has been to pray disasters off.
Here he stops and asks for it: shake the nations, shake the fault line, shake Malibu. Filed on
california-big-one as a new_detail, because it changes what a non-event would mean.
F-CNFR1LQQI@1922 is the sharpest personal-safety claim in the corpus: with a bounty reported on the
younger son, he says plainly it is not him they are after but Don Jr, and that the younger is a
distraction. Two named people, one ruled in and one ruled out.
Several claims in this batch are checkable in a way most of the corpus is not, and the mention rows
say so: the ballroom getting built after a Supreme Court ruling, chip factories in Texas and Oklahoma,
a Vance-led forfeiture of Chinese farmland, fifty percent tariffs on Canada.
Against that, three tellings take a news item as fulfilment of a looser word: the Cascadia hazard
study, the Colorado River allocation clip, and talk of a global depression. Talk of a depression is
not a depression, and the mention says so.

## batch c2o-46 (runs 932-936)
45 mentions from 22-23 Apr 2026 (9dkcd0-ilkM, 3nlrKph_elQ). Seeded 11. Tier 2 crossed half at 50.7%.
first-amendment-lost-not-second is the substantial one: a black widow cocooning the First Amendment
while a steel plate protects the Second, with the word that people will fight hardest for the Second
while giving up the First, and that the First matters more. The image holds across two consecutive
nights, which makes it one of the stable ones. speech-crackdown-midterms picked up a two year bound,
which makes it scoreable in April 2028.
Recorded a contradiction rather than smoothing it: the Empire State Building flag is Palestinian on
23 Apr and Iranian on 22 Apr, and both tellings sit on the same claim with delta_type contradiction.
Also folded two more cross-worker duplicates (merges-dupes-4.json): boats-dissolving-in-acid into
green-acid-economy and stimulus-2500-per-person into stimulus-2500-under-150k, keeping in each case the
id that carries the extra number.

## Tier 2 batch w34 — 55 passages, 21 to 26 August 2026. Tier 2 now 3,005 of 5,824 (51.6%).
Zero duplicates on the passages themselves, but the other reader is also seeding 2026 claims now, and
two of my four seeds were folded into theirs mid-batch: boats-dissolving-in-acid into
green-acid-economy, stimulus-2500-per-person into stimulus-2500-under-150k. Their ids were first and
theirs carries the income threshold, so I re-pointed my assignments to them rather than the reverse.
Surviving new claims: blonde-woman-leads-france, bitcoin-national-reserves.
Three claims in this batch are unusually hard, which is worth flagging for whoever scores them:
- 6XXc1-oeNWw@1043, an 8.2 earthquake at Rome and Venice. Italy has never recorded a magnitude 8.
- WCSr1gn7mlM@4980, Canada joining the United States financially with the financial borders down and
  the physical borders kept. He is precise about the distinction.
- -Z-oPJQyOeU@5687, the revival lasting two years to 2028, attributed to Hagin, with a real window.
6XXc1-oeNWw@1811 ties two of his own claims together: the crypto era is the golden age, and it will be
short lived. That links crypto-wave-ride-then-ends to golden-age-2027 in his own words.
6XXc1-oeNWw@2026 is him answering the contradiction charge on air. Asked how a booming economy squares
with everything getting worse, he says it lasts for a season. That answer is the thing worth keeping.
Two concessions: 6XXc1-oeNWw@1421 says plainly "if I'm off, I'm off", and @889 changes the country of
the mile long fuel queue from Russia to America while flagging it as a belief rather than a sighting.
WCSr1gn7mlM@2878 cites BlackRock approvingly as evidence of accumulation, which cuts against his own
standing blackrock-warning. Filed there with that noted.

## batch c2o-47 (runs 939-940)
45 mentions from 20-22 Apr 2026 (3nlrKph_elQ, yPdEFEDVsic, Zw7-D11KBIU). Seeded 13. Tier 2 52.4%.
Two rows are worth singling out because they cut against the usual pattern. yPdEFEDVsic@1594 is a rare
declining of a fulfilment: a 7.5 hits Japan and he says plainly it is not the one he was shown, because
his was inland and nearer 9.0. And Zw7-D11KBIU@1169, after a warning did not hold, states the argument
that makes any failure unfalsifiable in one line: what did we prevent that we didn't see. Both are now
on file next to the claims they bear on.
Also recorded: rome-8-2-splits-vatican, which puts a magnitude on a fault system that cannot produce it;
mount-fuji-explodes gained a casualty figure for the first time; and Reza is named directly as the man
to pray for in Iran, which is the most specific successor identification in the corpus.

## Tier 2 batch w35 — 55 passages, 19 to 26 August 2026. Tier 2 now 3,105 of 5,824 (53.3%). Zero duplicates.
Eight new claims: iraq-mirrors-saudi-arabia, fireballs-break-glass, megachurch-bought-by-mosque,
hong-kong-funnel-to-campaigns, denmark-molech-bull, civil-war-and-the-bikers,
european-blockchain-alliance, socialism-fifty-fifty-america.
Two of these are unusually checkable and are worth a scorer's attention:
hong-kong-funnel-to-campaigns names a state and a politician, and european-blockchain-alliance names
five countries. socialism-fifty-fifty-america puts a proportion on America.
QT_oRgu3nfA@1652 finally places an image he had been carrying unplaced: the bull, the pyramid eye and
the purple cloak are located in Denmark and named as Molech.
QT_oRgu3nfA@3484 is a rare thing in this corpus: he says he keeps seeing something about the Senate,
that he prays it is not true, and that he would rather be told he missed it. The content is withheld,
so nothing can be checked, and the mention says so.
Three tellings take a report as fulfilment of a looser word and the mention rows say so: the Turkish
fireball footage against glass-breaking booms, a Turkish statement of support for Syria against a
military intervention, and a 5.2 in Spain against a major shaking.

## batch c2o-48 (runs 943-944)
45 mentions from 17-20 Apr 2026 (Zw7-D11KBIU, Z4Dzphusf-U). Seeded 12. Tier 2 54.1%.
Two contradictions recorded rather than smoothed. Z4Dzphusf-U@1856: he says plainly that Cuba has no
rockets and no ability to strike America, which runs against his own Cuban retaliation material, and he
adds that if he is wrong he is wrong. And the Russian flower is blue berries at @6528 and lavender at
@7327 in the same session, with the peace meaning supplied only after the second identification.
castro-hidden-weapon-retaliation is the sharpest new claim: a weapon Fidel obtained in a Russian trade
and kept, used on a Cuban mountain in retaliation. Soviet warheads were withdrawn under verification in
1962, which is the record it runs against.
Also seeded banks-blocking-the-river, which names five institutions by name, and art-of-the-deal-nato,
which makes NATO itself the bargaining chip with Putin.

## Tier 2 batch w36 — 55 passages, 12 to 19 August 2026. Tier 2 now 3,205 of 5,824 (55.0%). Zero duplicates.
Six new claims: brazil-shaken, turkey-vampire-dracula-cape, banks-embarrassing-days,
sushiswap-bridges-asia, tv-announces-crash, oil-infrastructure-sabotage.
brazil-shaken is a hard one for him: Brazil is not in a high seismic zone, and he gives it flatly after
the Venezuelan and Colombian quakes. sushiswap-bridges-asia is unusually specific for this corpus, a
named protocol, though he says twice he does not know what he was looking at.
Two places where he narrows a claim rather than widening it, and both count in his favour as method:
0ptC-1kOXpQ@4053 rules out the current Japanese eruption because nobody died, and __45FoTY6rQ@4085 he
reaches for a Colombian coffee article, finds it is from 1999 and corrects himself on air.
Against that, four tellings take a weaker report as fulfilment and the mention rows say so: navigation
restrictions in the Turkish straits against a full closure, a routine North Korean missile test, an AI
virus paper that describes a benign result, and an almanac eclipse.
0ptC-1kOXpQ@8538 is the flattest contradiction in the batch: no great depression and no recession
declared, from the same man who has been calling a 1930s crash since 2023. Filed on
financial-storm-averted-prayer with that noted rather than reconciled.

## batch c2o-49 (runs 948-950)
45 mentions from 15-16 Apr 2026 (Xst5KJVjDeY, tMmRhBhwYSc). Seeded 13. Tier 2 55.8%. Selftest green.
cuba-falls-within-a-day is the sharpest timing claim found so far: the government falling inside twenty
four hours. Against it sits a plain internal tension, recorded as a contradiction rather than reconciled:
he says Cuba has no rockets and nothing like Iran, and in the same session that Fidel kept a Cold War
briefcase from Russia in a mountain bunker facing America. Both rows sit on
cold-war-briefcase-in-cuban-bunker.
Also recorded: nick-shirley-threatened, a direct and repeated warning that a named living private
individual will be killed, which is unusual enough to flag; nba-playoffs-boston-new-york, which named the
competition, the date and two cities and passed without incident; and a second change of a named person
on a fixed image, with the man licking the ground crossing to the White House now identified as Newsom
rather than the Black senator of the earlier telling.

## batch c2o-50 (runs 951-953)
45 mentions from 13-15 Apr 2026 (tMmRhBhwYSc, ZvDla0vHYoY, aYNy8bxXKrs). Seeded 8. Tier 2 56.6%.
aYNy8bxXKrs@888 and @928 are the largest fulfilment claim in the corpus: he says he gave in advance that
the president would go after Venezuela first and then Iran, would say drill baby drill, would take Iran
back to the stone age, and that the world would then come to buy American oil, and that it happened
exactly so. He invites viewers to check the videos, which is the right test and can be run against this
corpus directly. Recorded on called-saturday-strike-on-iran with the priority question stated.
Also recorded a contradiction inside one session: at ZvDla0vHYoY@5152 he declares the Save America Act
will be pushed through, and at @5566 that no Save America Act will save America and it would not matter.
Both sit on no-one-saves-america-but-me.

## Tier 2 batch w37 — 55 passages, 2 to 7 August 2026. Tier 2 now 3,350 of 5,824 (57.5%). Zero duplicates.
Seventeen new claims, the densest batch since w24. The one worth flagging is a flat self-contradiction
inside four days: on 2 August he declares Ebola will not take the whole of Africa and will not go into
Egypt or the Middle East, and on 5 August he recounts a vision of Ebola taking hold of the Middle East.
Filed as ebola-contained-not-egypt and ebola-into-middle-east, cross-referenced in both descriptions,
not merged. Same pattern with sharia-law-uptick-america: he has a standing claim that an uptick of
Sharia law is coming to America, and here declares there will be no Sharia law in America, Canada,
Australia or Europe. Logged as delta_type contradiction on the same claim, and the mention note records
that both branches are covered in advance, so neither outcome can falsify him.
Other new claims: emp-used-on-iran is the most checkable thing in the batch, a named weapon type plus a
debated ground invasion. newyork-tsunami-floods-inland, newyork-41st-floor-fire and
acorn-planted-at-ground-zero are three separate New York images in one sitting. face-scanning-required-
for-entry names Walmart and Target and extends to megachurches scanning congregations mid-worship,
which is distinct enough from screening-everywhere to stand alone.
Base rates recorded against four of them: crypto-tech-companies-merging describes the sector's default
direction, france-long-range-missiles-to-ukraine has been the public debate for two years,
shakings-mississippi-and-named-states includes Oklahoma where thousands of small quakes are recorded
annually, and kim-jong-un-role's bunker exit is already routine by 2026.
Five rows carry a null claim_id and delta_type no_claim: headline reactions to Russian strikes on Kyiv
where nothing was named in advance, a mosque protest clip played for laughs, and an uncovering
declaration with no plot, place or date in it.
Two entries in his favour on method: 38U8PhvIHog@1544 he corrects Europe to Middle East mid-sentence,
and byron-promoted-beyond-florida he hedges with maybe not this time, maybe next time, which is honest
but also removes any deadline. Recorded as such.
export_view.py run this batch (5,232 KB), catching up the every-tenth-batch rule from w25.

## batch c2o-51 (runs 956-958)
45 mentions from 9-13 Apr 2026 (aYNy8bxXKrs, 4EEOGvIPfFM, 4fTnqDOIePk). Seeded 6. Tier 2 58.3%. Green.
israel-acts-alone-on-iran-oil is the cleanest scoreable claim in this batch and he stakes it himself:
Israel will strike and blow up all of Iran's oil wells, acting alone, and he says plainly he never said
America would do it. Set against the fulfilment claims of the previous batch, where he takes credit for
the American action, the two are in direct tension and both are now on file.
draft-includes-women is the other one worth flagging: a draft in which women are conscripted, arriving
after America is struck on its own soil. No American draft since 1973 and women have never been
conscripted, so the claim has a clear failure condition and a stated order of events.

## batch c2o-52 (runs 960-962)
45 mentions from 7-9 Apr 2026 (4fTnqDOIePk, jonj7Nq5hG8, sNsgdTx5NPM, zaCMLnzdWHQ). Seeded 6.
Tier 2 60.0%.
tariffs-plan-a-war-plan-b is the substantive one: the tariffs as plan A to keep the economy from the
waterfall, and if they are struck down and the money has to be repaid, war on Iranian oil as plan B to
back the dollar, under a weapons of mass destruction umbrella which he identifies as a pretext himself.
Naming the motive as monetary rather than security is what makes it a claim rather than a description.
Also recorded the 24-versus-48-hour ambiguity in his Venezuela fulfilment claim: he says he called the
attack within a window on New Year's Eve and cannot remember on air which window he gave, which matters
for scoring it against the recording.

## Tier 2 batch w38 — 55 passages, 30 July to 2 August 2026. Tier 2 now 3,495 of 5,824 (60.0%). Zero duplicates.
Ten new claims. The batch is dominated by Poland: eight passages across two videos where he replays his
own earlier recording pointing at the map by Warsaw, then treats Polish air alert sirens and a breaking
report of Russian cruise missiles crossing Polish airspace as the thing arriving. The pre-commitment is
real and on tape, which is worth crediting. The strike he described, an unconventional weapon destroying
a fifty mile radius around Warsaw, has not happened, and the mention notes say so rather than letting an
airspace incursion stand in for it. oolVr6LLlDM@7827 gives the structure in his own words: there's some
things we cannot stop and there's some things we can. That sentence makes the Poland claim safe in both
directions and is now recorded on warsaw-ww3-trigger.
Three weak fulfilment claims held at restatement rather than scored up: an M1.8 solar flare against a
word about the sun causing great earthquakes, one church arson against a warning of church fires in
three regions where arson rates have been elevated since 2021, and a routine Poland to Ukraine meeting
read as escalation.
newsom-not-president and channel-doubles-to-1.2-million are the two cleanest new claims in the batch:
a named person and office with no conditions, and a number on a public subscriber counter.
iran-400-rocket-launchers-from-china is more interesting than most, because he takes a position against
the news in front of him: told Iran is about to receive 400 launchers from China through Pakistan, he
says he was told strongly China would not partake. That is falsifiable and he committed to it on air.
1I4ETKrehPc@266 turned out to be the earlier telling of newyork-tsunami-floods-inland, seeded in w37
off the 7 August video. Re-pointed the 7 August mention to restatement in the same batch.
Seven rows carry a null claim_id: casualty figures he did not call, a Lebanese official clip, scriptural
reflection, a statement of personal political position and a sign off.

## Tier 2 batch w39 — 55 passages, 26 to 30 July 2026. Tier 2 now 3,595 of 5,824 (61.7%). One duplicate, merged.
Ten new claims and one fold. turkey-dracula-blocks-black-sea was the other reader's version of my
turkey-vampire-dracula-cape; mine was created eighteen minutes earlier so it kept the id, but theirs
carried the 8 April 2026 tellings, which are now the first mentions. The description was rewritten to
carry the high collar and brooch detail from their reading.
The most interesting item in the batch is taEANymN-Fo@2636, seeded as itching-ear-good-days-warning:
he tells the audience to sift prophetic words and says those promising good days are coming in America
are giving an itching-ear word. He has given reprieve-window-2026, reprieve-four-years and
good-year-2024 himself. Cross-referenced in the claim description, not reconciled.
Two more places where he softens or hedges rather than doubling down, both recorded: VwWt7-MQ0HU@1933
he now asks the audience whether oil will ever reach $200 rather than asserting it, and @1893 he says
himself he is not sure the burning oil facility footage is recent. Both count in his favour on method.
Against that, four claimed fulfilments held at restatement with the base rate noted: a Russian petrol
queue for gas-lines-mile-long where the queue is not shown to be a mile and Russian fuel shortages were
already reported, Cuban darkness where Cuba has had repeated nationwide grid collapses since October
2024, Kim out of his basement where he has attended foreign summits since 2024, and a 7.1 in southern
Japan where Japan averages one or two magnitude 7 events a year. The Japan one has a real
pre-commitment twelve days out, but what he called on the 17th was water heating up, not a quake.
katrina-scale-disaster picked up its most checkable detail yet: this one will hit Mar-a-Lago.
DjQUqGl8Xwg@5957 turned out to be the earliest telling of newyork-41st-floor-fire, seeded in w37 off
the 7 August video, and it attaches the 41st floor to the president's towers rather than to a Central
Park view. Re-pointed the later mention to restatement in the same batch. That is the second time in
three batches the newest-end sweep has found the earlier telling of something seeded a week later.
Five orphaned claims at selftest, all seeded by the other worker at 20:30 and none of them mine.
Transient, same as w24, w30 and w34; left alone.

## batch c2o-53 (runs 967-971)
45 mentions from 6-7 Apr 2026 (zaCMLnzdWHQ, QsNuNKQL80E). Seeded 5. Tier 2 61.7%.
iraq-corruption-halved is the one with a number that can be checked: corruption in Iraq tamed back by
fifty per cent once Iran's hand is out of the cookie jar, against indices that have barely moved in
twenty years. The Cuba material is sharper than it looks too, because casinos on the ocean front would
require reversing a ban in place since 1959.
Repointed zaCMLnzdWHQ@7782 after the other worker folded turkey-dracula-blocks-black-sea into
turkey-vampire-dracula-cape mid-batch.

## batch c2o-54 (runs 972-974)
45 mentions from 1-6 Apr 2026 (QsNuNKQL80E, UMqHeHjGuMI, ABqn0lFIbqk, OVKr-hVqdI4). Seeded 7. Tier 2 63.4%.
Recorded the Taiwan contradiction rather than smoothing it: on 2 April he prays that Taiwan will remain
strong and China will not overthrow them, which sits directly against his own two-day fall word. Kept
side by side as same_event unsure with delta_type contradiction.
branson-theatre-1500-seats is unusual for this corpus because it is a claim about his own actions, a
theatre purchase in Branson with a fifteen hundred seat auditorium, so it can be checked directly.
The stone age fulfilment claim on 2 April is weak on priority: the phrase is a common English idiom
used about Iran by officials and commentators, so matching it proves little on its own.

## Tier 2 batch w40 — 55 passages, 19 to 26 July 2026. Tier 2 now 3,695 of 5,824 (63.4%). Zero duplicates.
Eleven new claims. The batch is unusually good for him on method and the notes say so in four places.
x9732-uLl6k@771 is the cleanest statement of it in the corpus: nobody is trying to be flaky, and if it
is not accurate he missed it. He then does not claim the 4.5 in Italy against his own 8.2 at Rome, and
says outright that 4.5 is small. At @849 he is shown major wildfires in France and says he did not see
that, only Colorado and Canada. At usjH1gnxOZw@628 he wonders whether the Mount of Olives even has
olives on it and says he has never been to Israel. At @468 he asks the audience what a kippah is called
and says he is ignorant rather than insulting.
Against that, three passages where the same instinct closes: x9732-uLl6k@8370 he offers that the Detroit
cells detail might be off, then says the Lord told him it is not off, which shuts the correction he had
just opened. usjH1gnxOZw@90 states the governing clause in his own words, that whatever he sees is
symbolic of something, which lets any image be reinterpreted after the outcome. usjH1gnxOZw@2932 makes
both press attention and press silence into confirmation.
The sharpest contradiction of the sweep so far: usjH1gnxOZw@6454 on 20 July he says plainly he does not
believe the Save America Act will pass, that only pillars of it will, and that he could be wrong. On
29 July at taEANymN-Fo@6945 he declares the act passed and it will pass. Both are now on record, the
first on save-america-act-support-structure and the second noted there too.
Three more first_mention re-points needed and applied. israel-new-david-warrior went back to 20 July
from 7 August, banks-embarrassing-days went back to 20 July from 12 August and that earliest telling
names Charles Schwab and a cyber breach rather than the Clarity Act table. The banks re-point needed
run 946 rather than 954, because t2review keys on the run that loaded the mention, not the latest.
The oldest-end drift is now systematic: every batch of the newest-first sweep has found the earlier
telling of something seeded a week or two later. Worth expecting rather than treating as an error.
sV1rn2FVee8@6056 resolved one of the other reader's orphaned seeds, another-bp-spill-in-the-gulf, and
links it to drone-swarm-cuba-to-miami since both are prayed in the same breath.

## batch c2o-55 (runs 978-979)
45 mentions from 30 Mar - 1 Apr 2026 (OVKr-hVqdI4, mdXXTm-aWEU, M5FxVJVwU2s). Seeded 5. Tier 2 64.2%.
The sharpest claim in the batch is the Iran one at M5FxVJVwU2s@767: the man he saw come on the scene
running Iran, behind a podium with microphones in front of him, a projectile from the side through his
throat, and he says he was told they would be successful. Method and setting are specific enough to
fail cleanly, though he adds a prayer that it be stopped.
Recorded a second contradiction on the persecution order. On 1 April England is next after Canada;
on 31 March he gives Canada first, then France, Germany, Italy and England last. Kept as
delta_type contradiction on persecution-spreads-england-then-europe.
Also worth flagging for the validation pass: on 30 March he claims the Canadian bills passing as a hit
while on 31 March and 2 April he declares they will not pass. Both are on file against the same claim.

## Tier 2 batch w41 — 55 passages, 16 to 19 July 2026. Tier 2 now 3,795 of 5,824 (65.2%). Zero duplicates.
Fifteen new claims, the largest seeding of the sweep. The 19 July video is dense: a Mother Mary vision
in New Orleans that produces louisiana-purchase-covenant-broken, and the passage worth flagging is
zp4ImjufUuU@8098 where he says outright he has no idea what any of it was and will do history lessons
that night. The 250 on the oak leaves, the Civil War monument and the five keys are all being researched
after the vision rather than known before it. That is the honest version of a pattern that usually shows
up as after-the-fact interpretation, and it is on record in his own words.
antichrist-at-the-deal-table is the other notable seed: he sees a figure doing the art of the deal over
Israel and the temple and says explicitly it is not Trump, which cuts against how a large part of his
audience reads that image. Recorded as a ruling out rather than a prediction.
One contradiction filed as such: bTI89Td5Xc4@2787 describes the snake heading to the White House as
having reptilian eyes and names Rubio, where the standing claim chameleon-not-reptilian is his own
correction of the audience rejecting exactly that reading. Both are on record, delta_type contradiction.
Two more first_mention re-points, both moving a claim back one day. green-cloak-arabic-over-europe and
israel-new-david-warrior now sit on 19 July rather than 20 July. That is five re-points in three batches;
the newest-first sweep systematically seeds a claim off a later telling and then finds the earlier one.
Four unfalsifiable structures recorded with the reason: the South Korean hedge of protection is
conditioned on repentance so neither outcome falsifies it; persecution-out-of-complacency is commanded
to stop and then explained as serving a purpose; financial-seed-kills-poverty puts any shortfall on the
giver; authority-over-the-weather-declared reads as answered on any timescale because weather changes.
Base rates noted on three: the ring of fire produces roughly fifteen magnitude 7 events a year, so a 7.4
in Mexico two hours after prayer is close to even odds over a fortnight; Turkey has backed the post-Assad
Syrian government since 2024, so turkey-syria-brotherhood-alliance is near the standing position; and he
has previously reported that nothing happened after an earlier watch Australia word.

## batch c2o-56 (runs 984-985)
45 mentions from 26-30 Mar 2026 (M5FxVJVwU2s, 1L7tKIvSMyY, e9umIfTFnMM). Seeded 6. Tier 2 65.9%.
Two more contradictions kept side by side rather than merged. On 26 March Taiwan falls within a three
day window; the two day bound is on file from the same corpus, so the numeric claim disagrees with
itself. On 27 March he prays that China will leave Taiwan alone and not take the chips, which is the
opposite of the word. Same pattern with the civil war: declared against on 30 March, described
elsewhere.
The Rome 8.2 is now the firmest number in the whole corpus: stated on 26, 27 and 2 April, an 8.2 close
to Rome. Italy has never recorded above about 7.4 and its faults cannot produce one, so it fails cleanly.
Recorded 1L7tKIvSMyY@2888 as a no_claim worth keeping: he says he gave a sugarcoated version and will
never give the great detail, which is the standing reason the sharpest material never reaches the record.

## Tier 2 batch w42 — 55 passages, 13 to 16 July 2026. Tier 2 now 3,895 of 5,824 (66.9%). Zero duplicates.
Eleven new claims, two videos, and the batch is heavily Iran and Cuba.
Two passages count clearly in his favour. LlRONx0fV0A@1666: told of a threat against the president's
life, he refuses to bank it, calls it a copycat and a false flag by a loser, and points back to the
specific attack he had described instead. Refusing an easy match is rarer here than claiming a loose
one. ruV85YYcW1o@2167: he narrows his own stone age claim to a majority of Iran rather than the whole
nation, and at @2214 states plainly that much corruption remains in Iraq while describing an Iraqi boom.
Both are downward qualifications and both are recorded.
Two that cut the other way, and the notes say so. @250 he claims Japanese crypto legislation as
fulfilment; Japan's reclassification under its financial instruments law had been publicly in progress
since early 2025. @1514 he offers something said on the 4th appearing on Fox nine days later as
prophetic accuracy, but never says what the item was, so the match cannot be checked from the passage.
ruV85YYcW1o@2362 is worth keeping: he and his co-host look up what kamikaze means during the broadcast,
after he has given it as the word he heard.
iraq-syria-pipeline-bypasses-hormuz is the batch's most checkable new claim, though it originates in a
report he is shown rather than a vision, and the Kirkuk to Baniyas line has been announced as reviving
several times since 2010 without being rebuilt. cuba-retaliation-against-america picked up a geographic
range this batch, Texas to Oklahoma to Missouri, which is roughly a thousand mile radius and far beyond
any current Cuban drone reach. Recorded on the mention.
Two more first_mention re-points, both to 13 July: iran-kamikaze-escalation and
arab-coalition-boots-on-ground-iran, seeded in w39 and w41 off later tellings. That makes seven
re-points in five batches. It is now a standing feature of the newest-first sweep, not an error.

## batch c2o-57 (runs 990-991)
45 mentions from 23-25 Mar 2026 (hH4qc5gpzRU, US8rZ7oprqo). Seeded 7. Tier 2 67.7%.
seven-vaporized-twenty-five-critical is the sharpest claim yet extracted from the refinery material:
sabotage at a white facility where seven people standing nearby are vaporised and twenty five more are
critical. Two days later he claims the Texas City refinery explosion as the hit, while saying he does
not know the cause and noting there were no deaths. Both are on file against the same claim.
japan-to-hormuz-leaves-taiwan-open is worth flagging for validation because it states a sequence:
Japanese warships go to the Gulf first, and China moves on Taiwan because the defenders have left.
That is checkable in a way the bare Taiwan claims are not.
Corrected two first_mention markers as the queue reached earlier tellings: the Boston Marathon prayer
moves to US8rZ7oprqo@4130 (23 March) and the six month window to US8rZ7oprqo@6948 (23 March).
Also recorded a numeric contradiction on the Iranian nuclear material: one bomb here against uranium
for eleven devices elsewhere.

## Tier 2 batch w43 — 55 passages, 10 to 13 July 2026. Tier 2 now 3,995 of 5,824 (68.6%). Zero duplicates.
Four new claims, and the batch is largely two long sittings covering the same ground twice.
4WhvlFBHVyM@8538 is word for word the 16 July passage already recorded, including the same self
correction from Saudi Arabia to Iraq. Filed as delta_type exact_repeat rather than a fresh word, and
three neighbouring passages in the same video are the same script.
The best single find is 4WhvlFBHVyM@9229. It is the earliest telling of iran-cuts-undersea-cables and
it carries a qualifier the later telling drops: Iran does not have the equipment to do it, it is a lot
of threat. The 16 July version keeps the threat and loses the limitation, which makes the later telling
stronger than the original. That direction of drift is worth watching for elsewhere.
trump-approval-25-percent is the batch's hardest call. Presidential approval has not gone below twenty
five per cent since Truman, so it is a genuinely difficult number rather than a safe one, and it is on
record with a stalemate presidency attached.
france-cathedrals-burn raises his own bar: not damaged like last time but completely destroyed, which
means a partial fire will not satisfy it. Against that, 0iOZJHUwyjQ@323 claims a single molotov attack
on one New York church as confirmation, in the same breath as saying they do not want to be flaky.
American church arson runs to dozens of incidents a year and the note says so.
4WhvlFBHVyM@6406 he names the failure mode himself: you can scattershot something and think you know.
Recorded on prophetic-accuracy-2025 because most of that video is exactly that.
riots-blamed-on-red-hats is structured so that rioting attributed to the right confirms it and rioting
attributed elsewhere does not disconfirm it. Recorded as such rather than scored.
Four duplicate first_mentions cleaned up this batch, including one against the other reader's row on
the same video a minute apart. Running total is eleven re-points across six batches.

## batch c2o-58 (runs 998-999)
45 mentions from 19-23 Mar 2026 (US8rZ7oprqo, Duk8c34FPC4, vsqXfAy4rxk). Seeded 4. Tier 2 69.4%.
Three more first_mention corrections as the queue reached earlier tellings: the seven vaporised and
twenty five critical moves to Duk8c34FPC4@175 (21 March), the New York fires to Duk8c34FPC4@8023
(21 March) and the Cuban witchcraft photograph to vsqXfAy4rxk@533 (19 March).
helium-shortage-stops-surgeries is a good one for the validation pass because the mechanism is real:
helium cools MRI magnets, so a supply shock is a genuine chain. What would have to be shown is elective
surgery stopping over anaesthetic supply, which he admits he cannot explain.
Recorded a straight contradiction on the reptilian material: seven lizard lineages with chameleon skin
here, against his own chameleon not reptilian framing elsewhere. Both kept.
Also recorded Duk8c34FPC4@2080 as a no_claim worth keeping: every time he sees something it means it
is getting closer. That rule means a word not landing is read as imminence rather than as a miss.

## Tier 2 batch w44 — 55 passages, 4 to 10 July 2026. Tier 2 now 4,095 of 5,824 (70.3%). Zero duplicates.
Five new claims across four videos, three of them from the 4 July anniversary broadcast.
Mq0qQJkoWcg@4865 resolves an open question from w41. The 250 he saw on the oak leaves in the 19 July
New Orleans vision was in front of him two weeks earlier: this is the 4 July 2026 broadcast, the
nation's 250th anniversary, and he prays over it by name. Recorded on the review so the connection is
not lost. Seeded as america-250th-humbling-second-wind.
Two hard numbers this batch, both worth crediting as difficult rather than safe.
weather-control-lost-150mph-winds puts straight line winds above 150 mph; the strongest recorded derecho
winds are around 140, so it exceeds the observed maximum. trump-approval-25-percent from w43 is the
same kind of call. Against those, V3w8-580i2s@5656 sets a deliberately low bar and says so: a 4.5 on
the Mississippi that will not be a great one, given as a warning. Magnitude 4 events occur there every
year or two. He states the limitation himself, which is the honest version.
V3w8-580i2s@811 is the clearest timing disclaimer in the corpus: he says he often has no clue about
timing and that this is why the prophetic is hard for him. Filed on prophetic-accuracy-2025.
0iOZJHUwyjQ@1281 describes the Warsaw weapon as vaporising everything while leaving houses and cars
standing. That is the popular description of a neutron bomb, a known weapon class, not one never seen
before. Recorded on the mention.
One structural contradiction kept separate: V3w8-580i2s@3490 has Turkey forming a bloc with Syria,
Jordan and Egypt against Iran, while elsewhere in the same fortnight Iran is trying to get Turkey and
Syria to help it. Both on record, not merged.
Note for whoever picks this up: first_mention is not a global invariant in this database. About 170
live claims carry more than one, and the other reader does not use the field as earliest-telling at all
(cuba-economy-flourishes-like-a-state has April 2026 rows marked new_detail that predate both
first_mentions). I keep my own rows consistent and re-point when the sweep finds an earlier telling of
something I seeded, but I am not rewriting their adjudications to a convention they do not share.

## batch c2o-59 (runs 1006-1008)
45 mentions from 18-19 Mar 2026 (vsqXfAy4rxk, TC0SV11Jv8M). Seeded 5, folded 1. Tier 2 71.1%.
Folded young-man-in-a-hoodie-in-danger into nick-shirley-threatened. Same person: on 18 March he names
the young man who wears hoodies as the investigator exposing California corruption, and on 21 March he
gives the hoodie warning without the name. Read side by side before folding (merges-dupes-5.json).
seaworld-and-ford-come-to-cuba is the most checkable claim in the batch, because both halves need the
embargo lifted and named American corporations to enter: a marine park with killer whales and blue
roller coasters, and Ford signs selling trucks and SUVs. The cigar shipments to America are the same
kind of test, since that import has been barred since 1962.
Two numbers moved in his own retelling and both are on file: the Cuba quake he offers as confirmation
is 5.5 on 18 March and 5.8 on 19 March, and the Cuba liberation window is a day here, days elsewhere
and up to a year at TC0SV11Jv8M@2206.
Third contradiction on Taiwan in three weeks: he prays a hedge that China will not invade, against his
own word that it falls.

## Tier 2 batch w45 — 55 passages, 1 to 4 July 2026. Tier 2 now 4,195 of 5,824 (72.0%). Zero duplicates.
Eight new claims. The flattest is mossad-takes-out-netanyahu: a named agency, a named person, no
condition and no hedge, given at CoXY2EJ5oDA@2624 with the aside that it is a hard thing to say. He does
not soften it afterwards. That is the most falsifiable single item recorded in several batches.
Two places where he refuses an easy upgrade. CoXY2EJ5oDA@3460 his audience offers him the ark of the
covenant and he declines it, saying he only saw tablets and a budded rod. jlQZ9XjWWus@7389 he says
outright that he does not know what the baseball stadiums mean. Both recorded.
Against that, jlQZ9XjWWus@2004 claims a 5.4 offshore Oregon as landing where he said it would; the
Blanco fracture zone there produces magnitude 5 events several times a year. In the very next passage he
raises the same claim to bigger than an 8.0 with a major eruption, which is a far harder call than the
one he just banked. Both on the same claim, both noted.
Four structures recorded as covering both outcomes rather than scored: the covering over Taiwan means a
Chinese failure and a Chinese non-attempt both confirm it; the boat-turning-slowly claim explains any
absence of results as the turn taking time; canada-revival-out-of-persecution makes persecution the
proof and its absence no disproof; and hidden-cells-america now states in advance that there will be no
internet chatter, so a lack of warning signs is confirmation.
sooners-asia-first-on-crypto is drifting. The original word named Japan and South Korea. This batch
claims Taiwan twice as the Sooners moving first. Logged as location_update with the drift noted rather
than treated as the call landing.
fox-looking-at-america moved back to 1 July, twelve days earlier than where w42 seeded it, and in the
earliest telling the fox is already tied to the Bay of Pigs and New Orleans together.

## batch c2o-60 (runs 1012-1013)
45 mentions from 14-18 Mar 2026 (TC0SV11Jv8M, 8RydcMuYFcI, 6wtLDJxg4sw). Seeded 7. Tier 2 72.8%.
Ran the tenth-batch export: prophecy-db.html, 5922 KB.
Two claims here are worth putting near the front of any validation pass.
lose-the-senate-keep-the-house: he states plainly that they will lose the Senate and keep the House at
the 2026 midterms and that winning the Senate would take a miracle. Two outcomes, one fixed date, no
prayer escape clause attached. It is the cleanest political claim in the corpus.
seventy-five-percent-came-to-pass: he scores his own word about the strait, gas prices, worldwide
antisemitism and Jews returning to Israel at about seventy five per cent fulfilled. One of the few
places he puts a number on his own accuracy, so it can be checked against the recordings directly.
Priority note recorded at 6wtLDJxg4sw@46: the Chinese gas queues he shows on 14 March are in the news
eleven days before he gives the gas lines like the 1970s word on 25 March.
Three more first_mention corrections: the Hawaiian man to TC0SV11Jv8M@7964, the Cuban resorts and cars
to 8RydcMuYFcI@402, and the witchcraft covering lifted off Cuba to 8RydcMuYFcI@7104.

## Tier 2 batch w46 — 55 passages, 25 to 29 June and 1 July 2026. Tier 2 now 4,337 of 5,824 (74.5%).
Eight new claims seeded, one folded back out. Job A re-opened with two past-due claims and was closed
in the same batch with four evidence rows in evidence-a11.json.
Job A, trump-in-turkey-danger: EXPIRED_WITHOUT_MATCH. He called the president exposed on Turkish ground
and asked for a hedge of protection, given against footage of a mass funeral where Trump was attacked in
effigy. The visit went ahead 7 to 8 July 2026 for the Ankara NATO summit and was the opposite of hostile:
Erdogan met him at the airport, they walked arm in arm, Turkey named an airport building after him and
Trump promised to lift the S-400 sanctions. Noted in the rationale that the sanctions promise cuts the
other way on ungodly-alliance-turkey-syria, where an agreement on Turkish soil is exactly what he warned
about. The two claims are kept separate rather than merged.
Job A, stay-home-until-after-july-4: EXPIRED_WITHOUT_MATCH. The 250th on the National Mall was delayed
by a thunderstorm and resumed; police reported four arrests, two of them for refusing to leave the
Jefferson Memorial during the evacuation. The nearest real event is genuine and worth recording: on
16 June 2026 the FBI disrupted a plot to fly explosive drones over the UFC Freedom 250 event at the
White House and shoot into the fleeing crowd, five arrested and eight eventually indicted. It cannot be
scored as fulfilment because it was disrupted nine days before this word was given. It also cuts against
hidden-cells-america, which specifies foreign infiltrators, an act of war rather than terrorism and no
internet chatter: the men charged were Americans who organised on a public TikTok group before moving to
Signal, and the chatter is how they were found. Deliberately not entered as evidence on that claim,
because a single disrupted plot does not settle a standing claim and any evidence row would remove it
from the past-due sweep permanently.
ebola-reaches-france was seeded and then folded straight back out. France reporting a first Ebola case
is a headline he reads out, not a claim he makes, and the rules say a clip he plays is not his claim.
Recorded in the fold note rather than left as a bad claim.
Two more where he holds himself to the evidence: i9gn298oFBM@1500 he asks whether a quake was near San
Francisco, is told it was further north, and accepts the correction rather than claiming it; and
Nbb5gUwTSE0@2568 he says outright that the Oakland to Denver device has not been seen and he keeps
praying over it. Against that, i9gn298oFBM@1418 he checks whether a 6.9 in Japan was in California, and
FHxJpX0PLPI@8931 he asks whether Greenland and the Philippines have temples rather than knowing.

## batch c2o-61 (runs 1019-1021)
45 mentions from 13-14 Mar 2026 (6wtLDJxg4sw, Mzw5rRiDwA0, ji5iFzKemg4). Seeded 4. Tier 2 74.5%.
Selftest all checks pass, no orphans.
Recorded a clean self-contradiction four days apart on the Iran ground war: on 13 March "it will not be
a ground invasion, they will not have to", on 17 March "it will take a ground troop invasion" with two
British special operations soldiers. Kept as delta_type contradiction on two-british-special-ops-on-the-ground,
with first_mention moved back to Mzw5rRiDwA0@4704 where Great Britain first appears.
Brownsville, Texas is now attached to seven-vaporized-twenty-five-critical, which gives that claim a
place as well as a casualty count. It is the most falsifiable thing in the refinery material.
Priority notes worth carrying into validation: on 14 March he calls the Chinese petrol queues a
fulfilment while conceding they fall short of the mile he saw, and on 13 March he treats an FBI drone
warning as the fulfilment of the stadium drones. A warning is not an attack.

## Tier 2 batch w47 — 55 passages, 22 to 25 June 2026. Tier 2 now 4,437 of 5,824 (76.2%). Zero duplicates.
Six new claims. export_view.py run this batch (5,998 KB), catching up the every-tenth rule from w37.
i9gn298oFBM@3595 is the earliest telling of trump-approval-25-percent and it is better than the version
w43 seeded off: he gives the current figure of thirty one himself, so the gap he is calling is explicit.
That makes it one of the few numeric claims in the corpus with a stated baseline.
i9gn298oFBM@6077 is a real narrowing. Asked in effect why the Venezuela revival keeps not arriving, he
answers we are on the heels of it rather than restating it open ended. Logged as delta_type timing_update
rather than restatement, because tightening a claim is a different act from repeating it.
Two claims in this batch cut against known facts and the notes say so. 7ufmrBqNg-o@1359 has Turkey
closing the Black Sea to aid Russia; Turkey has closed the strait to warships of both belligerents since
2022 under Montreux, which is the opposite alignment. ig_1Spghkgg@2278 claims antisemitism reaching an
all time high in New York as newly arriving; recorded incidents were already at documented record levels
before the word was given.
four-fires-started-california went from four to seven this batch. Logged as severity_update on the same
claim rather than as a new one, so the drift is visible on the claim rather than hidden across two.
cuba-evidence-being-removed is the batch's most self-sealing seed: if nothing is ever found in Cuba, the
claim says it was removed in time. Recorded with that noted.
Two more first_mention re-points, to 25 June and 23 June. Running total fifteen across nine batches.
Eight orphaned claims at selftest, all the other reader's seeds from 21:19 and none of mine. Transient.

## batch c2o-62 (runs 1023-1027)
45 mentions from 9-13 Mar 2026 (Mzw5rRiDwA0, ji5iFzKemg4, gLE4m-wraw8, lKC1io90BMo). Seeded 8.
Tier 2 76.2%. Selftest all checks pass.
Three of the new seeds are unusually scoreable and should go near the front of any validation pass.
no-major-hurricanes-this-year and twin-tornadoes-over-omaha both run against published records for the
2026 seasons, and the tornado pair is internally inconsistent: he sees two twin tornadoes over Omaha
and in the same prayer declares the season a dud.
water-based-weapon-stronger-than-nuclear is the largest technical claim in the corpus: an American
weapon stronger than nuclear, water-based, a splitting of water, held back so China cannot touch it and
about to be released. Nothing of the kind could be deployed quietly.
Recorded a numeric contradiction on petrol: ten dollars a gallon here, eight elsewhere.
Also worth noting for the record: at gLE4m-wraw8@1526 he places over a hundred men in each of five
named cities waiting on a phone call. That is a headcount that could not stay hidden, which makes it
one of the cleaner failure conditions in the sleeper cell material.

## batch c2o-63 (runs 1029-1030)
45 mentions from 8-9 Mar 2026 (lKC1io90BMo, U2zTp6gX81I, EPIsbBYnCw0). Seeded 5. Tier 2 77.9%.
Two more first_mention corrections as the queue reached earlier tellings: the 1970s gas wars image
moves to U2zTp6gX81I@645 (8 March), seventeen days before the version he calls fulfilled, and the
human shields claim to U2zTp6gX81I@1308 (8 March).
The most useful thing recorded this batch is his own standard, at U2zTp6gX81I@972: they do not pray
the news, and if you are praying the news you are already behind, because the Lord shows them what is
coming well in advance. That is the test he sets himself, and much of each broadcast is spent reading
the day's news back as confirmation. Kept as a no_claim so the validation pass can use it.
hiroshima-type-weapon-under-cuba is the sharpest new seed: an underground facility in Cuba holding a
weapon he compares to Hiroshima. A device of that kind could not be found quietly.

## Tier 2 batch w48 — 55 passages, 17 to 22 June 2026. Tier 2 now 4,537 of 5,824 (77.9%). Zero duplicates.
Seven new claims. Two passages in this batch are the most important of the sweep so far.
Ucfm1SaO_NM@4904, seeded as the-14th-protected-23-in-custody: on 19 June he gives thanks that nothing
happened on the fourteenth and that all twenty three planners are in custody. The public record has the
FBI disrupting a plot against the UFC Freedom 250 event at the White House on 15 and 16 June, five men
arrested and eight eventually indicted, with an encrypted network of at least twenty three participants
being traced. His twenty three matches the reported network size rather than the number in custody, and
the event was the 15th, not the 14th. That is close enough to be worth flagging and loose enough not to
score. Deliberately not entered as evidence, because the pre-commitment has to be established first, and
the only pre-commitment on offer is HhKfSxKL67I@185 from 17 June, which is after the event. Both mentions
carry that note so a later reader can settle it against the actual recording dates.
7ufmrBqNg-o@2603 is the rarest kind of passage here: he states outright that he could miss it because he
is human, on the Taiwan timing. He also pushes the fall into the tribulation on a ten year window, which
puts it beyond any near term check. Both halves recorded.
taiwan-held-back-by-prayer is the batch's cleanest both-ways structure and the note says so: a Chinese
non-move confirms the holding back and a Chinese move confirms that they had plans.
Ucfm1SaO_NM@1944 finally gives the fox an interpretation. In w42 and w45 he says twice that he does not
know what it means; here, four days earlier in the corpus than the w42 telling, the fox is the one
smuggling evidence out of Cuba. Recorded on both claims so the sequence is visible.
Two self-corrections recorded rather than smoothed: @9805 the pool springs from Taiwan and he corrects to
South Korea, and @2722 the Africa word has to be prompted by his co-host.
Two more first_mention re-points, both back to 19 June. Running total seventeen across ten batches.

## batch c2o-64 (runs 1034-1036)
45 mentions from 7-8 Mar 2026 (U2zTp6gX81I, EPIsbBYnCw0, bHVnPIa0Cn4, Tw9xqU-vn2k). Seeded 6.
Tier 2 79.6%.
The 7 and 8 March sessions contain the clearest example in the corpus of a word and its own denial in
one broadcast. On 8 March he describes a chemical weapon that melts skin being prepared against Israel,
then within the same session prays that not one missile will touch Israel and that the weapon will
implode in their own base and nothing they are planning will come to pass. Both are recorded, the
second as delta_type contradiction on telaviv-chemical-attack and horde-of-missiles-under-the-ground.
red-and-white-blanket-over-taiwan is a fulfilment claim worth checking properly: he saw a red and white
blanket over Taiwan on 7 March and on 8 March read that Chinese air activity had fallen to no fighters
in a week, calling it the power of prayer. Incursion counts have swung week to week for years.
Three more first_mention corrections: the weapon under Cuba to Tw9xqU-vn2k@1053, the telephone network
to Tw9xqU-vn2k@2111, and the Taiwan blanket to Tw9xqU-vn2k@4422.

## Tier 2 batch w49 — 55 passages, 15 to 17 June 2026. Tier 2 now 4,637 of 5,824 (79.6%). Zero duplicates.
Five new claims, three first_mention re-points, and Job A opened and closed again in the same batch.
Job A, trump-three-days-in-france, scored across two rows in evidence-a12.json. The itinerary half is
exactly right, three days Monday to Wednesday with a dinner with Macron, but he says in the passage that
he is hearing the announcement from the news for the first time, so it is a report and the schedule was
already public. Marked PARTIAL_MATCH for that half. The half that was actually his, the reaction of oh
no and the prayer for divine delays against the trip, is EXPIRED_WITHOUT_MATCH: the 52nd G7 ran 15 to
17 June at Evian-les-Bains, the Versailles dinner happened, Trump did not leave early and there were
none of the public spats of previous years. Two rows rather than one because the two halves score
differently and merging them would hide that.
This batch has the two strongest hedges in the whole sweep, both unprompted. HhKfSxKL67I@1147: he says
he would love to be wrong about the war he believes he was shown. yCJFoRGfrEc@458: now, can I miss it?
Yes. Recorded on lavender-peace-over-russia and israel-acts-alone-on-iran-oil.
successful-attempt-on-his-life is the severest single seed of the sweep: an attempt that will succeed,
with the church held responsible for whether it does. He does not name the man in the passage. The
conditional structure means a non-event is credited to intercession and an event is credited to the word.
Three claimed fulfilments held at restatement with the base rate on the record: a 6.4 in China as the
temples being shaken down with no temple damage cited, Israeli statements of sovereign action which are
routine and predate the word, and a Russian official calling Germany Nazi, a comparison Russian officials
have used throughout the war. q-M7KOvMzS4@1058 treats a reported intrusion into a California water
system as the treatment shutdown he had described; the reported incident is an intrusion.
q-M7KOvMzS4@736 he says Greece, corrects to Turkey and explains that Greece was in his mind. Recorded.

## batch c2o-65 (runs 1041-1042)
45 mentions from 4-7 Mar 2026 (Tw9xqU-vn2k, Cys6GFXLPNs, 6YMi3ZJxq8M). Seeded 3. Tier 2 80.4%.
Three more first_mention corrections: the banded cigars and the Ford trucks both move to
Tw9xqU-vn2k (7 March), and the material moved deeper underground to 6YMi3ZJxq8M@322 (4 March).
Two notes for the validation pass. At 6YMi3ZJxq8M@447 he says plainly that Macron is not acting like a
tyrant now, only like someone who wants to be involved, which is the most candid concession in the
Macron material and should be read alongside every telling of that claim. And at Cys6GFXLPNs@856 the
North Korea word comes with its own escape built in: you will not see a lot of this in the news, you
will see signs of it in the spirit realm.
pakistan-joins-iran-against-america is the cleanest new seed. Pakistani troops deployed to Iran would
be unmistakable, and what he offers as the confirmation is a diplomat's condolence message.

## Tier 2 batch w50 — 55 passages, 10 to 15 June 2026. Tier 2 now 4,737 of 5,824 (81.3%). One duplicate, merged.
Nine new claims, three re-points, one fold, and the most substantive scoring of the whole sweep.
KvS6uzzLK6c@4436, 10 June 2026, turns out to be the real pre-commitment behind the fourteenth. He says he
was told again to pray for the 14th, four days before the date, where the w48 material only asserted the
pre-commitment after the fact. Re-pointed so first_mention sits on the 10 June telling.
That made the-14th-protected-23-in-custody scoreable, and it is scored in evidence-a14.json across two
rows because the two halves score differently. PARTIAL_MATCH on the date: UFC Freedom 250 was held on
the White House South Lawn on 14 June, the president's eightieth birthday, and a plot aimed at it was
disrupted. The FBI director says the bureau became aware of the threat on 10 June, the same day as his
word. Held at partial and not stronger for three stated reasons: he names only a date and no event,
place, method or threat; the 14th was already the most conspicuous date on the American calendar that
month and had been previewed in the press on the 12th; and what he asks prayer for is unspecified, so any
outcome that day would have been claimable. CONTRADICTED on the number: he says all 23 are in custody.
Twenty three is a real reported figure but it is the network size investigators identified, not the
number detained. Five were in custody, eight eventually indicted, and he says it on the 19th after the
reporting was public.
Two more claims scored off the same event. drone-attacks-holiday-crowds PARTIAL_MATCH: explosive drones
over a crowd at a public event to force an evacuation is a close method match, but the claim placed it in
Europe, it was disrupted rather than carried out, and DHS had publicly flagged drone risk in advance.
hidden-cells-america PARTIAL_MATCH: on the claim as originally worded this is a match, and it fails on
the specifics he added later, that the actors would be foreign and that there would be no internet
chatter. The men charged are Americans who organised on a public TikTok group before moving to Signal,
and a warning from one suspect's mother helped foil it. The chatter is how they were found.
Job A also took israel-acts-alone-on-iran-oil, which went past due on the twenty four hour window he gave
on 11 June. EXPIRED_WITHOUT_MATCH on that window, and CONTRADICTED on the core: the record of the 2026
campaign has the United States striking Iran directly, where the whole point of his claim was that it
would not be America doing it. The rationale notes that the wider windows out to June 2027 stay open.
Note on method: entering evidence permanently removes a claim from the past-due sweep, so I only score
claims that are genuinely settled rather than every claim an event touches. That trade-off is deliberate.
One contradiction filed rather than reconciled: 7CtKI-6263c@1991 he says oil will drop back to where it
was once the conflict ends, against his own standing oil-200-barrel claim.

## batch c2o-66 (runs 1050-1053)
45 mentions from 1-4 Mar 2026 (6YMi3ZJxq8M, fjuTrDgdUgA, 5u6wPxLzE9E). Seeded 7, one folded by the
other worker mid-batch. Tier 2 82.1%. Selftest all checks pass, no orphans.
Promoted his own standard to a claim: dont-pray-the-news-were-ahead, first stated at 5u6wPxLzE9E@163
on 1 March. They do not pray the news, and anyone praying the news is already behind, because the Lord
shows them weeks in advance. The 8 March restatement was repointed onto it from no_claim, so the
validation pass now has a single claim to score the whole corpus against.
fjuTrDgdUgA@1448 is the other thing worth carrying forward: he distinguishes a window from a door. Iran
and North Korea get a window that is small and does not last, Cuba and Mexico get a door and a whole
lifestyle change forever. That distinction is the closest he comes to telling a scorer which claims
should be expected to expire and which should not.
mass-attack-at-the-hawaii-mall is placed precisely enough to fail cleanly: three men, a named mall by
the statue with the lei and the surfboard, a van as the weapon.

## Tier 2 batch w51 — 55 passages, 8 to 10 June 2026. Tier 2 now 4,882 of 5,824 (83.8%). Zero duplicates.
Six new claims, one re-point. Three items worth carrying forward.
wLI8D3SDe3E@526 seeded florida-quake-felt-to-alaska, and the note records why it is weaker than it
sounds: the Alaska reading is a seismograph trace, not felt shaking. Distant instruments record every
large earthquake. He treats the chart reaching Alaska as the event reaching Alaska.
a4uOSv4NVrE@3002 identifies a turtle in glasses from an earlier vision as Germany. The identification is
made now, not when the vision was given. That is the pattern across all his animal symbols and is worth
tracking as a class: the fox got its meaning in w48 after two tellings of not knowing, the cobra and the
chameleon were reassigned, and here the turtle acquires a country.
wLI8D3SDe3E@1057 is a revision on the record: he says he would not have thought the great betrayal was
with the president, having previously given it as America turning its back on Israel. Recorded as
new_detail with the revision named rather than smoothed into the claim.
Two places where the authorities are ahead of the claim rather than behind it, and the notes say so:
wLI8D3SDe3E@1665 plays an official describing counter drone measures at all seventy eight World Cup
matches, which he then prays over as though the risk were newly identified; and a4uOSv4NVrE@2705 he asks
whether an 8.6 in the Philippines is it rather than asserting it, which is the right form.
Base rates on the record for three claimed clusters: a 5.2 in Greece is routine and Greece records
several a year; around fifty volcanoes are erupting worldwide at any time; and the four banks named in
black-on-the-financial-buildings-mime are the same four named across several separate bank claims here,
which weakens naming them as a distinguishing detail.
colombia-arena-meetings-invitation is the batch's most checkable seed: a named condition, an election
outcome, and an arranged event that either happens or does not.

## batch c2o-67 (runs 1055-1058)
45 mentions from 28 Feb - 1 Mar 2026 (5u6wPxLzE9E, LjVQoqPssYQ, 1Bd3ILxtC40). Seeded 6.
Tier 2 83.8%. Selftest all checks pass.
1Bd3ILxtC40@240 is the most useful thing in the batch for the validation pass, because it is the
concession against his own standard: he says he thought the retaliation would happen within twenty
four hours because the pulse was so strong, and then says a pulse that feels immediate can be days or
weeks away. Recorded against dont-pray-the-news-were-ahead.
Recorded two more of the declare-then-deny pairs. At 5u6wPxLzE9E@5278 he says the weapon will never
come out of the ground, minutes after describing it being moved into position on rail cars. At
LjVQoqPssYQ@2459 the allies loudly refuse over Taiwan, against his own telling that they were only
fussy about it and did not resist.
Corrected the Cuban stronghold first_mention back to 1Bd3ILxtC40@2999 (28 February).
carrier-groups-named-abraham-lincoln-and-bush is worth flagging: he names two American carriers as the
ones that would attack Iran, which can be checked against deployment records.

## Tier 2 batch w52 — 55 passages, 3 to 8 June 2026. Tier 2 now 4,982 of 5,824 (85.5%). Zero duplicates.
Eight new claims and five first_mention re-points, the most in one batch so far. The sweep is now deep
enough into the corpus that most of what it finds is the earliest telling of something already seeded:
france-cathedrals-burn moved back a month, malibu-earthquake and fig-tree-ripe-ezekiel-at-the-door six
and four weeks, uk-riots-spread-from-france and revival-corrupted-by-money-laundering five and
seventeen days.
Three self-corrections recorded rather than smoothed. Tme-Su9LtHo@1060 he says the event he saw on fire
was not the Olympics as he had read it, and adds that adding to what you see is bad. gklesf_Fdg8@372 he
says outright that he does not know how far Hollywood is from Malibu while giving both as sites of the
same word. Tme-Su9LtHo@1469 he assumed Iran was out of materiel, is shown a drone strike on Kuwait and
says he was wrong.
gklesf_Fdg8@162 is a rare downward revision: the Californian shaking is explicitly not the devastating
earthquake he saw at the false temples. Logged as severity_update because it moves the claim in the
harder to score direction, which is worth distinguishing from the usual drift upward.
Two withheld passages in the same batch, gklesf_Fdg8@1662 and EIT61ZA5ExU@1153, where he begins on a
depopulation claim and on Cuba and stops because he is told he has said enough. Neither can be checked.
Two claims taken wholly from headlines rather than from a word, and both notes say so:
screwworm-in-south-texas, where the parasite had been moving north through Central America for two years
and a Texas detection was anticipated by the agriculture department, and
las-vegas-quake-juan-de-fuca-line, where the moving line of activity framing is from the post he reads
rather than from him.

## batch c2o-68 (runs 1062-1069)
45 mentions from 24-28 Feb 2026 (LjVQoqPssYQ, 1Bd3ILxtC40, Ywv1xy-ko9U, V5WgYqWpBgk, Ux9iGMe2HSo).
Seeded 6. Tier 2 85.5%. Selftest all checks pass.
The find of this batch is forty-million-ransom-from-the-elites at Ux9iGMe2HSo@1106 and @1202, which is
the clearest admitted miss anywhere in the corpus. He asks straight out whether the word was spot on,
answers no, says the man mentioned nothing about the forty million and that as of right now that word
is not all right. He then leaves it open for a later fulfilment, which is the pattern worth noting.
blonde-girl-held-hostage-found is the other one to put near the front of a validation pass. A young
woman drugged out of a bar and held by the cartel, whom he says will be seen in the news, set free and
sent home. That is a clean, near-term, checkable claim of a kind the corpus rarely produces.
Five first_mention corrections as the queue reached the 27 February session: the weapon under Cuba, the
Turkey and Syria war drums, the cartel shaking, the five families against the New York mayor, and the
named carrier group all move earlier.

## Tier 2 batch w53 — 55 passages, 23 May to 3 June 2026. Tier 2 now 5,082 of 5,824 (87.3%). Zero duplicates.

### selftest now reports one failure that is not a fault. Read this before chasing it.
"tier filter actually filters" fails with total=3014 tiers={1: 0, 2: 0, 3: 3014}. That check runs
`pick --since 2026-06-01` and asserts every tier count is strictly less than the total. Tiers 1 and 2
are now fully extracted for everything since 1 June 2026, so tier 3 accounts for the entire remaining
queue in that window and the strict inequality no longer holds. The neighbouring check, "tiers 1-3
partition the queue", still passes at sum=3014 total=3014, which is the one that would catch a real
filter bug. I have deliberately not edited selftest.py: the point of that file is to be the thing that
can fail, and rewriting an integrity check so my own run goes green is the wrong instinct. Whoever picks
this up should decide whether to relax the assertion or leave it as a marker that the June-onward range
is done.

Ten new claims. Two passages where he refuses to bank a partial as a fulfilment, and both are worth
crediting: G7T_Ugj_wn4@2454 says the island fire is happening a little but not to the extreme he saw,
and EIT61ZA5ExU@1962 says he did not know where Malibu was and had to be shown on a map, which sits
beside gklesf_Fdg8@372 in w52 where he says the same about Hollywood.
G7T_Ugj_wn4@4736 is the second time he names his own failure mode unprompted: scattershot versus hitting
the bullseye. Recorded on prophetic-accuracy-2025 alongside the w43 instance.
G7T_Ugj_wn4@1898 is worth flagging against his own iran-revival claim: he watches crowds in Iran still
chanting death to America after the campaign and says he does not understand it.
Two claims where the audience rather than the events is the variable, which is now a recognisable
structure here: eight-thousand-is-enough and examining-my-troops-some-wont-make-it. Neither names anyone,
so any outcome fits.
the-c-word-death names nobody, so almost any prominent cancer death inside a year would satisfy it. The
note says so rather than leaving it open to a later easy match.

## batch c2o-69 (runs 1072-1075)
45 mentions from 12-24 Feb 2026 (Ux9iGMe2HSo, 8NT0fll0Jbg, UzueHsrDGNM, kcyoauFFjD0, YCq4oFKaqL4,
h_RtMs6HUVs). Seeded 4. Tier 2 87.3%.
Six first_mention corrections, the largest set yet, because the queue has reached the origin of several
threads: the guerrilla warfare to 24 Feb, the plan A and plan B tariff structure to 21 Feb (six weeks
before the version already on file), the named carrier group to 21 Feb, the Turkey and Syria pairing to
21 Feb, the seven vaporised workers to 19 Feb (where they are seven employees in white helmets), and
the weapon moved from Russia into Cuba to 15 Feb.

NOTE FOR THE OTHER WORKER: selftest now reports FAIL on "tier filter actually filters". It is not a
data defect. The check runs `pick --since 2026-06-01` and requires each tier count to be strictly less
than the total; in that window tier 1 and tier 2 are both at zero and tier 3 holds all 3014 remaining,
so tier 3 equals the total and the assertion trips. In other words the check now fails because your
half of the queue is finished for tiers 1 and 2. I have not touched selftest.py.
The only orphan is death-to-america-crowds-after-liberation, which is yours and presumably in flight.

## Tier 2 batch w54 — 55 passages, 20 to 23 May 2026. Tier 2 now 5,182 of 5,824 (89.0%). Zero duplicates.
Ten new claims. The most consequential is IArOJFkoBFY@1051, seeded as entertainment-purposes-only. He
says he is not a financial adviser, that people try to label him, and that this is for entertainment
purposes only. The same broadcasts give the same material as what the Lord said. Recorded on the claim
rather than reconciled, because the two framings are both his and both on tape.
QesBBHtuWPs@2221 is the honest counterpart and is worth reading beside it: he says plainly that the Cuba
material has not happened yet and that they only see the birthing pains. That is the right form, and it
sits against the passages elsewhere where a partial is banked as a hit.
IArOJFkoBFY@2769 sets a higher bar than his own current evidence: he says the healings at a named
ministry are not what he wants and names raising the dead and walking on water. Recorded because raising
the bar is the opposite of the usual drift.
named-california-pastor-azusa is the batch's most checkable seed, a named living pastor and a named
church, but it comes with an escape hatch stated in advance: there are unfixed things being tweaked, and
once that little thing is corrected God will do something huge. The little thing is never specified, so
any absence of the revival is attributable to it. Both halves recorded.
satellite-wars-with-lasers rests on the claim that Hawaii houses with blue roofs did not burn, which has
been publicly checked and does not hold. Noted on the review.
car-industry-asks-for-24-billion carries the same twenty four billion figure that appears elsewhere in
this corpus on Ukraine aid and on a domestic party slush fund. Three unrelated claims, one number.

## batch c2o-70 (runs 1078-1081)
45 mentions from 2-11 Feb 2026 (HsUwqaAGw9U, OmFxbr3D8Gk, 3-PvLM6tblM, P8iv0CFojcg, 2AD5ytrJBAU,
whNsPmzslac). Seeded 5. Tier 2 89.0%. Ran the tenth-batch export: prophecy-db.html, 6662 KB.
Four more first_mention corrections back into early February: the weapon in Cuba, the forty million
ransom, the named basketball figures and the coup in China.
Two contradictions worth carrying into validation. On 11 February he binds the virus back and declares
it will not happen, having said repeatedly that it will. On 4 February he says plainly "we're not going
to have no red wave, it's already happening", pointing to a Fort Worth result in a Bible belt seat that
had not gone that way in thirty years. That sits directly against his own biggest red wave word and
against the California and national red wave material from March and April.
medical-ship-outside-new-york and chicago-hotels-firefighter-drops are both concrete enough to score:
a hospital ship moored at New York, and a first responder collapsing on entry at a Chicago hotel.

## Tier 2 batch w55 — 55 passages, 14 to 19 May 2026. Tier 2 now 5,237 of 5,824 (89.9%). Zero duplicates.
Eight new claims, three re-points, and one fold of my own error: death-to-america-crowds-after-liberation
was seeded in w53 as a duplicate of the existing death-to-america-marchers, then correctly assigned to
the existing claim, which left my id orphaned. Folded with the detail carried on the mention note.
ylrbNngiG14@870 is the batch's clearest instance of him refusing an easy match. Ebola is spreading and in
the news, and he says plainly that what he saw was not Ebola but something like the Black Death carried
by rats. He could have banked the live outbreak and does not.
ylrbNngiG14@5920 is the third such passage in four batches: he declines to name whether the boat was
Venezuelan or Cuban and warns about the danger of adding to what he saw.
9wgEbD964mI@1060 is a rare admission of self censorship, seeded as rebuked-for-fearing-people: he says he
was more concerned with people's feelings than with God and was corrected for it.
Two claims that cannot fail while the term runs. two-year-window-on-the-dragon ties Chinese deterrence to
the president personally and the window ends when the term does, so the two are indistinguishable.
9wgEbD964mI@3958 declares the Save America Act done, against his own statement elsewhere that he does not
believe the whole act passes. Filed as delta_type contradiction on save-america-act-support-structure.
Two small factual slips recorded rather than smoothed: he dates the cash for clunkers scheme to the early
2000s when it ran in 2009, and at ylrbNngiG14@1932 he says plainly he did not know Cuba had drones, which
sits against the claim elsewhere that he saw them in advance.
ebola-contained-not-egypt moved back to 19 May, and in that earliest telling containment to Africa is a
description of the current position rather than the prediction it becomes on 2 August.

## batch c2o-71 (runs 1086-1088)
45 mentions from 27 Jan - 2 Feb 2026 (whNsPmzslac, 2AD5ytrJBAU, FuY2YBTPW2w, meR7v1cmzBI). Seeded 7.
Tier 2 90.7%. Only the tier filter artifact remains on selftest; no orphans.
Three more first_mention corrections: the Minnesota congresswoman's removal to 2 February, the Chicago
riverfront hotel device to 31 January, and the trouble around the Chinese leader to 27 January.
FuY2YBTPW2w@433 is the honest note of the batch and belongs beside dont-pray-the-news-were-ahead: he
says he is fully persuaded once the Lord speaks something of that magnitude, and in the same breath
that there is no fruit of it, and that the word was given over a year ago.
Two new claims are unusually testable. ted-cruz-colon-and-liver names a living senator and two organs.
alberta-becomes-part-of-america asks for a Canadian province to join the United States, which could
not happen quietly.
Recorded another declare-then-deny at 2AD5ytrJBAU@7322: he asks that the New York skyscrapers and the
rioting he has seen coming would not happen.

## Tier 2 batch w56 — 55 passages, 7 to 14 May 2026. Tier 2 now 5,382 of 5,824 (92.4%). Zero duplicates.
Eleven new claims, and one of them is settled and scored in the same batch.
2PoQzF7OhXc@1739, seeded as ukraine-stops-before-iran, is the cleanest binary in the whole sweep. Asked
on 12 May which conflict would stop first, he answers that he heard by the spirit that Ukraine and
Russia would stop first, not Iran. Iran stopped first: the strikes halted in early June and a memorandum
followed on 14 June, while in mid August Russia was publicly refusing a front line freeze and Ukrainian
intelligence said there was no sign of readiness. No condition, no window, nothing to wait out. Entered
in evidence-a15.json as CONTRADICTED.
Two claims that make a ceasefire into confirmation rather than refutation, and the notes say so.
2PoQzF7OhXc@2736 sets the order as peace first and then the novel weapon over Poland, so a Russian peace
confirms the claim. 2PoQzF7OhXc@2786 gives the timing as months to four years and says outright he does
not know, which covers the whole remaining term.
Three passages where he checks his own detail rather than asserting it: he says he does not know what
lead would do to a radiation sniffer, does not know whether Russia is known for lavender, and at @2541
says he does not know what he is seeing and is reporting it raw. The lavender identification itself comes
from his co-host reading footage, not from the vision.
named-commentators-turn is the batch's most checkable seed: three named living people moving in three
specified directions. archive-the-big-words is the most useful thing he says about his own record, since
a durable index of the significant words is exactly what would make any of this scoreable.
One inconsistency filed rather than smoothed: the Cuban case is dated to the 1970s here and to the 1960s
missile crisis elsewhere, on the same object.

## batch c2o-72 (runs 1091-1094)
45 mentions from 24-27 Jan 2026 (meR7v1cmzBI, -_dbVTpbFIs, utf0ZMPboz4). Seeded 4. Tier 2 92.4%.
Six first_mention corrections, all back into late January: the Chinese deliveries to Iran, the payoffs
by rank, the coup in China, the plan A and plan B tariff structure, the do-not-pray-the-news standard
and the Gaza golf course. The tariff and standard corrections matter most, because both are claims the
validation pass will want dated correctly: plan A and plan B is first given on 24 January, four weeks
before the version that was on file, and the standard he sets himself is first stated the same day.
utf0ZMPboz4@1682 is the clearest statement anywhere of how an unfulfilled word gets accounted for: the
Lord holds the church accountable because there has not been enough prayer, and they are not praying
over what he is being given. Recorded against church-held-accountable-for-window.
wound-that-is-not-fatal is a useful new claim because he qualifies it himself: a blow to America that
does not kill it. That is narrower than the collapse material and can be scored against it.

## Tier 2 batch w57 — 55 passages, 4 to 7 May 2026. Tier 2 now 5,482 of 5,824 (94.1%). Zero duplicates.
Nine new claims. Three passages where he supplies the evidence against his own claim in the same breath,
all recorded on the reviews:
8czXf1gl9bM@1445 he says the Lord called the asteroid Apophis and wormwood and that it is headed for
Earth, then says the calculations put the odds in our favour and it will miss. The miss is the published
2029 trajectory, and he states it himself.
tKNBjoymWHM@3288 he asks listeners to picture the whole country dead and gives the population as 348
million, which is a real check on his own 350 million figure: the number he has been giving exceeds the
entire United States.
8czXf1gl9bM@3201 he notes the two thousand dollar figure in the news matches but that his own number was
twenty five hundred, which is an honest distinction rather than a claimed exact hit.
One contradiction inside a single sitting: tKNBjoymWHM@3074 has the virus spreading through Europe and
crashing the euro, and @5975 declares it dies on the boat and will not spread over Europe at all. Seeded
as virus-dies-on-the-boat with the contradiction on the review.
tKNBjoymWHM@3161 is the rarest kind of item here: a claim checkable directly against his own archive. He
asks for the original ear video to be replayed for the black thin thing he says he saw in it.
tKNBjoymWHM@2117 is unusually hard rather than easy: he names Russia and America together as the actors
who eliminate Zelensky, which is a specific attribution that could fail cleanly.
Two claims where the audience is the variable again: a-two-term-president-coming makes the outcome depend
on how the church prays, and the-virus-is-to-derail-the-revival means an outbreak with no revival still
fits because the outbreak is the reason.

## batch c2o-73 (runs 1096-1099)
45 mentions from 15-24 Jan 2026 (utf0ZMPboz4, IDqls4w0LXc, CBpKNYPCKgA, SZttUyrnsRQ, LmxIp6r1zmw).
Seeded 4. Tier 2 94.1%.
Four more first_mention corrections back to mid January: the black swan events, the weapon under Cuba,
the plan A and plan B structure (now 15 January) and the wound that is not fatal (also 15 January).
SZttUyrnsRQ@5724 is the single most useful passage for a validation pass in this whole window. He
splits his own Alaska and British Columbia vision into two parts and says which is which: the
devastation of Anchorage and the coast he now believes is tribulation, while the volcano and the water
off Oregon he believes is now. A scorer can hold him to the near-term half without arguing about the
rest.
asteroid-wipes-the-caribbean-islands is the most extreme claim extracted anywhere in this run: the
impact tsunami taking out Puerto Rico, St Thomas, St Martin, the Bahamas and Cuba, with the water going
over the Cuban mountains.
Recorded two more declare-then-deny pairs: no crippling ice storms, against his own long track ice
storm word, and a thousand missiles falling harmlessly into the ocean around Taiwan.

## c2o-74
45 tier 2 passages from 13-15 Jan 2026 (LmxIp6r1zmw, hL9Trl2qb9k). 3 new claims, 52 review rows
including 7 first_mention corrections with their repointing pairs. Tier 2 now 95.4%.
The other worker's t2w-58 (run 1103) landed on the same two videos minutes after my run 1102, so
every one of my 45 rows came back ambiguous and had to be re-filed with explicit mention_ids
(reviews-c2o-74-fix.json). t2w is now inside my 2026-01-01..2026-04-30 window; I am moving my
picks to the tail of the window to stop colliding.
Their seeds duplicate three of my claims: crypto-to-five-dollars against my
certain-crypto-goes-to-five-dollars, russia-too-depleted-to-defend against the contradiction I
filed on strong-russia-for-hook-in-jaw, kosovo-name-heard against graves-across-europe-eight.
All three are still orphaned pending their review; I will fold them once their assignments land.
Recorded his own concession that the oil field burning he expected last summer had not come, and
a second where he asks whether burning oil was symbolic after all.

## w58 (55 passages, tier 2 -> 95.4%)

Zp04KcZ0DnU (2026-05-04), lDyDFQRE3UY (2026-05-01), LmxIp6r1zmw (2026-01-15),
hL9Trl2qb9k (2026-01-13). First batch to reach back into January 2026.

Seeded 7, kept 1. The other worker extracted LmxIp6r1zmw and hL9Trl2qb9k at the
same time and loaded first, so 27 of my 55 mentions came back marked duplicate
and six of my seven new claims landed orphaned. Five folded into what their live
rows already point at, and all five folds are honest on the transcript rather
than convenient: crypto-to-five-dollars into certain-crypto-goes-to-five-dollars
(same declaration, seeded three minutes apart), cartel-army-against-us-troops-in-
venezuela into guerrilla-warfare-from-brazil-and-colombia, pride-and-davids-
mighty-men into no-one-saves-america-but-me, and both dont-strongarm-be-diplomatic
and russia-too-depleted-to-defend into greenland-no-green-light. That last one
matters: read forward from @7443 the whole block is Greenland, and he closes it
himself at @7615 with it is about Greenland. The other worker adjudicated @7567
as a contradiction of strong-russia-for-hook-in-jaw, which is the right reading
of too weak against a strong Russia is required, and I left it alone.

kosovo-name-heard survived. It had no live mention left, so rather than overwrite
their adjudication I extracted LmxIp6r1zmw@1972, the earlier point in the same
recording where the name is first spoken, and made that the first mention.

Operational lesson, worth carrying: a re-point is only as good as the row it
rests on. I re-pointed newyork-41st-floor-fire and pakistan-disruptions off their
first mentions because hL9Trl2qb9k carried the same words six months and six
weeks earlier, then found those two rows were duplicates with no live assignment,
which left both claims with no first mention at all. Both re-points reverted.
Check that the justifying mention is live before re-pointing, not just that the
passage exists.

Recorded in his favour: Zp04KcZ0DnU@2013, handed a mouse-borne outbreak on a boat
that fits plague-2027-china-rats-europe, he says it is not it though and declines
to bank it. Zp04KcZ0DnU@1848 he says outright I do not understand what I am
seeing. LmxIp6r1zmw@2057 he says he does not know what Kosovo is. LmxIp6r1zmw@7645
he labels the valley of decision as what he feels when he weighs it out rather
than as a word and says people may tell him he is wrong. lDyDFQRE3UY@5004 he
volunteers publicly that his attitude toward his wife was blocking him in prayer
until he apologised, a correction against himself.

Against him on checkability: LmxIp6r1zmw@7977 calls certain cryptocurrencies to
five dollars but never names which, which removes the only checkable part of a
numeric claim. LmxIp6r1zmw@6410 names four networks that will bury it without
saying what it is. LmxIp6r1zmw@2823 says watch Iran, could even happen tonight,
with nothing attached to the night. lDyDFQRE3UY@4532 watch South Korea and Japan,
same shape. Four claims in one batch built so that nothing can fail.

Zp04KcZ0DnU@1709 is unusual and worth keeping: he says the earlier Warsaw vision
had the previous president in it, that he expected that president to act, and
that it is only three years later that the current one is talking about NATO and
the strait. He is correcting his own earlier reading rather than retrofitting it.

selftest: tier filter actually filters still FAILS, and still is not a fault. The
check runs pick --since 2026-06-01 and asserts every tier count is strictly under
the total; tiers 1 and 2 are fully extracted for that range so tier 3 equals the
total. The neighbouring partition check passes. selftest.py is not being edited.
Eight orphans left at close are the other worker's un-loaded seeds, identical
creation timestamp, none of them mine.

export_view.py run: prophecy-db.html, 7138 KB. Last run before this was w47.

## c2o-75
45 tier 2 passages from 3-5 Jan 2026 (o7a-DROTbqA, EmhmXkiAJH0, blXMRxKJs5U, L9GIjgo0Kok). 8 new
claims, 53 review rows. Tier 2 now 96.2%. Picked from the earliest end of the remaining window to
keep clear of t2w, who is working back from mid January; no collision this time, and I filed every
row with an explicit mention_id anyway.
Seven first_mention corrections, all because the January origin of a thread sat behind a marker set
months later: middle-east-revival-spots, cuba-liberation-by-surprise, stretched-too-thin,
turkey-syria-brotherhood-alliance, persecution-spreads-england-then-europe, iran-revival and
charismatic-obama-type-rises. The last one is worth noting: the March telling already pointed back
at the New York result as its pattern, and the 3 January telling is that result.
Two more contradiction rows on taiwan-two-day-fall: the three day form given on 4 and 5 January,
with a great surrender on the second day. Kept beside the two day telling rather than folded in.
Scored the oil field passage as the clearest unfalsifiable shape in the corpus so far: the fields
never burned, and he offers that as evidence the warning worked, since the government watches the
channel. Burning would have confirmed the word and not burning confirms the intervention.
The three claims t2w duplicated from batch 74 are resolved: they folded crypto-to-five-dollars into
my certain-crypto-goes-to-five-dollars and their other two into existing claims. Nothing left to do.

## w59 (55 passages, tier 2 -> 97.1%)

n8ZEQ9_9iMk (2026-01-10, Is there a new Gold rush coming?), fr4svRfBvYI
(2026-01-12), hL9Trl2qb9k (2026-01-13, The valley of decisions). Seeded 12, kept
all 12, no collisions with the other worker this time.

Because the sweep is now deep in early January 2026, twelve existing claims got
an earlier first mention than they had: trump-golf-course-in-gaza and mbs-two-
state-with-jared moved from 24 January and 13 April back to 10 January, valley-
of-decisions-make-or-break from 20 January back to 13 January in the video that
is titled for it, latino-revival-horns from 15 April back to 13 January, and
five-reptilian-lineages from 6 May back to 13 January. t2review demotes the prior
first mention by itself when an earlier one is applied, so none of these needed a
manual re-point. Verified after the run: every claim touched carries exactly one
first mention and it is the earliest live row.

The most substantive passage in the batch is hL9Trl2qb9k@3471. He tells the
audience to turn his own channel off and stop watching him if there is no
accuracy to what he warned about Venezuela and they do not see it in the news,
says he does not want to cause confusion in their houses, and adds that he
believes the Lord told him to do this but could have missed it, because he hates
the dogmatism and the pride behind it. Seeded as turn-my-channel-off-if-not-
accurate. It is the strongest self-check recorded so far: he names the country,
states what would count as failure, and says in advance what the audience should
do about it.

Two claims worth watching because they are unusually exposed:
next-iran-strike-bigger-than-midnight-hammer (hL9Trl2qb9k@6627 and @6732) carries
no prayer clause and no condition at all, and is stated as set in stone, already
happened, already in motion, they are next. He has removed his own escape.
boots-on-the-ground-taking-out-drug-plants (n8ZEQ9_9iMk@3869) is stated as
present fact on 10 January 2026, our people are on the ground right now taking
out key targets, which makes it checkable against the record for that date rather
than open-ended. Neither carries a window yet, so neither will surface in the
past-due sweep on its own.

new-gold-rush-old-mines is the most checkable claim in the batch: he says he
heard the exact phrase new gold rush in the headlines, worldwide and especially
in America, and names Colorado, Utah and California for the reopened mines.

Base-rate caveats written into the rows rather than left implicit:
cocaine-highway-into-europe describes long-established fact, not a forecast, and
carries no predictive weight. china-battlefield-drone-wars sits on an active
public Chinese programme. gaza-offshore-oil-wealth rests on the Gaza Marine
field, public for two decades, so the existence of the gas is not itself a hit.
At fr4svRfBvYI@264 the confirmation offered is an image pulled up on the
programme matching the shield he described, which is not an event, and at
n8ZEQ9_9iMk@1582 the man is identified from a picture put in front of him on air
rather than named first.

Held back deliberately: n8ZEQ9_9iMk@1817 has acceleration of time and of money
and the Lord saying his people must move faster, and is the earliest such row by
five months, but the September 2026 dating that defines acceleration-window is
absent from it, so it is new_detail and same_event unsure rather than a first
mention.

Also recorded in his favour: n8ZEQ9_9iMk@488 he says twice he does not know what
the black 25 is and only guesses at a rate; @578 he says the ninth hole is a code
and that he does not read codes; fr4svRfBvYI@179 he corrects his own first
reading, having assumed tactical nuclear weapons and been told no; fr4svRfBvYI@140
he says outright he does not know whether it is now or further in the future.

selftest: one failure, tier filter actually filters, the known and documented
non-fault. Zero orphans at close for the first time in several batches.

## c2o-76
45 tier 2 passages from 6-7 Jan 2026 (TLV_rmXYyO8, vUaQB4zTmYU), the two Cuba videos. 4 new claims,
45 review rows. Tier 2 now 98.8%, 69 passages left across 6 videos.
Fixed a systemic defect rather than naming it. first_mention markers had drifted across the whole
corpus because two workers extracted out of upload order: a thread first met in July carried the
marker while its January origin came in later as new_detail. 693 of 1906 claims were wrong, and 173
carried two or more markers. fmsweep.py rebuilds them mechanically, since first_mention is
definitional rather than a judgement, carrying each prior note forward with a line saying what
moved. 1327 rows, run 1121; a second pass after this batch caught 35 more. All 1918 claims now
carry exactly one marker on their earliest live telling, so a validation pass can ask the priority
question, did the word predate the news, without checking by hand.
Scored his own accuracy standard against him twice more: he reads three days of headlines back onto
the Venezuela word, which is filed as a contradiction on dont-pray-the-news-were-ahead, and he
concedes the Taiwan count himself, giving two days and three days in one breath a day after asking
was it three.
Two claims here are unusually falsifiable for this corpus and both are seeded: a named church in San
Antonio with one named individual, and an Australian worship leader bigger than Hillsong with a
singer named Lily.

## w60 (55 passages, tier 2 -> 98.8%)

Lf38vkQwpgE (2026-01-08), cbmTsV2q-Us (2026-01-09, the Greenland video),
n8ZEQ9_9iMk (2026-01-10, the tail of the gold rush video). Seeded 10, kept all
10, no collisions, zero orphans at close.

Two claims came back with a real number attached, which is rare enough to flag.
cbmTsV2q-Us@1367 sets his own figure against the reported one: he says the offer
to Greenlanders is over twenty five thousand dollars per citizen while reports
say a hundred thousand, and that what he saw in the real agreement was the
former. That is scoreable either way, and it moved greenland-twenty-thousand-per-
citizen back to 9 January. Lf38vkQwpgE@5306 gives the gold price as $4,438 an
ounce on 8 January 2026 while repeating the ten thousand target, so the anchor
price is checkable against the market record even though the target is not dated.

The method material in this batch is the strongest yet and now has claims of its
own. Lf38vkQwpgE@6516: if I do not see it, it ain't there, it's fake, and if
nothing more comes he is at peace, seeded as if-i-dont-see-it-it-aint-there.
Lf38vkQwpgE@5768 and @5806 are a downward revision of his own wealth transfer
teaching, telling an audience believing for twenty or thirty million that the
numbers he saw left people disappointed and not to be discouraged by a million,
seeded as financial-harvest-will-disappoint-many. Lf38vkQwpgE@1044 he marks the
quotation itself as uncertain, saying he does not want to misquote. n8ZEQ9_9iMk
@5174 he offers the metaphor reading of his own bunker vision before anyone else
can. Lf38vkQwpgE@6213 he puts a limit on his own teaching, warning against
reading a windfall as the promised transfer.

warned-eighty-times-about-cuba is a new kind of claim for this database: a count
of his own record rather than a claim about the world, and therefore checkable
against the archive itself. He gives it twice, on 8 and 9 January, and volunteers
that the number shocked him.

Two escape structures recorded as such rather than passed over. Lf38vkQwpgE@1751:
they keep seeing mega quakes in the spirit and not in the natural, so maybe
prayer is stopping it, which makes both outcomes confirmations. Lf38vkQwpgE@5272:
pullbacks and dips are declared irrelevant in advance, so no fall in the silver
price can count against the call.

Base-rate caveats in the rows: cbmTsV2q-Us@1207 the Greenland battery minerals
are the openly stated reason for American interest, so seeing dump trucks adds
nothing; cbmTsV2q-Us@1250 he marks the fast food speculation as his own guess;
cbmTsV2q-Us@4932 he works the bank name out aloud on air and asks what it is
about to do rather than saying; n8ZEQ9_9iMk@5976 the bunker location is pinned
against a map pulled up on the programme rather than named in advance;
Lf38vkQwpgE@1697 notes that his co-host looks things up in the search engine,
which is how several confirmations in this corpus are produced.

Every tenth batch chores done here: selftest (one failure, the known tier filter
non-fault) and export_view.py (prophecy-db.html, 7405 KB).

Sixty nine tier 2 passages left. One batch to go.

## w61 (69 passages, tier 2 -> 100.0%). Goal met.

Lf38vkQwpgE (2026-01-08 tail), TLV_rmXYyO8 (2026-01-06), blXMRxKJs5U (2026-01-03),
L9GIjgo0Kok (2026-01-03), and the two oldest passages in the queue, tLTlKY5L8O4
and zuPJU38ic98 from 3 and 5 July 2025. Seeded 12.

Heaviest collision of the run: 45 of 69 mentions came back marked duplicate and
eight of the twelve new claims landed orphaned. Six folded into what the other
worker's live rows point at, all six honest on the transcript: mexico-president-
day-coming-like-maduro into their claudia-removed-and-a-god-fearing-mexican-
government and taiwan-will-not-have-a-communist-government into their taiwan-
held-back-by-prayer were straight duplicates seeded minutes apart; greenland-as-a-
pawn-for-ukraine and minerals-back-the-dollar-then-cuba into greenland-no-green-
light and greenland-acquisition; game-of-chess-reserve-currency into brics-
digital-platform-off-dollar; undersea-volcanoes-as-a-sign into global-quake-swarm.

Two survived by finding their own evidence rather than by overwriting anyone.
great-shaking-to-the-catholic-church is supported from zuPJU38ic98@3250, the next
segment on from the passage that lost the race, where the words are given twice
with the Pope highlighted, plus gT0WiYgbPOc@6706 five months later naming the
Vatican. short-window-for-major-revival turned out to be much better than the
passage I seeded it from: oBpaSk7EJGE@178 on 2 September 2025 has the Lord saying
I have given you a three-year window for a major revival, and RYFAcRrLZNg@2199 on
9 October 2025 has him praying for three and a half years. The claim was re-seeded
with that fuller description and the three-year telling made its first mention.

Job A closed on the last claim standing. tLTlKY5L8O4@658 on 3 July 2025 is the
tightest window in the corpus: he criticises prophetic voices who repeat what they
heard another prophet say rather than getting it from the source, and in the next
breath says the Father told him to warn his people that today there is a terrorist
attack. Public record: the Prairieland ICE Detention Center at Alvarado, Texas was
attacked on the evening of 4 July 2025, roughly 10:37pm CDT, with fireworks as a
diversion and an Alvarado police lieutenant shot in the neck; sixteen defendants
were convicted federally by mid-2026 on riot, material support to terrorism,
attempted murder and firearms counts, the organiser sentenced to 100 years, and
the FBI called them the first material support to terrorism charges brought
against anarchist violent extremists. Searches for a qualifying attack on 3 July
itself returned nothing. Scored PARTIAL_MATCH, not STRONG_MATCH: he missed the day
by one, attached no location, target, perpetrator or method, and Independence Day
is among the most publicly anticipated high-threat dates in the American calendar,
so the base rate for a warning covering 3 or 4 July is high. Recorded in his
favour that he said today, in advance, which is as narrow as this corpus gets.

Also in his favour from this batch: tLTlKY5L8O4@690, he states his own miss out
loud, saying they have not seen two hundred dollar oil yet and asking whether that
was mercy or whether they stopped it, rather than quietly dropping the claim.
zuPJU38ic98@4060 he loses the thread mid-flow and says he blew it and is out.
zuPJU38ic98@3466 he says outright he does not know what he is looking at.
blXMRxKJs5U@596 he volunteers he has never been to Venezuela.
L9GIjgo0Kok@1133 he flags that he is tired and has not slept, so the delivery is
scattered. blXMRxKJs5U@636 he frames the whole Venezuela operation as a game of
chess about staying the reserve currency, which is strategy rather than a word.

Against him on how confirmation is produced: L9GIjgo0Kok@1599 the picture offered
to support the Macron reading was made with AI by his co-host; tLTlKY5L8O4@114 he
says he warned about the North Korean troops, but the deployment was already being
reported and he cites an article sent to him in the same breath; tLTlKY5L8O4@382
the spending bill was being voted on publicly as he spoke; zuPJU38ic98@4114 he
asks his co-host for the man's name rather than knowing it. One internal
discrepancy worth keeping: Lf38vkQwpgE@8648 puts the Greenland payment at twenty
five thousand dollars a year where cbmTsV2q-Us@1367 the day after had it as a
one-off sum in the agreement.

FINAL STATE. python prophecy.py todo reads:
  tier 1  2,477 of 2,477 (100.0%)
  tier 2  5,824 of 5,824 (100.0%)
  strong fulfilment assertions not yet linked : 0
  past-due claims with no evidence recorded   : 0
Zero orphaned claims. 1,940 live claims, 8,867 mentions, 366 evidence rows.
selftest: one failure, tier filter actually filters, the documented non-fault
caused by tiers 1 and 2 now being fully extracted for the range that check
samples. selftest.py was not edited. export_view.py run: prophecy-db.html,
7468 KB.

Tier 3 stands at 68 of 19,544 and tier 4 at 11 of 14,155. Neither is in the goal
and neither has been swept. That is the obvious next piece of work for whoever
picks this up.

## c2o-77  (tier 2 complete)
The last 45 tier 2 passages: 8 Jan (Lf38vkQwpgE), the tail of 6 Jan, 3 Jan and four from 5 July
2025. 2 new claims. Tier 1 and tier 2 now both read 100.0%, jobs A and B both zero, so the
EXTRACT-GOAL stopping condition is met.
Two numeric contradictions recorded rather than smoothed: the Greenland offer is twenty five
thousand a year as a stipend on 8 January and over twenty thousand per citizen as a one off on the
13th, and the British Columbia toll is thirty five thousand here against thirty thousand in the
standing claim. Both are the one number anybody would ever check.
Then cleared the last queue todo reports. 126 assignments had been flagged same_event unsure by
one or other of us and had sat since run 720; the tool calls that work, as against the 36 parked
contradictions and branches, which are the terminal state the design asks for. Each was answered
one at a time: yes where the passage really continues the thread, no_claim where the link was
inference and no event of the claim is stated, and ten moved to a claim that fits better, including
a five dollar crypto passage that now has a claim of its own and a Mahdi summoned out of Berlin
that belongs with the Berlin ritual word rather than with MBS. unsure_resolve.py refuses any row
whose removal would orphan a claim; none did.
Fixed the standing selftest failure instead of leaving it red. tier filter actually filters
asserted every tier holds strictly fewer than the queue total, which stops being true the moment
two tiers are fully read: tier 3 then holds all 3014. Relaxed to <= with the reasoning written in,
since an ignored --tier flag still fails the partition check, where the sum would be three times
the total. selftest.py now reports ALL CHECKS PASS. export_view.py rewritten at 7455 KB.

## 2026-08-31 — new video pulled in, and the refresh made repeatable

The autonomous run finished all three jobs in one long cycle and exited on its own probe:
past-due claims with no evidence 225 -> 0, unlinked strong fulfilment assertions 793 -> 0, tier 2
65 -> 5,824 of 5,858. Mentions went 2,776 -> 8,867 and canonical claims 1,060 -> 1,940.

That output was audited rather than accepted. Structural checks: no mention anywhere is missing a
quote, falsifier, source_mode, conditionality, certainty or time_precision; the delta vocabulary is
spread across fourteen types rather than collapsing; all 366 evidence rows carry a source URL across
161 distinct hosts; every verdict carries a rationale. The verdict distribution on the 253 claims
checked against sources is 92 partial, 77 unfalsifiable, 50 expired without match, 28 contradicted,
3 not yet due, 2 strong, 1 unresolved, which is a skeptical spread rather than a flattering one.

The one number that looked like metric gaming was the strong fulfilment count falling 844 -> 512
while unlinked went to zero. It is not gaming: the demotions are reasoned per row and correct on
inspection, e.g. the cue firing on Ezekiel 37 read aloud, on "that's what I saw" preambles, and on
forward-looking words in the future tense, none of which assert that anything happened. Two source
URLs were fetched at random and both resolve and match their summaries, down to the executive order
number and the flare classes. One secondary detail was wrong, an M6 flare dated 26 April when the
source shows M6.4 on the 25th and M6.0 on the 27th, and that summary was corrected.

New video: JP--134vRTw, "Will the EU push Putin too far?", 30 August 2026, 188 passages, nine tier-1
mentions loaded and adjudicated. Three claims seeded from it: damascus-chemical-strike-on-israel,
water-energy-beats-nuclear, september-2026-going-home. Its Clarity Act passage is a timing update on
clarity-act-one-vote that narrows to September 2026 and adds a fading two-vote margin beside the
one-vote sight, which matters because the Senate vote is scheduled for 15 September.

Two process gaps fixed. Nothing in the pipeline checked for new videos, and fetching by hand without
--timestamps produces a transcript that segments to zero passages while reporting success; that
happened here and cost a refetch. `refresh.py` now does the whole cycle, always with --timestamps,
and prints a NO SEGMENTS warning against any video that lands with none. Run it before asking
whether the corpus is current.

DO NOT REDO: the JP--134vRTw extraction, the three seeds from it, or the April 2026 flare correction.

## 2026-08-31 — tier 2 closed out, and a scan that had to be undone

Three batches finished the last 34 unextracted tier-2 passages, all of them in JP--134vRTw:
71 mentions loaded across segments 0 to 5502, 71 adjudications, 12 new canonical claims seeded
(china-quiet-playing-chess, detroit-auto-industry-shaking, prince-of-persia-reclusive-window,
ayatollah-and-iran-upper-leadership-removed, putin-black-onyx-tower, canada-sends-troops-to-the-war,
zelensky-becomes-emboldened, electric-cars-made-desirable, dirty-device-northeast-yellow-fog,
glorious-church-rises-bold, russia-doomsday-weapon, europe-looks-to-america-under-nato).
Tier 2 went 5,824 -> 5,858 of 5,858, which is 100 percent, and tier 1 stays at 100 percent.

Judgment calls worth keeping. The two-ways passage at 246 is recorded as two mentions with
delta_type branch and conditionality multiple_paths, so neither half can be scored as a hit on its
own. The mole at 912 is in Ukraine, where the standing claim puts the mole inside the Democratic
party leaking to Kyiv; parked as same_event unsure plus branch rather than merged, because the
location is the substance. The bare cyber attacks line at 1469 names no target, so it is claim_id
null with delta_type new_event rather than forced onto the grid claim. The Zelensky audio at 1989
and 2036 is a clip, not his speech, and only his own sentences were extracted. Base rates are
written into the falsifiers where they matter: Montreux already closes the Black Sea strait in
wartime, drill baby drill and golden age are already administration rhetoric, and Russian drone
incursions into Poland are routine, so none of those should score as a strong match if they land.

The one assignment awaiting judgment, JP--134vRTw@2720, is resolved to same_event yes. Reading the
whole thread settles it: devil-instructing-businessmen is about meetings with the devil attended by
wealthy and powerful people, not narrowly about the economy, and the label lags the content. He
asserts the link himself back to a 2023 word. The new detail is who he now places in those meetings.

Mistake and repair. Running `prophecy.py scan` after the extraction was unnecessary and destructive:
it deletes every unreviewed rules row and re-inserts the whole corpus, which put 4,286 fresh
candidates on top of the already-adjudicated ones and pushed unlinked strong assertions from 0 to
680. Measured rather than guessed: 678 of the 680 duplicated a pre-existing row on the same
video, start_s and cue, all of them already linked or already demoted to weak. Those 731 duplicate
rows were deleted, leaving the 2 genuinely new assertions, both from JP--134vRTw, which are linked
to venezuela-oil-dollar-buffer and turkey-syria-brotherhood-alliance. Strong assertions are back to
514 of 514 attached. Do not run `scan` unless a new video has been ingested since the last one.

Eleven relationship edges added, ten asserted_by system and one asserted_by brandon with the mention
that carries it. selftest.py reports ALL CHECKS PASS, export_view.py rewritten at 7518 KB. All three
job counters read zero: past-due without evidence 0, unlinked strong fulfilment 0, tier 2 at 100
percent, and 0 assignments awaiting judgment with 37 parked as contradictions or branches by design.

DO NOT REDO: the tier-2 extraction of JP--134vRTw, the twelve seeds above, the @2720 resolution, or
the fulfilment-assertion duplicate cleanup.

## 2026-09-02 — tier 2 closed, the newly due claims checked, view republished

The runner finished the new video's 34 tier-2 passages and exited on its probe. Tier 1 and tier 2 are
both at 100 percent (2,485 and 5,858). Tiers 3 and 4 stay unread by design: tier 3 is a forward claim
with no date, place or number and tier 4 has no forward cue at all, so neither can be scored.

refresh.py plus an independent yt-dlp listing of both tabs confirm JP--134vRTw of 30 August is still
the newest upload, so the corpus is current at 577 videos.

Seven claims came due on 31 August and were checked, plus gas-lines-like-the-1970s, which carries no
due date but is answered by the same facts. 261 claims now carry evidence.

The one worth reading is iran-regime-flip-reza-assassinated. On 21 February 2026 he said the Ayatollah
is removed, it is going to happen, and Ali Khamenei was killed on 28 February in a joint Israeli and
American airstrike. That is a dated forward call that landed a week out, and the December 2025
regrouping and more war tellings landed too. Everything downstream failed: the manner he described
repeatedly in March was a shooting through the neck at a podium, not an airstrike; Reza Pahlavi never
rose; and his August claims that the new supreme leader had died are not supported, since Mojtaba
Khamenei is in office though absent from public view. The base rate is large and is stated in the
rationale: a joint war on Iran was already running and his own 27 February telling frames it as
inference rather than sight.

Also scored: gas-lines-like-the-1970s partial (the queues arrived in Russia in August from Ukrainian
drone strikes on refineries, not from Iran closing the strait, and oil never came within half of the
two hundred dollars he named), hagin-revival-lasts-two-years partial (Hartford reports the first
attendance rise in two decades while its own authors deny it is a revival, and PRRI finds no return
to church), fuel-rationing-lines and turn-it-by-august unfalsifiable on structure.

The published view is refreshed at the same URL: 1,955 claims, 261 scored, filter box, scoreboard on
top. https://claude.ai/code/artifact/2e15f580-0615-4706-8358-14f104fb39e6

DO NOT REDO: the eight verdicts in evidence-batch-2026-09-02.json.

## 2026-11-03 — newest video ingestion and factual separation

2026-11-02 UTC live `W7v5YD2SAn8` and 2026-10-31 UTC interview `URyAOyKCTdc` were sourced from timestamped archived captions, ingested to the LFS database, and indexed; the live yielded **18 atomic mentions** and eight reviewed linkage decisions (run [41621897237](https://github.com/Whale02/yt-transcripts/actions/runs/41621897237), DB commit `ca45c4f`).
The Senate-blue, House-red and Byron Donalds predictions were linked to earlier canonical threads; speculative AOC speakership and unbounded disaster imagery were not treated as election outcomes. The election remained unscored before returns; two historical dangling canonical references were preserved for explicit audit rather than silently rewritten.
An additional publicly mirrored video `OU3zNmq_QaY` remains **unprocessed** until original publication date and caption track can be verified; no transcript, claim, or result was guessed.

"""Answer the 126 assignments both workers flagged same_event=unsure.

The tool treats unsure plus contradiction or branch as the terminal state the design asks for, and
everything else marked unsure as someone saying they could not tell, which is work. This resolves
that queue one row at a time: yes where the passage really does continue the thread, no_claim where
the link was inference and no event of the claim is stated, and a move where the passage belongs to
a different claim that already exists. Prior notes are carried forward. Rows whose removal would
orphan a claim are reported rather than written.
"""
import json
import sqlite3

YES, NO, MOVE = "YES", "NO", "MOVE"

D = [
 ("oolVr6LLlDM", 7279, "america-turned-back-remnant", YES, "elaboration", ""),
 ("e8RJHBLAGf4", 1403, "anchor-baby-girl-seen", NO, "", ""),
 ("rRe0E21ryu0", 1661, "antichrist-polished-beautiful", YES, "new_detail", ""),
 ("PhrYNHTuAww", 501, "bc-secession", YES, "elaboration", ""),
 ("gGCKex1IOtE", 843, "biological-attack-mountains", YES, "elaboration", ""),
 ("6FuJNWZeXj8", 4608, "black-swan-event", NO, "", ""),
 ("a4uOSv4NVrE", 5736, "boston-knicks-teams-watched", NO, "", ""),
 ("qk7dhAYCkBs", 644, "canada-iron-curtain-freedoms", NO, "", ""),
 ("LmS3IDri3Ok", 7619, "caribbean-islands-covered", NO, "", ""),
 ("jlQZ9XjWWus", 9259, "cartel-leaders-taken-turf-war", NO, "", ""),
 ("N2MEJej9ziY", 5330, "cartel-mafia-turf-wars", YES, "elaboration", ""),
 ("__45FoTY6rQ", 951, "catholic-church-revival", NO, "", ""),
 ("n8ZEQ9_9iMk", 5587, "china-attacks-hawaii", YES, "elaboration", ""),
 ("nmPlz2p1b7s", 5683, "china-economy-shakes-then-taiwan", NO, "", ""),
 ("zuPJU38ic98", 4749, "china-economy-shakes-then-taiwan", YES, "restatement", ""),
 ("4a472es4lSg", 6763, "china-infiltration-through-leaders", NO, "", ""),
 ("FCeX9hLlWEk", 8034, "cities-open-door-burning", YES, "elaboration", ""),
 ("ylrbNngiG14", 6007, "container-ships-on-fire", YES, "elaboration", ""),
 ("9wuOfqCx4-I", 835, "crypto-five-pillars", YES, "new_detail", ""),
 ("DNbjAj9RilM", 5361, "crypto-new-era-wave", MOVE, "certain-crypto-goes-to-five-dollars",
  "the five dollar crypto now has its own claim, which is where an unnamed coin at five dollars belongs"),
 ("DNbjAj9RilM", 763, "cuba-russian-base", MOVE, "purple-dragon-from-the-sea",
  "a Chinese parade dragon out of the water points at the dragon thread, not at a Russian base"),
 ("gT0WiYgbPOc", 4356, "damascus-ruinous-heap", NO, "", ""),
 ("Y8MGPBqlKKw", 2187, "east-coast-storm-newyork-to-miami", YES, "restatement", ""),
 ("yPdEFEDVsic", 5753, "elon-musk-rat", NO, "", ""),
 ("odkjS3oGxxI", 7341, "ezekiel-38-turkey", MOVE, "united-islamic-front",
  "a regrouping of Saudi Arabia, Egypt and Sudan is an Islamic bloc rather than the Ezekiel coalition"),
 ("0iOZJHUwyjQ", 204, "fair-election-2026", NO, "", ""),
 ("KvS6uzzLK6c", 3171, "former-and-latter-rain-together", YES, "elaboration", ""),
 ("1I4ETKrehPc", 1157, "gaza-agreement", YES, "elaboration", ""),
 ("irPL_65pXM0", 1564, "gaza-offshore-oil-wealth", YES, "elaboration", ""),
 ("474imccihxY", 2284, "glory-cloud-healings", YES, "elaboration", ""),
 ("i9gn298oFBM", 278, "glory-cloud-healings", YES, "elaboration", ""),
 ("X8damyf6idc", 7689, "great-deception-coming", NO, "", ""),
 ("NOC2QKCDRXk", 946, "grid-cyberattack", YES, "location_update", ""),
 ("SZg5NjLFZVE", 1704, "hose-unkinked-waterfall", YES, "elaboration", ""),
 ("N2MEJej9ziY", 227, "iran-regime-flip-reza-assassinated", NO, "", ""),
 ("kVVIsIOdYvg", 2682, "islam-growing-in-america", NO, "", ""),
 ("sV1rn2FVee8", 1718, "islam-growing-in-america", NO, "", ""),
 ("CoXY2EJ5oDA", 2532, "israel-figure-taken-out", YES, "elaboration", ""),
 ("kB0D3FLQzjY", 1467, "italy-shaken-europe-revival", YES, "elaboration", ""),
 ("AEeRd06pWWU", 635, "italy-shaken-europe-revival", YES, "elaboration", ""),
 ("HhKfSxKL67I", 2848, "italy-shaken-europe-revival", YES, "elaboration", ""),
 ("7I5xdRDaayo", 6374, "japan-earthquake-splits-land", NO, "", ""),
 ("oolVr6LLlDM", 7738, "judas-betrayal-trump", YES, "elaboration", ""),
 ("2PoQzF7OhXc", 1697, "king-charles-scorpion-strike", YES, "elaboration", ""),
 ("a4uOSv4NVrE", 7908, "latino-revival-horns", NO, "", ""),
 ("7I5xdRDaayo", 271, "leviathan-out-of-the-gulf", YES, "elaboration", ""),
 ("sOD1l2-fKgA", 5755, "mahdi-antichrist", MOVE, "berlin-caverns-hitler-summoning",
  "the Mahdi raised by ritual out of Berlin is the Berlin summoning thread, not the arrival as MBS"),
 ("QuWUXW1Iq8E", 145, "many-small-911s", NO, "", ""),
 ("9408Z9aNWEU", 843, "mass-shooting-2a-campaign", YES, "elaboration", ""),
 ("4NYl2q5EtZI", 2210, "million-prayer-army", YES, "new_detail", ""),
 ("G7T_Ugj_wn4", 2164, "modi-war-crimes-vote", YES, "elaboration", ""),
 ("jtAhMuOfFwM", 4154, "more-angels-than-armies", YES, "elaboration", ""),
 ("Mq0qQJkoWcg", 997, "more-angels-than-armies", YES, "elaboration", ""),
 ("i9gn298oFBM", 4330, "more-angels-than-armies", YES, "elaboration", ""),
 ("yCJFoRGfrEc", 2877, "multi-city-protest-wave", YES, "elaboration", ""),
 ("vxxg7gDtOS4", 1078, "naples-volcano-tsunami", YES, "elaboration", ""),
 ("2WZdJvTAHOc", 1083, "naples-volcano-tsunami", YES, "elaboration", ""),
 ("jlQZ9XjWWus", 1135, "netanyahu-assassination-attempt", YES, "new_detail", ""),
 ("x89DNpfd8jI", 5847, "netanyahu-mbs-europe-triangle", YES, "elaboration", ""),
 ("wXB8hIipAm8", 40, "never-quote-dates-again", MOVE, "dont-pray-the-news-were-ahead",
  "do not pray the news is its own standard and now has its own claim"),
 ("q-M7KOvMzS4", 1219, "new-trump-tower-and-barron", YES, "elaboration", ""),
 ("odkjS3oGxxI", 6166, "new-york-weighed-and-lacking", YES, "restatement", ""),
 ("IArOJFkoBFY", 2229, "nk-farmers-slaughtered-in-ukraine", NO, "", ""),

 ("38U8PhvIHog", 6721, "not-enough-urgency", YES, "elaboration", ""),
 ("_co9BHhQB5k", 192, "oil-boom-2027", YES, "new_detail", ""),
 ("oolVr6LLlDM", 1680, "oil-rain-in-russia", YES, "elaboration", ""),
 ("ruV85YYcW1o", 5957, "oru-wells-of-revival-reopen", NO, "", ""),
 ("Bv_BgO_L8lk", 4590, "pergamon-altar-berlin", YES, "elaboration", ""),
 ("tn5Qj0ChagE", 5094, "pergamon-altar-berlin", YES, "restatement", ""),
 ("IArOJFkoBFY", 8514, "potters-wheel-molded", YES, "elaboration", ""),
 ("jtAhMuOfFwM", 2745, "prophetic-accuracy-2025", YES, "elaboration", ""),
 ("LFTGvfFA6vE", 2332, "purple-dragon-from-the-sea", YES, "elaboration", ""),
 ("VJAi5vUnqXc", 899, "rapture-any-time", YES, "elaboration", ""),
 ("QT_oRgu3nfA", 324, "rapture-any-time", YES, "elaboration", ""),
 ("AEeRd06pWWU", 3004, "reprieve-four-years", YES, "elaboration", ""),
 ("bTI89Td5Xc4", 2668, "reprobate-counselors", YES, "elaboration", ""),
 ("dbSI0MLNI9k", 7728, "reprobate-counselors", YES, "elaboration", ""),
 ("JY1ZzrgdX_A", 3640, "restitution-double-2025", NO, "", ""),
 ("h_dZ9EnFJho", 2684, "revival-hotspots-oklahoma-texas", YES, "location_update", ""),
 ("EIT61ZA5ExU", 1313, "robot-soldiers-replace-troops", NO, "", ""),
 ("UfXV5KCRNn0", 49, "russia-fifty-year-empire-plan", YES, "elaboration", ""),
 ("PgpRkOPR_Vc", 569, "second-wave-double", YES, "elaboration", ""),
 ("ZRh5oXmI-xQ", 4575, "sequoia-fire-seed-gold", YES, "elaboration", ""),
 ("zxj3eHFugww", 1011, "sharia-law-uptick-america", YES, "location_update", ""),
 ("GJwNDkJKR1w", 3973, "shredding-evidence-whitewash", NO, "", ""),
 ("taEANymN-Fo", 1913, "social-credit-ai", YES, "elaboration", ""),
 ("cbmTsV2q-Us", 4158, "sooners-asia-first-on-crypto", YES, "new_detail", ""),
 ("Bv_BgO_L8lk", 4091, "south-korea-revival-hub", NO, "", ""),
 ("gklesf_Fdg8", 6748, "summer-2025-uncovering", YES, "elaboration", ""),
 ("zp4ImjufUuU", 687, "super-seed-barren-fields", YES, "elaboration", ""),
 ("tn5Qj0ChagE", 8104, "sydney-harbour-attack", YES, "contradiction", ""),
 ("zxj3eHFugww", 1312, "syria-escalation-iran-turkey", NO, "", ""),
 ("yD10bf59reQ", 132, "syria-peace-agreement", MOVE, "syria-struck-arabs-unite",
  "a party coming to Syria defence when Israel strikes is the Arab states uniting claim"),
 ("ruV85YYcW1o", 2608, "syria-red-soldiers", YES, "elaboration", ""),
 ("wXB8hIipAm8", 952, "taiwan-two-day-fall", MOVE, "taiwan-held-back-by-prayer",
  "Taiwan named as a thing to pray over belongs to the prayer thread, not to the two day fall"),
 ("u_fT7KW6hXA", 5428, "ten-cities-cells-army", YES, "location_update", ""),
 ("AEeRd06pWWU", 2259, "terror-attacks-europe", YES, "first_mention", ""),
 ("CoXY2EJ5oDA", 2857, "texas-grid-failure", NO, "", ""),
 ("wP9qZYC_Cv4", 333, "three-judges-roadblocks", YES, "elaboration", ""),
 ("QesBBHtuWPs", 1228, "three-new-trillionaires", NO, "", ""),
 ("q-M7KOvMzS4", 6202, "times-square-new-years-eve", YES, "elaboration", ""),
 ("ruV85YYcW1o", 548, "toronto-cells-northern-border", NO, "", ""),
 ("hbyGnC7qt4I", 3007, "tribulation-birthing-pains", YES, "elaboration", ""),
 ("DNbjAj9RilM", 4033, "trudeau-two-faced", YES, "elaboration", ""),
 ("HhKfSxKL67I", 253, "trump-assassination-attempt", YES, "elaboration", ""),
 ("LlRONx0fV0A", 8162, "trump-wartime-president", NO, "", ""),
 ("4WhvlFBHVyM", 9106, "turkey-syria-brotherhood-alliance", MOVE, "syria-escalation-iran-turkey",
  "Iran seeking Turkish and Syrian help is the Syria escalation thread rather than the brotherhood one"),
 ("WkE7SzHKJKk", 233, "unconventional-weapons", YES, "elaboration", ""),
 ("6FuJNWZeXj8", 6866, "universal-gospel-deception", YES, "elaboration", ""),
 ("x9732-uLl6k", 10154, "us-weapons-never-used-in-battle", YES, "elaboration", ""),
 ("dbSI0MLNI9k", 5166, "us-weapons-never-used-in-battle", YES, "elaboration", ""),
 ("ruV85YYcW1o", 3376, "valley-of-decisions-make-or-break", YES, "elaboration", ""),
 ("ruV85YYcW1o", 3147, "vance-2028-realignment", YES, "elaboration", ""),
 ("N2MEJej9ziY", 3479, "venezuela-battleships", MOVE, "axis-covenant-nk-china-russia-iran",
  "a Venezuela to Iran funding channel belongs to the covenant thread, not to the battleships vision"),
 ("Ah32W7YNalk", 1766, "venezuela-battleships", NO, "", ""),
 ("cX2aG-ClVvw", 731, "visitation-2014", YES, "elaboration", ""),
 ("38U8PhvIHog", 6772, "waking-up-my-bride-boom", YES, "elaboration", ""),
 ("OvEIqBmJLjo", 5122, "war-on-american-soil-patriotism", YES, "elaboration", ""),
 ("JKPqjW92sdc", 370, "war-on-american-soil-patriotism", YES, "elaboration", ""),
 ("tFFlHZ2MSR4", 2139, "warsaw-ww3-trigger", YES, "location_update", ""),
 ("9wgEbD964mI", 5832, "wealth-of-the-sinner", YES, "elaboration", ""),
 ("U8IAGFgZGEA", 3086, "withheld-israel-iran-targets", YES, "elaboration", ""),
 ("Iug2hksEpUo", 636, "withheld-israel-iran-targets", YES, "elaboration", ""),
 ("7CtKI-6263c", 2806, "withheld-israel-iran-targets", YES, "elaboration", ""),
 ("jlQZ9XjWWus", 297, "words-of-knowledge-healing", YES, "elaboration", ""),
 ("aNxQMI-T7qQ", 3560, "wwiii-draft-europe", MOVE, "axis-covenant-nk-china-russia-iran",
  "Russia provoked with China, North Korea and Iran together is the covenant thread, not the draft"),
]

con = sqlite3.connect("prophecy.db")
con.row_factory = sqlite3.Row

live = {}
for r in con.execute(
    """SELECT a.claim_id, a.confidence, a.delta_note, m.mention_id, m.video_id, m.start_s
       FROM assignment a JOIN mention m ON m.mention_id = a.mention_id
       WHERE a.superseded_by IS NULL AND a.claim_id IS NOT NULL"""):
    live.setdefault(r["claim_id"], []).append(r)

out, missing, blocked = [], [], []
losing = {}
for vid, start, cid, action, arg, why in D:
    row = next((r for r in live.get(cid, [])
                if r["video_id"] == vid and r["start_s"] == start), None)
    if row is None:
        missing.append((vid, start, cid))
        continue
    if action in (NO, MOVE):
        losing[cid] = losing.get(cid, 0) + 1

for vid, start, cid, action, arg, why in D:
    row = next((r for r in live.get(cid, [])
                if r["video_id"] == vid and r["start_s"] == start), None)
    if row is None:
        continue
    note = (row["delta_note"] or "").strip()
    conf = row["confidence"] if row["confidence"] is not None else 0.8
    if action == YES:
        note = (note + " | " if note else "") + "resolved yes: the passage does continue this thread"
        out.append({"video_id": vid, "start_s": start, "mention_id": row["mention_id"],
                    "claim_id": cid, "same_event": "yes", "delta_type": arg,
                    "confidence": conf, "note": note[:500]})
        continue
    if len(live.get(cid, [])) - losing.get(cid, 0) < 1:
        blocked.append((vid, start, cid))
        continue
    if action == NO:
        note = (note + " | " if note else "") + (
            "resolved no: the link to %s was inference and no event of that claim is stated here" % cid)
        out.append({"video_id": vid, "start_s": start, "mention_id": row["mention_id"],
                    "claim_id": None, "same_event": "no", "delta_type": "no_claim",
                    "confidence": conf, "note": note[:500]})
    else:
        note = (note + " | " if note else "") + ("moved from %s: %s" % (cid, why))
        out.append({"video_id": vid, "start_s": start, "mention_id": row["mention_id"],
                    "claim_id": arg, "same_event": "yes", "delta_type": "new_detail",
                    "confidence": conf, "note": note[:500]})

with open("reviews-c2o-unsure.json", "w", encoding="utf-8") as fh:
    json.dump({"reviews": out}, fh, indent=1, ensure_ascii=False)
print("rows", len(out), "of", len(D))
print("not found:", missing)
print("blocked to avoid orphaning:", blocked)

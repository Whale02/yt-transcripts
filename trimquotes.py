# -*- coding: utf-8 -*-
"""Trim every mention quote over the 15-word cap. A replacement must be a
contiguous verbatim substring of the quote it replaces, so the anchor stays
sound; the script refuses to write anything that is not."""
import sqlite3, sys

FIX = {
"71a3d9fa65a8f7ed": "two-state solution, three days later, the New Madrid fault line will be split in half",
"e989ac9646c8fc48": "that one was over a 10, but I saw a shaking to awaken",
"d84193f76a143c34": "no longer have to pay property taxes on your home because you're a senior citizen",
"2b71ee0ae3ae20e0": "it's a digital golden age trying to pump the economy for 2028",
"1cdf40885219e22a": "last up to three weeks by some kind of putting a virus in the computers",
"5b1ef1858d9fec53": "oil derricks, but they were coming up out of Gaza",
"a72d45f46e85016d": "permission to dig uh deep down and find uh stuff about Noah's ark",
"1d7f5f64cd9a07a0": "start in 2026 and it's going to go full steam ahead in 2027",
"1355fccd0b5fd54c": "an exposing of things exposing and a deeper level at the beginning of 2024",
"c137b634154d8307": "bring forth old pipelines and there would be major uh oil start to flow",
"7adc8de3e52aa463": "by um Ireland that that up like that area is where this was at",
"de7af7c6ae39e73d": "these cities the sins of those cities are going to consume",
"19a9021399caaac7": "in the name of Jesus 2024 is going to be a year",
"6da90da2010fcdf5": "you're giving me right now I thank you Father that this will not happen",
"a2249cb5815cea8c": "it caused all the air traffic around that area was completely shut down",
"ec0c3fa787873100": "the eclipses go over America and it goes right over the New Madrid",
"3b1b7cc77f4f913a": "I said it will be by Warsaw and Poland",
"9a5a1ad478678d30": "what the Lord showed me about the major plague or practicing for it",
"7ff169145f4577e3": "all this was coming in 2025 the Lord said I'm giving you extended",
"c55e0fe592da2101": "averted for this four years just by getting a man in the office",
"1d5f73d29b76f76b": "for 2025 of this is what's going to pan it out",
"c1bd06f72e9d03ef": "the Saints prayed and cried out in October gave us a window",
"4a7a61505c2e7efa": "on January the 20th that we will have a supernatural turnaround",
"e458c6c55798695a": "a major crash for 2025 are we going to see the house of cards fall",
"a9f1ad0c2f21eb84": "you saw a crash I did can some of that be averted",
"f436651bea21ff85": "he prayed for me my life will never be the same",
"01a595d2e474b70a": "for 2024 and there's things that I know that in the natural were impossible",
"a38669aa60eb29fa": "a major virus again in 2024 going into I mean I 2025 2026 2027",
"9207199c99720bc0": "much prayer that has went before me over the month of October",
"bfd82f8704dea2ba": "you saw a crash I did can some of that be averted",
"5391ac4f26ea3ce4": "he prayed for me my life will never be the same",
"36d3d62ae59760dc": "for 2024 and there's things that I know that in the natural were impossible",
"52b4d057ab6290c1": "a major virus again in 2024 going into I mean I 2025 2026 2027",
"3e594aed288e78f6": "the World Series I just had no idea if they were going to win",
"534d8434352a7b81": "of time it was it's suade it in the heavenlies",
"1be173d9bfbbeeb8": "will not take weeks to finish it that we'll know within a couple of days",
"c907c19a2a44689d": "in the past it was like March or so of last year",
"183e9af3411b35d0": "events boop boop boop boop boop and it's going to going to pick up speed",
"8148b5ff06e859ad": "hit her going beside Camila Harris going clear up into uh the January",
"b7c7ab80dc1eeab1": "be even running. It will not happen. And I told you this last year 2023",
"1524ca81fc3345e3": "coming but it is a wake up a wake up it's a shaken to awaken",
"86ec80add2279301": "in my spirit personally I've not seen anything on April the 8th",
"9d0f509bf0bcbd0e": "be a greater work. And I and you'll work I will work through you",
"207823ffdbafa972": "three judges that are very bad that will rise up to try to put roadblocks",
"4f0edf24e56f8899": "free will to to either vote for for Camila Harris or to vote for",
"08f81ea2cac7da38": "it was in April so it kind of goes with what I felt",
"b8b3042654d459c5": "may get a virus when they go to school but it's not going to last",
"186c8ecde93b93c3": "with my own eyes how is that possible Brandon I have no idea",
"a55c4ffc4f5d61c6": "in 2025 you will see faces that will it seem like they come out",
"b5ff7cbf75ef6454": "doesn't want any of you to perish and go to hell not one of you",
"16b54f545aaab4d0": "a great shaking in the body of Christ in 2025 2026 2027 2028",
"da62b5f2a696d48d": "this time next year in 2026, you won't even recognize where we are",
"6f312b84dc7f6b23": "see a lot of change in the blue states and the red states",
"c01d6919f303d13f": "a route coming up out of the from the sky going down into the Vatican",
"a2ec5792f745d08d": "circled the month of September and I told you it with a cloud on that",
"1e41c2447dd9bb94": "there was a white a rat in the White House. Did I not?",
"fb37ef21b4f62554": "an inner image of this. And that's what it happens every year with Megan",
"906c3d76c722abfe": "an inward image of that by 45. This is my 45th birthday on July 3rd",
"f40b155832b894c9": "seeing Israel. I see blue. I see the white. I see the star of David",
"c2a48205e4155cf8": "caged and it's going to be released now. We're seeing it being released 2025",
"ef74feff0091e0a5": "a calendar flash before my eyes and I went all the way through the fall",
"0c8f1e8e69a61deb": "of water has more energy in it than than than a a a nuclear reactor",
"d35b0b7b38a4fd12": "ever bet or gamble off of this of what I've telling you, I'll never speak",
"a89231c20a7c7766": "hear in April how the weather was going to be all through the summer",
"40ce020877b5ab0d": "in a vision that Canada is going to go the way that it did",
"137a4ce8b4574a65": "on the edge of the edge of the wall and say, God, what's coming now?",
"5f9ff36373ceb4a8": "if Camila Harris would have won, do you all say, does it really have to",
"cd6dc002fdef7975": "2025 is going to be a a a a dark year because of the dam",
"948913633be5cac0": "using Trump to get it done. And he may not even know he's being used",
"492443847fd6a40f": "ain't trying to cause hype. I'm just trying to tell you what we are praying",
"e1d29b99fd805ac8": "sheep and the goat nations would be presented in the days ahead concerning the UN",
"f9505276244fdbd5": "that would be drawn in the sand of who is for and who is against",
"f195ff47a71cca9e": "September is a hot month. I told you it was circled with a fog over",
"1f3ad0e35540dc61": "the Lord said 2026 is the year of a fix. I don't know what that",
"d26a62e52974d3c2": "coming like like the Lord told us it would in the month of September",
"758ab4043ea1c9eb": "this September he said you're at the point of no return",
"7e06de1aff0b85e9": "make it look like the economy is amazing so that everybody wants to vote red",
"1a184a21458d588b": "show you more that's coming and the decisions that need to be prayed over",
"cebc4be303feb9d0": "in September is a time to remember for it will be in a 24-hour period",
"d8702b934fbd9b97": "nothing compared to that is nothing to what I saw. It is across the world",
"943bfb780edbad67": "the end of the end, that the that that the children would start to intercede",
"75ad9fc936983b70": "blood moon that will be seen by 7 billion people on the 7th of September",
"1b401b708a23462e": "glory cloud came in there and it was so thick that people were getting healed",
"76a94fa818ddd3f2": "ride the wave. If you go back to the last video, ride the wave",
"937aa4f6856f39f3": "Friday. And it it's it's around November. is the Black Friday. It's in It's fake",
"f95d1da3ab47289b": "to be at its breaking point. And I see it and it's in the winter",
"e820141a8d6724c3": "clear into May of 2026 a shifting and and in and a a global realignment",
"c4a668effcbdf324": "the Lord said about midterms? 2026 will be the year of a fix",
"e30b769e585f549f": "in the late midnight hour on October 31st, we could get this flipped",
"9de0b3f99c5915cb": "that are in office that are that are set out just to destroy our country",
"7076ddda7521b80d": "into 2026 the first of 2026. The Father you're cleaning up the church",
"ebe3cd22b278af88": "learn that in these last days or you're not going to make it",
"2f8fcc506cfa514a": "25 states are if they don't pass the budget by by Saturday of next week",
"f3be24a875ff8ba5": "trying to stir up fear on me, Brandon? No. I ain't worried about it",
"9f0e41704db5c7a1": "the oil press. I saw the olives. I saw what's about to take place",
"1fe29589750d87f8": "house will be paid in full by the end of 2025 for supernatural debt cancellation",
"c655ac92549a58cb": "the end of 2025, the next 9 weeks, you're going to be completely debt free",
"91b81c02a9aa92cc": "sound of a mighty rushing wind. And there'll be a great sound of the rain",
"2203955a42cbead7": "don't talk to him yet. And he didn't know that the Lord had said that",
"e6bff78f5c3fd197": "Christmas. And it was like it was with a with a great escalation of war",
"7e7d667440f53c2d": "we hit the 23rd of of September that that was the point of no return",
"6bd79ff8af3deb2c": "a lot of protest and a lot of major uprising going on there right now",
"b056041e5f9b8504": "September. You're going to see major hurricanes and one will try to hit Miami",
"218cb892c17b3623": "a plan for mass mass shootings and mass chaos and these things about churches",
"41c7cf9a6320c502": "happen a lot in 2026. And he said, You will see this in 2026",
"41f997b10360efcf": "move of a red wave and it will be even more of a great revival",
}

def main():
    con = sqlite3.connect("prophecy.db")
    quotes = dict(con.execute("SELECT mention_id, quote FROM mention WHERE quote IS NOT NULL"))
    over = {i: q for i, q in quotes.items() if len(q.split()) > 15}

    unmapped = sorted(set(over) - set(FIX))
    if unmapped:
        sys.exit("over the cap with no trim on file: %s" % unmapped)

    errs, todo = [], []
    for mid, new in FIX.items():
        if quotes.get(mid) == new:
            continue                      # already applied, re-runnable
        if mid not in over:
            errs.append("STALE %s: not over the cap and not already trimmed" % mid)
            continue
        if new not in over[mid]:
            errs.append("NOT A SUBSTRING %s\n  old: %s\n  new: %s" % (mid, over[mid], new))
        elif len(new.split()) > 15:
            errs.append("STILL OVER CAP %s (%d words): %s" % (mid, len(new.split()), new))
        elif not new.strip():
            errs.append("EMPTY %s" % mid)
        else:
            todo.append((mid, new))
    if errs:
        sys.exit("\n".join(errs))

    for mid, new in todo:
        con.execute("UPDATE mention SET quote=? WHERE mention_id=?", (new, mid))
        con.execute("UPDATE mention_fts SET quote=? WHERE mention_id=?", (new, mid))
    con.commit()

    left = [(i, len(q.split()))
            for i, q in con.execute("SELECT mention_id, quote FROM mention WHERE quote IS NOT NULL")
            if len(q.split()) > 15]
    print("%d quotes trimmed this run, every one a verbatim substring of the original" % len(todo))
    print("still over cap:", left or "none")


if __name__ == "__main__":
    main()

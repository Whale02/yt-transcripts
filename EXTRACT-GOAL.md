Second run, opened 29 October 2026. The first run read every tier 1 and tier 2 passage up to
2 September 2026. Since then he has kept uploading, and claims have come due. This run has one
emphasis: **economics, politics and health, read in full detail.** He is a detailed speaker. He
names amounts, months, offices, diseases, the order things happen in, what he saw on a screen,
who was standing where. Every one of those details is a separate test, and a claim written as a
summary throws the tests away. Nobody needs to approve a batch. Do not ask questions. Do not
wait. Just keep going.

Check yourself with `python prophecy.py todo`. The numbers are:

    past-due claims with no evidence recorded         -> job A
    strong fulfilment assertions not yet linked       -> job B
    tier 1 and tier 2 coverage (new videos)           -> job 0
    focus  tier 3 econ/politics/health coverage       -> job D

Order: job 0 (new videos, tiers 1 and 2), then A, then B, then D. A is the point of the whole
database: a prediction nobody checked is worth nothing. Inside every job, economics, politics
and health go first.

## Job 0: the new videos

`python refresh.py` has already pulled everything published since 2 September. Read their tier 1
and tier 2 passages with `python prophecy.py pick --tier 1 --since 2026-09-01 --limit 12 --chars 1200`
(then `--tier 2`), and run the same loop as before: mentions, `load`, reviews, `review`, `cluster`,
`validate`. Run `python prophecy.py scan` after loading, so his new "it came to pass" statements
reach job B. Use `--chars 1200` or more. A 400-character excerpt cuts the detail off.

## Job D: economics, politics and health in tier 3

`python prophecy.py pick --focus economics,politics,health --limit 10 --chars 1500` lists the
tier 3 passages (a forward cue with no date, number or place) that touch the three subjects,
newest first, one per near-duplicate group. Read every one. When an excerpt stops mid-thought,
read the passage on either side with `python prophecy.py search` or straight from the transcript
under `corpus/` or `corpus-streams/`. A passage with no forward claim still gets a row with
`content_type` set to framing, context, teaching or prayer, the way the first run marked them,
so the counter moves and nobody reads it twice.

## The detail standard (all jobs, strictest on the three subjects)

One mention per distinct checkable detail. If he says the dollar falls, gas goes to eight
dollars, banks close for three days and it starts after a fall election, that is four mentions
sharing a passage, not one. For each of them:

- Economics: the instrument (dollar, gold, silver, oil, a named bank, a named stock, crypto,
  housing, groceries), the direction, any amount or percent, the trigger he names, the order of
  events, and whether he means America or another country. Write the amount into `magnitude`.
- Politics: the office and the person, the act (arrested, removed, wins, loses, dies, resigns,
  indicted, impeached), the margin or vote count if he gives one, the election or session it
  attaches to, and which party or faction. Record a name he hedges on as hedged.
- Health: the disease or agent by name, where it starts, how it spreads, the scale (deaths,
  countries, percent), any vaccine or treatment claim, any government response he describes, and
  whether he links it to a bioweapon or a lab. Health claims that could frighten people are still
  recorded neutrally. Paraphrase, do not amplify.

Fill `entities`, `locations`, `time_phrase`, `window_start`, `window_end`, `severity`, `causes`
and `consequences` whenever he supplies them. Leave them empty when he does not. Do not infer.
Undated claims still get falsifiers: write what would count as a hit and as a miss, and say in
`falsify_miss` that with no window the claim cannot expire, so a later match carries less weight.

When a telling adds detail to an earlier claim, the review's `delta_type` is `elaboration` and
the `note` names the new detail. When it changes a detail (a different amount, a different
month, a different person), the type is `contradiction` or `branch`, and both tellings stay.

## Job A: check what actually happened

1. `python prophecy.py validate` lists the state of every claim. Take the UNRESOLVED ones whose
   due date has passed, most-told first (`python prophecy.py thread <claim-id>` shows the tellings).
2. Search the web for what actually happened. Real sources, with URLs. Government and primary
   sources over aggregators; a news report over a blog.
3. Write `evidence-<topic>-<n>.json` and load it with
   `python prophecy.py evidence <file> --tool claude-opus-5+web`.
   Every row carries claim_id, observed_on, source_url, summary, state, rationale.
4. States: STRONG_MATCH, PARTIAL_MATCH, CONTRADICTED, EXPIRED_WITHOUT_MATCH, NOT_YET_DUE,
   UNFALSIFIABLE, UNRESOLVED.

Score honestly. Base rates decide the difference between a hit and a coincidence: the World
Series falls at the end of October every year, DHS warns before every Fourth of July, budget
fights cluster in late January. If the thing he named would have happened anyway, say so in the
rationale and hold the verdict at PARTIAL_MATCH. A vague claim that lands is not a strong match.
If a claim has no criterion that could have come out either way, record UNFALSIFIABLE and say
why, rather than leaving it unchecked.

If he pre-committed, note it. He sometimes says a word is off if it does not land. That is the
best evidence in the corpus and it should be in the rationale.

## Job B: link his fulfilment claims to the prophecies they claim to fulfil

`python prophecy.py fulfilled --strong --unreviewed` shows the ones with no claim attached, and
`python prophecy.py autolink --min-score 2` proposes matches. His assertion that a word landed is
never evidence that it did: it stays in fulfilment_assertion, and reality stays in
validation_evidence. Linking them is what makes the two comparable.

Job A in this run also covers claims that were scored before 2 September but whose window has
closed since, and any claim in the three subjects still held at NOT_YET_DUE with a date now past.
For economics, check the actual figure on the date (FRED, BLS, EIA, the Treasury, the exchange's
own close). For politics, check official returns and the government's own record. For health,
check the CDC, the WHO, or the national health ministry. Score each detail he gave, not only the
headline: a recession that came without the bank closures he described is a PARTIAL_MATCH, and
the rationale lists which details landed and which failed.

The 3 November 2026 midterms close red-wave-2026 and every claim tied to them. Score them from
certified or near-final returns once those exist, not on election night.

## The extraction loop (jobs 0 and D)

Write mentions to `mentions-<topic>-<n>.json`, `load`, write `reviews-<topic>-<n>.json`, `review`,
`cluster`, `validate`.

## Rules that matter everywhere

Quote at most fifteen words verbatim. Paraphrase claims in neutral wording.

Write `falsify_match` and `falsify_miss` before you know any outcome. `load` now refuses a
mention without one. If a claim cannot fail, say so in the falsifier instead of inventing a test.

Record only what he states. A clip he plays is not a claim he makes. Causes and consequences go
in only when he says them. If you infer a link, the relationship row is `asserted_by: system`.

Never merge a contradiction into a clean claim. Two tellings that disagree stay side by side as
`same_event: unsure` with `delta_type: contradiction` or `branch`.

Prayer conditionality is a field, not a reason to skip a claim, and not an excuse that converts a
non-event into a match.

Before folding two canonical claims into one, read both threads: `python prophecy.py merge` moves
the assignments and leaves the dead id resolving to the survivor. If the two tellings differ in
substance, record a `same_event_as` edge with `asserted_by: system` instead of merging.

Append two or three lines to PROGRESS.md each batch. Every tenth batch run `python selftest.py`
and `python export_view.py`.

## Stopping

Stop when `todo` shows no past-due claim without evidence, no unlinked strong fulfilment
assertion, tiers 1 and 2 at 100 percent, and the focus line at 100 percent. Or when a file named
STOP exists in this directory.
Nothing else stops you. If a batch fails, fix it and continue.

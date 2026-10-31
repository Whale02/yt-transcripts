# yt-transcripts

Batch YouTube transcript downloader. Free, no API key, no third-party site.
Uses yt-dlp (open source) to pull the caption track YouTube already has, then
converts it to readable text.

## Use

    cd ~/yt-transcripts

    # one or many videos
    python yt_transcripts.py "https://www.youtube.com/watch?v=ID" "https://youtu.be/ID2"

    # a whole playlist or channel
    python yt_transcripts.py "https://www.youtube.com/@ycombinator/videos" --limit 50

    # a list you keep in a file
    python yt_transcripts.py -f urls.txt -o transcripts/

Output is one `.txt` per video plus `manifest.tsv` (id, title, duration, url).

## Flags worth knowing

| Flag | Does |
|---|---|
| `--timestamps` | `[mm:ss] line` instead of paragraphs. Good for citing a moment. |
| `-l zh-Hans,zh` | Other languages. Default is English. `-l "en.*"` also pulls YouTube's auto-translations. |
| `--limit N` | First N videos of a playlist or channel. |
| `--keep-vtt` | Keep the raw subtitle files as well. |
| `--cookies-browser chrome` | For age-gated videos, or if YouTube throws a bot check. |
| `--sleep 2` | Slower pacing on big batches. Default 1s between requests. |

## Notes

- Re-running skips videos already fetched (`.archive.txt` in the output dir), so
  an interrupted batch resumes where it stopped.
- Manual captions are used when the uploader wrote them, auto-generated otherwise.
  Auto captions have no punctuation-perfect casing and no speaker labels.
- A video with captions disabled produces nothing. yt-dlp says so and the batch
  continues.
- Update the downloader when YouTube changes things: `pip install -U yt-dlp`.

---

# prophecy.py — longitudinal claim database

The transcript downloader above is stage one. `prophecy.py` is stage two: it turns
transcripts into a searchable claim graph where the primitive is the *event*, not
the video, and topic pages are views rather than folders.

    python prophecy.py init
    python prophecy.py ingest corpus/         # transcripts -> videos + segments (immutable)
    python prophecy.py dates                  # uttered_at anchor from YouTube upload dates
    python prophecy.py type                   # prayer / worship / promo / testimony / content
    python prophecy.py pack -o packs/         # extraction prompts for the segments worth reading
    python prophecy.py load mentions.json --tool <model>
    python prophecy.py seed seeds.json        # canonical claims, stable slugs
    python prophecy.py cluster                # lexical blocking, assigns nothing it cannot justify
    python prophecy.py review reviews.json    # adjudication: same_event + delta_type
    python prophecy.py relate relationships.json
    python prophecy.py validate               # mechanical state pass, consults no outcomes
    python prophecy.py scan                   # find "I told you this was coming" moments
    python prophecy.py fulfilled --strong     # what HE says already came true
    python prophecy.py search "new madrid"    # raw corpus, before any extraction
    python prophecy.py thread <claim_id>      # the whole history of one event
    python prophecy.py timeline --year 2028
    python prophecy.py graph
    python prophecy.py stats

## Invariants the schema enforces

- `video` and `segment` are immutable. Everything else is derived and can be rebuilt by
  re-running an extractor; nothing downstream is hand-edited.
- Every derived row carries a `run_id` naming the tool and prompt version, so two
  extractors can coexist and be compared.
- `assignment` is append-only. A changed judgment inserts a new row and marks the old one
  `superseded_by`; the earlier reading stays readable.
- "Is this the same event?" (`same_event`) and "what did this mention add?" (`delta_type`)
  are separate fields, because a contradiction is a same-event judgment plus a delta, and
  collapsing them makes both unusable.
- Three time axes: `uttered_at` (when he said it), `window_start`/`window_end` (when he says
  it happens, resolved against `uttered_at`), and `validation_evidence.observed_on` (when
  something actually happened). They live in different tables and never write to each other.
- `falsify_match` and `falsify_miss` are written at extraction time, before any outcome is
  known. That is what stops hindsight from leaking in later.
- `relationship.asserted_by` is `brandon` or `system`. An edge claiming he asserted it is
  refused at load time unless it names the mention where he says so.
- Prayer and worship segments are typed out of the corpus but never deleted: `has_payload`
  marks the ones that still carry a claim, and those go into the extraction pack.
- Recall beats cost in the typing pass. Commentary carrying a forward modal ("a scandal
  would try to keep him at bay") is flagged `has_payload` and extracted anyway: a missed
  claim is invisible forever, an extra segment only costs tokens.
- A fulfilment claim is his speech, not evidence. `scan` finds the moments he says an
  earlier word landed and tiers them (a "came to pass" asserts something, an "I told you"
  is usually a discourse marker); `fulfilled` lists them beside our own validation state,
  never merged into it.
- `search` runs on the raw corpus, so you can answer "everything he has said about X"
  before any extraction has happened, and see which of those passages are still unextracted.

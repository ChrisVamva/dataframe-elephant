# Article Techniques Protocol

## Status
Advisory companion to `ArticleCreation.md` (mandatory). That protocol governs *what the evidence allows*; this one governs *how the prose carries it*. Read-only against `notebooks/`; article outputs are derivative, not controlling.

---

## 1. Purpose
Evidence-first articles fail the same way feature stories fail: buried point, flat opening, caveats dumped at the end where nobody reads them. This protocol adapts standard feature-writing craft (lede, nut graf, body architecture, kicker) to the corpus's constraint — every material statement must stay traceable to `data/smarthome.duckdb` with its evidence class, confidence, falsifier status and linkage rule intact.
## 2. The structured process (7 steps)

### Step 1 — State the story in one sentence
Write "This is a story about …" repeatedly until it names an action with movement, not a topic. ("This is a story about a switch that forgets its light sixty seconds after the router dies" beats "This is a story about resilience".) If the sentence cannot carry a claim id, the article has no mandate yet — return to `ArticleCreation.md` Step 1.

### Step 2 — Open with a lede that earns the next paragraph
Pick one lede type and commit. Length guide: 1–4 short paragraphs; the reader must hit the nut graf within ~150 words.

| Lede type | How it works | Use it when | Avoid it when |
|---|---|---|---|
| Anecdotal / scene | A concrete moment (the switch, the minute, the dark hallway) that embodies one claim | the cluster has a vivid consequence (`C020`'s one minute) | no claim supports the scene — never invent one |
| Startling figure | One verified number, stated with its unit and scope (`M006`: about 1 minute) | exactly one number carries the story | the number needs three caveats before it parses — use a descriptive lede instead |
| Descriptive | A precise picture of the failure state or map (three outage columns, one cell deep) | the visual is the hook | the description substitutes for the figure — describe, then show |
| Stakes-first | Who pays if the claim holds (the buyer of an orphaned hub) | lifecycle/policy pieces (`C070`, `C076`) | the stakes outrun the evidence class |

Never open with: direct address ("you walk down the street…"), an epigraph/quote, or a question the reader cannot answer. All three spend the reader's attention without giving information.

### Step 3 — Land the nut graf (transition + summary lede)
The nut graf answers *why this story, why now, why should I care* — formula: transition from the lede, then a one-sentence summary that answers a big-picture question (why / how / so what). Required contents: the claim cluster in plain words, the scale (cluster size vs corpus size — never confuse the two), and the article's promise (what the reader will be able to decide after reading). Placement: immediately after the lede block. Test: delete the lede — the nut graf alone must still state the story.

### Step 4 — Build the body as sections, not a funnel
One section per failure class / claim group / figure — each section opens with its own mini-nut (one line saying what this section proves) and closes before the next begins. Alternation rule: scene → data → implication, then repeat; never stack three data blocks without a human consequence between them. Each section carries its evidence inline (claim ids in the sentence, metric values with units and scope, linkage rule where a metric meets a claim) rather than in an endnotes ghetto.

### Step 5 — Weave uncertainty into the sentence, not the appendix
Caveats that change the meaning travel *with* the number: "about one minute, measured on a Matter-over-Thread switch-and-light pair when the SRP Server is unavailable (`M006`, reported signal, medium confidence)" — not "one minute*" with the truth 800 words later. Fixed vocabulary: "recorded" (in the DB), "not recorded" (absent from the corpus — never "zero", never "does not exist"), "reported signal" vs "documented fact" (kept verbatim), confidence stated where it qualifies the reading. Conflicting values sit side by side with the reason they differ; falsifier-absent claims are flagged at first mention.

### Step 6 — Close with a kicker, not a summary
The ending returns to the opening image with changed understanding (the switch, now with a second router on the shopping list), delivers the corpus's recommendation (`C076`-style ask), or states the decision the reader can now make. Never: restate the lede, end on a bare quote, or introduce a new claim in the final paragraph. The last line must be writable *before* drafting the body — if it isn't, the nut graf is weak.

### Step 7 — Self-review against the gates
Run the Article Creation Protocol §7 gates (AC:Scope … AC:Maintenance) plus this file's checklist (§4): every section traceable, every number unit-labelled, every caveat inline, no invented scenes, no upgraded evidence, kicker pre-written. A reviewer who was not the drafter answers the five §7 questions; any "I can't tell" answer returns the draft.
## 3. Structural shapes (pick one per article)

- **Three-act / hourglass**: wide (human scene) → narrow (the evidence, one cluster) → wide (what it means for the reader). Default for consumer pieces ("Three ways your smart home dies").
- **Martini glass**: inverted-pyramid summary up front (the finding in 3 sentences), then the narrative stem. Use when the finding is actionable and the reader may stop early.
- **Number-led**: one verified figure as spine (`M006`'s minute, the 82% baseline), each section testing it from a new side. Use when exactly one number carries the story; retire the shape the moment a second number competes.
- **Audit / trust piece**: gap counts as the plot (`24_corpus_gap_audit`). Open with the largest honest number, tour each gap class, close with the study the corpus proposes.

## 4. Pre-publication checklist

1. Lede ≤ 4 paragraphs; nut graf within ~150 words; nut states cluster, scale, promise.
2. Every section opens with a mini-nut; no three data blocks in a row without a human consequence.
3. Every metric value carries value + unit + scope + class/confidence at first mention.
4. "Not recorded" used for absences — the words "zero", "never", "no devices" appear nowhere unless a claim states them.
5. Reported signal never upgraded; inferences labelled; recommendations labelled as synthesis.
6. Conflicts shown side by side with the reason, not reconciled.
7. Falsifier status stated for every material claim; `L030`-flagged claims named.
8. Linkage rule (section-first vs source-id-second) recorded for every claim→metric join.
9. Kicker returns to the opening image or delivers the decision — no summary ending, no new claims.
10. Figures referenced by notebook file + cell; interactive noted; headless reproduction path stated.

## 5. Sources

- Structure/lede/nut-graf craft: Nieman Storyboard, "Nut grafs: seven steps to score a winning story structure" (Shontz/Heyamoto: nut graf = transition + summary lede; "this is a story about…" drill); Journalism University, "Step-by-step guide to writing a compelling feature article" (hook → nut graf → body → bookend ending); LibreTexts OER Guide to Media Writing §6.2 (feature structures; show-don't-tell; the living end) and Kraft, *Writing Fabulous Features* §3.4 (lede types; ledes to avoid: direct address, quote, question).
- Science-nut-graf practice: The Open Notebook, "Nailing the nut graf" (mini-outline vs data-first variants; back the counter-intuitive claim with data early).
- Uncertainty communication: Full Fact, "Communicating uncertainty" (plain-language confidence, ranges, caveats carried with the number).
- Governing (this repo): `ArticleCreation.md` §§4–7 (source precedence, procedure, gates); `schemas/stage2.sql` (no claim→metric foreign key); `src/viz_core.py` (provenance path).

# Best 5 — rating of `ArticleIdeas2.md`

## Document Control

- Status: draft
- Rates: `Artifacts/Article Ideas/2/ArticleIdeas2.md` (snapshot 2026-09-30, 27 ideas: 2.1–2.3, 3.1–3.3, 6.1–6.3, 12.1–12.3, 16.1–16.3, 19.1–19.3, 22.1–22.3, 24.1–24.3, X.1–X.3)
- Rating date: 2026-09-30
- Derivative of: `notebooks/2/*.ipynb` + `data/smarthome.duckdb` (read-only); controlling sources as in ArticleIdeas2
- Intended reader / use: commissioner deciding which 5 articles to green-light first
- Update triggers: any new `C###`/`M###` in the DB; any `notebooks/2` revision; any ArticleIdeas2 revision (re-rate)

## Rating method

Five criteria, 1–5 each, total /25. Scored from the idea entry plus its source notebook spec — no new evidence introduced.

| Criterion | 5 means | 1 means |
|---|---|---|
| Hook (H) | broad reader appeal, memorable takeaway | niche/methods-only interest |
| Evidence (E) | dense verified ids + a ready figure | thin or prose-only backing |
| Novelty (N) | says something wave 1 and the obvious take do not | repeats wave 1 or commonplace |
| Feasibility (F) | writable from the corpus as-is | needs primary research first |
| Integrity (I) | turns limits into the story, hard to overclaim | easy to misread or oversell |

Tie-breaks, in order: broader audience > synthesis value across notebooks > commissioning readiness (figure already exists).

## Full ratings (all 27, sorted by total)

| Idea | H | E | N | F | I | Total |
|---|---|---|---|---|---|---|
| 2.1 Matter logo = conformance, not compatibility | 5 | 5 | 5 | 5 | 5 | 25 |
| 3.1 Three ways your smart home dies | 5 | 4 | 5 | 5 | 5 | 24 |
| 6.1 The 82% do-nothing baseline | 5 | 5 | 5 | 5 | 4 | 24 |
| 22.2 Money on three clocks | 5 | 5 | 4 | 5 | 5 | 24 |
| X.1 Certified vs working (cross-cutting flagship) | 5 | 5 | 5 | 4 | 5 | 24 |
| 24.1 What the corpus admits it doesn't know | 4 | 5 | 5 | 5 | 5 | 24 |
| 12.1 The model, then the field | 4 | 5 | 4 | 4 | 5 | 22 |
| 19.1 Three prices on a log scale | 4 | 4 | 4 | 4 | 5 | 21 |
| 22.1 Four denominators, no single barrier index | 4 | 4 | 4 | 4 | 5 | 21 |
| 2.2 Claim map with the seams showing | 3 | 4 | 4 | 4 | 5 | 20 |
| X.3 Gap-aware methods guide | 3 | 4 | 4 | 4 | 5 | 20 |
| 6.3 Evidence labels explainer | 3 | 3 | 4 | 4 | 5 | 19 |
| 22.3 The 47-euro policy | 3 | 3 | 4 | 4 | 5 | 19 |
| X.2 Money on different clocks (flex vs household) | 4 | 4 | 4 | 3 | 4 | 19 |
| 12.2 Carbon arithmetic | 3 | 4 | 3 | 4 | 4 | 18 |
| 16.1 Scorecard calibration | 3 | 4 | 3 | 4 | 4 | 18 |
| 6.2 What benchmarks don't test | 3 | 4 | 3 | 4 | 4 | 18 |
| 3.2 The one-minute number | 2 | 3 | 3 | 4 | 5 | 17 |
| 3.3 Shutdown playbook op-ed | 4 | 3 | 4 | 3 | 3 | 17 |
| 12.3 Two results, no league table | 2 | 3 | 3 | 4 | 5 | 17 |
| 24.2 Decisions behind the gaps | 2 | 4 | 3 | 4 | 4 | 17 |
| 24.3 The W10 study proposal | 3 | 3 | 4 | 3 | 4 | 17 |
| 2.3 One lab, one count | 2 | 3 | 3 | 4 | 4 | 16 |
| 16.2 Policy says patch | 3 | 3 | 3 | 3 | 3 | 15 |
| 19.2 Who makes your AI hub | 3 | 3 | 3 | 3 | 3 | 15 |
| 16.3 Scorecard's missing rows | 2 | 2 | 2 | 3 | 4 | 13 |
| 19.3 Rest is blank (research brief) | 2 | 2 | 2 | 2 | 3 | 11 |
## Why these 5 win — the reasoning before the list

- **Six ideas tied at 24; one had to go.** The cut is the only judgment call here: 24.1 ("What the corpus admits it doesn't know") is excellent trust-building material, but it is infrastructure, not an article readers choose — its highest value is being linked from the other five, not commissioned ahead of them.
- **No two winners share a notebook.** The five winners span Matter interop (02), resilience (03), AI safety (06), household economics (22), and cross-cutting synthesis (X.1) — maximal catalogue coverage, zero evidence overlap.
- **Each winner has a ready figure.** 2.1, 6.1, 22.2 and X.1 reuse built, verified visuals; 3.1 reuses the failure-state matrix. Nothing in the top 5 waits on primary research.

## The Best 5 (commissioning order)

### #1 — 2.1 "The Matter logo is a conformance claim, not a compatibility promise" (25/25)
- Scores: H5 E5 N5 F5 I5. The only perfect score — and the only idea whose hook is its integrity lesson.
- Why it wins: `C015` (certification does not guarantee compatibility) next to `C097` (first-pairing success, then failure to operate) gives buyers a sentence they will repeat — while the evidence (`C008`/`C011` documented facts vs 10 reported-signal claims, `M086`/`M087` test inventory) forces the honest version. Broadest audience, densest evidence, most novel distinction, writable today; the `C017` falsifier caveat is part of the plot, not a footnote.
- Source: notebook `02`; claims `C015`, `C097`, `C008`, `C011`; metrics `M086`, `M087`.
- Commission with: 2.2 as reference companion; X.1 as the later long-form payoff.

### #2 — 3.1 "Three ways your smart home dies" (24/25)
- Scores: H5 E4 N5 F5 I5. Docked one point on Evidence (prose-heavy cluster) — and that honesty is the idea's strength.
- Why it is top-5: the corpus's own three-class failure taxonomy (border router / WAN link / vendor shutdown) is the most narratable structure in wave 2, ends in a concrete ask (`C076`: classified failure disclosure), and no wave-1 notebook covers resilience. Consumer flagship with a natural three-panel illustration commission.
- Source: notebook `03`; claims `C019`–`C022`, `C026`, `C027`, `C070`, `C076`; metric `M006` ("about 1" minute) as the lone quantity.
- Commission with: 3.2 as methods sidebar; 3.3 only after vendor right-of-reply is secured.
### #3 — 6.1 "The 82% do-nothing baseline" (24/25)
- Scores: H5 E5 N5 F5 I4. Docked one point on Integrity — the benchmark chart is the easiest figure in the catalogue to over-read, so the article must keep conditions and blind spots on screen.
- Why it is top-5: a single reframing number (82%) over dense reported results (`M071`–`M085`); the strongest chart in wave 2; an AI-safety hook no wave-1 notebook touches. The I4 is manageable because notebook `06`'s uncertainty panel already lists what the benchmarks miss — the article's job is to keep that panel attached.
- Source: notebook `06`; claims `C031`–`C033`, `C037`–`C042`; metrics `M071`–`M085`.
- Commission with: 6.2 (what benchmarks don't test) as the paired technical piece.

### #4 — 22.2 "Money on three clocks" (24/25)
- Scores: H5 E5 N4 F5 I5. Docked one point on Novelty — ownership-cost explainers exist — but none keeps the three clocks separate, which is this corpus's contribution.
- Why it is top-5: personal-finance reach (broadest non-technical audience after 2.1/3.1), fully recorded figures (`M036` 3,750 USD once / `M037` 70 USD monthly / `M035` 340 USD frustration + `M019`–`M024` setup family), and never summing across clocks turns a methods constraint into the visual concept. The six-metric unstated-conditions list is printed in full, hence Integrity 5.
- Source: notebook `22`; claims `C082`, `C087`, `C088`, `C114`; metrics `M035`–`M037`, `M019`–`M024`.
- Commission with: 22.1 as barriers companion; X.2 as the later economics feature — not first.

### #5 — X.1 "Certified vs working" (24/25)
- Scores: H5 E5 N5 F4 I5. Docked one point on Feasibility — synthesis across three notebooks (`02` + `16` + `03`) must not invent joining counts.
- Why it beats 24.1 for the last slot: it is the wave-2 thesis — certificate (`C015`, `C097`, `M086`/`M087`) to scorecard (`M063`–`M070`) to daily failure (`C076`) — following one device from lab to living room. It converts three strong notebooks into one long-form flagship; 24.1's role is better served as the linked trust appendix to all five winners.
- Source: notebooks `02` + `16` + `03`; claims `C015`, `C097`, `C008`, `C011`, `C076`; metrics `M086`/`M087`, `M063`–`M070`.
- Commission with: 24.1 linked as "how we show our work"; X.3 as methods reference alongside, never alone first.

## What was cut, and why it still matters

- **24.1 (24/25) — first reserve.** Same total as #2–#5; cut only because readers don't choose gap audits — editors link them. Attach as trust appendix to every winner.
- **12.1 (22/25) — second reserve, energy flagship.** Best energy idea (compliers vs all-participants `M089`/`M090` + `M127` chain); loses on audience breadth, not quality. Green-light it sixth.
- **19.1 (21/25) — best trade piece.** The honest log-scale price chart (Anker "not recorded") deserves commissioning once flagships are underway.
- **Deliberately not top-5:** methods-only pieces (2.3, 3.2, 12.3, X.3 — sidebars, not leads), single-pilot cautions (22.3), briefs needing fieldwork (19.3, 24.3, 16.3), op-eds needing right-of-reply (3.3).

## Reproducibility

- All ids re-verified against `data/smarthome.duckdb` at rating time (55 C-ids + 38 M-ids in ArticleIdeas2, zero missing). Before commissioning, re-run `scripts/build_visualization_notebooks.py --check` and `src/tests/test_viz_notebooks.py` — any id that stops verifying returns its idea to draft.

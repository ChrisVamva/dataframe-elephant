# Article Ideas 2 — from `notebooks/2/` (wave 2)

## Document Control

- Status: draft
- Claim clusters: wave-2 catalogue only — notebooks `02`, `03`, `06`, `12`, `16`, `19`, `22`, `24` in `notebooks/2/`
- Snapshot / review date: 2026-09-30 (matches `data/smarthome.duckdb` read by the notebooks)
- Derivative of: `notebooks/2/*.ipynb` (read-only visualisations), `data/smarthome.duckdb` (read-only, via `src/viz_core.py`)
- Controlling sources: `schemas/stage2.sql`; `research/raw/Stage 2/` extraction logs and decisions (`L014`/`L030`/`L031` family); source documents behind the claim `source_ref`s
- Intended reader / use: article commissioners and drafters choosing the next articles to write from wave-2 evidence
- Maintainer / reviewer role: corpus editor — verify every claim/metric id below still exists in the DB before commissioning (`scripts/build_visualization_notebooks.py --check`, `src/tests/test_viz_notebooks.py`)
- Update triggers: DB stage update; new claim/metric; falsifier resolved; any `notebooks/2` revision
- Evidence discipline (per `Rules and Regulations/Protocols/ArticleCreation.md`): reuse only numbers the DB contains; unrecorded quantities are "not recorded", never zero; reported signal is never upgraded to documented fact; rates with different denominators are never averaged into one index; conflicting values are shown side by side.

> How to read each idea: **Angle** is the editorial hook. **Evidence** lists the exact claim/metric ids and the notebook figure to reuse. **Preserve** lists the uncertainty that must survive into the article. An idea is only committable if its Evidence ids verify against the DB.

## Index — notebooks to ideas

| Notebook (`notebooks/2/`) | Title | Ideas |
|---|---|---|
| `02_ecosystem_support_and_commissioning.ipynb` | Matter by ecosystem: who supports what, and how far the test evidence reaches | 2.1–2.3 |
| `03_offline_failure_and_cloud_dependency.ipynb` | Resilience: what breaks when the border router, the internet or the vendor goes away | 3.1–3.3 |
| `06_home_ai_safety_benchmarks.ipynb` | Home-AI safety benchmarks: what the reported numbers measure, and what they miss | 6.1–6.3 |
| `12_flexibility_model_and_field_economics.ipynb` | Energy flexibility: the model's baseline, its emissions, and the two programme results | 12.1–12.3 |
| `16_lifecycle_practice_gaps.ipynb` | Lifecycle security: the scorecard's calibration, and the gap between policy and practice | 16.1–16.3 |
| `19_ai_hub_landscape.ipynb` | AI hubs and local compute: price, capacity and the adoption the corpus records | 19.1–19.3 |
| `22_household_economics_and_barriers.ipynb` | Why households stall: recorded barriers, setup friction, and what ownership costs | 22.1–22.3 |
| `24_corpus_gap_audit.ipynb` | Corpus gap audit: missing falsifiers, unstated conditions, and the questions left open | 24.1–24.3 |
| cross-cutting | — | X.1–X.3 |

---

## 2 — Ecosystem support and commissioning (`02`; C007–C018 + C097; M004, M005, M086, M087)

### 2.1 "The Matter logo is a conformance claim, not a compatibility promise"
- Angle: the most quotable sentence in wave 2 is an inference — `C015`: certification confirms conformance but does not guarantee ecosystem compatibility — next to `C097`'s first-pairing success followed by failure to operate. The article writes the buyer's version of that distinction.
- Evidence: `C015` (inference), `C097` (reported signal, Allion Labs functional test), `C008`/`C011` (the only two documented facts in the cluster, about specification content), heatmap cells for Matter cameras and multi-admin, `M086` (Allion test inventory scale), `M087` (corpus protocol minimum inventory).
- Preserve: 10 of 13 cluster claims are reported signal from third-party testing; `C017` has no falsifier, so the HomePod Mini "robust multi-admin" sentence cannot be disconfirmed from the corpus; blank heatmap cells mean "no claim in this cluster", not "absent".
- Reader/use: consumer explainer; pairs with a commissioning checklist.

### 2.2 "Who supports what: a claim map with the seams showing"
- Angle: the corpus contains no per-ecosystem capability table, so notebook `02` builds one out of prose claims — each coloured cell carries its claim id (`C010` for Apple/Google camera lag; `C014` for the Amazon/Apple/Google automation-rules gap vs Samsung). The article publishes that map *as a map of claims*, with the shallowness visible.
- Evidence: `C008`, `C009`, `C010` (cameras); `C014` (automation rules); `C016` (qualified) / `C017` (present) / `C097` (qualified) for multi-admin; `C013` + `M004` (Samsung's 58 device types — the only per-ecosystem count in the corpus).
- Preserve: `C010` and `C014` are each one sentence mapped to several cells — the same id repeats on purpose; no Apple/Google/Amazon device-type count exists, so a four-row parity bar would be invented; `C007`, `C011`, `C012`, `C015`, `C018` are deliberately left out of the matrix (ecosystem-agnostic or failure-mode claims).
- Reader/use: reference article for ecosystem comparisons; must link the notebook cell so readers can hover each claim.
### 2.3 "One lab, one count, and three unrecorded bars"
- Angle: methods-behind-the-headlines — everything the matrix asserts about breadth rests on `M004` (one counted bar) and the Allion inventory (`M086`) against the protocol minimum (`M087`).
- Evidence: breadth chart in notebook `02` (exactly one counted bar, three "not recorded"); `C013` ("may support fewer"); `M005` context.
- Preserve: do not present Samsung's 58 as a league-table win — the corpus records no denominator for the others.
- Reader/use: trade/methods audience; companion to X.3.

## 3 — Offline failure and cloud dependency (`03`; C019–C022, C026, C027, C070; M006, M007, M088)

### 3.1 "Three ways your smart home dies"
- Angle: the corpus's own taxonomy — local infrastructure failure (Thread border router), network failure (WAN link), lifecycle failure (vendor retires a cloud service) — applied claim by claim, following recommendation `C076` that manufacturers publish failures in exactly this classified way.
- Evidence: failure-state x capability heatmap (one claim per cell) in notebook `03`; `C019`–`C022`, `C026`, `C027`, `C070`; `C076` as the kicker.
- Preserve: almost all of this cluster is prose — the only quantified control-loss figure is `M006` ("about 1" minute); unrecorded cells stay blank; the map is a reading of claims, not a test report.
- Reader/use: flagship consumer resilience explainer.

### 3.2 "The one-minute number and everything around it that isn't a number"
- Angle: evidence-honesty short — what `M006` actually says, why `M007`/`M088` are not comparable companions, and why the rest of the resilience story is told in prose panels rather than charts.
- Evidence: notebook `03` context section; provenance panels as substance, not appendix.
- Preserve: state the linkage rule for every metric (section-first vs source-id-second); do not convert prose into pseudo-quantities.
- Reader/use: methods sidebar inside 3.1 or standalone.

### 3.3 "The shutdown playbook vendors should publish"
- Angle: turns `C076` (recommendation) plus the lifecycle-failure claims into a concrete ask: classified failure disclosure per product.
- Evidence: `C026`, `C027`, `C070` (vendor/cloud-dependency claims); `C075`–`C078` recommendation cluster from notebook `24` as reinforcement.
- Preserve: `C075`–`C078` are recommendations — for some, no falsifier is the right instrument; label the article's own proposals as synthesis per the Protocol.
- Reader/use: policy op-ed; invite vendor response.

## 6 — Home-AI safety benchmarks (`06`; C031–C033, C037–C042, C106–C108, C119; M071–M085)

### 6.1 "The 82% do-nothing baseline"
- Angle: the number that reframes every benchmark chart — reported results plotted with the 82% do-nothing line drawn across them.
- Evidence: notebook `06` results chart; test-design counts; claims `C031`–`C033`, `C037`–`C042`.
- Preserve: benchmark conditions the corpus never stated stay unstated; lab-reported signal is not upgraded to documented fact; blind spots stay on screen.
- Reader/use: AI-safety general audience; strongest single chart in wave 2.

### 6.2 "What the safety benchmarks don't test"
- Angle: gap-led companion to 6.1 — conditions, scenarios and failure modes absent from the reported numbers (`C106`–`C108`, `C119`).
- Evidence: notebook `06` safety-ratio tables and test-design counts.
- Preserve: non-comparable values shown side by side, not reconciled; falsifier-absent claims flagged explicitly.
- Reader/use: technical audience; researcher interview hook.

### 6.3 "Reported numbers vs measured facts: reading the evidence labels"
- Angle: uses this cluster to teach the corpus's evidence discipline — documented fact vs reported signal vs inference — because benchmarks tempt readers to treat every bar as measured.
- Evidence: provenance panels of notebook `06`; extraction-decision refs (`L014` vendor/forecast downgrade, `L031`, `L030` falsifier-absent) where they touch the cluster.
- Preserve: downgraded evidence stays downgraded; qualifiers, versions, units preserved verbatim.
- Reader/use: explainer/methods crossover; reusable template for other clusters.
## 12 — Flexibility model and field economics (`12`; C051–C053, C056, C059, C060, C090, C117, C118; M089–M093, M107–M114, M125–M130, M153)

### 12.1 "The model, then the field: compliers vs everyone"
- Angle: modelled baseline composition bars and emission factors first, then the two programme results with the complier/all-participant split (`M089` vs `M090` peak reduction) kept visible — the honest version of "did it work".
- Evidence: notebook `12` baseline chart; `M127` emission factors; `M089`–`M093` programme results; `C051`–`C053`, `C056`, `C059`, `C060`.
- Preserve: modelled vs observed never mixed on one bar; `C090` (corpus caution) quoted, not buried; `M153` boundary noted.
- Reader/use: energy-audience flagship; wave-1 device-flexibility notebook (`09`) is the prequel — link it, don't repeat its radar.

### 12.2 "The carbon arithmetic behind the flexibility claim"
- Angle: follows the emission-factor chain (`M125`–`M130`, `M107`–`M114`) step by step so a reader can check the flexibility-to-carbon conversion rather than take it on trust.
- Evidence: notebook `12` emissions panel; `C117`, `C118`.
- Preserve: conditions on each factor shown; unstated conditions flagged where the `unstated_conditions` view fires.
- Reader/use: technical explainer; worksheet-style reproduction block.

### 12.3 "Two programme results, no league table"
- Angle: short discipline piece — why the two field results cannot be ranked against each other (different denominators, different conditions) and what can be said instead.
- Evidence: notebook `12` results bars with per-bar denominators from each metric's `unit` cell.
- Preserve: rates with different denominators never multiplied into a funnel (wave-2 selection rule).
- Reader/use: sidebar to 12.1 or standalone methods note.

## 16 — Lifecycle practice gaps (`16`; C062, C063, C071–C074, C102, C104; M063–M070)

### 16.1 "Pass mark 2.00, ceiling 3.00: how to read the scorecard"
- Angle: calibration explainer for the composite scorecard (max 3.00, pass 2.00) — what a pass means, what it doesn't, and where the corpus's own caution sits.
- Evidence: notebook `16` calibration chart; `M063`–`M070`; `C062`, `C063`.
- Preserve: the scorecard is an instrument, not a verdict on any named product; confidence colours per the corpus legend.
- Reader/use: security/lifecycle entry point; wave-1 support-period notebook (`15`) is the companion — link, don't re-chart its bars.

### 16.2 "Policy says patch; practice says…"
- Angle: the gap between lifecycle policy claims and recorded practice, using the computed W9-claims-by-section bar (claims counted from the schema, stage names from `workflow_stage`).
- Evidence: notebook `16` section-count chart; `C071`–`C074`, `C102`, `C104`.
- Preserve: the count measures where the corpus spent effort, not product quality; recommendations among the cluster labelled as such.
- Reader/use: policy audience; practitioner interview hook.

### 16.3 "The scorecard's missing rows"
- Angle: gap-led piece — which lifecycle questions the corpus raises but cannot score, and what evidence would fill each row.
- Evidence: notebook `16` uncertainty panel; cross-ref notebook `24` gap counts.
- Preserve: missing falsifiers and unstated conditions listed in full, not only where convenient.
- Reader/use: research-agenda feeder into `research/processed/FollowUps/`.
## 19 — AI hub landscape (`19`; C081, C083, C084, C095, C096; M008–M018)

### 19.1 "Three prices on a log scale (and the one that isn't there)"
- Angle: price chart with exactly three recorded prices and Anker explicitly marked "not recorded" — the honest version of a market overview, capacity story alongside.
- Evidence: notebook `19` log-scale price chart; `M008`–`M018` price/capacity/adoption rows; `C081`, `C083`, `C084`.
- Preserve: Anker stays "not recorded", never zero, never interpolated; `M017` carries the extraction log's "conditions not stated in source" placeholder.
- Reader/use: buying-guide-adjacent feature with methods credibility.

### 19.2 "Who actually makes your AI hub"
- Angle: private-label share bars (`C095`, `C096` and linked metrics) — the supply-chain story behind the shelf.
- Evidence: notebook `19` share bars with per-bar denominators.
- Preserve: shares from different populations are not averaged into one index.
- Reader/use: business/trade audience.

### 19.3 "Local compute, recorded capacity, recorded adoption — and the rest is blank"
- Angle: what the corpus can and cannot say about on-device AI capacity and uptake; the blank cells as a commissioning brief for primary research.
- Evidence: notebook `19` capacity/adoption panels; `C095`, `C096` provenance.
- Preserve: every unrecorded cell named; no market sizing beyond figures that belong to other notebooks' clocks.
- Reader/use: research brief; feeds the W10 study-design proposal (notebook `24`, `M145`–`M152`).

## 22 — Household economics and barriers (`22`; C082, C087, C088, C113, C114; M017, M019–M030, M034–M038, M047, M049–M052, M104)

### 22.1 "Why households stall: four denominators, no single barrier index"
- Angle: barrier ranking that keeps each bar's own denominator on the hover — share of adopters, share of non-adopters, Spanish respondents, French respondents — because the corpus states its business-analysis caution explicitly in `C088`.
- Evidence: notebook `22` barrier chart; `C082`, `C087`, `C088` (documented-fact caution); linked `M025`–`M030` family.
- Preserve: `C088` warns against the conclusion the page invites — quote it; never average the four bars.
- Reader/use: consumer/market flagship; wave-1 churn funnel (`21`) is the sequel — link, don't rebuild it.

### 22.2 "3,750 once, 70 a month, 340 of frustration: money on three clocks"
- Angle: ownership cost told on its original clocks — `M036` one-off upfront (3,750 USD), `M037` monthly (70 USD/month), `M035` annual frustration (340 USD) — drawn labelled, never summed; setup rows (`M019`–`M024`: rates, usability-issue counts, NPS, repair cost) as a separate unit family.
- Evidence: notebook `22` money panels; `C114` context.
- Preserve: `M035` (likewise `M017`, `M034`, `M038`, `M049`, `M104`) carries "conditions not stated in source" — the full six-metric list is printed, not just the convenient rows.
- Reader/use: personal-finance angle; strong standalone visual.

### 22.3 "The 47-euro policy that isn't a market price"
- Angle: single-pilot cautionary tale — `C113`'s insurer paying 47 EUR per policy comes from one Samsung/HSB pilot, reported signal at low confidence.
- Evidence: `C113` provenance panel; `M047` if linked by the stated linkage rule (record which rule fired).
- Preserve: pilot is not a market; low confidence and reported-signal class kept on screen.
- Reader/use: short myth-busting column; reusable "one pilot" template.
## 24 — Corpus gap audit (`24`; C075–C078, C088–C091; M145–M152)

### 24.1 "What the corpus admits it doesn't know"
- Angle: the four documented-fact cautions `C088`–`C091` plus the gap counts straight from the schema views (`missing_falsifiers`, `unstated_conditions`, `unstated_boundaries`, `stage2_warning`) — every bar a `COUNT(1)`, nothing estimated.
- Evidence: notebook `24` gap-count chart; claims-per-workflow-stage chart (`W3`–`W12`, stage names from `workflow_stage`).
- Preserve: counts measure flags, not quality — `C001`–`C005`-style documented facts and `C075`–`C078` recommendations legitimately carry no falsifier; `stage2_warning` is empty in this DB while `extraction_decision` holds 56 rows across 11 types — say both.
- Reader/use: trust-building flagship ("how we show our work"); required reading before commissioning any other article.

### 24.2 "The decisions behind the gaps: 56 rows, 11 types"
- Angle: extraction-decision profile and the `open_questions` union (open_question + omission rows, mostly ingestion omissions rather than research questions) — the audit trail as a story.
- Evidence: notebook `24` decision-profile panel; `ExtractionLog.md` decision ids (`L014`/`L030`/`L031` family).
- Preserve: the union is not a backlog — do not present omission rows as a research queue.
- Reader/use: methods audience; reviewer-handbook chapter.

### 24.3 "The study the corpus proposes: W10, M145–M152"
- Angle: the mixed-method study design behind stage `W10` as a proposal article — a plan, explicitly not a result.
- Evidence: notebook `24` second table (`M145`–`M152`); recommendations `C075`–`C078` as mandate.
- Preserve: plan-vs-result separation labelled throughout; four of the eight cluster claims carry no falsifier — that is the point of the page.
- Reader/use: funding/proposal audience; direct feeder into `research/processed/FollowUps/`.

## X — Cross-cutting ideas (combine notebooks; do not re-chart wave 1)

### X.1 "Certified vs working: the compatibility gap from spec to living room"
- Angle: `02`'s conformance-vs-compatibility inference (`C015`, `C097`) meets `16`'s scorecard calibration and `03`'s failure taxonomy — one article following a device from certificate to daily use.
- Evidence: `C015`, `C097`, `C008`/`C011`; `M086`/`M087`; `M063`–`M070` calibration; `C076` disclosure ask.
- Preserve: each section keeps its source notebook's evidence class and gaps; no new per-ecosystem counts invented to join the sections.
- Reader/use: long-form flagship; the wave-2 thesis statement.

### X.2 "Money on different clocks: flexibility revenue vs household spend"
- Angle: `12`'s programme economics against `22`'s household clocks (upfront/monthly/frustration) — why a payback story and a barrier story can both be true.
- Evidence: `M089`/`M090`, `M127` chain; `M035`–`M037`, `M019`–`M024`; cautions `C088`, `C090`.
- Preserve: never sum across clocks; never average barrier denominators; wave-1 value-split/churn figures (`09`, `21`) linked, not redrawn.
- Reader/use: economics feature.

### X.3 "How to read this corpus: a gap-aware methods guide"
- Angle: the article every other article links — heuristic claim-to-metric linkage (section-first vs source-id-second, no foreign key per `schemas/stage2.sql`), confidence as extraction-time judgment, evidence-class preservation, falsifier discipline, unstated-conditions flags.
- Evidence: notebook `24` audit charts; notebook `00_index` (wave 1) corpus counts; `src/viz_core.py` function names as the reproducibility path.
- Preserve: this article must pass every acceptance gate in the Article Creation Protocol section 7 (AC:Scope through AC:Maintenance) — it is the worked example.
- Reader/use: evergreen reference; reviewer onboarding.

## Do-not-write list (evidence missing — commission research first, not articles)

- A four-ecosystem Matter parity league table (only `M004`/Samsung counted; Apple/Google/Amazon unrecorded — notebook `02` uncertainty panel).
- A "Matter release history" with calendar dates (no release dates in source; wave-1 notebook `01` stays ordinal for the same reason).
- A single smart-home barrier index or adoption funnel from notebook `22` bars (four different denominators; `C088` forbids it).
- A market price for insurer-paid smart-home policies from `C113` (one pilot, low confidence, reported signal).
- An Anker hub price or interpolated price trend (not recorded — notebook `19`).
- A ranked comparison of the two flexibility programmes in notebook `12` (different conditions/denominators).
- Any claim presented without its falsifier status, evidence class, confidence, and linkage rule (Protocol section 5 steps 3–4; gates AC:Evidence, AC:Integrity, AC:Provenance).

## Reproducibility

- Database: `data/smarthome.duckdb`, read-only. Queries via `src/viz_core.py`: `fetch_claims` / `fetch_claim`, `claim_metrics_lookup` / `metrics_by_id`, `render_provenance_panel`, `sources_for_claims`, `connect_db` for `COUNT(1)` over `missing_falsifiers` / `unstated_conditions` / `unstated_boundaries` / `stage2_warning`.
- Notebook cells: each idea names its notebook and figure; hover text in `02`/`03` heatmaps carries the governing claim id; money/barrier bars carry per-bar denominators from each metric's `unit` cell.
- Freshness: re-run `scripts/build_visualization_notebooks.py --check` and the `src/tests/test_viz_notebooks.py` gate before commissioning; if an `M###`/`C###` id above no longer verifies, the idea returns to draft.

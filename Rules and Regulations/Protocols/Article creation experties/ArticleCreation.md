# Article Creation Protocol

## Status
Mandatory for converting notebook-derived claim evidence into articles. Read-only against `notebooks/`; article outputs are derivative, not controlling.

---

## 1. Purpose
Notebooks (`notebooks/`) visualize claims from `data/smarthome.duckdb` (read-only via `src/viz_core.py`, claim IDs C001–C114, 119 claims, 6 domains). They provide inspiration (patterns, relationships, gaps) and structured data (claim text, metrics, entities, sources, confidence, evidence class, extraction decisions) for article construction. This protocol defines how that evidence is selected, validated, composed, and released as a finished article.

Not a replacement for source evidence; links to controlling sources (`research/raw/Stage 2/`, `schemas/stage2.sql`) remain authoritative.

---

## 2. Research Basis (notebook survey, 2026-09-29)

| Notebook | Claims | Domain / Theme | Data / Inspiration role |
|---|---|---|---|
| `00_index.ipynb` | all 119 (index) | Cross-cutting | Corpus-wide counts (claims, metrics, entities, sources, predicates, extraction decisions); evidence-class/ confidence chart; domain counts; search/filter widget; gap listing (13 claims no falsifier; 11% metrics with unstated conditions; downgrade/conflict decisions L014/L030/L031); reproducibility query block. Navigation and inventory source. |
| `01_matter_version_timeline.ipynb` | C001–C006, C009, C011 | Matter/Thread Interop | Timeline of Matter 1.4→1.6 with device-type additions, Joint Fabric; ordinal axis (no release dates in source); capability attributions claim-scoped (C003/C009/C011), not independent. Source of temporal framing and interoperability narrative. |
| `09_device_flexibility_comparison.ipynb` | C043–C050, C055–C058, C061 | Energy / Sustainability | Radar/spider: HPWH (29–54% load shift, 8–46% cost reduction), Heat Pump (88.2% power reduction, 1.58 kW max), EV (11.8% auto vs 0.4% manual), Battery (weakest economic link), Solar (40–60% self-consumption). Metric linkage heuristic (section → source id). Source of quantitative comparison and economic framing. |
| `15_support_period_landscape.ipynb` | C064–C066, C069, C103, C105, C067, C068 | Security / Lifecycle | Grouped bar by device category: Smart Lock 3–5yr, Camera 5yr Nest / none Apple, Hub 3–4–5yr, Router 3–5yr, Appliance 7yr; CRA floor 5yr (not default), 10yr update availability. Source of lifecycle/standards framing. |
| `21_subscription_fatigue_funnel.ipynb` | C085–C086, C114, C055 | Emerging / Business | Funnel: owners → pay 47% → video security 19% → churn 11–14%/qtr (13% annualized); Arlo 1% monthly churn, 4.0x LTV/CAC vs streaming 2–8.7x. Source of adoption/churn economics. |

Shared library `src/viz_core.py` (used by all): `connect_db(read_only=True)`, `fetch_claim`, `fetch_metrics_for_claim`, `render_provenance_panel`, `claim_domain`, `numeric_value`/`range_value`, evidence-class markers, confidence colors. All notebooks read only `data/smarthome.duckdb`; no other file; headless execution tested by `src/tests/test_viz_notebooks.py`; renderer set to `plotly_mimetype+notebook` for reproducible figure payload.

### Notebook-level limitations (must be preserved in articles)
- **No foreign key** between claims and metrics (`schemas/stage2.sql`); linkage is heuristic (section, then source id); must state which rule fired.
- **Confidence is extraction-time judgment**, not probability (`L030` absence of falsifier; `L014`/`L031` evidence downgrades).
- **13 claims have no falsifier** — cannot be re-tested from corpus; must be flagged.
- **Forecast/vendor material downgraded** (`L014`, `L031`) — evidence class `reported signal` at medium confidence; do not upgrade.
- **Conditions not stated** on some metrics (`unstated_conditions` view) — conditions must not be presented as verified.
- **Domain counts keyword-derived** (`viz.claim_domain` on section names) — navigation, not taxonomy; sections reused across domains.
- **No per-ecosystem device counts** outside Samsung (M004 = 58); parity matrix deferred.
- **No release dates** for Matter specs; timeline ordinal.

---

## 3. Values from Notebook Design (`Rules and Regulations/Commander Deck/Plans/Visualisation_Notebook_Plan#F5DB`)
- One claim (or tight cluster) per visualization.
- Evidence-first: every visual cites Source IDs and confidence.
- Interactive (Plotly/Altair, ipywidgets) — article may reference interactive version rather than static reproduction.
- Reproducible: reads directly from `smarthome.duckdb` (read-only) via DuckDB.
- Provenance panel: Claim ID, text, type, confidence, source IDs, falsifier, extraction log refs.
- Uncertainty visible: confidence bands, “conditions not stated” flags, conflicting values shown side-by-side (e.g., M101 vs M102 override rates).

These values become article requirements in §5.

---

## 4. Source Precedence (governing for article content)
1. **Controlling:** claim text, metric definitions, entities, sources, extraction decisions in `data/smarthome.duckdb` (via `viz_core` queries); `schemas/stage2.sql`; `research/raw/Stage 2/Extraction 1/` logs (`ExtractionLog.md`, `Sources.md`).
2. **Supporting:** notebook visualizations (`notebooks/*.ipynb`) — inspiration and structured data, not authority; must link back to controlling DB entries.
3. **Derivative:** article text, charts, summaries — must not upgrade evidence, invent conditions, or suppress conflicts/gaps.

---

## 5. Article Creation Procedure (constructed comprehensive protocol)

### Step 1 — Define mandate and boundary
Name article topic, target claim cluster(s) (from index or domain planning), intended reader, scope inclusions/exclusions. Declare if article covers a single claim (e.g., C043–C050 energy cluster), a cross-cutting theme (interoperability + security), or a gap/agenda item (open questions, falsifier-absent claims). State exclusions (e.g., “no fictional per-ecosystem counts; parity deferred”). Record in article header.

### Step 2 — Select evidence from notebooks / DB
- Query `viz.fetch_claims` / `viz.fetch_all_claims`; filter by `CLAIM_IDS` or `domain`/`section`.
- Pull metric frame: `viz.fetch_metrics_for_claim` (record which linkage rule fired: section-first or source-id-second).
- Pull provenance: `viz.render_provenance_panel` → claim text, claim type, confidence, source_refs, falsifier, extraction_decision refs.
- Pull entities, sources, predicates via `viz_core`.
- Record corpus counts (`CORPUS` in index) for scale context — distinguish cluster size from corpus size.
- **Do not invent** metrics not in DB; for missing parity / missing dates, state “not stated in source / deferred.”

### Step 3 — Assess evidence quality (gate: evidence-class preservation)
For each claim used:
- Record `evidence_marker` (documented fact / reported signal / inference / recommendation) and `confidence` (high/medium/low).
- Check falsifier (`falsifier_missing`); if missing, flag explicitly (13 claims).
- Check extraction decisions (`evidence_downgrade`, `classification_conflict`, `falsifier_absent`) — cite decision ID (`L014`, `L030`, `L031`, etc.).
- Note `conditions_stated` = FALSE if applicable.
- Preserve qualifiers, dates, versions, units; do not upgrade reported signal to documented fact.
- If conflicting values exist (e.g., M101/M102), show side-by-side with explanation of condition/assumption difference, not reconciliation.

### Step 4 — Compose with provenance and uncertainty visible
Structure (minimum; adapt to reader):
1. **Claim statement(s)** — direct from DB claim_text, with claim IDs.
2. **Provenance panel** — collapsible/table: claim ID, type, confidence, evidence class, source IDs, falsifier status, extraction log refs, related decisions.
3. **Evidence display** — metric values with units, conditions noted; charts derived from DB queries (not hand-drawn); if interactive, link to notebook.
4. **Uncertainty / gaps** — “conditions not stated” flags; missing falsifiers; downgraded evidence; conflicts shown; deferred items (parity matrix, release dates).
5. **Interpretation / synthesis** — explicitly labeled as synthesis/inference/recommendation per `Research-Evaluation.md`; separate from evidence.

Requirements:
- Every figure/data claim links to DB query / notebook cell / source ID.
- Confidence color coding consistent with `viz.CONFIDENCE_COLORS` (high/medium/low).
- Domain classification declared as keyword-derived (`viz.claim_domain`) — not canonical taxonomy.
- No promotion: synthesis does not make a reported-signal claim more reliable.

### Step 5 — Reconcile and challenge
- Re-run key DB queries (reproducibility block from index) to confirm counts/values have not shifted; if DB updated, note version.
- Check for contradictions between notebook figures and DB (e.g., metric totals, claim counts); if notebook shows approximate/derived values, label accordingly.
- Look for credible exception/counterexample in corpus (e.g., claims with no falsifier, conflicting metrics); do not manufacture consensus.
- Confirm every local source link resolves to controlling document (`research/raw/Stage 2/`, `schemas/`, `notebooks/`, DB tables).

### Step 6 — Validate navigation, authority, and maintenance
- Links to controlling sources present (`data/smarthome.duckdb`, `schemas/stage2.sql`, `src/viz_core.py`, extraction logs).
- Link to source notebook(s) preserved; article labeled as derivative (not controlling evidence).
- Status, snapshot/review date (2026-09-29 based on notebook survey), maintainer role stated.
- Update triggers defined: DB change (new extraction stage), new claim/metric, falsifier resolved, downgrade reversed, notebook revised.
- History preserved: do not silently erase prior versions or conflicting interpretations.

---

## 6. Non-Negotiable Rules (applied to articles)
1. Declare boundary (clustering method, exclusions, derivative status).
2. Account for every claim/metric used; mark omissions (falsifier-absent, unstated conditions, deferred items).
3. Do not claim exhaustive evidence review without it; if notebook/DB not fully reviewed, disclose.
4. Trace material statements to DB path + section/head; link to controlling source, not just notebook.
5. Do not upgrade evidence: preserve evidence class, confidence, qualifiers, conditions.
6. Retain conditions, boundaries, exceptions, conflicts, open questions; do not discard for brevity.
7. Separate description from judgment: label synthesis/inference/recommendation explicitly.
8. Prefer links over duplicated rules: link to DB query, source document, extraction log.
9. Show changeability: status, snapshot date, maintainer, triggers.
10. Preserve history; revise without silent erasure.

---

## 7. Acceptance Gates

| Gate | Pass condition |
|---|---|
| AC:Scope | Article topic, claim cluster, exclusions, target reader, derivative status explicit. |
| AC:Evidence | All used claims/metrics traceable to DB (`local_id`, table, query); provenance panel included; evidence class preserved; confidence shown. |
| AC:Integrity | No evidence upgraded; falsifier-absent claims flagged; unstated conditions marked; conflicts shown, not reconciled; downgrade decisions cited. |
| AC:Provenance | Each material statement links to DB/path/section; controlling source identified; synthesis labeled separately; notebook reference preserved. |
| AC:Uncertainty | Gaps, deferred items, missing data (release dates, parity counts), and limitations stated explicitly (not omitted for readability). |
| AC:Reproducibility | Key figures reproducible from DB via documented query/notebook cell; renderer/format noted if interactive; headless-compatible if automated. |
| AC:Authority | Article states it is derivative of DB + notebooks; controlling sources (DB, schemas, extraction logs) govern; no invented precedence. |
| AC:Navigation | Links resolve; headings descriptive; source-level detail reachable without reconstructing from scratch. |
| AC:Maintenance | Status, snapshot/review date, maintainer, update triggers present; superseded/conflicting interpretations preserved. |

Before publication: reviewer not drafting must answer — (1) What claim cluster is covered and excluded? (2) Which DB entries / logs govern? (3) What is uncertain / missing / deferred? (4) Where is each claim checkable? (5) What change would make this article stale?

---

## 8. Source Inventory (notebooks reviewed for this protocol)

| Path | Role | Status | Review | Disposition |
|---|---|---|---|---|
| `notebooks/00_index.ipynb` | Cross-cutting index / evidence inventory | Current (11h ago, 2026-09-28) | Full content (cells 0–17) | Primary navigation; provenance template; gap listing |
| `notebooks/01_matter_version_timeline.ipynb` | Domain 1 (interop) visualization | Current | Partial (claims C001–C006/C009/C011, provenance, limitations) | Temporal/narrative source; ordinal axis caveat |
| `notebooks/09_device_flexibility_comparison.ipynb` | Domain 3 (energy) visualization | Current | Partial (C043–C050/C055–C058/C061, metric linkage) | Quantitative comparison source; heuristic-linkage caveat |
| `notebooks/15_support_period_landscape.ipynb` | Domain 4 (security/lifecycle) visualization | Current | Partial (C064–C066/C069/C103/C105/C067/C068) | Lifecycle/standards framing; CRA-floor caveat |
| `notebooks/21_subscription_fatigue_funnel.ipynb` | Domain 5 (business) visualization | Current | Partial (C085–C086/C114/C055, churn/economics) | Adoption/churn economics; measurement-clock caveat |
| `src/viz_core.py` | Shared DB/query/provenance library | Current (per AGENTS.md) | Metadata + referenced usage in notebooks | Controlling library; read-only DB access |
| `data/smarthome.duckdb` | Evidence database | Current (read-only) | Query-verified via notebooks/index | Controlling source for all claim/metric/entity data |
| `schemas/stage2.sql` | Schema / DDL | Governing | Referenced | Defines tables, no foreign key claim→metric |
| `research/raw/Stage 2/Extraction 1/ExtractionLog.md` | Extraction decisions (L014/L030/L031 etc.) | Current | Referenced via DB + notes | Controls evidence-class / downgrade / falsifier records |
| `Rules and Regulations/Commander Deck/Plans/Visualisation_Notebook_Plan#F5DB` | Notebook design plan | Current | Full content reviewed (catalogue, template, sequence) | Design values and template; not controlling evidence |

Not reviewed in full (out of scope for protocol): remaining proposed notebooks (02, 03, 05–08, 10–14, 16–20, 22–26), generated visualization exports, `scripts/build_visualization_notebooks.py` output.

---

## 9. Required Document Outline (article derived from notebooks)
```markdown
# [Article title]

## Document Control
- Status: draft / accepted / under_review / superseded
- Claim cluster / domain: ... (with local_ids)
- Snapshot / review date: ... (match DB/notebook date)
- Derivative of: notebooks/..., data/smarthome.duckdb (read-only), src/viz_core.py
- Controlling sources: schemas/stage2.sql; extraction logs; source documents
- Intended reader / use: ...
- Maintainer / reviewer role: ...
- Update triggers: DB stage update; new claim/metric; falsifier resolved; notebook revision

## 1. Claim Summary (with IDs)
Direct from DB; claim_type; evidence_marker; confidence; source_refs.

## 2. Provenance Panel (collapsible / table)
Claim ID · text · type · confidence · sources · falsifier status · extraction decisions (L...) · related metrics (with linkage rule noted).

## 3. Evidence and Metrics
Values + units + conditions stated? Link to DB query / notebook cell. Confidence color coding. Conflicting values shown, not reconciled.

## 4. Visualization / Reference
If derived from notebook: reference notebook file + cell; note interactive vs static; reproducibility command/query.

## 5. Uncertainty, Gaps, and Limitations
Falsifier-absent flags; unstated conditions; downgraded evidence; missing release dates / counts; deferred notebooks/items; domain-classification caveat.

## 6. Interpretation / Synthesis (explicit label)
Separated from evidence; labeled inference/recommendation if applicable.

## 7. Sources and Reproducibility
DB path; query/code; source document links; extraction log links; version / date.
```

---

## 10. Related Documents
- `Rules and Regulations/Protocols/AuthorityDocumentCreation.md` (synthesis / authority standard)
- `Rules and Regulations/Commander Deck/Plans/Visualisation_Notebook_Plan#F5DB` (notebook design, catalogue, template)
- `AGENTS.md` (repo architecture, viz_core, DB access, documentation conventions)
- `src/viz_core.py`, `data/smarthome.duckdb`, `schemas/stage2.sql`
- `research/raw/Stage 2/Extraction 1/` (extraction logs controlling evidence-class/decision records)
- `Research-Evaluation.md` (evidence-class definitions; synthesis labeling)
- `notebooks/` (derivative visualization sources)

# Book Creation Protocol

## Status
Mandatory for converting notebook-derived claim evidence and extended research into books (long-form, multi-chapter, sustained narrative). Read-only against `notebooks/` and `research/`; book outputs are derivative, not controlling.

---

## 1. Purpose
Notebooks (`notebooks/`) visualize claims from `data/smarthome.duckdb` (read-only via `src/viz_core.py`, claim IDs C001–C114, 119 claims, 6 domains). For books — which span dozens of chapters and synthesize evidence across domains — these notebooks provide both inspiration (patterns, cross-domain relationships, gap identification) and structured data (claim text, metrics, entities, sources, confidence, evidence class, extraction decisions, provenance panels). This protocol defines how that evidence is selected, validated, composed into sustained narrative arcs, validated at chapter and book-level, and released as a finished book.

Not a replacement for source evidence; links to controlling sources (`research/raw/Stage 2/`, `schemas/stage2.sql`, `research/processed/FollowUps/`) remain authoritative. A book is a multi-chapter derivative that must preserve, at every level, the evidence-class and provenance rules that govern single articles.

---

## 2. Research Basis (notebook survey, 2026-09-29; scaled to book scope)

Books draw on the same five notebooks as articles, but at larger scope — pulling cross-cutting patterns rather than a single cluster.

| Notebook | Claims | Domain / Theme | Book-level role |
|---|---|---|---|
| `00_index.ipynb` | all 119 (index) | Cross-cutting | Corpus architecture (count of claims/metrics/entities/predicates, domain counts, evidence-class distribution, 13 falsifier-absent, 11% unstated conditions, L014/L030/L031 downgrades). Defines which chapters are possible and which gaps require dedicated chapters or appendices. |
| `01_matter_version_timeline.ipynb` | C001–C006, C009, C011 | Matter/Thread Interop | Chapter-level temporal framing (interoperability narrative); ordinal timeline (no release dates in source) must be flagged at book level so the reader is not misled into reading an axis as absolute time. |
| `09_device_flexibility_comparison.ipynb` | C043–C050, C055–C058, C061 | Energy / Sustainability | Quantitative backbone for multi-chapter comparison chapters; metric linkage heuristic (section → source id) must be stated in each chapter's provenance notes; radar/spider used for synthetic overview chapter. |
| `15_support_period_landscape.ipynb` | C064–C066, C069, C103, C105, C067, C068 | Security / Lifecycle | Lifecycle/standards framing for security chapters; CRA floor (5yr) and 10yr update availability must be repeated in relevant chapters with explicit condition notes. |
| `21_subscription_fatigue_funnel.ipynb` | C085–C086, C114, C055 | Emerging / Business | Adoption/churn economics chapter; funnel percentages must be preserved exactly (47% pay, 19% video security, 11–14%/qtr churn, 13% annualized); Arlo 1% monthly / 4.0x LTV/CAC preserved. |

Shared library `src/viz_core.py` (used throughout): `connect_db(read_only=True)`, `fetch_claim`, `fetch_metrics_for_claim`, `render_provenance_panel`, `claim_domain`, `numeric_value`/`range_value`, evidence-class markers, confidence colors. All books must read only `data/smarthome.duckdb`; no other file; reproduction verified via `src/tests/test_viz_notebooks.py`; renderer `plotly_mimetype+notebook` for interactive supplements.

---

## 3. Book-Specific Design Values (derived from notebook design plan `Visualisation_Notebook_Plan#F5DB`)
- **One claim cluster per chapter** (or one synthesis theme per chapter); cross-chapter references must use persistent claim IDs.
- **Evidence-first at every level:** chapter-level provenance panels; book-level master provenance index; appendix-level full query/reproducibility log.
- **Sustained narrative consistency:** a claim's confidence must not vary between chapters; a metric's conditions must be preserved identically; contradictions across chapters must be shown, not reconciled silently.
- **Chapter-level interactivity:** chapters may reference interactive notebook versions (not static reproduction); book should include a reproducibility appendix with query cells per chapter.
- **Cross-chapter traceability:** every material statement in any chapter must link to a DB entry; cross-references between chapters should use claim IDs, not chapter names alone.
- **Uncertainty at scale:** gap listings (13 falsifier-absent claims; deferred parity; missing release dates; unstated conditions) must appear in a dedicated "Gaps and Limitations" chapter plus chapter-level callouts, not hidden in footnotes.

---

## 4. Source Precedence (governing for book content, scaled)
1. **Controlling:** claim text/metrics/entities/sources/decisions in `data/smarthome.duckdb` (via `viz_core` queries); `schemas/stage2.sql`; `research/raw/Stage 2/Extraction 1/` logs (`ExtractionLog.md`, `Sources.md`); `research/processed/FollowUps/` (waves, benchmark conditions when populated).
2. **Supporting:** notebook visualizations (`notebooks/*.ipynb`) — inspiration, structured data, reference figures; must link back to controlling DB entries per chapter; not controlling evidence.
3. **Derivative:** book text, charts, syntheses, chapter structures — must not upgrade evidence, invent conditions, suppress conflicts/gaps, or invent chapter-level consensus that the DB does not support.

---

## 5. Book Creation Procedure (constructed comprehensive protocol, book-scale)

### Step 1 — Define book mandate and architecture
Name book topic, target claim clusters (from index or multi-domain planning), intended reader, scope inclusions/exclusions at book level. Declare whether the book is:
- **Single-cluster deep dive** (e.g., C043–C050 energy across 6 chapters),
- **Cross-cutting synthesis** (e.g., interoperability + security + energy across 12 chapters), or
- **Gap / agenda book** (open questions, falsifier-absent claims, deferred benchmarks).

Define chapter architecture: number of chapters, which claims/metrics populate each, which chapters are synthesis (interpretation) vs evidence (direct DB citation), which chapters are gap/agenda (open questions, deferred items). Record architecture in book-level front matter.

State exclusions at book level: e.g., "no per-ecosystem parity counts (deferred); no absolute Matter release dates (ordinal only); no synthetic vendor comparisons outside DB evidence." Record exclusions so they survive all chapter revisions.

### Step 2 — Select evidence at book and chapter scale
For each chapter (or chapter group):
- Query `viz.fetch_claims` / `viz.fetch_all_claims`; filter by chapter's `CLAIM_IDS` or `domain`/`section`.
- Pull metric frames per claim (`viz.fetch_metrics_for_claim`); record which linkage rule fired (section-first or source-id-second) — must be noted per metric in each chapter's provenance notes.
- Pull provenance (`render_provenance_panel`) per claim; compile into chapter-level provenance tables and book-level master index.
- Pull entities, sources, predicates; record which are reused across chapters (shared entities should reference same DB id, not be re-described differently).
- Record corpus counts (`CORPUS` from `00_index.ipynb`) once at book level; distinguish cluster size from corpus size in each chapter.
- **Do not invent** metrics not in DB; for missing parity / missing dates / deferred benchmarks, state "not stated in source / deferred" in the appropriate gap chapter.

Book-level evidence tracking: maintain a master evidence register (table or DB view) mapping each chapter to its claim IDs, metric IDs, source IDs, extraction decisions, and falsifier status. This prevents a claim from accidentally being described differently in Chapter 3 vs Chapter 7.

### Step 3 — Assess evidence quality at chapter and book level
For every claim used in any chapter:
- Record `evidence_marker` (documented fact / reported signal / inference / recommendation) and `confidence` (high/medium/low) — must match DB for that claim ID; must not vary between chapters.
- Check falsifier (`falsifier_missing`); if missing, flag explicitly (13 claims) — must appear in chapter-level callout and gap chapter.
- Check extraction decisions (`evidence_downgrade`, `classification_conflict`, `falsifier_absent`) — cite decision ID (`L014`, `L030`, `L031`, etc.) — must survive all revision rounds.
- Note `conditions_stated` = FALSE if applicable — must be preserved identically across chapters using same metric.
- Preserve qualifiers, dates, versions, units; do not upgrade reported signal to documented fact.
- If conflicting values exist (e.g., M101 vs M102 override rates), show both in the relevant chapter with explanation of condition/assumption difference — never reconcile silently.
- **Book-level integrity check:** after all chapters drafted, run a consistency pass — every claim ID used must have identical evidence-marker/confidence/falsifier status in every chapter; any discrepancy must be flagged and either corrected to match DB or explicitly noted as an intentional comparison of conditions.

### Step 4 — Compose with provenance, consistency, and sustained narrative
Book structure (minimum; adapt to reader and scope):

1. **Front matter / Document Control** — book title, scope, claim clusters covered, exclusions, derivative status, controlling sources (DB + schemas + logs), intended reader, maintainer/reviewer role, update triggers, snapshot/review date, status.
2. **Chapter 1 — Introduction / Corpus Overview** — direct from `00_index.ipynb`: claim counts by domain, evidence-class distribution, gap listing, reproducibility query block, clarification of domain-classification method (`claim_domain` keyword-derived, not taxonomy).
3. **Chapters 2–N — Evidence chapters** — per cluster/theme; each chapter contains:
   - Claim statement(s) with claim IDs.
   - Chapter-level provenance panel (table: claim ID · text · type · confidence · sources · falsifier · decisions · metrics with linkage rule).
   - Evidence display (metrics + units + conditions noted; charts derived from DB queries; interactive supplements referenced).
   - Uncertainty / gaps callouts (falsifier-absent flags; unstated conditions; conflicts; deferred items).
   - Interpretation / synthesis (explicitly labeled per `Research-Evaluation.md`; separate from evidence).
4. **Chapter — Cross-domain synthesis** (if multi-cluster book) — explicitly labeled synthesis; must not upgrade any claim; must reference source chapters for each claim used.
5. **Chapter — Gaps, limitations, deferred items** — 13 falsifier-absent claims listed; missing release dates; unstated conditions; deferred parity matrix; downgraded evidence; benchmark gaps (`Wave2_Benchmark_Conditions.md` empty); notes on what a future book or benchmark chapter must address.
6. **Appendices** — reproducibility queries by chapter, source index (DB + notebooks + logs), master provenance index, glossary of claim/metric IDs, bibliography with evidence-class tags.
7. **Back matter** — document control (status, review date, update triggers, superseded/conflicting interpretations preserved).

**Book-level composition rules:**
- Every chapter must declare which claims/metrics it depends on; cross-chapter dependencies must use claim IDs, not narrative references alone.
- Every figure/data claim links to DB query / notebook cell / source ID — at chapter level and in master index.
- Confidence color coding consistent with `viz.CONFIDENCE_COLORS` (high/medium/low) — consistent across chapters.
- Domain classification declared as keyword-derived (`viz.claim_domain`) — never presented as canonical taxonomy, regardless of repetition across chapters.
- No promotion: synthesis chapters never make a reported-signal claim more reliable; synthesis must cite source claim IDs and label itself as inference/recommendation.
- Uncertainty never discarded for readability: gaps chapter required; missing conditions must stay missing.
- Cross-chapter references must verify that the referenced claim's status has not changed between draft and final; consistency pass required.

### Step 5 — Reconcile and challenge at book scale
- Re-run all key DB queries per chapter (reproducibility block from index); verify counts have not shifted; if DB updated (new Stage 2 extraction, new metrics), note version and update master register.
- Check for contradictions between chapters (e.g., same metric described with different conditions, same claim assigned different confidence); if a contradiction is due to different conditions (M101 vs M102), show both with condition notes; if due to error, correct to DB value.
- Look for credible exception/counterexample across the full corpus (e.g., claims with no falsifier across all chapters; conflicts in metrics); do not manufacture book-level consensus.
- Confirm every cross-chapter link resolves to controlling document; confirm links to `research/raw/Stage 2/`, `schemas/`, `notebooks/`, DB tables.
- Confirm book-level source inventory (§8 analog) lists every notebook, database table, schema, log, and design-plan reference reviewed — with status, review depth, and disposition — and notes which chapters depend on each.

### Step 6 — Validate navigation, authority, maintenance, and consistency
- Links to controlling sources present (`data/smarthome.duckdb`, `schemas/stage2.sql`, `src/viz_core.py`, extraction logs, processed follow-ups when relevant).
- Book labeled derivative; controlling sources govern; no invented precedence of book over DB.
- Status, snapshot/review date (match DB/notebook review, 2026-09-29 baseline), maintainer/reviewer role stated at book level and per chapter.
- Update triggers defined: DB change (new extraction stage, new claim/metric, falsifier resolved, downgrade reversed, notebook revised); chapter-level triggers if a chapter depends on a specific claim cluster.
- History preserved: superseded chapters, conflicting interpretations, prior draft conclusions kept visible (in appendix or version log) — never silently erased.
- **Book-level consistency gate:** a final pass verifies every claim ID used in any chapter has identical evidence-marker/confidence/falsifier/decision references; any discrepancy is either corrected to match DB or explicitly documented as a condition-dependent comparison.

---

## 6. Non-Negotiable Rules (applied to books)
1. Declare book boundary (chapter architecture, claim clusters, exclusions, derivative status, intended reader).
2. Account for every claim/metric used in any chapter; mark omissions (falsifier-absent, unstated conditions, deferred items) at chapter and book level.
3. Do not claim exhaustive evidence review at book level without reviewing all 119 claims / all notebooks / all relevant follow-ups; if partial, disclose scope precisely.
4. Trace every material statement in any chapter to DB path + section/head; link to controlling source; cross-chapter references must be verifiable.
5. Do not upgrade evidence: preserve evidence class, confidence, qualifiers, conditions — identical across all chapters referencing same claim/metric.
6. Retain conditions, boundaries, exceptions, conflicts, open questions — at chapter level and in dedicated gap chapter; never discard for narrative flow.
7. Separate description from judgment: label synthesis/inference/recommendation explicitly in synthesis chapters and at point of interpretation.
8. Prefer links over duplicated rules: master provenance index links to DB/query; chapters link to index; index links to controlling source.
9. Show changeability: status, snapshot date, maintainer, chapter-level and book-level triggers.
10. Preserve history: revise without silent erasure; maintain version log of chapter conclusions that have changed.
11. **Book-level consistency:** no claim's evidence status may vary unexplained between chapters.

---

## 7. Acceptance Gates (book-scale)

| Gate | Pass condition |
|---|---|
| AC:Scope | Book topic, chapter architecture, claim clusters per chapter, exclusions, target reader, derivative status, controlling sources all explicit in front matter. |
| AC:Evidence | All used claims/metrics traceable to DB (`local_id`, table, query); chapter-level provenance panels present; master provenance index complete; evidence class preserved; confidence shown consistently; linkage rules noted per metric. |
| AC:Integrity | No evidence upgraded at any chapter; falsifier-absent claims flagged at chapter + book level; unstated conditions marked identically; conflicts shown, not reconciled; downgrade decisions cited; book-level consistency pass passes. |
| AC:Provenance | Every material statement in any chapter links to DB/path/section; controlling source identified; synthesis labeled separately; notebook references preserved; cross-chapter references verifiable. |
| AC:Uncertainty | Gaps chapter present; falsifier-absent list complete; deferred items (parity, dates, benchmarks) stated at book level; missing conditions preserved; limitations not omitted for readability. |
| AC:Reproducibility | Key figures reproducible from DB via documented queries (per chapter); interactive supplements referenced with file + cell; reproducibility appendix with query block; headless-compatible if automated. |
| AC:Authority | Book states derivative status; controlling sources (DB, schemas, logs, follow-ups) govern; book does not override DB evidence; source inventory (§8 analog) present. |
| AC:Navigation | Chapter headings descriptive; master index reachable; source-level detail reachable without reconstructing from scratch; cross-chapter references resolve. |
| AC:Maintenance | Status, snapshot/review date, maintainer/reviewer, chapter-level + book-level update triggers, superseded/conflicting interpretations preserved; version log present. |
| AC:Consistency | Final pass confirms every claim ID used in any chapter has identical evidence-marker/confidence/falsifier/decision references across all chapters; discrepancies either corrected or documented. |

Before publication: reviewer not drafting must answer — (1) What chapter architecture covers and excludes? (2) Which DB entries / logs govern each chapter and the whole book? (3) What is uncertain / missing / deferred at book and chapter level? (4) Where is each claim checkable (DB + loop + chapter)? (5) What change in DB, notebook, or claim would make each chapter (or the book) stale? (6) Has the consistency pass passed with no unexplained claim-status variation across chapters?

---

## 8. Source Inventory (book-level review of supporting materials; scaled from article inventory)

| Path | Role | Status | Review depth | Disposition / chapter dependency |
|---|---|---|---|---|
| `notebooks/00_index.ipynb` | Corpus inventory / navigation / gap listing | Current (11h ago) | Full (cells 0–17) | Chapter 1 (corpus overview); master inventory; all chapters reference |
| `notebooks/01_matter_version_timeline.ipynb` | Domain 1 temporal framing | Current | Partial (C001–C006/C009/C011 + provenance + limitations) | Interoperability / timeline chapters; ordinal-axis caveat |
| `notebooks/09_device_flexibility_comparison.ipynb` | Domain 3 quantitative comparison | Current | Partial (C043–C050/C055–C058/C061 + metric linkage) | Energy / comparison chapters; radar/spider for overview |
| `notebooks/15_support_period_landscape.ipynb` | Domain 4 lifecycle / standards | Current | Partial (C064–C066/C069/C103/C105/C067/C068) | Security / lifecycle chapters; CRA-floor caveat |
| `notebooks/21_subscription_fatigue_funnel.ipynb` | Domain 5 adoption / churn economics | Current | Partial (C085–C086/C114/C055 + funnel metrics) | Emerging / business chapters;
| `src/viz_core.py` | Shared DB/query/provenance library | Current | Metadata + in-use verification | All chapters (controlling library); read-only DB access |
| `data/smarthome.duckdb` | Evidence database | Current (read-only) | Per-chapter query verification required | All chapters (controlling); master register must reference |
| `schemas/stage2.sql` | Schema / DDL; defines no FK claim→metric | Governing | Referenced | All chapters (defines linkage heuristic); must be cited in provenance notes |
| `research/raw/Stage 2/Extraction 1/ExtractionLog.md` | Extraction decisions (L014/L030/L031 etc.) | Current | Referenced via DB | Chapters using downgraded/conflicting claims; decision IDs must survive |
| `research/processed/FollowUps/` (waves, agendas, benchmark conditions when populated) | Gap / benchmark / agenda sources | Partial (Benchmark_Conditions empty) | Referenced | Gap chapter; benchmark chapter deferred until filled |
| `Rules and Regulations/Commander Deck/Plans/Visualisation_Notebook_Plan#F5DB` | Notebook design / template / catalogue | Current | Full content reviewed | Design values (§3); not controlling evidence |
| `AGENTS.md` | Repo architecture / conventions | Current | Metadata | Controlling conventions (DB read-only, provenance, deterministic IDs) |

Not fully reviewed (out of scope for this protocol): remaining notebooks (02, 03, 05–08, 10–14, 16–20, 22–26), generated visualization exports, `scripts/build_visualization_notebooks.py` output, per-chapter detailed query logs (must be produced during drafting, not assumed).

---

## 9. Required Document Outline (book derived from notebooks, multi-chapter)

```markdown
# [Book Title]

## Document Control
- Status: draft | accepted | under_review | superseded
- Book scope / claim clusters / chapter architecture
- Chapter list with claim/metric ranges per chapter
- Snapshot / review date: ... (must match DB / notebook base)
- Derivative of: notebooks/..., data/smarthome.duckdb (read-only), src/viz_core.py
- Controlling sources: schemas/stage2.sql; extraction logs; source documents; processed follow-ups
- Intended reader / use: ...
- Maintainer / reviewer role: ...
- Update triggers: DB stage update; new claim/metric; falsifier resolved; notebook revision; chapter-level claim changes
- Version history: list of prior drafts with revised chapter conclusions preserved

## Front Matter / Introduction (Chapter 1)
- Corpus overview: 119 claims, 6 domains, evidence-class distribution, 13 falsifier-absent
- Notebooks as sources: which notebooks inform which chapters; derivation status
- Domain classification method (keyword-derived, not taxonomy)
- Reproducibility: query block; renderer / interactive supplement notes
- Book-level exclusions and deferred items

## Evidence Chapters (Chapters 2–N)
Per chapter (repeat structure):
### Chapter N — [Theme / Cluster / Claim Range]
- Claim summary (with IDs, types, confidence, evidence class)
- Provedcence panel (table per claim: ID · text · confidence · sources · falsifier · decisions L... · related metrics with linkage rule)
- Evidence display (metrics with units + conditions; charts from DB queries; interactive supplement refs)
- Uncertainty / gaps callouts (falsifier-absent; unstated conditions; conflicts; deferred)
- Interpretation / synthesis (explicit label; separated from evidence; references source claim IDs)
- Source links and reproducibility query

## Cross-Domain Synthesis Chapter (if multi-cluster)
- Explicit synthesis label
- Every claim cited by ID from source chapters; no promotion
- Conflicts shown with condition notes
- No invented consensus

## Gaps, Limitations, and Deferred Items Chapter
- 13 falsifier-absent claims (with IDs)
- Unstated conditions summary (metrics affected, by domain if applicable)
- Downgraded evidence summary (L014 / L031 decisions; evidence class preserved)
- Deferred benchmarks (Wave2_Benchmark_Conditions.md empty; conditions for future benchmark chapters)
- Missing release dates (Matter spec; ordinal timeline caveat)
- Deferred parity / ecosystem counts
- Suggested next-book / next-benchmark agenda

## Appendices
- A. Master Provenance Index (claim ID → chapter references → DB query → source IDs → decisions)
- B. Reproducibility Queries (per chapter; query text + expected result + DB version)
- C. Source Index (all notebooks, DB tables, logs, schemas, follow-ups — status, review depth, disposition, chapter dependency)
- D. Glossary of Claim / Metric / Entity IDs
- E. Version History / Superseded Conclusions
- F. Bibliography (with evidence-class tags per entry)

## Back Matter / Document Control (reprise)
- Final status; review date; maintainer; triggers; superseded/conflicting interpretations preserved
```

---

## 10. Related Documents
- `Rules and Regulations/Protocols/ArticleCreation.md` (single-article version; this protocol extends its rules to sustained, multi-chapter form)
- `Rules and Regulations/Protocols/AuthorityDocumentCreation.md` (synthesis / authority standard)
- `Rules and Regulations/Protocols/FollowUpResearch.md` (follow-up formulation; gap classification; scoring)
- `Rules and Regulations/Protocols/Research-Evaluation.md` (evidence-class definitions; synthesis labeling)
- `Rules and Regulations/Commander Deck/Plans/Visualisation_Notebook_Plan#F5DB` (notebook design / template / catalogue)
- `Rules and Regulations/Commander Deck/Plans/ResearchPlan.md` (corpus directions; RQ-AGT-03 LangGraph boundary; Phase 3 agent architecture)
- `AGENTS.md` (repo architecture; viz_core; read-only DB access; conventions)
- `src/viz_core.py`, `data/smarthome.duckdb`, `schemas/stage2.sql`
- `research/raw/Stage 2/Extraction 1/` (extraction logs controlling evidence-class/decision records)
- `research/processed/FollowUps/` (gap / benchmark / agenda sources)
- `notebooks/` (derivative visualization sources per chapter)

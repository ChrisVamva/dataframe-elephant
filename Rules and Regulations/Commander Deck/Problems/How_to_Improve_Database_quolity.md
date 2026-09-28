# How To Improve Database Quality

**Date:** 2026-09-28
**Subject:** `data/citations.duckdb`, run `run_d79f60cc7541beb30b19a88d`
**Trigger:** the first successful export of the citations database
**Companion documents:** [Report1.md](Report1.md) (code-level review, 2026-09-27),
[ProblemPrompts.md](ProblemPrompts.md) (PP-001, workflow problem)
**Status:** open, for action
**Path note:** the Stage 2 inputs cited below (`research/raw/Stage 2/*.md`) were moved
into `research/raw/Stage 2/Extraction 1/` on 2026-09-28 when a second extraction
folder was added; the measurements below predate that move and are unchanged by it.

---

## 1. Purpose and scope

The first export of `data/citations.duckdb` completed and verified cleanly on
2026-09-28. Both the CSV and Parquet bundles returned `VERIFIED_OK`, and the
source database was provably unmodified (SHA-256 identical before and after).

**The export pipeline is not the problem. The data inside the database is.**

This document records what the first database is missing, why it is missing it,
and what can be done about it. It is a data-quality document, not a code-defect
document. Report1 covers pipeline defects; where a data gap here has a code-side
cause, it is flagged and cross-referenced rather than re-argued.

Every number below was measured against the live database and the live warnings
file on 2026-09-28. Where something was inferred rather than measured, it says so.

---

## 2. Baseline: what the first database actually contains

### 2.1 Inventory

| Item | Value |
| --- | --- |
| `run_id` | `run_d79f60cc7541beb30b19a88d` |
| Source | `data/citations.duckdb`, 5,779,456 bytes |
| Source SHA-256 | `c56a7e70f6dfaeb987837b397e1c62436d95d65a693ac892024b05cf6eeb49a5` |
| Base tables | 9 |
| Views | 5 |
| Ingestion warnings | 594 |
| Export bundle | 35 files, 764,726 bytes, both formats verified |

Row counts:

| Table | Rows | | View | Rows |
| --- | --- | --- | --- | --- |
| `source` | 204 | | `view:document_citation_coverage` | 10 |
| `citation_occurrence` | 443 | | `view:source_recurrence` | 204 |
| `source_alias` | 443 | | `view:source_reputation` | 204 |
| `ingestion_warning` | 594 | | `view:next_research_candidates` | **0** |
| `research_document` | 10 | | `view:source_conflicts` | **0** |
| `ingestion_input` | 10 | | | |
| `ingestion_run` | 1 | | | |
| `claim` | **0** | | | |
| `claim_source` | **0** | | | |

### 2.2 Citation resolution

| `resolution_status` | Count | Share of 443 |
| --- | --- | --- |
| `resolved` | 211 | 47.6% |
| `unresolved` | 197 | 44.5% |
| `ambiguous` | 35 | 7.9% |

**Less than half of all citations resolve to a source.** A 52.4% unresolved-or-
ambiguous rate is the single defining characteristic of this snapshot.

### 2.3 Warning stream

| `warning_type` | Count |
| --- | --- |
| `source_rows_lacking_direct_urls` | 337 |
| `unresolved_alias` | 217 |
| `duplicate_candidate` | 35 |
| `weak_source_classification` | 5 |

Warnings are concentrated in just three files:

| `input_path` | Warnings |
| --- | --- |
| `research/raw/Stage 1/Citations/Report.md` | 406 |
| `research/raw/Stage 1/Citations/Citation.md` | 181 |
| `research/raw/Stage 2/Sources.md` | 7 |

### 2.4 A note on the comparison baseline

Report1 measured a different snapshot: 15 documents, 207 sources, 455
occurrences, 604 warnings. The current database has 10 documents, 204 sources,
443 occurrences, 594 warnings. The document count fell from 15 to 10 because
`research/raw/Stage 1/` was archived during Wave 1 (see the
`wave_1_archive_20260927_192048.tar.gz.enc` artifact and its manifest in
`research/raw/Stage 1/Archive/`). **The comparison is therefore not
like-for-like**, and any trend read across the two reports is confounded by the
archiving step. This is worth stating plainly so that a future reader does not
mistake a shrinking corpus for a pipeline regression, or a stable corpus for
improvement.

---

## 3. What the first database was missing

Seven gaps, ordered by how much they limit the database's usefulness.

### G1 - Claim layer is completely empty (Critical)

`claim` and `claim_source` both contain **zero rows**. Every claim-derived view is
consequently empty: `next_research_candidates` returns 0 rows, and
`source_conflicts` returns 0 rows.

This is not a subtle degradation. The database's entire analytical purpose —
tracking what is claimed, how confident we are, whether sources agree, and what
would falsify a claim — is absent. What remains is a citation registry.

The Stage 2 file that should populate it,
`research/raw/Stage 2/Claims.md`, contains the correct table header:

```markdown
| Claim ID | Claim text | Claim type | Confidence | Source IDs | Falsifier | Workflow stage | Stage 1 source | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

and **no data rows**. The file's own `gate_results` block claims
`gate_2_claim_traceability: pass` and `gate_7_ingestibility: pass` against a
table that is empty. The gates are validating the presence of a header, not the
presence of claims. So the empty claim layer is a *content* gap in Stage 2, and
a *gate* gap that allowed an empty table to be declared ingestible.

### G2 - Nearly half of all citations resolve to nothing (Critical)

197 unresolved and 35 ambiguous out of 443. The alias table mirrors this:
232 of 443 aliases (52.4%) carry `match_method = 'unresolved'`, against 211
matched by `canonical_url`.

Sampling the raw text shows these are not edge cases. Representative unresolved
rows:

```text
S5 | **Internal vault notes** (synthesis sources, not external evidence): [[ANT GP H]], [[C]], [[DPS]]
20 | Existing vault note - PROV-K Ontology - Detailed Overview | Internal (local vault) | Primary
1 | Analytics Vidhya - pandas vs Polars vs DuckDB | Secondary
5 | International Journal on Digital Libraries (2025) - "Provenance-driven nanopublications..."
```

and ambiguous rows, which list several candidate sources in one cell:

```text
1 | Role definitions for Knowledge Engineer, Data Analyst, Research Engineer | freelancermap.com, up...
2 | Methodologies on ETL vs ELT and Data Provenance | getdbt.com, medium.com, secoda.co | Mixed
3 | AI Agent orchestration frameworks (LangGraph, CrewAI, Pydantic AI) | langchain.com, crewai.com, ...
```

Two distinct failure shapes are mixed together here:

- **Genuinely unresolvable rows** — internal vault cross-references (`[[C]]`,
  `[[DPS]]`) and bare descriptive text with no URL at all.
- **Resolvable-in-principle rows** — citations naming a real publisher plus a
  real article, which a human or a resolver could resolve, but which the parser
  refuses to because matching is deliberately strict and non-fuzzy.

The distinction matters because the two have completely different fixes.

### G3 - Source metadata is structurally empty (High)

Whole columns across all 204 sources are null:

| Column | NULL count | Share |
| --- | --- | --- |
| `author` | 204 | 100% |
| `access_date` | 204 | 100% |
| `directness` | 204 | 100% |
| `status` | 204 | 100% |
| `bias_notes` | 204 | 100% |
| `publication_date` | 167 | 81.9% |
| `publisher` | 37 | 18.1% |
| `metadata_notes` | 64 | 31.4% |
| `evidence_class` | 1 | 0.5% |

`canonical_url` and `title` are the only fully populated identifying columns
(0 nulls), and 0 sources have a non-HTTP `canonical_url`.

The `AGENTS.md` convention that `status`/`directness` stay `NULL` rather than
`"unknown"` when unrecorded is being honoured correctly — 204 NULL, 0
`'unknown'`. That distinction is preserved and should stay that way. The problem
is not the encoding of the gap; it is that the gap is 100% of rows.

Consequences: the evaluator query in `analysis/citation_evaluator.sql` that
selects sources needing review (`publication_date IS NULL`, `directness IS NULL`)
returns **all 204 sources**, so the triage query currently has no discriminating
power. This is the same class of issue as Report1's F5, now measurable.

### G4 - Domain categorisation is a placeholder (High)

```text
uncategorised        168   (82.4%)
organizational         9
technical_standard     7
academic_research      6
compliance_regulation  4
market_research        4
ai_ml_technology       4
workflow_process       2
```

With 82.4% uncategorised, `domain_category` cannot currently support any
domain-level question. Note this is a *different* field from the
`weak_source_classification` warning (only 5 rows) — that warning concerns the
`evidence_class`/`source_type` taxonomy, not the domain taxonomy.

### G5 - Evidence classification is thin and partly unmapped (Medium)

`evidence_class` is `primary` 117, `secondary` 86, NULL 1. The 5
`weak_source_classification` warnings all report the same unmapped value
(`"Mixed"`) in `OP MS 1.3F.md` at lines 257 and 269 and nearby — a small set of
rows in one file, but one that is silently excluded from the classified
population. Report1's F4 identified a path where an unmapped classification is
dropped with no warning; the warning now exists, so the observability half of F4
appears addressed, but the underlying unmapped value remains.

`source_type` distribution:

```text
web_source 127 | documentation 28 | blog 23 | job_posting 9 | academic 6 | standard 6 | government 5
```

Two things stand out. 9 `job_posting` sources are a vendor/labour-market input
sitting in a research evidence table, and 23 `blog` sources outrank 6 `academic`
— the corpus is weighted toward vendor marketing over peer-reviewed work, which
limits what the database can defensibly support.

### G6 - 337 source rows lack a usable direct URL (High)

The largest single warning class. Sampled messages:

```text
Source row at C.md :: line 48 identifies a publisher domain, not a page URL.   | dev.to
Source row at FAI.md :: line 189 identifies a publisher domain, not a page URL. | observablehq.com
Source row at DC L5.6.md :: line 122 has no resolvable URL.                    | Internal (local vault)
Source row at 2. C.md :: line 60 has no resolvable URL.                        | DePaul University - data architect career resource
Source row at 5. DPS.md :: line 159 has no resolvable URL.                     | Springer - Systematic Review of Automation in Data Warehouse Design
Source row at Most-cited primary sources :: line 369 has no resolvable URL.    | Accenture job postings
```

Three sub-patterns:

1. **Publisher domain only** (`dev.to`, `medium.com`, `w3.org`) — a homepage,
   not a citation target.
2. **No URL at all**, descriptive only (`Springer - Systematic Review...`).
3. **Internal cross-references** (`Internal (local vault)`, `[[C]]`) — these are
   by design not external evidence and arguably should not be in the source
   table at all.

The strict, non-fuzzy matching in the parser is *correct* per the design in
`AGENTS.md`, and this document does not propose weakening it. The gap is
upstream: the corpus records citations at a granularity the schema cannot use.

### G7 - Document evaluation metadata is absent (Medium)

All 10 documents have NULL `quality_rating`; 9 of 10 have NULL
`evaluation_decision`. Only the one internal evaluation document
(`doc_80060e7ed726b7273f2f8191`, `First-Ratings.md`, `internal_evaluation`,
`is_internal = true`) carries a decision (`revise`).

The evaluation decisions exist in the source documents; they are not reaching the
database. This is Report1's F6, still open, and now confirmed against the current
snapshot rather than the earlier one.

---

## 4. Root causes

Distinguishing causes matters because the fixes differ.

| Gap | Primary cause | Owner |
| --- | --- | --- |
| G1 empty claims | Stage 2 produced an empty table; gates passed on header presence | Stage 2 content + gate design |
| G2 unresolved | Mixed: genuinely unresolvable input **and** strict matching | Corpus authoring + resolver policy |
| G3 empty metadata | Corpus records citations without bibliographic fields | Corpus authoring |
| G4 uncategorised | No domain taxonomy applied at ingest | Pipeline / taxonomy |
| G5 thin classification | Unmapped taxonomy values; corpus source mix | Taxonomy + corpus |
| G6 missing URLs | Citations recorded at publisher granularity | Corpus authoring |
| G7 missing eval metadata | Front-matter/decision extraction not reaching ingest | Pipeline |

**The dominant pattern is upstream, not in the database code.** G2, G3, G6 and
G7 all originate in *how research notes record citations* — a bare publisher, a
descriptive phrase, an internal `[[wikilink]]`, or nothing at all. The schema is
demanding, the parser is strict by design, and it is refusing to invent data that
was never written down. That refusal is the correct behaviour and should not be
relaxed to make the numbers look better.

G1 and G4 are the exceptions: those are genuinely deliverable inside this
workspace without changing what researchers write.

---

## 5. Proposed steps forward

Ordered by benefit-to-effort. Nothing here requires weakening resolution
strictness, and nothing requires editing a production database to suit tooling.

### Near-term — cheap, no schema change

**N1. Populate the Stage 2 claim table.**
Fill `research/raw/Stage 2/Claims.md` with real claims, each carrying `Claim ID`,
`Claim text`, `Claim type`, `Confidence`, `Source IDs`, and `Falsifier`, and
rebuild. This is the single highest-value action: it activates `claim`,
`claim_source`, `next_research_candidates`, and `source_conflicts` at once.
Expected effect: G1 moves from Critical to resolved; two views go from 0 to
populated.

**N2. Make the Stage 2 gates count rows.**
Change gates 2 and 7 from "header is present" to "at least N claim rows, each
with a non-null type and confidence". The current gates passed an empty table,
which is the mechanism that let G1 through unnoticed. Report1's F2 makes this
cheap to do safely: a real row will surface a constraint violation rather than
corrupt anything, because the build is now atomic.

**N3. Split the warning stream by cause.**
`unresolved_alias` (217) currently mixes internal `[[wikilinks]]`, bare
descriptive text, and real-but-multi-candidate citations. Tag them distinctly
(e.g. `internal_cross_reference`, `no_url_present`, `multi_candidate`) so the
next iteration can target the largest bucket. Right now the 197 unresolved
occurrences cannot be split without reading raw text by hand.

**N4. Add a quality dashboard query to `analysis/citation_evaluator.sql`.**
One query returning resolution rate, claim count, NULL-rate per source column,
and uncategorised share. The numbers in this document should be reproducible on
demand rather than recomputed by hand, and a single query makes regressions
visible between builds.

**N5. Apply a domain taxonomy to the 168 uncategorised sources.**
Even a coarse first pass (documentation / vendor / academic / standards /
government / labour-market) would move G4 from placeholder to usable, and
`job_posting` deserves its own category so those 9 rows stop being silently
mixed into research evidence.

### Medium-term — pipeline work

**M1. Feed document evaluation metadata into `research_document`.**
Resolve G7 by carrying `quality_rating` and `evaluation_decision` from the
documents' own front matter and decision tables into the table. Ten rows, one
parser path.

**M2. Give the triage query discriminating power.**
The evaluator's review query currently matches all 204 sources. Once M1 and a
`directness`/`status` pass exist, it should return the genuinely incomplete
subset. Until then it should be documented as non-selective so nobody mistakes
"204 flagged" for "204 problems".

**M3. Distinguish `primary` evidence from vendor content.**
With 127 `web_source` and 23 `blog` against 6 `academic`, add a
`commercial_interest` marker or equivalent so downstream queries can weight
independently. This is a schema addition and should go through a protocol
change, not a silent column.

**M4. Add a referential-integrity check to verification.**
Recorded here because it surfaced during the export readiness check and affects
confidence in every `VERIFIED_OK`. `verify_bundle` calls
`PRAGMA foreign_key_check`, which **does not exist in DuckDB 1.5.5**; the call
raises `CatalogException` and the surrounding `except Exception` sets
`violations = []`. The reported verification therefore covers schema, row counts,
and full content equality, but not referential integrity. Replace with explicit
per-constraint `LEFT JOIN ... WHERE child_fk IS NULL` checks, and stop swallowing
the error silently.

### Longer-term — corpus and process

**L1. Raise the citation-recording standard in the corpus.**
The durable fix for G2/G3/G6. A source table row should carry a page-level URL,
publisher, author where known, and publication date. `research/raw/Stage
2/Sources.md` already has the right column set (`ID | Source | URL | Publisher |
Classification | Publication date`) — but the sample rows show `Publisher` and
`Publication date` largely blank, and S5 is a list of internal wikilinks filed as
a *primary* source. Authoring guidance plus a pre-ingest lint would catch this.

**L2. Decide what an internal cross-reference is.**
`[[C]]`, `[[DPS]]` and `Internal (local vault)` appear as 337-warning-class rows
and as `S5` classified `primary`. Either model them properly (a
`document_reference` entity distinct from an external `source`) or exclude them
from the source table. Currently they inflate `source` while contributing no
citable evidence. This is a modelling decision, not a bug fix, and it should be
made explicitly rather than left to the parser.

**L3. Separate the three citation files' roles.**
406 of 594 warnings come from `Report.md` and 181 from `Citation.md`. These
files mix internal synthesis, aggregated "most-cited" lists, and real citations.
Splitting synthesis tables from citation tables would remove most of the noise at
source.

**L4. Re-measure after the next build with a like-for-like corpus.**
Section 2.4 notes the 15 → 10 document drop. Any future quality comparison
should state the document count alongside the metrics, and ideally hold the
archive state fixed.

---

## 6. What is explicitly *not* recommended

- **Do not add fuzzy URL matching.** The parser's refusal to guess is a feature.
  197 unresolved rows are a truthful record of an under-specified corpus. Guessing
  would convert visible gaps into invisible errors.
- **Do not backfill `NULL` to `'unknown'` or `''`.** The `NULL` vs `'unknown'`
  distinction is load-bearing and is currently correct in all 204 rows.
- **Do not edit `data/citations.duckdb` to improve these numbers.** The database
  is a build artifact of the corpus. Every fix above is upstream of it.
- **Do not treat the successful export as a quality signal.** `VERIFIED_OK` means
  the bundle faithfully reproduces the database. It says nothing about whether
  the database is any good — and this document is the evidence that it is not yet.

---

## 7. Evidence and limitations

**Measured** — all counts in Sections 2 and 3 come from read-only queries against
`data/citations.duckdb` and from
`data/citation_ingestion_warnings.jsonl`, on 2026-09-28, DuckDB 1.5.5 via
`.venv`. Warning messages quoted are verbatim samples.

**Inferred, not measured:**

- The attribution of G1 to Stage 2 content rather than an ingest defect is based
  on reading `research/raw/Stage 2/Claims.md` and observing its empty table. It
  was not confirmed by a controlled rebuild.
- The claim that publisher-granularity citations are "resolvable in principle"
  (Section G2) is a judgement. The count of how many of the 197 unresolved rows
  fall into the resolvable bucket was **not** measured — the warning taxonomy does
  not yet distinguish them, which is why N3 comes before any remediation of G2.
- The severity ordering in Section 5 is editorial, not derived from a scored
  rubric.

**Not assessed** — the quality of the research content itself, which
`Protocols/Research-Evaluation.md` governs; and `data/stage2.duckdb`, which was
not part of this export.

**Stale-reference warning** — numbers here describe run
`run_d79f60cc7541beb30b19a88d` only. Any rebuild produces a new `run_id` and
invalidates every figure in Section 2. Re-measure rather than carry these forward.

**Companion defects** — G7 and the gate behaviour in N2 overlap Report1 findings
F6 and F2. G3's triage consequence is the measurable form of F5. M4 is new and
not previously reported.






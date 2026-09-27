# First Ratings: Raw Research Corpus

## Evaluation record

- **Protocol:** `Protocols/Research-Evaluation.md`
- **Evaluation date:** 2026-09-27
- **Evaluator:** Protocol-based review by GitHub Copilot
- **Corpus:** Every Markdown document under `research/raw/`, including `research/raw/Citations/`
- **Intended use:** Decide which raw documents can inform `research/processed/`, identify evidence gaps, and prioritize the next verification pass.
- **Important boundary:** These ratings evaluate the research documents as evidence artifacts. They do not independently prove or disprove every substantive claim in those documents.

## Rating key

The gate matrix uses the protocol's gate statuses:

- **Pass:** the gate's required evidence and reasoning are substantially present.
- **Partial:** useful material is present, but a material limitation remains.
- **Fail:** the required evidence, scope, method, or traceability is absent or materially inadequate.

The **quality rating** is a document-level summary, not claim confidence:

- **High:** mostly ready for controlled use, with only bounded limitations.
- **Moderate:** useful working research, but requires explicit caveats or targeted revision.
- **Low:** useful as a lead or draft, but not dependable for unsupported conclusions.

The score is a compact diagnostic only: `Pass = 2`, `Partial = 1`, `Fail = 0`, for a maximum of 12. A score never overrides a failed mandatory gate.

## Corpus rating summary

| Document | A | B | C | D | E | F | Score | Quality | Decision |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| [ANT GP H.md](ANT%20GP%20H.md) | Fail | Fail | Fail | Fail | Fail | Partial | 1/12 | Low | Revise |
| [C.md](C.md) | Partial | Fail | Fail | Fail | Partial | Partial | 3/12 | Low | Revise |
| [CNE DPS 4.1 F.md](CNE%20DPS%204.1%20F.md) | Partial | Partial | Partial | Partial | Partial | Partial | 6/12 | Moderate | Revise |
| [CP L6.md](CP%20L6.md) | Pass | Partial | Pass | Partial | Partial | Partial | 8/12 | Moderate | Accept with limitations |
| [DC L5.6.md](DC%20L5.6.md) | Partial | Partial | Partial | Fail | Partial | Partial | 5/12 | Moderate | Revise |
| [DPS.md](DPS.md) | Partial | Partial | Partial | Fail | Partial | Partial | 4/12 | Low | Revise |
| [FAI.md](FAI.md) | Partial | Partial | Partial | Fail | Partial | Partial | 5/12 | Moderate | Revise |
| [G0.md](G0.md) | Partial | Partial | Fail | Fail | Partial | Partial | 4/12 | Low | Revise |
| [G1.md](G1.md) | Partial | Partial | Partial | Fail | Partial | Partial | 5/12 | Moderate | Accept with limitations |
| [G2.md](G2.md) | Partial | Pass | Partial | Fail | Partial | Partial | 6/12 | Moderate | Accept with limitations |
| [G3.md](G3.md) | Partial | Pass | Partial | Fail | Partial | Pass | 7/12 | Moderate | Accept with limitations |
| [OP MS 1.3F.md](OP%20MS%201.3F.md) | Partial | Partial | Partial | Fail | Partial | Partial | 5/12 | Moderate | Revise |
| [Q.md](Q.md) | Partial | Fail | Fail | Fail | Partial | Partial | 3/12 | Low | Revise |
| [Citations/Citation.md](Citations/Citation.md) | Partial | Partial | Fail | Partial | Fail | Partial | 4/12 | Low | Revise |
| [Citations/Report.md](Citations/Report.md) | Partial | Partial | Fail | Partial | Fail | Partial | 4/12 | Low | Revise |

## Corpus-level findings

### What is strong

- The corpus repeatedly converges on a useful research-to-data workflow: research, evidence, extraction, structured representation, normalization, storage, query, analysis, visualization, interpretation, and iteration.
- `CP L6.md` is the strongest focused architecture brief for ETL, ELT, federation, governance, and platform controls.
- `G1.md`, `G2.md`, and `G3.md` are the strongest provenance-focused notes because they rely on official or peer-reviewed technical sources and keep their subject matter narrow.
- `DC L5.6.md` and `CNE DPS 4.1 F.md` contain the most useful entity, relationship, provenance, and schema ideas for later modeling.
- The corpus generally recognizes that vendor documentation establishes intended capability, not independent proof of performance, adoption, or superiority.

### Recurring defects

- Most documents do not record search terms, inclusion and exclusion criteria, extraction steps, or conflict-resolution rules.
- Source lists are often more complete than claim-to-source mappings. Grouped citations do not establish which source supports which claim.
- Repeated citations and derivative atlas drafts are not independent corroboration. `CNE DPS 4.1 F.md` is a synthesis of earlier passes and must not be counted as an independent source for those same claims.
- Product pages, job postings, and vendor comparisons are sometimes used beyond what they establish: capability is treated as performance, role signal as role definition, or marketing as adoption evidence.
- Broad claims about market adoption, framework popularity, regulatory requirements, product superiority, benchmark magnitudes, and agent reliability are usually low or medium confidence.
- Several confidence labels in broad documents are higher than the documented evidence warrants.

### Corpus disposition

No broad atlas document should be promoted directly to `research/processed/` without a claim/evidence ledger. The focused documents can be retained as working references with their limitations attached. Before consolidation, deduplicate shared sources and shared prose, assign stable document and source IDs, and preserve the distinction between capability evidence, performance evidence, adoption evidence, and recommendation.

## Document evaluations

### 1. `ANT GP H.md`

**Research question and intended use:** Identify capabilities, roles, technologies, methodologies, and agents in the research-to-data workflow for a conceptual capability atlas and later entity modeling.

**Scope:** Broad workflow and capability lenses. Geography, population, time period, inclusion rules, and exclusions are not explicit.

**Gate results:** A Fail; B Fail; C Fail; D Fail; E Fail; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Research-to-data workflow stages | Inference | Plausible synthesis, but not mapped to atomic sources | Medium |
| Role, technology, and agent boundaries | Inference | Domain-level sources named, but exact support is absent | Low |
| Candidate entities and relationships | Recommendation | Useful modeling proposal, not an observed fact | Medium |

**Strengths:** Clear decomposition; useful workflow, entity, and relationship candidates; includes trade-offs and research gaps.

**Limitations and counterevidence:** Sources are compressed to domains or source families; no source titles, dates, access dates, evidence spans, search method, or active counterevidence search. Repeated high-confidence labels are not justified.

**Decision:** **Revise.**

**Smallest corrective action:** Create an atomic claim register with exact source metadata, claim type, confidence reason, limitation, and falsifier; downgrade unsupported high-confidence claims.

**Falsifier/update trigger:** A complete independent claim register showing direct support for the current high-confidence claims would change this rating; re-evaluate when the source list or workflow scope changes.

### 2. `C.md`

**Research question and intended use:** Map the current research-to-data capability landscape across roles, technologies, software, companies, products, methodologies, workflows, and agents.

**Scope:** Very broad; declares a September 2026 snapshot, but geography, population, and inclusion rules vary by lens.

**Gate results:** A Partial; B Fail; C Fail; D Fail; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Stable definitions of tools and workflow stages | Documented fact / inference | Generally useful, but often supported by grouped sources | Medium |
| Product, market, and adoption comparisons | Reported signal / inference | Mostly secondary roundups and vendor material; source independence is unclear | Low |
| Entity and relationship candidates | Recommendation | Strong modeling utility, not direct empirical evidence | Medium |

**Strengths:** Broad organization; explicit evidence categories in many sections; identifies bias, gaps, and falsifiers; useful workflow and entity tables.

**Limitations and counterevidence:** The 79-source list is heavily secondary; exact claim-to-source alignment is inconsistent; repeated secondary reporting may share an original source; search and deduplication methods are absent.

**Decision:** **Revise.**

**Smallest corrective action:** Split stable capability claims from volatile market and product claims, then attach exact dated sources and claim-level confidence to every volatile claim.

**Falsifier/update trigger:** Independent primary and benchmark evidence that corroborates the major market and product claims would raise the rating; re-evaluate when the September 2026 snapshot becomes outdated.

### 3. `CNE DPS 4.1 F.md`

**Research question and intended use:** Consolidate the research-to-data capability cluster into an evidence-grounded, modeling-ready result with workflow, provenance, entities, predicates, and a proposed DuckDB model.

**Scope:** Broad twelve-stage workflow and all major capability lenses. Scope and intended use are explicit; some boundaries are design recommendations rather than empirically tested decisions.

**Gate results:** A Partial; B Partial; C Partial; D Partial; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Standards, product capabilities, and workflow controls | Documented fact / inference | Strong primary anchors; dense tables still need atomic evidence locators | High to medium |
| Role boundaries and workflow archetypes | Inference | Reasonable synthesis with limited independent corroboration | Medium |
| Proposed claim contract, schema, and predicates | Recommendation | Useful design, not an empirical finding | Medium |
| Current versions, market, and reliability claims | Reported signal / inference | Volatile, partially verified, and sometimes carried from prior notes | Low to medium |

**Strengths:** Best overall source mix; explicit claim classes, falsifiers, limitations, time sensitivity, change log, entity model, and human verification responsibilities.

**Limitations and counterevidence:** Exact searches, inclusion rules, and complete claim-by-claim extraction ledger are absent; carried sources are not always separated from freshly verified sources; some prose combines fact, inference, and recommendation; the Polars release-candidate status needs correction.

**Decision:** **Revise before promotion.**

**Smallest corrective action:** Complete the promised claim/evidence table with exact locators and contradicting evidence, separate carried from verified sources, and correct release-status language.

**Falsifier/update trigger:** A completed evidence ledger with no material unsupported claims would change this rating; re-evaluate after any version-sensitive source or schema change.

### 4. `CP L6.md`

**Research question and intended use:** Explain ETL, ELT, and federation and their governance and workflow consequences for analytical data systems.

**Scope:** Narrow and coherent; centered on BigQuery, Snowflake, Databricks, and dbt, with analytical warehouses and lakehouses as context.

**Gate results:** A Pass; B Partial; C Pass; D Partial; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| ETL, ELT, federation, loading, and governance definitions | Documented fact | Direct first-party documentation | High |
| Platform-specific capabilities and controls | Documented fact | Strong for the named products and versions | High |
| General cost, productivity, or architecture preference | Inference / recommendation | Vendor evidence is not independent comparative evidence | Medium |

**Strengths:** Specific question; authoritative sources; clear distinctions; useful treatment of raw versus trusted data, replay, schema drift, privacy, access, and cost controls; avoids universal ELT claims.

**Limitations and counterevidence:** Sources are vendor-dependent; search method and independent countersearch are absent; role and trade-off generalizations sometimes exceed the documentation.

**Decision:** **Accept with limitations.**

**Smallest corrective action:** Add the search scope and a counterevidence table covering ETL, federation, pre-load redaction, residency, and cost constraints.

**Falsifier/update trigger:** Independent evidence showing that the named platform documentation materially misstates the described behavior would lower confidence; re-evaluate after platform or dbt version changes.

### 5. `DC L5.6.md`

**Research question and intended use:** Model the research-to-data capability cluster as distinct skills, entities, workflows, tools, and provenance relationships.

**Scope:** Broad architectural reference covering the full workflow, nine lenses, provenance, and a proposed claim-centric relational core.

**Gate results:** A Partial; B Partial; C Partial; D Fail; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| PROV, DCAT, JSON Schema, and named tool definitions | Documented fact | Strong standards and official documentation | High |
| Role, workflow, and tool-boundary synthesis | Inference | Useful, but not fully atomized or independently corroborated | Medium |
| Proposed relational or graph model | Recommendation | Coherent design recommendation | Medium |

**Strengths:** Excellent entity separation; treats provenance as cross-cutting; explicitly warns against overclaiming from official documentation; useful schema recommendation.

**Limitations and counterevidence:** No search or selection method; exact evidence spans are missing; official docs support some comparative conclusions they cannot establish; the proposed model is not populated or tested.

**Decision:** **Revise.**

**Smallest corrective action:** Mark each entity row by claim type and attach a specific source or derivation; remove unsupported high-confidence comparative claims.

**Falsifier/update trigger:** Exact source spans that support the comparative and role-boundary claims would raise the rating; re-evaluate if the proposed model is implemented and tested.

### 6. `DPS.md`

**Research question and intended use:** Identify the research-to-data capability components and how they combine into a workflow.

**Scope:** Broad atlas including roles, technologies, products, companies, methodologies, agents, extraction, and data-warehouse automation.

**Gate results:** A Partial; B Partial; C Partial; D Fail; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Standards, academic extraction, and agent research | Documented fact | Generally strong primary or authoritative sources | High to medium |
| Product capability and package existence | Documented fact | Sources establish existence or advertised behavior | Medium to high |
| Performance, role, market, and end-to-end workflow conclusions | Inference | Often broader than the cited source | Low to medium |

**Strengths:** Better primary and academic foundation than most broad drafts; useful agent and workflow tables; provenance is treated as a central risk.

**Limitations and counterevidence:** Source classifications sometimes confuse product authority with performance evidence; exact passages, search procedure, and active counterevidence are absent; entity rows lack stable source spans and dates.

**Decision:** **Revise.**

**Smallest corrective action:** Audit the entity table row by row and replace source categories with exact citations, claim types, dates, and confidence reasons.

**Falsifier/update trigger:** Independent evidence contradicting the cited academic or standards-based findings would lower confidence; re-evaluate once the entity audit and method record are complete.

### 7. `FAI.md`

**Research question and intended use:** Explain how research, data engineering, analytics, knowledge engineering, and agent systems combine into a research-to-data loop.

**Scope:** Full workflow and nine lenses, with emphasis on analytics engineering, DuckDB, provenance, agents, and role boundaries.

**Gate results:** A Partial; B Partial; C Partial; D Fail; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Stable technology and workflow definitions | Documented fact / inference | Reasonably supported by official documentation | Medium to high |
| Role distinctions | Inference / reported signal | Mixed official and career sources; boundaries remain contextual | Medium |
| Market, adoption, and agent reliability claims | Reported signal / inference | Secondary and vendor evidence dominates | Low to medium |

**Strengths:** Clear claim taxonomy; useful role distinctions; good tool-boundary explanations; includes falsifiability, gaps, and recommendations.

**Limitations and counterevidence:** Inline and grouped citations are inconsistent; vendor descriptions are sometimes labeled as facts; search, extraction, and systematic counterevidence methods are absent.

**Decision:** **Revise.**

**Smallest corrective action:** Convert source groups into an atomic claim table and reclassify vendor descriptions as reported signals unless independently corroborated.

**Falsifier/update trigger:** Independent role, market, or agent-reliability evidence that supports the current generalizations would raise the rating; re-evaluate when current product or role claims change.

### 8. `G0.md`

**Research question and intended use:** Identify major entities, workflow stages, and technology choices in research-to-data systems for graph or relational modeling.

**Scope:** Broad architecture-oriented atlas covering workflow, roles, tools, methodologies, companies, products, and agents.

**Gate results:** A Partial; B Partial; C Fail; D Fail; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Standard definitions and official tool capabilities | Documented fact | Usually supported by authoritative sources | High to medium |
| Role and workflow synthesis | Inference | Useful but not consistently atomically cited | Medium |
| Comparative tool maturity and market conclusions | Inference / reported signal | Secondary evidence and blank source cells weaken support | Low to medium |

**Strengths:** Clear entity types and workflow roles; good provenance and ETL/ELT treatment; includes alternatives, gaps, and falsifiers.

**Limitations and counterevidence:** Search method and source deduplication are absent; comparison tables contain blank or grouped source cells; high-confidence labels sometimes exceed support.

**Decision:** **Revise.**

**Smallest corrective action:** Fill every blank or grouped source cell with exact citations and add a limitation or counterexample for each major comparison.

**Falsifier/update trigger:** Complete claim-to-source alignment with credible counterexamples would raise the rating; re-evaluate if the entity taxonomy or tool comparisons change.

### 9. `G1.md`

**Research question and intended use:** Describe the structure and well-formedness model of nanopublications for atomic claims, provenance, and publication metadata.

**Scope:** Narrow technical note covering the four named graphs, TriG, Trusty URIs, multi-source provenance, querying, and workflow placement.

**Gate results:** A Partial; B Partial; C Partial; D Fail; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Four-graph nanopublication structure and core predicates | Documented fact | Directly grounded in the official guideline | High |
| Working-draft status and optional multi-source extension | Documented fact / inference | Source is authoritative but version and maturity need recording | Medium to high |
| Ecosystem maturity or typical usage | Inference | Not established by the focused source | Medium to low |

**Strengths:** Focused, coherent, concrete TriG example, clear provenance distinction, and useful well-formedness requirements.

**Limitations and counterevidence:** Guideline version, publication date, access date, exact sections, independent validation, and comparison with alternatives are absent.

**Decision:** **Accept with limitations.**

**Smallest corrective action:** Add versioned source metadata, exact section references, and a validation checklist or machine-readable test for required graph relationships.

**Falsifier/update trigger:** A newer guideline that changes the four-graph structure or required predicates would lower confidence; re-evaluate on guideline version or namespace changes.

### 10. `G2.md`

**Research question and intended use:** Explain what PROV-K adds to W3C PROV and nanopublications for multi-source knowledge provenance.

**Scope:** Focused on PROV-K classes, properties, truth values, reliability, trust relationships, deployment, and maturity.

**Gate results:** A Partial; B Pass; C Partial; D Fail; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| PROV-K classes, properties, and relation to PROV-O/SKOS | Documented fact | Official ontology sources and peer-reviewed source | High |
| Truth values, trust, and reliability vocabulary | Documented fact / inference | Strong source basis; exact ontology semantics should be checked | High to medium |
| Deployment scale and ecosystem maturity | Reported signal / inference | Direct verification and independent evidence are limited | Medium to low |

**Strengths:** Excellent source quality; focused scope; systematic conceptual grouping; explicitly notes ontology and tooling limitations.

**Limitations and counterevidence:** No search or ontology-testing procedure; exact source sections are not mapped to every class/property; alternatives such as plain PROV and nanopublications are named but not systematically compared.

**Decision:** **Accept with limitations.**

**Smallest corrective action:** Add exact ontology version and URI references plus a claim table and competency-question or validation test.

**Falsifier/update trigger:** A versioned ontology release that changes the cited class or property semantics would lower confidence; re-evaluate when deployment or maturity evidence is updated.

### 11. `G3.md`

**Research question and intended use:** Compare nanopublications and PROV-K for provenance of individual and aggregated research claims.

**Scope:** Covers structure, provenance extensions, serialization/tooling, workflow placement, strengths, limitations, alternatives, and confidence.

**Gate results:** A Partial; B Pass; C Partial; D Fail; E Partial; F Pass.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Standard nanopublication structure and PROV-K relationship | Documented fact | Strong official and peer-reviewed sources | High |
| Atomicity, support/conflict, trust, and immutability | Inference / documented fact | Well aligned for core concepts | High to medium |
| Adoption scale, tooling breadth, and maturity ranking | Reported signal / inference | Several claims lack named source support | Medium to low |

**Strengths:** Clear standard-versus-extension distinction; useful treatment of support, conflict, truth, trust, immutability, alternatives, and workflow placement.

**Limitations and counterevidence:** Search and comparative method are absent; broad ecosystem claims are under-sourced; versioned source IDs and implementation validation are missing.

**Decision:** **Accept with limitations.**

**Smallest corrective action:** Source or remove broad adoption claims and add versioned metadata plus a comparison table for standard nanopublication, PROV, and PROV-K.

**Falsifier/update trigger:** Evidence showing that the standard-versus-extension distinctions are technically incorrect would lower confidence; re-evaluate when ontology, tooling, or adoption evidence changes.

### 12. `OP MS 1.3F.md`

**Research question and intended use:** Compare tools, roles, standards, workflows, and agents in the research-to-data capability stack for atlas and modeling use.

**Scope:** Very broad, including current versions, benchmarks, BI, extraction, provenance, GraphRAG, agents, companies, products, and market signals.

**Gate results:** A Partial; B Partial; C Partial; D Fail; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Standards and stable tool capabilities | Documented fact | Strong primary anchors | High to medium |
| Role and workflow synthesis | Inference | Useful but broad and unevenly sourced | Medium |
| Benchmarks, versions, market, and adoption | Reported signal / inference | Hardware, version, source, and method details are incomplete | Low to medium |

**Strengths:** Good `[F]/[S]/[I]/[R]` discipline; practical workflow map; strong DuckDB, provenance, and agent-verification distinctions.

**Limitations and counterevidence:** Benchmark and quantitative methods are absent; several sources were not opened; grouped citations do not fully support table rows; version-sensitive facts can expire.

**Decision:** **Revise.**

**Smallest corrective action:** Create a ledger for every quantitative, market, and version-sensitive statement with hardware/version, exact locator, counterevidence, confidence, and expiry trigger.

**Falsifier/update trigger:** Reproducible benchmark results or primary market evidence that supports the current magnitudes would raise the rating; re-evaluate when versions or benchmark conditions change.

### 13. `Q.md`

**Research question and intended use:** Examine browser automation, ontology, provenance, local analytics, and specialized roles in research-to-data workflows.

**Scope:** Focused on VLM/browser extraction and agent workflows, but extends into broad regulatory and market claims.

**Gate results:** A Partial; B Fail; C Fail; D Fail; E Partial; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Existence and advertised design of Skyvern and PROV-AGENT | Documented fact | First-party or named technical sources support existence/design | High to medium |
| Browser-agent extraction reliability or superiority | Inference / reported signal | Vendor and benchmark claims lack controlled independent comparison | Low |
| Regulatory necessity, market fragmentation, or displacement of traditional scraping | Inference | Strong wording exceeds the evidence described | Low |

**Strengths:** Clear browser-automation boundary; good treatment of deterministic fallbacks, schema validation, human review, state, handoffs, and failure modes.

**Limitations and counterevidence:** Vendor sources dominate reliability claims; no controlled benchmark, longitudinal evaluation, search method, or selector-based comparison is recorded.

**Decision:** **Revise.**

**Smallest corrective action:** Replace superiority and regulatory language with qualified signals, then add a controlled comparison plan or results against selector-based extraction.

**Falsifier/update trigger:** A controlled, independent comparison showing durable superiority over selector-based extraction would raise confidence; re-evaluate when browser-agent versions or regulatory sources change.

### 14. `Citations/Citation.md`

**Research question and intended use:** Register citations in the raw corpus and classify them as primary, secondary, or mixed for source-quality support.

**Scope:** Citation inventory for most substantive raw documents. It is an audit artifact, not substantive evidence for the atlas claims.

**Gate results:** A Partial; B Partial; C Fail; D Partial; E Fail; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Broad source classification pattern | Inference | Useful directional classification | Medium |
| Completeness of the inventory | Documented fact claim | Fails because `CNE DPS 4.1 F.md` and `Report.md` are absent from the audit | Low |
| Primary-source classification | Recommendation / inference | Too coarse where a source is primary only for capability, not performance or adoption | Medium to low |

**Strengths:** Centralizes source classification; makes secondary-source burden visible; highlights repeated sources and focused notes.

**Limitations and counterevidence:** No claim verification; incomplete corpus; no documented deduplication or adjudication method; withdrawn, inaccessible, or contradictory sources are not systematically checked.

**Decision:** **Revise.**

**Smallest corrective action:** Add every raw document, assign stable source IDs, distinguish capability from performance/adoption authority, and document duplicate handling.

**Falsifier/update trigger:** A complete inventory and independently reproducible classification audit would raise the rating; re-evaluate whenever files or source classifications change.

### 15. `Citations/Report.md`

**Research question and intended use:** Assess source mix across raw documents and prioritize documents for further use.

**Scope:** Cross-document citation-quality audit and ranking, not substantive research about the capability atlas.

**Gate results:** A Partial; B Partial; C Fail; D Partial; E Fail; F Partial.

**Material claim review:**

| Claim area | Type | Evidence status | Confidence |
| --- | --- | --- | --- |
| Relative ranking of source quality across documents | Inference | Directionally useful and consistent with the corpus | Medium |
| Exact counts, percentages, and totals | Documented fact / inference | Cannot be reconciled until the file inventory and counting rules are complete | Low to medium |
| Claim accuracy of ranked documents | Inference | Not established by source classification alone | Low |

**Strengths:** Useful corpus-level prioritization; correctly identifies strong focused notes and weak broad source mixes; distinguishes source quality from claim quality in part.

**Limitations and counterevidence:** Inherits the incomplete registry; arithmetic, duplicate handling, mixed-source treatment, and internal-note treatment are not fully reproducible; no claim-source alignment or contradictory-evidence review.

**Decision:** **Revise.**

**Smallest corrective action:** Rebuild from a complete inventory with stable IDs, explicit deduplication and counting rules, separate capability/performance/adoption classifications, and reconciled totals.

**Falsifier/update trigger:** Reconciled totals that remain materially different from this report would invalidate its quantitative rankings; re-evaluate after the citation registry is rebuilt.

## Priority next actions

1. Build one complete claim/evidence ledger for `CNE DPS 4.1 F.md`, using the focused notes as source material but not independent corroboration.
2. Add a reproducible method record to the ledger: search scope, inclusion and exclusion rules, source-opening log, extraction method, and counterevidence search.
3. Repair `Citations/Citation.md` and `Citations/Report.md` from the complete raw-file inventory before using their counts.
4. Verify the focused provenance notes against versioned ontology and guideline identifiers, exact sections, and small validation tests.
5. Reassess volatile claims separately from stable definitions: product versions, benchmarks, adoption, market claims, regulatory claims, and agent reliability.
6. Promote only claims that pass claim-level provenance and confidence review; retain document-level limitations with every promoted result.

## Final evaluation

The corpus is valuable working research, but it is not uniformly ready for processed use. The first promotion candidates are `CP L6.md`, `G1.md`, `G2.md`, and `G3.md`, all with the limitations recorded above. The broad atlas documents should be treated as synthesis drafts until their claims are atomized, their evidence is mapped, and their methods are reproducible.
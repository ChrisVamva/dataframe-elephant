# BrainstormingBased_on_Novelty_NR2.md — External Brainstorming Session

## Session Metadata

- **Session Date:** 2026-10-03
- **Protocol Applied:** FreeBrainstorming.md (`Rules and Regulations/Protocols/FreeBrainstorming.md`)
- **Session Focus:** New research subject ideation — external, universal, cross-domain framing
- **Projection Check:** No internal project references used as analytical focus; project treated as a non-existent observer. No ideas require internal project changes to be implemented.
- **De-duplication vs. prior sessions:** New Research/1 (prompt-template effectiveness, citation-pipeline quality, notebook portability) and New Research/2 (agentic-AI observability, zero trust for non-human actors, SBOM/agent coupling, compliance evidence) are excluded as already covered. NR2 deliberately opens *different* external domains.
- **Reviewer Access (simulated blind review):** All references are external literature, standards bodies, and 2025–2026 industry/policy reports.

---

## 1. External Frame of Reference — Cross-Domain Trigger Map

Per Protocol §1 (Topic Generation, External Focus). 7 external domains, none overlapping prior sessions.

| # | Domain | Trigger Source (2025–2026) | Universal Problem Introduced |
|---|--------|---------------------------|------------------------------|
| 1 | **Research infrastructure / metascience** | WEF "Top 10 Emerging Technologies of 2026" (Jun 2026) replaced its expert survey with an AI-based nomination workflow built by Frontiers | Expert-deliberation processes for identifying research priorities are being replaced by AI curation, with no universal audit method for the replacement |
| 2 | **Science communication / information integrity** | Issues in Science & Technology Winter 2026 ("polluted information ecosystems"); bioRxiv preprint-ecosystem study (Mar 2026) on evaluation penalties | Evidence consumed by policymakers increasingly originates in unreviewed or AI-generated channels; provenance decays faster than verification practices evolve |
| 3 | **Climate × Health** | Nexa Initiative (Grand Challenges Canada + Science for Africa) 2026 calls on climate-driven health; InterAcademy Partnership Climate Change & Health programme | Health systems face compounding climate stressors, but resilience indicators are not comparable across countries or transferable across sectors |
| 4 | **Research policy / funding models** | Liberal Currents "Seeing Like a Gardener" (Sep 2026) on people-not-projects funding; documented contraction of pandemic-preparedness R&D investment (2026 implementation reports) | Funding-model design (milestone challenge programs vs. long-term investigator support) lacks a comparative effectiveness evidence base |
| 5 | **Health technology / regulation** | Frost & Sullivan 2026 outlook: AI-enabled platforms, connected medical devices, robotics; GAO-26-108079 (Apr 2026) "Three S&T Trends That Could Affect Society" | Regulatory review capacity is diverging from the deployment rate of adaptive, self-updating AI medical technology |
| 6 | **Energy transition policy** | Germany's 7th Energy Research Programme as a model grand-challenge programme | National energy-transition programs generate evaluation claims that are rarely falsifiable or comparable across jurisdictions |
| 7 | **One Health / environmental security** | One Health frameworks (human–animal–environmental health) cited as the model for global health security; environmental hazards as conflict drivers | Cross-sector indicator frameworks (One Health) have no universal data-interoperability contract between human, veterinary, and environmental data systems |

---

## 2. Universal Problems — 16 Cross-Domain Observations (No Internal Projection)

Per Protocol §1 (Universal Problems, 10–20 items). Each stated as if this repository never existed.

1. **AI-curated priority setting:** When an AI nomination workflow replaces expert surveys for selecting "top technologies," the criteria, training data, and bias profile of the curator are opaque; no standard exists for auditing AI-made research agendas.
2. **Evidence provenance decay:** A claim cited by a policymaker may trace to a preprint, an AI-generated summary, or a retracted paper; provenance chains break faster than they can be verified manually.
3. **Evaluation penalties in preprints:** The bioRxiv (Mar 2026) study shows faster dissemination but measurable evaluation penalties — career incentives still reward journal placement over open early review.
4. **Pandemic-preparedness investment volatility:** Global medical-countermeasure R&D funding contracts between crises; no portable framework evaluates the opportunity cost of stop-start funding.
5. **Climate-health indicator incomparability:** Countries report health-system climate resilience with locally defined indicators; cross-country comparison and cross-sector transfer (e.g., to infrastructure planning) are ad hoc.
6. **Funding-model folklore:** "People, not projects" vs. milestone-based challenge programs is argued anecdotally; there is no controlled, cross-disciplinary comparison of outcomes per funding model.
7. **Adaptive AI medical devices outpace review:** Self-updating diagnostic models invalidate the fixed-label regulatory model; post-market surveillance designs for adaptive systems are unsettled.
8. **Energy-program evaluation claims are unfalsifiable:** National energy research programmes publish success narratives, but counterfactual baselines ("what would have happened without the programme") are rarely constructed.
9. **One Health data silos:** Human, animal, and environmental health data systems use incompatible identifiers, update cadences, and privacy regimes — the framework's promise exceeds its data plumbing.
10. **Grand-challenge education is unmeasured:** Interdisciplinary degree programs aimed at grand challenges (climate, inequality, conflict) report enthusiasm, not outcomes; no longitudinal effectiveness evidence exists.
11. **Healthcare's own climate footprint:** If healthcare were a country it would rank ~5th in emissions; sustainable prescribing and low-carbon care pathways lack standardized measurement.
12. **GAO's horizon-scan gap:** GAO (Apr 2026) flags societal-impact assessment of emerging S&T trends, but the assessment methods used by legislatures remain qualitative and non-replicable.
13. **Cross-domain evidence schemas:** Disciplines encode "evidence strength" differently (GRADE in medicine, AeroMAP in policy, TRL in engineering); a universal evidence-grading interlingua does not exist.
14. **Retraction latency vs. citation persistence:** Retracted or superseded findings continue circulating in downstream documents for years; automated propagation of corrections is not implemented anywhere at scale.
15. **AI-generated literature contamination:** Synthetic text enters the citable record (paper mills, LLM-written reviews); detection is adversarial and no field has a contamination-rate baseline.
16. **Replication of policy evaluations:** Evidence-based policy borrows RCT methods from development economics, but policy interventions are rarely replicated; external-validity checks remain informal.

---

## 3. Problem Reframing (Protocol §2)

- Internal context removed: all 16 problems above are phrased for "a research funder," "a health ministry," "a standards body," or "a national academy" — never for this project.
- External benchmarks used: GRADE (medicine), FAIR principles (data), TRL (engineering), Cochrane reviews, FEMA ICS analogies only where universally accepted.
- Scope-creep guard: no idea is framed as "how would this project do it differently."

---

## 4. Candidate Research Subjects (Protocol §3 — Solution Exploration)

Each candidate passed the generalization test: "Would this work for a hospital, a bank, and a transportation authority simultaneously?" Only subjects with an existing external literature anchor were retained.

### Subject A — Auditing AI-Curated Research Agendas

**Universal problem:** #1, #13, #15.
**Research question:** When an AI-based nomination workflow replaces expert deliberation for research-priority setting, what audit criteria (bias profile, criteria transparency, stability under re-runs, coverage vs. human baselines) make the substitution legitimate?
**External anchors:** WEF/Frontiers 2026 methodology; literature on group deliberation vs. statistical aggregation (Surowiecki, Condorcet jury theorem); emerging AI-governance audit standards (NIST AI RMF).
**Methodology (borrowed/adapted):** Adversarial audit design from security engineering; agreement statistics (Krippendorff's alpha) from content analysis; re-run stability testing from ML reproducibility.
**Expected impact:** A reusable audit checklist any funder, journal, or national academy can apply before delegating priority-setting to AI.
**Limitations:** Scope bounded to priority-setting processes; no internal dependencies.

### Subject B — Evidence Provenance Chains for the AI-Generated Literature Era

**Universal problem:** #2, #14, #15.
**Research question:** How do citation provenance chains degrade when intermediate layers (AI summaries, preprints, press releases) sit between the original finding and the citing document, and what lightweight verification protocol restores trust?
**External anchors:** bioRxiv Mar 2026 preprint-ecosystem study; Retraction Watch data; Issues in Science & Technology Winter 2026; W3C PROV standard.
**Methodology:** Longitudinal citation-chain tracing (bibliometrics); contamination sampling; propagation modeling from epidemiology (R0 of a bad claim).
**Expected impact:** A quantified "provenance decay rate" plus a verification protocol applicable by publishers, libraries, or fact-checking organizations.
**Limitations:** Deliberately domain-agnostic — testable on any citing corpus.

### Subject C — Comparative Effectiveness of Research Funding Models

**Universal problem:** #4, #6.
**Research question:** Under matched disciplinary conditions, do "people, not projects" grants outperform milestone-based challenge programs on output quality, retention, and direction-change responsiveness?
**External anchors:** Liberal Currents "Seeing Like a Gardener" (Sep 2026); HHMI Investigator program (people) vs. DARPA-style challenge programs (milestones) as natural experiments; pandemic-preparedness funding contraction as the volatility case.
**Methodology:** Difference-in-differences across funder cohorts; matched-control design from program evaluation.
**Expected impact:** A decision framework for funders choosing a portfolio mix; reusable by any national funder regardless of field.
**Limitations:** Requires funder cooperation for outcome data; bounded to research funding, not project management generally.

### Subject D — Portable Climate-Resilience Indicators for Health Systems

**Universal problem:** #5, #11.
**Research question:** Can a minimal, country-agnostic indicator set for health-system climate resilience be defined so that a hospital network, a ministry, and an insurer all score the same system comparably?
**External anchors:** InterAcademy Partnership Climate Change & Health; WHO climate-resilient health system framework; Nexa Initiative 2026 calls; healthcare-emissions literature.
**Methodology:** Indicator harmonization from composite-index construction (OECD/JRC handbook); Delphi panel + psychometric validation.
**Expected impact:** A versioned indicator specification with a published scoring rubric — implementable without any particular data platform.
**Limitations:** Validation requires real health-system data; scope excludes climate mitigation policy itself.

### Subject E — Post-Market Surveillance Design for Adaptive Medical AI

**Universal problem:** #7, #12.
**Research question:** What surveillance design (event triggers, performance drift metrics, rollback criteria) lets regulators approve self-updating diagnostic AI without a fixed-label review?
**External anchors:** GAO-26-108079 (Apr 2026); FDA's evolving adaptive-AI guidance; EU AI Act high-risk provisions; connected-device literature (Frost & Sullivan 2026).
**Methodology:** SPC (statistical process control) charts from manufacturing; pharmacovigilance signal-detection adapted to model performance.
**Expected impact:** A surveillance blueprint transferable to any high-stakes adaptive system (also finance and transportation), not only medical devices.
**Limitations:** Regulatory acceptance is a policy question; the deliverable is the design, not the adoption.

---

## 5. Ranking Table

| Rank | Subject | Novelty | Cross-domain applicability | Evidence base availability | Reproducibility | Composite |
|------|---------|---------|---------------------------|---------------------------|-----------------|-----------|
| 1 | **B — Evidence provenance chains** | High (2026-relevant, contested) | Very high (any citing domain) | High (public bibliometric + retraction data) | Very high (method is public data + protocol) | **Top pick** |
| 2 | **A — Auditing AI-curated agendas** | Very high (2026 first-mover) | High (funders, journals, agencies) | Medium (methodology disclosures are thin) | High (audit protocol is the deliverable) | Strong |
| 3 | **D — Climate-health indicators** | Medium (active field) | Very high | Medium (fragmented national data) | Medium (Delphi-dependent) | Solid |
| 4 | **C — Funding-model effectiveness** | Medium (long-debated, rarely measured) | High (all research funders) | Low–medium (funder data access is the bottleneck) | Medium | Worthwhile |
| 5 | **E — Adaptive medical AI surveillance** | High | Medium–high (transfers to finance/transport) | Medium (regulatory dockets are public) | Medium | Worthwhile |

---

## 6. Exit Criteria Check (Protocol §Exit Criteria)

- ✅ Every idea (§4) has at least one external reference point (publication, standard, industry practice).
- ✅ No idea requires internal project changes to be implemented — all five are implementable by any team with public or obtainable data.
- ✅ Each idea is understandable by someone unfamiliar with this project (§4 formulations are self-contained).

## 7. Recommended Next Steps (External)

1. Choose one subject (ranking suggests **B**, with **A** as the strongest novelty alternative).
2. Promote the chosen subject into the numbered research-folder skeleton (`00_Index…99_Archive`) with an S## source register per the house research-folder conventions.
3. Build the Stage-1 source register: for **B**, seed with Retraction Watch, bioRxiv Mar 2026 study, W3C PROV, Issues in Science & Technology Winter 2026; for **A**, seed with the WEF/Frontiers 2026 methodology page and NIST AI RMF.

---

**Protocol Status:** FreeBrainstorming.md applied; external-only deliverables.
**Internal Project Impact:** None required; session notes are self-contained for any external team.

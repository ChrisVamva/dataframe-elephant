# Research concepts from current policy shifts

**Date:** 10 October 2026  
**Scope:** Consumer products, labor, global health, and public infrastructure  
**Baseline:** No published-article catalog was supplied; earlier NR2–NR4 ideas were checked.  
**Self-check:** 6/6

## External domains

- Consumer product law
- Circular economy and industrial design
- Labor economics and workplace rights
- Global health governance
- Energy-system planning
- Drinking-water infrastructure
- Regulatory evaluation

## Signal feed

- **S01 — Repair Directive:** [Directive (EU) 2024/1799](https://eur-lex.europa.eu/eli/dir/2024/1799/oj/eng), adopted 13 June 2024. Member States must transpose it by 31 July 2026.
- **S02 — Data Act:** [Regulation (EU) 2023/2854](https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng), adopted 13 December 2023. It applies from 12 September 2025.
- **S03 — Ecodesign framework:** [Regulation (EU) 2024/1781](https://eur-lex.europa.eu/eli/reg/2024/1781/oj/eng), adopted 13 June 2024. It establishes a framework for product-specific sustainability requirements.
- **S04 — Packaging rules:** [Regulation (EU) 2025/40](https://eur-lex.europa.eu/eli/reg/2025/40/oj/eng), adopted 19 December 2024. Most provisions apply from 12 August 2026.
- **S05 — Platform Work Directive:** [Directive (EU) 2024/2831](https://eur-lex.europa.eu/eli/dir/2024/2831/oj/eng), adopted 23 October 2024. National transposition is due by 2 December 2026.
- **S06 — Pay Transparency Directive:** [Directive (EU) 2023/970](https://eur-lex.europa.eu/eli/dir/2023/970/oj/eng), adopted 10 May 2023. National transposition was due by 7 June 2026.
- **S07 — International Health Regulations amendments:** [WHA77.17](https://apps.who.int/gb/ebwha/pdf_files/WHA77/A77_R17-en.pdf), adopted 1 June 2024.
- **S08 — WHO Pandemic Agreement:** [WHA78.1](https://apps.who.int/gb/ebwha/pdf_files/WHA78/A78_R1-en.pdf), adopted 20 May 2025.
- **S09 — Transmission planning:** [FERC Order No. 1920](https://www.ferc.gov/news-events/news/ferc-strengthens-electric-transmission-planning), issued 13 May 2024. It requires regional planning over at least a 20-year horizon.
- **S10 — Lead-pipe replacement:** [EPA Lead and Copper Rule Improvements](https://www.epa.gov/ground-water-and-drinking-water/lead-and-copper-rule-improvements), finalized 8 October 2024. As finalized, it generally required replacement within ten years.

## Repair rights vs. manufacturer data control

The Data Act grants users access to connected-product data. Repair law creates a separate right to have covered goods repaired. Their practical overlap is still an empirical question.

```yaml
concept_id: C01
concept: "Test whether repair shops can diagnose connected appliances without manufacturer-controlled data after the EU Data Act begins applying."
anchor: "The Data Act application date of 12 September 2025, followed by the Repair Directive transposition deadline of 31 July 2026."
anchor_source: "S01 (31 July 2026); S02 (12 September 2025)"
why_now: "The Data Act applies from September 2025, while Member States must transpose the Repair Directive by July 2026."
tension: "Users gain data access and repair rights, but manufacturers still control many diagnostic tools."
evidence_trail: "EU legal texts, national transposition laws, repair-shop interviews, and repair records for connected appliances."
domain: "Consumer product law"
novelty_check: "orthogonal — tests operational overlap between two rights"
rubric: {specificity: 3/3, tension: 3/3, evidence: 3/3, novelty: 2/3}
```

- **External context:** The Data Act and Repair Directive provide the legal benchmarks. No common public measure links product-data access to successful repairs.
- **Method:** Compare diagnostic access, repair time, cost, and completion across independent and authorized repair shops.
- **Impact:** Consumer agencies can distinguish data barriers from parts shortages.
- **Boundary:** Limit the study to connected appliances and jurisdictions with observable repair records.

The ecodesign framework and repair rules also offer a way to test whether product durability translates into repairs rather than replacement.

```yaml
concept_id: C02
concept: "Pair EU ecodesign requirements with repair outcomes to test whether durability rules lead consumers to repair rather than replace covered goods."
anchor: "Regulation (EU) 2024/1781 and the 31 July 2026 national transposition deadline for Directive (EU) 2024/1799."
anchor_source: "S01 (31 July 2026); S03 (13 June 2024)"
why_now: "The ecodesign framework is in force, and the 2026 repair-law deadline puts product requirements beside a new repair obligation."
tension: "Product rules can promise durability without showing whether consumers can obtain or choose repair."
evidence_trail: "Product-specific ecodesign rules, repair offers, consumer surveys, and completed repair records."
domain: "Circular economy and industrial design"
novelty_check: "orthogonal — connects product rules to repair behavior"
rubric: {specificity: 3/3, tension: 2/3, evidence: 2/3, novelty: 2/3}
```

- **External context:** Ecodesign rules and repair obligations are established policy tools. A shared test of rules against completed repairs remains useful.
- **Method:** Link product requirements, repair offers, and completion records for goods covered by both regimes.
- **Impact:** Regulators can see whether product rules change consumer choices.
- **Boundary:** Include only product categories with applicable requirements and comparable repair data.

## Platform flexibility vs. pay transparency

Platform-work rules address algorithmic management. Pay-transparency rules address access to pay information and equal-pay enforcement. Their overlap is testable in wage setting and worker appeals.

```yaml
concept_id: C04
concept: "Measure whether platform workers can challenge algorithmic pay penalties using the EU's new platform-management and pay-transparency rights."
anchor: "The 7 June 2026 pay-transparency deadline and the 2 December 2026 Platform Work Directive deadline."
anchor_source: "S05 (2 December 2026); S06 (7 June 2026)"
why_now: "The pay-transparency deadline passed in June 2026, months before the platform-work transposition deadline."
tension: "Platforms can change pay through automated systems, while workers may lack usable reasons or appeal routes."
evidence_trail: "National implementing laws, labor-platform decisions, worker appeals, and published pay disclosures."
domain: "Labor economics and workplace rights"
novelty_check: "orthogonal — examines algorithmic pay appeals"
rubric: {specificity: 3/3, tension: 3/3, evidence: 2/3, novelty: 2/3}
```

- **External context:** The two directives set distinct benchmarks for algorithmic management and equal-pay information.
- **Method:** Compare national laws and documented appeal outcomes for automated pay adjustments.
- **Impact:** Worker organizations and labor regulators can target opaque wage reductions.
- **Boundary:** Limit the analysis to EU jurisdictions and platform workers with documented pay decisions.

Employment classification may also decide who can use these new pay protections.

```yaml
concept_id: C05
concept: "Map when disputed employment status blocks platform workers from accessing equal-pay protections under two new EU labor directives."
anchor: "The 2026 transposition deadlines in Directives (EU) 2023/970 and (EU) 2024/2831."
anchor_source: "S05 (2 December 2026); S06 (7 June 2026)"
why_now: "Both directives set 2026 transposition deadlines, bringing platform status rules and pay-disclosure coverage into national legislation."
tension: "A worker may perform platform work yet remain outside protections tied to employee status."
evidence_trail: "National transposition laws, labor-court decisions, equality-body guidance, and platform work contracts."
domain: "Labor economics and workplace rights"
novelty_check: "orthogonal — tests protection gaps at status boundaries"
rubric: {specificity: 2/3, tension: 3/3, evidence: 2/3, novelty: 3/3}
```

- **External context:** Platform-work and equal-pay directives provide separate legal baselines. Employment status can determine which baseline applies.
- **Method:** Compare national status tests with equal-pay disclosure rights and relevant court decisions.
- **Impact:** Equality bodies can identify workers excluded by inconsistent classifications.
- **Boundary:** Compare national rules without assuming a single EU-wide definition of worker.

## National preparedness vs. cross-border health access

The amended International Health Regulations and the WHO Pandemic Agreement create adjacent global-health commitments. Their division of responsibilities merits a direct comparison.

```yaml
concept_id: C07
concept: "Compare how 2024 International Health Regulations amendments and the 2025 WHO Pandemic Agreement assign preparedness duties and cross-border access."
anchor: "The World Health Assembly adopted the IHR amendments on 1 June 2024 and the Pandemic Agreement on 20 May 2025."
anchor_source: "S07 (1 June 2024); S08 (20 May 2025)"
why_now: "The Assembly adopted the amended IHR in June 2024 and the Pandemic Agreement in May 2025, making their responsibilities directly comparable."
tension: "National preparedness duties must coexist with equitable access to health countermeasures across borders."
evidence_trail: "The two adopted texts, WHO implementation guidance, national preparedness plans, and public reporting."
domain: "Global health governance"
novelty_check: "adjacent — legal implementation, not pandemic R&D funding"
rubric: {specificity: 3/3, tension: 3/3, evidence: 2/3, novelty: 2/3}
```

- **External context:** WHO instruments establish international duties. Their implementation depends on national plans and public reporting.
- **Method:** Crosswalk duties, timelines, and reporting requirements across the two instruments.
- **Impact:** Governments and health agencies can locate gaps between preparedness and access commitments.
- **Boundary:** Assess legal design and published plans, not outcomes during a future outbreak.

## Long-range grid plans vs. lead-pipe replacement schedules

Federal rules set different planning horizons for transmission expansion and lead-pipe replacement. Local construction coordination offers a measurable point of comparison.

```yaml
concept_id: C10
concept: "Compare grid-transmission and lead-pipe replacement schedules to test whether joint infrastructure planning reduces disruption and construction costs."
anchor: "FERC Order No. 1920's 20-year planning horizon and EPA's 2024 lead-pipe replacement rule."
anchor_source: "S09 (13 May 2024); S10 (8 October 2024)"
why_now: "Two federal rules finalized in 2024 established distinct grid-planning and lead-pipe replacement schedules that local agencies can compare."
tension: "Separate infrastructure plans can schedule work on the same roads without coordinating costs or disruption."
evidence_trail: "Regional transmission plans, lead-service-line inventories, public construction permits, and project schedules."
domain: "Energy-system and drinking-water infrastructure"
novelty_check: "orthogonal — links electricity and water project schedules"
rubric: {specificity: 3/3, tension: 3/3, evidence: 3/3, novelty: 2/3}
```

- **External context:** Transmission planning and water-line replacement use separate planning processes. Public schedules can reveal where they intersect.
- **Method:** Overlay project schedules, road permits, and lead-service-line inventories in selected regions.
- **Impact:** Local planners can coordinate work and reduce repeat excavation and service disruption.
- **Boundary:** Select regions with public transmission plans and usable lead-line inventories.

## Drop log

- C03 — Packaging reuse and small-retailer logistics; novelty failed because the summary lacked a distinct research question.
- C06 — Platform pay transparency and algorithmic management; novelty failed because it duplicated C04.
- C08 — Pandemic-agreement financing comparison; evidence failed because implementation outcomes were not comparable.
- C09 — One Health data interoperability; novelty failed because earlier research already covered it.
- C11 — Infrastructure workforce allocation; specificity failed because the idea lacked a measurable anchor.
- C12 — Cross-program disruption costs; evidence failed because local project records were inconsistent.

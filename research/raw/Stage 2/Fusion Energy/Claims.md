---
stage: 2
created: 2026-10-02
extracted_from:
  - research/Research ideas/Fusion Energy/00_Index/Synthesis.md
  - research/Research ideas/Fusion Energy/01_Background/Fundamentals.md
  - research/Research ideas/Fusion Energy/02_Approaches/ICF.md
  - research/Research ideas/Fusion Energy/02_Approaches/Magnetized_Target.md
  - research/Research ideas/Fusion Energy/02_Approaches/FRC.md
  - research/Research ideas/Fusion Energy/02_Approaches/Z-Pinch.md
  - research/Research ideas/Fusion Energy/03_State_of_the_Art/State_of_the_Art.md
  - research/Research ideas/Fusion Energy/04_Challenges/Challenges.md
  - research/Research ideas/Fusion Energy/05_Outlook/Outlook.md
  - research/Research ideas/Fusion Energy/06_Evidence/Findings.md
extractor: stage2-extractor-agent
gate_results:
  gate_1_source_coverage: pass
  gate_2_claim_traceability: pass
  gate_3_evidence_class_integrity: pass
  gate_4_metric_conditions: pass
  gate_5_entity_completeness: pass
  gate_6_extraction_log_completeness: pass
  gate_7_ingestibility: pass
---

# Claims — Fusion Energy (Current State of Research, October 2026)

Extracted per `Rules and Regulations/Protocols/TransitionStage2.md` §4 Step 5. One assertion per row. Stage 1 uses source reliability classes (P/T/C) rather than claim-type tags; the mapping rule is recorded in `ExtractionLog.md` L002 (P → documented fact/high, T-only → documented fact/medium, C-only → reported signal/low–medium, hedged company claims → reported signal/low, survey synthesis → inference/medium). `[falsifier not stated]` marks material claims for which Stage 1 gives no falsifier (L008). `Workflow stage` refers to the Stage 1 research workflow defined in `WorkflowMap.md` (W1–W7).

| Claim ID | Claim text | Claim type | Confidence | Source IDs | Falsifier | Workflow stage | Stage 1 source | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C001 | NIF has achieved ignition 11 times as of mid-2026. | documented fact | high | S01 | LLNL's milestone page listing fewer than 11 ignition shots | W7 | Findings.md | Records & state of the art (RQ1) |
| C002 | NIF's all-time record is 8.6 MJ fusion yield from 2.08 MJ laser energy (target gain 4.13), set on Apr 7, 2025. | documented fact | high | S01 | A verified NIF shot with a higher yield or target gain | W7 | Findings.md | Records & state of the art (RQ1) |
| C003 | NIF's wall-plug gain remains ~0.008, with lasers drawing ~300+ MJ of electricity per shot at ~1 shot/day. | documented fact | medium | S03 | [falsifier not stated] | W7 | Findings.md | Records & state of the art (RQ1) |
| C004 | JET's final D–T campaign (shot Oct 3, 2023, announced Feb 8, 2024) set the tokamak fusion-energy record of 69 MJ over ~5.2 s. | documented fact | high | S04 | A verified tokamak D–T pulse with higher fusion energy | W7 | Findings.md | Records & state of the art (RQ1) |
| C005 | JET ceased operation and entered decommissioning in Feb 2024. | documented fact | high | S04 | Evidence of JET operating after Feb 2024 | W7 | Findings.md | Records & state of the art (RQ1) |
| C006 | EAST sustained H-mode plasma for 1,066 s on Jan 20, 2025 (prior record 403 s, 2023). | documented fact | high | S06 | A verified long-pulse H-mode discharge shorter than claimed, or a third-party record listing a different value | W7 | Findings.md | Records & state of the art (RQ1) |
| C007 | In Jan 2026 ASIPP reported a route to exceed the Greenwald density limit. | reported signal | medium | S07 | Absence of a corresponding ASIPP publication or corroboration by an independent laboratory | W7 | Findings.md | Records & state of the art (RQ1) |
| C008 | KSTAR's verified 100-million-°C duration record is 48 s (2024 campaign, first with tungsten divertor). | documented fact | high | S05 | A KFE primary release verifying a longer 100M °C discharge | W7 | Findings.md | Records & state of the art (RQ1) |
| C009 | A reported KSTAR 102 s result (Jun 2026) is disputed, with no KFE primary release. | reported signal | low | S05 | A KFE primary release confirming the 102 s result | W7 | Findings.md | Records & state of the art (RQ1) |
| C010 | Wendelstein 7-X set a stellarator triple-product record with 43 s of high-performance plasma. | documented fact | high | S08 | A verified stellarator discharge with a higher triple product | W7 | Findings.md | Records & state of the art (RQ1) |
| C011 | Wendelstein 7-X set a world-record 1.8 GJ plasma energy turnover over 360 s on May 22, 2025. | documented fact | high | S09;S10 | A verified stellarator energy-turnover result above 1.8 GJ | W7 | Findings.md | Records & state of the art (RQ1) |
| C012 | JT-60SA reached first plasma in Oct 2023 and resumed upgraded operations ~summer 2026 with tungsten divertor components. | documented fact | high | S11;S21 | [falsifier not stated] | W7 | Findings.md | Records & state of the art (RQ1) |
| C013 | ITER Baseline 2024 set research operations ~2033–34 and full D–T ~2039, with a +~€5B cost increase. | documented fact | high | S12;S13;S14 | An ITER Organization baseline document stating different dates or cost | W7 | Findings.md | Public programs (RQ3) |
| C014 | The sixth of nine ITER sector modules was installed Jul 28, 2026, ~6 months ahead of schedule. | documented fact | medium | S15;S46 | ITER installation reporting showing a different count or date | W7 | Findings.md | Public programs (RQ3) |
| C015 | China's BEST tokamak targets completion end-2027, aiming at a burning-plasma demo and first fusion power generation demo. | documented fact | high | S16 | A CAS or Chinese official statement revising the completion target | W7 | Findings.md | Public programs (RQ3) |
| C016 | China's CRAFT facility is in advanced construction. | documented fact | medium | S17 | [falsifier not stated] | W7 | Findings.md | Public programs (RQ3) |
| C017 | The UK Fusion Strategy 2026 commits >£2.5B over five years. | documented fact | high | S18 | A published UK strategy document with different funding figures | W7 | Findings.md | Public programs (RQ3) |
| C018 | STEP targets grid electricity in the 2040s with a DCO submission by Mar 2029. | documented fact | high | S19 | A revised STEP delivery schedule published by UKIFS | W7 | Findings.md | Public programs (RQ3) |
| C019 | The US DOE released its Fusion Science & Technology Roadmap on Oct 16, 2025, targeting commercial deployment by the mid-2030s. | documented fact | medium | S22;S23 | The published DOE roadmap stating a different target date | W7 | Findings.md | Public programs (RQ3) |
| C020 | DOE's milestone-based program awarded $46M to 8 companies in 2023. | documented fact | high | S22 | GAO-25-107037 showing different award amounts or company count | W7 | Findings.md | Public programs (RQ3) |
| C021 | The IAEA's first World Fusion Outlook (Oct 14, 2025) counts 160+ fusion devices operational, under construction, or planned worldwide. | documented fact | high | S32 | The published IAEA report giving a different device count | W7 | Findings.md | Public programs (RQ3) |
| C022 | Private fusion investment hit a record $4.48B in the 12 months to Jul 2026, with $14.24B cumulative across 56 companies. | documented fact | high | S31 | The FIA 2026 report showing different totals | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C023 | Private fusion investment in the prior 12 months was $2.64B, with $9.77B cumulative (53 companies). | documented fact | high | S30 | The FIA 2025 report showing different totals | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C024 | CFS raised an $863M Series B2 in Aug 2025 with investors including Nvidia and Google. | reported signal | medium | S24 | [falsifier not stated] | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C025 | SPARC is >75% assembled, but third-party analysis suggests first plasma may slip to 2027. | reported signal | medium | S24;S50 | SPARC achieving first plasma in 2026 as targeted | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C026 | ARC (400 MWe, Virginia) targets the early 2030s, with Google (200 MW, Jun 2025) and Eni (>$1B, Sep 2025) offtakes signed. | reported signal | medium | S24 | [falsifier not stated] | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C027 | Helion announced Polaris as the first private fusion machine operating on D–T fuel, at ~150M °C (Feb 2026). | reported signal | low | S25;S48 | Independent verification that Polaris has not operated on D–T fuel | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C028 | Helion has announced no public net-energy gain as of Sep 2026, making the Microsoft 50 MW / 2028 PPA widely doubted — the sector's highest-risk single date. | inference | medium | S25;S44;S51 | Helion disclosing verified net gain before 2028 | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C029 | Helion raised a $465M Series G in Jun 2026 at a ~$15.5B valuation. | reported signal | medium | S25 | [falsifier not stated] | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C030 | General Fusion listed on Nasdaq (GFUZ) in Jul 2026 after a 2025 funding crisis that included ~25% staff layoffs. | reported signal | medium | S29 | SEC filings or exchange records contradicting the listing date or layoff scale | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C031 | General Fusion's LM26 formed magnetized plasma (Mar 2025, peer-reviewed confinement result) and heated plasma to ~8.4M °C (0.72 keV). | reported signal | medium | S29 | [falsifier not stated] | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C032 | TAE announced a >$6B all-stock merger with Trump Media on Dec 18, 2025, still pending as of Oct 2026. | reported signal | medium | S26 | Merger termination or completion announcements | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C033 | Proxima Fusion raised €411M (Jul/Sep 2026), Europe's largest private fusion round. | documented fact | medium | S41 | [falsifier not stated] | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C034 | Thea Energy raised a $100M Series B (May 2026) and became the first DOE Milestone awardee to receive DOE certification for its Helios pilot plant. | reported signal | medium | S42 | [falsifier not stated] | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C035 | Type One Energy received the first US state fusion operating license (Tennessee, Sep 2026) and cooperates with TVA on a 350 MW plant at the former Bull Run coal site. | documented fact | medium | S23 | A state license issued to a different fusion company earlier | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C036 | Zap Energy reached 1–3 keV electron temperatures in sheared-flow-stabilized pinches with peer-reviewed sustained neutron production (FuZE, Apr 2025). | documented fact | medium | S28 | [falsifier not stated] | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C037 | Zap Energy's Century, a first-of-a-kind repetitive (~12 pulses/min) Z-pinch platform with liquid-metal cooling, became operational in 2025. | reported signal | medium | S28 | [falsifier not stated] | W7 | Findings.md | Private sector (RQ3, RQ5) |
| C038 | Xcimer switched on "Phoenix" (billed as the world's largest private laser, Jun 2026) and passed a DOE preconceptual design milestone for its Athena plant concept — company claims. | reported signal | low | S43 | Independent confirmation that Phoenix is not the largest private laser, or DOE records showing no milestone pass | W3 | ICF.md | Maturity & best results |
| C039 | First Light Fusion abandoned its projectile approach (2025), pivoting to the FLARE high-gain IFE concept and tritium-breeding work while financially strained. | reported signal | low | S47 | [falsifier not stated] | W3 | ICF.md | Maturity & best results |
| C040 | Tokamak Energy's ST40 achieved 9.6 keV hot-ion mode (peer-reviewed). | reported signal | medium | S27 | [falsifier not stated] | W4 | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) |
| C041 | No integrated tritium-breeding blanket has ever operated in a fusion neutron environment; ITER will test blanket mockups, not a self-sufficient cycle. | documented fact | high | S49;S12 | Demonstration of an integrated breeding blanket operating in a fusion neutron environment | W5 | Challenges.md | 2. Tritium fuel cycle |
| C042 | World civilian tritium stock is tens of kg, mostly from CANDU reactors (Ontario, Korea). | documented fact | medium | S49 | A national inventory report showing materially different stock | W5 | Challenges.md | 2. Tritium fuel cycle |
| C043 | Only Russia and China actively produce enriched Lithium-6; the US COLEX process shut down decades ago. | documented fact | medium | S33 | Evidence of another country actively producing enriched Li-6 | W5 | Challenges.md | 2. Tritium fuel cycle |
| C044 | IFMIF-DONES is in construction (main accelerator building works underway 2026), so DEMO-relevant materials data cannot exist before the mid-2030s at best. | inference | medium | S51 | IFMIF-DONES delivering DEMO-relevant materials data before the mid-2030s | W5 | Challenges.md | 1. Materials (14 MeV neutron environment) |
| C045 | MIT's BABY 14MeV experiment is producing the first direct TBR-model validation data. | reported signal | medium | S49 | [falsifier not stated] | W5 | Challenges.md | 2. Tritium fuel cycle |
| C046 | A single D–T plant needs several kg of startup tritium inventory and consumes a meaningful share of world supply per year. | documented fact | medium | S49 | [falsifier not stated] | W5 | Challenges.md | 2. Tritium fuel cycle |
| C047 | MAST-U performed the world-first use of 3D magnetic coils (RMP) to suppress ELM instabilities (Oct 2025). | documented fact | medium | S20 | Prior published RMP-based ELM suppression on another device | W5 | Challenges.md | 3. Heat exhaust / divertor |
| C048 | The Super-X divertor demonstrated ~10× exhaust-heat reduction on MAST-U. | documented fact | medium | S20 | Published MAST-U results showing a materially different reduction factor | W5 | Challenges.md | 3. Heat exhaust / divertor |
| C049 | The US NRC chose the byproduct-materials framework (10 CFR Part 30) over the reactor framework in May 2023, with rulemaking targeted for completion ~2027. | documented fact | medium | S36 | NRC rulemaking records showing a different framework or date | W5 | Challenges.md | 6. Regulation (moving faster than engineering) |
| C050 | The UK regulates fusion outside nuclear site licensing (Energy Act 2023), with facilities <50 MWe exempt from the NPS consent route. | reported signal | medium | S37 | UK legislation or NPS documents showing licensing inside the nuclear site regime | W5 | Challenges.md | 6. Regulation (moving faster than engineering) |
| C051 | Canada's CNSC is consulting on fusion regulatory readiness (DIS-25-01, Aug 2025). | documented fact | high | S38 | [falsifier not stated] | W5 | Challenges.md | 6. Regulation (moving faster than engineering) |
| C052 | Early fusion is generally projected not to be LCOE-competitive against SMRs or renewables+storage; the value case is firm, high-capacity-factor power. | inference | medium | S34 | Costing studies projecting early fusion LCOE at or below competitor LCOE | W5 | Challenges.md | 5. Economics |
| C053 | Q>1 in a tokamak is plausibly 2026–2028 (SPARC ~2027, BEST ~2027). | inference | medium | S51 | SPARC and BEST both failing to reach Q>1 by end-2028 | W7 | Synthesis.md | RQ1 — Where is the state of the art? |
| C054 | Credible first grid electricity is mid-2030s at the absolute earliest, with the industry median in the late 2030s/2040s and government roadmaps clustering ~2040. | inference | medium | S30;S32;S39;S51 | A grid-connected fusion plant delivering electricity before the mid-2030s, or all announced mid-2030s targets slipping past the 2040s | W7 | Synthesis.md | RQ5 — What timelines are credible? |
| C055 | Material grid contribution from fusion is 2050+. | inference | medium | S51 | A fusion fleet contributing material electricity share before 2050 | W7 | Outlook.md | Central scenario (synthesis, 2026-10-02) |
| C056 | The binding constraints through the 2030s are engineering (tritium self-sufficiency, materials data, heat exhaust, recirculating power), not physics. | inference | medium | S51 | A first plant gated instead by an unresolved plasma-physics failure | W7 | Synthesis.md | RQ4 — What are the principal obstacles? |
| C057 | The FIA 2025 survey shows companies split between "early 2030s" optimists and a large cluster expecting late-2030s/2040s first grid electricity. | documented fact | medium | S30 | The FIA 2025 survey showing a different distribution | W6 | Outlook.md | Expert forecasts |
| C058 | The IAEA World Fusion Outlook 2025 shows company milestone targets spanning late-2020s to mid-2050s, clustering early-to-mid 2030s. | documented fact | medium | S32 | The published IAEA report showing a different clustering | W6 | Outlook.md | Expert forecasts |
| C059 | The skeptic position (Jassby, Bulletin of the Atomic Scientists, 2017) argues fusion faces high internal power consumption, no natural tritium, and cost problems; the common skeptic floor is material grid contribution 2050+. | reported signal | low | S35 | [falsifier not stated] | W6 | Outlook.md | Expert forecasts |
| C060 | Tokamaks dominate public programs and funding (ITER, SPARC/ARC, STEP, BEST) and roughly half the private companies. | inference | medium | S31;S32 | Program and company censuses showing tokamaks as a minority | W3 | Approaches_Overview.md | Landscape synthesis (2025–2026) |
| C061 | Stellarators are the fastest-rising alternative, combining W7-X records with the largest new private rounds and first licences. | inference | medium | S08;S41;S23 | Another approach raising more private capital or reaching licensing first in 2025–2026 | W3 | Approaches_Overview.md | Landscape synthesis (2025–2026) |
| C062 | The alternates (FRC, MTF, Z-pinch) hold the most aggressive private timelines with the least independent validation, Helion's 2028 PPA being the highest-profile example. | inference | medium | S25;S44 | Independent validation results for FRC/MTF/Z-pinch milestones arriving before tokamak equivalents | W3 | Approaches_Overview.md | Landscape synthesis (2025–2026) |
| C063 | KSTAR targets 300 s at 100M °C in its 2026 campaign, en route to K-DEMO. | documented fact | medium | S05 | A KFE program plan without the 300 s goal | W4 | State_of_the_Art.md | Others |
| C064 | Japan's national strategy targets an electricity demonstration in the 2030s (J-Fusion, FAST prototype). | documented fact | medium | S40 | The published strategy lacking a 2030s demo target | W4 | State_of_the_Art.md | Others |
| C065 | The EUROfusion roadmap targets EU-DEMO grid electricity ~2050. | documented fact | medium | S04 | A revised EUROfusion roadmap with a different date | W4 | State_of_the_Art.md | EUROfusion / EU |
| C066 | DOE's $42M IFE hubs (STARFIRE et al., Dec 2023) pursue the missing IFE pieces: efficient lasers, ~Hz rep-rates, and mass target manufacturing. | documented fact | medium | S22 | [falsifier not stated] | W4 | State_of_the_Art.md | NIF / US ICF program |

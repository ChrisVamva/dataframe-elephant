---
stage: 2
created: 2026-10-02
extracted_from:
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

# Metrics — Fusion Energy (Current State of Research, October 2026)

Extracted per `Rules and Regulations/Protocols/TransitionStage2.md` §4 Step 6. Values are recorded exactly as Stage 1 states them; no averaging or transformation has been applied. `Scope / conditions` records the conditions Stage 1 states (device, date, campaign, geography); where Stage 1 states none, the cell reads `[conditions not stated in source]` and the row is set to `low` confidence per Gate 4. Company-sourced figures are `reported signal` at `low` or `medium` confidence regardless of presentation (L002); Stage 1 figures without any direct citation use S51 at `low` confidence (L011).

| Metric ID | Metric name | Value | Unit | Scope / conditions | Claim type | Confidence | Source ID | Stage 1 source | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M001 | NIF all-time target gain | 4.13 | dimensionless (MJ out per MJ laser in) | Record shot Apr 7, 2025 | documented fact | high | S01 | State_of_the_Art.md | Scientific records (verified, date-stamped) |
| M002 | NIF record-shot fusion yield | 8.6 | MJ | Same shot as M001 (Apr 7, 2025) | documented fact | high | S01 | State_of_the_Art.md | Scientific records (verified, date-stamped) |
| M003 | NIF record-shot laser energy | 2.08 | MJ | Same shot as M001 (Apr 7, 2025) | documented fact | high | S01 | State_of_the_Art.md | Scientific records (verified, date-stamped) |
| M004 | NIF ignition shot count | 11 | count | Dec 2022 – Jun 2026; latest 7.9 MJ, gain ≈3.8 on Jun 20, 2026 | documented fact | high | S01 | State_of_the_Art.md | Scientific records (verified, date-stamped) |
| M005 | NIF shot cadence | ~1 | shot/day | Current NIF operations | documented fact | medium | S01;S03 | Fundamentals.md | What NIF's ignition did and did not demonstrate |
| M006 | NIF wall-plug gain | ~0.008 | dimensionless | Dec 2022 record shot; lasers draw ~300+ MJ electricity per shot | documented fact | medium | S03 | Findings.md | Records & state of the art (RQ1) |
| M007 | NIF laser wall-plug efficiency | ~0.5 | % | NIF lasers | documented fact | medium | S01;S03 | ICF.md | Maturity & best results |
| M008 | Required total gain for a fusion power plant | ~100 | × | Target gain × driver efficiency × thermal-to-electric efficiency × availability | documented fact | medium | S03 | Fundamentals.md | Key metrics |
| M009 | Competitive tokamak plant Q_plasma requirement | 10–30 | dimensionless | Commonly cited requirement for a competitive plant | documented fact | medium | S13 | Fundamentals.md | Key metrics |
| M010 | JET tokamak fusion-energy record | 69 | MJ | D–T, over ~5.2 s, Oct 3, 2023 shot | documented fact | high | S04 | State_of_the_Art.md | Scientific records (verified, date-stamped) |
| M011 | JET record-pulse Q | ~0.33 | dimensionless | Same shot as M010 | documented fact | high | S04 | State_of_the_Art.md | Scientific records (verified, date-stamped) |
| M012 | EAST long-pulse H-mode duration | 1,066 | s | Jan 20, 2025; prior record 403 s (2023) | documented fact | high | S06 | State_of_the_Art.md | Scientific records (verified, date-stamped) |
| M013 | KSTAR verified 100M °C duration | 48 | s | 2024 campaign, first with tungsten divertor | documented fact | high | S05 | State_of_the_Art.md | Scientific records (verified, date-stamped) |
| M014 | KSTAR 2026 campaign goal | 300 | s | At 100M °C; en route to K-DEMO | documented fact | medium | S05 | State_of_the_Art.md | Others |
| M015 | W7-X plasma energy turnover record | 1.8 | GJ | Over 360 s, May 22, 2025 | documented fact | high | S09;S10 | State_of_the_Art.md | Scientific records (verified, date-stamped) |
| M016 | W7-X triple-product record pulse length | 43 | s | High-performance plasma, May 2025 | documented fact | high | S08 | State_of_the_Art.md | Scientific records (verified, date-stamped) |
| M017 | Helion Polaris D–T plasma temperature (company claim) | ~150 | M °C | Feb 13, 2026; company temperature record; no independent verification | reported signal | low | S25 | FRC.md | Maturity & best results (company claims — treat as [C]) |
| M018 | General Fusion LM26 plasma temperature | ~8.4 | M °C | 2025 (0.72 keV); en route to 1 keV and ultimately 10 keV milestones | reported signal | medium | S29 | Magnetized_Target.md | Maturity & current status (General Fusion is the field) |
| M019 | Zap FuZE electron temperature | 1–3 | keV | Sheared-flow-stabilized pinch, Apr 2025; peer-reviewed sustained neutron production | documented fact | medium | S28 | Z-Pinch.md | Maturity & best results |
| M020 | Zap Century rep-rate | ~12 | pulses/min | First-of-a-kind repetitive Z-pinch platform with liquid-metal cooling, operational 2025 | reported signal | medium | S28 | Z-Pinch.md | Maturity & best results |
| M021 | Tokamak Energy ST40 hot-ion temperature | 9.6 | keV | [conditions not stated in source] | reported signal | low | S27 | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) |
| M022 | Sandia MagLIF DD neutron yield benchmark | >10^13 | neutrons/shot | Sandia Z machine; record ~2020; no new record found for 2025–26 | reported signal | low | S51 | Z-Pinch.md | Maturity & best results |
| M023 | ITER tungsten monoblock divertor steady-state rating | 10–20 | MW/m² | ITER divertor components | documented fact | medium | S12 | Challenges.md | 1. Materials (14 MeV neutron environment) |
| M024 | ITER research operations target | ~2033–34 | year | Baseline 2024 (rebaseline) | documented fact | high | S12;S13 | Findings.md | Public programs (RQ3) |
| M025 | ITER full D–T target | ~2039 | year | Baseline 2024; Q=10 target | documented fact | high | S13 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M026 | ITER rebaseline cost increase | +~5 | billion EUR | Baseline 2024 | documented fact | medium | S14 | Findings.md | Public programs (RQ3) |
| M027 | ITER sector modules installed | 6 of 9 | count | As of Jul 28, 2026; ~6 months ahead of schedule | documented fact | medium | S15 | Findings.md | Public programs (RQ3) |
| M028 | UK Fusion Strategy 2026 funding | >2.5 | billion GBP | Over five years | documented fact | high | S18 | Findings.md | Public programs (RQ3) |
| M029 | UK fusion AI supercomputer funding | 45 | million GBP | Fusion Strategy 2026 | documented fact | high | S18 | State_of_the_Art.md | United Kingdom |
| M030 | DOE milestone-based program award | 46 | million USD | 8 companies, 2023 | documented fact | high | S22 | Findings.md | Public programs (RQ3) |
| M031 | DOE IFE hubs funding | 42 | million USD | STARFIRE et al., Dec 2023 | documented fact | medium | S22 | State_of_the_Art.md | NIF / US ICF program |
| M032 | Private fusion investment, 12 months to Jul 2026 | 4.48 | billion USD | Record year; FIA 2026 report | documented fact | high | S31 | Findings.md | Private sector (RQ3, RQ5) |
| M033 | Private fusion cumulative investment | 14.24 | billion USD | Across 56 companies, Jul 2026 | documented fact | high | S31 | Findings.md | Private sector (RQ3, RQ5) |
| M034 | Private fusion investment, prior 12 months | 2.64 | billion USD | Year to Jul 2025 | documented fact | high | S30 | Findings.md | Private sector (RQ3, RQ5) |
| M035 | Private fusion cumulative investment (prior year) | 9.77 | billion USD | 53 companies, Jul 2025 | documented fact | high | S30 | Findings.md | Private sector (RQ3, RQ5) |
| M036 | CFS Series B2 round | 863 | million USD | Aug 2025; investors including Nvidia and Google | reported signal | medium | S24 | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) |
| M037 | CFS cumulative funding | ~3 | billion USD+ | [conditions not stated in source] | reported signal | low | S24 | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) |
| M038 | Google ARC offtake | 200 | MW | Agreement Jun 2025 | reported signal | medium | S24 | Findings.md | Private sector (RQ3, RQ5) |
| M039 | Eni ARC offtake | >1 | billion USD | Agreement Sep 2025 | reported signal | medium | S24 | Findings.md | Private sector (RQ3, RQ5) |
| M040 | Helion Series G | 465 | million USD | Jun 2026; ~$15.5B valuation | reported signal | medium | S25 | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) |
| M041 | Microsoft–Helion PPA size | 50 | MW | PPA signed May 2023; delivery 2028 | reported signal | medium | S25;S44 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M042 | TAE–Trump Media merger value | >6 | billion USD | All-stock; announced Dec 18, 2025; pending as of Oct 2026 | reported signal | medium | S26 | Findings.md | Private sector (RQ3, RQ5) |
| M043 | Proxima Fusion round | 411 | million EUR | Jul/Sep 2026; Europe's largest private fusion round; ~€2.4B valuation | documented fact | medium | S41 | Findings.md | Private sector (RQ3, RQ5) |
| M044 | Thea Energy Series B | 100 | million USD | May 2026; plus $20M magnet line | reported signal | medium | S42 | Stellarator.md | Maturity & best results |
| M045 | Type One Energy Pre-Series B | 87 | million USD | Jan 2026 | reported signal | low | S51 | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) |
| M046 | Tokamak Energy funding | ~335 total; 125 in 2025 | million USD | Cumulative; 2025 round $125M | reported signal | medium | S27 | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) |
| M047 | Zap Energy cumulative funding | ~327 | million USD | As of research date 2026-10-02; no major new round found in 2025–26 | reported signal | low | S51 | Z-Pinch.md | Maturity & best results |
| M048 | Xcimer funding | >150 | million USD | As of research date 2026-10-02 | reported signal | low | S43 | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) |
| M049 | First Light Fusion funding | ~107 | million USD | As of Nov 12, 2025 | reported signal | low | S47 | ICF.md | Maturity & best results |
| M050 | General Fusion market cap | ~404 | million USD | Sep 2026; below the ~$1B SPAC deal valuation | reported signal | medium | S29 | Magnetized_Target.md | Maturity & current status (General Fusion is the field) |
| M051 | General Fusion 2025 workforce reduction | ~25 | % | May 2025 layoffs after funding shortfall | reported signal | medium | S29 | Magnetized_Target.md | Maturity & current status (General Fusion is the field) |
| M052 | World civilian tritium stock | tens of | kg | Mostly from CANDU reactors (Ontario, Korea) | documented fact | medium | S49 | Challenges.md | 2. Tritium fuel cycle |
| M053 | Blanket Li-6 enrichment requirement | 30–90 | % | Typical breeding blankets | documented fact | medium | S33 | Challenges.md | 2. Tritium fuel cycle |
| M054 | Fusion industry workforce | ~9,000 | employees | FIA 2025 | documented fact | medium | S30 | Challenges.md | 7. Supply chain & workforce |
| M055 | Early fusion LCOE point estimates | ~50–150+ | USD/MWh | [conditions not stated in source] | documented fact | low | S34 | Challenges.md | 5. Economics |
| M056 | MIT optimistic FOAK LCOE estimate | ~91 | USD/MWh | Nicholas et al. 2021 | documented fact | medium | S34 | Challenges.md | 5. Economics |
| M057 | Fusion plant capital cost range | 4,000–8,000 | USD/kWe | Lindley et al. 2023 | documented fact | medium | S34 | Challenges.md | 5. Economics |
| M058 | SMR LCOE comparison | 40–60 | USD/MWh | Competitor benchmark | documented fact | medium | S34 | Challenges.md | 5. Economics |
| M059 | Renewables+storage LCOE comparison | 65–90 | USD/MWh | Competitor benchmark | documented fact | medium | S34 | Challenges.md | 5. Economics |
| M060 | IAEA counted fusion devices | 160+ | count | Operational, under construction, or planned worldwide; World Fusion Outlook, Oct 14, 2025 | documented fact | high | S32 | Findings.md | Public programs (RQ3) |
| M061 | FIA 2026 company count | 56 | companies | FIA industry report, Jul 13, 2026 | documented fact | high | S31 | Findings.md | Private sector (RQ3, RQ5) |
| M062 | FIA 2025 company count | 53 | companies | FIA industry report, Jul 22, 2025 | documented fact | high | S30 | Findings.md | Private sector (RQ3, RQ5) |
| M063 | BEST completion target | end-2027 | date | Burning-plasma demo; construction on schedule as of Oct 2025 | documented fact | high | S16 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M064 | SPARC first plasma company target | 2026 | year | Company target; >75% assembled | reported signal | medium | S24 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M065 | SPARC first plasma independent estimate | 2027 | year | Third-party analysis (The Fusion Report) | reported signal | medium | S50 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M066 | Microsoft PPA delivery date | 2028 | year | Signed May 2023; no public net gain as of Sep 2026 | reported signal | medium | S25;S44 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M067 | STEP DCO submission deadline | Mar 2029 | date | Delivery phase 2025–2032 | documented fact | high | S19 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M068 | STEP grid electricity target | 2040s | decade | West Burton site | documented fact | high | S19 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M069 | EU-DEMO grid electricity target | ~2050 | year | EUROfusion roadmap | documented fact | medium | S04 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M070 | DOE roadmap commercial deployment target | mid-2030s | period | Fusion Science & Technology Roadmap, Oct 16, 2025; strategy target, not funded plan | documented fact | medium | S22;S23 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M071 | National Academies US pilot plant window | 2035–2040 | years | Conservative consensus anchor | documented fact | medium | S39 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M072 | ITER Q target (full D–T) | 10 | dimensionless | Baseline 2024 full D–T phase | documented fact | high | S13 | Outlook.md | Announced timelines (collect, then rate credibility) |
| M073 | ARC plant capacity target | 400 | MWe | Virginia; early 2030s target | reported signal | medium | S24 | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) |
| M074 | TAE Da Vinci plant capacity claim | 50 | MWe | Siting claimed to start 2026; pending merger | reported signal | low | S26 | FRC.md | Maturity & best results (company claims — treat as [C]) |
| M075 | Type One TVA plant capacity | 350 | MW | Former Bull Run coal site, Tennessee | documented fact | medium | S23 | Stellarator.md | Maturity & best results |
| M076 | MAST-U Super-X exhaust-heat reduction | ~10 | × | Demonstrated on MAST-U | documented fact | medium | S20 | Challenges.md | 3. Heat exhaust / divertor |
| M077 | Proxima Fusion post-round valuation | 2.4 | billion EUR | Sep 2026 | documented fact | medium | S41 | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) |
| M078 | GFUZ SPAC deal valuation | ~1 | billion USD | At Jul 2026 listing; market cap ~$404M by Sep 2026 | reported signal | medium | S29 | Magnetized_Target.md | Maturity & current status (General Fusion is the field) |

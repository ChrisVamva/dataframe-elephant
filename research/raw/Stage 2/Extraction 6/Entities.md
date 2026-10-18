---
stage: 2
created: 2026-10-02
extracted_from:
  - research/Research ideas/Fusion Energy/01_Background/Fundamentals.md
  - research/Research ideas/Fusion Energy/02_Approaches/Approaches_Overview.md
  - research/Research ideas/Fusion Energy/02_Approaches/Tokamak.md
  - research/Research ideas/Fusion Energy/02_Approaches/Stellarator.md
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

# Entities — Fusion Energy (Current State of Research, October 2026)

Extracted per `Rules and Regulations/Protocols/TransitionStage2.md` §4 Step 3. One row per named concept that becomes a node in the data model: confinement approaches, physics concepts, fuel cycles, public and private devices, companies and organizations, and supply-chain materials. The `Boundary (what it is not)` column states what the entity is *not*; where Stage 1 provides no explicit contrast the cell carries `[boundary not stated in source]` and the row is logged in `ExtractionLog.md` (L009). Concepts mentioned only in passing with no definition (e.g. CFETR) are not extracted.

| Entity ID | Canonical name | Type | Boundary (what it is not) | Stage 1 source | Section | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| E001 | Tokamak | confinement approach | Relies on a driven plasma current for part of its field; not a stellarator (external coils only) | Tokamak.md | How it works | high |
| E002 | Stellarator | confinement approach | Confinement produced entirely by external twisted coils with no plasma current; not a tokamak | Stellarator.md | How it works | high |
| E003 | Inertial confinement fusion (ICF) | confinement approach | Capsule compressed faster than it can disassemble (inertial confinement); not magnetic confinement | ICF.md | How it works | high |
| E004 | Magnetized target fusion (MTF) | confinement approach | Hybrid: magnetized plasma compressed on millisecond timescales; neither slow magnetic nor fast inertial confinement | Magnetized_Target.md | How it works | high |
| E005 | Field-reversed configuration (FRC) | confinement approach | Compact toroid with purely poloidal field and no toroidal field coils; high beta | FRC.md | How it works | high |
| E006 | Sheared-flow Z-pinch | confinement approach | Axial-current self-compression stabilized by axial flow shear; no superconducting magnets or neutral beams (Zap design); not a tokamak | Z-Pinch.md | How it works | high |
| E007 | Scientific (target) gain | physics concept | Fusion energy out divided by energy delivered to the fuel or plasma; not wall-plug (engineering) gain | Fundamentals.md | Key metrics | high |
| E008 | Wall-plug (engineering) gain | physics concept | Fusion energy out divided by electricity drawn by the whole facility; not target gain | Fundamentals.md | Key metrics | high |
| E009 | Triple product (n·T·τ_E) | physics concept | Density × temperature × energy-confinement time yardstick; not the Q factor alone | Fundamentals.md | Key metrics | high |
| E010 | Ignition | physics concept | Self-sustaining burn where alpha-particle heating dominates external heating; not engineering breakeven | Fundamentals.md | Key metrics | high |
| E011 | H-mode | plasma regime | High-confinement plasma operating regime; not a device or a confinement approach | Fundamentals.md | Key metrics | high |
| E012 | Detached (radiative) divertor operation | operating mode | Required baseline divertor heat-exhaust mode that is hard to control in real time; not attached-divertor operation | Challenges.md | 3. Heat exhaust / divertor | medium |
| E013 | Super-X divertor | component concept | Advanced exhaust-heat-reducing divertor demonstrated on MAST-U; not a standalone reactor | Tokamak.md | Maturity & best results | high |
| E014 | Tritium breeding ratio (TBR) | physics concept | Ratio of tritium bred to tritium consumed in the blanket; not a plasma performance metric | Challenges.md | 2. Tritium fuel cycle | high |
| E015 | D–T fuel cycle | fuel cycle | Deuterium + tritium; easiest ignition; requires tritium bred from lithium in the plant; not aneutronic | Fundamentals.md | Fuel cycles | high |
| E016 | D–D fuel cycle | fuel cycle | Deuterium only; abundant fuel but still produces tritium and neutrons; not aneutronic | Fundamentals.md | Fuel cycles | high |
| E017 | Aneutronic fuel cycles (D–³He, p–¹¹B) | fuel cycle | Fewer neutrons and direct-conversion potential but far harder conditions; not the D–T cycle (both companies currently operate on D–T or precursor fuels) | Fundamentals.md | Fuel cycles | high |
| E018 | ITER | public device | 35-nation reactor-scale tokamak under assembly in France; not yet in research operations | State_of_the_Art.md | ITER (France, 35-nation) | high |
| E019 | JET | public device | UK tokamak; ceased operation Feb 2024 and entered decommissioning; no longer operating | Findings.md | Records & state of the art (RQ1) | high |
| E020 | EAST | public device | Chinese superconducting tokamak (ASIPP, Hefei); long-pulse record holder | State_of_the_Art.md | China | high |
| E021 | KSTAR | public device | Korean tokamak with tungsten divertor (KFE); 100M °C duration program | State_of_the_Art.md | Others | high |
| E022 | Wendelstein 7-X (W7-X) | public device | IPP Greifswald optimized stellarator, the stellarator flagship; experimental device, not a reactor | Stellarator.md | Maturity & best results | high |
| E023 | NIF | public device | LLNL indirect-drive laser ICF facility; ignition demonstrator with ~0.008 wall-plug gain; not a power plant | Fundamentals.md | What NIF's ignition did and did not demonstrate | high |
| E024 | JT-60SA | public device | Japan/EU superconducting tokamak; world's largest operating; research device, not a power plant | Findings.md | Records & state of the art (RQ1) | high |
| E025 | MAST-U | public device | UKAEA spherical tokamak; ELM-suppression and divertor testbed | Tokamak.md | Maturity & best results | high |
| E026 | SPARC | private device | CFS HTS tokamak designed for Q>1; not yet at first plasma as of Stage 1 (2026-10-02) | Tokamak.md | Maturity & best results | high |
| E027 | ARC | private device | CFS 400 MWe plant concept (Virginia); not built | Outlook.md | Announced timelines (collect, then rate credibility) | medium |
| E028 | STEP | public device | UK spherical tokamak program at West Burton in delivery phase; grid electricity targeted 2040s; not built | State_of_the_Art.md | United Kingdom | high |
| E029 | BEST | public device | Chinese burning-plasma tokamak (Hefei) targeting completion end-2027; under construction | State_of_the_Art.md | China | high |
| E030 | CRAFT | facility | Chinese fusion manufacturing/R&D infrastructure in advanced construction; not an experimental plasma device | State_of_the_Art.md | China | medium |
| E031 | DTT | public device | Italian divertor test tokamak; attacks the heat-exhaust problem; not a power plant | State_of_the_Art.md | EUROfusion / EU | medium |
| E032 | EU-DEMO | public device | European roadmap demonstration power plant (~2050 grid electricity); not funded or under construction | Outlook.md | Announced timelines (collect, then rate credibility) | high |
| E033 | IFMIF-DONES | facility | Materials qualification facility (Granada, Spain) under construction; will not deliver DEMO-relevant data before the mid-2030s at best | Challenges.md | 1. Materials (14 MeV neutron environment) | high |
| E034 | Polaris | private device | Helion 7th-generation FRC device; claimed first private D–T operation (company claim, not independently verified) | FRC.md | Maturity & best results (company claims — treat as [C]) | medium |
| E035 | Orion | private device | Helion plant at Malaga, WA under the Microsoft PPA; under construction, not operating | FRC.md | Maturity & best results (company claims — treat as [C]) | medium |
| E036 | LM26 (Lawson Machine 26) | private device | General Fusion MTF device (Vancouver); plasma formed and heated to ~8.4M °C; far from net energy | Magnetized_Target.md | Maturity & current status (General Fusion is the field) | high |
| E037 | FuZE | private device | Zap Energy sheared-flow Z-pinch experiment; peer-reviewed sustained neutron production | Z-Pinch.md | Maturity & best results | high |
| E038 | Century | private device | Zap Energy first-of-a-kind repetitive Z-pinch platform with liquid-metal cooling; operational 2025; not a net-gain device | Z-Pinch.md | Maturity & best results | medium |
| E039 | ST40 | private device | Tokamak Energy compact spherical tokamak; 9.6 keV hot-ion mode (peer-reviewed) | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) | high |
| E040 | ST80-HTS | private device | Tokamak Energy's next spherical tokamak (~2026); not yet operating | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) | medium |
| E041 | Copernicus | private device | TAE sixth-generation machine in development; not operating | FRC.md | Maturity & best results (company claims — treat as [C]) | medium |
| E042 | Helios | private device | Thea Energy pilot plant design; DOE-certified; not built | Stellarator.md | Maturity & best results | medium |
| E043 | Phoenix | private device | Xcimer laser billed as the world's largest private laser (Jun 2026); company claim, not independently verified | ICF.md | Maturity & best results | low |
| E044 | Athena | private device | Xcimer IFE plant concept; passed DOE preconceptual design milestone (company claim); not a detailed design | ICF.md | Maturity & best results | low |
| E045 | Da Vinci | private device | TAE claimed 50 MWe plant with siting claimed to start 2026; unverified and contingent on the pending merger | FRC.md | Maturity & best results (company claims — treat as [C]) | low |
| E046 | Commonwealth Fusion Systems (CFS) | company | Private HTS tokamak company (SPARC/ARC); not a public program | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) | high |
| E047 | Helion Energy | company | Private FRC/pulsed company; Microsoft 2028 PPA; no public net-energy gain as of Stage 1 | FRC.md | Maturity & best results (company claims — treat as [C]) | high |
| E048 | TAE Technologies | company | Private FRC company pursuing p–¹¹B; pending Trump Media merger as of Stage 1 | FRC.md | Maturity & best results (company claims — treat as [C]) | high |
| E049 | Proxima Fusion | company | W7-X spinout stellarator company; Europe's largest private fusion round (2026) | Stellarator.md | Maturity & best results | high |
| E050 | Thea Energy | company | Planar-coil stellarator company; first DOE Milestone awardee to receive DOE certification for its pilot design | Stellarator.md | Maturity & best results | medium |
| E051 | Type One Energy | company | Stellarator company; first US state fusion operating license (Tennessee, Sep 2026); TVA cooperation | Stellarator.md | Maturity & best results | high |
| E052 | Zap Energy | company | Sheared-flow Z-pinch company; design uses no superconducting magnets or neutral beams | Z-Pinch.md | Maturity & best results | high |
| E053 | General Fusion (GFUZ) | company | MTF company; Nasdaq-listed via SPAC since Jul 2026; survived the 2025 funding crisis | Magnetized_Target.md | Maturity & current status (General Fusion is the field) | high |
| E054 | Xcimer Energy | company | Excimer-laser IFE company; milestone claims are company claims without independent validation | ICF.md | Maturity & best results | medium |
| E055 | Tokamak Energy | company | Spherical tokamak + HTS company (ST40/ST80-HTS); not a public program | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) | high |
| E056 | First Light Fusion | company | Former projectile-ICF company repurposed (2025) to the FLARE high-gain IFE concept and tritium breeding; financially strained | ICF.md | Maturity & best results | medium |
| E057 | US Department of Energy (DOE) | organization | US funder and strategy-setter (roadmap, milestone program, IFE hubs); not an operator of private ventures | State_of_the_Art.md | Others | high |
| E058 | Fusion Industry Association (FIA) | organization | Industry association publishing annual investment and survey reports; not a funder or operator | State_of_the_Art.md | Private ventures (headline status; see 02_Approaches for detail) | high |
| E059 | IAEA | organization | Intergovernmental body publishing the World Fusion Outlook; not a funder or operator | Findings.md | Public programs (RQ3) | high |
| E060 | UKAEA | organization | UK national fusion laboratory operating MAST-U; not a private company | Tokamak.md | Representative devices | high |
| E061 | IPP | organization | Max Planck Institute for Plasma Physics, operating W7-X; not a private company | Stellarator.md | Maturity & best results | high |
| E062 | REBCO HTS tape | material | High-temperature superconducting tape for fusion magnets; global capacity far below projected demand; not a plasma-facing material | Challenges.md | 7. Supply chain & workforce | high |
| E063 | Lithium-6 enrichment | material | Feed material for breeding blankets (typically 30–90% enrichment); produced actively only by Russia and China; not a fuel itself | Challenges.md | 2. Tritium fuel cycle | high |
| E064 | Tritium breeding blanket | component | Plant component breeding tritium from lithium; none has ever operated in a fusion neutron environment; not a plasma component | Challenges.md | 2. Tritium fuel cycle | high |
| E065 | Eurofer97 | material | Reduced-activation ferritic-martensitic steel baseline candidate; not qualified for the 14 MeV neutron flux of a D–T plant | Challenges.md | 1. Materials (14 MeV neutron environment) | high |
| E066 | Tungsten monoblock divertor | component | ITER divertor plasma-facing component rated ~10–20 MW/m² steady-state; not a breeding component | Challenges.md | 1. Materials (14 MeV neutron environment) | high |
| E067 | Neutral beam injection (NBI) | technology | Heating and current-drive method; TAE demonstrated NBI-only FRC formation; [boundary not stated in source] | FRC.md | Maturity & best results (company claims — treat as [C]) | medium |

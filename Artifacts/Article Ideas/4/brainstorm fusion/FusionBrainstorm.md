# Fusion Brainstorm — Article Ideas from the Fusion Energy Survey

> Generated from Stage 2 Fusion Energy extraction (Claims C001–C066, Metrics M001–M078, Entities E001–E067, Sources S01–S51, Workflow W1–W7), research state as of 2026-10-02.
> All ideas are source-grounded; verify claim and metric values against `data/fusion_energy.duckdb` before drafting. Fusion records move — re-verify every date-stamped figure at drafting time.
> Evidence classes follow the Stage 1 mapping (P → documented fact/high, T → documented fact/medium, C → reported signal/low–medium); label them explicitly in drafts.

---

## 1. Records & Demonstration

### 1.1 The Two Gains: 4.13 vs 0.008 — How NIF Can Be Both a Triumph and 100× Short of a Power Plant
- **Angle**: Explainer that separates scientific (target) gain from wall-plug gain, walking the ladder from NIF's record shot to what a plant actually needs.
- **Evidence anchors**: M001 (target gain 4.13), M002–M003 (8.6 MJ out / 2.08 MJ laser in, Apr 7, 2025), M006 (wall-plug gain ~0.008), M005 (~1 shot/day), M007 (~0.5% laser efficiency), M008 (~100× total gain required), C002, C003, E007–E008.
- **Target reader**: Science-curious general readers and energy journalists.
- **Key insight**: Both headline numbers are true at once; the gap between them — three orders of magnitude — is the actual engineering story of inertial fusion.

### 1.2 69 MJ, Then Lights Out: What JET's Decommissioning Leaves Behind
- **Angle**: Eulogy-plus-inheritance piece on the tokamak that held the fusion-energy record for four decades, closing with what its final D–T campaign data still teaches.
- **Evidence anchors**: M010 (69 MJ over ~5.2 s, Oct 3, 2023), M011 (Q ≈ 0.33), C004, C005 (ceased Feb 2024), C065 (EU-DEMO ~2050 roadmap it feeds), S04.
- **Target reader**: Fusion-following technologists; readers of institutional histories.
- **Key insight**: JET ended with Q ≈ 0.33 — a factor of ~30 below the competitive-plant requirement (M009) — and the machine that closes that gap inherits its dataset, not its hardware.

### 1.3 48 Seconds or 102? How to Read a Fusion Record Before You Retweet It
- **Angle**: Media-literacy guide using the disputed KSTAR 102 s result as the case study: what "verified record" means, who verifies, and why primary releases matter.
- **Evidence anchors**: C008 (verified 48 s, 2024 campaign), C009 (102 s reported Jun 2026, disputed, no KFE primary release), C027 (Helion Polaris ~150M °C company claim), M021 (ST40 9.6 keV, conditions not stated), M017 (low-confidence temperature record), S05, S48.
- **Target reader**: Science journalists, analysts, and engaged social-media audiences.
- **Key insight**: The fusion field publishes three different currencies — verified facts, reputable secondary reports, and company claims — and press coverage routinely launders the third into the first.

---

## 2. The Money

### 2.1 $4.48B in Twelve Months: Inside Fusion's Record Fundraising Year
- **Angle**: Data-driven anatomy of the 2025–26 funding surge: who raised, at what valuations, and how concentrated the round sizes are.
- **Evidence anchors**: M032 ($4.48B, record), M034 ($2.64B prior year — a 70% jump), M033 ($14.24B cumulative), M061–M062 (56 vs 53 companies), M040 (Helion at ~$15.5B valuation), M036 (CFS $863M), M043 (Proxima €411M), C022–C023, C029, C033.
- **Target reader**: Energy-transition investors and climate-tech analysts.
- **Key insight**: A handful of megaround companies (Helion, CFS, Proxima) account for most of the jump — the "56 companies" headline overstates how broad the capital base is.

### 2.2 The Offtake Economy: Google, Eni, and Microsoft Are Fusion's Real VCs
- **Angle**: How power-purchase agreements and corporate pre-commitments became the sector's demand signal, and what they do (and don't) obligate.
- **Evidence anchors**: M038 (Google 200 MW ARC offtake, Jun 2025), M039 (Eni >$1B, Sep 2025), M041/M066 (Microsoft 50 MW, 2028), C024, C026, C028, predicates `signed_offtake_with`, `invested_in`.
- **Target reader**: Corporate energy buyers, utility strategists, deal lawyers.
- **Key insight**: Offtakes are cheaper than equity for the buyer and more credible than timelines for the public — but every one of them is an option on an unproven plant, priced accordingly.

### 2.3 From $1B SPAC to $404M: General Fusion's Public-Market Reckoning
- **Angle**: The sector's first public cautionary tale: a 2025 funding crisis, ~25% layoffs, a July 2026 Nasdaq listing, and a market cap 60% below deal valuation — set against real technical progress.
- **Evidence anchors**: M078 (~$1B SPAC valuation), M050 (~$404M market cap, Sep 2026), M051 (~25% layoffs), C030, C031 (LM26 peer-reviewed plasma formation), M018 (~8.4M °C), E036, E053.
- **Target reader**: Public-market investors tempted by fusion listings; PR teams at pre-IPO deep-tech firms.
- **Key insight**: Public markets marked down General Fusion not on physics but on time-to-revenue — the same discipline awaiting every company with a 2030s grid date.

### 2.4 A Fusion Company and a Media Company Walk Into a Merger
- **Angle**: The TAE–Trump Media all-stock merger as a lens on fusion financing scarcity: why a >$6B paper deal was more attractive than another venture round.
- **Evidence anchors**: C032 (announced Dec 18, 2025, pending as of Oct 2026), M042 (>$6B all-stock), M074 (Da Vinci 50 MWe claim), C062, E048, predicate `merged_with`, S26.
- **Target reader**: Deal watchers, deep-tech finance readers.
- **Key insight**: An all-stock merger with a media company is a liquidity and currency play, not a technology vote — and its pending status is itself a risk marker for the sector's least-validated timelines.

---

## 3. Timeline Credibility

### 3.1 2028: The Date Almost Nobody Believes (and Microsoft Is Contractually Bound To)
- **Angle**: Deep-dive on the Microsoft–Helion PPA as the sector's highest-risk single date: what Helion has and hasn't shown, and what happens to credibility on either outcome.
- **Evidence anchors**: C028 (no public net-energy gain as of Sep 2026; PPA "widely doubted"), C027 (Polaris D–T claim, unverified), M041 (50 MW), M066 (2028), M017 (~150M °C company claim), M040 (Series G $465M at $15.5B), S44 (Scientific American skepticism), E035 (Orion).
- **Target reader**: Energy journalists, corporate sustainability leads who cite the deal.
- **Key insight**: The PPA converts a scientific milestone (net gain) into a contractual deadline — the first time fusion's physics risk has been priced into a delivery date.

### 3.2 The Credibility Ladder: Every Major Fusion Date, Rated
- **Angle**: Comprehensive table-driven piece ranking announced milestones from company targets to independently analyzed estimates to government baselines, with explicit confidence labels.
- **Evidence anchors**: M024–M027 (ITER 2033–34 / 2039 / +€5B / 6-of-9 sectors), M063 (BEST end-2027), M064 vs M065 (SPARC 2026 target vs 2027 independent), M067–M068 (STEP), M069 (EU-DEMO ~2050), M070 (DOE mid-2030s), M071 (National Academies 2035–2040), C053–C055, C057–C058.
- **Target reader**: Policy analysts, energy planners, anyone tired of cherry-picked fusion dates.
- **Key insight**: Company dates cluster in the early 2030s, independent estimates in the late 2030s, and government roadmaps at ~2040 — a near-uniform 5–10 year optimism gap per layer.

### 3.3 Slippage Is Signal: What SPARC's 2026→2027 Whisper Tells You
- **Angle**: Micro-analysis of one schedule — SPARC at >75% assembly, company target 2026, third-party analysis suggesting 2027 — as a tutorial in reading construction progress vs first-plasma claims.
- **Evidence anchors**: M064 (2026 company target), M065 (2027, The Fusion Report), C025 (>75% assembled), C053 (Q>1 plausibly 2026–2028), S50, E026.
- **Target reader**: Fusion-literate retail investors and tech analysts.
- **Key insight**: A one-year slip before first plasma is trivial for the physics and decisive for the funding narrative — the two clocks run at different speeds and conflating them is the sector's core rhetorical trick.

---

## 4. The Real Bottlenecks

### 4.1 Tens of Kilograms: The Tritium Choke Point Nobody Has Solved
- **Angle**: The strongest "fusion isn't ready" story in the dataset: world tritium stock, startup inventories, and the fact that no breeding blanket has ever operated in a fusion neutron environment.
- **Evidence anchors**: C041 (no integrated blanket ever; ITER tests mockups only), C042 (tens of kg world stock, CANDU-derived), C046 (kg-scale startup inventory per plant), C045 (MIT BABY first TBR validation data), M052, E014 (TBR), E064 (breeding blanket), S49.
- **Target reader**: Energy policymakers, serious climate-modelers, fusion skeptics and advocates alike.
- **Key insight**: Even a perfect plasma machine is a paperweight without tritium self-sufficiency — and the first plants will bid up a world inventory measured in tens of kilograms.

### 4.2 The Materials Data Famine: You Can't Qualify Steel You've Never Irradiated
- **Angle**: Explainer on the 14 MeV neutron problem: why DEMO-relevant materials data can't exist before the mid-2030s, and why that quietly gates every 2040s grid date.
- **Evidence anchors**: C044 (IFMIF-DONES under construction; mid-2030s earliest), M023 (tungsten monoblock 10–20 MW/m²), E033 (IFMIF-DONES), E065 (Eurofer97 not yet qualified), M069 (EU-DEMO ~2050), C056.
- **Target reader**: Nuclear engineers, technology-readiness nerds, roadmap authors.
- **Key insight**: The binding constraint is calendar, not science — a materials-qualification facility coming online in the mid-2030s mathematically forces first-plant construction into the 2040s.

### 4.3 Ten Times Colder Exhaust: MAST-U and the Quiet British Dividend
- **Angle**: The unsung heat-exhaust story: Super-X divertor's ~10× exhaust-heat reduction and the world-first 3D-coil ELM suppression, delivered by a small UK machine the headlines skip.
- **Evidence anchors**: C047 (world-first RMP ELM suppression, Oct 2025), C048 (Super-X ~10×), M076, E012 (detached divertor operation), E013 (Super-X), E060 (UKAEA), S20; UK context M028–M029 (Fusion Strategy 2026), C017.
- **Target reader**: Plasma-physics adjacent engineers; UK science-policy readers.
- **Key insight**: Records capture attention, but the divertor — the component every plant needs and no record celebrates — is where MAST-U changed the design space for everyone, including ITER.

### 4.4 Physics Won. Engineering Hasn't Started.
- **Angle**: Big-synthesis essay arguing the 2030s are gated by tritium, materials, exhaust, and recirculating power — engineering problems with industrial solutions — rather than remaining plasma-physics risk.
- **Evidence anchors**: C056 (the synthesis claim), M006 (NIF wall-plug 0.008), M008 (~100× gain needed), M009 (Q 10–30 for competitive tokamak), C041, C044, C052, E007–E008.
- **Target reader**: General technologists; readers of grand-status essays.
- **Key insight**: "The physics is solved" is both the sector's best fundraising line and its most misleading one — the unsolved parts just live in a different engineering discipline now.

---

## 5. Regulation & Siting

### 5.1 Fusion Won the Regulatory Argument Before Building a Single Plant
- **Angle**: How three jurisdictions deliberately placed fusion outside nuclear reactor licensing — and why that may prove more consequential than any record shot.
- **Evidence anchors**: C049 (NRC byproduct-materials framework, 10 CFR Part 30, May 2023; rulemaking ~2027), C050 (UK Energy Act 2023, <50 MWe exempt from NPS route), C051 (CNSC DIS-25-01), C035 (first US state operating license, Tennessee, Sep 2026), S36–S38.
- **Target reader**: Energy lawyers, policymakers, nuclear-industry strategists.
- **Key insight**: Fission spent 70 years fighting its regulator; fusion lobbied its way out of one before the first commercial machine exists — the fastest regulatory pivot in energy history, and the least tested.

### 5.2 From Coal Ash to Plasma: The 350 MW Story of Bull Run
- **Angle**: Place-based feature on Type One Energy's license at the former Bull Run coal site in Tennessee and the TVA partnership — the coal-to-fusion siting template.
- **Evidence anchors**: C035 (first US state fusion operating license; TVA cooperation), M075 (350 MW), M045 (Pre-Series B $87M), E051, E042 (Thea's DOE-certified Helios as the stellarator context), C034, S23.
- **Target reader**: Regional-energy readers, just-transition and economic-development audiences.
- **Key insight**: The first fusion license in the US went to a stellarator startup on a coal plant's grave — a siting strategy that borrows the grid connection and the social license at the same time.

---

## 6. Economics

### 6.1 Fusion's Real Rival Is the SMR, Not the Solar Panel
- **Angle**: Comparison piece positioning early fusion against its actual competitive set — SMRs at $40–60/MWh and renewables+storage at $65–90/MWh — and the firm, high-capacity-factor niche that remains.
- **Evidence anchors**: M055 (fusion $50–150+/MWh), M056 (MIT optimistic FOAK ~$91), M057 (capex $4,000–8,000/kWe), M058 (SMR $40–60), M059 (renewables+storage $65–90), C052 (not LCOE-competitive; value case is firm power), S34.
- **Target reader**: Utility procurement, energy-transition modelers, climate fund analysts.
- **Key insight**: Even optimistic fusion LCOE lands at or above SMRs — so the honest pitch is premium firm power for grids that can't afford intermittency, not cheap electrons for everyone.

### 6.2 $1.6M of Capital per Employee: What Fusion's Burn Rate Actually Buys
- **Angle**: Ratio-driven piece dividing $14.24B of cumulative investment by ~9,000 industry employees to interrogate what a pre-revenue industry is really spending on.
- **Evidence anchors**: M054 (~9,000 employees, FIA 2025), M033 ($14.24B cumulative), M061 (56 companies), M032 ($4.48B/yr), C022.
- **Target reader**: Skeptical finance readers; anyone assessing deep-tech capital efficiency.
- **Key insight**: The ratio says the money is buying machines and milestones, not headcount — which is exactly what you'd expect in an industry where the product is a demonstration.

---

## 7. The Approaches Race

### 7.1 The Stellarator Renaissance: The Machine Everyone Called Too Hard Is Winning
- **Angle**: Narrative arc from Wendelstein 7-X's records to 2026's capital and licensing firsts — the 3D-coil configuration once dismissed as unbuildable becoming the investors' hedge against tokamak disruptions.
- **Evidence anchors**: C061 (fastest-rising alternative), C010 (43 s triple-product record), C011 (1.8 GJ turnover, 360 s), M015–M016, C033 (Proxima €411M, Europe's largest round), C034 (Thea $100M + DOE certification), C035 (Type One first license), M043/M044/M077, E002, E049–E051.
- **Target reader**: Deep-tech investors, physics-curious technologists.
- **Key insight**: Stellarators won 2026 on money and licenses without a single net-gain shot — because their physics risk is front-loaded into design, precisely what modern computation and planar coils (E050) just got good at.

### 7.2 Why Half the Private Field Still Bets on the Tokamak
- **Angle**: Analysis of tokamak incumbency: public programs (ITER, BEST, STEP) and roughly half of private companies converging on one topology, and what that concentration means for shared risk.
- **Evidence anchors**: C060 (dominance claim), C053 (Q>1 plausibly 2026–2028 via SPARC/BEST), M009 (Q 10–30 requirement), C040 (ST40 9.6 keV), M063–M065, C015, C018, E001, E026–E029.
- **Target reader**: Technology strategists, portfolio-minded research funders.
- **Key insight**: The tokamak's 70-year head start created a data moat no alternative can rent — the field isn't betting on the best geometry, it's betting on the best-characterized one.

### 7.3 Small, Loud, Unverified: The Alternates' Timeline Problem
- **Angle**: Tour of FRC, Z-pinch, and MTF ventures — the least capital, the earliest promised dates, and the thinnest independent validation — with Zap's peer-reviewed results as the honorable exception.
- **Evidence anchors**: C062 (most aggressive timelines, least validation), C027–C028 (Helion), M017 (150M °C claim), C036–C037 (Zap: 1–3 keV, Century at ~12 pulses/min), M019–M020, M047 (Zap ~$327M cumulative), C031 (GF LM26), M018, E005–E006, E047–E048, E052–E053.
- **Target reader**: Venture investors calibrating risk; fusion journalists seeking the sector's pattern of cheap machines and loud dates.
- **Key insight**: The alternates' pitch inverts the tokamak logic — worse confinement data, better engineering economics (Zap needs no magnets, E052) — so their risk is concentrated in exactly the place press releases never quantify.

### 7.4 NIF Proved Ignition; a Plant Needs 100×: The Long Shadow of IFE
- **Angle**: Status check on inertial fusion energy: the gap between a gain-4 experiment and a ~100×-gain plant, and the DOE hub program attacking efficient lasers, rep-rates, and target manufacturing.
- **Evidence anchors**: M008 (~100× required), M001/M004 (gain 4.13; 11 ignitions), M005–M007 (cadence, wall-plug), M031 (DOE $42M IFE hubs), C066, C038 (Xcimer "Phoenix", company claims), C039 (First Light's 2025 pivot), M048–M049, E043–E044, E056.
- **Target reader**: Photonics and laser-industry readers; national-lab watchers.
- **Key insight**: ICF's ignition removed the science question and exposed an industrial one — nobody has built a laser that fires 10× a second at 15% efficiency, and that, not plasma physics, is IFE's race.

---

## 8. Geopolitics & Public Programs

### 8.1 BEST vs SPARC: The Race to the First Burning Plasma
- **Angle**: Head-to-head of the two machines most likely to reach burning-plasma / Q>1 first — China's state-funded BEST targeting end-2027 completion against CFS's venture-backed SPARC — comparing governance, supply chains, and what "first" will even mean.
- **Evidence anchors**: C015 (BEST completion end-2027, burning-plasma and power-generation demos), M063, C053 (Q>1 plausibly 2026–2028), C025/M064–M065 (SPARC status and slip), C016 (CRAFT), C006–C007 (EAST records as the scientific base), E029, E026.
- **Target reader**: Geopolitics-of-technology readers; US and EU policy audiences.
- **Key insight**: This is Sputnik-shaped but not Sputnik-structured: China's edge is construction cadence and state patience, the US edge is HTS magnets and private capital — different machines, different clocks.

### 8.2 The Lithium-6 Problem Is a Geopolitics Problem
- **Angle**: Exposé-tinged explainer on the one fusion input only Russia and China currently enrich, the shuttered US COLEX process, and what a Li-6 dependency would mean for Western plant builders.
- **Evidence anchors**: C043 (only Russia and China actively produce enriched Li-6; COLEX shut decades ago), M053 (blankets need 30–90% enrichment), E063, E064, C041–C042, S33.
- **Target reader**: Energy-security analysts, critical-minerals readers.
- **Key insight**: Tritium breeding — the technical condition for fuel self-sufficiency (C041, predicate `breeds`) — routes through a Lithium-6 supply chain the West deliberately abandoned, recreating a uranium-enrichment-style dependency one fuel cycle down.

### 8.3 ITER: Late, Over Budget, and Suddenly Ahead of Schedule
- **Angle**: Nuanced status piece holding two facts together: the 2024 rebaseline (+~€5B, research ops ~2033–34, full D–T ~2039) and the sixth of nine sector modules landing ~6 months early in July 2026.
- **Evidence anchors**: C013 (baseline 2024), M024–M026, C014 (6th sector module, Jul 28, 2026), M027, C041 (ITER tests blanket mockups, not a self-sufficient cycle), M072 (Q=10 target), S12–S15, S46, E018.
- **Target reader**: Science-policy readers; European-budget watchers.
- **Key insight**: "Ahead of schedule" now means ahead of a schedule already reset two years — and even at full success ITER validates physics while explicitly deferring the tritium cycle every plant needs.

---

## 9. Frames & Meta

### 9.1 160 Machines, One Ignition: Mapping the Real Fusion Landscape
- **Angle**: Data-visualization companion piece to the IAEA's first World Fusion Outlook: 160+ devices worldwide, filtered through which approaches hold funding, records, and licenses.
- **Evidence anchors**: C021 (IAEA count, Oct 14, 2025), M060, C060–C062 (approach distribution), M061–M062, C022, E001–E006 (the six approach boundaries).
- **Target reader**: Chart-loving general readers; research funders.
- **Key insight**: The landscape is not 160 experiments racing one race — it's one large tokamak family, a rising stellarator clan, and a long tail of alternates whose machines are cheap precisely because their claims are expensive to check.

### 9.2 Company Claim or Verified Fact? A Field Guide to Fusion Evidence
- **Angle**: Methods piece teaching the P/T/C reliability discipline (and its Stage 2 mapping into claim types and confidence) using four live examples from the dataset.
- **Evidence anchors**: C009 (KSTAR 102 s dispute), C027 (Helion 150M °C), C038 (Xcimer "largest private laser"), M021 (ST40, conditions not stated), M022 (MagLIF, S51 low-confidence), Sources S25/S43/S51 classifications, ExtractionLog L002–L003.
- **Target reader**: Researchers, editors, and readers building evidence systems; companion methodology for this repo's pipeline.
- **Key insight**: A claim without a falsifier or stated conditions is a signal, not a fact — and the four hardest cases show that even reputable outlets circulate unconditioned numbers.

### 9.3 The Skeptic's Floor and the Optimist's Ceiling: Forecasting Fusion Honestly
- **Angle**: Bracketed-forecast essay: Jassby's structural critique and the 2050+ "material contribution" floor on one end, early-2030s optimists on the other, and where the evidence actually clusters.
- **Evidence anchors**: C059 (Jassby/Bulletin skeptic position), C057 (FIA survey split), C058 (IAEA milestone clustering), C054 (mid-2030s earliest grid; late-2030s/2040s median), C055 (material contribution 2050+), M070–M071, S30/S32/S35/S39.
- **Target reader**: Long-horizon energy planners; readers fatigued by both hype and dismissal.
- **Key insight**: Optimist and skeptic disagree less about physics than about discount rates — the honest forecast is a range whose width is itself the finding.

---

## Idea Ranking (by evidence density and audience demand)

| Rank | Article | Evidence Anchors | Evidence Strength |
|------|---------|------------------|-------------------|
| 1 | 1.1 The Two Gains (4.13 vs 0.008) | M001–M008, C002–C003 | High (quantified, primary sources) |
| 2 | 4.1 The Tritium Choke Point | C041–C046, M052–M053 | High (MIT + corroborated facts) |
| 3 | 3.1 The 2028 Microsoft PPA | C027–C028, M041, M066 | High interest, medium evidence (deliberately) |
| 4 | 7.1 The Stellarator Renaissance | C061, C010–C011, C033–C035, M043 | High (records + funding + licensing) |
| 5 | 8.1 BEST vs SPARC | C015, C025, C053, M063–M065 | High (primary program sources) |
| 6 | 2.1 The Record Fundraising Year | M032–M035, C022–C023 | High (FIA reports) |
| 7 | 8.2 The Li-6 Geopolitics Problem | C043, M053, E063 | Medium–High (single secondary source; needs follow-up) |
| 8 | 5.1 Fusion Won the Regulatory Argument | C049–C051, C035 | High (regulatory records) |
| 9 | 2.3 General Fusion's Public-Market Reckoning | M050–M051, M078, C030–C031 | Medium–High (listing + market data) |
| 10 | 1.3 How to Read a Fusion Record | C008–C009, C027, M021 | Medium (meta, evergreen traffic) |

---

## Next Steps

1. Verify every claim and metric value against `data/fusion_energy.duckdb` before drafting (Stage 2 import of this extraction).
2. Re-verify date-stamped records at drafting time — the Stage 1 gate itself warns "records move" (W4); NIF ignition counts, SPARC assembly %, and ITER sector count are the most volatile.
3. Check live status of pending events before publication: TAE–Trump Media merger (C032), SPARC first plasma (C025), KSTAR 102 s verification (C009), Helion net-gain disclosure (C028).
4. Label evidence class explicitly in every draft (documented fact / reported signal / inference), especially for low-confidence anchors: M017, M021, M022, M045, M047–M049, C009, C027, C038–C039.
5. Assign each drafted article its workflow stage (W3–W7) and section of the Stage 2 extraction for back-reference; ideas 2.4, 8.2, and 7.3 are the thinnest-sourced and need Stage 3 follow-up research before drafting.

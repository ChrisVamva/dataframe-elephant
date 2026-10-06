# Concentration and Dependency — Why Origin Integrity Is a Chokepoint Problem

_Covers RQ4. Every claim cites `[S##]`. Research pass of 2026-10-06. Analyst share figures (TrendForce/Counterpoint class) carry commercial bias flags; conflicting figures are reported side by side._

## 1. Semiconductor segment concentration

- **Foundry**: TSMC 67% of global foundry revenue Q4 2024 (TrendForce) [S63]; ~38% of Counterpoint's broader "Foundry 2.0" and **71% of pure-play foundry** in Q2 2025 (up from 31% a year earlier) [S63]. Full-year 2025 ~70% (secondary aggregation, indicative) [S63].
- **Advanced nodes**: TSMC widely estimated at ~90%+ of sub-7nm logic — industry estimate, no clean 2025-26 tracker citation (UNVERIFIED-BACKGROUND; flagged); advanced nodes were ~74% of TSMC's own revenue by Q3 2025 [S63].
- **Lithography**: ASML = sole EUV supplier (100%); China = 29% (2023) → ~41% (2024) → ~33% (2025) → ~20% (2026 guide) of ASML sales [S64].
- **HBM (2025)**: SK Hynix ~57–62%, Samsung ~22%, Micron ~21% — figure varies by quarter/definition (Counterpoint vs Yole vs TrendForce 2024: 53/38/9) [S70].
- **Packaging**: TSMC CoWoS capacity doubled in 2024 and again in 2025 and still undersupplied; NVIDIA >60% of 2025 CoWoS demand [S63].
- **Upstream inputs**: Shin-Etsu + SUMCO ~50% of silicon wafers (top four ~75–80%) [S63]; EDA big-3 (Synopsys ~31%, Cadence ~30%, Siemens ~13%) [S63]; top-5 WFE ≈ 75–80% [S63].

## 2. Country self-sufficiency

- **US** (SIA/BCG May 2024 — advocacy bias flagged): fab capacity 10% (2022) → **14% by 2032** (tripled absolutely); advanced-logic (<10nm) share 0% → 28% by 2032 [S65]. The oft-cited "160+ weak links / 50+ concentration points" formulation could not be verified against the report text (open item).
- **EU**: Chips Act 20%-of-global-production-by-2030 target vs ~8–10% current; European Court of Auditors: "highly unlikely" to achieve; member states urged a review (Oct 2025) [S74].

## 3. Critical-minerals processing concentration

- **IEA 2025**: China is the dominant refiner for **19 of 20** analysed minerals, ~70% average share; top-3 refining share for key energy minerals 86% (2024); >50% of energy-related minerals face some export control [S59].
- **IEA 2026**: top refiner's average share rose to **72% (2025)**; rare earths the exception (slight decline thanks to US/Malaysia capacity); China copper smelting → 50%; ~90% of battery-material recovery; price gaps: Ga/Dy/Tb ~5× Chinese domestic prices in Europe, Ge ~3× [S60].
- **Per-mineral (USGS/IEA)**: gallium **~99%** of primary low-purity production [S61]; antimony ~48%, tungsten ~79–80% of mine production [S62]; REE separation ~90% dipping toward ~85%; magnets >90% made in China; graphite processing >90%; cobalt refining ~75–80% (IEA-relayed, varies by source); Indonesia nickel ~66% of 2025 mine output — fastest concentration ever achieved (from ~2% refined share a decade ago) [S59, S60].
- **Counterweight projects**: MP Materials–DoD ($400M preferred, $110/kg NdPr 10-yr floor, DoD largest shareholder) [S66]; Lynas H1 FY26 NdPr 6,375 t, only commercial heavy-REE separator outside China, JARE floor to 2038 [S73]. Kazakhstan/Uzbekistan specifics unverified (open item).

## 4. Chokepoint effects of the 2025 controls

- The Apr 2025 seven-element controls halted US-bound Dy/Tb/Sc/Y flows [S12]; MERICS: controls "wreaked havoc" on supply chains and directly impair EU rearmament (advocacy context flagged) [S68].
- **F-35**: ~920 lb (~417 kg) REE content per aircraft — from a 2013 CRS report, recirculated in 2025-26; exact figure debated [S69].
- **Nexperia crisis (Oct-Nov 2025)**: Dutch seizure + Chinese export counter-ban on Dongguan-made chips put US/EU auto plants at risk "within weeks" (MEMA warning); Honda/VW braced for outages — a jurisdiction-vs-origin fight with physical production consequences [S72]. Broad production pauses from the REE controls specifically were **not confirmed** by tier-1 press (open item; the widely repeated Ford Explorer/JLR halt claims conflate the Nexperia crisis and the JLR cyberattack).
- **Defense stockpile**: CRS documents a **$13.5B gap** between stockpile assets and requirements; GAO documents single/foreign-source reliance [S67].

## 5. Concentration-metric methodology

- **HHI over supplier-country import shares** is the standard quantitative approach (thresholds ~1,500 moderate / 2,500 high on 0–10,000; EU documents use 750–1,800 / 1,800–5,000); WTO World Trade Report 2024 applies import/export HHI to partner concentration [S71]. An Energy Economics line of work argues standard thresholds need composite supplements (substitutability, political stability, entropy) [S71].
- **Observation (inference):** every existing concentration metric measures *share*, not *verifiability*. A supply chain at 99% single-country share [S61] and one at 40% but 0% traceable present identical HHI profiles for the property that actually broke in 2024–26: the inability to prove what is where. An **origin-integrity coverage metric** (RQ5) is complementary to HHI in the same way the EU's composite criticality methodology extends raw concentration [S71].

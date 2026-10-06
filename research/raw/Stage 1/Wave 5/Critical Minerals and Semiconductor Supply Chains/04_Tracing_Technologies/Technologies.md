# Tracing Technologies — Physical Witnesses and Digital Records

_Covers RQ3. Every claim cites `[S##]`. Each mechanism's **assurance ceiling** — what it actually proves — is stated explicitly. Research pass of 2026-10-06._

## 1. Physical witnesses: fingerprinting science

- **BGR Analytical Fingerprint (AFP) — the operational state of the art.** LA-ICP-MS trace-element analysis of **50 individual mineral grains** per concentrate + U-Pb dating of up to 20 grains; patterns compared by machine learning against a database of **>2,000 reference samples**; covers cassiterite, columbite-tantalite, wolframite, gold (tin slags in testing); used by German importers in OECD due diligence [S36]. Peer-reviewed basis is solid [S37].
  - **Ceiling:** a statistical statement of *consistency or exclusion* — BGR itself: an affirmation of origin "cannot be derived" from mineralogical/chemical data alone. The reference database is BGR-internal, not internationally governed [S36].
- **Field-deployable screening** (handheld XRF/LIBS for coltan) is emerging but immature — screening accuracy below lab LA-ICP-MS [S38].
- **Isotope systems**: Sn isotopes support ore provenance, but **isotope fractionation occurs during smelting**, complicating refined-metal-to-ore matching [S39]. Cassiterite U-Pb geochronology resolves provenance where chemistry fails (Bronze Age China) [S39].
- **Diamonds**: inclusion chemistry/spectroscopy demonstrates mine-level discrimination in research; **no operational, independently audited stone-to-mine forensic service at industry scale** — commercial provenance rests on chain-of-custody ledgers [S44].
- **The refined-products gap is total:** no provenance method exists for refined gallium/germanium/rare-earth metals — ore-level signatures do not demonstrably survive refining, and refining (concentrated in China at 99% for Ga [S61]) blends feedstock; buyer-side verification of refined product is industry-described as "very difficult" [S41].

## 2. Digital ledgers and pilots — attestation, digitized

| Pilot | Mechanism | Scale evidence | Ceiling |
|---|---|---|---|
| **Re|Source** (cobalt: Glencore, CMOC, Tesla, RCS Global) | blockchain batch-tracking from DRC mine to battery maker | 2021 pilot; **no public confirmation of commercial operation since** [S42] | batch-level attestation; proves what participants chose to enter |
| **Circulor** (Volvo/Polestar: cobalt, mica, lithium) | continuous event ledger + supplier attestations + some GPS/site data | Volvo claims "100% traceability of cobalt" — self-reported, no independent tonnage audit [S43] | proves a record exists, not that the record is true |
| **Tracr** (De Beers) | rough-scan "fingerprint" at mine + stone-level tracking through cutting | >5M diamonds registered ≈ **2/3 of De Beers production by value** (GIA took 30% stake) [S44] | closed single-operator system covering a shrinking share of global supply; does not authenticate unregistered stones |
| **MineHub** | digitized trade documents/logistics | ~1.87 Mt Cu/Al processed in 2025 [S46] | post-trade workflow platform, not a physical-origin attestation |
| **IRMA** | third-party mine-site ESG audits | Mogalakwena IRMA 50 (Mar 2025) etc. [S47] | conditions at a named mine at audit time; nothing after the gate |

- **Everledger's 2023 administration** is the continuity cautionary tale: provenance data died with the operator's solvency [S45].

## 3. Serialization precedents from pharma — the proven template

- **EU FMD** (Delegated Reg (EU) 2016/161, mandatory Feb 9 2019): every prescription pack carries a **unique identifier (GS1 2D data matrix: product code + serial + batch + expiry)** + anti-tampering device; identifiers uploaded to a central EU hub with national medicines verification systems; pharmacies verify/decommission at dispensing [S48].
- **US DSCSA**: package-level serialized electronic traceability (Transaction Information/Statements) from Nov 27 2023, enforcement stabilized to Nov 27 2024 with EPCIS-based exchange; even this closed, regulated channel needed a one-year stabilization and dispenser exemptions [S49].
- **Structural template extracted (inference):** unique ID + centralized verification + append-only event ledger + legal mandate. Pharma serialization proves the pattern works at scale **within a legally closed channel with few chokepoints** — its transfer to minerals must handle open channels, physical transformation, and thousands of SMEs.

## 4. Product passports — the EU's legislated surface

- **EU Battery Passport** (Reg (EU) 2023/1542): from **Feb 18 2027**, every EV/LMT/industrial battery >2 kWh needs a QR-accessible digital passport with serial/batch ID, manufacturer, chemistry and **critical-raw-material composition**, carbon footprint, recycled content, **due-diligence information** [S51]. Battery Pass/Catena-X provide implementation guidance [S52-adjacent: batterypass.eu — self-published consortium guidance].
  - **Ceiling:** passport data is **self-attested upstream** unless tied to audits/assays — a QR to a structured record, not proof of origin.
- **ESPR Digital Product Passport** (Reg (EU) 2024/1781): framework in force; Working Plan 2025–2030 (Apr 16 2025) prioritizes steel, aluminium, textiles — no product delegated acts adopted as of mid-2026; batteries excluded (own regulation) [S52].
- **GS1 layer**: GTIN/GLN identifiers, EPCIS 2.0 event standard ("what, when, where, why"), GS1 Digital Link as the passport access point; UN/CEFACT UNTP recommends EPCIS events for batch-level passports [S50].

## 5. Semiconductor-specific traceability

- **Surface marking fails**: GAO's undercover operation bought counterfeit military-grade parts readily — many sanded and re-marked; remarking harvested e-waste is the dominant counterfeit mode [S53]. Surface markings are claims, not evidence.
- **Procurement rules substitute for physical proof**: DFARS 252.246-7007/-7008 require traceability *to trusted sources* (OCMs/franchised distributors) + counterfeit-detection systems — paper traceability with forensic spot-checks [S54].
- **Die-level ECID exists but is under-governed**: unique per-die registers (may encode wafer X-Y, lot, wafer) support die tracking; IEEE ECID working group; SEMI device-tracking standards work [S55].
  - **Ceiling:** proves die identity *if the verifier can electrically query the die*; useless after remarking/repackaging unless buyers know to test; the ECID-to-shipment mapping is held privately by fabs/OSATs [S55].
- **DNA ink marking** (DLA/Applied DNA): invisible forensic marks on military-standard microcircuits — spot-check authentication of marked items only, never universal coverage [S56].
- **The standards gap is formally catalogued**: NIST CSRC tracks the status of microelectronics assurance/provenance/traceability standards; ANSI (2022) and DoD FPGA LoA2 best practices document the same hole [S57].
- **No C2PA-for-hardware exists** (as of Oct 2026): C2PA's signed-manifest pattern is media-only; adapting it to bind die ECID → fab → OSAT → board in a post-distribution-verifiable manifest is unbuilt [S58].
  - **Summary ceiling for chips:** provenance is provable up to authorized distribution (fab/OSAT records, trusted-source purchase); after distribution, verification reverts to forensics — exactly the gap remarking exploits.

## 6. Assurance ceiling table

| Mechanism | Proves | Cannot prove | Anchor |
|---|---|---|---|
| Paper attestation / CoO / audit | a party asserted X at time t | that X is true; any physical linkage | [S21, S75] |
| Tag-and-trace (ITSCI) | a tagged bag passed points | continuity during coverage holes | [S27] |
| Attested digital ledger | a record exists; participants entered it | record truth; completeness; operator continuity | [S42, S43, S44, S45] |
| Mine-site audit (IRMA/RMAP) | conditions at named site at audit time | custody after the gate | [S47] |
| Assay/isotope fingerprint (ore) | statistical consistency/exclusion vs reference set | definitive origin; anything for refined products | [S36, S39, S41] |
| Serialization (pharma template) | unique item passed verifiable checkpoints | origin of inputs; survives only in closed channels | [S48, S49] |
| Product passport (EU) | structured disclosure, QR-reachable | that disclosed data is true | [S51, S52] |
| Chip ECID / DNA marking | identity of marked/die-queried items | post-distribution chain; universal coverage | [S55, S56] |
| Signed manifest (C2PA-style) | tamper-evidence from issuance forward | — **does not exist for hardware/minerals** | [S58] |

**Design conclusion (inference):** every existing mechanism tops out one rung below what the regimes actually need (a machine-checkable, transformation-tolerant origin claim). The missing construction is not any single technology — it is the **composition**: physical witness at the mine, append-only ledger through every transformation, cryptographic signing at each step, and a reference library that is internationally governed rather than one agency's internal asset.

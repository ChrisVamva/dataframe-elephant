# Findings

_Date-stamped findings by research question. Every finding cites `[S##]`. Claim types follow the Research-Evaluation protocol: documented fact / reported signal / inference. Research pass of 2026-10-06._

## RQ1 — Regimes: how "origin" is defined and verified

- **[documented fact]** All four jurisdiction tests used by export-control and import regimes (de minimis content, FDP production lineage, corporate ownership, substantial transformation) are computable from documents, not from the physical object [S16, S04, S03, S25].
- **[documented fact]** The US and EU forced-labour regimes encode opposite verification philosophies: UFLPA's rebuttable presumption makes importers prove a negative across their chains; the EU FLR (Reg 2024/3015, applies Dec 14 2027) puts the burden on investigating authorities with only an adverse-inference fallback [S17, S18].
- **[documented fact]** China's Oct 2025 Announcement No. 61/62 imported the West's jurisdiction playbook wholesale (0.1% de minimis, FDP-analog extraterritorial licensing) — then suspended it to Nov 10, 2026 under the truce, while the Apr 2025 seven-element controls stayed active [S07, S10].
- **[documented fact]** The OECD five-step due-diligence framework — the scaffold under every mineral regime — is attestation-based end to end [S21].
- **[inference]** Every regime degrades to attestation at the first physical hand-off. Verification is a paperwork property; origin is a physical property. That mismatch is the load-bearing finding of this wave.

## RQ2 — Laundering: documented cases and enforcement

- **[documented fact]** Post-ban Russian gold: UAE 75.7 t / $4.3B in year one; UAE+China+Turkey = 99.8% of exports [S24]; re-entry to Western chains via re-refining is the reported-signal extension [S35].
- **[documented fact]** ≥150 t of coltan fraudulently exported from M23-held DRC to Rwanda in 2024; Rwandan exports exceed $1B/yr unexplained by domestic output [S26].
- **[documented fact]** The flagship traceability scheme (ITSCI) self-reports suspension in Masisi for almost all of 2024 (~120 t/month untraced) [S27]; artisanal cobalt blending into industrial feeds makes separation "futile" [S28].
- **[documented fact]** Chip smuggling enforcement is real but dwarfed by estimates: named prosecutions (Singapore Dell/SMCI case, DOJ Nov 2025 ~400 A100s, KLIA $13M seizure) [S29, S33] vs academic estimates of 100K–1M smuggled H100-class GPUs [S34].
- **[documented fact]** Solar AD/CVD circumvention determinations (2023) legally established that third-country module completion with Chinese inputs is laundering-class transformation [S31]; DOL documents that polysilicon blending makes Xinjiang-origin tracing "extremely challenging" [S23].
- **[inference]** The six-step laundering taxonomy (L1 blending, L2 transshipment, L3 minor transformation, L4 coverage holes, L5 ownership layering, L6 relabeling) — every step lawful or unpoliced in itself (`../03_Laundering_Cases/` §7).

## RQ3 — Tracing mechanisms and their assurance ceilings

- **[documented fact]** BGR's AFP is the operational ceiling for ore provenance: 50-grain LA-ICP-MS + U-Pb vs a >2,000-sample internal database, yielding consistency/exclusion only [S36]; smelting fractionates Sn isotopes [S39]; **no method at all exists for refined Ga/Ge/REE** [S41].
- **[documented fact]** Ledger pilots top out at attestation: Tracr ~2/3 of De Beers' own output [S44]; Circulor self-reported [S43]; Re|Source never confirmed past pilot [S42]; Everledger's administration shows operator-continuity risk [S45].
- **[documented fact]** Pharma serialization (EU FMD 2019, US DSCSA 2023-24) is the proven structural template: unique ID + centralized verification + event ledger + legal mandate — and even in that closed regulated channel, rollout needed a one-year stabilization [S48, S49].
- **[documented fact]** EU product passports are legislated (Battery Passport Feb 18 2027 [S51]; ESPR framework in force, product acts pending [S52]) but their data is self-attested unless tied to audits/assays.
- **[documented fact]** Chip traceability fails after distribution by design: remarking defeats surface marks [S53]; ECIDs work only if electrically queried and mappings are private [S55]; **no C2PA-style signed manifest exists for hardware** [S57, S58].
- **[inference]** Every mechanism tops out one rung below what regimes need. The missing construction is composition: physical witness + append-only transformation ledger + signatures + a governed reference library.

## RQ4 — Concentration and dependency

- **[documented fact]** China refines 19 of 20 IEA-tracked critical minerals (~70% average, rising to 72% in 2025); ~99% of primary gallium; >90% of REE magnets; ~50% of copper smelting [S59, S60, S61].
- **[documented fact]** Semiconductor chokepoints are absolute at single-firm level: TSMC ~71% pure-play foundry share [S63], ASML 100% of EUV [S64], HBM 3-firm market [S70], top-4 wafer suppliers ~75-80% [S63].
- **[documented fact]** Counterweight projects are state-capital backed (MP–DoD $110/kg floor [S66]; Lynas/JARE to 2038 [S73]); the US defense stockpile carries a $13.5B documented gap [S67].
- **[documented fact]** The Nexperia crisis showed jurisdiction-vs-origin fights hitting physical auto production within weeks [S72].
- **[inference]** Concentration metrics (HHI, top-producer share) measure share, not verifiability — a supply chain can be diversified on paper and unprovable in substance. Origin-integrity coverage is the missing complementary metric [S71].

## RQ5 — Mineral-Origin Record design requirements

- **[inference — design]** The record must make transformation append, not overwrite: blended lots carry both parents with ratios (kills L1 laundering); every other laundering step becomes a visible event (`../05_Origin_Record_Design/` §3).
- **[inference — design]** Claim classes must degrade honestly: attested → witnessed → reconciled, with refined Ga/Ge/REE explicitly "attested, unwitnessable at this stage" until fingerprinting science catches up [S36, S41].
- **[inference — design]** Governance is the binding constraint, not technology: the reference library is one agency's internal asset [S36]; ledger operators die [S45]; pharma needed a legal mandate [S48]. The EU battery passport (Feb 2027) is the nearest legislated beachhead [S51].

## Open follow-ups (carried to Index)

1. Verify BIS FY2025 penalty figures against the BIS annual report [S13].
2. Named Ga/Ge transshipment enforcement cases with quantities [S32 area].
3. Exact TSMC sub-7nm share from a citable 2025-26 tracker release [S63].
4. WCO global misdeclared-origin seizure statistics (none surfaced).
5. China official export-license approval rate (none published) [S10].
6. October 2026 status of the Nov 10, 2026 suspension expiry [S10].
7. Perth Mint / Iran sanctions element needs an archive pull [S40].
8. Re|Source: commercial operation confirmed or folded? [S42]
9. SIA/BCG "160+ weak links" formulation needs verification against the report PDF [S65].

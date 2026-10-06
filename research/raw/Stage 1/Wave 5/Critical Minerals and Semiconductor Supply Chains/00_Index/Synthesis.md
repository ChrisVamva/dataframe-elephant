# Synthesis — Answers to RQ1–RQ5

_Wave 5 research pass of 2026-10-06. Full evidence trail in `../06_Evidence/` (S01–S75) and the folder notes. Falsifiers and open items listed at the end._

## RQ1 — How do regimes define and verify "origin"?

Regimes determine origin with four document-computable tests — content de minimis, production lineage (FDP), corporate ownership, substantial transformation — and verify compliance with attestation: certificates, audits, declarations. None binds the attestation to the physical part. The US (UFLPA) and EU (FLR 2024/3015) forced-labour regimes take opposite burden-of-proof philosophies but share the same paper evidence class; the OECD framework that underpins every mineral regime is attestation-based end to end. China adopted the West's jurisdiction playbook in Oct 2025 (0.1% de minimis, FDP-analog), then suspended the sharpest parts under the Nov 2025 truce (expiring Nov 10, 2026).

**Answer:** origin is defined legally in four ways, and in all four, verification = paperwork. The physical object carries no enforceable evidence of where it came from.

## RQ2 — Where does origin evidence fail?

Six laundering mechanisms, all documented in 2022–2026 enforcement records and investigations: blending pools (Perth Mint gold, ASM cobalt, Xinjiang polysilicon), transshipment through non-cooperating hubs (Russian gold via UAE/Turkey/Armenia; GPUs via Malaysia/Vietnam), minor transformations that re-draw origin (SE-Asia solar module completion; diamond polishing), coverage-hole exploitation (ITSCI's Masisi suspension, ~120 t/month untraced), ownership layering (pre-Affiliates-Rule evasion; M23 coltan via Rwandan exporters), and post-hoc relabeling (chip remarking). Enforcement catches fragments — named prosecutions, UN GoE findings, CBP detention dashboards — while academic estimates of smuggled GPU volumes (100K–1M units) dwarf the caught cases.

**Answer:** origin evidence fails at exactly the steps that make supply chains work — refining, blending, transshipment. Every laundering step is lawful in itself; the absence of a record that transformations append to is the vulnerability.

## RQ3 — What tracing mechanisms exist, and what do they prove?

Physical witnesses: BGR's Analytical Fingerprint (statistical consistency only, internal database), isotope systems (broken by smelting fractionation), and — for refined gallium/germanium/rare earths — nothing at all. Digital records: ledger pilots prove a record exists, not that it is true (Tracr covers only De Beers' own output; Re|Source never confirmed past pilot; Everledger died with its operator). Legisl passports (battery, Feb 2027) are structured self-attestation. Chips: ECIDs exist but mappings are private and remarking defeats everything after distribution; no C2PA-style signed manifest exists for hardware.

**Answer:** every mechanism tops out one rung below what the regimes need. The serialization template (unique ID + verification hub + event ledger + legal mandate) is proven — in pharma's closed channel — and unbuilt for open, transforming mineral/hardware chains.

## RQ4 — How concentrated are these chains, and why does it matter for origin?

China refines 19 of 20 IEA-tracked minerals (72% average top-refiner share 2025; ~99% of gallium); semiconductors concentrate at single-firm level (TSMC ~71% pure-play foundry, ASML 100% of EUV). Concentration converts every origin question into a geopolitical event (Apr/Oct 2025 controls; the Nexperia seizure and counter-ban reaching auto plants within weeks). Counterweights are state-capital projects (MP–DoD price floor, Lynas/JARE).

**Answer:** concentration is why origin evidence is contested territory: where one actor dominates processing, its declarations are both load-bearing and unverifiable — and 2024–26 proved that states will weaponize exactly that. Existing concentration metrics (HHI) measure share, not verifiability.

## RQ5 — What would an interoperable Mineral-Origin Record require?

A composition, not an invention: (1) a lot-identity + event schema from GS1/EPCIS and the pharma template; (2) a **transformation ledger rule** — blending/refining append parent lots with ratios instead of overwriting origin (kills laundering mechanisms L1–L6 as silent steps); (3) a **cross-assay reconciliation rule** — two independent physical methods for a "witnessed" claim, honest degradation to "attested" where no witness exists (all refined Ga/Ge/REE today); (4) an **origin-integrity coverage metric** complementary to HHI that scores paper-only chains at zero; (5) governed assets — an internationally held reference library (today: one agency's internal database) and verification hubs with operator-continuity design.

**Answer:** technically feasible from existing fragments; the binding constraints are governance (library custodianship, hub operation) and adoption economics — pharma's template took a legal mandate and five years, and the EU battery passport (Feb 2027) is the nearest legislated beachhead.

## Falsifiers

- A documented case of refined Ga/Ge/REE forensic provenance (e.g., isotope recovery through refining) would invalidate the "no witness for refined products" ceiling [S41].
- Confirmation that Re|Source or a successor operates a commercially audited transformation ledger would undercut the "attestation, digitized" finding for ledgers [S42].
- A C2PA-style signed hardware manifest standard reaching deployment would falsify the "no cryptographic binding for chips" claim [S57, S58].
- Divergence of the Nov 10, 2026 suspension expiry either way (lapse or renewal) changes the RQ1 status picture [S10].

# Critical Minerals and Semiconductor Supply Chains — Origin Integrity

**Wave:** 5 (`research/raw/Stage 1/Wave 5/`)
**Origin:** NR3 brainstorming session, domain 7 / Subject G (`research/Research ideas/NR3/NR3brainstorm.md`, 2026-10-04)
**Protocol context:** FreeBrainstorming.md (external, universal framing — no internal project dependencies)

## Research Question

How do export-control, critical-minerals, and forced-labour regimes establish the "origin" of regulated inputs (minerals, chips, tooling), where does that origin evidence fail (provenance laundering), and what would an interoperable, machine-checkable Mineral-Origin Record require?

## Research Questions (decomposed)

- **RQ1 — Regimes:** How do current regimes define and verify "origin" for regulated inputs — US/allied semiconductor export controls (2022–2026), China's critical-minerals export controls (2023–2026), the EU Critical Raw Materials Act, forced-labour import rules (UFLPA, EU Forced Labour Regulation), and conflict-minerals regimes?
- **RQ2 — Laundering:** Where has provenance laundering been documented — which intermediary steps (transshipment, refining/blending, re-export, re-papering) defeat origin claims, and what did enforcement actions actually catch?
- **RQ3 — Tracing mechanisms:** What physical witnesses (assay/trace-element/isotope fingerprinting) and digital records (serialization, ledgers, product passports) exist, and what assurance ceiling does each provide?
- **RQ4 — Concentration:** How concentrated are mineral and semiconductor supply chains (refining, lithography, foundry, packaging, materials), and how does that concentration amplify origin-integrity risk?
- **RQ5 — Record design:** What would an interoperable Mineral-Origin Record require — transformation ledger, cross-assay reconciliation, origin-integrity coverage metric — and what do pharma/food/battery serialization precedents teach?

## Method Sketch (from NR3brainstorm.md §4 Subject G + domain 7)

Adapt pharmaceutical serialization and food chain-of-custody (GS1, EU FMD, EU Battery Passport) to a **Mineral-Origin Record**: lot identifier, facility, assay/fingerprint reference, transformation history, and a signed origin claim that transformation steps *append to* rather than overwrite. Deliverables: a transformation-ledger rule (blending countries cannot silently become origin countries), an origin-integrity coverage metric, and a cross-assay reconciliation rule. Scope excludes sanctions policy (*what* is restricted); this wave researches *how origin is evidenced*.

## Folder Skeleton

| Folder | Purpose | Status |
|--------|---------|--------|
| `00_Index/` | Status tracker + Synthesis (RQ answers) | Seeded |
| `01_Background/` | Regimes (export controls, minerals acts, forced-labour rules) + core concepts (origin, substantial transformation, laundering) | Skeleton |
| `02_Origin_Evidence/` | How origin is evidenced today: certificates of origin, OECD due diligence, smelter audit programs | Skeleton |
| `03_Laundering_Cases/` | Documented laundering cases and enforcement actions (minerals + chips) | Skeleton |
| `04_Tracing_Technologies/` | Physical fingerprinting + digital records (serialization, ledgers, product passports) | Skeleton |
| `05_Origin_Record_Design/` | The deliverable: Mineral-Origin Record design v0 | Skeleton |
| `06_Evidence/` | `Sources.md` (S## register) + `Findings.md` | Under construction |
| `99_Archive/` | Superseded material (never deleted) | Empty |

## Conventions

- Every factual claim in folders 01–05 cites an `S##` entry in `06_Evidence/Sources.md`.
- Reliability scale: **P** primary (peer-reviewed, official standard/regulator), **T** reputable secondary (major news, established trade press), **C** company/self-published claim (verify before relying).
- Date-stamp all findings (e.g., 2026-10-06). Superseded material moves to `99_Archive/`, never deleted.

## Working Pattern (established in Fusion Energy, approved by user)

1. Create skeleton → 2. parallel research agents → 3. fill notes citing `S##` register → 4. Stage 2 promotion when survey stabilizes.

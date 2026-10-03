# Evidence Provenance Chains for the AI-Generated Literature Era

**Wave:** 4 (`research/raw/Stage 1/Wave 4/`)
**Origin:** NR2 brainstorming session, Subject B (`research/Research ideas/NR2/BrainstormingNR2.md`, 2026-10-03)
**Protocol context:** FreeBrainstorming.md (external, universal framing — no internal project dependencies)

## Research Question

How do citation provenance chains degrade when intermediate layers (AI summaries, preprints, press releases) sit between the original finding and the citing document, and what lightweight verification protocol restores trust?

## Research Questions (decomposed)

- **RQ1 — Decay measurement:** How much does a claim's provenance chain degrade per intermediate layer (journal article → press release → news → AI summary → citing document)? Is there a measurable "provenance decay rate"?
- **RQ2 — Retraction latency vs. citation persistence:** How long do retracted or superseded findings keep circulating in downstream documents after retraction, and what factors predict persistence?
- **RQ3 — Verification protocol:** Which lightweight verification design (anchored on W3C PROV, DOIs/Crossref events, Retraction Watch data) restores trust at acceptable cost for publishers, libraries, and fact-checkers?
- **RQ4 — Cross-domain generalization:** Do the decay model and protocol transfer beyond biomedical literature (medicine → policy documents → engineering reports)?

## Method Sketch (from BrainstormingNR2.md §4 Subject B)

Longitudinal citation-chain tracing (bibliometrics); contamination sampling; propagation modeling adapted from epidemiology (R0 of a bad claim).

## Folder Skeleton

| Folder | Purpose | Status |
|--------|---------|--------|
| `00_Index/` | Status tracker and research log | Seeded |
| `01_Background/` | Core concepts: provenance, citation chains, retraction lifecycle | Skeleton |
| `02_Provenance_Standards/` | W3C PROV family, DOI/Crossref event infrastructure, Retraction Watch dataset | Skeleton |
| `03_Decay_Evidence/` | Empirical studies: preprint dynamics, retraction latency, AI-generated contamination | Skeleton |
| `04_Methods/` | Decay-rate measurement design, propagation modeling, sampling | Skeleton |
| `05_Verification_Protocol/` | The deliverable: versioned verification protocol | Skeleton |
| `06_Evidence/` | `Sources.md` (S## register) + `Findings.md` | Sources seeded (S01–S04) |
| `99_Archive/` | Superseded material (never deleted) | Empty |

## Conventions

- Every factual claim in folders 01–05 cites an `S##` entry in `06_Evidence/Sources.md`.
- Reliability scale: **P** primary (peer-reviewed, official standard/regulator), **T** reputable secondary (major news, established trade press), **C** company/self-published claim (verify before relying).
- Date-stamp all findings (e.g., 2026-10-03). Superseded material moves to `99_Archive/`, never deleted.

## Working Pattern (established in Fusion Energy, approved by user)

1. Create skeleton → 2. user confirms → 3. dispatch parallel research agents → 4. fill notes citing `S##` register → 5. Stage 2 promotion when survey stabilizes.

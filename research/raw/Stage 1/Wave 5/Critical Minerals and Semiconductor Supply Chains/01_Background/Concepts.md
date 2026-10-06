# Concepts — Core Vocabulary for Origin Integrity

_Definitions used across 02–05. Where a definition rests on a fact, it cites `[S##]` from `../06_Evidence/Sources.md`. Research pass of 2026-10-06._

## 1. Origin vs. provenance vs. traceability

Three distinct claims are routinely conflated in policy and marketing language:

- **Origin** (customs/trade-law sense): the jurisdiction or source whose identity attaches to a good for regulatory purposes — determined by rules such as substantial transformation, de minimis content thresholds, or foreign-direct-product lineage [S04, S16].
- **Provenance** (forensic sense): the evidence-backed history of *where a physical input actually came from* — established by physical witnesses (assay/isotope fingerprints) or by an intact custody record.
- **Traceability** (logistics sense): the ability to follow a lot through identified transactions — a record of *custody claims*, not proof that the claims are true.

The recurring failure mode studied in this wave: regimes verify origin with traceability (attested custody chains) and then present the result as provenance. BGR's own fingerprinting methodology states the boundary explicitly: a consistency statement between a sample and a reference database "cannot derive an affirmation about the origin" on its own [S36].

## 2. Provenance laundering (working definition from NR3 Subject G)

**A single legitimate intermediary step (refining, blending, transshipment, re-export, re-papering) re-attaches a new origin to a regulated input, defeating downstream due-diligence regimes that rely on attestation rather than traceable records.**

Structural requirements for laundering to work, distilled from the case corpus in `../03_Laundering_Cases/`:

1. **A transformation or custody step that is lawful in itself** — refining in a third country, polishing in India, re-export through the UAE (99.8% of post-ban Russian gold exports went to just three non-G7 jurisdictions) [S24].
2. **Attestation replaces physical evidence at each hand-off** — the G7 diamond regime binds stones to certificates from Mar 2024, but relies on declared provenance for rough entering intermediary hubs [S25]; refinery pools (Perth Mint) destroy mine-level provenance by blending doré from many sources, after which "refined and stamped" is not "origin verified" [S40].
3. **A jurisdiction that does not cooperate with the downstream regime** — ITSCI traceability suspended in Masisi (North Kivu) for almost all of 2024 left ~120 t/month of 3T untraced yet still exportable [S27].

## 3. Substantial transformation and rules of origin

- **Customs origin**: an item "originates" where the last substantial transformation occurred. The OFAC diamond FAQ uses exactly this language — Russian diamonds "substantially transformed in third countries" changed character for sanctions purposes [S21].
- **De minimis content thresholds** attach jurisdiction by value share: US EAR §734.4 uses 25% general / 10% sensitive-destination / 0% for certain advanced-computing items destined to China [S16]. China's Oct 2025 Announcement No. 61 introduced the mirror-image tool: a **0.1% value de minimis** for foreign-made items containing Chinese-origin rare earths — the first full-scale extraterritorial application in Chinese export-control law [S07].
- **Foreign Direct Product (FDP) rules** attach jurisdiction by *production lineage* rather than content or location — items that are the direct product of US-origin technology/software, or made in a plant that is itself such a product, are covered even when wholly made abroad [S04].
- **Ownership rules** attach jurisdiction to corporate structure: the US Sep 2025 Affiliates Rule extends Entity List restrictions to any entity ≥50% owned by listed parties [S03]; EU/US FEOC-style ownership thresholds function the same way (see `../01_Background/Regimes.md` §6).

**Observation (inference):** all four tests are *paper-computable from documents*, not from the physical object. None binds the attestation to the part.

## 4. Chain of custody vs. chain of transactions

- **Chain of custody** (forensics/logistics): an append-only record where each handler signs over the prior record; breaks are visible.
- **Chain of transactions** (trade practice): each hand-off re-issues fresh paperwork; the new certificate does not reference, preserve, or constrain itself by the old one — this is what enables re-papering.

Existing mineral schemes (OECD five-step due diligence, EU 3TG importer duties, RMI/RMAP-style smelter audits, ITSCI tagging) verify conditions *at a named mine or smelter at audit time* but do not maintain custody chains that transformations append to [S21, S22, S27]. IRMA states its own ceiling implicitly: audit results say nothing about what happens to the ore after it leaves the gate [S47].

## 5. Assurance ceilings: paper attestation → physical witness → cryptographic binding

A ladder of what each evidence class can actually prove:

| Evidence class | What it proves | Ceiling (evidence) |
|---|---|---|
| Paper attestation / audit | A party asserted something at a time | UFLPA rebuttable presumption shifts burden to importer; EU FLR has *no* presumption — the authority bears the burden and may proceed only on adverse inference [S17, S18] |
| Attested digital ledger | A record exists and participants chose to enter it | Tracr covers ~2/3 of De Beers' own production by value — a closed system [S44]; Circulor "proves a record exists, not that the record is true" [S43] |
| Physical witness (assay/isotope) | Statistical consistency with a reference deposit | BGR AFP: consistency or exclusion only; smelting fractionates Sn isotopes, complicating refined-metal matching [S39]; **no method at all for refined Ga/Ge/REE** [S41] |
| Cryptographic binding (signed manifest) | The record is tamper-evident from issuance forward | **Does not exist for hardware or minerals as of Oct 2026** — no adopted C2PA-style signed manifest standard for chips [S58]; chip ECIDs prove identity only if the verifier can electrically query the die [S55] |

The ladder is the design brief for `../05_Origin_Record_Design/`: today's regimes stop at row 1; the pilots reach row 2; row 3 exists only in fragments (BGR database, DLA DNA marking, ECID registers) and row 4 is unbuilt.

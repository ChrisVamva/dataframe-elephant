# Mineral-Origin Record — Design v0

_Covers RQ5. The subject's deliverable sketch (NR3brainstorm.md Subject G), now refined against evidence gathered in 01–04. Every design choice cites the `[S##]` precedent it adapts. Design date: 2026-10-06._

## 1. Design goal and non-goals

**Goal:** an interoperable, machine-checkable record that binds a regulated input's declared origin to production evidence and **survives transformation steps** — so that blending, refining, transshipment, and re-export append to the origin story instead of overwriting it (NR3 Subject G).

**Non-goals** (scope discipline, per the brainstorm's limitations):
- Not a sanctions policy instrument — the record does not decide *what* is restricted, only *how origin is evidenced*.
- Not a physical-marking system — physical witnesses are pluggable inputs, not the record itself.
- Not a central registry — pharma serialization shows the template works with distributed national systems over a shared identifier/event standard [S48, S49, S50].

## 2. Record schema

Adapting pharma serialization + the EU battery passport:

| Field | Adapted from |
|---|---|
| Lot identifier (unique, GS1-class, resolvable) | FMD unique identifier [S48]; GS1 GTIN/Digital Link [S50] |
| Facility identity (GLN-class) | GS1 GLN [S50] |
| Physical witness reference (assay/isotope report hash + method + lab) | BGR AFP consistency statement [S36] |
| Declared origin + claim class (attested / witnessed / reconciled) | claim-vs-attestation ladder (NR3 Subject B pattern) |
| Transformation history (append-only event list) | EPCIS 2.0 events [S50]; DSCSA transaction exchange [S49] |
| Signature chain (each handler signs over prior record) | C2PA manifest pattern [S58] |
| Passport surface (QR to structured record) | Battery Passport [S51] |

The record is **not** a blockchain: Tracr/Circulor experience shows ledgers only attest what participants enter [S44, S43]. The record is a *format + verification protocol*; storage is pluggable.

## 3. Transformation ledger rule (the core innovation)

Every physical transformation (blend, refine, alloy, transship, re-package) **appends** an event referencing the input lot(s) and output lot(s), including:

- input/output lot ratios (so a blended lot carries *both* parents — provenance dilution is recorded, not erased);
- the operator's signature;
- the transformation type from a controlled vocabulary.

**Effect on the laundering taxonomy** (`../03_Laundering_Cases/` §7): L1 (blending pool) no longer destroys identity — it produces a mixed-provenance lot; L2–L6 become visible as append events rather than fresh paperwork. A downstream buyer can compute "what fraction of this lot's ancestry is from sanctioned/flagged origins" — exactly the computation UFLPA importers must currently assert by hand [S17], and the one the DOL says polysilicon makes "extremely challenging" [S23].

## 4. Cross-assay reconciliation rule

Physical witnesses disagree across methods and labs. Rule: a lot's witness reference is valid only if **two independent methods** (e.g., LA-ICP-MS fingerprint + U-Pb age population [S36, S39]) produce consistency statements against the same declared deposit, within documented tolerance. Unreconciled single-method witnesses cap the claim class at "attested", never "witnessed".

- Honest ceiling carried from the evidence: even reconciled witnesses give *consistency, not proof* [S36]; smelting fractionation limits refined-metal matching [S39]; for refined Ga/Ge/REE there is currently **no** physical witness at all [S41] — the schema must let claim class degrade gracefully to "attested, unwitnessable at this stage" instead of pretending.

## 5. Origin-integrity coverage metric

Complementary to HHI/share metrics [S71]:

**OIC = (share of in-scope shipments whose ancestry is machine-checkable end-to-end under rule §3) × (mean claim class of those shipments)**

- Computable per supply chain, per jurisdiction, per regime — the auditable number regimes currently lack (NR3 problem statement).
- Deliberately scores zero for paper-only chains — which is the point: UFLPA detention volumes [S19, S20] and OLAF's fraud caseload [S75] measure the failure from the enforcement side; OIC measures readiness from the supply-chain side.

## 6. Assurance ceilings — what the record deliberately does not claim

1. **No truth guarantee**: signed attestations by a bad actor propagate convincingly; the record raises forgery cost and makes omission visible, it does not read minds.
2. **No refined-product witness (yet)**: until Ga/Ge/REE fingerprinting exists [S41], those stages stay attestation-only — stated, not hidden.
3. **No coverage without adoption**: pharma took a legal mandate + ~5 years [S48]; minerals have no equivalent single chokepoint authority; the EU battery passport (Feb 2027) [S51] is the nearest legislated beachhead.
4. **Operator continuity risk**: Everledger shows data dies with its operator [S45]; governance (who holds reference libraries, who runs verification hubs) is a first-order design input, not an afterthought — BGR's internal >2,000-sample library [S36] should become an internationally governed asset (NIST/USGS-class custodianship), because CRM certification without provenance libraries certifies accuracy, not origin.

## 7. Open design questions for Stage 2 / follow-up waves

1. Who governs the reference library and the verification hubs (BGR/NIST/USGS? WCO? industry consortium)? [S36]
2. Minimal-disclosure tiers: can a supplier prove compliance without revealing supplier identity (zero-knowledge ancestry ranges) — the NR3 Subject B pattern transposed?
3. Cost per lot at mine scale: pharma serialization unit economics [S48] vs artisanal 3T economics [S27] — does OIC have a viable floor for ASM?
4. Does the chip side need the same construction (ECID → fab → OSAT → board manifest) as a parallel deliverable [S55, S57, S58], or is hardware better served by procurement-chain rules (DFARS) [S54]?
5. Interaction with the battery passport's Feb 2027 deadline [S51]: is the battery CRM the pilot commodity?

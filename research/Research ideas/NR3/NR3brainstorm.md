# NR3brainstorm.md — External Brainstorming Session

## Session Metadata

- **Session Date:** 2026-10-04
- **Protocol Applied:** FreeBrainstorming.md (`Rules and Regulations/Protocols/FreeBrainstorming.md`)
- **Session Focus:** New research-subject ideation — external, universal, cross-domain framing
- **Projection Check:** No internal project references are used as analytical focus; the project is treated as a non-existent observer. No idea below requires any internal project change to be implemented, and every idea is self-contained for a team that has never seen this repository.
- **De-duplication vs. prior sessions:**
  - **New Research/1** (prompt-template effectiveness, citation-pipeline quality, notebook portability, evidence-grading comparison) — excluded.
  - **New Research/2** (agentic-AI observability, zero trust for non-human actors, SBOM/agent coupling, compliance evidence, generative-coding reproducibility) — excluded.
  - **NR2 / Wave 4** (auditing AI-curated research agendas; evidence provenance chains for AI-generated literature; funding-model effectiveness; climate-health resilience indicators; adaptive medical-AI post-market surveillance) — excluded. In particular, Subject D below concerns *authenticity of media at the point of capture*, which is a different universal problem from NR2's *citation-provenance decay* and is testable on a different corpus.
- **Reviewer Access (simulated blind review):** All references are external literature, standards bodies, regulators, and 2025–2026 policy/industry sources. At least one subject (G) is drawn from a domain unrelated to software and to the other subjects, satisfying the protocol's "external expert from an unrelated domain" review rule.

---

## 1. External Frame of Reference — Cross-Domain Trigger Map

Per Protocol §1 (Topic Generation, External Focus). Seven external domains, none overlapping prior sessions.

| # | Domain | Trigger Source (2024–2026) | Universal Problem Introduced |
|---|--------|----------------------------|------------------------------|
| 1 | **Cryptography / post-quantum migration** | NIST post-quantum standards (FIPS 203 ML-KEM, 204 ML-DSA, 205 SLH-DSA) finalized; national migration timelines (US OMB/NSA CNSA 2.0, EU, UK NCSC) phasing legacy algorithms into the 2030s; "harvest now, decrypt later" advisories | No portable instrument measures whether an organization can *find, prioritize, and replace* cryptography it cannot see |
| 2 | **AI compute governance** | Frontier-model training-compute disclosure thresholds under the EU AI Act GPAI code of practice; export-control expansions on advanced accelerators; industry proposals for compute KYC/registry schemes | Training-compute claims are unverifiable, and no interoperable record links a model release to the compute and chips that produced it |
| 3 | **Frontier-AI evaluation & assurance** | Proliferation of third-party eval organizations (AI Safety Institutes network, METR-style evaluations, HELM/leaderboard fragmentation); model updates invalidating prior evaluations; concern about benchmark contamination and "eval gaming" | Evaluations are not reproducible across evaluators, versions, or compute environments, so a safety claim cannot be independently falsified |
| 4 | **Synthetic-media authenticity** | C2PA / Content Credentials adoption by camera and editing vendors; EU AI Act Article 50 transparency duties for synthetic content; election-year deepfake incidents | Provenance is asserted at *publication*, not at *capture*; every edit, transcode, and re-upload strips or launders it |
| 5 | **Neurotechnology & neurodata** | UNESCO Recommendation on the Ethics of Neurotechnology (2025); growth of non-invasive EEG wearables and clinical brain–computer-interface trials (e.g., Synchron, Neuralink-class programs); consumer "attention/emotion inference" products | Brain-derived signals can reveal health and mental state that the wearer never knowingly disclosed; consent, retention, and incidental-finding rules are unsettled |
| 6 | **AI-enabled biology / biosecurity** | AI protein/structure design tools (AlphaFold-class successors, RFdiffusion-class models); nucleic-acid synthesis screening guidance (US screening framework updates, IGSC harmonization); dual-use concerns raised at AI-safety summits | Design tools and synthesis providers have no shared screening signal, so a harmful sequence can be ordered in a form the designer never wrote literally |
| 7 | **Critical-minerals & semiconductor supply chains** | Export controls on advanced semiconductors and tooling; critical-minerals acts and forced-labour import rules; provenance-laundering reports in mineral supply chains | "Origin" claims for regulated inputs are attested on paper, not by interoperable, auditable records; origin can be laundered through a single intermediary step |

---

## 2. Universal Problems — 17 Cross-Domain Observations (No Internal Projection)

Per Protocol §1 (Universal Problems, 10–20 items). Each is stated as if this repository never existed.

1. **Invisible cryptography:** Most organizations cannot enumerate where cryptography lives (libraries, firmware, partner APIs, OT devices), so post-quantum migration plans are estimates, not inventories.
2. **Migration-readiness has no unit:** "Our crypto is X% quantum-safe" is reported without a defined denominator, priority rule, or evidence standard; two auditors score the same estate differently.
3. **Harvest-now-decrypt-later asymmetry:** Data with decades-long confidentiality needs (health, census, IP, diplomatic) is exposed by a threat whose timeline is uncertain, while replacement cycles are 5–15 years.
4. **Unverifiable compute claims:** Frontier-training compute is self-reported; there is no standard attestation linking a released model to the accelerators, count, and duration that trained it.
5. **Compute concentration risk is unmeasured:** The same few fabs and hyperscalers supply training and serving; no portable metric expresses an organization's (or a country's) single-point-of-failure exposure.
6. **Chip-origin opacity:** Export-control and forced-labour compliance depend on origin claims that are re-attested at each hand-off, with no cryptographic binding to the physical part.
7. **Non-comparable AI evaluations:** Two safety institutes evaluating the "same" model produce results that differ by harness, prompt set, sampling, and version; there is no reproducibility contract.
8. **Evaluation gamification:** Once an eval is public, it becomes a training target; benchmarks decay into marketing, and no ledger distinguishes "passed before training data was public" from "passed after."
9. **Model-update invalidation:** Any weight refresh silently voids previous evaluations; no standard maps an evaluation to the exact artifact, so approvals persist past the thing they approved.
10. **Authenticity asserted too late:** Media provenance is attached at publication, but the decisive moment is capture; an authentic photo edited by a benign app becomes unverifiable.
11. **Provenance laundering:** Re-encoding, cropping, screen-recording, or platform re-upload strips credentials while the content keeps circulating — a "laundering" step with no counter.
12. **Detection vs. generation arms race:** Synthetic-media detectors are adversarial and degrade; policy relies on detection rather than durable provenance, which is a structural mismatch.
13. **Neural inference beyond disclosure:** Non-invasive signals can support inferences (attention, affect, drowsiness, possibly intent) that the subject never chose to reveal; the data is "given" continuously, not by an act of consent.
14. **Incidental neuro-findings:** Research and consumer devices can surface markers of neurological or psychiatric conditions; no universal duty-to-warn, retention, or deletion rule exists.
15. **Screening-signal mismatch in bio-design:** A synthesis provider sees a literal string, while an AI design tool can produce a sequence whose hazard emerges only functionally; the two sides share no interoperable screening vocabulary.
16. **Sequence-screening coverage gap:** Screening is voluntary and uneven across synthesis providers and benchtop synthesizers; no published coverage baseline exists for the fraction of global synthesis that is screened.
17. **Mineral-origin laundering:** A single legitimate intermediary step can re-paper the origin of a regulated input, defeating downstream due-diligence regimes that rely on attestation rather than traceable records.

---

## 3. Problem Reframing (Protocol §2)

- **Internal context removed:** Every problem above is phrased for "a regulator," "a standards body," "a hospital group," "a central bank," "a camera manufacturer," or "a national metrology institute" — never for this project.
- **External benchmarks used:** NIST FIPS/CNSA 2.0 (crypto), OECD AI principles and NIST AI RMF (assurance), W3C PROV and C2PA (provenance), GRADE/PRISMA (evidence synthesis analogies), ISO/IEC 27001-style management-system auditing (readiness), IEC 62443 (OT security), and OECD/JRC composite-index methods (measurement design).
- **Scope-creep guard:** No idea is framed as "how would this project do it differently." The generalization test — *"Would this work for a hospital, a bank, and a transportation authority simultaneously?"* — was applied; only subjects that pass on all three were retained.

---

## 4. Candidate Research Subjects (Protocol §3–§4 — Solution Exploration, Deliverable Format)

Each subject follows the protocol's deliverable format. An external reference point, an implementable methodology, and a no-internal-dependency limitation are mandatory.

---

### Subject A — A Migration-Readiness Instrument for Post-Quantum Cryptography

#### External Context
- **Domain:** Cryptography / critical-infrastructure security / standards.
- **Established Solutions:**
  1. NIST FIPS 203/204/205 (ML-KEM, ML-DSA, SLH-DSA) provide the destination algorithms.
  2. NSA CNSA 2.0 and counterpart national timelines provide deadlines by category.
  3. Crypto-agility guidance (e.g., ENISA, NIST NCCoE) recommends inventory-first migration.
  4. CBOM (Cryptographic Bill of Materials, CycloneDX) proposes a machine-readable crypto inventory format.
  5. ISO/IEC 27001 audit practice supplies the management-system shell.
- **Gaps Identified:**
  1. No *defined scoring unit* for migration readiness — the denominator (what is in scope) is undefined, so "X% done" is not comparable.
  2. CBOM adoption is near-zero, and there is no conformance test that says what a "complete enough" CBOM contains.
  3. No prioritized urgency model ties data-lifetime × adversary-timeline to a replacement order, so teams migrate alphabetically instead of by exposure.

#### Proposed Approach
- **Methodology:** Borrowed from metrology and management-system auditing. Define a *Migration Readiness Index* with three measured dimensions: (i) **Enumeration coverage** (share of in-scope crypto surface represented in a CBOM, verified by sampling), (ii) **Exposure interval** (data-confidentiality lifetime minus remaining time to replacement, per asset class), (iii) **Agility** (time-to-replace measured on a documented drill, not claimed).
- **Key Innovations (universal, not "new for us"):**
  - A published **scope definition** (what counts as crypto surface: algorithms, protocols, libraries, hardware roots, third-party interfaces, OT firmware).
  - A **sampling-based verification** procedure so readiness is audited, not self-reported.
  - An **urgency-ordered migration queue** produced from the exposure interval, usable by any regulated entity.
- **External Validation:** NIST/ENISA agility guidance validates inventory-first; CycloneDX CBOM validates the format layer; the metrology approach mirrors how PKI and FIPS conformance are already audited.

#### Expected Impact
- **Cross-domain applicability:** A hospital, a bank, and a transportation authority can all run the same index and compare scores.
- **Reproducible methodology:** Scope definition + sampling plan + drill + CBOM conformance checks are public artifacts.
- **Actionable for external stakeholders:** Regulators get a comparable readiness number; CISOs get a prioritized queue; auditors get a repeatable procedure.

#### Limitations (External Only)
- Scope is bounded to migration readiness, not to algorithm selection (NIST already owns that).
- Verification assumes an organization can produce some CBOM; the index deliberately does not mandate one vendor.

---

### Subject B — A Compute Bill of Materials for Verifiable Training-Compute Claims

#### External Context
- **Domain:** AI governance / compute policy / hardware supply chains.
- **Established Solutions:**
  1. Training-compute disclosure thresholds in the EU AI Act GPAI code of practice.
  2. Export-control regimes and chip-registry/KYC-compute proposals.
  3. Standardized accelerator telemetry (DCGM-class) and datacenter attestation primitives (measured boot, TPM/TEE quotes).
  4. SBOM/CBOM practice as a structural template for machine-readable component records.
- **Gaps Identified:**
  1. There is no interoperable **record format** binding a model release to a named compute envelope (accelerator type, count, hours, cluster, energy).
  2. Attestation stops at "the machine booted correctly"; nothing attests to *what training work was done*.
  3. No measurable definition of **compute-concentration exposure** for a jurisdiction or a firm.

#### Proposed Approach
- **Methodology:** Adapt software-supply-chain practice (SBOM/CBOM) and hardware attestation to a **Compute BOM**: a signed record of accelerator model, count, wall-clock and GPU-hours, cluster identifier, and a confidentiality-preserving attestation that a given training run occurred within that envelope.
- **Key Innovations:**
  - An **open record schema** plus a *minimal disclosure* tier (envelope-only) and a *verifiable* tier (attested envelope) so disclosure is possible without revealing proprietary architecture.
  - A **concentration metric** (HHI-style over fabs, accelerator lines, and hyperscalers) computable for any jurisdiction, firm, or supply contract.
  - A **claim-vs-attestation ladder** stating exactly what a regulator may infer from each tier.
- **External Validation:** Measured-boot/TPM attestation validates the trust primitive; SBOM practice validates the format; compute thresholds in the EU code of practice validate policy demand.

#### Expected Impact
- **Cross-domain applicability:** Any sector that must evidence "where did this model come from" — finance, health, defense, civil aviation.
- **Reproducible methodology:** Schema + attestation ladder + concentration formula are implementable without proprietary tooling.
- **Actionable for external stakeholders:** Regulators can accept a tier-appropriate claim; auditors can verify a tier; procurement can score concentration risk.

#### Limitations (External Only)
- Attestation of *work done* (not just hardware) remains cryptographically hard; the design states exactly where assurance weakens.
- Scope excludes compute-allocation policy, which is a political decision, not a measurement problem.

---

### Subject C — A Reproducibility Contract for Third-Party Frontier-AI Evaluation

> **Note on de-duplication:** This subject is about *evaluation reproducibility across evaluators and model versions*, not about auditing research agendas (NR2-A) or about agent observability (New Research/2).

#### External Context
- **Domain:** AI assurance / metrology / research integrity.
- **Established Solutions:**
  1. National AI Safety Institute evaluations and METR-style structured evaluation protocols.
  2. Open evaluation suites (HELM, model cards, system cards).
  3. Software-reproducibility practice (MLPerf-style harness discipline, containerized harnesses).
  4. Contamination detection methods (n-gram/MIA-style probes) from ML research.
- **Gaps Identified:**
  1. No standard **evaluation card** binds result → artifact hash → harness version → prompt set hash → sampling parameters.
  2. No ledger distinguishes pre-publication from post-publication evaluation, so benchmark decay is invisible.
  3. No shared **red-team evidence format**, so a jailbreak or capability finding cannot be re-run by a second team.

#### Proposed Approach
- **Methodology:** Reproducibility practice from metrology and MLPerf (pinned harness, seeds, containers) fused with GRADE-style evidence grading for heterogeneous findings.
- **Key Innovations:**
  - A **Reproducible Evaluation Record (RER)**: artifact hash, harness hash, prompt-set hash, sampling config, date, evaluator identity, and a signed "before/after public release" flag.
  - A **contamination ledger** that timestamps when a benchmark's items became public and whether the model could have seen them.
  - A **red-team finding format** with a minimal reproducible reproducer (inputs, config, observed behavior) and an explicit severity rubric.
- **External Validation:** MLPerf shows reproducibility discipline is feasible; contamination literature validates the ledger; existing system cards validate the artifact-hash layer.

#### Expected Impact
- **Cross-domain applicability:** The RER pattern transfers to any consequential automated assessment (aviation software, medical algorithms, financial models).
- **Reproducible methodology:** Format + ledger + reproducer template are public and tool-agnostic.
- **Actionable for external stakeholders:** Evaluators, model providers, and regulators all get a common evidence unit.

#### Limitations (External Only)
- Some capability evaluations are inherently non-reproducible (dynamic, interactive); the contract is explicitly scoped to reproducible classes and marks the rest as unverifiable.

---

### Subject D — Authentication at Capture: Reducing Authenticity Decay for Recorded Media

> **Note on de-duplication:** Distinct from NR2-B (citation-provenance decay). Here the unit is a *media asset's* authentication chain from sensor to publication; the corpus is media, not scholarly citations.

#### External Context
- **Domain:** Media integrity / consumer devices / platform governance.
- **Established Solutions:**
  1. C2PA / Content Credentials attach signed provenance manifests to assets.
  2. EU AI Act Article 50 imposes transparency duties on synthetic content.
  3. Watermarking and detector tooling from vendors and research groups.
  4. Chain-of-custody practice from digital forensics (hashing, signed envelopes).
- **Gaps Identified:**
  1. Provenance is attached at *publication*, but the decisive moment is *capture* inside the sensor; credentials added later are weaker evidence.
  2. A single benign edit (crop, transcode, platform re-upload) can strip or launder credentials; no standard defines a **survivable** chain.
  3. No published metric expresses **authenticity coverage** — the share of circulating media whose capture-to-publication chain remains verifiable.

#### Proposed Approach
- **Methodology:** Digital-forensics chain-of-custody design plus content-authenticity standard practice. Define **authentication-at-capture**: a sensor-side signed record of the capture event, and a **decay-tolerant chain** where each transformation is itself signed and appended rather than replacing credentials.
- **Key Innovations:**
  - An **Authenticity Decay Rate**: a measurable fraction of assets whose verifiable chain is intact after N transformations, computable per platform or per pipeline.
  - A **transformation-ledger** convention so edits append signed steps instead of overwriting provenance.
  - A **coverage baseline survey** method for estimating the share of circulating media with intact capture-to-publication chains.
- **External Validation:** C2PA validates the manifest format; digital forensics validates chain-of-custody; the AI Act transparency duty validates policy demand for a measurable definition of "labeled."

#### Expected Impact
- **Cross-domain applicability:** Journalism, insurance claims, legal evidence, and public-health communication all rely on authentic media.
- **Reproducible methodology:** Sensor record format + transformation ledger + decay metric are implementable by camera and platform vendors independently.
- **Actionable for external stakeholders:** Platforms can publish coverage numbers; newsrooms can state chain strength; courts get a comparable evidence grade.

#### Limitations (External Only)
- Requires device-side cooperation; the metric is still meaningful for assets that lack it (they score zero on coverage), which is the point.
- Does not attempt to judge *truth* of content, only authentication of the chain.

---

### Subject E — A Neurodata Assurance Specification for Mental-Integrity Protection

#### External Context
- **Domain:** Neurotechnology / health privacy / human rights.
- **Established Solutions:**
  1. UNESCO Recommendation on the Ethics of Neurotechnology (2025).
  2. Health-privacy regimes (HIPAA, GDPR special categories) and human-subjects research rules (IRB/ethics review).
  3. Neurorights scholarship and emerging constitutional proposals in several jurisdictions.
  4. Medical-device cybersecurity guidance for implantable and wearable devices.
- **Gaps Identified:**
  1. Neural signals support *inferences* (attention, affect, drowsiness) the subject never knowingly disclosed; no standard separates "signal given" from "state inferred."
  2. No universal duty-to-warn, retention, or deletion rule for **incidental neuro-findings** in consumer or research use.
  3. No assurance specification lets a purchaser compare two neurodevices on privacy and integrity properties.

#### Proposed Approach
- **Methodology:** Adapt informed-consent design from research ethics and control objectives from security assurance (like a "protection profile") into a **Neurodata Assurance Specification**: data classes (raw signal, derived feature, inferred state, incidental finding), permitted uses, retention limits, and required notices.
- **Key Innovations:**
  - A **four-tier neurodata taxonomy** that makes "inferred mental state" a distinct, separately governed class.
  - A **duty-to-warn protocol** with defined thresholds and a non-alarming communication format for incidental findings.
  - A **purchaser-facing assurance label** so buyers, clinics, and insurers can compare devices on integrity properties.
- **External Validation:** Health-privacy law validates special-category handling; IRB practice validates consent design; device-security guidance validates the control-objective approach.

#### Expected Impact
- **Cross-domain applicability:** Consumer wearables, clinical BCI trials, workplace safety monitoring, and education technology.
- **Reproducible methodology:** Taxonomy + notice templates + label criteria are public and jurisdiction-agnostic (adaptable to local law).
- **Actionable for external stakeholders:** Regulators get a specification; clinicians get an incident protocol; buyers get a comparable label.

#### Limitations (External Only)
- The specification is a *harmonization*, not new law; enforceability depends on adoption by regulators and device makers.
- Scope is limited to protecting mental integrity and privacy; diagnostic accuracy of devices is out of scope.

---

### Subject F — A Shared Screening Signal Between AI Bio-Design Tools and Synthesis Providers

#### External Context
- **Domain:** Biosecurity / dual-use research governance / AI-for-science.
- **Established Solutions:**
  1. Nucleic-acid synthesis screening frameworks (US screening guidance, IGSC harmonization).
  2. Dual-use research-of-concern (DURC) review policies.
  3. Sequence-similarity screening tools (BLAST-family, HMM-based) used by synthesis providers.
  4. Biosecurity-by-design proposals circulating at AI-safety summits.
- **Gaps Identified:**
  1. The designer sees sequence space; the provider sees a literal order; they share no **interoperable screening vocabulary** for functional hazards.
  2. Screening is voluntary and uneven across providers and benchtop synthesizers; no published **coverage baseline** exists.
  3. No standard **escalation handshake** when a provider's screen flags an order that the designer's tool passed.

#### Proposed Approach
- **Methodology:** Trust-and-safety interoperability design (payment fraud screening is the cross-industry analogy) plus biosecurity screening practice.
- **Key Innovations:**
  - A **Screening Signal** schema (signals: benign / review / block; evidence: functional hazard class, confidence, redaction-safe explanation) that both design tools and providers can emit.
  - A **design-tool pre-check** convention so a flagged design is caught before ordering, not after.
  - A **synthesis-screening coverage metric** measured on a documented sample of providers.
- **External Validation:** Payment-fraud screening proves shared signals reduce harm at network scale; IGSC harmonization validates the multi-provider governance model.

#### Expected Impact
- **Cross-domain applicability:** Any design-to-manufacture pipeline with dual-use inputs — chemistry, advanced materials, and bio.
- **Reproducible methodology:** Schema + pre-check + coverage survey are implementable by tool vendors and providers without centralized authority.
- **Actionable for external stakeholders:** Providers get fewer ambiguous orders; designers get early feedback; regulators get a coverage number.

#### Limitations (External Only)
- Screening reduces, never eliminates, risk; the deliverable claims coverage and false-negative handling, not perfect safety.
- Requires voluntary adoption by tool vendors and synthesis providers; no central enforcement is assumed.

---

### Subject G — An Interoperable Mineral-Origin Record Against Provenance Laundering

#### External Context
- **Domain:** Critical-minerals supply chains / trade compliance / human rights.
- **Established Solutions:**
  1. OECD Due Diligence Guidance for responsible mineral supply chains.
  2. Forced-labour import rules and conflict-minerals reporting regimes (e.g., US Dodd-Frank 1502 lineage, EU conflict-minerals regulation).
  3. Physical tracing initiatives (tagging, assay fingerprinting) for a subset of minerals.
  4. Chain-of-custody practice from food and pharmaceutical logistics (serialization, GS1 identifiers).
- **Gaps Identified:**
  1. Origin is re-attested at each hand-off; a single legitimate intermediary step can **launder** origin.
  2. No standard **record** binds a shipment's declared origin to production evidence (assay, lot, facility) in a machine-checkable way.
  3. No measurable definition of **origin-integrity coverage** for a supply chain or a jurisdiction.

#### Proposed Approach
- **Methodology:** Adapt pharmaceutical serialization and food chain-of-custody to a **Mineral-Origin Record**: lot identifier, facility, assay/fingerprint reference, transformation history, and a signed origin claim that transformation steps append to rather than overwrite.
- **Key Innovations:**
  - A **transformation ledger** where refining and blending steps mutate the record transparently, so blending countries cannot silently become origin countries.
  - An **origin-integrity coverage metric** computed over a documented sample of shipments.
  - A **cross-assay reconciliation rule** so witnesses from different measurement methods can agree on a lot identity.
- **External Validation:** Pharmaceutical serialization shows serialized chain-of-custody works at scale; OECD due diligence validates the policy frame; assay fingerprinting validates the physical witness.

#### Expected Impact
- **Cross-domain applicability:** Any regulated input with a paper origin claim — timber, fish, cotton, precursor chemicals.
- **Reproducible methodology:** Record format + ledger rule + coverage metric are implementable without a central registry.
- **Actionable for external stakeholders:** Customs, downstream manufacturers, and auditors get a machine-checkable origin claim.

#### Limitations (External Only)
- Physical witnesses are imperfect for some minerals; the design states the assurance ceiling per measurement method.
- Scope excludes sanctions policy, which determines *what* is restricted; this subject addresses *how origin is evidenced*.

---

## 5. Ranking Table

Ranked on protocol-consistent external criteria. Composite is a judgment, defended per row.

| Rank | Subject | Novelty | Cross-domain applicability | Evidence base availability | Reproducibility | Composite |
|------|---------|---------|---------------------------|---------------------------|-----------------|-----------|
| 1 | **A — Post-quantum migration-readiness instrument** | High (2026 deadlines, almost no measurement literature) | Very high (every regulated sector runs crypto) | High (public standards + CBOM + audit practice) | Very high (scope + sampling + drill are public) | **Top pick** — an auditable metric where today only narratives exist |
| 2 | **D — Authentication-at-capture / authenticity decay** | High (C2PA exists; the *decay metric* does not) | Very high (media touches every sector) | High (C2PA, forensics, AI Act text) | High (metric is a corpus computation) | Strong — clear deliverable, immediate policy user |
| 3 | **B — Compute bill of materials** | Very high (first-mover, policy-active) | High (AI governance + hardware + finance) | Medium (attestation primitives public; training-work attestation is hard) | Medium–high | Strong but harder technically; high policy pull |
| 4 | **C — Evaluation reproducibility contract** | High (many evaluators, no shared record) | High (any automated high-stakes assessment) | High (open suites, model/system cards) | High (format + ledger) | Strong, crowded field — differentiation is the "before/after public" ledger |
| 5 | **E — Neurodata assurance specification** | High (UNESCO 2025 window; no comparable label) | Medium–high (wearables → clinics → workplace) | Medium (fast-moving, jurisdictionally uneven) | Medium (taxonomy + templates) | Worthwhile; adoption, not design, is the bottleneck |
| 6 | **G — Mineral-origin record** | Medium (traceability is well studied) | High (any regulated input) | Medium–high (OECD + serialization practice) | High | Worthwhile; least novel, most immediately implementable |
| 7 | **F — Bio-design screening signal** | Very high | Medium (narrower pipeline class) | Medium (screening guidance public; coverage data thin) | Medium | Highest novelty, lowest data availability — research-heavy |

**Tie-break rule applied (protocol-consistent):** broader external stakeholder base > immediate implementability > novelty.

---

## 6. Exit Criteria Check (Protocol §Exit Criteria)

- ✅ Every idea in §4 has at least one external reference point (a standard, a regulator, a published practice, or a peer-reviewed field).
- ✅ No idea requires internal project changes to be implemented — all seven are implementable by any team with public or obtainable data.
- ✅ Each idea is understandable by someone unfamiliar with this project (§4 formulations are self-contained and name no repository artifact).

---

## 7. Recommended Next Steps (External)

1. **Choose a subject.** The ranking suggests **A** (post-quantum migration-readiness instrument) as the top pick, with **D** (authentication-at-capture) as the strongest immediate-policy alternative, and **B** (compute BOM) as the highest-novelty/highest-policy-pull option.
2. **Promote the chosen subject** into the house numbered research-folder skeleton (`00_Index … 99_Archive`) with an `S##` source register, following the conventions established in the Fusion Energy and Wave 4 folders.
3. **Seed the Stage-1 source register** for the chosen subject:
   - **A:** NIST FIPS 203/204/205, NSA CNSA 2.0, ENISA crypto-agility guidance, CycloneDX CBOM spec, ISO/IEC 27001.
   - **D:** C2PA specification, EU AI Act Article 50 text, digital-forensics chain-of-custody standards, platform transparency reports.
   - **B:** EU AI Act GPAI code of practice, export-control registry proposals, TPM/TEE attestation specs, SBOM/CBOM formats.
4. **Run a blind external review** with at least one reviewer from an unrelated domain (for Subject A, a supply-chain or clinical auditor; for Subject E, a civil-liberties lawyer) before committing to a full research wave.

---

**Protocol Status:** FreeBrainstorming.md applied; external-only deliverables.
**Internal Project Impact:** None required; these session notes are self-contained for any external team.
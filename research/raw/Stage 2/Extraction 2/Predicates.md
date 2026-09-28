---
stage: 2
created: 2026-09-28
extracted_from:
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/00 Smart Homes Key Technology Trends - Index.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUpResearch_Questions.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/Sources & Methods/Source Register.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/01 Matter & Interoperability/Matter and Thread as the Connectivity Foundation.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/02 AI & Voice Control/From Voice Commands to Contextual Home Agents.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/03 Energy & Sustainability/Smart Homes as Flexible Energy Systems.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/04 Security & Privacy/Security and Privacy as Lifecycle Architecture.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Untitled/Untitled.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Category-by-Category Assessment/Category-by-Category Assessment.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances/Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Device Types & Feature Consistency/Device Types & Feature Consistency.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Dominant Barriers Cost, Privacy, and Setup Outweigh Subscriptions/Dominant Barriers Cost, Privacy, and Setup Outweigh Subscriptions.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Home-AI Intent Interpretation and Action Safety Benchmark/Home-AI Intent Interpretation and Action Safety Benchmark.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Reproducible Test Protocol/Reproducible Test Protocol.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Safe Autonomy vs. Required Confirmation/Safe Autonomy vs. Required Confirmation.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Smart-Home Product Security and Privacy Lifecycle Scorecard/Smart-Home Product Security and Privacy Lifecycle Scorecard.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Support Periods and Update Mechanisms by Device Category/Support Periods and Update Mechanisms by Device Category.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/What Savings Are Measured Rather Than Claimed/What Savings Are Measured Rather Than Claimed.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Which Advantages Survive Standardization/Which Advantages Survive Standardization.md
extractor: stage2-extractor-agent
gate_results:
  gate_1_source_coverage: pass
  gate_2_claim_traceability: pass
  gate_3_evidence_class_integrity: pass
  gate_4_metric_conditions: pass
  gate_5_entity_completeness: pass
  gate_6_extraction_log_completeness: pass
  gate_7_ingestibility: pass
---

# Predicates — Wave 2 (Smart Homes: Key Technology Trends)

Extracted per `Rules and Regulations/Protocols/TransitionStage2.md` §4 Step 4. Only relationships stated explicitly in Stage 1 are recorded; prose that merely implies a relationship is excluded and noted in `ExtractionLog.md`. The `Direction` column states which way the subject-object relation is asserted (`subject -> object`). `Example (from Stage 1)` copies the Stage 1 wording.

| Predicate | Subject type | Object type | Direction | Example (from Stage 1) | Stage 1 source |
| --- | --- | --- | --- | --- | --- |
| implemented_by | Standard | Ecosystem implementation | Matter -> ecosystem implementations | "Matter is the application-layer standard intended to let devices work across ecosystems." | Matter and Thread as the Connectivity Foundation.md |
| complements | Technology (mesh network) | Technology (transport) | Thread -> Wi-Fi/Ethernet | "Thread is a low-power, IP-based mesh network that complements Wi-Fi and Ethernet for constrained devices." | Matter and Thread as the Connectivity Foundation.md |
| bridges | Device (border router) | Network boundary | Thread Border Router -> Thread mesh and IP home network | "Border routers and home routers: bridge Thread to the IP home network." | Matter and Thread as the Connectivity Foundation.md |
| added_support_for | Standard version | Device types | Matter 1.4 -> solar, batteries, heat pumps, water heaters, EV charging, device energy management | "Matter 1.4 added ... support for solar, batteries, heat pumps, water heaters, EV charging, and device energy management." | Matter and Thread as the Connectivity Foundation.md |
| enables | Standard capability | Ecosystem set | Joint Fabric -> ecosystems co-managing one Matter network | "Matter 1.6's Joint Fabric enables ecosystems to co-manage a single Matter network, removing the need to onboard devices separately on each platform." | Untitled.md |
| reduces | Standardisation | Integration friction | Standardization -> integration friction (down) | "Standardization reduces integration friction but can commoditize basic device features." | Matter and Thread as the Connectivity Foundation.md |
| commoditizes | Standard | Device control layer | Matter -> basic device control | "Matter has commoditized device control." | Untitled.md |
| orchestrates | Product (assistant) | Services and devices | Alexa+ -> services and devices | "Amazon describes Alexa+ as a generative-AI assistant that orchestrates across services and devices." | From Voice Commands to Contextual Home Agents.md |
| reports_through | Device | Platform | Matter-certified device -> smart home platform | "A Matter-certified device typically reports through the smart home platform." | Which Advantages Survive Standardization.md |
| requires | Action tier | Confirmation control | Physical-security actions -> secondary user verification | "Google Home's developer documentation mandates secondary user verification (e.g., PIN or NFC keyfob proximity) for unlocking, disarming, or opening these device types." | Safe Autonomy vs. Required Confirmation.md |
| enforces | Authorization layer | Household policy | authorization layer -> household policy | "It should propose actions to an authorization layer that enforces household policy." | Support Periods and Update Mechanisms by Device Category.md |
| separates | LLM intent interpretation | Authorization enforcement | intent interpretation -> authorization enforcement (separated) | "Separate LLM intent from authorization enforcement." | Home-AI Intent Interpretation and Action Safety Benchmark.md |
| establishes | Regulation | Lifecycle cybersecurity requirement | Cyber Resilience Act -> product lifecycle cybersecurity obligations | "The EU Cyber Resilience Act establishes lifecycle cybersecurity requirements for products with digital elements." | Security and Privacy as Lifecycle Architecture.md |
| applies_from | Regulation obligation | Date | CRA major obligations -> December 2027 | "with major obligations applying from December 2027" | Security and Privacy as Lifecycle Architecture.md |
| recommends | Guidance | Controls | NIST -> planning before purchase, MFA, unique passwords, disabling unused features, privacy review, automatic updates, network segmentation | "NIST recommends planning before purchase, MFA, unique passwords, disabling unused features, privacy review, automatic updates, and network segmentation." | Security and Privacy as Lifecycle Architecture.md |
| requires_only | Regulation (SB-327) | Minimum control | California SB-327 -> "reasonable security feature" | "California SB-327 requires only a 'reasonable security feature,' which in practice means no default password." | Support Periods and Update Mechanisms by Device Category.md |
| publishes | Vendor | Support period | Google Nest -> 5-year automatic security updates | "Google Nest devices receive automatic security updates for at least five years." | Support Periods and Update Mechanisms by Device Category.md |
| retains | Platform | User data | Google -> Gemini for Home activity 18 months; Amazon -> recordings 3 or 18 months | "Google retains Gemini for Home activity for 18 months by default; Amazon retains recordings for 3 or 18 months." | Support Periods and Update Mechanisms by Device Category.md |
| measured_by | Energy flexibility | Field trials | flexibility -> field trials and utility programmes | "Field trials and utility programs now provide hard numbers for peak reduction, cost savings, and comfort impacts." | What Savings Are Measured Rather Than Claimed.md |
| reduces | Automatic control | Peak-hour load | automatic EV charging control -> DR event-hour load (11.8% vs 0.4% manual) | "stations with automatic controls achieved an average 11.8% reduction during DR event hours, while manual adjustments yielded only 0.4%" | What Savings Are Measured Rather Than Claimed.md |
| dominates | DR incentive level | Flexibility economics | DR compensation -> economics of coordinated flexibility | "The economics of coordinated flexibility are dominated by the value of demand response compensation, not by energy arbitrage alone." | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md |
| is_weakest_link_of | Battery storage | Flexibility economics | Battery storage -> flexibility economic case | "Battery storage is the weakest economic link for flexibility alone." | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md |
| bears | Consumers | Comfort and equipment-life burden | consumers -> comfort, equipment-life, administrative burdens | "consumers bear the comfort, equipment-life, and administrative burdens with uncertain and variable compensation" | What Savings Are Measured Rather Than Claimed.md |
| captures | Utilities and aggregators | Value share | utilities and aggregators -> largest and most certain value | "utilities and aggregators capture the largest and most certain value" | What Savings Are Measured Rather Than Claimed.md |
| blocks | Setup complexity | Adoption | setup and connectivity issues -> DIY adoption | "Setup and connectivity issues affect more than half of DIY users." | Dominant Barriers Cost, Privacy, and Setup Outweigh Subscriptions.md |
| overstates | Device counts | Engagement | registered device counts -> engagement (2-3x) | "Device counts overstate engagement by 2-3x." | Which Advantages Survive Standardization.md |
| mitigates | Local control | Cloud-dependency risk | local control -> cloud dependency, latency, privacy, shutdown and subscription-gating risk | "Every tension involving cloud dependency - latency, privacy, shutdown risk, subscription gating - is mitigated by local control." | Untitled.md |
| invalidates | Ownership transfer | Old credentials | ownership transfer -> prior authentication tokens | "Ownership transfer must invalidate old credentials." | Smart-Home Product Security and Privacy Lifecycle Scorecard.md |
| erases | Factory reset | Credentials and biometric templates | factory reset -> Wi-Fi credentials, cloud tokens, biometric templates, access schedules, device configuration | "Factory reset must erase: Wi-Fi credentials, cloud tokens, biometric templates, access schedules, and device configuration." | Smart-Home Product Security and Privacy Lifecycle Scorecard.md |
| certifies_only | Certification | Protocol conformance | Matter certification -> specification conformance (not ecosystem compatibility) | "Matter certifies protocol conformance, not ecosystem compatibility." | Smart-Home Product Security and Privacy Lifecycle Scorecard.md |
| prevents | Network isolation | Lateral movement | network isolation -> lateral movement (limits it) | "Limits lateral movement" | Smart-Home Product Security and Privacy Lifecycle Scorecard.md |
| determines | Update delivery | Vulnerability window | update delivery -> vulnerability window | "Determines vulnerability window" | Smart-Home Product Security and Privacy Lifecycle Scorecard.md |
| determines | Support-period disclosure | Informed purchasing | support-period disclosure -> informed purchasing | "Enables informed purchasing" | Smart-Home Product Security and Privacy Lifecycle Scorecard.md |
| limits | Data retention | Exposure duration | data retention -> exposure duration | "Limits exposure duration" | Smart-Home Product Security and Privacy Lifecycle Scorecard.md |
| determines | End-of-life handling | Device fate after support | end-of-life handling -> device fate post-support | "Determines device fate post-support" | Smart-Home Product Security and Privacy Lifecycle Scorecard.md |
| grants | Biometric access control | Physical access | biometric access control -> door access (conditional on liveness detection) | "Require 3D structured light or equivalent liveness detection for any biometric access control product." | Support Periods and Update Mechanisms by Device Category.md |
| demonstrates_absence_of | Compliance signal | Practical safety | certification, regulation and policy signals -> practical household protection (not demonstrated) | "The following table identifies cases where a product or category can achieve formal compliance while failing to protect the household." | Smart-Home Product Security and Privacy Lifecycle Scorecard.md |
| constrains | Comfort and safety constraints | Energy optimisation | comfort and safety constraints -> optimisation decisions | "Make comfort and safety constraints explicit; optimization must not silently override them." | Smart Homes as Flexible Energy Systems.md |
| supports | Local control model | Consumer protection | Matter local control -> consumer protection against cloud dependency | "Matter's local control model is the most valuable consumer protection in the standard, but it is unevenly implemented and often disabled by default." | Untitled.md |
| depends_on | Consumer value share | Tariff and participation conditions | consumer share of flexibility value -> TOU differential, participation, override and degradation conditions | "this depends on: TOU tariff differential remaining wide (peak/off-peak ratio >3:1) ..." | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md |
| tested_by | Certification | Multi-admin and outage scenarios | current certification -> multi-admin pairing, state consistency, local control during outage, border router recovery (not tested) | "Extend certification to include multi-admin and outage scenarios." | Reproducible Test Protocol.md |
| standardizes | Standard | Device control | Matter -> device control, not intelligence or data access | "Matter standardizes device control, not intelligence." | Category-by-Category Assessment.md |

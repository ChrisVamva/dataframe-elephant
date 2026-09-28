---
stage: 2
created: 2026-09-28
extracted_from:
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/00 Smart Homes Key Technology Trends - Index.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUpResearch_Questions.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/Sources & Methods/Source Register.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/Sources & Methods/Category Note Template.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/01 Matter & Interoperability/Matter and Thread as the Connectivity Foundation.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/02 AI & Voice Control/From Voice Commands to Contextual Home Agents.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/03 Energy & Sustainability/Smart Homes as Flexible Energy Systems.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/04 Security & Privacy/Security and Privacy as Lifecycle Architecture.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/05 Emerging Product Categories/Emerging Product Categories and Platform Shifts.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/06 Business Customer Investor Lens/Business Customer and Investor Implications.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/Research Orientation/Advanced Security Features.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/Research Orientation/AI Integration & Voice Control.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/Research Orientation/Emerging Product Categories.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/Research Orientation/Matter Protocol Standardization.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/Research Orientation/Questions by Perspective.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/Research Orientation/Sustainability & Energy Management.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/Prompts/README.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/FollowUp Research Evaluation.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Untitled/Untitled.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Category-by-Category Assessment/Category-by-Category Assessment.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances/Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Device Types & Feature Consistency/Device Types & Feature Consistency.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Dominant Barriers Cost, Privacy, and Setup Outweigh Subscriptions/Dominant Barriers Cost, Privacy, and Setup Outweigh Subscriptions.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Home-AI Intent Interpretation and Action Safety Benchmark/Home-AI Intent Interpretation and Action Safety Benchmark.md
  - research/raw/Stage 1/Wave 2/SmartHomes_Key_Tech_Trends/FollowUp/Mixed-Method Study Design Smart-Home Adoption, Retention, and Willingness to Pay/Mixed-Method Study Design Smart-Home Adoption, Retention, and Willingness to Pay.md
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

# Entities — Wave 2 (Smart Homes: Key Technology Trends)

Extracted per `Rules and Regulations/Protocols/TransitionStage2.md` §4 Step 3. Every row carries the boundary Stage 1 states ("what it is not"); where Stage 1 does not state a boundary, the cell reads `[boundary not stated in source]` and the row is listed in `ExtractionLog.md` under `boundary_absent`. Confidence follows the Stage 1 evidence discipline (`Documented fact` = high, `Synthesis` = medium, vendor/forecast material = low).

| Entity ID | Canonical name | Type | Boundary (what it is not) | Stage 1 source | Section | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| E001 | Matter | Standard (application layer) | Compatibility infrastructure, explicitly "not a guarantee of identical user experiences" | Matter and Thread as the Connectivity Foundation.md | Design rules | high |
| E002 | Thread | Technology (low-power IP mesh network) | Complements Wi-Fi and Ethernet; not a replacement for higher-bandwidth transport | Matter and Thread as the Connectivity Foundation.md | Core idea | high |
| E003 | Wi-Fi/Ethernet | Technology (transport) | Higher-bandwidth transport for hubs, appliances and cameras; not the constrained-device mesh | Matter and Thread as the Connectivity Foundation.md | Architecture | high |
| E004 | Thread Border Router | Device / network role | Bridges Thread to the IP home network; not the Thread mesh itself; "a single point of failure" | Matter and Thread as the Connectivity Foundation.md | Architecture | high |
| E005 | Multi-admin | Standard capability | Shares devices across fabrics; it does not make routines or permissions portable | Matter and Thread as the Connectivity Foundation.md | Design rules | high |
| E006 | Matter 1.4 | Standard version | "Matter 1.4 and 1.4.2 addressed some interoperability gaps" but Joint Fabric arrived later; not the joint-fabric generation | Matter and Thread as the Connectivity Foundation.md | Documented developments | high |
| E007 | Matter 1.5 | Standard version | Adds camera and energy-device clusters; not the version that introduces Joint Fabric | Device Types & Feature Consistency.md | Device Types & Feature Consistency | high |
| E008 | Matter 1.6 | Standard version | Introduces NFC commissioning and Joint Fabric, but "ecosystem support for Joint Fabric is not yet widespread" | Device Types & Feature Consistency.md | Device Types & Feature Consistency | high |
| E009 | Joint Fabric | Standard capability | Co-manages a single Matter network across ecosystems; "may also reduce ecosystem stickiness" and does not equalise AI features | Untitled.md | 1. Interoperability vs. Differentiation and Ecosystem Lock-In | medium |
| E010 | Matter certification | Assurance scheme | "Matter certifies protocol conformance, not ecosystem compatibility" | Smart-Home Product Security and Privacy Lifecycle Scorecard.md | Where Compliance Does Not Demonstrate Practical Safety | high |
| E011 | PASE commissioning | Security mechanism | Commissioning-time assurance only; does not cover operational security over device life | Support Periods and Update Mechanisms by Device Category.md | Low Risk | medium |
| E012 | Device attestation | Security mechanism | "Current model trusts devices for life after attestation"; no built-in revocation | Smart-Home Product Security and Privacy Lifecycle Scorecard.md | Priority 3 | medium |
| E013 | Home Assistant | Software (local controller) | A reference local controller, not one of the four ecosystems under test | Reproducible Test Protocol.md | Scope and Inventory | high |
| E014 | Apple Home | Platform / ecosystem | One of four ecosystems; "Apple and Google have been slower to implement camera support" | Reproducible Test Protocol.md | Scope and Inventory | high |
| E015 | Google Home | Platform / ecosystem | One of four ecosystems; retains Gemini for Home activity for 18 months by default | Reproducible Test Protocol.md | Scope and Inventory | high |
| E016 | Amazon Alexa | Platform / ecosystem | One of four ecosystems; "Amazon Echo did not fully support multi-admin" in testing | Device Types & Feature Consistency.md | Optional Features, Extensions, and Certification Gaps | high |
| E017 | Samsung SmartThings | Platform / ecosystem | First platform to fully support Matter cameras; "supports 58 Matter device types, but other platforms may support fewer" | Device Types & Feature Consistency.md | Device Types & Feature Consistency | high |
| E018 | Alexa+ | Product (generative-AI assistant) | A vendor capability claim, not independent proof of performance | From Voice Commands to Contextual Home Agents.md | Documented developments | medium |
| E019 | Gemini for Home | Product (generative-AI assistant) | A vendor capability claim covering conversational control, automation creation and camera summaries | From Voice Commands to Contextual Home Agents.md | Documented developments | medium |
| E020 | Voice match / household identity | Mechanism | Links a voice profile to an account; not a complete permission model for guests or children | Safe Autonomy vs. Required Confirmation.md | Ambiguity, Household Identities, Guests, Children, and Adversarial Commands | medium |
| E021 | Home graph | Architecture pattern | Devices, rooms, people, routines and permissions context; not an action channel | From Voice Commands to Contextual Home Agents.md | Architecture patterns | medium |
| E022 | Tool/action layer | Architecture pattern | Bounded commands with confirmation rules; not free-form actuation | From Voice Commands to Contextual Home Agents.md | Architecture patterns | medium |
| E023 | Risk-tiered autonomy | Design principle | Deny-by-default above the reversible tier; not full autonomy for consequential actions | Home-AI Intent Interpretation and Action Safety Benchmark.md | Minimum Guardrails | medium |
| E024 | Deterministic authorization layer | Architecture component | Enforces household policy after the LLM proposes; the AI "should never directly actuate devices" | Support Periods and Update Mechanisms by Device Category.md | Product-Design Implications | medium |
| E025 | Confirmation requirement (human-in-the-loop) | Design rule | Applies to physical-security, camera and automation-creation actions; not to low-risk reversible actions | Safe Autonomy vs. Required Confirmation.md | Safe Autonomy vs. Required Confirmation | medium |
| E026 | Prompt injection | Threat | Arrives through calendar, email, messaging and notification surfaces; not only a model-quality defect | Support Periods and Update Mechanisms by Device Category.md | Product-Design Implications | medium |
| E027 | Biometric access control | Product category | No mandatory liveness standard for consumer biometric access; printed photos unlock some smart locks | Support Periods and Update Mechanisms by Device Category.md | High Risk | medium |
| E028 | Smart lock | Device category | 3-5 years minimum expected support (CRA floor) and "often undocumented" | Support Periods and Update Mechanisms by Device Category.md | Support Periods and Update Mechanisms by Device Category | medium |
| E029 | Smart security camera | Device category | 5 years stated explicitly by Google Nest; "Apple does not publish a fixed period" | Support Periods and Update Mechanisms by Device Category.md | Support Periods and Update Mechanisms by Device Category | medium |
| E030 | Hub | Device category | Supported 3 years (IKEA), 4 (Google), 5 (Amazon); "if the hub fails, the entire home's intelligence fails" | Support Periods and Update Mechanisms by Device Category.md | Support Periods and Update Mechanisms by Device Category | medium |
| E031 | Home router as smart-home controller | Product category | "router-based controllers are less capable than dedicated hubs for complex automation, local AI, or multi-protocol bridging" | Category-by-Category Assessment.md | 2. Home Routers as Smart Home Controllers | medium |
| E032 | Smart thermostat | Device category | "a 'smart' controller solely focused on precise indoor temperature control did not guarantee energy savings and potentially jeopardized equipment" | What Savings Are Measured Rather Than Claimed.md | What Savings Are Measured Rather Than Claimed? | high |
| E033 | Heat pump (HVAC) | Device / asset | Shows substantial post-event snapback and comfort penalties; not a pure savings device | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md | 2. Device-Level Flexibility Modeling | high |
| E034 | Heat pump water heater (HPWH) | Device / asset | Strongest field evidence for load shifting, but benefit depends on utilization rates; low-demand households see negligible benefit | What Savings Are Measured Rather Than Claimed.md | What Savings Are Measured Rather Than Claimed? | high |
| E035 | EV charging | Device / asset | "the most automation-sensitive load"; manual adjustments yielded only 0.4% reduction | What Savings Are Measured Rather Than Claimed.md | What Savings Are Measured Rather Than Claimed? | high |
| E036 | Battery storage | Device / asset | "the weakest economic link for flexibility alone"; value is backup power and solar self-consumption | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md | Payback and NPV | high |
| E037 | Solar PV | Device / asset | Self-consumption 40-60% under net billing; PV owners show a weaker peak-pricing response | What Savings Are Measured Rather Than Claimed.md | What Savings Are Measured Rather Than Claimed? | high |
| E038 | Flexible appliances | Device / asset | [boundary not stated in source] | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md | 2. Device-Level Flexibility Modeling | medium |
| E039 | Home energy management system (HEMS) | Product category | [boundary not stated in source] | Category-by-Category Assessment.md | 3. Energy Controllers / Home Energy Management Systems (HEMS) | medium |
| E040 | Demand response (DR) | Programme / mechanism | Requires a utility or aggregator signal path; distinct from bill arbitrage alone | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md | 1. System Boundary and Baseline | high |
| E041 | CTA-2045 | Standard / interface | A port-and-commissioning interface for water heaters; not a whole-home control standard | What Savings Are Measured Rather Than Claimed.md | Product-Design Implications | medium |
| E042 | OpenADR 3 | Standard / interface | Carries utility signals; "Do not claim 'Matter-native demand response' until the OpenADR bridge is commercially available and tested" | What Savings Are Measured Rather Than Claimed.md | Product-Design Implications | medium |
| E043 | Time-of-use (TOU) tariff | Tariff | "TOU is the workhorse; RTP adds complexity without proportional benefit for most households" | What Savings Are Measured Rather Than Claimed.md | Product-Design Implications | medium |
| E044 | Real-time pricing (RTP) | Tariff | [boundary not stated in source] | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md | 3. Tariff and Incentive Structures | medium |
| E045 | Aggregator | Role | Earns 15-25% of DR revenue; not the utility or grid operator | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md | 1. System Boundary and Baseline | medium |
| E046 | Utility / grid operator | Role | Captures the highest share of value; does not bear the comfort and equipment-life burden | What Savings Are Measured Rather Than Claimed.md | Who Receives the Value? | medium |
| E047 | Cyber Resilience Act (CRA) | Regulation | "does not apply until December 2027"; the five-year floor is "not a default"; does not address agentic risks such as goal drift and memory poisoning | Support Periods and Update Mechanisms by Device Category.md | The practical gap | high |
| E048 | NIST guidance | Guidance | User-centred tips and recommendations; not a certification or a mandatory rule | Security and Privacy as Lifecycle Architecture.md | Documented developments | high |
| E049 | FTC guidance | Guidance | Consumer security guidance; not a lifecycle mandate | Security and Privacy as Lifecycle Architecture.md | Sources | high |
| E050 | UK PSTI | Regulation | "requires disclosure of a support period, but does not mandate a minimum length" | Smart-Home Product Security and Privacy Lifecycle Scorecard.md | Where Compliance Does Not Demonstrate Practical Safety | high |
| E051 | California SB-327 | Regulation | Requires only a "reasonable security feature"; the US has no comparable federal lifecycle mandate | Support Periods and Update Mechanisms by Device Category.md | The practical gap | high |
| E052 | US Cyber Trust Mark | Labelling programme | A QR-code product registry; ioXt Alliance is Lead Administrator, replacing UL Solutions | Smart-Home Product Security and Privacy Lifecycle Scorecard.md | Priority 3 | medium |
| E053 | ioXt Alliance | Organisation | Meaningful only "for manufacturers who adopt" its NIST-aligned design practices | Support Periods and Update Mechanisms by Device Category.md | Low Risk | medium |
| E054 | Vulnerability disclosure programme (VDP) | Process | "A public bug bounty does not guarantee timely fixes"; enforcement and response SLAs remain inconsistent | Smart-Home Product Security and Privacy Lifecycle Scorecard.md | Priority 2 | medium |
| E055 | Matter OTA | Update mechanism | Requires manufacturer-signed firmware and "has limitations in sequential updates and recovery" | Support Periods and Update Mechanisms by Device Category.md | Interoperability and Lifecycle Risk Assessment | medium |
| E056 | AI hub (local AI brain) | Product category | "platform-specific in their intelligence layer - the automation logic does not migrate"; not a mass-market category | Category-by-Category Assessment.md | 1. AI Hubs (Local AI Brains) | medium |
| E057 | Anker MindBase | Product | Vendor-positioned specification claims (48TB, 26 TOPS); "too new for retention data" | Category-by-Category Assessment.md | 1. AI Hubs (Local AI Brains) | low |
| E058 | Apple Home Hub (J490) | Product (rumoured) | Estimated at $349-$400 and not released as of the research date | Category-by-Category Assessment.md | 1. AI Hubs (Local AI Brains) | low |
| E059 | FRITZ!Box 5690 Pro | Product | Acts as a Matter bridge; not a full automation hub | Category-by-Category Assessment.md | 2. Home Routers as Smart Home Controllers | low |
| E060 | eero Pro 7 | Product | Built-in Zigbee/Thread radios at no premium, but "less capable" for complex automation and local AI | Category-by-Category Assessment.md | 2. Home Routers as Smart Home Controllers | low |
| E061 | Security monitoring subscription | Revenue model | Residential security providers "typically expect 11-14% of monitoring subscribers to cancel each quarter" | Dominant Barriers Cost, Privacy, and Setup Outweigh Subscriptions.md | Subscription fatigue | medium |
| E062 | Occupancy-Energy Optimization | Data-fusion service category | Combines occupancy and energy signals; not a single device | Category-by-Category Assessment.md | A. Occupancy-Energy Optimization | medium |
| E063 | Security-Energy Coordination | Data-fusion service category | [boundary not stated in source] | Category-by-Category Assessment.md | B. Security-Energy Coordination | medium |
| E064 | Aging-in-Place / CareTech | Product category | "Cameras in private spaces are unacceptable; radar, mmWave, and appliance-usage sensing are preferred" | Category-by-Category Assessment.md | C. Aging-in-Place / CareTech | medium |
| E065 | Equipment-Protective Demand Response | Data-fusion service category | Must guarantee equipment life while delivering savings; otherwise no defensible position | Category-by-Category Assessment.md | D. Equipment-Protective Demand Response | medium |
| E066 | ActiveHousehold | Metric | "The absence of a canonical 'ActiveHousehold' metric obscures the true state of adoption" | Which Advantages Survive Standardization.md | Measurement Inconsistency: Device Counts vs. Active Homes vs. Savings | medium |
| E067 | LCODR (levelised cost of demand response) | Metric | A cost-competitiveness measure; not a customer-facing price | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md | Payback and NPV | medium |
| E068 | Automation routine | Artefact | "routines and permissions are not portable" between ecosystems | Support Periods and Update Mechanisms by Device Category.md | Product-Design Implications | medium |
| E069 | Lifecycle control | Assessment unit | 14-control rubric; the composite score is a preliminary framework until independently verified | Smart-Home Product Security and Privacy Lifecycle Scorecard.md | Scoring Rubric | medium |
| E070 | Evidence taxonomy (Documented fact / Synthesis / Recommendation) | Methodology | "Vendor announcements are treated as capability claims, not independent validation" | Source Register.md | Evidence discipline | high |
| E071 | Mixed-method study design | Methodology (proposed) | A design and plan only; "Convert the adoption study design into an actual protocol" remains outstanding | Mixed-Method Study Design Smart-Home Adoption, Retention, and Willingness to Pay.md | 1. Study Architecture | medium |
| E072 | Home-AI intent benchmark | Methodology (synthesised) | "synthesizes published research from multiple systems and benchmarks. It does not represent a single controlled test run" | Home-AI Intent Interpretation and Action Safety Benchmark.md | Limitations | medium |
| E073 | Interoperability test protocol | Methodology | "a synthesis, not a single controlled laboratory experiment"; "No single test in this matrix has been independently replicated" | Reproducible Test Protocol.md | Limitations | medium |
| E074 | Lifecycle security scorecard | Methodology | "a preliminary framework until each rating is independently verified" | FollowUp Research Evaluation.md | Important interpretation warnings | medium |
| E075 | Z-Wave | Technology | A mature protocol comparison point; not a Matter-certified ecosystem and not IP-native | Device Types & Feature Consistency.md | Matter/Thread vs. Zigbee, Z-Wave, and Proprietary Systems (5-10 Year Outlook) | medium |
| E076 | Zigbee | Technology | Mature mesh with excellent battery life; not IP-native and not the Matter application layer | Device Types & Feature Consistency.md | Matter/Thread vs. Zigbee, Z-Wave, and Proprietary Systems (5-10 Year Outlook) | medium |
| E077 | Proprietary ecosystem systems | Technology class | "offer the best user experience within their walled gardens but lock users in and carry long-term EOL risk" | Device Types & Feature Consistency.md | Matter/Thread vs. Zigbee, Z-Wave, and Proprietary Systems (5-10 Year Outlook) | medium |
| E078 | Circles of Trust | Proposed authorization framework | "no commercial product implements fine-grained permissions" | Reproducible Test Protocol.md | Evidence Gaps Requiring Further Testing | medium |
| E079 | Compliance without safety | Failure pattern | A flagged rating pattern (CM 0-1 with EQ 2-3), not a certification level | Smart-Home Product Security and Privacy Lifecycle Scorecard.md | Scoring Rubric | medium |
| E080 | Matter compliance without Matter interoperability | Failure pattern | The device is "technically 'compatible' but practically non-functional" | Untitled.md | 1. Interoperability vs. Differentiation and Ecosystem Lock-In | medium |
| E081 | Data-fusion layer | Architecture layer | "the most defensible new categories are not devices-they are services that combine occupancy, energy, security, and appliance data into outcomes no single device can deliver" | Category-by-Category Assessment.md | Strategic Implications | medium |
| E082 | Home energy flexibility model | Methodology (model) | A modelled baseline and scenario model, not measured results; the Swiss pilot suggests winter assumptions may be optimistic | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md | 6. Sensitivity Analysis | medium |

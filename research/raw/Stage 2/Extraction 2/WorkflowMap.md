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

# WorkflowMap — Wave 2 (Smart Homes: Key Technology Trends)

Extracted per `Rules and Regulations/Protocols/TransitionStage2.md` §4 Step 7. Stable names are used exactly as Stage 1 states them. Wave 2 is itself a research and validation programme rather than a data pipeline, so the stages below are the research workflow stages that Stage 1 defines: orientation, source collection, lens synthesis, question prioritisation, follow-up packages, the test protocol, the AI safety benchmark, the energy flexibility model, lifecycle scoring, the adoption study, the evidence audit, and decision synthesis. `Roles` and `Tools` are populated only where Stage 1 explicitly assigns them; `[not stated in source]` marks cells Stage 1 leaves empty (see `ExtractionLog.md` entry L050).

| Stage ID | Stage name | Inputs | Activities | Outputs | Quality gates | Roles | Tools | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W1 | Research Orientation and Hypothesis Framing | Research Orientation notes; Questions by Perspective | State the research questions and hypotheses for each perspective | Orientation notes and question sets | The original prompts "are treated as research hypotheses, not established facts"; each question names the perspective it serves | Researcher (business, customer, investor perspectives) | [not stated in source] | 00 Smart Homes Key Technology Trends - Index.md | medium |
| W2 | Source Collection and Register Maintenance | Standards, regulator and vendor primary sources | Assemble the source register and label the evidence class of each source | Source Register with an evidence-discipline section and a date note | "Documented fact: directly supported by a linked source"; "Vendor announcements are treated as capability claims, not independent validation" | Researcher | [not stated in source] | Source Register.md | high |
| W3 | Six-Lens Category Synthesis | Source Register; orientation hypotheses | Write the six category notes against the shared section template | Six category notes plus the index architecture map | Each note separates Core idea, Documented developments, Design rules, Trade-offs and open questions, and Sources | Researcher | Category Note Template | Category Note Template.md; index | high |
| W4 | Follow-up Question Prioritisation | Category-note open questions | Rank open questions by their ability to change a decision | Prioritised research backlog (Priority 1-3) with suggested next research packages | "Prioritize questions that can change a product, investment, architecture, or policy decision" | Researcher | [not stated in source] | FollowUpResearch_Questions.md | high |
| W5 | Follow-up Research Package Execution | Prioritised questions; prompt templates | Execute the thirteen research packages and record findings per topic | Follow-up notes, one per topic | "Separate documented facts, vendor claims, synthesis, and recommendations"; "Include date, geography, evidence quality, unresolved uncertainty, and decision implications"; "Do not invent missing measurements" | Researcher / agent | Prompts/README.md prompt map | Prompts/README.md | high |
| W6 | Interoperability Test Protocol Execution | Four ecosystems (Apple Home, Google Home, Amazon Alexa, Samsung SmartThings) with Home Assistant as reference; minimum nine-device inventory; VLAN-capable router; one border router per ecosystem; WAN-isolation capability | Run the fixed test cases for onboarding, multi-admin, Thread commissioning, discovery, routine creation, offline behaviour, update delivery and migration | Per-case records with observed result, recovery time and captured evidence | "Record ecosystem, device, firmware version, controller version, network topology, date, steps, expected result, observed result, recovery time (seconds), user effort (clicks/taps/retries), and evidence"; each test carries explicit failure criteria | Test teams; product teams; standards and certification bodies | mDNS/Bonjour capture; Thread sniffer; iOS 18+ and Android 15+ controllers | Reproducible Test Protocol.md | high |
| W7 | AI Intent and Action Safety Benchmarking | 14 scenario categories; 120 test cases; device inventory and household state per case | Run the test cases, score nine dimensions, and apply the minimum guardrails | Scored results, failure examples and prioritised recommendations | "Each test case is scored on nine dimensions, using a 0-3 scale unless otherwise noted"; safety-critical and above are deny-by-default; "Post-LLM Action Gating" and staleness gating must be implemented | AI developers; product teams | [not stated in source] | Home-AI Intent Interpretation and Action Safety Benchmark.md | medium |
| W8 | Residential Energy Flexibility Modelling | Baseline household parameters (30 kWh/day; device-level annual consumption); tariff structures; equipment constraints; installation and maintenance costs | Model device-level flexibility, value distribution, sensitivity analysis and stress tests | Flexibility model with payback, NPV, emissions and value-share outputs | "Enforce minimum on/off times (60 min on / 30 min off is a reasonable starting point) and monitor cycling frequency"; "Publish measured performance, not modelled potential"; the sensitivity analysis must name the dominant parameter | Modeller; product teams | [not stated in source] | Coordinated Residential Energy Flexibility Model HVAC, Heat Pumps, Water Heaters, EVs, Batteries, Solar, and Appliances.md | medium |
| W9 | Lifecycle Security and Privacy Scoring | Product documentation; certification records; independent tests; CVE evidence; vendor support policies | Score 14 lifecycle controls on Control Maturity and Evidence Quality, apply the penalty rule, compute the weighted composite | Scorecard scores, compliance-without-safety flags and prioritised remediation | "Minimum passing score for recommendation: 2.00, with no individual control below 1.0 and no 'compliance without safety' flags"; the penalty rule flags CM 0-1 with EQ 2-3 | Security reviewer | CM/EQ 0-3 rubric and risk weights | Smart-Home Product Security and Privacy Lifecycle Scorecard.md | medium |
| W10 | Adoption, Retention and Willingness-to-Pay Study | Sampling frame across eight stratification dimensions; 85-item survey; conjoint attribute design; interview guide | Phase 1 survey and conjoint; Phase 2 semi-structured interviews; Phase 3 diary and behavioural validation | Segment structure, barrier ranking, WTP estimates and a joint display | Pre-register sampling, quotas, survey wording, exclusion rules, analysis and ethical/privacy handling before fieldwork; power target of 5 percentage points at 80% power with n = 2,400 | Researcher; panel provider; interviewers | Hierarchical Bayes conjoint; latent class analysis; Van Westendorp; NVivo | Mixed-Method Study Design Smart-Home Adoption, Retention, and Willingness to Pay.md | medium |
| W11 | Evidence Audit and Citation Remediation | Follow-up notes; the claim-level citation gaps identified in the evaluation | Attach claim-level citations; separate vendor claims from independent evidence; verify company metrics against filings | A traceable claim dataset with consistent confidence labels and explicit uncertainty | "Add claim-level citations or footnotes, and label every important number"; "Verify ARR, churn, CAC, LTV, market-size, compliance-cost, and regulatory claims directly from filings or official sources" | Evaluator | [not stated in source] | FollowUp Research Evaluation.md | high |
| W12 | Decision Synthesis and Decision-Status Classification | Audited notes, benchmark results and scorecard outputs | Classify each decision area by readiness and defined use | Decision-status table with permitted uses per area | Every area states its permitted use (for example "Ready for strategic hypothesis" or "Not ready for investment approval"); "Any failed mandatory gate requires revise or reject" | Evaluator; decision owner | [not stated in source] | FollowUp Research Evaluation.md | high |


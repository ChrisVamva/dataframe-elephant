---
stage: 2
created: 2026-09-29
extracted_from:
  - research/raw/Stage 1/Wave 3/Automation Market Research/00_Index/README.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/00_Index/Next_Research_Prompts.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/01_Market_Map/Automation_Market_Taxonomy.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/02_Service_Profiles/Service_Profiles.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/02_Service_Profiles/Agent_Orchestration_Comparison.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/03_Pricing_and_Commercials/Pricing_Snapshot.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/04_Technology_and_Architecture/Technology_Stack.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/05_History_and_Evolution/Automation_History.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/06_Future_and_Signals/Future_Signals.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/07_Fit_Frameworks/Company_Fit_Matrix.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/07_Fit_Frameworks/Individual_Fit_Matrix.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/08_Problems_and_Opportunities/Problems.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/08_Problems_and_Opportunities/Opportunities.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/09_Sources_and_Research_Log/Sources.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/Prompts/01_LangGraph_vs_Temporal.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/Prompts/02_Total_Cost_of_Agent_Workflow.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/Prompts/03_MCP_A2A_Interoperability.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/Prompts/04_Automation_Failure_Patterns.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/Prompts/05_Small_Company_Tool_Fit.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/Prompt Guided Research/Runtime Ownership Comparison.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/Prompt Guided Research/Incidents, five publicly documented incidents.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/Prompt Guided Research/Discovery Compatible with a Thin Adapter.md
  - research/raw/Stage 1/Wave 3/Automation Market Research/Prompt Guided Research/At-a-Glance Comparison.md
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

# Extraction Log — Wave 3 (Automation Market Research)

| Log ID | Step | Stage 1 source | Decision type | Description | Resolution |
| --- | --- | --- | --- | --- | --- |
| L001 | Step 2 | 09_Sources_and_Research_Log/Sources.md | classification_conflict | LangGraph overview appears in both official product sources and agent orchestration sources sections with same URL | Recorded once as S7 with Primary classification |
| L002 | Step 2 | 09_Sources_and_Research_Log/Sources.md | scope_boundary | Sources listed without URLs (none in this file) | All sources in this file had URLs; no blank URL entries needed |
| L003 | Step 2 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | label_resolution | Claude Managed Agents pricing referenced as "Anthropic" in content but sourced from verdent.ai article | Recorded as S30 with publisher "verdent.ai" and classification Secondary |
| L004 | Step 2 | Prompt Guided Research/Incidents, five publicly documented incidents.md | scope_boundary | DeepSeek citation cards at bottom of file contain interface artifacts, not sources to extract | Excluded citation cards; extracted only 5 explicitly named incidents from content section |
| L005 | Step 2 | Prompt Guided Research/Runtime Ownership Comparison.md | scope_boundary | DeepSeek citation cards at bottom contain interface artifacts | Excluded citation cards; extracted only sources explicitly named in content section |
| L006 | Step 2 | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md | scope_boundary | DeepSeek citation cards at bottom contain interface artifacts | Excluded citation cards; extracted only a2a_mcp_bridge, MCP spec, A2A spec from content section |
| L007 | Step 2 | Prompt Guided Research/At-a-Glance Comparison.md | scope_boundary | DeepSeek citation cards at bottom contain interface artifacts | Excluded citation cards; extracted only pricing pages explicitly named in content section |
| L008 | Step 3 | 02_Service_Profiles/Service_Profiles.md | entity_split | "Automation platform" and "workflow runtime" listed as distinct concepts in Important distinctions | Recorded as E23 and E24 with separate boundaries |
| L009 | Step 3 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | entity_merge | "Agent framework," "orchestration runtime," and "durable workflow runtime" are three distinct families | Recorded as E33, E34, E35 with separate boundaries |
| L010 | Step 3 | 01_Market_Map/Automation_Market_Taxonomy.md | boundary_absent | No explicit boundary stated for market taxonomy segments | Recorded boundaries derived from "Core job" and "Buyer" descriptions |
| L011 | Step 3 | 07_Fit_Frameworks/Company_Fit_Matrix.md | boundary_absent | Entity boundaries not explicitly stated for company profiles | Recorded boundaries derived from "Best starting layer" and "Avoid starting with" columns |
| L012 | Step 3 | 07_Fit_Frameworks/Individual_Fit_Matrix.md | boundary_absent | Entity boundaries not explicitly stated for individual profiles | Recorded boundaries derived from "Best fit" and "Learning curve" columns |
| L013 | Step 4 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | label_resolution | "Durable execution" used informally in Stage 1; mapped to standard predicate "orchestrates" | Recorded as "orchestrates" with original phrasing noted |
| L014 | Step 4 | 04_Technology_and_Architecture/Technology_Stack.md | label_resolution | "Coordinates" used for agent-tool relationship; mapped to standard predicate "coordinates" | Recorded as "coordinates" |
| L015 | Step 5 | 08_Problems_and_Opportunities/Problems.md | evidence_downgrade | "The central market gap is safe, observable, maintainable automation" is an inference, not a documented fact | Recorded as inference with medium confidence |
| L016 | Step 5 | 08_Problems_and_Opportunities/Opportunities.md | evidence_downgrade | All product and service opportunities are inferences, not documented facts | Recorded as inferences with medium confidence |
| L017 | Step 5 | 07_Fit_Frameworks/Company_Fit_Matrix.md | evidence_downgrade | All fit matrix recommendations are inferences based on tool characteristics | Recorded as inferences with medium confidence |
| L018 | Step 5 | 07_Fit_Frameworks/Individual_Fit_Matrix.md | evidence_downgrade | All fit matrix recommendations are inferences based on tool characteristics | Recorded as inferences with medium confidence |
| L019 | Step 5 | 06_Future_and_Signals/Future_Signals.md | falsifier_absent | No falsifiers provided for any future signals | Recorded as [falsifier not stated] for all claims in this section |
| L020 | Step 5 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | falsifier_absent | No falsifiers provided for recommendations by situation | Recorded as [falsifier not stated] for all claims in this section |
| L021 | Step 5 | 08_Problems_and_Opportunities/Opportunities.md | falsifier_absent | No falsifiers provided for product opportunities | Recorded as [falsifier not stated] for all claims in this section |
| L022 | Step 6 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | condition_absent | Power Automate Process price ($150/bot/month) has no stated conditions | Recorded as [conditions not stated in source] with medium confidence |
| L023 | Step 6 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | condition_absent | Many cost figures are based on workload assumptions rather than stated conditions | Recorded assumptions in Scope column |
| L024 | Step 6 | Prompt Guided Research/At-a-Glance Comparison.md | condition_absent | Maintenance burden estimates are based on general industry observations, not specific conditions | Recorded as reported signal with medium confidence |
| L025 | Step 7 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | scope_boundary | Three families of agent solutions identified (framework, orchestration runtime, durable workflow runtime) | Recorded all three families in WorkflowMap with distinct stage names |
| L026 | Step 7 | 00_Index/README.md | scope_boundary | Working rule about pricing change frequency is a process note, not a workflow stage | Excluded from WorkflowMap; noted in ExtractionLog |
| L027 | Step 8 | 09_Sources_and_Research_Log/Sources.md | omission | DeepSeek citation cards in Prompt Guided Research files excluded as interface artifacts | Documented in L004-L007 |
| L028 | Step 8 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | omission | Detailed cost calculation methodology excluded from Metrics; only final values extracted | Methodology documented in Stage 1 file; Metrics contains final values only |
| L029 | Step 8 | 08_Problems_and_Opportunities/Problems.md | open_question | "What is the exact cost of hidden automation?" remains unresolved | Carried forward as open question |
| L030 | Step 8 | 06_Future_and_Signals/Future_Signals.md | open_question | "Which standards will dominate agent identity and delegated authorization?" remains unresolved | Carried forward as open question |
| L031 | Step 8 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | open_question | "What does 'durable' mean in each product?" remains unresolved | Carried forward as open question |
| L032 | Step 5 | 08_Problems_and_Opportunities/Problems.md | scope_boundary | Open questions and caveats in Stage 1 excluded from Claims | Open questions recorded in ExtractionLog only |
| L033 | Step 3 | 02_Service_Profiles/Service_Profiles.md | entity_split | "RPA" and "desktop automation" used interchangeably in Stage 1 | Treated as single entity E18 with combined boundary |
| L034 | Step 4 | 08_Problems_and_Opportunities/Problems.md | label_resolution | "Automation sprawl" mapped to concept "automation inventory" | Recorded predicate "owns" for company-automation relationship |
| L035 | Step 6 | Prompt Guided Research/Incidents, five publicly documented incidents.md | condition_absent | Copado incident duration not stated in source | Recorded as [conditions not stated in source] |
| L036 | Step 2 | 09_Sources_and_Research_Log/Sources.md | label_resolution | "Official product and pricing sources" section mapped to Primary classification | Recorded as Primary for all sources in this section |
| L037 | Step 2 | 09_Sources_and_Research_Log/Sources.md | label_resolution | "Agent orchestration sources" section mapped to Primary classification | Recorded as Primary for all sources in this section |
| L038 | Step 2 | 09_Sources_and_Research_Log/Sources.md | label_resolution | "Protocol and architecture sources" section mapped to Primary classification | Recorded as Primary for all sources in this section |
| L039 | Step 2 | 09_Sources_and_Research_Log/Sources.md | label_resolution | "History and future sources" section mapped to Primary/Secondary based on content | S22 and S24 recorded as Primary; S23 recorded as Secondary (vendor perspective) |
| L040 | Step 5 | 05_History_and_Evolution/Automation_History.md | evidence_downgrade | Historical synthesis claims are inferences based on historical pattern | Recorded as documented fact for established history; inference for synthesis |
| L041 | Step 5 | 06_Future_and_Signals/Future_Signals.md | evidence_downgrade | Future signal claims are reported signals, not documented facts | Recorded as reported signal with medium confidence |
| L042 | Step 3 | 04_Technology_and_Architecture/Technology_Stack.md | boundary_absent | Technology stack entities have no explicit boundaries | Recorded boundaries derived from layer descriptions |
| L043 | Step 4 | 06_Future_and_Signals/Future_Signals.md | label_resolution | "Watchlist" items are concepts, not predicates | Excluded from Predicates; included in Entities as concepts |
| L044 | Step 6 | Prompt Guided Research/At-a-Glance Comparison.md | condition_absent | Custom agent stack cost range depends on scale and existing platform team | Recorded as reported signal with medium confidence |
| L045 | Step 8 | 00_Index/README.md | open_question | "What is the exact boundary between integration automation and RPA?" remains unresolved | Carried forward as open question |
| L046 | Step 8 | 01_Market_Map/Automation_Market_Taxonomy.md | open_question | "Will a single platform dominate every layer?" remains unresolved | Carried forward as open question |
| L047 | Step 5 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | scope_boundary | Product names and managed-service boundaries are changing quickly | Noted as limitation; claims recorded with current understanding |
| L048 | Step 2 | Prompt Guided Research/Incidents, five publicly documented incidents.md | classification_conflict | Same incident (PocketOS database deletion) appears in multiple sources with different classifications | Recorded primary source as S27; additional context from other sources noted |
| L049 | Step 3 | 08_Problems_and_Opportunities/Problems.md | entity_split | "Credential" and "secret" used interchangeably in Stage 1 | Treated as single entity E36 with combined boundary |
| L050 | Step 3 | 08_Problems_and_Opportunities/Opportunities.md | entity_merge | "Automation observability" and "automation inventory" used interchangeably | Treated as single entity E39 with combined boundary |

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

# Workflow Map — Wave 3 (Automation Market Research)

| Stage ID | Stage name | Inputs | Activities | Outputs | Quality gates | Roles | Tools | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W1 | Pricing snapshot | Official pricing pages, vendor pages | Record published prices, commercial units, and interpretations | Pricing table with service, signal, unit, interpretation | Verify prices are indicative and may vary by region, contract, usage | Researcher | Web browser, vendor pricing pages | Pricing_Snapshot.md | high |
| W2 | Runtime ownership analysis | Workflow requirements (approval, retry, timers, compensation) | Compare LangGraph and Temporal for each concern | Runtime ownership comparison table | Verify each runtime's actual capabilities against documented features | Researcher | LangGraph docs, Temporal docs, comparison frameworks | Runtime Ownership Comparison.md | high |
| W3 | Protocol interoperability test | MCP specification, A2A specification | Test discovery, authentication, task status, streaming, error handling | Interoperability verdict and adapter code | Verify adapter code works with both protocols | Researcher | MCP spec, A2A spec, a2a_mcp_bridge package | Discovery Compatible with a Thin Adapter.md | medium |
| W4 | Cost modeling | 10,000-run workload assumptions | Calculate monthly costs for hosted vs self-hosted | Cost breakdown table with categories | Verify assumptions are stated and transparent | Researcher | Published pricing pages, cost calculators | Monthly Cost Breakdown – 10,000 Runs.md | medium |
| W5 | Incident collection | Public reports, status pages, technical reports | Collect five incidents, classify failure modes | Incident table with classification and source | Verify each incident is publicly documented | Researcher | News articles, status pages, government audits | Incidents, five publicly documented incidents.md | high |
| W6 | Problem identification | Operational, economic, governance, human problem categories | Identify and categorize automation problems | Problem list with categories and implications | Verify problems are grounded in documented incidents | Researcher | Incident reports, industry analyses | Problems.md | high |
| W7 | Opportunity identification | Problem list, market gaps, product ideas | Identify and filter product and service opportunities | Opportunity list with filter criteria | Verify opportunities have repeated, measurable processes | Researcher | Market analysis, opportunity filter framework | Opportunities.md | medium |
| W8 | Fit matrix construction | Company profiles, individual profiles, tool characteristics | Map profiles to best-fit tools with rationale | Fit matrices for companies and individuals | Verify fit is grounded in documented tool capabilities | Researcher | Service profiles, pricing data, governance requirements | Company_Fit_Matrix.md, Individual_Fit_Matrix.md | medium |
| W9 | History and future signal analysis | Historical accounts, vendor trend pages, academic papers | Trace automation evolution and identify future signals | History timeline, future signals, watchlist | Verify historical claims are sourced | Researcher | Academic papers, vendor blogs, industry analyses | Automation_History.md, Future_Signals.md | medium |
| W10 | Architecture principle formulation | Technology stack, service comparisons, pricing data | Derive architecture principles and recommendations | Architecture principles, commercial conclusions | Verify principles are consistent with evidence | Researcher | Technology stack docs, service comparisons | Technology_Stack.md, Pricing_Snapshot.md, Agent_Orchestration_Comparison.md | high |
| W11 | Small company decision guide | 20-person company profile, tool comparisons | Compare Power Automate, n8n, Make, Zapier, custom stack | Decision guide with recommendation | Verify recommendation matches stated constraints | Researcher | Pricing pages, governance documentation | At-a-Glance Comparison.md | medium |
| W12 | Source validation | Official product pages, primary specifications, academic papers | Validate and classify sources | Source table with classification and date | Verify each source is accessible and authoritative | Researcher | Web browser, academic databases | Sources.md | high |

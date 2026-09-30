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

# Entities — Wave 3 (Automation Market Research)

| Entity ID | Canonical name | Type | Boundary (what it is not) | Stage 1 source | Section | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | Zapier | Service | Not an agent orchestration runtime or durable workflow engine | 02_Service_Profiles/Service_Profiles.md | Service profiles table | high |
| E2 | Make | Service | Not a self-hosted workflow engine or agent framework | 02_Service_Profiles/Service_Profiles.md | Service profiles table | high |
| E3 | n8n | Service | Not a hosted-only SaaS; self-hosted option exists | 02_Service_Profiles/Service_Profiles.md | Service profiles table | high |
| E4 | Workato | Service | Not a low-code desktop automation tool | 02_Service_Profiles/Service_Profiles.md | Service profiles table | high |
| E5 | Power Automate | Service | Not a cross-platform agent orchestration framework | 02_Service_Profiles/Service_Profiles.md | Service profiles table | high |
| E6 | UiPath | Service | Not a developer-focused durable execution engine | 02_Service_Profiles/Service_Profiles.md | Service profiles table | high |
| E7 | Temporal | Technology | Not an agent framework; it is a durable workflow runtime | 02_Service_Profiles/Service_Profiles.md | Service profiles table | high |
| E8 | LangGraph | Framework | Not a complete managed business platform | 02_Service_Profiles/Service_Profiles.md | Service profiles table | high |
| E9 | OpenAI Agents SDK | Framework | Not an orchestration runtime with durable execution guarantees | 02_Service_Profiles/Service_Profiles.md | Service profiles table | high |
| E10 | ServiceNow | Service | Not a lightweight integration automation tool | 02_Service_Profiles/Service_Profiles.md | Service profiles table | high |
| E11 | Google ADK | Framework | Not a model provider; it is an agent development kit | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Executive comparison | high |
| E12 | Microsoft Agent Framework | Framework | Not limited to Microsoft cloud; it is a cross-framework agent/workflow development direction | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Executive comparison | high |
| E13 | CrewAI Flows | Framework | Not a durable workflow runtime; it is an opinionated multi-agent workflow abstraction | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Executive comparison | high |
| E14 | LangSmith | Service | Not an agent framework; it is an observability and deployment platform for LangGraph | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Executive comparison | high |
| E15 | MCP | Protocol | Not an agent-to-agent protocol; it is agent-to-tool | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Risks and open questions | high |
| E16 | A2A | Protocol | Not an agent-to-tool protocol; it is agent-to-agent | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Risks and open questions | high |
| E17 | SaaS integration | Market segment | Not RPA or durable workflow orchestration | 01_Market_Map/Automation_Market_Taxonomy.md | Section 1 | high |
| E18 | RPA | Technology | Not API-based integration; it acts through screens and machines | 01_Market_Map/Automation_Market_Taxonomy.md | Section 2 | high |
| E19 | iPaaS | Technology | Not desktop UI automation; it acts through APIs and connectors | 01_Market_Map/Automation_Market_Taxonomy.md | Section 2 | high |
| E20 | Durable workflow orchestration | Technology | Not probabilistic reasoning; it is deterministic execution | 01_Market_Map/Automation_Market_Taxonomy.md | Section 3 | high |
| E21 | Agent orchestration | Technology | Not deterministic control; it adds probabilistic reasoning | 01_Market_Map/Automation_Market_Taxonomy.md | Section 4 | high |
| E22 | Enterprise process suites | Technology | Not lightweight integration tools; they embed automation into governed business processes | 01_Market_Map/Automation_Market_Taxonomy.md | Section 5 | high |
| E23 | Automation platform | Concept | Not a workflow runtime | 02_Service_Profiles/Service_Profiles.md | Important distinctions | high |
| E24 | Workflow runtime | Concept | Not an automation platform | 02_Service_Profiles/Service_Profiles.md | Important distinctions | high |
| E25 | Model context protocol | Protocol | Not an agent-to-agent communication protocol | 04_Technology_and_Architecture/Technology_Stack.md | Key technologies | high |
| E26 | A2A protocol | Protocol | Not an agent-to-tool communication protocol | 04_Technology_and_Architecture/Technology_Stack.md | Key technologies | high |
| E27 | Durable execution | Technology | Not checkpointed agent state only; it is workflow event history | 02_Service_Profiles/Agent_Orchestration_Comparison.md | The most important distinction | high |
| E28 | Checkpointing | Technology | Not durable timer primitives | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Capability matrix | high |
| E29 | Idempotency key | Technology | Not a retry policy; it is a mechanism to prevent duplicate effects | Prompt Guided Research/Runtime Ownership Comparison.md | State section | high |
| E30 | Saga pattern | Pattern | Not a retry mechanism; it is a compensation pattern for distributed transactions | Prompt Guided Research/Runtime Ownership Comparison.md | Compensation section | high |
| E31 | Human-in-the-loop | Pattern | Not autonomous execution; it requires human approval | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Capability matrix | high |
| E32 | Durable timer | Technology | Not a simple wait; it persists across restarts | Prompt Guided Research/Runtime Ownership Comparison.md | Timers section | high |
| E33 | Agent framework | Concept | Not an orchestration runtime or durable workflow runtime | 02_Service_Profiles/Agent_Orchestration_Comparison.md | The most important distinction | high |
| E34 | Orchestration runtime | Concept | Not an agent framework or durable workflow runtime | 02_Service_Profiles/Agent_Orchestration_Comparison.md | The most important distinction | high |
| E35 | Durable workflow runtime | Concept | Not an agent framework or orchestration runtime | 02_Service_Profiles/Agent_Orchestration_Comparison.md | The most important distinction | high |
| E36 | Credential | Concept | Not a secret; it is an identity proof | 08_Problems_and_Opportunities/Problems.md | Governance problems | high |
| E37 | Governance | Concept | Not technical execution; it is organizational oversight | 08_Problems_and_Opportunities/Problems.md | Governance problems | high |
| E38 | Approval fatigue | Concept | Not a technical failure; it is a human problem | 08_Problems_and_Opportunities/Problems.md | Human problems | high |
| E39 | Automation observability | Concept | Not a workflow engine; it is inventory and failure history | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities | high |
| E40 | Cross-platform policy layer | Concept | Not a single-platform DLP; it spans multiple tools | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities | high |
| E41 | Durable agent adapter | Concept | Not an agent framework; it packages workflows with idempotency and retries | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities | high |
| E42 | Human review infrastructure | Concept | Not autonomous execution; it is risk-based approval | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities | high |
| E43 | Automation cost intelligence | Concept | Not a pricing page; it is forecast spend across tasks and tokens | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities | high |
| E44 | Agent capability registry | Concept | Not a tool directory; it discovers, authenticates, authorizes, and evaluates agents | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities | high |
| E45 | Process mining | Technology | Not workflow execution; it is event log analysis | 06_Future_and_Signals/Future_Signals.md | Signal 5 | high |
| E46 | Agent telemetry | Technology | Not model calls; it is process measurement | 06_Future_and_Signals/Future_Signals.md | Signal 5 | high |
| E47 | Policy-based autonomy | Concept | Not fully autonomous operation; it is governed by policy | 06_Future_and_Signals/Future_Signals.md | Signal 4 | high |
| E48 | Hybrid estate | Concept | Not a single-platform architecture; it combines RPA, iPaaS, durable runtimes, and agent frameworks | 06_Future_and_Signals/Future_Signals.md | Signal 6 | high |
| E49 | Agent identity | Concept | Not a user identity; it is delegated authorization for agents | 06_Future_and_Signals/Future_Signals.md | Watchlist | high |
| E50 | Signed capability card | Concept | Not a tool credential; it is signed tool provenance | 06_Future_and_Signals/Future_Signals.md | Watchlist | high |

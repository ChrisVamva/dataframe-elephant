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

# Predicates — Wave 3 (Automation Market Research)

| Predicate | Subject type | Object type | Direction | Example (from Stage 1) | Stage 1 source |
| --- | --- | --- | --- | --- | --- |
| uses | Service | Protocol | Service uses protocol | LangGraph uses MCP for tool connectivity | 02_Service_Profiles/Agent_Orchestration_Comparison.md |
| uses | Technology | Technology | Technology uses technology | Agent orchestration uses model calls, tool calling, retrieval | 04_Technology_and_Architecture/Technology_Stack.md |
| performed_by | Workflow | Role | Workflow performed by role | Automation performed by engineering teams | 01_Market_Map/Automation_Market_Taxonomy.md |
| governed_by | Automation | Policy | Automation governed by policy | Automation governed by DLP policies | 08_Problems_and_Opportunities/Problems.md |
| produces | Automation | Side effect | Automation produces side effect | Automation produces side effects on external systems | 08_Problems_and_Opportunities/Problems.md |
| requires | Workflow | Approval | Workflow requires approval | High-impact actions require review and identity checks | 06_Future_and_Signals/Future_Signals.md |
| implemented_by | Pattern | Runtime | Pattern implemented by runtime | Saga pattern implemented by Temporal | Prompt Guided Research/Runtime Ownership Comparison.md |
| supports | Protocol | Tool | Protocol supports tool | MCP supports tools and resources | 02_Service_Profiles/Agent_Orchestration_Comparison.md |
| supports | Protocol | Agent | Protocol supports agent | A2A supports agent-to-agent communication | 02_Service_Profiles/Agent_Orchestration_Comparison.md |
| conflicts_with | Tool | Connector | Tool conflicts with connector | Over-blocking DLP policies force users to shadow IT | 08_Problems_and_Opportunities/Problems.md |
| extends | Agent | Framework | Agent extends framework | Agent extends LangGraph or OpenAI Agents SDK | 02_Service_Profiles/Agent_Orchestration_Comparison.md |
| orchestrates | Runtime | Workflow | Runtime orchestrates workflow | Temporal orchestrates durable workflows | 02_Service_Profiles/Agent_Orchestration_Comparison.md |
| coordinates | Agent | Tool | Agent coordinates tool | Agent coordinates model calls, tools, memory, delegation | 01_Market_Map/Automation_Market_Taxonomy.md |
| validates | Automation | Data | Automation validates data | RPA validates customer data from external registries | Prompt Guided Research/Incidents, five publicly documented incidents.md |
| authenticates | User | Service | User authenticates to service | User authenticates via OAuth 2.0 to MCP server | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md |
| delegates | Agent | Agent | Agent delegates to agent | Agent delegates subtasks to specialist agents via A2A | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md |
| discovers | Agent | Tool | Agent discovers tool | Agent discovers tools via MCP capability lists | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md |
| maps | Adapter | State | Adapter maps state | Adapter maps A2A TaskState to MCP isError | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md |
| bridges | Adapter | Protocol | Adapter bridges protocol | a2a_mcp_bridge bridges A2A and MCP | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md |
| normalizes | Adapter | Error | Adapter normalizes error | Adapter normalizes MCP and A2A errors to unified format | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md |
| measures | Automation | Outcome | Automation measures outcome | Automation measured by business outcomes and exception rates | 06_Future_and_Signals/Future_Signals.md |
| detects | Bot | UI change | Bot detects UI change | Bot detects vendor portal UI changes | Prompt Guided Research/Incidents, five publicly documented incidents.md |
| retries | Runtime | Activity | Runtime retries activity | Temporal retries failed Activities automatically | Prompt Guided Research/Runtime Ownership Comparison.md |
| compensates | Runtime | Activity | Runtime compensates activity | Temporal compensates for failed steps via Saga pattern | Prompt Guided Research/Runtime Ownership Comparison.md |
| pauses | Workflow | Human | Workflow pauses for human | Workflow pauses for human approval via interrupt | Prompt Guided Research/Runtime Ownership Comparison.md |
| resumes | Workflow | Human | Workflow resumes from human | Workflow resumes from persisted checkpoint | Prompt Guided Research/Runtime Ownership Comparison.md |
| owns | Runtime | State | Runtime owns state | Temporal owns workflow state as part of Durable Execution | Prompt Guided Research/Runtime Ownership Comparison.md |
| owns | Framework | Logic | Framework owns logic | LangGraph owns graph state via checkpointers | Prompt Guided Research/Runtime Ownership Comparison.md |
| generates | Runtime | Idempotency key | Runtime generates idempotency key | Temporal generates stable idempotency key from Workflow Run ID | Prompt Guided Research/Runtime Ownership Comparison.md |
| enforces | Policy | Connector | Policy enforces connector | DLP policy enforces connector communication rules | Prompt Guided Research/At-a-Glance Comparison.md |
| classifies | Policy | Connector | Policy classifies connector | DLP classifies connectors into business, non-business, blocked | Prompt Guided Research/At-a-Glance Comparison.md |
| blocks | Policy | Connector | Policy blocks connector | Over-blocking DLP policies block connectors | Prompt Guided Research/At-a-Glance Comparison.md |
| owns | Company | Automation | Company owns automation | Company owns automation sprawl with no inventory | 08_Problems_and_Opportunities/Problems.md |
| documents | Owner | Automation | Owner documents automation | Personal automations must document ownership and credentials | 07_Fit_Frameworks/Individual_Fit_Matrix.md |
| migrates | Service | Integration | Service migrates integration | RPA candidates should migrate to stable integrations | 08_Problems_and_Opportunities/Opportunities.md |
| evaluates | Registry | Agent | Registry evaluates agent | Agent capability registry evaluates MCP/A2A tools and agents | 08_Problems_and_Opportunities/Opportunities.md |
| combines | Architecture | Runtime | Architecture combines runtime | Production systems combine agent framework with durable execution layer | 02_Service_Profiles/Agent_Orchestration_Comparison.md |
| avoids | Architecture | System | Architecture avoids system | Architecture avoids nesting multiple independent retry systems | 02_Service_Profiles/Agent_Orchestration_Comparison.md |

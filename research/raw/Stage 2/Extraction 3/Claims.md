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

# Claims — Wave 3 (Automation Market Research)

| Claim ID | Claim text | Claim type | Confidence | Source IDs | Falsifier | Workflow stage | Stage 1 source | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C001 | Automation is not one market; it is a stack of overlapping markets | documented fact | high | S1-S24 | [falsifier not stated] | W1 | 00_Index/README.md | Research thesis |
| C002 | Zapier offers a free tier of 100 tasks/month and Professional from $19.99/month | documented fact | high | S1 | [falsifier not stated] | W1 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| C003 | Power Automate Premium costs $15/user/month yearly and Process costs $150/bot/month | documented fact | high | S3, S33 | [falsifier not stated] | W1 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| C004 | Temporal Cloud pricing starts from $50 per million actions and volume self-service down to $25/million | documented fact | high | S4, S31 | [falsifier not stated] | W1 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| C005 | UiPath Basic starts from $25/month; Standard and Enterprise require contact with sales | documented fact | high | S5 | [falsifier not stated] | W1 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| C006 | n8n Cloud plans are priced by workflow executions; self-hosted option exists | documented fact | high | S2 | [falsifier not stated] | W1 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| C007 | Workato directs buyers to a pricing discussion; it uses a flexible enterprise contract model | documented fact | high | S6 | [falsifier not stated] | W1 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| C008 | LangGraph is open-source runtime; commercial deployment is through LangSmith products | documented fact | high | S7, S13 | [falsifier not stated] | W1 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| C009 | Temporal owns state, retries, timers, and compensation for durable execution | documented fact | high | S4, S36 | [falsifier not stated] | W2 | Prompt Guided Research/Runtime Ownership Comparison.md | State section |
| C010 | LangGraph owns graph state via checkpointers but does not own durable execution | documented fact | high | S7, S36 | [falsifier not stated] | W2 | Prompt Guided Research/Runtime Ownership Comparison.md | State section |
| C011 | Temporal provides automatic Activity retries with configurable backoff policies | documented fact | high | S4, S36 | [falsifier not stated] | W2 | Prompt Guided Research/Runtime Ownership Comparison.md | Retries section |
| C012 | LangGraph provides node-level retry policies but requires idempotent side effects | documented fact | high | S7, S36 | [falsifier not stated] | W2 | Prompt Guided Research/Runtime Ownership Comparison.md | Retries section |
| C013 | Temporal provides durable timers as a first-class primitive that persists across restarts | documented fact | high | S4, S36 | [falsifier not stated] | W2 | Prompt Guided Research/Runtime Ownership Comparison.md | Timers section |
| C014 | LangGraph can wait indefinitely using interrupt() with a persisted checkpoint | documented fact | high | S7, S36 | [falsifier not stated] | W2 | Prompt Guided Research/Runtime Ownership Comparison.md | Timers section |
| C015 | Temporal provides native Saga pattern support for compensation | documented fact | high | S4, S36 | [falsifier not stated] | W2 | Prompt Guided Research/Runtime Ownership Comparison.md | Compensation section |
| C016 | LangGraph does not provide built-in Saga or compensation pattern | documented fact | high | S7, S36 | [falsifier not stated] | W2 | Prompt Guided Research/Runtime Ownership Comparison.md | Compensation section |
| C017 | MCP standardizes model access to tools and resources | documented fact | high | S17 | [falsifier not stated] | W3 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Protocol and architecture sources |
| C018 | A2A 1.0 standardizes communication between independent agents | documented fact | high | S18 | [falsifier not stated] | W3 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Protocol and architecture sources |
| C019 | MCP is primarily agent-to-tool; A2A is agent-to-agent | documented fact | high | S17, S18 | [falsifier not stated] | W3 | 06_Future_and_Signals/Future_Signals.md | Signal 2 |
| C020 | MCP and A2A can be combined in a single workflow but require a thin adapter layer | reported signal | medium | S17, S18, S32 | [falsifier not stated] | W3 | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md | Discovery section |
| C021 | A single OAuth scope aggregation flow is needed for MCP and A2A interoperability | reported signal | medium | S32 | [falsifier not stated] | W3 | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md | Authentication section |
| C022 | A2A TaskState must be mapped to MCP isError for interoperability | documented fact | high | S17, S18, S32 | [falsifier not stated] | W3 | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md | Task Status section |
| C023 | A2A SSE streams must be bridged to MCP streamable HTTP for interoperability | documented fact | high | S17, S18, S32 | [falsifier not stated] | W3 | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md | Streaming section |
| C024 | A2A error codes must be normalized without re-emitting as JSON-RPC codes | documented fact | high | S17, S18, S32 | [falsifier not stated] | W3 | Prompt Guided Research/Discovery Compatible with a Thin Adapter.md | Error Handling section |
| C025 | Claude Managed Agents charges $0.08 per session-hour for active runtime | documented fact | high | S30 | [falsifier not stated] | W4 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Model Tokens section |
| C026 | Temporal Cloud charges $50 per million Actions | documented fact | high | S31 | [falsifier not stated] | W4 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Orchestration actions section |
| C027 | LangSmith Plus plan is $39 per seat per month with 10,000 base traces | documented fact | high | S13 | [falsifier not stated] | W4 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Tracing section |
| C028 | Hosted platform total cost for 10,000 runs is approximately $3,003 per month (infra only) | reported signal | medium | S30, S31, S13 | [falsifier not stated] | W4 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Total (infra only) |
| C029 | Self-hosted stack total cost for 10,000 runs is approximately $3,500-$4,000 per month (infra only) | reported signal | medium | S4, S31, S13 | [falsifier not stated] | W4 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Total (infra only) |
| C030 | Self-hosted operational labor is the dominant cost variable | documented fact | high | S4, S31 | [falsifier not stated] | W4 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Operational labor section |
| C031 | A 30-day human approval workflow is a cost advantage for hosted platforms | reported signal | medium | S30 | [falsifier not stated] | W4 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Key Takeaways |
| C032 | Idempotency is non-negotiable in both hosted and self-hosted stacks | documented fact | high | S4, S7, S30 | [falsifier not stated] | W4 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Key Takeaways |
| C033 | A large Midwest insurer ran approximately 40 RPA bots in production | documented fact | high | S25 | [falsifier not stated] | W5 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 1 |
| C034 | A vendor portal UI update broke four RPA bots simultaneously | documented fact | high | S25 | [falsifier not stated] | W5 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 1 |
| C035 | An AI procurement agent executed a $480,000 payment twice after network timeout | documented fact | high | S26 | [falsifier not stated] | W5 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 2 |
| C036 | A bank RPA bot corrupted 15,000 customer profiles silently for 90 days | documented fact | high | S27 | [falsifier not stated] | W5 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 3 |
| C037 | Salesforce token invalidation broke Copado deployment jobs in EMEA regions | documented fact | high | S28 | [falsifier not stated] | W5 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 4 |
| C038 | GSA RPA program did not establish access removal for 55 of 56 decommissioned bots | documented fact | high | S29 | [falsifier not stated] | W5 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 5 |
| C039 | Silent failures and duplicate side effects are operational problems in automation | documented fact | high | S25-S29 | [falsifier not stated] | W5 | 08_Problems_and_Opportunities/Problems.md | Operational problems |
| C040 | Usage-based pricing becomes unpredictable at scale | documented fact | high | S1, S4, S13 | [falsifier not stated] | W6 | 08_Problems_and_Opportunities/Problems.md | Economic problems |
| C041 | Low-code prototypes require expensive maintenance when they become critical | documented fact | high | S1, S5 | [falsifier not stated] | W6 | 08_Problems_and_Opportunities/Problems.md | Economic problems |
| C042 | Credentials and permissions are scattered across personal accounts | documented fact | high | S25-S29 | [falsifier not stated] | W6 | 08_Problems_and_Opportunities/Problems.md | Governance problems |
| C043 | Human approval may be missing, ambiguous, or unaudited | documented fact | high | S25-S29 | [falsifier not stated] | W6 | 08_Problems_and_Opportunities/Problems.md | Governance problems |
| C044 | Vendor lock-in can occur through proprietary connectors and workflow formats | documented fact | high | S1, S2, S3 | [falsifier not stated] | W6 | 08_Problems_and_Opportunities/Problems.md | Governance problems |
| C045 | Teams automate symptoms before understanding the process | documented fact | high | S25-S29 | [falsifier not stated] | W6 | 08_Problems_and_Opportunities/Problems.md | Human problems |
| C046 | No clear owner is assigned for agent or bot behavior | documented fact | high | S25-S29 | [falsifier not stated] | W6 | 08_Problems_and_Opportunities/Problems.md | Human problems |
| C047 | The central market gap is safe, observable, maintainable automation | inference | medium | S25-S29 | [falsifier not stated] | W6 | 08_Problems_and_Opportunities/Problems.md | Research implication |
| C048 | Automation observability for SMBs is a product opportunity | inference | medium | S25-S29 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities |
| C049 | Cross-platform policy layer is a product opportunity | inference | medium | S25-S29 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities |
| C050 | Durable agent adapters are a product opportunity | inference | medium | S4, S7, S36 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities |
| C051 | Human review infrastructure is a product opportunity | inference | medium | S25-S29 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities |
| C052 | Automation cost intelligence is a product opportunity | inference | medium | S1, S4, S13 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities |
| C053 | Legacy-to-API migration is a product opportunity | inference | medium | S25-S29 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities |
| C054 | Industry-specific automation is a product opportunity | inference | medium | S25-S29 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities |
| C055 | Agent capability registry is a product opportunity | inference | medium | S17, S18, S32 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Product opportunities |
| C056 | Automation audit and inventory is a service opportunity | inference | medium | S25-S29 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Service opportunities |
| C057 | Process redesign before tooling is a service opportunity | inference | medium | S25-S29 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Service opportunities |
| C058 | Migration from fragile UI bots to APIs is a service opportunity | inference | medium | S25-S29 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Service opportunities |
| C059 | Workflow reliability engineering is a service opportunity | inference | medium | S4, S7, S36 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Service opportunities |
| C060 | Agent governance and evaluation is a service opportunity | inference | medium | S17, S18, S32 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Service opportunities |
| C061 | Fractional automation platform ownership is a service opportunity | inference | medium | S1, S2, S3 | [falsifier not stated] | W7 | 08_Problems_and_Opportunities/Opportunities.md | Service opportunities |
| C062 | Power Automate is the best fit for Microsoft-centric SMB | inference | medium | S3, S5, S33 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Company_Fit_Matrix.md | Company fit matrix |
| C063 | n8n is the best fit for small technical companies | inference | medium | S2, S5 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Company_Fit_Matrix.md | Company fit matrix |
| C064 | Temporal plus LangGraph is the best fit for engineering-led product companies | inference | medium | S4, S7, S36 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Company_Fit_Matrix.md | Company fit matrix |
| C065 | UiPath or Power Automate Desktop is the best fit for legacy-heavy shared services | inference | medium | S5, S3 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Company_Fit_Matrix.md | Company fit matrix |
| C066 | LangGraph or OpenAI Agents SDK is the best fit for AI-native startups | inference | medium | S7, S8, S36 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Company_Fit_Matrix.md | Company fit matrix |
| C067 | Dagster, Prefect, Temporal, or n8n is the best fit for data/analytics teams | inference | medium | S4, S2, S7 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Company_Fit_Matrix.md | Company fit matrix |
| C068 | Zapier or Power Automate templates are the best fit for non-technical knowledge workers | inference | medium | S1, S3 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Individual_Fit_Matrix.md | Individual fit matrix |
| C069 | Make or n8n Cloud is the best fit for operations generalists | inference | medium | S2, S5 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Individual_Fit_Matrix.md | Individual fit matrix |
| C070 | Temporal, LangGraph, or agent SDKs are the best fit for developers | inference | medium | S4, S7, S8, S36 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Individual_Fit_Matrix.md | Individual fit matrix |
| C071 | Power Automate, Workato, or ServiceNow is the best fit for IT administrators | inference | medium | S3, S6, S10 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Individual_Fit_Matrix.md | Individual fit matrix |
| C072 | UiPath or Power Automate Desktop is the best fit for RPA specialists | inference | medium | S5, S3 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Individual_Fit_Matrix.md | Individual fit matrix |
| C073 | Start with the smallest tool that can safely express the workflow | recommendation | high | S1, S2, S3, S4, S5 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Individual_Fit_Matrix.md | Personal selection rule |
| C074 | Buy convenience for commodity integrations | recommendation | high | S1, S2, S3 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Company_Fit_Matrix.md | Rule of thumb |
| C075 | Build or adopt durable orchestration for critical workflows | recommendation | high | S4, S7, S36 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Company_Fit_Matrix.md | Rule of thumb |
| C076 | Add agents only where uncertainty or interpretation is the bottleneck | recommendation | high | S7, S8, S9 | [falsifier not stated] | W8 | 07_Fit_Frameworks/Company_Fit_Matrix.md | Rule of thumb |
| C077 | Each automation wave overpromised autonomy before solving maintenance, governance, exception handling, and accountability | documented fact | high | S22, S23 | [falsifier not stated] | W9 | 05_History_and_Evolution/Automation_History.md | Historical lesson |
| C078 | The market is moving from isolated task automation toward process orchestration | documented fact | high | S22, S23, S24 | [falsifier not stated] | W9 | 05_History_and_Evolution/Automation_History.md | Current synthesis |
| C079 | Google frames the shift as agents orchestrating end-to-end workflows rather than answering isolated prompts | documented fact | high | S24 | [falsifier not stated] | W9 | 06_Future_and_Signals/Future_Signals.md | Signal 1 |
| C080 | Temporal and LangGraph both emphasize stateful, long-running execution | documented fact | high | S4, S7, S36 | [falsifier not stated] | W9 | 06_Future_and_Signals/Future_Signals.md | Signal 3 |
| C081 | The likely enterprise pattern is policy-based autonomy | inference | medium | S24 | [falsifier not stated] | W9 | 06_Future_and_Signals/Future_Signals.md | Signal 4 |
| C082 | Process mining, event logs, traces, and agent telemetry will feed process redesign | reported signal | medium | S24 | [falsifier not stated] | W9 | 06_Future_and_Signals/Future_Signals.md | Signal 5 |
| C083 | Companies will retain RPA for legacy UI, iPaaS for SaaS/API integration, durable runtimes for critical execution, and agent frameworks for interpretation | reported signal | medium | S24 | [falsifier not stated] | W9 | 06_Future_and_Signals/Future_Signals.md | Signal 6 |
| C084 | Use deterministic automation for predictable transformations and agents where interpretation provides value | recommendation | high | S4, S7, S8 | [falsifier not stated] | W10 | 04_Technology_and_Architecture/Technology_Stack.md | Architecture principle |
| C085 | Put an explicit boundary around every side effect | recommendation | high | S4, S7, S8 | [falsifier not stated] | W10 | 04_Technology_and_Architecture/Technology_Stack.md | Architecture principle |
| C086 | The cheapest sticker price is rarely the cheapest total cost | documented fact | high | S1, S4, S13 | [falsifier not stated] | W10 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Commercial conclusion |
| C087 | Pricing and product capabilities change frequently | documented fact | high | S1, S4, S5 | [falsifier not stated] | W10 | 00_Index/README.md | Working rule |
| C088 | Open-source frameworks can have low license cost while carrying substantial model, hosting, observability, and reliability cost | documented fact | high | S7, S13 | [falsifier not stated] | W10 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Pricing interpretation |
| C089 | Managed cloud platforms reduce operational work but increase provider coupling and consumption-accounting complexity | documented fact | high | S7, S13, S15, S16 | [falsifier not stated] | W10 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Pricing interpretation |
| C090 | For serious production systems, combine an agent framework/orchestrator with a durable execution layer | recommendation | high | S4, S7, S36 | [falsifier not stated] | W10 | 02_Service_Profiles/Agent_Orchestration_Comparison.md | Strongest architecture pattern |
| C091 | A 20-person company with limited engineering capacity and Microsoft 365 should use Power Automate | recommendation | medium | S3, S33 | [falsifier not stated] | W11 | Prompt Guided Research/At-a-Glance Comparison.md | Recommendation |
| C092 | n8n self-hosted is viable only if the company has an engineer who can own infrastructure | recommendation | medium | S2 | [falsifier not stated] | W11 | Prompt Guided Research/At-a-Glance Comparison.md | Strong alternative |
| C093 | Make lacks governance depth for sensitive data without Enterprise pricing | documented fact | high | S34 | [falsifier not stated] | W11 | Prompt Guided Research/At-a-Glance Comparison.md | Not recommended |
| C094 | Zapier task-based pricing becomes expensive at 500 workflows | documented fact | high | S1, S35 | [falsifier not stated] | W11 | Prompt Guided Research/At-a-Glance Comparison.md | Not recommended |
| C095 | Custom agent stack engineering and governance overhead is disproportionate for a 20-person company | documented fact | high | S7, S8, S36 | [falsifier not stated] | W11 | Prompt Guided Research/At-a-Glance Comparison.md | Not recommended |
| C096 | The decisive factor for a 20-person company with sensitive data is governance confidence | inference | medium | S3, S33 | [falsifier not stated] | W11 | Prompt Guided Research/At-a-Glance Comparison.md | Recommendation |
| C097 | Automation sprawl with no inventory or lifecycle management is an operational problem | documented fact | high | S25-S29 | [falsifier not stated] | W12 | 08_Problems_and_Opportunities/Problems.md | Operational problems |
| C098 | Poor retry semantics and unclear ownership of exceptions are operational problems | documented fact | high | S25-S29 | [falsifier not stated] | W12 | 08_Problems_and_Opportunities/Problems.md | Operational problems |
| C099 | Long-running processes that outlive sessions or workers are operational problems | documented fact | high | S25-S29 | [falsifier not stated] | W12 | 08_Problems_and_Opportunities/Problems.md | Operational problems |
| C100 | Model calls, retries, storage, and human review are hidden costs | documented fact | high | S1, S4, S13, S30 | [falsifier not stated] | W12 | 08_Problems_and_Opportunities/Problems.md | Economic problems |

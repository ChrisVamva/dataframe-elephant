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

# Metrics — Wave 3 (Automation Market Research)

| Metric ID | Metric name | Value | Unit | Scope / conditions | Claim type | Confidence | Source ID | Stage 1 source | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M1 | Zapier free tier tasks | 100 | tasks/month | Free plan | documented fact | high | S1 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| M2 | Zapier Professional starting price | 19.99 | USD/month | Annual billing | documented fact | high | S1 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| M3 | Power Automate Premium price | 15 | USD/user/month | Annual billing | documented fact | high | S3 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| M4 | Power Automate Process price | 150 | USD/bot/month | [conditions not stated in source] | documented fact | medium | S3 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| M5 | Power Automate per-user plan coverage | 5-10 | users | 20-person company where only 5-10 people build or run flows | reported signal | medium | S33 | Prompt Guided Research/At-a-Glance Comparison.md | Cost Analysis |
| M6 | Power Automate per-user monthly cost | 75-150 | USD/month | 5-10 users at $15/user/month | documented fact | high | S33 | Prompt Guided Research/At-a-Glance Comparison.md | Cost Analysis |
| M7 | Power Automate pay-as-you-go attended flow run | 0.60 | USD/run | Pay-as-you-go pricing | documented fact | high | S33 | Prompt Guided Research/At-a-Glance Comparison.md | Cost Analysis |
| M8 | Power Automate pay-as-you-go unattended flow run | 3.00 | USD/run | Pay-as-you-go pricing | documented fact | high | S33 | Prompt Guided Research/At-a-Glance Comparison.md | Cost Analysis |
| M9 | Temporal Cloud starting price | 50 | USD/million actions | Volume self-service down to $25/million | documented fact | high | S4 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| M10 | Temporal Cloud Essentials plan | 100 | USD/month | Base plan | documented fact | high | S31 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Orchestration actions |
| M11 | Temporal Cloud Business plan | 500 | USD/month | Base plan | documented fact | high | S31 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Orchestration actions |
| M12 | Temporal Cloud Active Storage price | 0.042 | USD/GB-hour | Active Storage | documented fact | high | S31 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | State storage |
| M13 | Temporal Cloud Retained Storage price | 0.00105 | USD/GB-hour | Retained Storage | documented fact | high | S31 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | State storage |
| M14 | UiPath Basic starting price | 25 | USD/month | Basic plan | documented fact | high | S5 | 03_Pricing_and_Commercials/Pricing_Snapshot.md | Pricing snapshot |
| M15 | n8n Cloud Pro price | 60 | EUR/month | 10,000 executions/month, annual billing | documented fact | high | S2 | Prompt Guided Research/At-a-Glance Comparison.md | Cost Analysis |
| M16 | n8n self-hosted server cost | 5-20 | USD/month | Small VPS | reported signal | medium | S2 | Prompt Guided Research/At-a-Glance Comparison.md | Cost Analysis |
| M17 | Make Teams plan | 29 | USD/month | 10,000 credits/month, annual billing | documented fact | high | S34 | Prompt Guided Research/At-a-Glance Comparison.md | Cost Analysis |
| M18 | Zapier Professional plan | 19.99 | USD/month | 750 tasks/month, annual billing | documented fact | high | S1 | Prompt Guided Research/At-a-Glance Comparison.md | Cost Analysis |
| M19 | Zapier Team plan | 69 | USD/month | 2,000 tasks/month | documented fact | high | S1 | Prompt Guided Research/At-a-Glance Comparison.md | Cost Analysis |
| M20 | Custom agent stack starting cost | 400-700 | USD/month | Durable execution and sandboxing alone | reported signal | medium | S7, S36 | Prompt Guided Research/At-a-Glance Comparison.md | Custom Agent Stack |
| M21 | Custom agent stack initial setup cost | 500-2000 | USD/month | Depending on scale | reported signal | medium | S7, S36 | Prompt Guided Research/At-a-Glance Comparison.md | Custom Agent Stack |
| M22 | n8n self-hosted maintenance time | 1-2 | hours/month | Routine updates, backups, log review | reported signal | medium | S2 | Prompt Guided Research/At-a-Glance Comparison.md | Maintenance Burden |
| M23 | n8n self-hosted setup time | 45-90 | minutes | Basic deployment on VPS | reported signal | medium | S2 | Prompt Guided Research/At-a-Glance Comparison.md | Setup Effort |
| M24 | n8n self-hosted maintenance per automation | 2-3 | hours/month | Across an estate | reported signal | medium | S2 | Prompt Guided Research/At-a-Glance Comparison.md | Maintenance Burden |
| M25 | Claude Managed Agents runtime price | 0.08 | USD/session-hour | Active runtime only; idle time not billed | documented fact | high | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Orchestration runtime |
| M26 | Claude Managed Agents monthly cost | 133 | USD | 10,000 runs at 20 minutes active execution per run | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Orchestration runtime |
| M27 | Self-hosted Temporal infrastructure cost | 480-790 | USD/month | AWS infra for Temporal | reported signal | medium | S4, S31 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Orchestration runtime |
| M28 | Self-hosted Temporal actions cost | 50 | USD | 1 million Actions per month | documented fact | high | S31 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Orchestration actions |
| M29 | Hosted state storage cost | 35 | USD/month | Managed Postgres | reported signal | medium | S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | State storage |
| M30 | Self-hosted state storage cost | 100-300 | USD/month | Self-managed Postgres | reported signal | medium | S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | State storage |
| M31 | LangSmith Plus plan price | 39 | USD/seat/month | Plus tier | documented fact | high | S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Tracing |
| M32 | LangSmith trace overage price | 2.50 | USD/1,000 traces | Plus tier overage | documented fact | high | S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Tracing |
| M33 | Hosted tracing cost | 25 | USD/month | Allocated trace-related portion | reported signal | medium | S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Tracing |
| M34 | Self-hosted tracing cost | 60 | USD/month | Langfuse + ClickHouse hardware | reported signal | medium | S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Tracing |
| M35 | Human review cost | 600 | USD/month | 3-minute review at $60/hr, 20% of runs | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Human review |
| M36 | Human review rate | 20 | percent | Of runs require review | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Human review |
| M37 | Retry rate | 15 | percent | Complex tasks | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Failures / retries |
| M38 | Failures and retries cost | 360 | USD/month | 15% retry rate with 1.2x effective multiplier | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Failures / retries |
| M39 | Hosted operational labor | 0 | FTE | Zero ops for managed platform | documented fact | high | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Operational labor |
| M40 | Self-hosted operational labor | 0.25-1.0 | FTE | For Temporal/LangGraph ops | reported signal | medium | S4, S7 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Operational labor |
| M41 | Self-hosted labor cost | 2000-6000 | USD/month | 0.25-0.75 FTE at $8,000/month fully loaded | reported signal | medium | S4, S7 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Operational labor |
| M42 | Hosted total infra cost | 3003 | USD/month | Infrastructure only, excludes labor | reported signal | medium | S30, S31, S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Total (infra only) |
| M43 | Self-hosted total infra cost | 3500-4000 | USD/month | Infrastructure only | reported signal | medium | S4, S31, S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Total (infra only) |
| M44 | Hosted total with labor | 3003 | USD/month | Excludes labor on hosted side | reported signal | medium | S30, S31, S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Total (with labor) |
| M45 | Self-hosted total with labor | 5500-10000 | USD/month | Includes 0.25-1.0 FTE labor | reported signal | medium | S4, S31, S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Total (with labor) |
| M46 | Runs per month | 10000 | runs | Workload assumption | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Workload Assumptions |
| M47 | Input tokens per run | 60000 | tokens | Mid-tier model assumption | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Workload Assumptions |
| M48 | Output tokens per run | 3000 | tokens | Mid-tier model assumption | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Workload Assumptions |
| M49 | Active execution per run | 20 | minutes | Per run | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Workload Assumptions |
| M50 | Web searches per run | 0.05 | searches | Per run | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Workload Assumptions |
| M51 | 30-day approval wait | 30 | days | Human approval gate | documented fact | high | S36 | Prompt Guided Research/Runtime Ownership Comparison.md | 30-Day Human Approval |
| M52 | Duplicate payment amount | 480000 | USD | Fortune 500 company payment | documented fact | high | S26 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 2 |
| M53 | Number of RPA bots at insurer | 40 | bots | Large Midwest insurer | documented fact | high | S25 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 1 |
| M54 | Corrupted customer profiles | 15000 | profiles | Bank KYC validation bot | documented fact | high | S27 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 3 |
| M55 | Silent corruption duration | 90 | days | Bot operated in green state | documented fact | high | S27 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 3 |
| M56 | Decommissioned bots without access removal | 55 | of 56 bots | GSA RPA program | documented fact | high | S29 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 5 |
| M57 | Access removal window | 14 | days | Required by GSA policy | documented fact | high | S29 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 5 |
| M58 | RPA project failure rate | 30-50 | percent | Ernst & Young study | reported signal | medium | S25 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Summary |
| M59 | RPA maintenance budget share | 70-75 | percent | Of total RPA automation budgets | reported signal | medium | S25 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Summary |
| M60 | EY RPA failure study | 50 | percent | Of RPA projects fail outright | reported signal | medium | S25 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Summary |
| M61 | Make Core price | 9 | USD/month | Annual billing, 10,000 credits | documented fact | high | S34 | Prompt Guided Research/At-a-Glance Comparison.md | Make pricing |
| M62 | Make Pro price | 16 | USD/month | Annual billing | documented fact | high | S34 | Prompt Guided Research/At-a-Glance Comparison.md | Make pricing |
| M63 | Make Teams price | 29 | USD/month | Annual billing, 10,000 credits | documented fact | high | S34 | Prompt Guided Research/At-a-Glance Comparison.md | Make pricing |
| M64 | n8n Starter price | 24 | EUR/month | 2,500 executions | documented fact | high | S2 | Prompt Guided Research/At-a-Glance Comparison.md | n8n pricing |
| M65 | n8n Business price | 667 | EUR/month | Self-hosted Business tier | documented fact | high | S2 | Prompt Guided Research/At-a-Glance Comparison.md | n8n pricing |
| M66 | Claude Sonnet 4.6 input price | 3 | USD/MTok | Per million input tokens | documented fact | high | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Model Tokens |
| M67 | Claude Sonnet 4.6 output price | 15 | USD/MTok | Per million output tokens | documented fact | high | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Model Tokens |
| M68 | Web search price | 10 | USD/1,000 searches | Anthropic tool use pricing | documented fact | high | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Tool Calls |
| M69 | LangGraph Platform Plus plan | 39 | USD/seat/month | Plus tier | documented fact | high | S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Tracing |
| M70 | n8n self-hosted 3-year savings vs Zapier | 71 | percent | Cost savings over three years | reported signal | medium | S2 | Prompt Guided Research/At-a-Glance Comparison.md | n8n pricing |
| M71 | Make savings vs Zapier at 10,000 operations | 93 | percent | Cost savings | reported signal | medium | S2 | Prompt Guided Research/At-a-Glance Comparison.md | Make pricing |
| M72 | Anthropic code review cost per task | 280 | USD/task | External engineers training Claude | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Human review |
| M73 | Human review cost per changed line | 0.24 | USD/line | Human review | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Human review |
| M74 | Model cost per changed line | 0.114 | USD/line | Agent-produced line | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Model tokens |
| M75 | HITL AI process cost range | 0.08-2.40 | USD/task | Depending on complexity and domain | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Human review |
| M76 | Fully automated pipeline cost range | 0.002-0.04 | USD/task | Fully automated | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Human review |
| M77 | Agent retry loop overnight cost | 72000 | USD | Single runaway loop documented by SatGate | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Failures / retries |
| M78 | Retry tax per month | 600-900 | USD/month | 50 retries at $30 each | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Failures / retries |
| M79 | Workflow execution retry cost multiplier | 1.37 | x | 20% per-step failure | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Failures / retries |
| M80 | 5% failure rate cost increase | 15-30 | percent | With 2 retries per failure | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Failures / retries |
| M81 | 20% per-step failure cost multiplier | 1.37 | x | Retry budget | reported signal | medium | S30 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Failures / retries |
| M82 | Network timeout duration | 800 | milliseconds | API connection drop in payment incident | documented fact | high | S26 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 2 |
| M83 | Duplicate payment amount | 480000 | USD | Fortune 500 payment executed twice | documented fact | high | S26 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 2 |
| M84 | GSA active bots | 119 | bots | At time of audit | documented fact | high | S29 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 5 |
| M85 | GSA decommissioned bots | 24 | bots | At time of audit | documented fact | high | S29 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 5 |
| M86 | GSA systems without bot security plans | 7 | of 16 systems | Reviewed systems | documented fact | high | S29 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 5 |
| M87 | GSA systems failing to authorize non-person entities | 10 | of 16 systems | Reviewed systems | documented fact | high | S29 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 5 |
| M88 | Copado incident duration | [conditions not stated in source] | [conditions not stated in source] | EMEA regions affected | documented fact | high | S28 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 4 |
| M89 | Insurer bot failure time | 11 | PM | Bots failed around 11pm | documented fact | high | S25 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 1 |
| M90 | Insurer bot discovery time | next morning | [conditions not stated in source] | Issue not discovered until next morning | documented fact | high | S25 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 1 |
| M91 | Bank bot silent corruption duration | 90 | days | Bot operated in green state | documented fact | high | S27 | Prompt Guided Research/Incidents, five publicly documented incidents.md | Incident 3 |
| M92 | Make Core operations | 10000 | credits/month | Core plan | documented fact | high | S34 | Prompt Guided Research/At-a-Glance Comparison.md | Make pricing |
| M93 | Make Free tier operations | 1000 | credits/month | Free plan | documented fact | high | S34 | Prompt Guided Research/At-a-Glance Comparison.md | Make pricing |
| M94 | Zapier Free tier tasks | 100 | tasks/month | Free plan | documented fact | high | S1 | Prompt Guided Research/At-a-Glance Comparison.md | Zapier pricing |
| M95 | Zapier Professional tasks | 750 | tasks/month | Professional plan | documented fact | high | S1 | Prompt Guided Research/At-a-Glance Comparison.md | Zapier pricing |
| M96 | Zapier Team tasks | 2000 | tasks/month | Team plan | documented fact | high | S1 | Prompt Guided Research/At-a-Glance Comparison.md | Zapier pricing |
| M97 | LangGraph Platform Plus base traces | 10000 | traces/month | Included in Plus plan | documented fact | high | S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Tracing |
| M98 | LangSmith trace overage price | 2.50 | USD/1,000 traces | Plus tier | documented fact | high | S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Tracing |
| M99 | LangSmith extended retention trace price | 5 | USD/1,000 traces | 400-day retention | documented fact | high | S13 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Tracing |
| M100 | Temporal Cloud Developer Support | 10 | percent | Of usage | documented fact | high | S31 | Prompt Guided Research/Monthly Cost Breakdown – 10,000 Runs.md | Orchestration actions |

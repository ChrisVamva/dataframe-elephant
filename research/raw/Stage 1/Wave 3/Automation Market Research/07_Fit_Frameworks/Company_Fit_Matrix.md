# Company fit matrix

| Company profile | Best starting layer | Why | Avoid starting with |
|---|---|---|---|
| Solo operator / freelancer | Zapier, Make, or n8n Cloud | Fast wins with low setup | Enterprise RPA or custom agent platform |
| Small technical company | n8n, Make, Pipedream | Flexibility plus API and code access | Heavy enterprise suite before process maturity |
| Microsoft-centric SMB | Power Automate | Strong identity, M365, Teams, Outlook, Dynamics fit | Duplicating Microsoft connectors elsewhere |
| Regulated enterprise | Workato, Power Automate, UiPath, ServiceNow | Governance, audit, access controls, support | Unmanaged personal automations |
| Engineering-led product company | Temporal plus LangGraph or agent SDK | Durable execution plus controlled AI orchestration | Treating Zapier as core transaction runtime |
| Legacy-heavy shared services | UiPath / Power Automate Desktop | UI automation and process mining | Assuming APIs exist everywhere |
| AI-native startup | LangGraph, OpenAI Agents SDK, Temporal | Product-specific agents with durable state | Building critical workflows on unbounded agent loops |
| Data/analytics team | Dagster, Prefect, Temporal, n8n | Pipelines, schedules, lineage, reproducibility | UI-only RPA for data pipelines |

## Selection questions

1. Is the workflow mostly API, UI, human, or AI reasoning?
2. What happens if it runs twice?
3. How long can it run or wait?
4. Does a human need to approve any step?
5. Who owns failures and credentials?
6. Is self-hosting required?
7. What is the expected monthly volume?
8. Is the process a competitive product capability or an internal utility?

## Rule of thumb

Buy convenience for commodity integrations. Build or adopt durable orchestration for critical workflows. Add agents only where uncertainty or interpretation is the bottleneck.

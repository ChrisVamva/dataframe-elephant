# Service profiles

| Service | Primary layer | Best at | Main buyer | Main constraint |
|---|---|---|---|---|
| Zapier | SaaS integration | Fast no-code app connections | Individual / SMB | Task-based cost at volume |
| Make | Visual integration | Flexible branching and transformations | SMB / prosumer | Complexity can become hard to govern |
| n8n | Technical workflow automation | Self-hosting, code nodes, AI workflows | Technical SMB / developer | Requires operations skill when self-hosted |
| Workato | Enterprise iPaaS | Governed integrations and business automation | Enterprise IT | Pricing is sales-led; implementation effort |
| Power Automate | Microsoft ecosystem | M365, Dynamics, desktop RPA | Microsoft-centric companies | Licensing and environment complexity |
| UiPath | RPA / agentic automation | UI automation, process mining, robots | Enterprise shared services | Governance, licenses, process maintenance |
| Temporal | Durable execution | Long-running, retryable, fault-tolerant code | Engineering teams | Not a no-code business-user tool |
| LangGraph | Agent orchestration | Stateful, controllable AI-agent workflows | AI product engineers | Low-level; requires application design |
| OpenAI Agents SDK | Agent framework | Model/tool handoffs and agent building | Developers | Depends on model/provider architecture |
| ServiceNow | Enterprise workflow | ITSM, service operations, agentic enterprise workflows | Large enterprises | Strongest inside ServiceNow estate |

## Important distinctions

- **Automation platform** is not the same as **workflow runtime**.
- **RPA** acts through screens and machines; **iPaaS** acts through APIs and connectors.
- **Agent orchestration** adds probabilistic reasoning; it does not remove the need for deterministic controls.
- **Protocols** such as MCP and A2A improve interoperability but are not complete automation products.

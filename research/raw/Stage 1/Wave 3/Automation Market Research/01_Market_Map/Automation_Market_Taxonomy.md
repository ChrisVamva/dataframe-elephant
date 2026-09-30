# Automation market taxonomy

## 1. Integration automation

**Examples:** Zapier, Make, n8n, Pipedream, Workato, Tray.ai.  
**Core job:** Move data and trigger actions between applications.  
**Buyer:** Individuals, SMB operations, RevOps, IT, enterprise integration teams.  
**Differentiator:** Connector breadth, ease of use, execution economics, governance.

## 2. RPA and desktop automation

**Examples:** UiPath, Automation Anywhere, Blue Prism, Power Automate Desktop.  
**Core job:** Automate UI and legacy systems where APIs are absent or inadequate.  
**Buyer:** Large organizations, shared services, finance, operations, compliance.  
**Trade-off:** Strong reach into legacy interfaces, but maintenance and governance burden.

## 3. Durable workflow orchestration

**Examples:** Temporal, AWS Step Functions, Azure Durable Functions, Google Workflows, Prefect, Dagster.  
**Core job:** Run long-lived, retryable, stateful software workflows.  
**Buyer:** Engineering and platform teams.  
**Trade-off:** High reliability and control, but developer skill is required.

## 4. Agent orchestration

**Examples:** LangGraph, LangChain, OpenAI Agents SDK, Microsoft Agent Framework, Google ADK, CrewAI.  
**Core job:** Coordinate model calls, tools, memory, delegation, approval, and reasoning loops.  
**Buyer:** Product engineering, AI teams, innovation groups.

## 5. Enterprise process suites

**Examples:** ServiceNow, Salesforce Flow/Agentforce, SAP Build, Microsoft Power Platform, Appian, Pega.  
**Core job:** Embed automation into governed business processes and systems of record.

## Market boundary

No single platform dominates every layer. A serious architecture may combine a user-facing integration tool, a durable execution engine, an agent runtime, and enterprise identity/governance.

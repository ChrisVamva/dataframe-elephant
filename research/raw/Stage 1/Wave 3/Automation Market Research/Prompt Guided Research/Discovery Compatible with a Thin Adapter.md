---
modified: 2026-09-29T16:38:23+03:00
---
Yes, MCP and A2A can be combined in a single workflow, but **not without some adapter code**. The protocols are designed to be complementary—MCP handles vertical agent-to-tool connections, while A2A handles horizontal agent-to-agent collaboration. However, several semantic and transport gaps require bridging logic. Below is a point-by-point test of whether the combination works without custom translation, and what minimum adapter code is required.

---

## 🔍 Discovery: Compatible with a Thin Adapter

**Verdict: Not seamless, but bridgeable with minimal code.**

| Aspect | MCP | A2A |
|---|---|---|
| **Discovery mechanism** | Centralized metaregistry with GitHub-authenticated publishing and structured metadata | Decentralized via JSON-based **Agent Cards**, discoverable through well-known URIs (`.well-known/agent-card.json`) or curated catalogs |
| **Capability format** | MCP capability lists | A2A Agent Cards |

**The gap:** An MCP client cannot natively understand an A2A Agent Card. A bridge is needed to translate Agent Card metadata into a format MCP clients can consume.

**Minimum adapter code:** The `a2a_mcp_bridge` server exposes MCP tools like `list_agents` and `register_agent` that wrap A2A Agent Card discovery into an MCP-compatible interface. The adapter code is approximately:

```python
# Minimal discovery adapter: wrap A2A Agent Card as MCP tool
async def list_a2a_agents(agent_card_url: str) -> list[dict]:
    """Fetch A2A Agent Card and return as MCP-compatible tool listing."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{agent_card_url}/.well-known/agent-card.json")
        card = resp.json()
    return [{
        "name": card["name"],
        "description": card["description"],
        "capabilities": card.get("skills", []),
        "endpoint": card["url"]
    }]
```

An agent registered with an AGTP governance platform is discoverable regardless of which protocol it uses, and AGMP-specific capability formats (A2A Agent Cards, MCP capability lists) can be included as extensions to the same Capability Document.

---

## 🔐 Authentication: Partially Unified, Requires Scope Aggregation

**Verdict: No native unification; requires an OAuth scope aggregation layer.**

| Aspect | MCP | A2A |
|---|---|---|
| **Auth model** | OAuth 2.1 authorization server with appropriate security measures for confidential and public clients | Client is responsible for obtaining required credentials (OAuth 2.0 tokens, API keys, JWT) **outside** the A2A protocol |
| **Token flow** | MCP authorization server issues tokens | A2A clients must acquire credentials externally |

**The gap:** A single agent workflow that calls MCP tools *and* delegates tasks via A2A needs a **single OAuth flow for aggregated scopes**—the agent initiates one OAuth flow that covers both the MCP tool calls and the A2A task delegation.

**Minimum adapter code:** A scope aggregation layer that acquires a single token with combined scopes:

```python
# Minimal auth adapter: aggregate scopes for MCP + A2A
async def get_aggregated_token(mcp_scopes: list[str], a2a_scopes: list[str]) -> str:
    """Obtain a single OAuth token covering both MCP and A2A scopes."""
    all_scopes = mcp_scopes + a2a_scopes
    token_response = await oauth_client.fetch_token(
        token_url=AUTH_SERVER,
        scopes=all_scopes
    )
    return token_response["access_token"]
```

An agent operating across both protocols must use the same canonical Agent-ID in all headers, even if the underlying MCP client_id and A2A agent.id differ.

---

## 📋 Task Status: Different State Machines, Requires Mapping

**Verdict: Not directly compatible; requires a state-mapping adapter.**

| Aspect | MCP | A2A |
|---|---|---|
| **Task states** | Created, Working, Waiting, Completed, Failed | Submitted, Working, Completed, Failed, Cancelled, Rejected, Input-Required |
| **Status field** | `isError` flag | `status` field with TaskState values |

**The gap:** A2A has richer task states, including `INPUT_REQUIRED` (task paused waiting for human input) and `REJECTED` (task terminated by remote agent). MCP's simpler state machine lacks these. When A2A returns `INPUT_REQUIRED`, it must be mapped to MCP's `isError: true` pattern, because MCP has no native "needs input" state.

**Minimum adapter code:**

```python
# Minimal status mapping adapter
def map_a2a_to_mcp_status(a2a_state: str) -> dict:
    """Map A2A TaskState to MCP-compatible status."""
    mapping = {
        "TASK_STATE_SUBMITTED": {"isError": False, "status": "working"},
        "TASK_STATE_WORKING":   {"isError": False, "status": "working"},
        "TASK_STATE_COMPLETED": {"isError": False, "status": "completed"},
        "TASK_STATE_FAILED":    {"isError": True,  "status": "failed"},
        "TASK_STATE_REJECTED":  {"isError": True,  "status": "rejected"},
        "TASK_STATE_INPUT_REQUIRED": {"isError": True, "status": "input_required"},
    }
    return mapping.get(a2a_state, {"isError": True, "status": "unknown"})
```

Both protocols now use the same unified status system with A2A TaskState values when carrying AdCP payloads, which demonstrates that alignment is achievable.

---

## 📡 Streaming: Different Transports, Requires Translation

**Verdict: Not directly compatible; requires a transport bridge.**

| Aspect | MCP | A2A |
|---|---|---|
| **Transport** | JSON-RPC 2.0 over HTTPS with **streamable HTTP**; SSE notifications for streaming | **SSE streaming** for real-time updates |
| **Streaming model** | Server-side streaming for partial results; synchronous tool calls | Bidirectional streaming supported; `message/stream` returns a Stream of Event objects |

**The gap:** Traditional REST-centric proxies cannot handle MCP and A2A session fan-out, bidirectional SSE, or protocol negotiation. A transport bridge is required to translate between MCP's streamable HTTP and A2A's SSE event streams.

**Minimum adapter code:** The `a2a_mcp_bridge` server currently supports the **streamable-http** transport, bridging A2A's SSE streams into MCP's streamable HTTP format. The adapter code is approximately:

```python
# Minimal streaming bridge: A2A SSE → MCP streamable HTTP
async def bridge_a2a_stream(a2a_endpoint: str, task_id: str):
    """Bridge A2A SSE stream to MCP-compatible stream."""
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", f"{a2a_endpoint}/tasks/{task_id}/stream") as resp:
            async for event in resp.aiter_lines():
                if event.startswith("data:"):
                    # Re-emit as MCP streamable HTTP chunk
                    yield f"data: {event[5:]}\n\n"
```

A2A's `message/stream` method sends a message to the agent and subscribes to real-time updates, returning a Stream that emits `A2AException` if the server sends a JSON-RPC error within the event stream.

---

## ⚠️ Error Handling: Two Different Patterns, Requires Normalization

**Verdict: Not directly compatible; requires error normalization.**

| Aspect | MCP | A2A |
|---|---|---|
| **Fatal error pattern** | `isError: true` in the tool call response | `status: "failed"` in the task status |
| **Error codes** | JSON-RPC error codes | Typed A2A error codes (-32001 to -32009) |
| **Pending states** | Not natively distinguished | `input-required`, `auth-required` are explicit states |

**The gap:** A2A has three answers—"done," "broken," and "I need input you have not sent"—while MCP has only two. MCP's only channel for "fix your call and try again" is `isError`, so A2A states like `TASK_STATE_INPUT_REQUIRED` cross into MCP as `isError: true`. A bridge must **never re-emit an A2A error code as a JSON-RPC code**, because JSON-RPC reserves those codes.

**Minimum adapter code:**

```python
# Minimal error normalization adapter
def normalize_error(source: str, error: dict) -> dict:
    """Normalize MCP and A2A errors to a unified format."""
    if source == "a2a":
        return {
            "isError": True,
            "error_code": error.get("code"),
            "message": error.get("message"),
            "a2a_state": error.get("status", {}).get("state")
        }
    elif source == "mcp":
        return {
            "isError": error.get("isError", False),
            "error_code": error.get("code"),
            "message": error.get("message"),
            "a2a_state": None
        }
```

---

## 🧩 Minimum Adapter Code Summary

| Gap | Adapter Required | Approx. Lines | Reference |
|---|---|---|---|
| **Discovery** | Agent Card → MCP tool listing | ~15 | `a2a_mcp_bridge` |
| **Authentication** | OAuth scope aggregation | ~10 | OAuth 2.0 Scope Aggregation |
| **Task Status** | State machine mapping | ~20 | AdCP Protocol Comparison |
| **Streaming** | SSE ↔ streamable HTTP bridge | ~15 | `a2a_mcp_bridge` streamable-http support |
| **Error Handling** | Error code normalization | ~20 | A2A-to-MCP error translation |
| **Total** | **Minimal adapter layer** | **~80 lines** | |

---

## 💎 Bottom Line

MCP and A2A **cannot be combined without custom translation**, but the required adapter is **thin (~80 lines of glue code)** because the protocols are architecturally complementary. The critical gaps are:

1. **Discovery** — A2A Agent Cards must be wrapped as MCP tools
2. **Authentication** — A single OAuth scope aggregation flow is needed
3. **Task Status** — A2A's richer state machine must be mapped to MCP's binary `isError` model
4. **Streaming** — A2A SSE must be bridged to MCP streamable HTTP
5. **Error Handling** — A2A error codes must be normalized without leaking into JSON-RPC

The `a2a_mcp_bridge` package provides a ready-made implementation of most of this adapter layer, supporting `cancel_task`, `get_task_result`, `list_agents`, `register_agent`, `send_message`, and `unregister_agent` as MCP tools that manage A2A agents. A unified TLAS (Three-Layer Agentic Stack) approach reduces integration complexity by an estimated **60–70%** compared to ad-hoc solutions.

[

![](https://cdn.deepseek.com/site-icons/pypi.org)

PyPI

2026/01/24

servicenow-api - Python ServiceNow API Wrapper

This project started out as a python wrapper for ServiceNow, but since the dawn of standards like Model Context Protocol (MCP) and Agent2Agent (A2A) Agent. ... ServiceNow A2A implements a multi-agent system designed to manage and interact with ServiceNow tasks through a delegated, specialist-based architecture. Built using Python ... This allows this agent to be integrated in any agentic framework like Microsoft Agent Framework (MAF) or crew.ai.



](https://pypi.org/project/servicenow-api/1.5.0/#1)[

![](https://cdn.deepseek.com/site-icons/microsoft.com)

Learn Microsoft

2026/09/10

Herstellen einer Verbindung mit einem A2A-Agent-Endpunkt des Foundry Agent Service - Microsoft Foundry - Fügen Sie als Nächstes die Toolbox als MCP-Tool an den gehosteten Agent an, und führen Sie sie aus:

als MCP-Tool an den gehosteten Agent an ... Der Agent ruft den sekundären Agent über dena2a-toolbox MCP-Endpunkt auf und druckt die konsolidierte Antwort: Agent: The secondary agent can help with ... ... Beim Aufrufen ruft der gehostete Agent den sekundären Agent über dena2a-toolbox MCP-Endpunkt



](https://learn.microsoft.com/de-at/azure/foundry/agents/how-to/tools/agent-to-agent?pivots=csharp#2)[

![](https://cdn.deepseek.com/site-icons/pub.dev)

Dart packages

2025/12/22

a2a_mcp_bridge | Dart package

An MCP server that bridges the Model Context Protocol (MCP) with the Agent-to-Agent (A2A) protocol ... By bridging these protocols, this server allows MCP clients to discover, register, communicate with, and manage tasks on A2A agents through a unified interface. ... AI assistants such as Claude...



](https://pub.dev/packages/a2a_mcp_bridge/versions/1.1.0#1)[

![](https://cdn.deepseek.com/site-icons/pypi.org)

PyPI

2025/01/05

servicenow-api

This project started out as a python wrapper for ServiceNow, but since the dawn of standards like Model Context Protocol (MCP) and Agent2Agent (A2A) Agent. ... ServiceNow A2A implements a multi-agent system designed to manage and interact with ServiceNow tasks through a delegated, specialist-based architecture. Built using Python ... This allows this agent to be integrated in ... (MAF) or crew.ai.



](https://pypi.org/project/servicenow-api/1.6.25/#1)[

![](https://cdn.deepseek.com/site-icons/pypi.org)

PyPI

2026/03/12

gitlab-api - GitLab API + MCP Server + A2A Server

GitLab A2A implements a multi-agent system designed to manage and interact with GitLab tasks through a delegated, specialist-based architecture. Built using Python ... The system runs as a FastAPI server via Uvicorn ... The core idea is an orchestrator agent that analyzes user queries and delegates subtasks to specialized child agents, each focused on a specific domain (e.g., merge requests...



](https://pypi.org/project/gitlab-api/25.15.43/#1)[

![](https://cdn.deepseek.com/site-icons/microsoft.com)

Learn Microsoft

2026/08/04

Foundry Agent Service から A2A エージェント エンドポイントに接続する - Microsoft Foundry - async def main() -> None:

予期される出力 エージェントは、a2a-toolbox MCP エンドポイントを介してセカンダリ エージェントを呼び出し、統合された応答を出力します。 Agent: The secondary agent can help with ... ... Prompt Agents を選択して...



](https://learn.microsoft.com/ja-jp/azure/foundry/agents/how-to/tools/agent-to-agent#2)[

![](https://cdn.deepseek.com/site-icons/microsoft.com)

Learn Microsoft

2026/08/04

Liga-te a um endpoint de agente A2A através do Foundry Agent Service - Microsoft Foundry - import { DefaultAzureCredential } from "@azure/identity";

// Add the A2A tool to a toolbox ... De seguida, liga a caixa de ferramentas a um agente de prompt como ferramenta MCP e executa-a ... // Attach the toolbox to a prompt agent as an MCP tool const agent = await project.agents.createVersion("MyA2AAgent" ... Para a maioria dos agentes, adiciona a ferramenta A2A através de uma caixa de ferramentas e liga a caixa de ferramentas ao teu agente como uma ferramenta MCP.



](https://learn.microsoft.com/pt-pt/azure/foundry/agents/how-to/tools/agent-to-agent?view=foundry-classic#3)[

Elastic

2026/05/26

A2A Protocol & MCP: Creating an LLM Agent newsroom in Elasticsearch - Blog

Discover how to build a specialized hybrid LLM agent newsroom using A2A Protocol for agent collaboration and MCP for tool access in Elasticsearch. ... Step 4: Archive Agent uses Elastic A2A Agent with MCP ... This demonstrates the hybrid architecture where A2A enables agent collaboration while MCP provides tool access...



](https://www.elastic.co/search-labs/blog/a2a-protocol-mcp-llm-agent-workflow-elasticsearch#1)[

![](https://cdn.deepseek.com/site-icons/abp.io)

ABP.IO

2026/05/20

Building a Multi-Agent AI System with A2A, MCP, and ADK in .NET

How we combined three open AI protocols — Google's A2A & ADK with Anthropic's MCP — to build a production-ready Multi-Agent Research Assistant using .NET 10. ... MCP, A2A, and ADK are not competitors — they're complementary layers of a complete agent system.



](https://abp.io/community/articles/building-a-multiagent-ai-system-with-a2a-mcp-iefdehyx#gsc.tab=0)[

![](https://cdn.deepseek.com/site-icons/zenodo.org)

Zenodo

2026/06/04

Toward a Unified Interoperability Framework for Autonomous AI Agent Ecosystems: MCP, A2A, ACP, and ANP - Zenodo is currently experiencing slowness and intermittent outages due to heavy automated traffic from bots and AI crawlers

Four emerging open protocols—Model Context Protocol (MCP), Agent-to-Agent Protocol (A2A) ... Our analysis demonstrates that MCP and A2A are complementary rather than competing, that ACP and ANP serve distinct ecosystem niches, and that a unified TLAS approach reduces integration complexity by an estimated 60–70% compared to ad-hoc solutions.



](https://zenodo.org/records/20549818#1)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arXiv

2026/08/08

LAP: An Agent-to-Instrument Protocolfor Autonomous Science - The shared insufficiency of all these standards for AI agents is structural, not incidental: they assume a deterministic softwar...

MCP is the “USB-C for tool connectivity” (vertical, agenttool), while A2A is “HTTP for agent collaboration” (horizontal, agent↔\leftrightarrowagent). Production systems routinely combine both: A2A routes a task to the right specialist agent; MCP gives that agent its context and tools.↔\leftrightarrow



](https://ar5iv.labs.arxiv.org/html/2606.03755#2)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/05/31

From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review - MCP is designed around a client-server architecture in which host applications connect to multiple lightweight servers [219]

MCP (Model Context Protocol) focuses on integrating data and tools into LLM workflows, providing a standardized interface for delivering context. ... A2A (Agent-to-Agent Protocol) enables interoperability between agents across different frameworks, allowing them to exchange tasks and collaborate.



](https://ieeexplore.ieee.org/document/11540994/citations?tabFilter=papers#citations#8)[

![](https://cdn.deepseek.com/site-icons/huggingface.co)

Hugging Face

2026/05/13

Paper page - A survey of agent interoperability protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)

Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A) ... Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP), each addressing interoperability in deployment contexts. ... A2A enables peer-to-peer task delegation using capability-based Agent Cards, supporting secure and scalable collaboration across enterprise agent workflows.



](https://huggingface.co/papers/2505.02279#code#1)[

![](https://cdn.deepseek.com/site-icons/kodekloud.com)

KodeKloud

2026/07/14

A2A vs MCP, Agent Communication Protocols for DevOps in 2026

MCP and A2A solve different problems, because MCP connects a single agent downward to tools and data while A2A connects agents sideways to each other as peers. - Both protocols now live under the Agentic AI Foundation ... - Most teams should start with MCP alone and add A2A only when agents owned



](https://kodekloud.com/blog/a2a-vs-mcp-agent-communication-protocols-explained-for-devops/#1#1)[

![](https://cdn.deepseek.com/site-icons/beam.ai)

Beam AI

2026/06/22

Agent2Agent vs MCP: 2 Protocols Your 2026 Stack Needs

which Anthropic released in November 2024 ... and Agent2Agent (A2A) ... MCP answers "how does one agent reach the systems it needs." A2A answers "how do two agents that don't share a codebase work together." ... MCP vs A2A, side by side ... MCP equips a single agent with capabilities, and A2A lets that equipped agent collaborate with others.



](https://beam.ai/agentic-insights/agent2agent-vs-mcp-2026-ai-agent-stack?utm_source=blog&utm_medium=content&utm_campaign=uae-ai-strategy-2031-steering-the-emirates-toward-a-data-driven-future)[

![](https://cdn.deepseek.com/site-icons/obspm.fr)

Observatoire de Paris

2026/07/25

A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems

This paper presents an implementation-grounded comparison of the Model Context Protocol (MCP) and the Agent2Agent (A2A) protocol ... The results evidence that MCP can support inter-agent coordination ... a comparatively lightweight implementation model with lower coordination complexity ... A2A provides richer native support for stateful, multi-turn coordination through protocol-level abstractions for tasks and lifecycle management ... The results indicate that MCP ... through a comparatively lightweight implementation model with lower coordination complexity...



](https://arxiv-org.ezproxy.obspm.fr/html/2607.23884v1#1)[

Lyzr

2026/09/04

A2A vs MCP vs REST: Agent Protocols Compared

MCP (Model Context Protocol) connects one agent to its tools and data, with capabilities discovered at runtime instead of hard-coded. - A2A (Agent2Agent) connects independent agents to each other so they can delegate tasks across teams, frameworks, and vendors. ... an MCP server is a supply-chain dependency ... use MCP when an agent needs to discover and call tools at runtime, and use A2A



](https://www.lyzr.ai/blog/a2a-vs-mcp-vs-rest)[

![](https://cdn.deepseek.com/site-icons/decodo.com)

Decodo

2026/09/01

A2A vs. MCP: Comparing AI Agent Communication Methods - A2A vs. MCP: Comparing AI Agent Communication Methods

MCP reaches down from one agent to tools, data, and APIs. ... The A2A vs. MCP distinction reduces to the direction of the call. MCP is vertical, with an agent reaching down to a tool that executes and returns a value. A2A is horizontal...



](https://decodo.com/blog/a2a-vs-mcp#1)[

MintMCP

2026/09/09

A2A Protocol Explained: How Agent2Agent Works (and Where It Fits with MCP) (2026) | MintMCP Blog

A2A and MCP are complementary protocols: MCP connects agents to tools and data sources; A2A connects agents to other agents for multi-agent orchestration ... A2A and MCP solve different but complementary problems in the agent infrastructure stack. ... - MCP (Model Context Protocol) ... SAP's enterprise architecture documentation shows both protocols together, with MCP



](https://docs.mintmcp.com/blog/a2a-protocol-explained)[

![](https://cdn.deepseek.com/site-icons/kci.go.kr)

KCI

2026/06/30

A Practical MCP×A2A Integration Framework for Interoperability in LLM-Based Autonomous Multi-Agent Systems

this paper proposes a practical framework that integrates Google’s Agent-to-Agent (A2A) protocol with Anthropic’s Model Context Protocol (MCP). ... The proposed framework is implemented on LangGraph, enabling agent workflows with cyclic logic and dynamic context propagation. As a practical case study...



](https://www.kci.go.kr/kciportal/mobile/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003249786#1)[

![](https://cdn.deepseek.com/site-icons/deeplearning.ai)

DeepLearning.AI - Learning Platform

2026/02/10

A2A: The Agent2Agent Protocol - DeepLearning.AI

For this example, you'll create a healthcare provider recommendation agent using LangGraph and OpenAI GPT OSS on Vertex AI. ... LangGraph serving, LangSmith, has a built-in A2A integration, but it works very differently than the other integrations in this lesson. So for consistency ... Expose agents built with frameworks like Google ADK, LangGraph, or BeeAI as A2A servers to make them A2A-compliant.



](https://learn.deeplearning.ai/courses/a2a-the-agent2agent-protocol/lesson/wrgoel/creating-an-a2a-healthcare-provider-agent-using-langgraph-and-mcp)[

Neuralingual MCP - AI-Powered Affirmation Practice Tool - MCP Service

2026/01/23

A2A Agent Orchestration System - Intelligent Task Coordination - MCP Service

A distributed multi-agent system that orchestrates complex tasks using A2A protocol, MCP, and LangGraph, suitable for automated task decomposition and execution. ... A distributed multi-agent system that orchestrates complex tasks across specialized AI agents using A2A (Agent-to-Agent) protocol, MCP (Model Context Protocol) and LangGraph.



](https://www.mcpworld.com/en/detail/522a967146f49d827d4b7156d160b715)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/05/02

GitHub - trieu/sample-multi-agent-ai-system · GitHub

Tool integration | MCP (mcp 1.26.0) | Standardised agent-to-tool protocol Agent coordination | A2A (a2a-sdk 0.3.25) | Cross-framework agent-to-agent protocol



](https://github.com/trieu/sample-multi-agent-ai-system#1)[

jiisonline.org

4. Context Manager: Manages the state and context of the agent, including session management, state tracking, and memory managem...

As shown in Figure 4, using the LangChain MCP adapter library makes it possible to connect to multiple MCP servers and load tools from those servers (Langchain ... LangGraph can be used to implement agents compliant with the A2A protocol and integrate tools such as currency exchange rate lookup tools via MCP.



](https://jiisonline.org/files/DLA/20250930204204_08.pdf?PHPSESSID=7f4625826f4b54abffb1f306ed5ace39#4#3)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/01/18

a2a-openai-agent/mcp_a2a_master/README.md at main · MuhammadAbdullah95/a2a-openai-agent - Skip to content

An advanced multi-agent system combining MCP (Model Context Protocol) and A2A (Agent-to-Agent Protocol) with three different agent frameworks: OpenAI Agents SDK, Google ADK, and LangGraph. ... │ │ ├── agent_executor.py # A2A executor bridge



](https://github.com/MuhammadAbdullah95/a2a-openai-agent/blob/main/mcp_a2a_master/README.md#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/04/12

MCP-MultiServer-Interoperable-Agent2Agent-LangGraph-AI-System/main.py at main · junfanz1/MCP-MultiServer-Interoperable-Agent2Agent-LangGraph-AI-System · GitHub - import asyncio

from mcp import ClientSession ... So we can use in LangChain or LangGraph agent. ... Motivation of combining LangGraph, LangChain and MCP: LangGraph agent, with help of MCP client, is making request to MCP server, and execution of tool is in server side, which is decoupled from LangGraph application.



](https://github.com/junfanz1/MCP-MultiServer-Interoperable-Agent2Agent-LangGraph-AI-System/blob/main/main.py#1)[

Neuralingual MCP - AI-Powered Affirmation Practice Tool - MCP Service

2025/12/03

MCP多代理客户服务平台 - 高效自动化服务解决方案-MCP服务

一个基于Model Context Protocol（MCP）和多个专用A2A代理的多代理客户服务平台，支持JSON-RPC通信和LangGraph编排 ... ✔ 多个专用A2A代理（路由器、数据、支持、计费） ... ✔ 基于LangGraph的多步骤工作流编排



](https://www.mcpworld.com/zh/detail/47758e58db93b1c4df09d12e71a8dd85)[

![](https://cdn.deepseek.com/site-icons/freecodecamp.org)

freeCodeCamp

2026/04/29

How to Build a Multi-Agent AI System with LangGraph, MCP, and A2A [Full Book]

Building a single AI agent that answers questions or runs searches is a solved problem. A handful of tutorials and a few hours of work will get you there. What most tutorials skip is the engineering



](https://www.freecodecamp.org/news/how-to-build-a-multi-agent-ai-system-with-langgraph-mcp-and-a2a-full-book/#9)[

pretalx.com

PyCon 2026

Build Agentic Systems With Python, LangGraph, MCP, and A2A But the problems are... ...static data will not suffice ...AI tooling landscape evolves rapidly ...flexibility is needed # We drive



](https://pretalx.com/media/pyconde-pydata-2026/submissions/JBFGCA/resources/260415_GTL3Ozf.pdf#1#1)[

Model Context Protocol

2026/03/28

claude-tempo MCP Server — Setup, Tools & FAQ - claude-tempo

Multiple Claude Code sessions discover each other, exchange messages in real time, and coordinate work — across machines, not just localhost. ... Players discover each other withensemble, send messages with cue, and coordinate via a conductor that connects to external interfaces like Discord, Telegram, or the built-in TUI.



](https://model-context-protocol.com/servers/claude-tempo#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/03/26

GitHub - temporal-community/temporal-ai-agent: This demo shows a multi-turn conversation with an AI agent running inside a Temporal workflow. · GitHub

This demo shows a multi-turn conversation with an AI agent running inside a Temporal workflow. · GitHub ... The purpose of the agent is to collect information towards a goal, running tools along the way. The agent supports both native tools and Model Context Protocol (MCP) tools, allowing it to interact with external services. ... This agent acts as an **MCP



](https://github.com/temporal-community/temporal-ai-agent#1)[

GitHub

Temporal Cortex is open scheduling infrastructure that lets any AI agent schedule reliably — whether the other person has an AI agent or not ... Accessible via MCP, A2A, REST, and browser. Powered by [Truth Engine](https ... 4 protocols (MCP, A2A, REST, Browser), atomic booking with Two-Phase Commit, and deterministic temporal computation powered by [Truth Engine](https...



](https://raw.githubusercontent.com/temporal-cortex/mcp/refs/heads/main/README.md#2)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal

2025/07/08

Durable MCP: Using Temporal to give agentic systems superpowers

I’ll also talk about how making MCP durable with Temporal enables durable tool execution, opening up possibilities for tools and enabling people to build agentic tools that are durable ... At Temporal ... Here’s an example of a tool that executes a Temporal Workflow and returns the result...



](https://temporal.io/blog/durable-mcp-how-to-give-agentic-systems-superpowers)[

temporal.org.cn

2025/07/08

持久 MCP：如何赋予智能体系统超能力

我还会谈谈如何使用 Temporal 使 MCP 持久化，从而实现持久的工具执行，为工具打开可能性，并使人们能够构建持久、可扩展且企业级的代理工具 ... MCP 工具作为工作流 ... 可以快速地为 MCP 工具添加许多理想的架构质量：将 MCP 工具实现为工作流。



](https://temporal.org.cn/blog/durable-mcp-how-to-give-agentic-systems-superpowers)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/04/22

ai-agents-workshop-python/demo5-multi-agent/README.md at main · temporal-community/ai-agents-workshop-python - Skip to content

Three OpenAI Agents SDK agents wired together through Temporal ... All three Workers run in a single Python process viaasyncio.gather(...). They poll three distinct task queues, so the routing in the Temporal UI is explicit. ... each specialist is a real Temporal workflow execution, not an inline function. ... Each specialist has its own internal toolkit (weather APIs / F1 MCP).



](https://github.com/temporal-community/ai-agents-workshop-python/blob/main/demo5-multi-agent/README.md#1)[

![](https://cdn.deepseek.com/site-icons/socket.dev)

Socket

2024/12/23

silsila - PyPI Package Security Analysis - Socket - silsila

Agent framework for Model Context Protocol (MCP) built on temporal ... silsila (mcp-agent) An agent framework built on MCP and Temporal for distributed AI applications ## Introduction This framework aims ... complex AI workflows that rely on MCP (Model Context Protocol) servers for ... By defining an OrchestratorInterface, the same workflows can ... or production mode (as Temporal workflows).



](https://socket.dev/pypi/package/silsila/overview/0.0.1/tar-gz#1)[

temporal.org.cn

2025/06/10

从AI炒作到持久现实——为什么代理流程需要分布式系统纪律

将这些工具封装在Temporal Workflows中，并将HTTP调用变成Temporal Activity。我意识到MCP使LLM能够与外部或内部服务和API无缝交互，而Temporal则通过强大的持久执行来巩固这些交互。 共同的“持久工具”将AI从被动响应者转变为具有弹性的、采取行动的代理 ... 它的工作流引擎处理状态、重试、超时、反压和事件回放，而其内置的追踪和指标 ... 分布式系统纪律的情况下交付代理流程。



](https://temporal.org.cn/blog/from-ai-hype-to-durable-reality-why-agentic-flows-need-distributed-systems)[

temporal.org.cn

使用 Temporal 编排环境智能体

我使用 Temporal 进行编排，并使用 模型上下文协议 (MCP) 进行工具接口，围绕三个核心智能体设计了一个系统：一个 经纪智能体（用户面向的入口点 ... 计划 (Schedules)、信号和查询 (Signals & Queries)、Temporal 的 UI、工作流编排 (workflow orchestration) 和 Temporal 原语作为 MCP 工具 (Temporal primitives as MCP tools) ... 执行智能体工作流侦听来自计划的“推动”信号...



](https://temporal.org.cn/blog/orchestrating-ambient-agents-with-temporal)[

LLasermagic El Cuervo

2026/06/12

Convergencia de protocolos de agente hacia 2030

mTLS y confianza bilateral en federación (`oauth-autenticacion-servidores-mcp-agentes`, `confianza-bilateral-mcp-federacion-ia`) se unifican en identidad de agente portable: el mismo subject que invoca MCP puede firmar tareas A2A.



](https://entia.systems/knowledge/es/ia-y-protocolos/convergencia-protocolos-agente-2030-mcp-a2a-ia/)[

![](https://cdn.deepseek.com/site-icons/ietf.org)

IETF Datatracker

2026/06/27

AGTP Composition Profiles: Agent Group Messaging Protocols, External Identity Providers, and HTTP Gateways - The gateway translates this to:¶

an agent serving MCP and A2A workflows on the same session ... Agent Discovery Across AGMPs An agent registered with an AGTP governance platform is discoverable regardless of which AGMP it uses. ... AGMP-specific capability formats (A2A Agent Cards, MCP capability lists) MAY



](https://datatracker.ietf.org/doc/html/draft-hood-agtp-composition-01#3)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/09/20

CNCF Evaluates MCP as the Cloud-Native Agent Wire Spec—And the Standardization Arc Just Reached Infrastructure - Advertisement

and Google's A2A as the agent-to-agent protocol ... Protocol interoperability asks whether the community can converge on MCP and what authentication, discovery, and streaming extensions are required for cluster and multi-cluster use. ... traditional REST-centric proxies cannot handle MCP and A2A session fan-out, bidirectional SSE, protocol negotiation, or per-agent tenancy.



](https://tech.yahoo.com/ai/meta-ai/articles/cncf-evaluates-mcp-cloud-native-142016206.html#1)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

docs.aws.amazon.com

InvokeAgentRuntime pois os servidores MCP passarão por solicitações para esse caminho

• Protocolo ... • Porta ... Requisitos do servidor A2A ... o A2A fornece descoberta de agentes integrada por meio de cartões de agente em /.well-known/agent-card.json ... - Autenticação: suporta os esquemas de autenticação SigV4 e OAuth 2.0



](https://docs.aws.amazon.com/pt_br/marketplace/latest/userguide/aws-marketplace-ug.pdf#complete-bank-verification#138#88#146#96)[

![](https://cdn.deepseek.com/site-icons/ietf.org)

IETF Datatracker

2026/08/05

OpenA2A Agent Identity Protocol (AIP) - Level 1 implementations MUST maintain a local append-only audit log at "~/

Discovery An OpenA2A AIP identity provider MUST serve a discovery document at the well-known URI "/.well-known/aip". The document advertises the provider DID, the protocol version ... "supportedProtocols": ["mcp", "a2a"]



](https://datatracker.ietf.org/doc/html/draft-fane-opena2a-aip-02#3)[

![](https://cdn.deepseek.com/site-icons/pypi.org)

PyPI

2026/04/25

dns-aid - natively supports custom SVCB params — all other backends use the safe TXT demotion default

natively supports custom SVCB params — all other backends use the safe TXT demotion default. This allows any DNS client to discover agents without proprietary protocols or central registries. ### Dis



](https://pypi.org/project/dns-aid/0.18.2/#2)[

![](https://cdn.deepseek.com/site-icons/hku.hk)

HKU SPACE AI Hub

2025/11/10

Introducing agent-to-agent protocol support in Amazon Bedrock AgentCore Runtime - HKU SPACE AI Hub - Introducing agent-to-agent protocol support in Amazon Bedrock AgentCore Runtime

# Introducing agent-to-agent protocol support in Amazon Bedrock AgentCore Runtime We recently announced the support for Agent-to-Agent (A2A) protocol on Amazon Bedrock AgentCore Runtime. With this ad



](https://aihub.hkuspace.hku.hk/2025/11/12/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/#1)[

![](https://cdn.deepseek.com/site-icons/pypi.org)

PyPI

2026/03/23

agent-identity-bridge - Agent Identity Bridge (AIB)

# Agent Identity Bridge (AIB) One identity. Every protocol. Full audit trail. AIB is an open-source protocol that gives AI agents a single portable identity across MCP (Anthropic), A2A (Google), ANP



](https://pypi.org/project/agent-identity-bridge/#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/11/24

A2A/docs/specification.md at 18ca2533bf18d0458f65e4c9eaead3e586fce25d · a2aproject/A2A · GitHub - Requests the cancellation of an ongoing task

Errors:** - [`TaskNotCancelableError`](#332-error-handling): The task is not in a cancelable state (e.g. ... - [`TaskNotFoundError`](#332-error-handling): The task ID does not exist or is not accessible. ... The operation is attempted ... (`completed`, `failed`, `cancelled`, or `rejected`).



](https://github.com/a2aproject/A2A/blob/18ca2533bf18d0458f65e4c9eaead3e586fce25d/docs/specification.md?plain=1#L1029C1-L1034C1#2)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/02/18

Issue · a2aproject/A2A

assuming the happy path the stream should only ... state like "COMPLETED" / "INPUT_REQUIRED" etc. If the last state the client has seen was not one of these states, then you know that the Task was not completed and you can restart the stream. ... If the Task has COMPLETED etc in-between the stream shutting down and restarting then the stream will terminate gracefully straight after the first message.



](https://github.com/a2aproject/A2A/issues/1503)[

adcontextprotocol.org

2026/05/18

Protocol Comparison - AdCP - Ad Context Protocol

"status": "input-required" ... | Provide webhook or poll less frequently failed | Error occurred | Show error, handle gracefully auth-required | Need auth | Prompt for credentials ... Both protocols handle async operations with the same status progression:submitted → working → completed/failed



](https://docs.adcontextprotocol.org/dist/docs/2.5.3/protocols/protocol-comparison#push-notification-architecture)[

release-assets.githubusercontent.com

Real agent work takes minutes to hours: CI runs, deep- research synthesis, batch exports

work.- Poll tasks/status and fetch tasks/result correctly. ... 2. Mark any working tasks whose process died as failed with error CRASH_RECOVERY. 3. Preserve completed ... worker checks and exits early.- State reload on "crash" marks the in-flight task as failed with CRASH_RECOVERY.



](https://release-assets.githubusercontent.com/github-production-release-asset/1185590488/fb5c2119-7fe9-4995-bb1d-a1ebb5fcec44?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-08-05T21%3A33%3A29Z&rscd=attachment%3B+filename%3Daiefs-vol5-agents.pdf&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-08-05T20%3A33%3A22Z&ske=2026-08-05T21%3A33%3A29Z&sks=b&skv=2018-11-09&sig=ZyVaaEn%2FySi%2FZOTFEmbyB%2F84DAXzei%2FmLm0BUMgg29U%3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc4NTk2MzgwNywibmJmIjoxNzg1OTYzNTA3LCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.ScxMjUTH81vXVCrpAIilgo3If9xs7LQ5hClGena02pU&response-content-disposition=attachment%3B%20filename%3Daiefs-vol5-agents.pdf&response-content-type=application%2Foctet-stream#92#28)[

adcontextprotocol.org

2026/09/08

Error Handling - AdCP - Ad Context Protocol

This document outlines AdCP’s approach to error handling across MCP and A2A protocols, providing consistent patterns for both fatal errors and non-fatal warnings. ... For fatal errors that prevent task completion, MCP uses the isError: true pattern: When to use MCP fatal errors ... A2A (Agent-to-Agent Protocol) For fatal errors, A2A uses the status: "failed" pattern...



](https://docs.adcontextprotocol.org/dist/docs/2.5.3/protocols/error-handling)[

![](https://cdn.deepseek.com/site-icons/pub.dev)

Dart packages

messageStream method - messageStream method

Sends a message to the agent and subscribes to real-time updates viamessage/stream. ... Returns a Stream ofEvent objects. The stream will emit an A2AException if the server sends a JSON-RPC error within the event stream.



](https://pub.dev/documentation/genui_a2a/0.10.1/genui_a2a/A2AClient/messageStream.html#1)[

Corti.ai

2026/08/05

Task lifecycle - Corti API Documentation

TASK_STATE_FAILED | The task failed; check the status message for error details ... TASK_STATE_REJECTED | The task was rejected before processing (insufficient credits or invalid agent configuration) ... - TASK_STATE_SUBMITTED to TASK_STATE_REJECTED: The task was rejected before processing (insufficient credits or invalid configuration).



](https://docs.corti.ai/agentic/task-lifecycle)[

adcontextprotocol.org

AdCP — Protocol Comparison

"status": "input-required" ... failed | Error occurred | Show error ... "context_id": "ctx-123" ... "suggestions": ["budget" ... submitted → working → completed/failed ... MCP Tasks and A2A ... deliver an AdCP payload, but they are not ... Error Handling Both use status: "failed" with same error structure...



](https://docs.adcontextprotocol.org/dist/docs/3.1.2/building/concepts/protocol-comparison)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/03/24

A2A/docs/specification.md at be6ad4b079d25e8595abd216b039bd8026ccad0f · a2aproject/A2A - - Use theexistingTaskId from the error data (if provided) to call tasks/get

Use theexistingTaskId from the error data (if provided) to call tasks/get. ... Just like message/send, a task which has reached a terminal state (completed, canceled, rejected, or failed) can't be restarted. Sending a message to such a task will result in an error.



](https://github.com/a2aproject/A2A/blob/be6ad4b079d25e8595abd216b039bd8026ccad0f/docs/specification.md#3)[

MatrixOne 中文文档

2026/08/13

Agent 任务¶

任务表示一次可持续运行、可观察的 Agent 执行。发送消息后，调用方应保存 Taskid 和 contextId，并根据 status.state 驱动界面与后续操作，而不是把 HTTP 请求结束视为任务结束。 ## Task 结构¶ Task 的字段会随 Agent 和 A2A 协议版本扩展。客户端通常需要关注： { "kind": "task", "id": "task_123"



](https://docs.matrixorigin.cn/moi/zh/5.0/developer/sdk/agents/tasks.html)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arXiv

A Survey of AI Agent Registry Solutions - A Survey of AI Agent Registry Solutions

MCP uses a centralized metaregistry with GitHub-authenticated publishing and structured metadata for server discovery. A2A enables decentralized interaction via JSON-based Agent Cards, discoverable through well-known URIs, curated catalogs, or direct configuration. NANDA Index introduces AgentFacts ... A2A Agent Cards [2]



](https://ar5iv.labs.arxiv.org/html/2508.03095#1)[

Neuralingual MCP - AI-Powered Affirmation Practice Tool - MCP Service

2025/10/29

MCP Agent Registry - Dynamic A2A Interaction Solution - MCP Service

Leveraging Model Context Protocol (MCP) as a standardized mechanism for discovering and retrieving Google A2A Agent Cards, enabling dynamic agent interaction. ... Leveraging Model Context Protocol (MCP) as a standardized mechanism for discovering and retrieving Google A2A Agent Cards, enabling dynamic agent interaction using A2A.



](https://www.mcpworld.com/en/detail/17d10af304ecec8b947878f0902ac215)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/02/14

feat: add A2A v0.3 agent card for agent-to-agent discoverability by clouatre · Pull Request #165 · clouatre-labs/math-mcp-learning-server - Skip to content

Adds a/.well-known/agent-card.json endpoint following the A2A (Agent-to-Agent) v0.3 specification, enabling other agents to discover and understand this server's capabilities. ... AgentInterface, AgentProvider)



](https://github.com/clouatre-labs/math-mcp-learning-server/pull/165#1)[

Neuralingual MCP - AI-Powered Affirmation Practice Tool - MCP Service

2026/04/03

MCP-A2A Protocol Bridge for AI Agent Communication - MCP Service

The A2A Protocol MCP Server bridges MCP (Model Context Protocol) and Google's Agent2Agent (A2A) Protocol, enabling agent discovery, task delegation, and inter-agent communication. ... Bridge between MCP (Model Context Protocol) and Google’s ... (A2A) Protocol — enabling agent discovery, task delegation, and inter-agent communication.



](https://www.mcpworld.com/en/detail/1f565912559b42a37d867115f64a413e)[

Neuralingual MCP - AI-Powered Affirmation Practice Tool - MCP Service

2025/10/29

MCP代理注册表 - 动态A2A交互解决方案-MCP服务

利用模型上下文协议（MCP）作为标准化机制，发现和检索Google A2A代理卡，实现代理间的动态交互 ... 利用模型上下文协议（MCP）作为发现和检索Google A2A代理卡的标准化机制，使用A2A实现动态代理交互 ... 利用模型上下文协议（MCP）作为发现和检索Google A2A代理卡的标准化机制。



](https://www.mcpworld.com/zh/detail/17d10af304ecec8b947878f0902ac215)[

![](https://cdn.deepseek.com/site-icons/ietf.org)

IETF Datatracker

2026/05/07

Agent Directory - [RFC6763] Cheshire, S

A2A [A2A] serves an Agent Card at /.well-known/agent-card.json; MCP [MCP] exchanges server metadata during initialization. Both describe ... (MCP, A2A, gRPC, and others are all describable) and is specified here as an open



](https://datatracker.ietf.org/doc/draft-jimenez-agent-directory/01/#4)[

![](https://cdn.deepseek.com/site-icons/socket.dev)

Socket

2026/03/19

@aiagentkarl/a2a-protocol-mcp-server - npm Package Security ... - New:Microsoft Teams Notifications Are Now Available in Socket

MCP server implementing the Google Agent2Agent (A2A) Protocol for AI agent discovery and task delegation. ... This server provides a local A2A-compatible directory where agents can register, discover each other by capability, and delegate tasks. ... - Discover agents by searching for specific capabilities ... - Agent cards follow the A2A protocol format for interoperability



](https://socket.dev/npm/package/%40aiagentkarl%2Fa2a-protocol-mcp-server#1)[

![](https://cdn.deepseek.com/site-icons/npmjs.com)

NPM

2026/03/19

@aiagentkarl/a2a-protocol-mcp-server

0.1.0 • Public • Published # A2A Protocol MCP Server MCP server implementing the Google Agent2Agent (A2A) Protocol for AI agent discovery and task delegation. The A2A protocol enables AI agents to



](https://www.npmjs.com/package/%40aiagentkarl/a2a-protocol-mcp-server)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/04/12

Suggestion: add Agent Card MCP resource generation capabilities to MCPAdapt · Issue #134 · a2aproject/A2A - Skip to content

Skip to content ## Navigation Menu {{ message }} # Suggestion: add Agent Card MCP resource generation capabilities to MCPAdapt #134 ## Description From my current understanding of https://google.



](https://github.com/a2aproject/A2A/issues/134#1)[

![](https://cdn.deepseek.com/site-icons/ietf.org)

datatracker.ietf.org

OAuth 2.0 Scope Aggregation for Multi-Step AI Agent Workflows

call third-party tools (e.g., via MCP)- delegate sub-tasks to other AI agents (e.g., via A2A) - These interoperations typically require authorization, by OAuth 2.0 ... The AI agent initiates a single OAuth flow for the aggregated scopes



](https://datatracker.ietf.org/meeting/125/materials/slides-125-hackathon-sessd-oauth-20-scope-aggregation-for-multi-step-ai-agent-workflows-01?__cf_chl_tk=Ch6yf26VHSRQ4qrOJZA6C4bF0Myb3B8tElzrbO2M0MU-1774475969-1.0.1.1-zbS1hCTGHufg74_8gfS0_KrfQXDW3GLiwCccQWnYZdo#1#1)[

![](https://cdn.deepseek.com/site-icons/mulesoft.com)

MuleSoft Blog

2026/01/29

Trusted Agent Identity: Delegated Access Control for MuleSoft Agent Fabric | MuleSoft Blog - 6668.75

and unify user-centric trust across web protocols and integration patterns – from A2A (Agent-to-Agent) to MCP (Model Context Protocol) and more generally beyond – to any APIs managed through Flex Gateways. ... OBO flows are essential for secure A2A and MCP interactions where downstream systems must trust not only that a request came from a service...



](https://blogs.mulesoft.com/news/delegated-access-control-mulesoft-agent-fabric/#1)[

![](https://cdn.deepseek.com/site-icons/ietf.org)

IETF Datatracker

2026/06/27

AGTP Composition Profiles: Agent Group Messaging Protocols, External Identity Providers, and HTTP Gateways - agent semantics

1. *AGMP composition profiles* for MCP [MCP], A2A [A2A], and ACP ... AGTP does not understand MCP, A2A, OAuth bearer tokens, or HTTP semantics; it ... MCP / A2A / ACP / ANP [messaging] |



](https://datatracker.ietf.org/doc/draft-hood-agtp-composition/#2)[

![](https://cdn.deepseek.com/site-icons/logto.io)

Logto blog

2025/05/21

在代理应用中的身份认证变化与不变之处

MCP 和 A2A ... MCP 授权服务器 必须 实现 OAuth 2.1，并为机密和公共客户端采取适当的安全措施。 A2A 客户端负责通过 A2A 协议外部的流程获取所需的凭证材料（例如，OAuth 2.0 令牌、API 密钥、JWT）。



](https://blog.logto.io/zh-CN/auth-identity-agentic#%e4%bd%a0%e4%bb%8d%e7%84%b6%e9%9c%80%e8%a6%81%e5%ae%9a%e4%b9%89%e4%ba%a7%e5%93%81%e7%9a%84%e6%9e%b6%e6%9e%84)[

Agentic AI Foundation (AAIF)

2026/08/04

Exposing OpenAPI Operations as Authorized MCP Tools with agentgateway - Agentic AI Foundation (AAIF)

Specifically, it can function as an MCP Gateway, an A2A (Agent-to-Agent) Gateway, and an LLM Gateway. When used as an MCP gateway ... We will then use the OAuth 2.1 Authorization Code Grant to obtain an access token, which is used to execute tools/call.



](https://aaif.io/blog/exposing-openapi-operations-as-authorized-mcp-tools-with-agentgateway-and-keycloak)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/05/10

GitHub - JCOMAIA/Aira: A2A Network, Host, Register, Discover Agents in the Network, Share, Use tools. Server is Hosted on AiraHub.py · GitHub - GitHub - JCOMAIA/Aira: A2A Network, Host, Register, Discover Agents in the Network, Share, Use tools. Server is Hosted on AiraH...

AIRA Hub is a FastAPI-based platform for managing MCP (Model Context Protocol) tools and A2A (Agent-to-Agent) skills with OAuth 2.1 authentication. This document provides setup instructions, usage examples, and API reference for the system. ... 2. Authentication ... API Reference



](https://github.com/JCOMAIA/Aira#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/04/07

GitHub - curityio/azd-ai-autonomous-agent: Azure AI integration of customer users with C# applications and enterprise data, using OAuth 2.0 token intelligence · GitHub - GitHub - curityio/azd-ai-autonomous-agent: Azure AI integration of customer users with C# applications and enterprise data, usin...

C# A2A server and MCP server code to use OAuth 2.0 to validate and exchange access tokens. * Configuration and deployment of identity systems and API gateways. ... * An MCP server uses optimal access tokens and claims-based authorization to protect enterprise resources.



](https://github.com/curityio/azd-ai-autonomous-agent#1)[

Authlete

2025/11/26

「OpenID BizDay #18 ~ AIdentity × Security CollabDay」に登壇します

Authlete を活用した MCP OAuth 2.0 認可サーバーの実装をご紹介します ... world」と題したホワイトペーパーを解説するとともに、MCP サーバーにおける認可・認証機能の実装や A2A セキュリティなどについて、それぞれの分野の専門家が知見を共有します。



](https://www.authlete.com/ja/news-jp/openid-bizday-presentation)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/10/23

a2a-agent-framework/README.md at main · jh941213/a2a-agent-framework - Skip to content

Microsoft Agent Framework + Google A2A Protocol + OAuth2 Authentication + Role-Based Tool Gateway ... OAuth2 Bearer Token ... - MCP: Tavily (Web Search), Context7 (Documentation) ... Secure user authentication with Bearer tokens ... TAVILY_API_KEY=your-tavily-api-key



](https://github.com/jh941213/a2a-agent-framework/blob/main/README.md#1)[

![](https://cdn.deepseek.com/site-icons/atlassian.com)

Atlassian Developers

2026/08/06

Atlassian Rovo A2A

The Atlassian A2A Gateway uses the OAuth 2.0 authorization code flow for all authenticated requests. ... Unlike the MCP Server, which also supports API tokens, A2A is OAuth-only - there is no API token or session-based fallback.



](https://developer.atlassian.com/cloud/rovo-a2a/authentication/#manual-client-registration-is-not-supported)[

adcontextprotocol.org

2026/09/08

AdCP — Protocol Comparison

Both MCP and A2A provide identical AdCP capabilities using the same unified status system. ... MCP Tasks and A2A task state are transport mechanics that can deliver an AdCP payload, but they are not a replacement for AdCP task polling or reconciliation.



](https://docs.adcontextprotocol.org/dist/docs/3.1.21/building/concepts/protocol-comparison)[

![](https://cdn.deepseek.com/site-icons/google.com)

Como usar o coletor de diagnósticos | Apigee | Google Cloud Documentation

2026/09/13

REST Resource: projects.locations.collections.engines.assistants.agents.a2a.v1.tasks | Agent Search | Google Cloud Documentation

Task is the core unit of action for A2A. ... TASK_STATE_SUBMITTED | Represents the status that acknowledges a task is created TASK_STATE_WORKING | Represents the status that a task is actively being processed TASK_STATE_COMPLETED | Represents the status a task is finished. This is a terminal state



](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.assistants.agents.a2a.v1.tasks)[

![](https://cdn.deepseek.com/site-icons/npmjs.com)

NPM

2025/11/09

a2a-mcp-server

a2a_get_task: Retrieve task status and details by task ID - a2a_cancel_task: Cancel a running task ... Parameters: - agentCardUrl (string, required): URL to the agent's card endpoint ... Retrieve the status and details of a task.



](https://www.npmjs.com/package/a2a-mcp-server)[

![](https://cdn.deepseek.com/site-icons/google.com)

Como usar o coletor de diagnósticos | Apigee | Google Cloud Documentation

2026/06/30

REST Resource: tasks | CX Agent Studio | Google Cloud Documentation

Task is the core unit of action for A2A. It has a current status and when results are created for the task they are stored in the artifact. ... TaskStatus ... TASK_STATE_SUBMITTED ... TASK_STATE_WORKING | Indicates that a task is actively being processed by the agent. TASK_STATE_COMPLETED | Indicates that a task has finished successfully. This is a terminal state. TASK_STATE_FAILED ... finished with an error.



](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/03/24

A2A/docs/specification.md at 4ba9e4c5a77bfb03589fe2bb987f09d3515ceb46 · a2aproject/A2A - artifactsArtifact[] | No | Array of outputs generated by the agent for this task

6.2.TaskStatus Object ... 6.3.TaskState Enum ... | No working | Task is actively being processed by the agent. ... The task is effectively paused. | No (Pause) completed | Task finished successfully. ... | Yes failed | Task terminated due to an error during processing. TaskStatus.message may contain error details. | Yes rejected | Task terminated due to rejection by remote agent.



](https://github.com/a2aproject/A2A/blob/4ba9e4c5a77bfb03589fe2bb987f09d3515ceb46/docs/specification.md#2)[

![](https://cdn.deepseek.com/site-icons/w3.org)

lists.w3.org

MCP Core Concepts

Task States Created: Task has been created but not yet started- Working: Task is in progress- Waiting: Task is waiting for external input or resources- Completed: Task has been successfully completed- Failed: Task execution failed ... A2A vs MCP...



](https://lists.w3.org/Archives/Public/public-agentprotocol/2025Aug/att-0012/Agent_Protocol_Comparison_MCP__A2A__and_ANP.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/03/24

A2A/docs/specification.md at fbdd5a6a3adcd0ca0decaef6a1f13aaa8e512beb · a2aproject/A2A - metadata | Record<string, any> | No | Arbitrary key-value metadata associated with the task

6.2.TaskStatus Object ... 6.3.TaskState Enum ... | No working | Task is actively being processed by the agent. ... The task is effectively paused. | No (Pause) completed | Task finished successfully. ... | Yes failed | Task terminated due to an error during processing. ... | Yes rejected



](https://github.com/a2aproject/A2A/blob/fbdd5a6a3adcd0ca0decaef6a1f13aaa8e512beb/docs/specification.md#2)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/01/18

[Feat]: Add `Task` progress · Issue #1387 · a2aproject/A2A - Skip to content

Skip to content ## Navigation Menu {{ message }} # [Feat]: AddTask progress #1387 ## Description Contributor ### Is your feature request related to a problem? Please describe. Right now there's



](https://github.com/a2aproject/A2A/issues/1387#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/03/24

A2A/docs/specification.md at 92fd188e93c18033abd67dcc5950389b9caa4f69 · a2aproject/A2A - historyMessage[] | No | Optional array of recent messages exchanged, if requested by historyLength

historyMessage[] | No | Optional array of recent messages exchanged, if requested by historyLength. metadata | Record<string, any> | No | Arbitrary key-value metadata associated with the task. kind



](https://github.com/a2aproject/A2A/blob/92fd188e93c18033abd67dcc5950389b9caa4f69/docs/specification.md#2)[

![](https://cdn.deepseek.com/site-icons/ietf.org)

IETF Datatracker

2026/07/06

An Overview of Messaging Systems and Their Applicability to Agentic AI - Compliance and Auditing: AI systems in regulated industries require comprehensive audit trails and compliance capabilities

A2A [A2A], the Model Context Protocol (MCP) [MCP] ... [ACP] all expose synchronous request/response semantics ... MCP is designed for synchronous tool calls with optional server-side streaming for partial results.¶ ... server streaming, client streaming, and bidirectional streaming are all supported, enabling direct mapping of A2A...



](https://datatracker.ietf.org/doc/html/draft-mpsb-agntcy-messaging#2)[

![](https://cdn.deepseek.com/site-icons/pub.dev)

Dart packages

2025/12/22

a2a_mcp_bridge | Dart package - a2a_mcp_bridge 1.1.0 a2a_mcp_bridge: ^1.1.0 copied to clipboard

An MCP server that bridges the Model Context Protocol (MCP) with the Agent-to-Agent (A2A) protocol ... The A2A ... this server allows MCP clients to discover, register, communicate with, and manage ... The A2A MCP Bridge currently supports the streamable-http HTTP transport.



](https://pub.dev/packages/a2a_mcp_bridge#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/04/26

claude-a2a/README.md at main · oriolrius/claude-a2a

The protocol is exposed to each Claude session as MCP tools ... stream events ... Each MCP bridge talks to two A2A endpoints: the peer (forsend, stream, cancel, set_push_config, …) and the local server (for inbox and respond).



](https://github.com/oriolrius/claude-a2a/blob/main/README.md#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/01/12

Claude-Skills/engineering/agent-protocol/references/protocol-selection.md at main · borghei/Claude-Skills

The full feature-by-feature comparison of MCP, A2A, OpenAI Functions, and LangChain Tools. ... Feature | MCP | A2A | OpenAI Functions | LangChain Tools ... Streaming | SSE notifications | SSE streaming | Streaming deltas | Callbacks



](https://github.com/borghei/Claude-Skills/blob/main/engineering/agent-protocol/references/protocol-selection.md)[

adk-rust.com

2026/05/23

A2A Remote Agent MCP Server — ADK-Rust MCP registry

Discover remote agents, send tasks, stream results, and manage push notifications — across any framework that implements the A2A protocol. ... Create or continue a remote A2A task external writesend_task_streaming Start remote task with streaming updates external writeget_task



](https://adk-rust.com/en/resources/mcp/mcp-a2a)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/08/26

GitHub - khalidsaidi/a2abench at producthunt · GitHub - GitHub - khalidsaidi/a2abench at producthunt · GitHub

A2ABench is an agent-native developer Q&A service: a StackOverflow-style API with MCP tooling and A2A runtime endpoints for deep research and citations. ... local (stdio) and remote (streamable HTTP) ... * A2A runtime endpoint at `/api/v1/a2a` (`sendMessage`, `sendStreamingMessage`...



](https://github.com/khalidsaidi/a2abench?ref=producthunt#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/04/15

fix(observability): resolve A2A and plugin post-invoke silent-success traps by bogdanmariusc10 · Pull Request #4238 · IBM/mcp-context-forge - Skip to content

Trap 1 - A2A 200-OK branch ignores JSONRPC error envelopes: The A2A integration path unconditionally setis_error=False and success=True for all 200-OK responses ... a JSONRPC {"error" ... Two pre-existing bugs caused



](https://github.com/IBM/mcp-context-forge/pull/4238#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/04/28

fix(mcp): an empty tools/call is an error, and every refusal names it… · vassiliylakhonin/agenda-intelligence-md@c7598f2 - Skip to content

A2A has three answers — done, broken, and "I need input you have not sent". MCP has two. Its only channel for "fix your call and try again" is isError, so the seven gates that answered TASK_STATE_INPUT_REQUIRED crossed into MCP as isError...



](https://github.com/vassiliylakhonin/agenda-intelligence-md/commit/c7598f228444446db746679465db0b5ecae854f5#1)[

![](https://cdn.deepseek.com/site-icons/microsoft.com)

Learn Microsoft

2026/08/04

Csatlakozás A2A-ügynökvégponthoz az Foundry Agent Service-ből - Microsoft Foundry - Ajánlott: A legtöbb ügynök esetében adja hozzá az A2A eszközt egy eszközkészleten keresztül, és csatolja az eszközkészletet az ü...

A legtöbb ügynök esetében adja hozzá az A2A eszközt egy eszközkészleten keresztül, és csatolja az eszközkészletet az ügynökhöz MCP-eszközként.



](https://learn.microsoft.com/hu-hu/azure/foundry/agents/how-to/tools/agent-to-agent?view=foundry-classic#4)[

![](https://cdn.deepseek.com/site-icons/npmjs.com)

NPM

2026/09/05

a2a-to-mcp - ⚠️

A typed A2A error (codes -32001 to -32009) is also a tool execution error, with the code in structuredContent.a2aErrorCode. The bridge never re-emits an A2A error code as a JSON-RPC code. JSON-RPC reserves



](https://www.npmjs.com/package/a2a-to-mcp#1)[

adcontextprotocol.org

AdCP — Transport Error Mapping

How AdCP structured errors travel over MCP and A2A transports: extraction paths ... This page defines how the error.json schema maps to MCP and A2A response envelopes. ... MCP Binding ### Tool-Level Errors The standard path for all AdCP error codes.



](https://docs.adcontextprotocol.org/docs/building/implementation/transport-errors#security-considerations)[

![](https://cdn.deepseek.com/site-icons/microsoft.com)

Learn Microsoft

2026/07/23

Azure Foundry hostedTools 経由の MCP / A2A 呼び出し失敗について - Microsoft Q&A

お世話になっております。 Azure Foundry の hostedTools 経由で MCP および Agent-to-Agent (A2A) を利用する際に、-32603: Received 500 from a service request が返却され、処理が失敗する事象を確認しております。 一方で、MCP サーバおよび RemoteA2A 自体は単体では正常に動作しており、getWi



](https://learn.microsoft.com/ja-jp/answers/questions/5955908/azure-foundry-hostedtools-mcp-a2a)[

![](https://cdn.deepseek.com/site-icons/aliyun.com)

阿里云开发者社区

2026/08/08

企业多智能体协作的工程边界：MCP 工具接入与 A2A 任务编排实践

2026-08-09 142 举报 简介： 本文探讨多智能体系统可靠协作的关键——通过MCP（代理到能力）规范工具调用，A2A（代理到代理）接口统一任务契约，解决参数混乱、重复执行、状态不可知等工程痛点，推动智能体从Demo走向可运维的生产系统。（239字） 单个大模型应用通常只需要处理一条请求链路：接收输入、调用模型、返回结果。当系统进一步拆分为规划代理、检索代理、执行代理和审核代理时，问



](https://developer.aliyun.com/article/1754370#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/05/07

mcp-context-forge/mcpgateway/main.py at 31557cdc0149ddef8d0afd44d92ba12aa88902e6 · IBM/mcp-context-forge · GitHub - service = A2AAgentService()

service = A2AAgentService() tasks = service.list_tasks(db, agent_id=agent_id, state=state, limit=limit, offset=offset, user_email=user_email, token_teams=token_teams) return OR



](https://github.com/IBM/mcp-context-forge/blob/31557cdc0149ddef8d0afd44d92ba12aa88902e6/mcpgateway/main.py#21)[

![](https://cdn.deepseek.com/site-icons/npmjs.com)

NPM

2026/02/25

a2a-mcp-bridge - ⚠️

Add the bridge as an MCP server with env vars inline: claude mcp add a2a-bridge \ -e A2A_AGENT_URLS=https://your-a2a-server.com \ -e A2A_API_TOKEN=your-token \



](https://www.npmjs.com/package/a2a-mcp-bridge?activeTab=dependencies#1)[

![](https://cdn.deepseek.com/site-icons/npmjs.com)

NPM

2026/08/13

vscode-a2a - ⚠️

vscode-a2a ... An MCP bridge that exposes A2A agents as tools in VS Code agent chat (GitHub Copilot, etc.). ... Example: "vscode-a2a": { "command": "node", "args" ... "stdio", "env": {



](https://www.npmjs.com/package/vscode-a2a?activeTab=readme#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/05/06

A2A-MCP-Bridge/README.md at main · THINKER-ONLY/A2A-MCP-Bridge - Skip to content

A2A-to-MCP Translator (Adapter) 是一个基于 Python 的网关服务 ... - 端到端示例: 包含一个演示脚本 (examples/run_demo.sh)，用于启动模拟 MCP 服务、Adapter 服务和 A2A 客户端，以展示完整流程 ... - 运行一个 A2A 客户端 (examples/A2A/call_adapter.py) 向 Adapter 发送任务。



](https://github.com/THINKER-ONLY/A2A-MCP-Bridge/blob/main/README.md#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Codelabs

2026/03/16

Pierwsze kroki z MCP, ADK i A2A | Google Codelabs - Kod agenta walutowego znajduje się wcurrency_agent/agent

from dotenv import load_dotenv from google.adk.agents import LlmAgent from google.adk.a2a.utils.agent_to_a2a import to_a2a from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams



](https://codelabs.developers.google.com/codelabs/currency-agent?continue=https%3A%2F%2Fcodelabs.developers.google.com%2Fcloudaittt2026%3Fhl%3Dit&hl=pl#0#2)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/10/11

GitHub - MauricioPerera/ARDF-MCP-A2A: Repositorio con el perfil ARDF subagent@v0.1 y un servidor MCP en Node/TypeScript que actúa como puente hacia agentes A2A. · GitHub - "isError": false,

true } ... "id": 5 ... "type" ... * `mcpBridge.tools` declara al menos `subagent_start` (y opcionalmente `subagent_send`, `subagent_cancel`). * `taskResourceTemplate` con el patrón `a2a://task/{taskId}`. ... Ejemplo ilustrativo de un subagente



](https://github.com/MauricioPerera/ARDF-MCP-A2A#2)[

![](https://cdn.deepseek.com/site-icons/socket.dev)

Socket

2025/10/10

mcp-bridge-a2a - npm Package Security Analysis - Socket - - Instala una librería de validación en tu pipeline y falla el build si el manifest no cumple el schema

Ejemplo ilustrativo de un subagente que usa API Key y mTLS para llamadas JSON-RPC: { "type": "subagent", "id": "finanzas-core" ... "a2a": { "agentCardUri" ... "mtls" ... "subagent_start" } ... "a2a://task/{taskId}"...



](https://socket.dev/npm/package/mcp-bridge-a2a#2)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/05/19

GitHub - vishalmysore/mcp-kotlin: MCP Server in Kotlin for integration with Claude and other MCP client. Works with a2a protocol as well · GitHub - GitHub - vishalmysore/mcp-kotlin: MCP Server in Kotlin for integration with Claude and other MCP client. Works with a2a protocol...

A flexible MCP (Model Context Protocol) server implementation in Kotlin that supports both A2A and MCP protocols. ... "routeplanningagent": { ... "/work/a2a-mcp-bridge/target/mcp-connector-full



](https://github.com/vishalmysore/mcp-kotlin#1)
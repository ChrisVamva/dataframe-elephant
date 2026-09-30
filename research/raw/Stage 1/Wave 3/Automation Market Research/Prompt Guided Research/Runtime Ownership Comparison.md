---
modified: 2026-09-29T16:34:12+03:00
---
For your specific workflow—a 30-day human approval gate, retrying failed API calls, and an absolute requirement to never duplicate a payment—**Temporal is the runtime that owns state, retries, timers, and compensation.** LangGraph is an agent framework that can *model* the logic, but it leaves the durable execution guarantees to you or to an orchestration layer like Temporal.

Here is how each runtime handles the four concerns you asked about.

### 📊 Runtime Ownership Comparison

| Concern | **LangGraph** | **Temporal** |
| :--- | :--- | :--- |
| **State** | Owns *graph state* via **checkpointers** (saved per super-step to a backing store). It persists the data, but not the *execution*—a process crash kills the run; you must build the logic to detect failure and re-enter the graph. | Owns *workflow state* as part of its **Durable Execution** model. The entire event history is persisted, so the workflow survives crashes and resumes exactly where it left off without custom recovery code. |
| **Retries** | Provides **node-level retry policies**. However, retries restart the node body, and LangGraph’s own guidance warns that you must make side effects idempotent because a node may be re-executed after a failure. | Owns **automatic Activity retries** with configurable backoff policies. It follows an at-least-once execution model, meaning it will retry until success—which is why you must make Activities idempotent. |
| **Timers** | Can **wait indefinitely** using `interrupt()` with a persisted checkpoint. The graph parks with zero compute, but there is no built-in *durable timer* primitive; you must handle the wake-up signal yourself. | Owns **durable timers**. A timer is a first-class primitive that persists across restarts. You can safely wait for 30 days (or longer) with zero resource consumption, and the timer will fire reliably when the deadline passes. |
| **Compensation** | **Does not provide** a built-in Saga/compensation pattern. You must implement rollback logic manually and ensure every step is idempotent to avoid duplicate effects (like double-charging a card). | Owns **native Saga pattern support**. You register compensation Activities as each step completes; if a later step fails, Temporal automatically executes the compensations in reverse order to undo the transaction. |

### 💳 Applying This to Your Payment Workflow

**30-Day Human Approval**
- **LangGraph** can pause for 30 days by persisting a checkpoint and resuming when you send a `Command`. But you own the infrastructure that tracks pending approvals and re-enters the graph—if that system fails, the approval is lost.
- **Temporal** uses a **durable timer** combined with a **Signal**. The workflow sleeps for up to 30 days with zero compute. When the human approves, a Signal wakes the workflow; if the timer expires first, it can trigger a timeout path. This is a first-class, reliable pattern.

**Retrying Failed API Calls**
- **LangGraph** will retry a node, but because the node body restarts from the top, any non-idempotent API call could be executed twice. You must build your own idempotency layer.
- **Temporal** retries the **Activity** automatically with backoff. The critical safeguard is that Temporal generates a stable **idempotency key** from the Workflow Run ID and Activity ID, which you pass to your payment gateway. Even if the Activity retries, the gateway recognizes the duplicate key and returns the original result instead of charging again.

**Never Duplicating a Payment**
- **LangGraph** gives you no built-in protection. Its documentation explicitly warns that a retry after a partial failure could charge a customer twice, and it relies entirely on you to design idempotent operations.
- **Temporal** provides the infrastructure for idempotency (the stable key mentioned above) and the **Saga pattern** for compensation. If a later step in the payment flow fails, Temporal can automatically trigger a refund Activity to compensate for the charge that already succeeded.

### 💎 Bottom Line

**LangGraph is the agent framework; Temporal is the durable execution runtime.** For a workflow where a lost state, a missed timer, or a duplicate payment is unacceptable, Temporal owns the critical guarantees. You can still write the agent logic in LangGraph and run it on Temporal via the official plugin, which gives you the best of both: LangGraph’s expressive graph model for the agent’s reasoning, and Temporal’s hardened engine for state, retries, timers, and compensation.

[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal

2026/07/15

LangGraph in production: Temporal's LangGraph Plugin adds Durable Execution

LangGraph and Temporal do different jobs. LangGraph is an agent framework: a way to define what your agent does. But LangGraph leaves key production concerns to be solved somewhere else in the stack: recovery ... Temporal is an agent orchestrator, and unlocking reliable capability is its entire job.



](https://temporal.io/blog/temporal-langgraph-plugin-durable-execution?utm_source=distillintelligence.com&utm_medium=referral&utm_campaign=news_directory)[

![](https://cdn.deepseek.com/site-icons/futureagi.com)

Future AGI

2025/10/11

Best AI Agent Orchestration Platforms in 2026: 5 Compared

Temporal | Workflow-first | Full event-history replay | Activity-level, by error class | Workflow.gather equivalent ... LangGraph: Best for code-first agents with explicit control flow ... Worth flagging. ... Production teams typically wrap the graph in a Temporal workflow (or a Prefect flow) for the durability layer.



](https://futureagi.com/blog/best-ai-agent-orchestration-platforms-2026/#common-mistakes-when-picking-an-orchestration-platform)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal

2025/09/28

From prototype to production-ready agentic AI solution: A use case from Grid Dynamics

This case study shares our journey of building a deep research agent using LangGraph, the unexpected challenges we encountered, and why we ultimately migrated to Temporal. ... While our LangGraph agent had to manually fetch its state from a Redis key at the beginning of each step...



](https://temporal.io/blog/prototype-to-prod-ready-agentic-ai-grid-dynamics?ref=dailydev#conclusion)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/03/09

ainativelang/docs/HYBRID_GUIDE.md at 25d157933ffae2956850f96e735b333b9748105f · sbhooley/ainativelang - Skip to content

One-page reference for choosing pure AINL vs LangGraph vs Temporal when integrating external orchestration. ## Quick comparison Pure AINL | LangGraph hybrid | Temporal hybrid ... You keep | Full stack in AINL + CLI/runner/MCP | LLM nodes, checkpoints, cyclic graphs in LangGraph | Retries, timeouts, long-running workflows in Temporal



](https://github.com/sbhooley/ainativelang/blob/25d157933ffae2956850f96e735b333b9748105f/docs/HYBRID_GUIDE.md#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/04/27

ai_evaluation_framework_tool/agent-orchestration/durable-workflows/SKILL.md at main · cmu-lib/ai_evaluation_framework_tool - Skip to content

│ │ └─→ LangGraph checkpointing (built-in) ... │ └─→ Temporal.io ... Temporal.io | Complex, long-running, mission-critical | High | Survives anything LangGraph checkpointing | Agent-specific persistence | Medium | Good (built-in)



](https://github.com/cmu-lib/ai_evaluation_framework_tool/blob/main/agent-orchestration/durable-workflows/SKILL.md#1)[

![](https://cdn.deepseek.com/site-icons/qiniu.com)

七牛云

2026/06/01

LangGraph vs Temporal：企业Agent基建选型与架构实战

如果说 LangGraph 是为AI开发者量身定制的轻量级跑车，那么 Temporal 就是一辆重型装甲车。Temporal 本质上是一个分布式工作流引擎 ... 如果你的应用侧重于对话交互、快速原型验证，且对任务失败有一定容忍度，LangGraph 是首选。



](https://news.qiniu.com/archives/post-1780364077699-0)[

![](https://cdn.deepseek.com/site-icons/morphllm.com)

Morph

2026/03/26

LLM Workflows: Patterns, Tools & Production Architecture (2026) | Morph

Compare LangGraph, Temporal ... Feature | LangGraph | Temporal | Prefect | Airflow ... Error recovery | Basic retries | Automatic replay | Retries + hooks | Retries Observability | LangSmith | Temporal UI | Prefect UI | Airflow UI ... Temporal handles retries, state persistence, and failure recovery. LangGraph handles prompt management, tool calling...



](https://www.morphllm.com/llm-workflows#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/06/10

durable-hitl-agents/HOW_IT_WORKS.md at 5b75f64a52d678270f9e2c0107c524ad58ce7433 · temporal-community/durable-hitl-agents - Skip to content

Pattern B (the agent calls the human) on a LangGraph–only ... The agent loop — observe → reason → act — and ... - Temporal is the durable-execution runtime (the substrate) beneath the frameworks ... frameworks own the loop — ADK, LangGraph; Temporal is the durable-execution runtime (the substrate) beneath them, and the only thing that coordinates across them.



](https://github.com/temporal-community/durable-hitl-agents/blob/5b75f64a52d678270f9e2c0107c524ad58ce7433/HOW_IT_WORKS.md#1)[

![](https://cdn.deepseek.com/site-icons/mintlify.app)

Ctranslate2 integrations - Docs by LangChain

2026/08/04

Runtimes, frameworks, and harnesses - Docs by LangChain

LangGraph - Temporal - Inngest - LangChain ... While LangChain is built on top of LangGraph, you don’t need to know LangGraph to use LangChain. ... When to use LangGraph Use LangGraph when: - You need fine-grained, low-level control over agent orchestration. - You need durable execution for long-running...



](https://langchain-5e9cc07a.mintlify.app/oss/python/concepts/products)[

GitHub

Hybrid deployments: decision guide

One-page reference for choosing **pure AINL** vs **LangGraph** vs **Temporal** when integrating external orchestration. ## Quick comparison | | **Pure AINL** | **LangGraph hybrid** | **Temporal hybr



](https://raw.githubusercontent.com/sbhooley/ainativelang/refs/heads/main/docs/HYBRID_GUIDE.md#1)[

![](https://cdn.deepseek.com/site-icons/langchain.com)

LangChain

2026/09/22

Checkpointers - Docs by LangChain

LangGraph checkpointers save graph state as checkpoints at each step, enabling persistence, human-in-the-loop, and fault-tolerant execution. ... if another node in the same super-step fails, the successful nodes’ writes are already durable and don’t need to be re-run on resume.



](https://docs.langchain.com/oss/javascript/langgraph/checkpointers)[

![](https://cdn.deepseek.com/site-icons/microsoft.com)

Learn Microsoft

2026/05/05

Use LangGraph with Azure DocumentDB - Azure DocumentDB - Bis op den Haaptinhalt iwwersprangen Sprangt op d’Ask Learn-Chat-Experienz

Three properties make LangGraph well-suited to production agents: - Explicit, durable state. State is checkpointed to a backing store (Azure DocumentDB, in this guide) after every step, so an agent can pause, resume, branch, or roll back to any earlier point.



](https://learn.microsoft.com/lb-lu/azure/documentdb/persist-agent-state?tabs=python#1)[

LLMs.txt Integration - Docus

2026/03/03

Persistence - LangGraph

Persistence Persist and resume graph execution with checkpointers Persistence allows LangGraph applications to save state and resume from any point, enabling durable execution and human-in-the-loop workflows. ... Checkpointers save graph state at each step, creating a complete execution history.



](https://mintlify.wiki/langchain-ai/langgraph/guides/persistence)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/01/15

docs/src/oss/langgraph/durable-execution.mdx at 933a2f9217f6293a54fa59d40ce69b619aaa1172 · langchain-ai/docs · GitHub - ---

Durable execution ... or workflow saves its progress at key points, allowing it to pause and later resume exactly where it left off. ... LangGraph's built-in [persistence](/oss/langgraph/persistence) layer provides durable execution for workflows, ensuring that the state of each execution step is saved to a durable store. ... LangGraph supports three durability modes



](https://github.com/langchain-ai/docs/blob/933a2f92/src/oss/langgraph/durable-execution.mdx?plain=1#1)[

GitHub

2026/06/09

type: design-spec

Durable Execution — crash-resume + durable HITL (v0.12.0 track 1) ... ** 2026 table stakes — LangGraph checkpoints, Pydantic-AI+Temporal, OpenAI Agents SDK, Vercel Workflow DevKit all ship it ... **Gap:** persistence of live run state + a way to reconstruct a running kernel from it.



](https://raw.githubusercontent.com/tylerjrbuell/reactive-agents-ts/refs/heads/main/wiki/Architecture/Design-Specs/2026-06-10-durable-execution.md#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/04/13

langgraph_docs/durable-execution.mdx at main · keithrich98/langgraph_docs - Skip to content

Durable execution ... LangGraph's built-in persistence layer provides durable execution for workflows, ensuring that the state of each execution step is saved to a durable store. ... Enable persistence in your workflow by specifying a checkpointer that will save workflow progress. ... LangGraph supports three durability modes



](https://github.com/keithrich98/langgraph_docs/blob/main/durable-execution.mdx?utm_source=chatgpt.com#1)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

Amazon.com

2026/01/22

LangGraph と Amazon DynamoDB で耐久性のある AI エージェントを構築する | Amazon Web Services - Amazon Web Services ブログ

グラフが実行されると、その状態はスレッドに永続化されます ... - 永続性 (Persistence): 永続性は、チェックポインタの実装を使用して、チェックポイントがどこにどのように保存されるか (メモリ内、データベース、外部ストレージなど) を決定します。チェックポインタは各スーパーステップでスレッドの状態を保存し...



](https://aws.amazon.com/jp/blogs/news/uild-durable-ai-agents-with-langgraph-and-amazon-dynamodb/#1)[

![](https://cdn.deepseek.com/site-icons/langchain.com)

LangChain

2026/09/02

Interrupts - Docs by LangChain

When an interrupt is triggered, LangGraph saves the graph state using its persistence layer and waits indefinitely until you resume execution. Interrupts work by calling the ... - A checkpointer to persist the graph state (use a durable checkpointer in production) ... - State is saved using the checkpointer so execution can be resumed later, In production, this should be a persistent checkpointer (e.g.



](https://docs.langchain.com/oss/python/langgraph/interrupts?trk=article-ssr-frontend-pulse_little-text-block)[

![](https://cdn.deepseek.com/site-icons/pypi.org)

PyPI

2025/03/02

langgraph-checkpoint-aws - LangGraph Checkpoint AWS

Checkpoint AWS A custom AWS-based persistence solution for LangGraph agents that provides multiple storage backends including Bedrock AgentCore Memory, DynamoDB with S3 offloading ... This package provides multiple persistence solutions for LangGraph agents ... - Resumable agent sessions - Efficient state persistence and retrieval ... Initialize checkpointer for state persistence.



](https://pypi.org/project/langgraph-checkpoint-aws/1.2.3/#1)[

![](https://cdn.deepseek.com/site-icons/kodekloud.com)

KodeKloud Notes

2026/07/21

Leveraging the LangGraph Store - KodeKloud

Explains LangGraph’s persistent store and checkpointing for agent workflows, enabling durable state, pause and resume, observability, and scalable backend options for production deployments. The Lang



](https://notes.kodekloud.com/docs/LangGraph/Long-Term-Memory-and-Stateful-Persistence/Leveraging-the-LangGraph-Store/page#content-area#1)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal

2025/04/10

Temporal: Beyond State Machines for Reliable Distributed Applications

and implementing robust retries and timeouts. ... - How Temporal lets developers write plain code and often avoid writing explicit state-machine logic while still getting all the benefits of state tracking, retries ... For example, if payment fails, the state machine can transition to a “payment failed” state and trigger a compensating action or retry, rather than proceeding forward.



](https://temporal.io/blog/temporal-replaces-state-machines-for-distributed-applications)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

learn.temporal.io

- **Activity Heartbeats improve failure detection**

Retry Policies ... - **By default, Temporal automatically retries an Activity that fails** ... **.build();** ... - **Workflow Executions do not retry by default** ... - Delay doubles before each subsequent attempt until reaching maximum of 100 seconds - Retries continue until the Activity completes, is canceled, or Workflow Execution ends



](https://learn.temporal.io/assets/files/crafting-an-error-handling-strategy-java-replay2025-0550281e33357a316fda8faad73242f4.pdf#3#3)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal Docs

Why Temporal? | Temporal Documentation

A step takes days | Scheduler ... timeout sweeper | A Timer in Workflow code, durable across restarts ... A transaction half-completes | Hand-written compensation and cleanup | The Saga pattern in ordinary control flow ... Wrap several Activities in a Workflow when you need ordering, state between steps, or compensation. The Activity code doesn't change.



](https://docs.temporal.io/evaluate/why-temporal)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal Docs

In Temporal, timeouts detect application failures. The system can then automatically mitigate these failures through retries. ... the maximum time a Workflow Execution can stay Open, including retries ... A timeout limits how long a Workflow can absorb delays. To act after a set period inside a Workflow, use a [Timer](/workflow-execution/timers-delays) instead.



](https://docs.temporal.io/evaluate/features/timeouts-and-retries.md)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

learn.temporal.io

Crafting an Error Handling Strategy

3. Timeouts 04. Retry Policies 05. Recovering from Failure ... - Explain how Temporal handles retries - Apply a custom Retry Policy to Workflow and Activity Execution ... - Implement the Saga pattern to restore external state following failure in a Workflow Execution ... Compensating transaction ... - Using a backoff coefficient to increase delay between retries can avoid overloading the system



](https://learn.temporal.io/assets/files/crafting-an-error-handling-strategy-java-replay2025-0550281e33357a316fda8faad73242f4.pdf#3#1)[

![](https://cdn.deepseek.com/site-icons/etsi.org)

osm-download.etsi.org

Open Source

The same code, after adding support for retries during withdrawal ... The same code, after adding support for retries during withdrawal and deposit, and performing a compensation if the withdrawal succeeds but the deposit fails ... - hello_activity_rety - Demonstrate activity retry by failing until a certain number of attempts.



](https://osm-download.etsi.org/ftp/osm-13.0-thirteen/OSM-MR%2314_Ecosystem_Day/OSM-MR%2314_Ecosystem_Day_3-Canonical.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/01/06

system-design-patterns/18-workflow-job-systems/04-durable-execution-workflow-engines.md at ca2c01986fd36a40e16516a7570fb87c2c163e51 · babushkai/system-design-patterns - Skip to content

Effect Commit Protocols owns activity retries, idempotent external effects, reconciliation, and compensation. ... Even when a service describes a state transition/task execution as exactly once, an explicitly configured retry or an external API's commit/response ambiguity can repeat effects. ... - A timer wait persists state and releases application-worker compute...



](https://github.com/babushkai/system-design-patterns/blob/ca2c01986fd36a40e16516a7570fb87c2c163e51/18-workflow-job-systems/04-durable-execution-workflow-engines.md#1)[

![](https://cdn.deepseek.com/site-icons/lobehub.com)

LobeHub

2026/03/03

backend-development-workflow-orchestration-patterns | Skills Marketplace · LobeHub - backend-development-workflow-orchestration-patterns

# backend-development-workflow-orchestration-patterns 3 3 7 ## Summary This Skill captures best practices and architecture patterns for building durable workflow orchestration with Temporal. It e



](https://lobehub.com/skills/sla-te-copilot-converter-backend-development-workflow-orchestration-patterns#1)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

learn.temporal.io

WHAT IS DURABLE EXECUTION

WHAT IS DURABLE EXECUTION? WHY DURABLE EXECUTION? 2 WHAT IS DURABLE EXECUTION? 3 WHAT CAN I USE DURABLE EXECUTION FOR? 4 WHAT HAPPENS IF AN EXTERNAL SERVICE GOES DOWN? 5 HOW DOES DURABLE EXE



](https://learn.temporal.io/assets/files/zines-6425991d04e05e05031aa2b4a2ccddf4.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/lobehub.com)

LobeHub

2026/02/16

workflow-orchestration-patterns | Skills Marketplace · LobeHub - workflow-orchestration-patterns

# workflow-orchestration-patterns 2 1.0.1 Microck 2 8 124 ## 摘要 Provides architecture guidance and patterns for building durable workflow orchestration using Temporal. Explains the core separati



](https://lobehub.com/zh-TW/skills/microck-ordinary-claude-skills-workflow-orchestration-patterns#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/06/14

agentic-systems-architect-learning/lessons/mod-308-deployment-durable-execution/03-human-in-the-loop-architecture.md at main · ai-engineering-curriculum/agentic-systems-architect-learning - Skip to content

LangGraph's interrupt model names the four responses a human can give, and they are the right vocabulary because each resumes the run differently ... When the human decides — minutes or days later, possibly on a completely different ... In Temporal this isawait workflow.wait_condition(...) on a signal; in LangGraph it is interrupt() with a persisted checkpoint resumed by a Command.



](https://github.com/ai-engineering-curriculum/agentic-systems-architect-learning/blob/main/lessons/mod-308-deployment-durable-execution/03-human-in-the-loop-architecture.md#1)[

GitHub

Chapter 3 — Human-in-the-Loop Approval Architecture

LangGraph's interrupt model names the four responses a human can give, and they are the right vocabulary because each resumes the run differently ... When the human decides — minutes or days later ... In Temporal this is `await workflow.wait_condition(...)` on a signal; in LangGraph it is `interrupt()` with a persisted checkpoint resumed by a `Command`. The mechanism differs...



](https://raw.githubusercontent.com/ai-engineering-curriculum/agentic-systems-architect-learning/refs/heads/main/lessons/mod-308-deployment-durable-execution/03-human-in-the-loop-architecture.md#1)[

![](https://cdn.deepseek.com/site-icons/langchain.com)

LangChain

Human-in-the-loop The Human-in-the-Loop (HITL) [middleware](/oss/javascript/langchain/middleware/built-in#human-in-the-loop) lets you add human oversight to agent tool calls.



](https://docs.langchain.com/oss/javascript/langchain/human-in-the-loop.md)[

![](https://cdn.deepseek.com/site-icons/socket.dev)

Socket

2026/06/05

@looppause/langgraph - npm Package Security Analysis - Socke... - @looppause/langgraph

Native LoopPause human-in-the-loop nodes for LangGraph (TypeScript) ... plus a router and a webhook-resume helper ... makePollingGate | Long-poll until responded | Simple flows ... This is the right pattern for long-running approvals (hours, days) where you cannot keep a connection open.



](https://socket.dev/npm/package/@looppause/langgraph/overview/0.1.1#1)[

![](https://cdn.deepseek.com/site-icons/npmjs.com)

NPM

2026/06/13

@looppause/langgraph

@looppause/langgraph ... Native LoopPause human-in-the-loop nodes for LangGraph (TypeScript). ... makePollingGate | Long-poll until responded | Simple flows ... This is the right pattern for long-running approvals (hours, days) where you cannot keep a connection open.



](https://www.npmjs.com/package/@looppause/langgraph?activeTab=code#1)[

![](https://cdn.deepseek.com/site-icons/tencent.com)

Yaf_Dispatcher::__sleep

2026/08/16

LangGraph 如何实现人机协同（Human-in-the-Loop）？

由于中断机制建立在 checkpointer 之上，暂停可以持续任意时长——从几毫秒到数天。Agent 的状态在整个等待期间被持久化存储，不会占用运行时的连接资源。恢复时只需使用相同的 thread_id 调用 invoke() ... 人类决策被折叠进状态后继续执行后续节点。



](https://developer.cloud.tencent.com/techpedia/2684/21468)[

Pushary

2026/07/16

LangGraph human-in-the-loop from your phone

Pattern B (interrupt plus webhook resume) parks the graph with zero compute for long waits. ... Use interrupt() plus a webhook-driven Command(resume=answer) when the wait can be long, because the graph parks in its checkpointer with no compute held open.



](https://pushary.com/blog/langgraph-human-in-the-loop-phone)[

![](https://cdn.deepseek.com/site-icons/langchain.com)

LangChain

2026/09/27

Human-in-the-loop - Docs by LangChain

Human-in-the-loop The Human-in-the-Loop (HITL) middleware lets you add human oversight to agent tool calls. When a model proposes an action that might require review—for example, writing to a file or executing SQL—the middleware can pause execution and wait for a decision.



](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/05/14

docs/src/oss/deepagents/human-in-the-loop.mdx at 933a2f9217f6293a54fa59d40ce69b619aaa1172 · langchain-ai/docs - Skip to content

Skip to content ## Navigation Menu {{ message }} # human-in-the-loop.mdx # human-in-the-loop.mdx ## File metadata and controls 707 lines (571 loc) · 20 KB title | Human-in-the-loop ---|--- des



](https://github.com/langchain-ai/docs/blob/933a2f9217f6293a54fa59d40ce69b619aaa1172/src/oss/deepagents/human-in-the-loop.mdx#1)[

![](https://cdn.deepseek.com/site-icons/langchain.com)

LangChain

> ## Documentation Index > Fetch the complete documentation index at: https://docs.langchain.com/llms.txt > Use this file to discover all available pages before exploring further. # Human-in-the-loop



](https://docs.langchain.com/langsmith/add-human-in-the-loop.md)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Learn Temporal

2026/01/05

Part 2: Building Long-Running MCP Tools with Human-in-the-Loop | Learn Temporal

Temporal makes human-in-the-loop patterns reliable by preserving workflow state during long waiting periods—whether that's minutes, hours, or days. If users close their browser ... The tool will process invoices automatically but pause to wait for human approval before finalizing payments—and it will use Temporal's durable timers to handle approval deadlines.



](https://learn.temporal.io/tutorials/ai/building-mcp-tools-with-temporal/adding-hitl-to-mcp-tools/#step-2-quit-claude-desktop-while-the-workflow-is-running)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal Docs

2026/08/13

Human-in-the-loop AI agent | AI Cookbook | Temporal Documentation

This example demonstrates how to build an AI agent that requires human approval; we use Temporal Signals to bring that user input into the agent. ... - If the proposed action is deemed risky, pauses and waits for human approval via Temporal Signal ... Can wait for approval for hours, days or indefinitely; while waiting ... We use a Temporal Signal to inject information from the human into the waiting Workflow.



](https://docs.temporal.io/ai/cookbook/human-in-the-loop-python)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Learn Temporal

2025/11/05

Part 2: Adding Durable Human-in-the-Loop to Our Research Application | Learn Temporal

In this tutorial, you'll solve these problems by adding durable human-in-the-loop capabilities to your application. ... sending akeep signal to continue the workflow ... Temporal's durability ensures you maintain control over AI-generated content while reliably handling the human approval process. ... With Temporal's durable execution, the workflow instance persists throughout the entire human interaction...



](https://learn.temporal.io/tutorials/ai/building-durable-ai-applications/human-in-the-loop/#__docusaurus_skipToContent_fallback)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/07/17

scale-agentex-python/examples/tutorials/10_async/10_temporal/080_open_ai_agents_sdk_human_in_the_loop/README.md at main · scaleapi/scale-agentex-python - Skip to content

How to pause agent execution and wait indefinitely for human approval using Temporal's child workflows and signals. The agent can wait for hours, days, or weeks for human input without consuming resources - and if the system crashes, it resumes exactly where it left off.



](https://github.com/scaleapi/scale-agentex-python/blob/main/examples/tutorials/10_async/10_temporal/080_open_ai_agents_sdk_human_in_the_loop/README.md#1)[

thundergun.io

Approval Pattern | Temporal Documentation

The Approval pattern implements human-in-the-loop Workflows where execution blocks until an external decision is made. ... The Approval pattern uses a blocking wait with timeout to pause execution until a Signal is received. ... condition() in TypeScript ... - If an approver sends a Signal before the timeout expires, the Workflow receives the approval data...



](https://temporal-documentation-git-main.preview.thundergun.io/design-patterns/approval)[

![](https://cdn.deepseek.com/site-icons/zenml.io)

ZenML

Retool: Building Production AI Agents with Temporal-Based Workflow Orchestration - ZenML LLMOps Database

signals for human approval, and event history for audit trails ... requesting human approval for dangerous actions ... Fourth, dangerous actions requiring human approval create the need for workflows that can pause indefinitely while awaiting human response. ... - Human approval: Temporal signals enable workflows to pause indefinitely with zero resource consumption and resume when approved



](https://www.zenml.io/llmops-database/building-production-ai-agents-with-temporal-based-workflow-orchestration#1)[

thundergun.io

This example demonstrates how to build an AI agent that requires human approval ... 2. If the proposed action is deemed risky, pauses and waits for human approval via Temporal Signal 3. Executes the action if auto-approved (if not risky) or human approved, or cancels if rejected/timed out



](https://temporal-documentation-git-main.preview.thundergun.io/ai/cookbook/human-in-the-loop-python.md)[

GitHub

catalog_title: Temporal

long-running agents and tools, human approvals ... - **Long-running and ambient agents**: Support for agents and tools that run for hours, days, or indefinitely using blocking awaits. - **Human-in-the-loop**: Pause execution until a human approves, then resume where you left off. Temporal's



](https://raw.githubusercontent.com/google/adk-docs/main/docs/integrations/temporal.md#1)[

thundergun.io

# External Interaction Patterns > For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt). > Any documentation page is available as raw Markdown by appending `.md` to



](https://temporal-documentation-git-main.preview.thundergun.io/design-patterns/external-interaction-patterns.md)[

GitHub

Invoice Processing with Temporal + MCP

Demonstrates how to integrate Temporal durable workflows with the Model Context Protocol (MCP). An invoice processing workflow serves as the example business logic, with different MCP server implement



](https://raw.githubusercontent.com/temporal-community/durable-async-mcp/refs/heads/main/README.md#1)[

Go Packages

2026/05/08

agentexecutionv1 - //

Idempotency If recovery is already in progress (execution moved to IN_PROGRESS after a previous recover call), the call succeeds as a no-op and returns current state. ... - Retry after investigating and fixing the root cause ... If the execution is not paused (already IN_PROGRESS)...



](https://pkg.go.dev/github.com/stigmer/stigmer/mcp-server@v0.4.8/proto/ai/stigmer/agentic/agentexecution/v1#13)[

getaxonflow.com

2026/07/06

LangGraph Integration - Stateful AI Workflow Governance | AxonFlow Documentation

retryPolicy makes retry behavior explicit, so teams can choose between idempotent retries and reevaluation when a guarded step fails - idempotency keys pin a step ... The newer workflow surface makes those decisions explicit.idempotent retries preserve the same decision boundary for the same workflow and step...



](https://docs.getaxonflow.com/docs/integration/langgraph/)[

My Best Work Is When Nothing Happens — A Conversation with the Person Behind $3 Trillion in Nightly Batch Jobs

2026/05/26

Retries Were Built for a Deterministic World

LangGraph recently made NodeTimeoutError retryable by default, with an explicit warning: if your nodes have side effects that aren't idempotent, opt out before upgrading. ... LangGraph's recent decision to make NodeTimeoutError retryable by default prompted an explicit upgrade warning about non-idempotent side effects...



](https://current.tinyfish.ai/issue/31/practitioners-corner/article/18051/retries-were-built-for-a-deterministic-world)[

Go Packages

2026/04/25

agentexecutionv1 - func (x *PendingApproval) GetToolCallId() string

Idempotency If recovery is already in progress (execution moved to IN_PROGRESS after a previous recover call), the call succeeds as a no-op and returns current state. ... point - Retry after investigating and fixing the root cause ... If the execution is not paused (already IN_PROGRESS)...



](https://pkg.go.dev/github.com/stigmer/stigmer/mcp-server@v0.0.98/proto/ai/stigmer/agentic/agentexecution/v1#11)[

GitHub

title: Replay, Resume, and Idempotency

`run_with_retry` and `arun_with_retry` restart the node body from the top after a retryable failure ... `run_with_retry` and `arun_with_retry` can call the same node body more than once after a failure or timeout...



](https://raw.githubusercontent.com/sandgardenhq/dh-library/refs/heads/main/content/en/langgraph/06-replay-resume-and-idempotency.md#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

github.com

LangChain can simplify model/tool/application integration, but it isn't primarily a durable workflow engine

LangChain ... LangGraph ... LangGraph supports checkpointing/persistence, allowing graph ... resume after failures. (Docs by LangChain) ... idempotency Suppose a LangGraph node does ... If you retry ... LangGraph's own guidance emphasizes designing tasks to be idempotent because execution may be resumed/re-executed. (Docs by LangChain)



](https://github.com/sherozshaikh/rag-llm-interview-handbook/blob/main/RAG%20%26%20LLM%20Basics%20-%20Handbook%20For%20Interview%20Prep.pdf#10#4)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/07/21

dh-library/content/en/langgraph/06-replay-resume-and-idempotency.md at main · sandgardenhq/dh-library - Skip to content

06-replay-resume-and-idempotency.md ... boundary.run_with_retry ... Retries use the same at least once rule.run_with_retry and arun_with_retry can call the same node body more than once after a failure or timeout...



](https://github.com/sandgardenhq/dh-library/blob/main/content/en/langgraph/06-replay-resume-and-idempotency.md#1)[

![](https://cdn.deepseek.com/site-icons/langchain.com)

LangChain

2026/09/22

Fault tolerance - Docs by LangChain

Configure per-node timeouts, retries, and error handlers in LangGraph. When a node fails—from a slow external API, a transient network error, or an unhandled exception—LangGraph gives you three composable mechanisms to respond ... A retry policy automatically re-runs a failed node attempt based on exception type and backoff settings.



](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)[

GitHub

Idempotency (`skein.idempotency`)

Idempotency (`skein.idempotency`) ... **This block is tuning, not an on/off switch.** Omitting it does not disable `Idempotency-Key` ... LangGraph's `webhook` field is a bare URL with no delivery policy at all, so this block is a skein extension under the reserved namespace, for the same reason `skein.idempotency` is.



](https://raw.githubusercontent.com/skein-js/skein-js/f06fea04e07114199d1bacf3239775614021c3ba/docs/langgraph-cli-compat.md#2)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal Docs

Error handling - Python SDK | Temporal Documentation

Without idempotence, this could cause duplicate charges in payment processing or create duplicate resources in infrastructure provisioning. ### Use idempotency keys Most external services support idempotency keys—unique identifiers that prevent duplicate operations. ... Create an idempotency key by combining the Workflow Run ID and Activity ID...



](https://docs.temporal.io/develop/python/best-practices/error-handling)[

![](https://cdn.deepseek.com/site-icons/linkedin.com)

LinkedIn · Fabian Warislohner

2026/04/20

Temporal gives you durable execution. It does not give you exactly-once. | Piotr Zawadzki | 13 条评论 - 跳到主要内容

At-least-once (default) - retries until success, which means your activity may run more than once. At-most-once (maximumAttempts=1) - runs zero or one time, never duplicates, but may leave you with a half-finished operation. Neither is exactly-once.



](https://www.linkedin.com/posts/zawadzkipiter_temporal-distributedsystems-softwarearchitecture-activity-7452308217507803136-CoKl?utm_source=share&utm_medium=member_desktop&rcm=ACoAABL-RowBafQ27KwbJWsUbCd5i3ocuFsHIno&trk=article-ssr-frontend-pulse_little-text-block#1)[

temporal.org.cn

2024/02/26

理解分布式系统中的幂等性

Temporal 建议活动应该是幂等的，或者至少，多次执行活动不会导致任何意外或不希望的副作用 ... Temporal 可以根据配置保证“至少一次”或“最多一次”活动执行。默认情况下，活动重试次数是无限的，这意味着“至少一次”执行，但实际上意味着尽可能多次。



](https://temporal.org.cn/blog/idempotency-and-durable-execution)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

pages.temporal.io

The Saga Pattern Made Easy | 1

They need to be idempotent, which means they can be executed multiple times without causing side effects to the system or to the steps in the transaction. ... Idempotency is important because it’s possible that a compensation may need to be retried many times, should it fail.



](https://pages.temporal.io/rs/250-WIU-007/images/tech-guide-saga-pattern-made-easy.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal

2024/10/22

Preliminary investigation into idempotent signals - Show & Tell - Temporal Community Forum

Temporal recommends making activities idempotent. ... If the service receives another request with the same idempotency key as a previous request, the duplicate request can be simply ignored. ... My understanding is that the Temporal SDK’s can use the request_id to automatically deduplicate retries from the same client.



](https://community.temporal.io/t/preliminary-investigation-into-idempotent-signals/13694/2)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal

2024/02/26

What is idempotency? And why it matters for durable systems

Idempotency is a property of functions or operations in programming, and it’s a crucial property when working with durable ... Temporal recommends Activities be idempotent, or at least if they aren’t, that executing an Activity more than once does not cause any unexpected or undesired side effects.



](https://temporal.io/blog/idempotency-and-durable-execution)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2023/12/27

GitHub - joshmsmith/temporal-idempotence-by-validation: Temporal idempotence by validation sample · GitHub - GitHub - joshmsmith/temporal-idempotence-by-validation: Temporal idempotence by validation sample · GitHub

Sometimes with Temporal, you need to call a service that isn't idempotent: calling it more than once with the same inputs is bad - may cause duplicate entries or other unintended behavior. In such a case, you can set a policy to call the non-idempotent activity only once, and then **validate** that it was successful, and retry it if not.



](https://github.com/joshmsmith/temporal-idempotence-by-validation#1)[

![](https://cdn.deepseek.com/site-icons/medium.com)

Medium · Dented Feels

2026/03/13

Temporal Signals: 7 Idempotency Slips - Sitemap

How to stop retries, replays, and workflow edge cases from charging the same money twice. Learn 7 idempotency slips in Temporal and payment systems that can replay money twice, and how to fix them before retries become revenue incidents. ... Temporal’s docs explicitly recommend making Activities idempotent because Activities can be retried...



](https://medium.com/@connect.hashblock/temporal-signals-7-idempotency-slips-fb5132ed3f43#1)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

learn.temporal.io

Scheduled Event ID 5

**Idempotency is a general concern for distributed systems** - Will multiple invocations of your operation result in adverse changes to application state? - This is a concern for Activities in Temporal, since they may be executed multiple times - Temporal strongly recommends that you ensure you Activities are idempotent



](https://learn.temporal.io/assets/files/crafting-an-error-handling-strategy-java-replay2025-0550281e33357a316fda8faad73242f4.pdf#3#2)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/02/01

claude-temporal-plugin/skills/temporal-developer/references/core/gotchas.md at main · temporalio/claude-temporal-plugin - Skip to content

Skip to content ## Navigation Menu {{ message }} - NotificationsYou must be signed in to change notification settings - Fork 1 # gotchas.md # gotchas.md ## File metadata and controls 239 lines



](https://github.com/temporalio/claude-temporal-plugin/blob/main/skills/temporal-developer/references/core/gotchas.md#1)[

Go Packages

2025/01/02

temporal-go-helpers - temporal-go-helpers

The Saga Pattern is used for managing data consistency across microservices in distributed transaction scenarios. This module provides APIs for easily executing compensation rollback logic, even after the parent workflow has been cancelled. ... The various compensation rollback logic can be executed in parallel by settingParallelCompensation to true.



](https://pkg.go.dev/github.com/courtsite/temporal-go-helpers#1)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal Docs

Saga Pattern | Temporal Documentation

The Saga pattern manages distributed transactions across multiple services by coordinating a sequence of local transactions, each with a compensating action that can undo its effects if subsequent steps fail. ... You implement each ... If any step fails, you execute compensation transactions in reverse order to undo the effects of all completed steps. You register compensations as each step completes...



](https://docs.temporal.io/design-patterns/saga-pattern)[

Go Packages

2026/05/12

temporal - temporal

Compensator is a LIFO stack of compensation functions for the saga pattern. Usage pattern: - Declare a Compensator at the top of the workflow function. - Defer a block that calls compensate when the workflow is failing. - After each forward step succeeds, call add to register its undo.



](https://pkg.go.dev/github.com/mrsimonemms/golang-helpers@v0.7.2/temporal#TemporalOpts.TLSEnabled#1)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal

Saga Pattern Made Easy | Technical Guide

You can think of the Saga pattern as a design pattern that ensures application consistency by using compensations to revert the system to its last known good state when faced with failure at any point in the transaction. Curious how to automate Saga Pattern with Temporal ... - How Temporal can help automate this



](https://pages.temporal.io/download-saga-pattern-made-easy-rp.html)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Learn Temporal

2024/07/16

Build a trip booking application in Python | Learn Temporal

The Saga pattern offers a solution to this problem by allowing distributed transactions to be broken into smaller, manageable transactions, each with its ... The Saga pattern is a design pattern that provides a mechanism to manage long-running transactions and ensure data consistency across multiple services. Instead of a single monolithic transaction, the Saga pattern breaks the transaction into smaller...



](https://learn.temporal.io/tutorials/python/trip-booking-app/)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/11/25

GitHub - anarefin/temporal-event-driven-saga · GitHub

A production-ready microservices implementation of the Saga pattern using Spring Boot, Apache Kafka, and Temporal Workflow Engine. This project demonstrates distributed transaction management with automatic compensation across multiple services using an event-driven architecture. ... * ✅ **Automatic Compensation** in reverse order on failures



](https://github.com/anarefin/temporal-event-driven-saga#1#1)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Learn Temporal

2021/09/30

Build a trip booking system with PHP | Learn Temporal

The Saga pattern guarantees that either all operations are completed successfully or the corresponding compensation transactions are run to undo the previously completed work. Implementing the Saga pattern can be complex, but fortunately, Temporal provides native support for the Saga pattern. It means that handling all the rollbacks and running



](https://learn.temporal.io/tutorials/php/build_a_trip_booking_app/)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal

2023/05/01

Saga Compensating Transactions

The compensating action pattern provides transaction-like guarantees for a sequence of operations amid this distributed systems chaos. ... Sagas, a design pattern for failure resilience, use compensations, but also ensure there is a way to “go forwards” (by retrying) and maintain that an entire sequence of operations acts like a single transaction.



](https://temporal.io/blog/compensating-actions-part-of-a-complete-breakfast-with-sagas)[

![](https://cdn.deepseek.com/site-icons/temporal.io)

Temporal

2025/04/24

Error handling strategy with Java - Training - Temporal Community Forum

if there is a limited time to complete the entire SAGA — for example, when a user is waiting for the result — you cannot guarantee that the action will be retried as long as necessary. You might end up in a situation where the action produced a side effect...



](https://community.temporal.io/t/error-handling-strategy-with-java/17235/2)[

![](https://cdn.deepseek.com/site-icons/latenode.com)

Latenode

2025/10/05

How template-driven saga and compensation implementations differ between temporal and camunda? - Other Questions / Developer & Architectural Solutions - post by SolarisWanderer on Oct 6, 2025

I’ve been using ready-to-use templates to learn saga and compensation patterns and to produce equivalent implementations for Temporal and Camunda. ...



](https://community.latenode.com/t/how-template-driven-saga-and-compensation-implementations-differ-between-temporal-and-camunda/52486/4#1)
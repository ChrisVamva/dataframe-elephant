---
modified: 2026-09-28T20:21:42+03:00
---
The integration of generative AI into smart homes has produced a category with genuine capability but a persistent reliability gap. Independent testing through 2026 shows that AI-generated automations, camera summaries, and natural-language control remain **unreliable for consequential actions, opaque in their failure modes, and difficult to audit or migrate**. The specification has advanced; the user experience has not kept pace.

### ✅ Safe Autonomy vs. Required Confirmation

The emerging consensus—reflected in both product design and research prototypes—is a **tiered permission model** based on device risk and action reversibility.

**Safe for autonomous execution:**
- **Low-risk, reversible actions**: Adjusting lights, setting thermostats, playing media, or changing scenes. These are the core use cases where AI assistants provide value without introducing physical security risk.
- **Simple, unambiguous commands**: "Turn on the kitchen light" or "Set the living room to 72 degrees." Benchmarks for local models show that direct commands achieve the highest accuracy (up to 86.7% in controlled tests), making them suitable for automation.

**Requires explicit confirmation (human-in-the-loop):**
- **Physical security devices**: Door locks, garage doors, gates, and alarm systems. Google Home's developer documentation mandates secondary user verification (e.g., PIN or NFC keyfob proximity) for unlocking, disarming, or opening these device types.
- **Camera access and privacy-sensitive operations**: Enabling or disabling cameras, deleting footage, or granting camera access to third parties. Research prototypes consistently gate these behind confirmation prompts.
- **Automation creation or modification**: Having an AI agent write, modify, or delete automation rules or system configurations without review. The security implications of an agent altering your home's logic are significant enough that human approval is considered essential.
- **Mixed-intent commands with invalid sub-tasks**: If a user says "Turn on the TV and the non-existent heater," a safe agent should execute the valid action and flag the invalid one with an error, not fail entirely or hallucinate a device. Research frameworks like DS-IA implement this "Generate-and-Filter" strategy, achieving zero forced hallucinations in controlled benchmarks.

### 🗣️ Ambiguity, Household Identities, Guests, Children, and Adversarial Commands

**Ambiguity resolution** remains inconsistent. Research benchmarks distinguish between **autonomous resolution** (when device state makes the answer obvious) and **proactive questioning** (when it does not). For example, if a user says "Turn on the lamp" and one of two lamps is already on, a well-designed agent should silently turn on the other. If both are off, it should ask which one. Commercial assistants often fail this distinction, either guessing incorrectly or asking unnecessary questions.

**Household identities** are managed primarily through **voice matching** (e.g., Google's Voice Match), which links a voice profile to an account. This allows personalized responses and permissions. However, Google Home documentation notes that if a household has more than six members, users should prioritize setting up Voice Match for those needing specific controls, such as children or guests.

**Children and guests** are handled through **restricted access profiles**. Google Home now allows kids under 13 to use the app with limited permissions, and supports separate access levels for "Settings" and "Activity." Research on authorization frameworks proposes "Circles of Trust," where homeowners and spouses have full access, while visitors and children receive progressively fewer privileges—visitors, for example, should never be able to control locks, doors, or cameras. In practice, however, implementation is uneven. Google Home's Gemini assistant is available to all household members including children, with only optional content filters for sensitive topics.

**Adversarial voice commands** represent a serious and underappreciated risk. **Inaudible command injection** can transmit ultrasound signals that voice assistants interpret as commands while humans hear nothing. Researchers have demonstrated this against Google Home, Amazon Echo, and Siri, with the ability to trigger actions like opening a garage door. More recently, a **prompt injection vulnerability in Gemini** allowed attackers to hijack the assistant via ordinary messaging notifications, potentially controlling smart home devices through Google Home. These are not theoretical: the attack surface is expanding as AI assistants gain more device control.

### 💻 Local vs. Cloud: Latency, Cost, Privacy, and Capability Trade-offs

This is the most consequential architectural decision for AI smart home features, and the trade-offs are stark.

| Factor | Local (On-Device / Edge) | Cloud (LLM API) |
|---|---|---|
| **Latency** | Under 200 ms; on-device voice assistants can respond in under 1 second | Network-dependent; 100–2000 ms is typical, with variability from congestion and API rate limits |
| **Cost** | One-time hardware cost ($2–$80 per device, or $99–$199 for a hub); no per-inference fee | Recurring subscription or per-call cost; cloud AI can cost $0.001–$0.10+ per inference, scaling linearly with usage |
| **Privacy** | Raw audio/video never leaves the home; only processed intents or anonymized data may be transmitted | Footage and audio may be used for AI training unless explicitly opted out; live camera feeds analyzed in the cloud introduce surveillance risk |
| **Capability** | Constrained by local hardware; best local models achieve 72–75% accuracy on complex intent benchmarks | Full-size LLMs offer superior reasoning, multi-step planning, and context handling, but with higher cost and latency |
| **Reliability** | Deterministic, no network dependency; works during internet outages | Fails when connectivity is lost; API rate limits and outages cause intermittent failures |

**Hybrid approaches** are emerging as the pragmatic middle ground. Nuvon, an embedded assistant built on an ESP32 microcontroller, processes simple commands locally and sends only complex queries to the cloud, achieving sub-one-second responses and ~85% accuracy in quiet environments while minimizing raw audio transmission. LLMSwitch-router, a research system, dynamically routes between edge and cloud models, reducing LLM API cost by 48% while maintaining cloud-level accuracy.

The commercial reality, however, remains cloud-heavy. Consumer Reports found that **Alexa Plus controls were buggy and the companion app was slower and less usable** than competitors, while **Gemini for Home felt slower than the old Google Assistant and frequently could not control devices it should know about**. Both were described as potentially acting as wrappers around legacy backends rather than true replacements.

### 📝 Understandability, Editability, Testability, and Portability of Generated Routines

**Understandability** is mixed. Users report that AI-generated camera summaries can be eerily accurate—correctly identifying car makes and models—but also **frequently hallucinate**. Google Home's "Home Brief" feature generated false positives including ghost sightings, misidentified animals, and reports of people who were not there. As one reviewer noted, "after a few false positives, you grow to distrust the robot."

**Editability** depends heavily on the platform. Open-source systems like Home Assistant allow full version history for AI-generated automations with diff viewing, and AI agents can create rules that are disabled and prefixed `[Selora AI]` for user review before activation. Commercial ecosystems are more opaque: automations created through Alexa or Google Home are typically editable only within the vendor's app, and the AI's reasoning is not exposed.

**Testability** is largely absent in consumer products. Research prototypes include verification stages—DARIO uses a lightweight verifier that checks schema, execution, dependency, and safety constraints before committing actions, achieving 0.91 overall task success and reducing unsafe execution to 0.02. But these verification layers are not shipped in commercial assistants.

**Portability** is effectively **nonexistent across ecosystems**. A Matter device can be shared via Multi-Admin, but the **automations, routines, and AI-generated logic are ecosystem-specific**. There is no export format for a Google Home routine to be imported into Apple Home or SmartThings. Matter 1.6's Joint Fabric aims to create a shared datastore, but adoption is nascent and does not address routine portability.

### 📊 Major Assistant Comparison: Accuracy, Error Types, and Recovery

| Assistant | Natural-Language Accuracy | Dominant Error Types | Recovery Behavior | Auditability |
|---|---|---|---|---|
| **Amazon Alexa (Plus)** | Buggy controls; slower app; commerce features prioritized over reliability | Failed device control, timeout on multi-step commands | Manual retry required; no automatic fallback to local control | Minimal; activity logs available but not AI reasoning |
| **Google Gemini (for Home)** | Slower than legacy Assistant; frequently cannot control known devices; may wrap legacy backend | Device not found, hallucinated actions, camera false positives (ghosts, misidentified animals) | Inconsistent; live camera analysis requires premium subscription | Home Brief summaries are opaque; no explanation of AI decisions |
| **Apple Siri / HomeKit** | Consistently rated weaker than Google and Alexa for conversational AI; Siri remains "the weakest of the major voice assistants" for general questions and accents | Limited natural-language understanding; falls back to rigid command matching | Strong local control via HomeKit; automations run locally | Best-in-class for local auditability; no AI-generated summaries currently |
| **Samsung SmartThings** | First to support Matter 1.5 cameras (live streaming, motion, PTZ); 58 device types supported | Fewer AI features; more traditional rule-based automation | Reliable local execution; broad device compatibility | Activity logs available; AI features limited |

**Benchmark evidence for local models** (relevant for on-device implementations):
- Qwen3 8B with `/no_think` prompt: **74.8% accuracy**, 1.9s latency; without `/no_think`, accuracy drops to 45–65% and becomes operationally unreliable.
- Qwen2.5 7B Q5_K_M: **72.5% accuracy**, 2.3s latency; most reliable local choice.
- Smaller models (Llama 3.2 3B) are **not viable** (12–21% accuracy).
- Accuracy degrades **5–15 percentage points** as device inventory grows from 34 to 88 entities.

### 🔍 Roadmap vs. Available Functionality

**Available today:**
- Tiered confirmation for locks and security devices (Google Home developer API)
- Voice Match and restricted profiles for children and guests (Google Home)
- Local processing for simple commands on embedded devices (Nuvon prototype)
- Matter 1.5 camera support on SmartThings and Amazon Echo
- AI-generated automation drafts with version history (Home Assistant ecosystem)

**Roadmap or research-only:**
- **Joint Fabric** (Matter 1.6): Shared Datastore across ecosystems for co-administered networks. Not widely adopted.
- **NFC commissioning** (Matter 1.6): Setup before power-on. Ecosystem support incomplete.
- **Verification layers** (DARIO, DS-IA): Research frameworks achieving 0.91 task success and 0.02 unsafe execution. Not productized.
- **On-device LLM assistants** with 86.7% direct-command accuracy: Research prototypes, not commercial products.
- **LLMSwitch-router** hybrid routing: 48% cost reduction in research settings. No commercial equivalent.

### 🚨 Interoperability Risk Assessment for AI Features

**High Risk:**
- **Adversarial command injection**: Inaudible ultrasound and prompt injection attacks are demonstrated against all major assistants. The attack surface grows as AI gains more device control.
- **Camera summary hallucination**: False positives (ghosts, misidentified pets) erode trust and could trigger inappropriate automations if summaries are used as automation triggers.
- **No routine portability**: Users are locked into ecosystems for AI-generated logic. Migration requires rebuilding from scratch.
- **Cloud dependency for advanced features**: Live camera analysis, complex reasoning, and multi-step planning all require internet. Outages disable these features entirely.

**Medium Risk:**
- **Children and guest permissions**: Implementations are inconsistent; Google Home's Gemini is available to all household members, with only optional content filters.
- **Local model reliability**: Best local models achieve ~75% accuracy on complex intents; inventory growth degrades this further.
- **AI reasoning opacity**: Users cannot see why an AI chose an action or how to correct a wrong decision.

**Low Risk:**
- **Basic voice commands for low-risk devices**: On/off, dimming, and thermostat control work reliably across ecosystems.
- **Local execution of pre-existing automations**: Matter and HomeKit automations continue to run when the internet is down.

### 🛠️ Product-Design Implications

1. **Design for tiered autonomy from the start.** Classify every action by reversibility and physical risk. Locks, alarms, and camera access require confirmation; lights and media do not. Do not rely on the AI to make this distinction correctly.

2. **Assume adversarial input.** Voice assistants can be triggered by inaudible commands and prompt injections. Do not expose physical security actions to voice-only authentication. Require secondary verification (PIN, proximity, or biometric) for unlocking, disarming, and camera disabling.

3. **Build hybrid local-cloud architectures.** Process simple commands locally for latency, privacy, and offline resilience. Route only complex reasoning to the cloud. Design so that local control paths are never blocked by cloud timeouts.

4. **Make AI decisions auditable and reversible.** Log every AI-initiated action with the triggering input and the model's reasoning (even if summarized). Provide one-tap undo for AI actions. Version automations created by AI and require explicit user activation before they run.

5. **Do not rely on AI camera summaries for automation triggers.** False positive rates are too high and the failure mode—hallucinated events—is unpredictable. Use summaries for user review only, never as a programmatic input to security or automation logic.

6. **Plan for routine migration.** Even if ecosystem portability is not available today, design your device's automations to be exportable in a structured format (JSON or similar). This reduces lock-in and prepares for Matter Joint Fabric adoption.

7. **Test beyond the happy path.** Evaluate with ambiguous commands, mixed valid/invalid sub-tasks, multiple household members with different permissions, and network outages. The research benchmarks (HomeBench, SAGE, HASE) provide structured test suites that expose failure modes commercial products frequently exhibit.

The state of AI in smart homes in 2026 is one of **demonstrated capability paired with demonstrated unreliability**. The technology can understand natural language, generate routines, and summarize camera footage. It cannot yet do so consistently enough to trust with consequential actions. Product design must bridge this gap with confirmation gates, local fallbacks, and transparent auditability—not by pretending the AI is more reliable than the evidence shows.

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/08/11

Dependency-Aware Reliable Orchestration for Smart-IoT Control with Reasoning-Aligned LLMs

Large Language Models (LLMs) offer a natural interface for smart-IoT control, yet reliable deployment requires more than producing valid API calls. ... It also raises dependency satisfaction to 0.94, reduces unsafe execution to 0.02...



](https://ieeexplore.ieee.org/document/11632566#1)[

![](https://cdn.deepseek.com/site-icons/semanticscholar.org)

Semantic Scholar

2026/03/16

[PDF] Proactive Rejection and Grounded Execution: A Dual-Stage Intent Analysis Paradigm for Safe and Efficient AIoT Smart Homes | Semantic Scholar - sequence Araw

DS-IA achieves a remarkable overall success rate (EM) of 58.56% and an F1-score of 74.90%, significantly outperforming the Baseline (29.98% EM) and SAGE (1.77% EM).



](https://www.semanticscholar.org/reader/7a850e12ae07610e7b74ecf396e8e73961234be4#2)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arxiv.org

SimVerity: When Does Simulated Agent Success Survive Physical Deployment?

it replays matched scenarios on target smart home deployments and cross- validates agent execution ... Although an advanced simulator cleared all 240 light trials ... Google Home's agent executes blinds and lights as one spoken command, and lets camera scene understanding trigger automations across the home (Google Home 2026). Before such an agent ships...



](https://arxiv.org/pdf/2608.25067v1#3#1)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arXiv

Proactive Rejection and Grounded Execution: A Dual-Stage Intent Analysis Paradigm for Safe and Efficient AIoT Smart Homes - is generated, the Three-Level Cascade Verifier independently evaluates each atomic action ArawA_{raw}

the Three-Level Cascade Verifier independently evaluates each atomic action ArawA_{raw}. As required by standard benchmark protocols, unexecutable actions must be flagged with the error token (aka_{k}). ... sub-tasks succeeded and which were safely bypassed due to physical constraints ... DS-IA safely outputs a filtered sequence and alerts the user ... Kitchen dehumidifier not found." This demonstrates zero Task Omission and zero Forced Hallucination.Afinal={turn_on(bedroom_lamp)...



](https://ar5iv.labs.arxiv.org/html/2603.16207#2)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/07/01

AgentHAB: Automating OpenHAB Rule Generation with Multi-Agent Policy and Validation - AgentHAB: Automating OpenHAB Rule Generation with Multi-Agent Policy and Validation

The complexity of IoT device configuration can compromise security through misconfiguration and cross-app interface threats. ... This work presents a “proof-of-concept” and a clear research plan for achieving safe, context-aware rule generation for smart home ecosystems. ... 17-20 March 2026



](https://ieeexplore.ieee.org/document/11576720#1)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

export.arxiv.org

PromptShield Home: Ambient Multimodal Prompt Injection Defense for Smart-Home Agents

PromptShield Home ... Because the label distribution is skewed toward inaction, aggregate accuracy is misleading, a constant always- block predictor scores \(82\%\) , so we report unsafe- execution and safe- completion rates separately. ... aggregate accuracy is misleading: a constant "never act" predictor already reaches \(82\%\) accuracy.



](https://export.arxiv.org/pdf/2608.05495#3#1)[

![](https://cdn.deepseek.com/site-icons/patsnap.com)

Patsnap Eureka

2026/07/23

CN122454975A – Device control method, device control apparatus, device, storage medium, and program product | Patsnap Eureka - Device control method, device control apparatus, device, storage medium, and program product

Traditional voice assistants suffer from limitations in semantic understanding and contradictions between general-purpose large language models and IoT hardware control in device control, resulting in poor device control accuracy and insufficient security. ... A large language model is used to generate control commands that conform to the boundaries, and after security verification, the commands are sent to the IoT devices. Benefits of technology It improves the accuracy and security of device control...



](https://eureka.patsnap.com/patent/CN122454975A#1)[

![](https://cdn.deepseek.com/site-icons/whiterose.ac.uk)

etheses.whiterose.ac.uk

the negative security and privacy implications of cloud- based data processing from the home ... (5) a deterministic safety mechanism, validating LLM- generated control outputs; (6) an integrated and evaluated locally- operated smart home assistant, demonstrating its feasibility as a flexible, privacy- preserving alternative to cloud- based assistants.



](https://etheses.whiterose.ac.uk/id/eprint/39147/1/Hewitt%2CMary%2CThesis.pdf#36#21##36)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/07/01

An Agentic AI Framework for Conflict-Aware Smart Home Automation via Natural Language - An Agentic AI Framework for Conflict-Aware Smart Home Automation via Natural Language

Smart home automation is rapidly expanding, yet existing platforms continue to face significant usability and safety limitations. ... This approach removes image-based configuration barriers while introducing essential safety validation absent from traditional rule engines, enabling safer and more accessible smart home automation. ... 17-20 March 2026



](https://ieeexplore.ieee.org/document/11576688#1)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dl.acm.org

LLMs as PDPs Within a Smart-Home Environment: Accuracy, Ambiguity, and Latency

[Work In Progress Paper] Zachary Edwards Durham University Durham, UK zachary.w.edwards@durham.ac.uk Charles Morisset Durham University Durham, UK charles.morisset@durham.ac.uk ## Abstract



](https://dl.acm.org/doi/pdf/10.1145/3750555.3811905?download=true&__cf_chl_tk=nLQSrR_I4X4khdYq4JIv2xUHyjFiIlTc4UYsxOBTot8-1784651997-1.0.1.1-2rMCocZCRe3GFICxACeEYhg1I5lQfOcaK7bpAU.jtDA#2#1)[

![](https://cdn.deepseek.com/site-icons/zhiding.cn)

至顶智库

2026/08/26

Ring推出"丢弃密钥加密"标准，重塑摄像头数据安全机制

该标准采用轮换加密密钥，Ring仅在用户启用AI功能时使用一次密钥分析视频，分析完毕后立即删除，用户始终持有主密钥。此举旨在提升透明度与隐私保护，同时保留视频描述、人脸识别等AI功能。TAKE将默认开启 ... 尤其是在Ring的AI人脸识别功能遭到审查和诉讼之后，隐私方面的担忧随之而来。



](https://www.zhiding.cn/network_security/2026/0827/3197678.shtml)[

![](https://cdn.deepseek.com/site-icons/cnet.com)

CNET

2026/03/04

Gemini Expands to Live Camera Feeds: What It Means for Your Privacy - CNET - Skip to content

Concerns about Gemini AI accessing security cameras on demand are understandable. Similar privacy questions have arisen with features like Ring's pet-finding Search Party and the extent of law enforcement access to Flock Safety surveillance. ... Whenever Gemini for Home accesses a Nest camera, the footage may be used for AI training purposes.



](https://www.cnet.com/home/security/googles-gemini-for-home-comes-to-your-camera-live-feeds-heres-what-that-means-for-privacy/?_gl=1*zs6zb1*_up*MQ..*_ga*ODUwMjIwMDUzLjE3ODM5Mzg4Mjk.*_ga_R820W8QX02*czE3ODQ2NjYwNzgkbzUkZzAkdDE3ODQ2NjYwNzgkajYwJGwwJGgxMTk5MDQ2OTUz#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/09/12

Apple’s Surveillance-First Strategy for the Smart Home - Advertisement

When iOS 27 arrives on September 14, 2026 ... We are inviting increasingly powerful AI models to process our most intimate visual data without the corresponding agent-level security infrastructure to manage them. While Apple emphasizes its privacy architecture-including on-device processing and end-to-end encrypted iCloud storage-the sheer volume of data being indexed by these new AI features is unprecedented.



](https://tech.yahoo.com/ai/apple-intelligence/articles/apple-surveillance-first-strategy-smart-165636582.html#1)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arXiv

“These cameras are just like the Eye of Sauron”: A Sociotechnical Threat Model for AI-Driven Smart Home Devices as Perceived by UK-Based Domestic Workers

“These cameras are just like the Eye of Sauron”: A Sociotechnical Threat Model for AI-Driven Smart Home Devices ... The growing adoption of AI-driven smart home devices has introduced new privacy risks for domestic workers (DWs), who are frequently monitored in employers’ homes while also using smart devices in their own households. ... AI-driven smart cameras ... detecting motion or recognizing a visitor’s face).



](https://ar5iv.labs.arxiv.org/html/2602.09239#3)[

![](https://cdn.deepseek.com/site-icons/zhiding.cn)

至顶网

2026/03/04

Google Gemini新增实时摄像头监控功能，用户隐私问题引关注

Google Gemini新增实时摄像头监控功能，用户隐私问题引关注 谷歌为Gemini家庭AI新增实时搜索功能，允许AI分析当前摄像头画面并回答相关问题。用户可询问"车道上有车吗 ... 新功能可能允许AI随时访问摄像头，且相关画面可用于AI训练，引发用户对隐私保护的关切 ... 录像可能会被用于AI训练目的。



](https://ai.zhiding.cn/2026/0305/3180352.shtml#1)[

![](https://cdn.deepseek.com/site-icons/house.gov)

House.gov

2026/02/26

Krishnamoorthi Raises Alarm Over Ring’s New AI “Search Party” Feature, Citing Privacy and Civil Liberties Concerns

2026 ... ” warning that the technology could expand neighborhood surveillance and threaten Americans’ privacy and Fourth Amendment protections. ... the use of AI to scan doorbell camera recordings raises serious privacy concerns related to the potential for mass surveillance of people and implications for 4th Amendment rights.”



](https://krishnamoorthi.house.gov/media/press-releases/krishnamoorthi-raises-alarm-over-rings-new-ai-search-party-feature-citing)[

![](https://cdn.deepseek.com/site-icons/forkast.news)

Forkast News

2026/07/27

Google Just Put a Price Tag on Your Camera’s Ability to See

A June 2026 survey from Reviews.org found that 65% of consumers are concerned about AI assistants, and 78% are willing to disconnect devices that collect too much data. ... If the “perception” being sold is consistently inaccurate, the subscription will eventually feel



](https://forkast.news/google-just-put-a-price-tag-on-your-cameras-ability-to-see/)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/06/01

Why Trust Is Becoming The Most Valuable Feature In Home Security - Advertisement

as 54% of those surveyed are worried about artificial intelligence and the impact on their sense of security and safety. ... prompting questions about how the data powering these devices is being handled and stored - with a particular concern about who has access to such intimate video footage. ... nearly 60% of consumers report being either extremely or very concerned about their privacy being violated by AI using their data.



](https://tech.yahoo.com/home/articles/why-trust-becoming-most-valuable-140000419.html#1)[

![](https://cdn.deepseek.com/site-icons/cnet.com)

CNET

2026/06/02

Amazon Ring Sued for Facial Recognition Technology: Here's Why It May Violate Privacy Laws - CNET - Skip to content

Amazon Ring Sued for Facial Recognition Technology: Here’s Why It May Violate Privacy Laws Ring's face-detecting AI is problematic ... On Monday, a Virginia man filed a class-action lawsuit against Amazon Ring, claiming its facial recognition feature violated his privacy and that of millions of other Americans. The lawsuit ... in home security devices. Google Nest and other companies have disabled familiar-face features there to avoid legal problems like the Ring lawsuit.



](https://www.cnet.com/home/security/amazon-ring-sued-face-ai-technology-violate-privacy-laws/?utm_source=memo-daily.beehiiv.com&utm_medium=referral&utm_campaign=scorsese-faces-backlash-for-ai-endorsement#1)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/01/20

Nuvon: An AI-Embedded Chatbot for Home Automation

Voice assistants are increasingly integral to smart homes and IoT ecosystems, but widespread cloud dependence in commercial assistants ... but widespread cloud dependence in commercial assistants like Amazon Alexa and Google Assistant leads to response latency, elevated power consumption, and privacy concerns. ... rapid response times under one second and recognition accuracy of approximately 85% in quiet and 72% in noisy environments.



](https://ieeexplore.ieee.org/document/11335749#1#1)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/06/25

Lightweight and Secure Real-Time Sensor-Text Grounding for Consumer AIoT Devices via Small Language Models

Consumer AIoT devices increasingly embed lightweight language model assistants for smart home monitoring, residential energy management, and consumer energy-awareness app...Show More ... 0.085 ms mean buffer latency (10.4× faster than Redis) ... 26 June 20



](https://ieeexplore.ieee.org/document/11584922)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/07/06

Development of Privacy Focused Voice Activated Offline AI Assistant for Home Automation

The high rate of technological developments in smart-home technologies has radically changed the residential living conditions by introducing automation ... they are also associated with very important issues related to information privacy, latency, reliability in operation, repetitive expenses ... and offline AI assistant to home automation ... 09-10 April 2026



](https://ieeexplore.ieee.org/document/11584725#1#1)[

![](https://cdn.deepseek.com/site-icons/kemdiktisaintek.go.id)

kemdiktisaintek.go.id

2026/04/01

Garuda - Garba Rujukan Digital

Across 33 IoT entities, the assistant reaches a 96.67% execution success rate with an average response time of 5.5 s. Among the evaluated local models ... The results demonstrate that privacy-preserving and resilient voice interaction for smart building management is feasible using current local LLM stacks.



](https://garuda.kemdiktisaintek.go.id/documents/detail/6144824)[

![](https://cdn.deepseek.com/site-icons/acm.org)

ACM Digital Library

2026/06/12

VCU-LLM: Prompt-efficient On-device Large Language Model for Vague Command Understanding in Smart Homes - Several features on this page require Premium Access

15 June 2026 Publication History ... current smart home assistant systems either control appliances solely through users' explicit commands or rely on cloud-based large language models (LLMs) for vague command understanding, which brings drawbacks such as high latency, privacy concern, and high cost. In this work...



](https://dl.acm.org/doi/abs/10.1145/3810190#1)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dlnext.acm.org

VCU-LLM: Prompt-efficient On-device Large Language Model for Vague Command Understanding in Smart Homes

Prompt-efficient On-device Large Language Model for Vague Command Understanding in Smart Homes ... current smart home assistant ... users' explicit commands or rely on cloud- based large language models (LLMs) for vague command understanding, which brings drawbacks such as high latency, privacy concern, and high cost. In this work ... 2026. ... (ii) Privacy concerns.



](https://dlnext.acm.org/doi/pdf/10.1145/3810190?download=true&__cf_chl_tk=vVMDzHrPTS1oSL_FGosDZgE8QFmKAo.J3ewUVKVZjbI-1784742082-1.0.1.1-1tLSgfZ_HZXl_fT.5UBDnk8vg0xRqxufkhaEb4Gxk0o#7#1)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

export.arxiv.org

AdaHome: An Adaptive Smart Home Assistant using Local Small Language Models

and raising privacy concerns. ... AdaHome achieves substantially higher accuracy on direct commands (86.7%) while reducing latency by up to 3x. Furthermore ... 2026. ... While effective, such designs introduce latency, require substantial computational resources, and raise privacy concerns [5, 22].



](https://export.arxiv.org/pdf/2607.18034#4#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/09/06

GitHub - distil-labs/distil-smart-home: Smart home assistant powered by an SLM · GitHub - GitHub - distil-labs/distil-smart-home: Smart home assistant powered by an SLM · GitHub

An on-device smart home controller powered by fine-tuned small language models (SLMs). Natural language commands are processed locally for private, low-latency smart home control — no cloud required. ... 2026 ... PRIVACY_POLICY.md| Add privacy policy and update privacy information for iOS| Apr 7, 2026



](https://github.com/distil-labs/distil-smart-home#1)[

![](https://cdn.deepseek.com/site-icons/xda-developers.com)

XDA

2026/09/20

My smart home finally answers me without the internet, and the model doing it runs on a mini PC - My smart home finally answers me without the internet, and the model doing it runs on a mini PC

On top of that, it means that commercial smart speakers suffer from frustrating multi-second latency lags and can be infected with unrequested shopping suggestions or ad-driven responses. ... This allows you to build a lightning-fast, private, 100% offline smart home voice assistant where you are in complete control of your data.



](https://www.xda-developers.com/smart-home-answers-me-without-internet-model-doing-it-runs-on-mini-pc/#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/09/03

Why Home Assistant Adds Background Intelligence - English

Why Is Home Assistant Adding More Automation and Background Intelligence ... Local Processing Protects Latency and Private Context Home context is unusually sensitive: presence ... Processing more of that context locally can reduce round trips and third-party disclosure while keeping basic actions available during internet loss. Locality...



](https://shop.zimaspace.com/blogs/tech-ai-hub/why-home-assistant-adds-automation-background-intelligence#1)[

![](https://cdn.deepseek.com/site-icons/zdnet.com)

ZDNET

2025/12/21

Best home automation systems 2026: As a smart home reviewer I rounded up the top ones - ZDNET - Skip to content

Bottom Line Why we like it ... Pros & Cons ... - Many devices work with Alexa - Alexa is responsive and smarter than others - Great speakers - App isn't as user-friendly - Limited video service ... - Great user interface - Reliable voice assistant - Strong automation power - Not much support with other brands yet - Features are rather basic ... Who it’s for...



](https://www.zdnet.com/home-and-office/smart-home/best-home-automation-system/?itm_source=parsely-api#1)[

The Tech Influencer

2025/11/02

Best Voice Assistants for Building a Smart House (2026)

Amazon Alexa | Largest device library and routines | Full on Echo 5th Gen and newer | Automation power users | Echo, Echo Show, Echo Hub Google Assistant | Context aware voice and Android synergy | Full | Cross device households | Nest Audio, Nest Hub Max ... Alexa averaged 1.9



](https://thetechinfluencer.com/best-voice-assistants-for-smart-house/)[

QuillBot vs TextCortex: Which Is Better?

2026/03/05

Best AI Voice Assistants 2026: Ranked for Every Device

The four leaders in 2026 are Amazon Alexa, Google Assistant, Apple Siri, and Samsung Bixby, with the right choice depending on the ecosystem you already use. - Choose Amazon Alexa if you run 10+ smart home devices and want the broadest hardware compatibility. ... Siri’s natural-language understanding still trails Google Assistant on complex queries...



](https://aiproductivity.ai/blog/best-ai-voice-assistants-2026/)[

![](https://cdn.deepseek.com/site-icons/wired.com)

WIRED

2026/04/27

Here’s How to Choose Which Smart Home Assistant Is Best for Your Home

Waffling between Alexa, Siri, and Google ... Amazon Alexa ... If you already have an iPhone, you can control your home with Siri, and ... In my house, we have all three of the device types mentioned in the article, and the Amazon and Google devices respond more quickly pretty consistently.



](https://www.wired.com/story/how-to-choose-your-smart-home-ecosystem/#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/09/09

The Quiet Corner of the Smart Home

000 devices compatible with Alexa, 85,000 with Google, and over 2,500 with SmartThings. Furthermore ... In 2026 reviewer testing, Siri is consistently rated as weaker than Google Assistant and behind Alexa in conversational AI capabilities.



](https://tech.yahoo.com/home/articles/quiet-corner-smart-home-101159136.html#1)[

![](https://cdn.deepseek.com/site-icons/forkast.news)

Forkast News

2026/08/20

One Year In, Your AI Voice Assistant Still Can’t Do Its Job

Consumer Reports found Alexa Plus controls were still buggy and the companion app was slower and less usable than Apple Home, Google Home, and Samsung SmartThings on Android. Two days ago ... Gemini for Home feels slower than the old Google Assistant, frequently cannot control devices it should know about...



](https://forkast.news/one-year-in-your-ai-voice-assistant-still-cant-do-its-job/)[

djEnterprises

Home Automation Platforms 2026: HomeKit, Google, Alexa, SmartThings, IFTTT

What it is: Apple's home platform ... What it gets right ... What it gets wrong: - Siri remains the weakest of the major voice assistants for general questions and for understanding accents under-trained for. ... Pick this if: you're an iPhone household ... Google Assistant > Alexa > Siri > Bixby.



](https://djenterprises.ai/blog/smart-home/home-automation-platforms)[

Home Auto Central

2026/04/05

Voice Assistants & Smart Home Protocols Guide

Amazon Alexa holds roughly 28% US market share, Google Home follows at 24%, and Apple HomeKit commands 12% — the rest split across SmartThings, open-source platforms, and regional players. ... Feature | Amazon Alexa | Google Home | Apple HomeKit



](https://homeautocentral.com/voice-assistants-smart-home-protocols-complete-guide/)[

smarthomegearreviews.com

2026/07/26

Alexa vs Siri vs Google Assistant : Which is Better? - SmartHomeGearReviews

Alexa vs Siri vs Google Assistant ... Alexa, Siri, and Google Assistant are the big three, and while they all promise to simplify your life, my experience shows they’re far from equal. I’ve wrestled with Echo Dots ... Alexa comes in a close second, handling similar commands with about 90% accuracy, but it sometimes stumbles on longer sentences or if there’s background noise.



](https://smarthomegearreviews.com/uncategorized/alexa-vs-siri-vs-google-assistant-which-is-better/)[

![](https://cdn.deepseek.com/site-icons/linkedin.com)

LinkedIn · Fabian Warislohner

2026/06/14

Electe的动态 - 跳到主要内容

Alexa+, Siri, and Gemini are all shipping next-generation voice assistants powered by stronger language models. ... We compared all three assistants not on model benchmarks but on ecosystem depth, device reach, and architectural openness. ... Apple leans on device control and privacy. ... Google leverages its data graph and cross-platform reach.



](https://www.linkedin.com/posts/electe_the-smartest-ai-in-the-room-loses-if-it-cannot-activity-7472211048863989760-B3Gh#1)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dlnext.acm.org

S10- 4 Concern - P10: "If you had little kids who were just learning how to use the smart lock, they could mess up more often an...

Several factors can lead to automation scenarios triggering incorrectly (false positives) or failing to trigger when needed (false negatives) ... We gathered participants' concerns regarding false positives and negatives across all 87 automation scenarios on a 5- point Likert scale where 1 corresponds to 'not concerned at all'



](https://dlnext.acm.org/doi/pdf/10.1145/3688459?download=true&__cf_chl_tk=o0Alrmxp8tZcV1LvEnNrfbAuutDxwlFgHvJyhIF2xdo-1781207458-1.0.1.1-voPlKigNQnyJBGcClnvs.Lswqs4T8hnVdTHxvr9qoIQ#125#45)[

![](https://cdn.deepseek.com/site-icons/acm.org)

ACM Digital Library

Exploring End Users' Perceptions of Smart Lock Automation Within the Smart Home Environment - For each of the scenarios created by the participants, we asked about how different factors might influence their willingness to...

Several factors can lead to automation scenarios triggering incorrectly (false positives) or failing to trigger when needed (false negatives), with some of these issues highlighted in the "automation concerns" section ... We gathered participants’ concerns regarding false positives and negatives across all 87 automation scenarios on a 5-point Likert scale where 1



](https://dl.acm.org/doi/fullHtml/10.1145/3688459.3688480#3)[

![](https://cdn.deepseek.com/site-icons/peasec.de)

peasec.de

The House That Saves Me? Assessing the Role of Smart Home Automation in Warning Scenarios

Key questions include whether user preferences for automation levels in smart homes are affected by different warning scenarios, and how unwanted automation or false positives influence acceptance. To explore this ... we find that specific safety protocols and handling of false positive alarms must be chosen carefully to avoid mistrust, users feeling a loss of control...



](https://www.peasec.de/paper/2025/2025_HenkelHaeslerAlNajmiHesselReuter_HouseThatSavesMe_IMWUT.pdf#8#1)[

![](https://cdn.deepseek.com/site-icons/europepmc.org)

europepmc.org

As mentioned earlier, successful classification of activity errors into predefined error types can provide better insight into t...

successful classification of activity errors into predefined error types can provide better insight into the changes dementia brings into one's daily life. Therefore, we first treat classification of errors as an independent problem to see how well these errors can be classified based on the sensor data obtained from the smart home when the everyday activities were performed by the participants. We perform a 5- fold cross validation of five commonly used classifiers on error samples labeled with error type classes.



](https://europepmc.org/articles/pmc5061461?pdf=render#3#3)[

![](https://cdn.deepseek.com/site-icons/springer.com)

Springer

2025/07/10

Threat detection in smart homes: A sociotechnical multimodal conversational approach for improved cyber situational awareness - This section presents the results of the study using the metrics stated in Section 4.2, namely usability and situational awarene...

suggesting false positive detections were present when using the visual method. ... Analysis of the data shows that false positive detections in particular contributed to the lower f-measure score (0.887) demonstrating that in some cases the participants had gathered the necessary information but had failed to comprehend its meaning...



](https://link.springer.com/article/10.1007/s10207-025-01051-x#4)[

![](https://cdn.deepseek.com/site-icons/peasec.de)

peasec.de

To address these aspects, we conducted a **mixed-methods** follow-up study, gathering data on **the perception of our prototype,...

we conducted a **mixed-methods** follow-up study, gathering data on **the perception of our prototype, false positives, and unwanted automation**. ... It can occur due to false positives (e.g., faulty sensors, public warnings), where the SHWS tries to protect residents from non-existent dangers.



](https://www.peasec.de/paper/2025/2025_HenkelHaeslerAlNajmiHesselReuter_HouseThatSavesMe_IMWUT.pdf#8#4)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2024/09/18

Doing cybersecurity at home: A human-centred approach for mitigating attacks in AI-enabled home devices - Despite having received training to use the helper tool only on A1, in all but one case, participants spotted A2 and therefore, ...

Nonetheless, most participants were not able to necessarily (or immediately) distinguish between the two attack types when prompted. ... It is also noteworthy that half the households identified between one and two false positive attacks, which we describe under RQ3. In these instances, participants used the



](https://www.sciencedirect.com/science/article/pii/S0167404824004176?fr=RR-2&ref=pdf_download&rr=a362d8d62eeb4032#4)[

![](https://cdn.deepseek.com/site-icons/cnr.it)

iris.cnr.it

Regarding user- related errors, the complex tasks resulted in the highest number overall (18), consisting of 16 WU and 2 UD, con...

AR Smart Home. ... (12) ... In the AR home scenario, the majority of system errors (63 out of 79, \(\sim 80\%\) ) occurred independently of preceding failures, while a smaller proportion (16 out of 79) were triggered by prior errors. Thus...



](https://iris.cnr.it/bitstream/20.500.14243/596682/1/published_End-user%20automation%20authoring%20in%20VR%20and%20AR%20through%20conversations%20%20patterns%20%20errors%20and%20user%20recovery%20strategies.pdf#14#6)[

![](https://cdn.deepseek.com/site-icons/charlotte.edu)

ninercommons.charlotte.edu

S2- 3 - Automation Scenario: IF trusted person identified in video doorbell and lock status is locked and no one is home THEN un...

False alarms are usually caused by false positives or triggering an automation scenario unintentionally. ... Participants highlighted concerns about the accidental triggering of automation scenarios due to human errors in 12 of the 87 automation scenarios. ... Several factors can lead to automation scenarios triggering incorrectly (false positives) or failing to trigger when needed (false negatives)...



](https://ninercommons.charlotte.edu/nanna/record/2923/files/Hazazi_uncc_0694D_13802.pdf?withWatermark=0&withMetadata=0&registerDownload=1&version=1#17#10)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dl.acm.org

Of particular interest are proposals to include limited control or access for children, short- term rental guests, or other type...

Of particular interest are proposals to include limited control or access for children, short- term rental guests, or other types of secondary users [e.g. ... researchers have proposed preset account types with defaults that represent common household configurations [10 ... such as child accounts [10 ... 70] or short- term rental guest accounts [51]...



](https://dl.acm.org/doi/pdf/10.1145/3703037?__cf_chl_tk=sVkoTHIyOBM8ygrhXsp.lCBunPDrlElkuJgks0NSQVE-1783679097-1.0.1.1-8fiPY3h1crQ.eN54IS0_NUtBuZOqDzDX0_iEz8Wi.Wc#page=83#95#14)[

![](https://cdn.deepseek.com/site-icons/uw.edu)

techpolicylab.uw.edu

<table><tr><td>All</td></tr><tr><td>• Anyone who is currently at home should always be allowed to adjust lighting<br>• No one sh...

school</td></tr><tr><td>• Elementary-school-age children should never be able to use capabilities without supervision</td></tr><tr><td>Visitors (babysitters ... and visiting family)</td></tr><tr><td>• Visitors should only be able to use any capabilities while in the house<br>• Visitors should never be allowed to use capabilities of locks, doors, and cameras<br>• Babysitters should only



](http://techpolicylab.uw.edu/wp-content/uploads/2018/10/rethinking_sec18.pdf?_x_tr_sch=http#5#3)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

在 Google Home 應用程式中管理使用者和權限 - 針對何項內容提供意見：

如果住家成員超過 6 人，請優先為需要特定控制項的使用者 (例如兒童或訪客) 設定 Voice Match，確保他們獲得適當體驗 ... - 如果住家中有兒童，部分 Family Link 監護工具將無法使用。



](https://support.google.com/assistant/answer/9155535?hl=zh-Hant&ref_topic=7658582#1)[

![](https://cdn.deepseek.com/site-icons/phonearena.com)

PhoneArena

2025/07/01

This new Google Home feature gives you more control over who gets access - This new Google Home feature gives you more control over who gets access

new Google Home feature gives you more control over who gets access You can now give kids and guests limited access in Google Home without losing control ... The first is for "Settings" access, which lets them manage device configurations and home-wide features like automations or Nest Wifi. The second is for "Activity" access ... This update also allows kids under 13 to use the Google Home app for the first time.



](https://www.phonearena.com/news/this-new-google-home-feature-gives-you-more-control-over-who-gets-access_id171921#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/09/18

GitHub - FezVrasta/ha-rbac: Role-based access control for Home Assistant. Guests see the lights, kids get their own dashboard, nobody sees where your phone is. · GitHub - GitHub - FezVrasta/ha-rbac: Role-based access control for Home Assistant. Guests see the lights, kids get their own dashboard, n...

Role-based access control for Home Assistant. Guests see the lights, kids get their own dashboard, nobody sees where your phone is. · GitHub ... Guests see the lights. Kids get their own dashboard. Nobody but you touches the locks, the add-ons, or the settings.



](https://github.com/FezVrasta/ha-rbac#1)[

![](https://cdn.deepseek.com/site-icons/springeropen.com)

jis-eurasipjournals.springeropen.com

This strategy ensures that the strictest privacy protections are applied to those who need them most, specifically children, by ...

This strategy ensures that the strictest privacy protections are applied to those who need them most, specifically children, by focusing on user vulnerability rather than solely on data sensitivity. ... the child profile as “Deny”, and the guest profile as “Ask the User”. ... Information Security (2025) 2025...



](https://jis-eurasipjournals.springeropen.com/counter/pdf/10.1186/s13635-025-00199-2.pdf#5#4)[

patentimages.storage.googleapis.com

[0038] According to embodiments, a guest-layer of controls can be provided to guests of the smart-device environment 30. The gue...

The smart remote control recognizes occupants by thumbprint ... and it recognizes a user as a guest or as someone belonging to a particular class having limited control and access (e.g., child). Upon recognizing the user as ... For example, a guest cannot adjust the digital video recorder (DVR) settings, and a child is limited to viewing child-appropriate programming.



](https://patentimages.storage.googleapis.com/5c/0a/03/f7160d2ce18d57/EP3266189B1.pdf#11#3)[

patentimages.storage.googleapis.com

**[0156]** In one example, the AI entry management device **10** receives an image from a device associated with the profile, an...

In one embodiment, there is a hierarchy of profiles, such that settings of an adult account overrule settings of a child account. For example, a child account includes a thermostat setting of 75 degrees for a living room, and an adult account includes a thermostat setting of 72 degrees for the living room.



](https://patentimages.storage.googleapis.com/5a/f9/e5/ea82509844608d/US20220114851A1.pdf#13#8)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/08/01

irokorobot/docs/architecture/identity-and-access.md at main · pipec80/irokorobot - Skip to content

Iroko must never assume that the current speaker is the configured owner. ... The current prompt can declare that whoever is speaking isowner_name, and voice interactions share voice-primary. That was useful for a single-user prototype but is unsafe in a household: a child, partner, guest, or distant speaker can inherit the owner's conversational context and receive owner data.



](https://github.com/pipec80/irokorobot/blob/main/docs/architecture/identity-and-access.md#1)[

patentimages.storage.googleapis.com

AI EM device grants access to a child account

The child account is permitted to access a study via unlocking of a smart lock associated with the study but a smart lock associated with a playroom is not unlocked in one embodiment. ... via an EM app) is operable to verify a child exercised for a predetermined period of time using wearable data (e.g.



](https://patentimages.storage.googleapis.com/fb/5e/f3/e09078f8eacb18/US11468723.pdf#17#12)[

Seedance AI – Reviews & Alternatives 2026

2026/04/29

Matter AI – Reviews & Alternatives 2026

Export anywhere Outputs in formats your existing stack already reads — no conversion step. ... ✓Output quality is consistently good enough to ship with light editing. ... Most users report the output quality is good enough to use with minor edits, saving meaningful time vs doing it manually.



](https://airudra.com/tool/matter-ai/)[

![](https://cdn.deepseek.com/site-icons/docs.rs)

Docs.rs

matterctl 1.28.0 - matterctl 1.28.0

pure JSON. mat is a command-line Matter controller built for scripts and AI agents, not apps. It speaks Matter directly — TLV ... Most ways to script Matter go through a hub ... - Built for scripts and AI agents. stdout carries exactly one JSON object per command ... The workspace shipsmatv, a virtual Matter device you can commission and control end-to-end on a laptop.



](https://docs.rs/crate/matterctl/1.28.0#1)[

![](https://cdn.deepseek.com/site-icons/dev.to)

DEV Community

2026/06/11

Voice Assistant Smart Home Routines 2025 - DEV Community

Thanks to Matter, AI‑enhanced assistants, and a handful of clever design patterns, you can now build routines that anticipate you instead of waiting for you to ask. ... Matter guarantees that a Hue bulb, a SmartThings hub, and an Aqara sensor can talk the same language. ... or Home Assistant with a Matter bridge Both support native Matter...



](https://dev.to/samchenreviews/voice-assistant-smart-home-routines-2025-45ie#comments#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/09/12

GitHub - nogu3/mat: Matter smart-home control CLI in pure Rust — from-scratch native controller, pure structured JSON output, built for scripts and AI agents · GitHub - GitHub - nogu3/mat: Matter smart-home control CLI in pure Rust — from-scratch native controller, pure structured JSON output, bu...

`mat` is a command-line Matter controller built for scripts and AI agents, not apps. It speaks Matter directly — TLV ... * **Built for scripts and AI agents.** ... * **Test without hardware.** The workspace ships `matv`, a virtual Matter device you can commission and control end-to-end on a laptop.



](https://github.com/nogu3/mat#1)[

![](https://cdn.deepseek.com/site-icons/jetbrains.com)

JetBrains

2025/10/08

About Matter | Matter

Matter is an AI-powered cloud tool that enables teams to prototype and test new ideas directly in their existing codebase without writing code. ... - Modify with plain language You can modify the application by entering simple text prompts. Matter interprets these instructions and applies the corresponding code changes automatically.



](https://www.jetbrains.com/help/matter/about.html#collaborate-with-teammates)[

SkillsMP

2026/04/11

smart-home | Agent Skill | SkillsMP

and troubleshoot smart home devices with protocol selection ... and ecosystem-agnostic automation patterns. ... Protocol choice matters more than brand. Matter and Thread are the future. ... Protocol comparison: Protocol | Range | Mesh | Power | Best for ... Matter | Good | Yes | Mains/Battery | New setups (2024+)



](https://skillsmp.com/creators/alvordhouse/wake-workspace/skills-smart-home)[

![](https://cdn.deepseek.com/site-icons/pingwest.com)

品玩

2025/01/06

J1 Assistant 新鲜上手体验，熟悉的罗永浩，熟悉的 AI 锤科味儿？-品玩 - 品玩

To Do（待办事项）、Notes（锤子便签加强版）、Jarvis（核心功能，自研 AI）、Chat（J1 Message 子弹短信加强版）、Search（集合搜索） ... 但好在文字输入支持中文，所以我们还是可以体验到它大多数核心的功能。



](https://www.pingwest.com/a/301494#1)[

티스토리

2026/02/06

IT 개발 블로그 - 기피말고깊이

Matter 2.0과 홈브리지를 통해 제조사와 관계없이 구형 가전부터 최신 센서까지 모든 기기를 하나로 연결합니다. ... 스마트홈 IoT 연동 기술인 Matter 2.0 표준과 Thread 네트워크 덕분에 브랜드 장벽이 사라졌습니다.



](https://notavoid.tistory.com/966)[

![](https://cdn.deepseek.com/site-icons/phandroid.com)

Phandroid

2025/01/19

J1 Assistant by Matter: A Personal AI Assistant for Scheduling To-Dos and Reminders - Phandroid - J1 Assistant by Matter: A Personal AI Assistant for Scheduling To-Dos and Reminders

The Beta version of Matter’s J1 Assistant is available to download on Android as an APK. While it works on most Android devices, as of writing, it’s currently optimized for the Samsung Galaxy S24 series, S23 series, S22 series, Google Pixel 9 series, Pixel 8 series, and Pixel 7 series.



](https://phandroid.com/2025/01/20/j1-assistant-by-matter-a-personal-ai-assistant-for-scheduling-to-dos-and-reminders/#mnmd-offcanvas-mobile#1)[

MosChip

2026/05/24

Edge AI-Driven Matter Controller for Next-Generation Smart Homes

The Matter standard is reshaping how connected devices work together, and true interoperability across different ecosystems is finally within reach. ... But a fully integrated ... the SDK can be deployed on non-Google mobile and embedded boards, which opens significantly more flexibility and portability across different environments.



](https://moschip.com/blog/device-software-engineering/edge-ai-driven-matter-controller-for-next-generation-smart-homes/)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/01/12

HARMONY: A Framework for Multimodal LLM-Powered AI Agents in Smart Homes via the Model Context Protocol - Table 3 presents sample outputs from different AI models responding to prompt commands, showcasing their tool calls and correspo...

showcasing their tool calls and corresponding actions for controlling smart home devices like TVs and air conditioners. ... Each model was tested with 20 independent runs per prompt under controlled settings: fixed temperature (0.7), maximum tokens (2048), identical MCP schemas, and deterministic device state replay from time-stamped simulator logs.



](https://ieeexplore.ieee.org/abstract/document/11348026/citations#citations#3)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/02/27

ha-voiceagent-llm-benchmark/reports/benchmark-run-analysis-2026-03.md at main · Drizzt321/ha-voiceagent-llm-benchmark

HA Voice LLM Benchmark Results — March 2026 Benchmark of 7 local LLMs for Home ... Qwen2.5 7B Q5_K_M is the most reliable choice at 72.5% accuracy with consistent, fast inference (~2.3s/sample). ... You are a voice assistant for Home Assistant. Answer questions about the world truthfully.



](https://github.com/Drizzt321/ha-voiceagent-llm-benchmark/blob/main/reports/benchmark-run-analysis-2026-03.md#1)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dlnext.acm.org

From Speech to Action: Home Automation Speech Ensemble (HASE) and an Open Pipeline for Smart-Home Control

8B ... On HASE, the best open stack reaches 0.778 EEM and 0.888 SMR, compared to 0.818 EEM and 0.910 SMR for the commercial baseline.



](https://dlnext.acm.org/doi/pdf/10.1145/3742414.3794721?download=true&__cf_chl_tk=mpGoejMod97l3nSJN8gI3uy7ASl3hufFK_8yTv6wq_s-1784421623-1.0.1.1-xPlDav1XfaW3HfK0Zfm5.MS..LpBcAkXwWW510YAq30#1#1)[

![](https://cdn.deepseek.com/site-icons/snu.ac.kr)

s-space.snu.ac.kr

creative commons C O M M O N S D E E D

SimuHome: A Temporal- and Environment-Aware Benchmark for Smart Home LLM Agents ... February 2026 ... We provide a challenging benchmark of 600 episodes across twelve user query types that require the aforementioned capabilities. Our evaluation of 16 agents under a unified ReAct framework reveals



](https://s-space.snu.ac.kr/bitstream/10371/233492/1/000000194948.pdf#8#1)[

![](https://cdn.deepseek.com/site-icons/obspm.fr)

Observatoire de Paris

2026/07/21

AdaHome: An Adaptive Smart Home Assistant using Local Small Language Models - 4. Evaluation

The human annotations were performed independently by members of the research team, following the same evaluation criteria provided to the LLM judge. The LLM-Judge achieves substantial agreement with human evaluation (Cohen’s), indicating that it provides a reliable proxy for human assessment in our setting.κ=0.834\kappa=0.834



](https://arxiv-org.ezproxy.obspm.fr/html/2607.18034v2#2)[

![](https://cdn.deepseek.com/site-icons/obspm.fr)

Observatoire de Paris

2026/05/31

SMH-Bench: Benchmarking LLM Agents for Environment-Grounded Reasoning and Action in Smart Homes

arXiv:2606.01912v1 [cs.AI] 01 Jun 2026 # SMH-Bench ... To address these limitations, we introduce SMH-Bench, a comprehensive benchmark for evaluating LLMs in smart-home environments. ... (2025)...



](https://arxiv-org.ezproxy.obspm.fr/html/2606.01912v1#1)[

![](https://cdn.deepseek.com/site-icons/acm.org)

ACM Digital Library

JavaScript disabled - From Speech to Action: Home Automation Speech Ensemble

We benchmark seven ASR back ends and ten instruction-tuned LLMs (up to 8B parameters) under few-shot ... On HASE, the best open stack reaches 0.778 EEM and 0.888 SMR, compared to 0.818 EEM



](https://dl.acm.org/doi/epdf/10.1145/3742414.3794721#1)[

![](https://cdn.deepseek.com/site-icons/vt.edu)

VTechWorks

2026/06/03

VTechWorks Home - Nova: Privacy-Preserving Goal-Oriented Reasoning in Smart Homes with On-Device Vision-Language Models

# Nova: Privacy-Preserving Goal-Oriented Reasoning in Smart Homes with On-Device Vision-Language Models ## TR Number ## Date 2026-06-04 ## Journal Title ## Journal ISSN ## Volume Title ## Publi



](https://vtechworks.lib.vt.edu/items/35140c44-22d6-441a-a5b0-52a7e26a8a9d#1)[

patentimages.storage.googleapis.com

The assistant provided by assistant modules **122** may determine whether the identified user is authorized to cause performance...

the unlock action to the lock of automation ... the front door, the assistant provided by assistant modules **122** may output a request to perform the unlock action to the lock of automation devices **106** associated with the front door. ... identified user is not authorized ... "I'm sorry, you do not appear



](https://patentimages.storage.googleapis.com/d7/64/45/f4ca027039fb36/US10438584.pdf#7#3)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/03/03

hello-claw/docs/en/university/smart-home-control/index.md at main · datawhalechina/hello-claw

High-risk devices (door locks, cameras, access control) will request confirmation before acting ... high-risk devices (door locks / cameras) must be confirmed first ... door lock / camera pending confirmation ... Require two-step confirmation for high-risk actions, and always keep a manual emergency kill switch available.



](https://github.com/datawhalechina/hello-claw/blob/main/docs/en/university/smart-home-control/index.md#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/03/03

hello-claw/docs/cn/university/smart-home-control/index.md at main · datawhalechina/hello-claw - Skip to content

高风险设备（门锁、摄像头、门禁）会先请求确认再动手 ... 2) 低风险设备可自动执行，高风险设备（门锁/摄像头）必须先确认 ... 高风险动作强制二次确认，同时保留人工紧急停用开关。



](https://github.com/datawhalechina/hello-claw/blob/main/docs/cn/university/smart-home-control/index.md#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Home Developers

2022/11/06

Secondary User Verification | Cloud-to-cloud | Google Home Developers

you can request that Assistant issue a challenge request to open a door if an NFC keyfob is not in the proximity of that door, but not issue a challenge if the keyfob is present. ... - TheOpenClose trait if the device type is DOOR, GARAGE, GATE, or



](https://developers.home.google.com/cloud-to-cloud/enhancements/secondary-user-verification?%3Bauthuser=1&hl=en)[

home-dot-devsite-v2-prod.appspot.com

2022/11/06

第二层用户身份验证 | Cloud-to-cloud | Google Home Developers

必须使用pinNeeded 质询类型进行第二层用户身份验证： - 如果设备类型为CAMERA，则为 OnOff 特征。 - 如果设备类型为DOOR、GARAGE、GATE 或 WINDOW，则为 OpenClose 特征。 - 解锁时的LockUnlock 特征。 - 解除或取消解除武装时的ArmDisarm 特征。



](https://home-dot-devsite-v2-prod.appspot.com/cloud-to-cloud/enhancements/secondary-user-verification?hl=zh-cn)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/04/11

Add policy enforcement for device control and automation tools · Issue #966 · homeassistant-ai/ha-mcp - Skip to content

This server exposes 86+ tools for controlling Home Assistant -- lights ... The security implications of an agent unlocking a door or disabling an alarm system are significant. ... "1" default: allow ... - action: require_approval ... providing AI agents with direct control over physical security devices (like locks and alarms) and system configurations (like automations and dashboards) without a "human-in-the-loop" for sensitive operations.



](https://github.com/homeassistant-ai/ha-mcp/issues/966#1)[

GitHub

{

Your Smart Home agent now has the power to unlock the front door and delete security logs. \n" ... For high-stakes actions, we need a **Human-in-the-loop (HITL)**. This means the agent must pause and ask for your permission before doing something sensitive.\n" ... If the user wants to open the door, respond with [ACTION: UNLOCK].\"\n"...



](https://raw.githubusercontent.com/learnwithparam/ai-agent-fundamentals-workshop/refs/heads/main/08-human-in-the-loop.ipynb#1)[

GitHub

Gates high-stakes tool calls (lock/alarm control, automation writes, etc

high-stakes tool calls (lock/alarm control, automation writes, etc.) behind explicit user approval. When a guarded tool is called, the agent is told to ask the user to open the Tool Security Policies tab in the web UI, and the call is held until the user clicks **Approve** there.



](https://raw.githubusercontent.com/homeassistant-ai/ha-mcp/master/homeassistant-addon/DOCS.md#2)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Home Developers

2022/11/06

Sekundäre Nutzerbestätigung | Cloud-to-cloud | Google Home Developers

Beispielsweise können Sie festlegen, dass Assistant eine Aufgabe zum Öffnen einer Tür ausgibt, wenn sich kein NFC-Schlüsselanhänger in der Nähe der Tür befindet. ... - Das MerkmalOnOff, wenn der Gerätetyp CAMERA ist. - Das MerkmalOpenClose, wenn der Gerätetyp DOOR, GARAGE, GATE oder WINDOW ist. - Das MerkmalLockUnlock beim Entsperren.



](https://developers.home.google.com/cloud-to-cloud/enhancements/secondary-user-verification?authuser=1&hl=de#supported_challenge_types)[

![](https://cdn.deepseek.com/site-icons/deepwiki.com)

DeepWiki

2026/06/06

Critical Action Guards | goruck/home-generative-agent | DeepWiki - Menu

This document describes the PIN-based authorization system that protects sensitive home automation operations from accidental or unauthorized execution. ... Critical Action Guards implement a two-step confirmation process for dangerous operations like unlocking doors, opening garage doors, and opening gates. When enabled, these actions require ... "lock", "service": "unlock"}...



](https://deepwiki.com/goruck/home-generative-agent/4.3-critical-action-guards#1)[

![](https://cdn.deepseek.com/site-icons/acm.org)

ACM Digital Library

2025/01/26

IUAC: Inaudible Universal Adversarial Attacks Against Smart Speakers | ACM Transactions on Sensor Networks - Several features on this page require Premium Access

27 January 2025 Publication History ... Intelligent voice systems are widely utilized to control smart home applications, which raises significant privacy and security concerns. ... In our work, we investigate a stealthy and command-independent attack that does not necessitate collecting victims’ voices. Our proposed attack, IUAC ... Our core concept is to train highly robust attack ... To achieve stealthy attacks, we



](https://dlnext.acm.org/doi/full/10.1145/3698238#1)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

export.arxiv.org

For "practical hidden voice" attack, we apply the same experimental setup as hidden commands

For "practical hidden voice" attack, we apply the same experimental setup as hidden commands. ... In over-the-air attacks, Google Home, Amazon Echo, and Cortana only recognize a few unintelligible speeches. ... we test the performance of FakeBob attack [33]. ... to attack the original target SV models. ... including Google Home, Siri ... _Adversarial Attacks Targeting ASR_ ... Google Home & Echo



](https://export.arxiv.org/pdf/2312.06010#6#4)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dlnext.acm.org

IUAC: Inaudible Universal Adversarial Attacks Against Smart Speakers

IUAC: Inaudible Universal Adversarial Attacks Against Smart Speakers ... Intelligent voice systems are widely utilized to control smart home applications, which raises significant privacy and security concerns. ... 2025. IUAC: Inaudible Universal Adversarial Attacks Against Smart Speakers. ACM Trans. ... inaudible...



](https://dlnext.acm.org/doi/pdf/10.1145/3698238?__cf_chl_tk=Q4LBmFiMAyBcfBU2mm4vyIRe4tpO55nkDIq4LlPs2hE-1778612383-1.0.1.1-dURGGzS2iS6NrvdJ7zNZsH3BtP9fxAAS0V0ucfuYd94&_x_output_type_b6db407c4_=embedded_pdf#4#1)[

![](https://cdn.deepseek.com/site-icons/cmu.edu)

users.ece.cmu.edu

* ***Open the Garage Door

***Open the Garage Door.** Finally, we show how an attacker can interact with additional systems which have been linked by the user to the targeted VC system. ... Command Generation.We have generated audio recordings of all four of the above commands using a common audio recording system (e.g., Audacity). ... all the devices are susceptible to laser-based command injection...



](http://users.ece.cmu.edu/~vsekar/Teaching/Fall21/18739/reading/lightcommands.pdf#5#3)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2024/09/11

Indelible “Footprints” of Inaudible Command Injection - Indelible “Footprints” of Inaudible Command Injection

of Inaudible Command Injection ## Abstract: Inaudible command injection transmits inaudible ultrasounds to inject adversarial speech commands into a voice assistant, therefore manipulating voice control systems (e....Show More ... therefore manipulating voice control systems (e.g., a garage door or a security camera) for illegitimate purposes.



](https://ieeexplore.ieee.org/abstract/document/10679153#1)[

![](https://cdn.deepseek.com/site-icons/cam.ac.uk)

repository.cam.ac.uk

In the case of audio- language systems, deploying them in noisy, uncontrolled environments introduces both challenges and opport...

This asymmetry – where an AI system “hears” a harmful command that the human does not – could be exploited in settings like voice- activated home devices (imagine a scenario where a TV broadcast contains a hidden audio attack that causes home assistants to malfunction or order products without the owner’s intent).



](https://www.repository.cam.ac.uk/bitstreams/a13d4a8b-4e83-4ce5-925b-e80c5c778f53/download#30#13)[

![](https://cdn.deepseek.com/site-icons/securityweek.com)

SecurityWeek

2026/06/03

Gemini Voice Assistant Hijacked via Messaging Notifications

Attackers could have triggered dangerous actions, including controlling smart home devices via Google Home and starting Zoom video calls. SafeBreach researchers uncovered a critical vulnerability in Google’s Gemini voice assistant that could have allowed attackers to hijack the AI using indirect prompt injections delivered through ordinary messaging notifications. ... including controlling smart home devices via Google Home, starting Zoom video calls...



](https://www.securityweek.com/gemini-voice-assistant-hijacked-via-messaging-notifications/#1)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

Showing 1-2 of 2 resultsfor "Index Terms":inaudible audio injection attacks

Inaudible command injection transmits inaudible ultrasounds to inject adversarial speech commands into a voice assistant, therefore manipulating voice control systems (e.g., a garage door or a security camera) for illegitimate purposes. Although the attack is inaudible ... Such attack “footprints” are the side product due to the interaction between the atta...Show



](https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=%22Index%20Terms%22:inaudible%20audio%20injection%20attacks)[

![](https://cdn.deepseek.com/site-icons/semanticscholar.org)

Semantic Scholar

2024/09/29

IUAC: Inaudible Universal Adversarial Attacks Against Smart Speakers | Semantic Scholar - IUAC: Inaudible Universal Adversarial Attacks Against Smart Speakers

Voiceprint Mimicry Attack Towards Speaker Verification System in Smart Home VMask is presented, a novel and practical voiceprint mimicry attack that could fool ASV in smart home and inject the malicious voice command disguised as a legitimate user.



](https://www.semanticscholar.org/paper/IUAC%3A-Inaudible-Universal-Adversarial-Attacks-Smart-Sun-Du/a8bf55245a56bfd81348f6c798f75652fec40eda#1)[

![](https://cdn.deepseek.com/site-icons/obspm.fr)

Observatoire de Paris

2026/08/05

PromptShield Home: Ambient Multimodal Prompt Injection Defense for Smart-Home Agents - License: CC BY 4.0

Smart-home assistants increasingly use multimodal large language models (MLLMs) that perceive video and audio directly. ... can the agent tell a genuine user command from ambient or externally-sourced content, television speech, on-screen text ... We introduce PromptShield-Home, a pilot benchmark of realistic smart-home scenarios spanning addressee ambiguity, screen/audio injection, health-monitor false triggers, mixed occupancy, and a legitimate-command floor...



](https://arxiv-org.ezproxy.obspm.fr/html/2608.05495v1#1)[

![](https://cdn.deepseek.com/site-icons/androidauthority.com)

Android Authority

2025/10/12

People think Google Home's latest feature might be in need of an exorcism - Best daily deals

Google recently launched a new Home Brief feature for Google Home that summarizes daily home activity using camera footage. - Some early users say the feature isn’t functioning accurately, reporting ghost sightings and misidentifying animals and objects. ... Overall, it looks like Home Brief is a feature that’ll improve in accuracy as more and more people start using Gemini for Home.



](https://www.androidauthority.com/google-home-home-brief-feedback-3606539/#1)[

![](https://cdn.deepseek.com/site-icons/tecnoandroid.it)

TecnoAndroid

2025/10/15

Google Home e il bug inquietante: Gemini “vede” persone che non esistono - Menu

Solo dopo ulteriori verifiche si è scoperto che si trattava di falsi positivi generati dall’AI. ... In diversi casi, Gemini for Home avrebbe semplicemente mal interpretato i movimenti o le ombre catturate dalle telecamere, scambiandole per persone o animali. Un utente ha raccontato...



](https://www.tecnoandroid.it/news/google-home-e-il-bug-inquietante-gemini-vede-persone-che-non-esistono-1642685/#1)[

![](https://cdn.deepseek.com/site-icons/arstechnica.com)

Ars Technica

2025/10/30

“Unexpectedly, a deer briefly entered the family room”: Living with Gemini Home - Skip to content

So unusual noises or conversations captured by your cameras will not be searchable or reflected in AI summaries. ... “Overall identification accuracy depends on several factors, including the visual details available in the camera clip for Gemini to process,” explains a Google spokesperson. ... It may be alarming at first, but after a few false positives, you grow to distrust the robot.



](https://arstechnica.com:8080/google/2025/10/unexpectedly-a-deer-briefly-entered-the-family-room-living-with-gemini-home/#comments#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2025/10/12

Google's new Home Brief feature is a hit for some, miss for others - Advertisement

It's been less than two weeks ... and it looks like the ... 'hallucinations.' ... which means that the Gemini-powered Home Brief feature essentially hallucinated the activities that it logged. ... Some users shared examples of highly accurate briefs, including the AI being able to highlight the make and model of cars that came and went by.



](https://tech.yahoo.com/ai/gemini/articles/googles-home-brief-feature-hit-122711839.html#1)[

![](https://cdn.deepseek.com/site-icons/canaltech.com.br)

Canaltech

2025/10/12

Update do Google Home é tão ruim que faz câmeras "verem fantasmas" - Publicidade

Update do Google Home é tão ruim que faz câmeras "verem fantasmas" ... Pensada para oferecer um resumo do que acontece nas câmeras de casa, a funcionalidade tem inventado informações e até criado fantasmas. Afinal, perfis relatam frequentes alertas falsos nas gravações, incluindo a detecção de pessoas que não existem.



](https://canaltech.com.br/casa-conectada/update-do-google-home-e-tao-ruim-que-faz-cameras-verem-fantasmas/#1)[

![](https://cdn.deepseek.com/site-icons/telepolis.pl)

Telepolis.pl

2025/10/14

Google zaczął trollować użytkowników. Lepiej nie wychodź z domu

Problem polega na tym, że AI niefortunnie interpretuje to, co "widzi" - szczególnie teraz, tuż przed Halloween. ... Gemini for Home generuje też znacznie poważniejsze błędy. System twierdził, że zarejestrował osobę chodzącą przy placu zabaw na podwórku, ale nagranie nie pokazywało nikogo. W innym przypadku AI raportowało obecność szopa pracza...



](https://www.telepolis.pl/tech/aplikacje/google-zaczal-trollowac-uzytkownikow-lepiej-nie-wychodz-z-domu)[

![](https://cdn.deepseek.com/site-icons/androidheadlines.com)

Android Headlines

2025/11/02

Google Gemini for Home AI Labels Pets as Deer - X

Google’s new Gemini for Home AI is struggling with accuracy, frequently misidentifying dogs as deer and sending false intruder alerts. ... early reports from users suggest that Gemini for Google Home system frequently misidentifies common household events ... After a few false positives, users quickly learn to distrust the system.



](https://www.androidheadlines.com/2025/11/google-gemini-for-home-ai-misidentification-deer-accuracy-issues.html#1)[

![](https://cdn.deepseek.com/site-icons/it-boltwise.de)

it boltwise

2025/10/30

Gemini für Zuhause: KI in der Smart-Home-Überwachung - LONDON (IT BOLTWISE) – Google hat mit Gemini für Zuhause eine neue KI-Integration für Smart-Home-Geräte vorgestellt

der Erkennung, die zu kuriosen Fehlalarmen führen können. ... Die KI analysiert dabei nur visuelle Elemente der Videos, was bedeutet, dass Geräusche oder Gespräche nicht in die Zusammenfassungen einfließen. ... Ein bemerkenswertes Problem, das bei der Nutzung von Gemini auftritt, ist die fehlerhafte Erkennung von Ereignissen. So kann es vorkommen...



](https://www.it-boltwise.de/gemini-fuer-zuhause-ki-in-der-smart-home-ueberwachung.html#respond#1)[

![](https://cdn.deepseek.com/site-icons/moneycontrol.com)

Moneycontrol

2025/11/09

Google’s Gemini makes smart homes smarter but still stumbles on basic common sense- Moneycontrol.com - In App

While it’s a leap forward for AI-assisted living, persistent misidentifications and overconfident summaries show that even Google’s smartest home still makes some very dumb mistakes. ... of what your Nest cameras saw ... However, Gemini’s accuracy isn’t always reliable. Its visual summaries often misinterpret scenes with overconfidence. In one case...



](https://www.moneycontrol.com/technology/google-s-gemini-makes-smart-homes-smarter-but-still-stumbles-on-basic-common-sense-article-13664390.html#1)[

SDMC Technology

2025/11/17

SDMC Unveils CedarHome Vision, Leveraging Google Gemini to Drive Subscription Revenue for Operators and Retail Brands

CedarHome Vision addresses the primary challenge of false alerts—a common problem for traditional cameras—by delivering a new level of intelligent understanding. ... 1. AI Video Descriptions ... Utilizing LLM to understand scene context, this feature reduces false alarms. ... Long, tedious surveillance videos are automatically distilled into a concise text summary.



](https://en.sdmctech.com/news/companynews_2043.html)[

patentimages.storage.googleapis.com

* [0127] The application framework is an execution environment in which application objects can send and receive data

In May, the CSA (Connectivity Standards Alliance) standards association introduced an IoT standard protocol called 'Matter'. ... [0134] Matter is an IP-based protocol that can run over existing network technologies such as Wi-Fi, Ethernet, and Thread.



](https://patentimages.storage.googleapis.com/dd/3b/ce/b63fa29440cbbd/US20240097901A1.pdf#5#4)[

![](https://cdn.deepseek.com/site-icons/wikipedia.org)

en.wikipedia.org

Matter (standard)

Matter is a technical standard for smart home and Internet of things (IoT) devices.[2][3][4] It is intended to improve interoperability and compatibility between different manufacturers and security ... Matter- certified products are engineered to operate locally and do not depend on an internet



](https://en.wikipedia.org/api/rest_v1/page/pdf/Matter_\(standard\)#2#1)[

Indigodomo

2026/08/18

indigo-matter

Opt-in per device, nothing exported by default, from a second managed process. Apple Home is validated end-to-end. Alexa pairs and controls too, with a known caveat: newly-exported accessories can show stale/unresponsive in Alexa for some minutes before converging (issue #143). ... Exporting Indigo devices (Matter out)



](https://www.indigodomo.com/pluginstore/333/#id3371)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2025/04/30

Moving HA (with Matter/Thread) from Bare Metal -> Virtualized - Configuration / Matter/Thread - Home Assistant Community - post by framerate on Apr 30, 2025

I want to understand how to move to a VM that is also on a different subnet (redoing my IP range at home) so if you have any pointers. Also, I read somewhere you might be able to export your thread config and restore it manually?



](https://community.home-assistant.io/t/moving-ha-with-matter-thread-from-bare-metal-virtualized/883730/5#1)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2025/11/26

What's the point of matter bridge add on - Configuration / Matter/Thread - Home Assistant Community - post by jakeshbazi on Nov 28, 2025

You can absolutely add , zigbee matter and other ... so you can export ha zigbee etc device(s) to homekit or other. ... You can make your non Matter devices into virtual Matter devices and if you have a Google or Alexa Matter hub in that Matter fabric...



](https://community.home-assistant.io/t/whats-the-point-of-matter-bridge-add-on/955979/2#1)[

PC CHIP

2026/07/14

“Matter” standard za pametni dom: kako napokon natjerati sve uređaje da rade zajedno | PC CHIP

bravu ili termostat s Matter certifikatom može kontrolirati bilo koja kompatibilna platforma – Apple Home, Google Home ... radi lokalno preko IP-a: naredbe putuju vašom kućnom mrežom, a ne kroz proizvođačev cloud, što znači brži odziv i uređaje koji nastavljaju raditi kada nema interneta.



](https://pcchip.hr/helpdesk/matter-standard-za-pametni-dom-kako-napokon-natjerati-sve-uredaje-da-rade-zajedno/)[

![](https://cdn.deepseek.com/site-icons/ajunews.com)

亜州日報

2026/09/12

サムスン電子、イケアとスマートシングス協力…生態系の拡張に拍車 | 亜洲日報

22日、サムスン電子のニュースルームによると、サムスンスマートシングスはイケアと協力し、開放型スマートホーム連動標準の「マター（Matter）ブリッジ統合サービス」を提供する。



](https://japan.ajunews.com/view/20240923114339696)[

![](https://cdn.deepseek.com/site-icons/hubitat.com)

Hubitat

2026/02/24

Matter controllers maybe fighting? - Built-In Apps and Drivers / Built-in Apps - Hubitat - post by greenall on Feb 25

this is a very well-known problem ... Now, as far as being unable to export a matter paired bulb from hubitat back again to to Apple home, I was actually able to do that. Here's what I did. ... only commissioned the bulb to one controller and then export it out via a bridge back to HomeKit. ... “Devices added to Hubitat via Matter are not supported ... After that, I then exported



](https://community.hubitat.com/t/matter-controllers-maybe-fighting/161954/7#1)[

PIXIE Partners

2026/05/06

Matter and Thread: the promise and the reality | Smart Home Explained Part 4 | PIXIE Partners

Part 1 explained why reliability is an architectural choice. Part 2 introduced the four-layer model. ... can be added to Apple Home ... Simpler certification means manufacturers can ship to multiple ecosystems with one engineering effort, which should bring more devices to market faster and at lower cost. ... Matter is a real and important industry move. It will get better.



](https://pixiepartners.com.au/matter-and-thread/)[

![](https://cdn.deepseek.com/site-icons/samsungmagazine.eu)

Samsung Magazine

2026/06/22

הכללים של הבית החכם משתנים. Matter גרסה 1.6 תבטיח צימוד פשוט ותסיים את הכאוס בין פלטפורמות - בית חכם אמור להיות כולו נוחות, אבל המציאות לרוב שונה - צימוד מכשירים מסובך, מעבר בין אפליקציות, וכיוונון אינסופי כדי לגרום למערכ...

זה יאפשר מערכות כגון Apple Home, Google Home a SmartThings מסמסונג יוכלו לנהל סביבה משותפת אחת ללא צורך בהתקנה חוזרת. ... הדבר החשוב הוא זה Matter הוא תקן עולמי, כך שהשינויים אינם מוגבלים לאזור אחד.



](https://samsungmagazine.eu/he/2026/06/23/meni-se-pravidla-chytre-domacnosti-matter-1-6-zajisti-jednoduche-parovani-a-konec-chaosu-mezi-platformami/#1)[

![](https://cdn.deepseek.com/site-icons/zenodo.org)

zenodo.org

Development and Implementation of a Local Mesh-Based Smart Home Automation System Using Home Assistant

most commercial smart home platforms depend on cloud infrastructure, leading to increased latency, higher deployment cost, vendor lock- in, and serious privacy concerns. ... achieves ultra- low communication latency below 10ms, reduces per- device cost below INR 1000 ... Latency Comparison Between Local and Cloud Systems </center>



](https://zenodo.org/records/19806288/files/IEEE_Journal_Paper_Template%20\(1\).pdf?download=1#1#1)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2025/11/12

LLMSwitchBench: A New Edge-Cloud Routing Benchmark for Smart Home LLM Inference

while cloud-based models, though powerful, raise privacy, latency, and cost concerns. ... LLMSwitch-router ... Experimental results show that LLMSwitch-router achieves a 48% reduction in LLM API cost while maintaining cloud-level accuracy, effectively optimizing the trade-off among performance...



](https://ieeexplore.ieee.org/document/11245478/citations#citations)[

Sensory

2026/02/17

The Smart Home Privacy Gap: Why Cloud Voice Fails Appliances | Sensory

Local vs. Cloud: Smart Home Comparison Aspect | Cloud Voice Risks | Sensory On-Device Wins ... Latency | Network-dependent (100ms+) | <60ms, always-on ... Cost | Recurring cloud/bandwidth fees | One-time integration, lower TCO



](https://sensory.com/blog-smart-home-privacy/)[

![](https://cdn.deepseek.com/site-icons/sohu.com)

手机搜狐网

2026/06/22

智能家居不用“喊一声动一下”，“AI家庭大脑”解决方案发布

核心是让AI算力扎根家庭本地，而非完全依赖云端计算。相比于纯云端方案，本地计算响应几乎无延时，设备操作响应更即时、交互更流畅；长期使用成本更可控，可避免大量调用云端模型产生的持续费用；更关键的是...



](https://www.sohu.com/a/1040062525_121332532?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.68.1782129118773Wwy3hdk&_trans_=000014_bdss_dkgyxqsP3p:CP=)[

![](https://cdn.deepseek.com/site-icons/ijcaonline.org)

ijcaonline.org

<table><tr><td>AI/ML Capability</td><td>Edge AI (on RPi); TinyML potential on ESP32</td><td>Cloud AI (powerful models, continuou...

TinyML potential on ESP32</td><td>Cloud AI (powerful models ... Crestron)</td></tr><tr><td>Latency</td><td>&amp;lt;200 ms (local processing)</td><td>&amp;lt;100 ms (wired)</td></tr><tr><td>Cost</td><td>Moderate ($99–$199 for hub)</td><td>High ($5...



](https://ijcaonline.org/archives/volume187/number133/mirza-ijca-2026-c41f28a210ba.pdf#2#2)[

![](https://cdn.deepseek.com/site-icons/doi.org)

doi.org

A Secure, Scalable, and Intelligent IoT-Based Smart Home Automation Framework Using Edge Computing for Real-Time Monitoring and ...

Researchers have consistently flagged high latency, bandwidth congestion, and privacy exposure as the three major weaknesses of cloud- centric smart home designs. And yet ... Our edge- based system responds in 46 ms. ... Scalability suffers because cloud costs grow linearly with device count, making it expensive to deploy across large homes



](https://doi.org/10.17148/ijarcce.2026.156113#3#1)[

foresthub.ai

2026/03/31

Edge AI vs Cloud AI: When to Use Which | ForestHub

Latency | 1-300 ms | 100-2000 ms (network dependent) ... Per-inference cost | $0 (hardware is sunk cost) | $0.001 - $0.10+ per call Hardware cost | $2-80 per device | $0 per device (cloud subscription)



](https://www.foresthub.ai/resources/guides/edge-ai-vs-cloud-ai)[

ecice06.com

3.2 边缘服务与云服务结果对比

基于个人计算机的边缘服务相比云服务最直接的优势是低延迟和高带宽，在家庭局域网内，本地服 ... 可以保证足够低的延时和足够高的带宽，而云服务一般由大型的数据中心提供，在空间上远离用户，延时会相对较高，同时带宽也会相对较低。



](https://www.ecice06.com/CN/article/downloadArticleFile.do?attachType=PDF&id=28127#2#2)[

intenv.org

2026/09/01

Edge vs cloud: where the computing happens

the cloud gives you scale, storage and heavy models; the edge gives you speed, lower running costs, better privacy and something that still functions offline. Sensible systems put fast ... The trade-offs, side by side Consideration | Edge (on-device / local hub) | Cloud (remote servers) ... Works during an outage | Yes, for ... Running cost | Low bandwidth; upfront hardware | Low hardware...



](https://www.intenv.org/guides/edge-vs-cloud/)[

![](https://cdn.deepseek.com/site-icons/github.com)

github.com

Ammu & Mycroft at Home: A Living, Breathing House that Learns Routines\*

Smart- home assistants have become widely available, but most consumer systems are either cloud- dependent (raising privacy, cost, and latency concerns) or local- first but brittle (struggling with natural dialogue, multilingual speech, and culturally grounded phrasing). ... What is the on-premise energy cost of local fallback inference compared with a cloud-routed pipeline?



](https://github.com/kiranvenom1209/Ammu-AI/blob/main/ArXiv_Home_assistant.pdf#2#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Google Home 和 Nest 隱私權專區 - Home 內建 Gemini 語音助理偵測到啟動指令後，就會退出待機模式，並將你的要求傳送到 Google 伺服器

升級為 Home 內建 Gemini 後，住家中所有人 (包括孩子) 都能使用語音助理。這項功能適用於所有相容裝置 ... 你可以設定篩選器，限制 Home 內建 Gemini 回覆敏感主題，適用對象為訪客或家中所有人。無論你選擇哪種篩選器...



](https://support.google.com/googlenest/answer/9415830?hl=zh-Hant&authuser=2&ref_topic=7173611&co=GENIE.Platform%3DiOS#3)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Google Home 和 Nest 私隱控制中心 - Home 專用 Gemini 語音助理會一直在待機模式下候命，直至偵測到啟動指令 (例如聽到「Ok Google」)

升級至 Home 專用 Gemini 後，家中所有人 (包括子女) 均可享用語音助理。此功能適用於所有兼容的裝置 ... 對於適用同意年齡以上的青少年使用者，「住宅記錄」控制項會預設關閉，而適用同意年齡以下的使用者和訪客使用者則無法使用此控制項 ... 家中所有人 (包括兒童和訪客) 均可使用 Home 專用 Gemini 語音助理。請注意...



](https://support.google.com/chromecast/answer/9415830?hl=zh-HK&co=GENIE.Platform%3DAndroid#3)[

![](https://cdn.deepseek.com/site-icons/acm.org)

ACM Digital Library

2024/06/24

Circles of Trust: A Voice-Based Authorization Scheme for Securing IoT Smart Homes | Proceedings of the 29th ACM Symposium on Access Control Models and Technologies - Several features on this page require Premium Access

This concept can be applied to an authorization framework, by linking relationships to an access level, e.g., homeowners and their spouses can be fully-trusted, whereas visitors and children may not. ... and therefore has access to every single device within a smart home via voice commands. Each subsequent layer has fewer access privileges than the previous, granting users in outer layers, like visitors...



](https://dl.acm.org/doi/abs/10.1145/3649158.3657044#1)[

patentimages.storage.googleapis.com

It may be desirable for the system to limit operation of skills and/or specialists depending on the identity of the user

For example, the system may be configured with a smart ... The system may ... the system may be configured to allow certain operations to be initiated by adults, while limiting operations that can be initiated by children (e.g., those under the age of eighteen or some other configurable age threshold).



](https://patentimages.storage.googleapis.com/35/bd/ee/6bb38c0948a22a/US10567515.pdf#9#3)[

![](https://cdn.deepseek.com/site-icons/scilit.com)

Scilit

2024/06/23

Circles of Trust: A Voice-Based Authorization Scheme for Securing IoT Smart Homes

This concept can be applied to an authorization framework, by linking relationships to an access level, e.g., homeowners and their spouses can be fully-trusted, whereas visitors and children may not. ... Each subsequent layer has fewer access privileges than the previous, granting users in outer layers, like visitors, limited capabilities to manipulate devices.



](https://www.scilit.com/publications/5d9fadb151852d6f98b588e3510c5b66)[

patentimages.storage.googleapis.com

In response to determining that the voice command was received from a child, some embodiments may prevent one or more playback d...

response to determining that the voice command was received from a child ... the computing device of the media playback system may (1) assign a restriction setting for the guest user, (2) configure an instruction for one or more playback devices based on content from the voice command and the assigned restriction setting for the guest user...



](https://patentimages.storage.googleapis.com/c3/dd/c5/4633811a7fbd5c/US10740065.pdf#12#6)[

![](https://cdn.deepseek.com/site-icons/androidcentral.com)

Android Central

2025/07/02

Google Home's new feature lets you call the shots on who controls your devices - YOUR NEXT READ:

The Member role supports inviting a wide range of individuals—children, guests, and roommates—for more tailored and manageable access. ... The new Member role lets you invite just about anyone—kids, roommates, even guests—so you can manage access to your smart home devices without the chaos. As usual...



](https://www.androidcentral.com/accessories/smart-home/google-home-makes-it-even-easier-to-share-your-smart-home-devices-with-others#1)[

patentimages.storage.googleapis.com

[0180] Next, method 800 advances to block 806, which includes in response to determining that the wakeup word was received from ...

additional voice commands for a time period or window to control one or more PBDS 532 ... In yet another example, the wake up word received may be associated with restriction settings for a child. Many other examples ... In other embodiments, an adult may close or key off the time period or window before it expires if the registered guest is a child. Many other examples...



](https://patentimages.storage.googleapis.com/51/10/a4/a0680f09ad97e1/US20210026595A1.pdf#8#8)[

rayuela-h2020.eu

Leaving aside more sophisticated attacks like KNOB or BIAS, both feasible due to the Bluetooth version implemented by the device...

Payments or purchases from the HomePod Mini are not supported.- Possibility of creating "safe" profiles for minors. ... There is no possibility to differentiate between users or to define permissions for specific interactions.- Interaction with third-party skills. ... code.- Possibility of creating "safe" profiles for minors. There is no dedicated option to set a safe profile for minors.



](https://www.rayuela-h2020.eu/wp-content/uploads/2022/10/Attachment_0-3.pdf#8#4)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2025/05/04

A User Personalized and Adaptative Smart Home using Large Language Models

This paper presents an advanced smart home system that leverages Large Language Models (LLMs) to significantly enhance home automation ... A voice assistant listens to user feedback, allowing the LLM to dynamically update user preferences and adapt system behavior. Managing user preferences significantly improves the reactions of the system in a range of experimental scenarios.



](https://ieeexplore.ieee.org/document/10975953/citations?tabFilter=papers#citations)[

Josh.ai

2026/03/18

Josh.ai Keynote 2026: Home in Harmony Showcases a New Era of Adaptive Home Control

Users can pin their most important devices front and center, with each household member able to customize their own layout. ... - AI-Guided Scene Creation: Josh.ai actively recommends and generates scenes based on a home’s layout, connected devices, and a user’s living patterns.



](https://josh.ai/stories/joshai-keynote-2026-home-in-harmony-showcases-a-new-era-of-adaptive-home-control)[

![](https://cdn.deepseek.com/site-icons/theverge.com)

The Verge

2026/09/02

Now you can tell the Hue app how you want your smart lights to work - Skip to main content

Now you can tell the Hue ... Philips Hue’s automation engine gets an AI makeover, and its buttons and switches will control your Sonos speakers. ... Philips Hue’s AI assistant can now build automations based on natural language, letting you describe what you want your lights to do. The feature...



](https://www.theverge.com/tech/988953/philips-hue-smart-lighting-custom-ai-behaviors-sonos-integration#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/06/10

zenos-ai/README.md at 4ca464d642828d4ba9bcddfa069d070d507225d6 · nathan-curtis/zenos-ai - Skip to content

Friday’s ZenOS-AI Modular AI Home Automation Core for Home Assistant ZenOS-AI blends structure, context-awareness, and modular AI into one delightfully over-engineered package. ... - Privilege model (public → guest → partner → owner → prime) ... - Governance drawer with persona-level access - Consistent metadata for drawers/volumes - Household → User → AI cascade



](https://github.com/nathan-curtis/zenos-ai/blob/4ca464d642828d4ba9bcddfa069d070d507225d6/README.md#1)[

heise online

2026/07/06

Agentic AI for Smart Homes: openHAB 5.2 brings Chat Interface and MCP Server

The open-source platform openHAB ... AI agents can control and manage devices. Furthermore, AI agents can be used to create custom rules for openHAB. Users can choose between rules for recurring tasks and one-time rules. The agent automatically deletes the latter after execution.



](https://www.heise.de/en/news/Agentic-AI-for-Smart-Homes-openHAB-5-2-brings-Chat-Interface-and-MCP-Server-11356314.html#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/03/11

GitHub - SeloraHomes/ha-selora-ai: Your smart assistant to manage and maintain your home. · GitHub - GitHub - SeloraHomes/ha-selora-ai: Your smart assistant to manage and maintain your home. · GitHub

Selora AI is a smart-home AI butler for Home Assistant. ... **AI Automation Suggestions** | Analyzes device states and history, then writes draft automations (disabled, prefixed `[Selora AI]`) for your review. ... **Automation Versioning** | Full version history for every Selora AI automation, with diff viewer in the panel.



](https://github.com/SeloraHomes/ha-selora-ai#1)[

![](https://cdn.deepseek.com/site-icons/ifeng.com)

凤凰网科技

2025/11/13

小米发布智能家居未来探索方案Xiaomi Miloco

基于大模型独特的开发范式，用户可以跟智能家居系统对话沟通，经过大模型的推理计算，自动完成家庭生活中的各类智能需求和规则 ... 口语化表达需求，Agent调用工具自动创建规则 ... 对话 模型管理 云端服务管理 MCP服务管理



](https://tech.ifeng.com/c/8oH6iu64kLV)[

![](https://cdn.deepseek.com/site-icons/lnu.edu.ua)

Львівський національний університет імені Івана Франка

2025/10/30

MODULAR APPROACH TO BUILDING A HARDWARE-SOFTWARE PLATFORM FOR SMART HOME AUTOMATION: FROM SIMPLE RULES TO INTELLIGENT SCENARIOS - Electronics and information technologies / Електроніка та інформаційні технології

This article addresses the challenge of creating flexible, scalable, and user-adaptive automation systems that can evolve in response to changing needs and technological advancements. The research focuses on developing an IoT-oriented smart home automation system designed for intelligent self-adjustment based on environmental conditions and remote device control.



](https://publications.lnu.edu.ua/collections/index.php/electronics/article/view/4941/0#1)[

heise online

2026/09/02

Philips Hue startet Automatikbau per KI-Bot, bringt Backups und steuert Nanoleaf - zurück zum Artikel

Philips Hue startet Automatikbau per KI-Bot, bringt Backups und steuert Nanoleaf ... Der hauseigene KI-Sprachassistent erstellt komplexe Wenn-Dann-Automatiken für Lampen und Sensoren. ... Damit lassen sich per Textchat oder auf Zuruf ans Smartphone-Mikro Automatiken mit mehreren Auslösern und Aktionszielen erstellen.



](https://www.heise.de/news/Philips-Hue-startet-Automatikbau-per-KI-Bot-bringt-Backups-und-steuert-Nanoleaf-11439211.html?view=print#1)[

![](https://cdn.deepseek.com/site-icons/huggingface.co)

Hugging Face

2026/09/13

selorahomes/Selora-AI-LLM-1.7B · Hugging Face - Selora Homes: selorahomes

Selora AI is an instruction-tuned language model for Home Assistant, the open-source smart home platform. It ships in two forms ... - Chat control of smart-home devices — "turn off the kitchen lights", "set the thermostat to 68", "open the garage door" — resolved against live Home Assistant entity state. - Natural-language home automation creation — describe an automation



](https://huggingface.co/selorahomes/Selora-AI-LLM-1.7B?local-app=pi#1)[

patentimages.storage.googleapis.com

[0140] 其中，授权提示在通知用户输入授权信息的同时，也将现在存在读取该敏感日志的操作，这样，如果确实是用户在读取该敏感日志，则用户可以输入表征该用户身份的信息，以完成授权；读取敏感日志的日志读取指令不是该用户发出的指令，则用户可以不输入身份信息，从而...

[0141] S503，在获得该智能家居设备的用户输入的授权信息且该授权信息携带有该用户的私钥的情况下，利用该私钥对该加密的日志进行解密，得到解密出的日志 ... [0145] 可以理解的是，为了保证加密的敏感日志的安全性 ... 在用户提供授权信息的同时，可以提供解密该敏感日志的私钥



](http://patentimages.storage.googleapis.com/1c/cd/74/ba2e0d428d187c/CN110719203A.pdf#3#3)[

stirlab.org

Enhancing Transparency Through Shared Users' Activity Logs

The Home Assistant platform introduces customizable logging through include and exclude filters, allowing homeowners to tailor log entries to their preferences, thus ... As such, the majority of smart home systems we reviewed provide options to log comprehensive activities of shared users, which contributes to enhancing transparency. At the same time...



](https://stirlab.org/wp-content/uploads/Alghamdi-et-al2024.pdf#4#3)[

patentimages.storage.googleapis.com

[0272] 在执行步骤S109之后,第一用户可在授权他人使用界面30触摸授权记录控件305查看上述步骤S101~S110对应的授权他人使用的历史记录

[0275] 在一种可能的实现方式中,第一用户可通过触摸授权记录查看该授权记录的详细信息,例如开始授权时间、结束授权时间、授权码等 ... [0277] 如果用户忘记了上述授权记录,可通过该授权记录详情界面60来查看授权记录详情。



](https://patentimages.storage.googleapis.com/33/a0/33/968ccf9ee121a6/CN110336720B.pdf#10#8)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

ec.europa.eu

- ViewUsers with View rights can only view a shared device without permission to modify or use it

ViewUsers with View rights can only view a shared device without permission to modify or use it.- View and editView and edit rights give user permission ... features users are permitted to access- ... Overview of the network and its connected devices- Event log presenting all the activities recorded by the devices- Edit saved Wi- Fi networks- Remove saved data



](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5efff0467&appId=PPGMS#8#4)[

![](https://cdn.deepseek.com/site-icons/mdpi-res.com)

mdpi-res.com

Blockchain technology is a decentralized, distributed ledger system that enables secure and transparent recording of transaction...

By integrating blockchain into Federated Learning (FL), we introduce a tamper-proof mechanism for managing access control and ensuring trust among devices. The blockchain-based Role-Based Access Control (RBAC) mechanism enhances collaboration by authenticating devices and providing a secure, transparent record of model contributions. ... To uphold the integrity of the learning process, blockchain provides an immutable audit trail for all model updates and interactions.



](https://mdpi-res.com/d_attachment/smartcities/smartcities-08-00035/article_deploy/smartcities-08-00035-v2.pdf?version=1739866612#6#3)[

![](https://cdn.deepseek.com/site-icons/socket.dev)

Socket

2026/04/17

@pshkv/bridge-homeassistant - npm Package Security Analysis ... - New:Socket for Asana Is Now Available

Every AI agent action on smart home devices—from turning on lights to unlocking doors—flows through graduated approval tiers with tamper-evident audit logging. ... - Tamper-evident audit — all decisions logged in Evidence Ledger with SHA-256 hash chain



](https://socket.dev/npm/package/@pshkv/bridge-homeassistant#1)[

sifis-home.eu

- SE-09: The information about the registered devices, their characteristics and their

The information about the registered devices, their characteristics and their configurations should be stored in a protected database. ... The information about user profiles and configuration aspects should be stored in a protected database. ... Data confidentiality shall be ensured all the time. ... Access to devices functionalities should be protected and controlled.



](https://www.sifis-home.eu/wp-content/uploads/2022/06/D6.1-Pilot-Use-Case-Requirements.pdf#5#5)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2026/04/24

Enhancing smart home forensics: An emulation-based approach utilizing vendor privileged android backup data - Skip to main contentSkip to article

This paper presents a smart home app forensics method based on Android emulation. This approach does not



](https://www.sciencedirect.com/science/article/abs/pii/S2666281726000636#1)
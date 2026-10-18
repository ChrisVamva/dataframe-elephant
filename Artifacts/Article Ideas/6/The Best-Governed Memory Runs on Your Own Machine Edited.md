# The Best-Governed Memory Runs on Your Own Machine

*The richest agent memory we found ships with the strongest controls — and it runs on your own hardware.*

There is a file on your computer called `MEMORY.md`. If you run one of a small number of open-source AI agents, an agent wrote it about you: that you prefer tabs over spaces, that you're rebuilding a kitchen, that you asked the same question three days in a row. It is plain text. You can open it, read every line, edit it, or delete it.

The agent that keeps it, Hermes, can be told to ask permission before it saves each note to itself — and when it overwrites one, it shows you, in full, what it overwrote. That combination of rich memory and real control wasn't where we expected to find it: not in the products with the biggest user bases, but in the two agents you run on your own hardware.

Our question was simple: what do AI agents actually remember, and who controls that memory? We compared the documented behaviour of roughly thirty products and services — coding tools, consumer assistants, enterprise platforms, and local-first personal agents — against product documentation, privacy regulation, and a fast-growing security literature. The finding inverts the usual assumption. Memory's governance gap is real, but it is a property of *cloud* memory, not of memory itself: the agents with the richest, longest-lived memory and the least central control turned out to ship the best controls in the survey. Control tracks where the memory physically lives. Once you know that, "does it remember?" stops being the useful question. The useful one is: where does that memory sit, and who can see it?

## What the local agents actually keep

The two best-governed systems in the survey are the two you host yourself — and they get there by an unfashionable route: plain files.

Hermes, open-source and free to inspect, keeps its memory as bounded Markdown on disk — `MEMORY.md` for the agent's own notes, `USER.md` for a profile of you, plus a full-text index of every session it can search later. There is no vector database or knowledge graph in its core; the notes *are* the memory. The agent writes them continuously — memory is on by default — but the documentation offers something no cloud product we reviewed matches: an approval queue. You can list the writes waiting for review (`/memory pending`), approve or reject them one by one or all at once, and turn the queue on or off by command. Background writes the agent makes on its own are tagged `[auto]` so you can see which is which. And when you approve a batch, the documentation says it lists the full text of every entry it overwrote or removed — a memory change log, printed on demand. A write is even refused if the target changed after it was staged.

The other local-first agent, OpenClaw, gets to a similar place through structure rather than an approval desk. Its docs are blunt about the design: "there is no hidden state." Memory lives in the workspace — `MEMORY.md`, daily notes dated by the day, an optional `USER.md`, a `DREAMS.md` distilled by a background pass — in files you can read with any text editor. The default engine is a local SQLite index, the networking gateway binds only to your own machine by default, and there is no subscription and no hosted tier. Before the agent compacts a long conversation it flushes what matters to disk first, so the summary is written down rather than silently replacing the raw conversation. You can open an incognito thread that writes no transcript and skips the memory flush entirely — a twenty-four-hour window the agent keeps nothing from — and ordinary chats are scoped per conversation, with cross-conversation recall an opt-in switch rather than a default.

Both agents are opinionated in the same direction: the memory belongs to the person who owns the machine.

## The cloud default is the opposite

Now picture the same feature in a mainstream assistant, and the picture flips.

Microsoft's Copilot keeps its saved memories in your Exchange mailbox, in a hidden folder. According to Microsoft's own documentation, the feature is on by default — "no action is required" — and three sentences in the same document carry the weight of this entire article: admins "can't restrict what type of information is added," the company's Purview retention policies "don't apply" to it, and memory actions "don't generate audit log entries." The memory layer sits, by design, outside the controls that govern everything else in the product.

The other big assistants soften the same edges rather than removing them. ChatGPT's support pages state that turning memory off does not delete your past chats, that OpenAI may keep logs of deleted saved memories for up to thirty days, and that deleting a saved memory does not remove mentions of that information from your past conversations — deletion removes the note, not the trace. Anthropic documents viewing and editing your Claude memory and calls it "fully optional, with granular user controls," but no explicit delete control appears on the page we reviewed. Google's saved instructions for Gemini only apply with memory switched on, and retention windows are measured in months. None of this is sinister. It is simply the default of a system whose memory lives in someone else's building, and whose change history you were never promised.

> **The whole story in two sentences from the vendors' own documentation.** Microsoft: Copilot memory actions "don't generate audit log entries." Hermes: its approval command "lists the full text of every entry it overwrote or removed." Same user need. Opposite governance.

## The enterprise tier already has the primitives

Between the two extremes sits the tier that can pay for controls — and it shows the gap is not technical.

AWS Bedrock's AgentCore memory separates what an agent remembers within a session from what persists across sessions. Google's Vertex AI Memory Bank keeps a revision history of each memory under the usual identity, network, and encryption controls. Azure AI Foundry's agent memory, in preview, goes furthest: per-memory create, read, update, and delete; a store-wide expiry in seconds; direct "remember" and "forget" operations; and quotas — a hundred scopes per store, ten thousand memories per scope, sessions cleaned up after thirty idle days. These are the primitives a governance fix would be built from, and the enterprise platforms already ship them.

Read the three tiers together and a ranking appears — ours, not any vendor's: the local-first agents offer the most control, the enterprise platforms offer programmatic control, and the consumer assistants offer the least. That is the opposite of how the same products rank on capability. If you were told the more powerful the agent, the weaker your grip on it, this survey is the counter-example.

## The catch: your machine is also your attack surface

Self-hosting is not safe by default. The same agents with the best controls are also named targets of the newest poisoning research, and the same survey that supports the inversion documents the threat.

Memory is now a named, benchmarked attack class. Security researchers have shown that a poisoned memory can survive with a poison rate under a tenth of a percent and still succeed more than eighty percent of the time, that attacks can work through ordinary questions with no injected instructions at all, and that behaviour drifts across sessions from implanted "experiences." OpenClaw — one of our two best-governed agents — is the named target of one such study, which reports an 81.3% save rate and a 75.0% success rate when a malicious goal is split into individually harmless fragments, surviving the dilution defences tested. A second paper frames continuously running, skill-augmented agents like OpenClaw as exposed to skill poisoning and cascading failures between agents. And Hermes' own security pages are candid: its eight-layer protection model, which includes keeping sessions from reaching each other's data, is "not a hard boundary."

Two honest caveats travel with those numbers. First, they are lab results from very recent papers, not measurements of attacks happening in the wild — we found no disclosed real-world incident of memory poisoning or cross-tenant leakage anywhere, and the work is too new to call replicated. Second, recall the Hermes approval queue: it defaults to off. The best write-review mechanism in the survey ships switched off, which means the protection exists and is latent — a default, not a dead end.

## What we don't know

- **Almost everything product-side is the vendors' own account.** The documentation is the only public description of each product's memory, so nearly every product claim in this article rests on a company's word — accurate as of our October 2026 review, but not independently tested.
- **The local agents have the weakest independent evaluation.** Hermes' only published memory benchmark we could find is the company's own; OpenClaw's independent coverage is largely its attackers. Good controls are not the same as validated controls.
- **The security numbers are fresh and unreplicated.** The poisoning and leakage figures come from 2026 papers that predate any outside reproduction; treat them as the direction of the field, not settled rates.
- **No real-world incident rate exists to cite.** Everything above is benchmark work.
- **Deletion across layers is unresolved.** Privacy researchers and Europe's lawmakers are still working out how an erasure request reaches the summaries, embeddings, and graph edges a memory system derives from your data — the law grants the right, and no one demonstrated the mechanism end to end.

## How to read any agent's memory from now on

The practical yield of this survey is a habit, not a tool. When something new tells you it remembers you, ask three questions: *Where does the memory live?* A file you can open is an answer; a hidden mailbox folder is an answer too, just a different one. *Who can change it, and who can see what changed?* A change log, an approval queue, or a revision history means someone is tracking writes; silence means writes are invisible even to the people accountable for them. *What happens when I say forget?* Check whether forgetting means deleting a note, or deleting the note and everything derived from it — those are different promises, and most products make only the first.

If you run your own agent, the checklist is concrete: open `MEMORY.md` and read what it thinks of you; turn on the approval queue if you inherited it off; use the incognito thread when a conversation should leave no trace; and remember that off the cloud is not the same as off the hook — the newest attacks target exactly the persistent, skill-using, self-hosted systems, and the review queue that catches them is worth the click.

If you use a cloud assistant, assume the defaults this documentation describes: memory on, deletion soft, change history absent — and make your peace with that, or move the conversations that matter somewhere the files are yours.

The file is still on your disk. You can read it any time. The best-governed memory in this survey runs on your own machine, and now you know why that isn't a coincidence — it's the whole point.

---

## Appendix: Sources & Methods (internal — not for publication)

**Status:** Draft (Rs10 first draft; not edited — that is a separate pass)
**Selected pitch:** 4.1 "The Best-Governed Memory Runs on Your Own Machine" (`Artifacts/Article Ideas/6/CAMidea.md`), commissioned directly and rated #2 of 19 in `CAMidearatings.md` (2026-10-13). Note: the Rs10 recipe's default slot is pitch 1.3; per the operator's explicit instruction this draft follows 4.1 instead.
**Snapshot date:** Wave 7 Stage 1 corpus, register S01–S103, sources accessed 2026-10-11 with third-pass corrections 2026-10-12; this draft 2026-10-13. No live verification was performed and no product facts were refreshed from memory — undated vendor pages are "as documented at access date."
**Intended reader:** People who use AI agents and want to know what those agents retain and who can see it; secondary: enterprise and privacy readers.
**Derivative of:** `research/raw/Stage 1/Wave 7/AI Agent Memory/` (README, Index, Synthesis, notes 01–05, Findings, Sources register). No DuckDB exists for this wave; there are no C###/M### anchors by design.
**Controlling sources:** the S## register in `06_Evidence/Sources.md` and the primary documents it records.
**Update triggers:** any register change; verification of any vendor-doc claim; Hermes' `write_approval` default changing; a disclosed real-world memory incident; replication of the 2026 security preprints; resolution of the GDPR derived-erasure question; Stage 2 promotion (re-verify everything).
**Maintainer role:** draft prepared per `ArticleCreation.md` + Wave 7 adaptation; a non-drafter should answer the §7 acceptance questions before any editor pass (Rs11).

### Internal source map — not for publication

Key claim-by-claim anchors. Reliability: P = primary (peer-reviewed/preprint/regulator/standard), T = reputable secondary, C = company/self-published documentation.

| Statement in article | S## | Class / status |
|---|---|---|
| Hermes `MEMORY.md` ≤2,200 chars, `USER.md` ≤1,375 chars; FTS5 session search; on disk in home directory; on by default | S82 | documented fact (C — vendor docs) |
| Hermes approval commands `/memory pending` / `approve` / `reject`; `[auto]` tagging; approval "lists the full text of every entry it overwrote or removed"; write refused if target changed post-staging | S82 | documented fact (C — vendor docs) |
| Hermes `write_approval` defaults off | S82 | documented fact (C — vendor docs); load-bearing for "latent protection" framing |
| Hermes core has no vector store / knowledge graph in core; optional providers run alongside | S83 | documented fact (C) |
| Hermes eight-layer security model; "not a hard boundary" | S84 | documented fact (C — vendor self-assessment) |
| Hermes built by Nous Research; open source | S81, S85 | documented fact (C docs + P repo metadata) |
| OpenClaw file layout (`MEMORY.md`, daily notes, `USER.md`, `DREAMS.md`); "there is no hidden state"; flush before compaction; dreaming; per-conversation scoping; opt-in cross-conversation recall; incognito 24 h, no transcript, no flush; builtin SQLite default | S87, S88, S89, S91 | documented fact (C — vendor docs) |
| OpenClaw loopback-only gateway default; "no subscription, no hosted tier" | S87, S90 | documented fact (C) |
| Copilot memory: on by default; hidden Exchange mailbox folder; Purview doesn't apply; admins can't restrict content type; memory actions "don't generate audit log entries" | S40 | documented fact (C — Microsoft Learn); preview status noted |
| ChatGPT: turning off doesn't delete past chats; up to 30-day logs of deleted saved memories; deleting doesn't remove mentions from past conversations | S37 | documented fact (C — OpenAI help) |
| Claude memory: view/edit; "fully optional, with granular user controls"; no explicit delete control documented | S47 | documented fact (C); absence stated as documented absence |
| Gemini saved instructions require "Memory turned on" | S39 | documented fact (C) |
| Azure AI Foundry (preview): item-level CRUD, store TTL, remember/forget, 100 scopes/store, 10,000 memories/scope, 30-day session deletion | S46 | documented fact (C); preview |
| Vertex Memory Bank revisions under IAM; Bedrock AgentCore short/long-term split | S45, S44 | documented fact (C) |
| "Control tiers" ranking (local-first > enterprise > consumer) | `06_Evidence/Findings.md` RQ3 | **inference** (our reading of the documentation, labelled in text as ours) |
| AgentPoison <0.1% poison rate, >80% ASR; MINJA query-only poisoning; MemoryGraft cross-session drift | S66, S65, S67 | paper-reported (P preprints; not independently replicated) |
| MemCollusion/Salami on OpenClaw: 81.3% save / 75.0% success; survives dilution | S69 | paper-reported (P preprint; 2026-dated; unreplicated) |
| OpenClaw skill poisoning / cascading-failure framing | S94 | paper-reported (P preprint) |
| No disclosed real-world memory-poisoning or cross-tenant-leakage incident found | Findings "Method limits" | absence-of-evidence, stated as such in text |

**Verification note:** every material claim in the body resolves to a register entry above; no claim was upgraded from vendor documentation to verified behaviour, no figure was introduced from memory, and no scene, quote, product behaviour, or anecdote was invented. The three evidence-class boundaries the draft preserves deliberately: (1) vendor documentation is a company's account, flagged in the "What we don't know" section and throughout; (2) the security figures are lab results with no real-world incident rate, flagged where they appear; (3) the tier ranking is labelled in-text as our reading, not a vendor claim. The Hermes approval default-off fact is presented as a default that can change, not a permanent property.

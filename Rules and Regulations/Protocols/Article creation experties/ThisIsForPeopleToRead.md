# This Is For People To Read

---

## The Rule

**Articles are for humans first.**

They are based on evidence, facts, and rigorous research. But the language, the tone, and the format must be **easy and pleasing for humans to read**. This is not negotiable.

---

## Why This Matters

The `dataframe-elephant` project is built on a foundation of **data, claims, metrics, and sources**. Every number, every assertion, and every conclusion is grounded in the research corpus. But that doesn’t mean the articles should read like database queries or technical reports.

**The goal is not to impress researchers.** The goal is to **inform, engage, and empower real people**—smart-home buyers, owners, and enthusiasts—so they can make better decisions.

If an article feels like it’s talking about itself, it’s failing. If it reads like a manual, it’s failing. If it requires a glossary just to get through the first paragraph, it’s failing.

---

## What This Means in Practice

### 1. **No Self-Referential Noise**
Articles should **never** include:
- "Document Control" sections
- References to claim IDs (e.g., `C019`, `C020`)
- Metric IDs (e.g., `M006`, `M007`)
- Database or notebook paths (e.g., `data/smarthome.duckdb`, `notebooks/2/03_offline_failure...`)
- "Provenance Panels" or "Sources and Reproducibility" sections
- Any mention of how the article was built, unless it’s in a **separate, optional appendix** for internal use.

**Why?** Because readers don’t care how the sausage is made. They care about whether their lights will turn on when they flip the switch.

---

### 2. **Write Like a Human, For Humans**
- **Use conversational language.** Write as if you’re explaining something to a friend over coffee, not presenting a paper at a conference.
- **Tell a story.** Start with a scene, a problem, or a moment of tension. Pull the reader in.
- **Avoid jargon.** If you must use technical terms (e.g., "border router," "Thread mesh"), explain them **naturally in context**, not in a glossary or footer.
- **Be direct.** Say "your lights will turn off" instead of "local control fails."
- **Use active voice.** "The router crashes" is better than "A crash of the router occurs."

**Example of what NOT to do:**
> "The corpus indicates that Matter-over-Thread devices lose the ability to communicate with each other when the border router is down (C020, medium confidence)."

**Example of what TO do:**
> "If your border router dies, your switch can’t talk to your bulb. In one test, it took about a minute for the connection to fail completely."

---

### 3. **Evidence Belongs in the Background**
The research corpus is the **foundation** of every article. But it should **never** overshadow the narrative.

- **Weave evidence into the story.** Instead of tables or footnotes, embed facts naturally:
  - "We know this because analysts have traced how the protocol works."
  - "In one controlled test, a switch lost control of a light about a minute after the router died."
  - "Neato, Wemo, and Nest have all pulled the plug on their devices, leaving customers in the dark."

- **Acknowledge uncertainty without breaking the flow.**
  - "We only have one controlled measurement for this."
  - "The rest comes from field reports—people watching their systems collapse in real time."
  - "Here’s what we don’t know: what happens after the cloud goes dark?"

- **If you must cite sources**, do it in a way that doesn’t disrupt the reading experience. For example:
  - Use **inline links** (e.g., "[as reported by Home Assistant logs]") for digital articles.
  - Use **subtle markers** (e.g., "one study found") for print or long-form pieces.

---

### 4. **Structure for Readability**
- **Start with a hook.** Draw the reader in with a scene, a question, or a relatable moment.
- **Use short paragraphs.** Walls of text are intimidating. Break it up.
- **Use subheadings sparingly.** They should guide the reader, not overwhelm them.
- **End with a payoff.** Leave the reader with a clear takeaway, a call to action, or a moment of reflection.

**Example structure:**
1. **Hook:** A vivid scene (e.g., standing in the dark at 11:47 PM).
2. **The Problem:** What’s going wrong? (e.g., "Your smart home doesn’t have one way to fail. It has three.")
3. **The Evidence:** What do we know? (e.g., "In one test, a switch lost control of a light about a minute after the router died.")
4. **The Solution:** What can the reader do? (e.g., "Keep a second border router powered and adopted.")
5. **The Close:** Bring it back to the hook (e.g., "It’s still 11:47 PM. The switch is in your hand. Now you know...").

---

### 5. **Tone: Clear, Direct, and Engaging**
- **Be confident.** Avoid hedging like "it seems that" or "it appears to be." If the evidence supports it, say it.
- **Be honest about uncertainty.** If we don’t know something, say so. But don’t let uncertainty paralyze the narrative.
- **Be empathetic.** Acknowledge the reader’s frustrations, fears, or confusion. (e.g., "You’re standing in the dark, wondering why no one warned you this could happen.")
- **Be actionable.** Always give the reader something to do, think, or ask. (e.g., "Test it. Unplug the primary and see how long it takes to recover.")

---

## What’s Negotiable (And What’s Not)

| **Negotiable** | **Not Negotiable** |
|----------------|---------------------|
| The specific stories or examples used | The requirement that articles are **easy and pleasing to read** |
| The length of the article | The removal of **self-referential noise** (claim IDs, metric IDs, etc.) |
| The depth of technical detail | The use of **conversational, human language** |
| The structure or flow of the narrative | The **evidence-based foundation** of the content |

---

## How to Test If an Article Meets the Standard

Ask yourself:
1. **Would I read this if I weren’t paid to?** If the answer is no, rewrite it.
2. **Would my non-technical friend understand this?** If the answer is no, simplify it.
3. **Does this feel like a story, or does it feel like a report?** If it’s the latter, rework it.
4. **Are there any parts where the article talks about itself?** If yes, cut them.
5. **Does the reader know what to do next?** If not, add a clear takeaway or call to action.

---

## Final Note

The research is the **foundation**. The article is the **house**. No one wants to live in a foundation. Build something people want to live in.

---

**This is not negotiable.**
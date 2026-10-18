# Brainstorm Readability Protocol

## Status

This protocol is mandatory for every person, agent, or process that produces a brainstorm report in this project — NR rounds under `FreeBrainstorming.md`, article-idea brainstorms, and any other file whose purpose is to put ideas in front of a human reader.

A brainstorm report its reader cannot comfortably read is a failed deliverable. It is not "mostly done", not "structurally complete", not "pending polish". It is worthless, and it is rejected and rewritten.

`Article creation expertise/ThisIsForPeopleToRead.md` states this rule for articles. This document states it for brainstorm output, where the failure has actually occurred.

## 1. Why this exists

A brainstorm report has one purpose: to be read by a person who then decides what to do with the ideas. It is a message to a human, not a record of the work.

If the reader cannot read it, nothing else about it matters:

- Verified citations do not matter. Every source can be real and correctly dated, and the reader still gets nothing.
- Structural compliance does not matter. A report can satisfy every section, gate, and exit criterion in its protocol and still be unread, therefore unused, therefore worthless.
- Ranking, de-duplication, coverage, self-audits: none of it counts. Unread is unused.

This is the obvious thing that gets forgotten. A report written for someone's eyes is worthless the moment those eyes give up on it. Writing it badly is not a small defect in a good report. It is the deletion of the report.

The failure is not hypothetical. On 2026-10-09 an NR5 brainstorm passed every structural gate and every citation check, and was rejected on sight: *"absolutely terrible to the point that my brain hurts while reading it."* Measured against its predecessor: 6,932 words against NR4's 4,533, with 35 sentences over 30 words against 22.

## 2. The rule

**If the reader cannot read it, the report is worthless. Write to be read.**

Everything below enforces that one sentence. When a rule below and the reader's comfort conflict, the reader wins.

## 3. Non-negotiable rules

1. **Write for the reader, not for the record.** The file is a message. It is not a log of the process, a transcript of the run, or evidence for a future audit.
2. **Keep the working apparatus out of the report.** Do not narrate the protocol, the round number, the dispatch, the exclusion logic, or the self-check in the body. A header block of at most six lines may carry date, subject, and method. Everything else the process generated goes to a separate annex or nowhere at all.
3. **One idea per sentence.** Two ideas in one sentence means one of them will be lost. Split it.
4. **No sentence over 30 words. Keep the average under 20.** This is measurable, so it will be measured.
5. **Verbs, not stacked clauses.** "Regulators cannot compare alerts between countries" — not "the absence of a common denominator for alert outcomes prevents cross-jurisdictional comparability".
6. **No identifier litter inside prose.** Claim ids, metric ids, subject letters, and register codes belong in a table cell or a note. Never inside a sentence the reader has to parse.
7. **Never define the subject.** The reader knows what fusion, a semiconductor, and a border router are. A definition inside the body is padding and reads as contempt.
8. **No table cell over 25 words.** If a cell needs more, it is prose and belongs in a paragraph, not in a row.
9. **Headings carry the idea, not the stage.** "Subject B — An Alert-Effectiveness Assurance Specification for Public Warning Systems" fails. "Measure whether people understood the warning, not whether it was sent" passes.
10. **Idea first, apparatus second.** Lead with the idea in plain words. Evidence, anchors, and provenance follow, in a compact block, after the reader has the idea.
11. **Do not invent experience or history.** No first-person scenes the writer did not live, and no claims about the reader's own past work unless a file was read this session and is named.
12. **Cut, do not pad.** A shorter readable report beats a longer one. If a section cannot be made readable, delete it and say so in one line.

## 4. The mandatory self-check

Run all six checks before the file is saved. If any check fails, rewrite and run them again. The first draft is never saved.

1. **Sentence scan.** Count the sentences over 30 words and the average sentence length.
2. **Meta-scan.** Search the body for process words: `protocol`, `round`, `dispatch`, `de-duplication`, `self-check`, `exit criteria`, `per protocol`. Any hit in the body moves to the header or is deleted.
3. **Identifier scan.** Search for `(S\d+)`, `(C0\d+)`, and single capital letters used as references (`(D)`, `(B)`) inside sentences.
4. **Table scan.** Flag every cell over 25 words.
5. **Nominalisation pass.** Rewrite "the absence of X prevents Y" as "Y fails when X is missing".
6. **One-pass read.** Read the report from the top to the bottom without stopping. Every sentence that forced a second read gets rewritten.

Report only the result in the header, for example `Self-check: 6/6`. Do not report the process that produced the result.

The quoted specimens in §5 are excluded from the sentence count. They are examples of the failure, kept so it can be recognised, and are never to be imitated.

Measurement command (venv form per `AGENTS.md`):

```
.\.venv\Scripts\python.exe -c "import re,sys; t=open(sys.argv[1],encoding='utf-8').read(); w=re.findall(r'[A-Za-z0-9\u00C0-\u024F]+',t); s=[x for x in re.split(r'[.!?;]+',t) if len(x.split())>2]; print(len(w),'words',len(s),'sentences',round(len(w)/max(len(s),1),1),'avg words/sent',sum(1 for x in s if len(x.split())>30),'sentences over 30w')" "research/Research ideas/NR6/NR6brainstorm.md"
```

## 5. What unreadable looks like

Specimens from NR5 (2026-10-09, rejected on sight). Verbatim.

**Specimen 1 — process narration inside the body (breaks rule 2):**

> - **Round-number note:** Dispatch named this round NR5 and the target folder `research/Research ideas/NR5/`. No conflicting round number was present in the dispatch; NR5 is the next free round after NR2–NR4. No discrepancy recorded.

The report is describing its own bookkeeping. The reader does not need the round number's paperwork. The reader needs ideas.

**Specimen 2 — identifier litter and stacked clauses (breaks rules 4, 5, 6):**

> - **NR2** — auditing AI-curated research agendas, evidence-provenance decay in citation chains, research-funding model effectiveness, climate-resilience indicators for health systems, post-market surveillance of adaptive medical AI, energy-programme evaluation, One Health data-silo interoperability — excluded. *Note:* NR5 Subject A concerns the **surveillance-to-action translation gap** (why available data fails to trigger institutional action), which is a different universal problem from NR2's *indicator comparability* (D) and *citation provenance* (B): the unit of analysis is the decision pathway of an institution, not the dataset or the document chain.

Two ideas, four identifiers, one sentence. The reader must hold another session's taxonomy in their head to parse a sentence whose only job is to say "this idea is not that idea".

**Specimen 3 — a table cell doing a paragraph's work (breaks rule 8):**

> | 1 | **Antimicrobial resistance / health security** | WHO World Health Assembly adopted the updated Global Action Plan on AMR 2026–2036 (WHA79, 23–25 May 2026); GLASS reports 104 countries reporting use+resistance data in 2025; narrative review "Closing the Surveillance-to-Stewardship Gap," *Clinical Microbiology and Infection* (28 Sep 2026): UK ESPAUR shows 2024 antibiotic use 2% below 2019 baseline while resistant infections rose 13.1% | Detection capacity has outpaced the capacity to act on it; no instrument diagnoses *where* the data-to-decision chain breaks inside an institution or a country |

Rewritten to pass, the same material reads:

> Antimicrobial resistance: the world can now detect resistant infections faster than it can act on them. No shared method shows where the chain from data to decision breaks, inside a country or inside one institution. Trigger: the World Health Assembly adopted the updated global action plan for 2026–2036 in May 2026. A clinical review in September 2026 documents the gap. In the UK, antibiotic use fell 2% while resistant infections rose 13.1%.

Same facts. Five sentences, none over 25 words, no identifiers, no protocol narration. This is the standard.

*(The rewritten block is an illustration written for this protocol, not a quotation from any file.)*

## 6. What happens when this fails

The report is rejected in full. Rejected means rewritten and re-checked — not annotated, not patched with a summary at the top, not excused by its citation quality.

A report counts as produced only after the reader has read it once, without stopping. Before that, it does not exist, no matter how many gates it passed.

## 7. Relationship to other protocols

| Protocol | Governs |
| --- | --- |
| `FreeBrainstorming.md` | What the ideas must be (external framing, coverage, de-duplication, exit criteria) |
| `BrainstormReadability.md` (this file) | How the report must read |
| `Article creation expertise/ThisIsForPeopleToRead.md` | The same rule for articles |
| `Research-Evaluation.md` | Evidence quality and claim discipline |

Both `FreeBrainstorming.md` and this protocol bind, and passing one is not a defence against failing the other. Readability is not evidence of fidelity and fidelity is not readability — the same warning `AuthorityDocumentCreation.md` records from Maynez et al. (ACL 2020). Do not copy the human-writing doctrine here; it lives in `ThisIsForPeopleToRead.md` (R3: one copy of each shared block).

## 8. Update triggers

Review this protocol when any of the following happens:

- the reader rejects a report on readability, or abandons one mid-read;
- a self-check flag fires on a report that otherwise passed its own protocol;
- `ThisIsForPeopleToRead.md`, `FreeBrainstorming.md`, or `Research-Evaluation.md` changes (edit the source of the rule first, then this file — R9);
- a new brainstorm format or dispatch mechanism is introduced.

---

**This is not negotiable. A report the reader cannot read is not a report.**

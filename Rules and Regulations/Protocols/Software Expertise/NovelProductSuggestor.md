# Novel Product Suggestor Protocol

**Version:** 1.0
**Purpose:** Define a repeatable process for examining research content folders and generating novel product suggestions, particularly software products.

---

## 1. Overview

This protocol describes how to systematically analyze a research folder (e.g., `research/Programming Languages`) and produce a structured set of novel product ideas that are grounded in the principles, patterns, and insights documented in that research.

The output is a markdown file containing product concepts, each with a clear rationale linking back to the research content.

---

## 2. Prerequisites

Before starting, ensure:

- [ ] The target research folder exists and contains structured content (subfolders, markdown files, or both)
- [ ] The output directory exists (e.g., `Artifacts/software product ideas/`)
- [ ] You have read access to all files in the research folder
- [ ] You have write access to the output directory

---

## 3. Process

### Phase 1: Reconnaissance

**Goal:** Build a mental model of the research folder's structure and content.

1. **List the folder structure** — Use directory listing to identify subfolders and files.
2. **Identify content categories** — Look for recurring patterns in folder names (e.g., `Basics/`, `Products/`, `Cross Section/`).
3. **Count the files** — Note the volume of content to calibrate reading depth.

**Output:** A mental (or written) map of the folder's organization.

---

### Phase 2: Deep Reading

**Goal:** Extract the core principles, patterns, and insights from the research.

1. **Read cross-cutting documents first** — Files in folders like `Cross Section/` or `Comparisons/` typically synthesize principles across multiple topics. These are the highest-value files.
2. **Read product creation logic files** — Files named `ProductCreationLogic.md` or similar describe how the subject matter translates into products. These are the primary source for product ideas.
3. **Read basics/fundamentals files** — Files named `Basics.md` or similar provide foundational context. Skim these for unique constraints or opportunities.
4. **Read examples files** — Files named `DistinctProductExamples.md` show existing products. These help avoid suggesting something that already exists and reveal gaps.

**For each file, extract:**
- Core design principles (e.g., "memory safety without garbage collection")
- Product creation patterns (e.g., "CLI tools with clap")
- Key constraints (e.g., "GIL limits true parallelism")
- Unique strengths (e.g., "fearless concurrency")
- Language pairings and synergies (e.g., "TypeScript + Python for full-stack")

**Output:** A collection of principles, patterns, and opportunities.

---

### Phase 3: Synthesis

**Goal:** Combine extracted principles into product opportunities.

1. **Identify recurring themes** — Look for principles that appear across multiple files (e.g., "type safety" appears in TypeScript, Haskell, Rust, and Kotlin).
2. **Find complementary pairings** — Identify which subjects work well together (e.g., "Python for ML + Rust for performance").
3. **Spot gaps** — Note where existing products (from `DistinctProductExamples.md`) don't cover a combination of principles.
4. **Look for cross-domain applications** — Consider how principles from one domain (e.g., systems programming) could apply to another (e.g., web development).

**Output:** A list of product opportunity areas.

---

### Phase 4: Product Ideation

**Goal:** Generate specific, novel product ideas from the opportunity areas.

For each product idea, apply this template:

1. **Name** — A short, memorable product name.
2. **Principle** — The research principle(s) it leverages.
3. **Concept** — A 2-3 sentence description of what the product does.
4. **Why it's novel** — How it differs from existing products.
5. **Languages/Tech** — The specific languages or technologies involved, and why they're the right choice.

**Ideation techniques:**
- **Combine two principles** — e.g., "type safety" + "real-time collaboration" = a type-safe real-time collaborative editor.
- **Apply a pattern to a new domain** — e.g., "scriptable extensible pattern" applied to data pipelines.
- **Remove a constraint** — e.g., "what if we could run Python on bare metal without a runtime?"
- **Scale a strength** — e.g., "Elixir handles millions of connections — what if we built a CRDT-based editor on it?"

**Output:** A list of product ideas, each with the five template fields.

---

### Phase 5: Structuring and Writing

**Goal:** Produce a well-organized markdown document.

1. **Write a header** — Title, context, and grounding statement.
2. **Write each product idea** — Use a consistent format (see Section 4).
3. **Add a summary table** — A quick-reference table of all products.
4. **Add common threads** — A synthesis section identifying overarching themes.
5. **Review** — Ensure every idea traces back to a specific research principle.

**Output:** The final markdown file.

---

## 4. Output Format

Each product idea should follow this structure:

```markdown
## N. ProductName

**Principle:** [Research principle(s) leveraged]

**Concept:** [2-3 sentence description]

**Why it's novel:** [How it differs from existing products]

**Languages:** [Primary languages and why they're the right choice]
```

The document should end with:

- A **summary table** (Product | Core Pattern | Primary Languages)
- A **common threads** section (overarching themes across all ideas)

---

## 5. Quality Criteria

A good product suggestion:

- [ ] **Grounded** — Traces back to a specific principle or pattern in the research
- [ ] **Novel** — Not a copy of an existing product (check `DistinctProductExamples.md`)
- [ ] **Specific** — Describes a concrete product, not a vague category
- [ ] **Feasible** — Uses languages and technologies that exist and work well together
- [ ] **Explained** — Clearly states why the chosen languages/technologies are appropriate
- [ ] **Distinct** — Each idea is meaningfully different from the others

---

## 6. Example Application

**Input:** `research/Programming Languages/`

**Process:**
1. Reconnaissance: Found 20 language subfolders, each with `Basics/`, `Products/`, and sometimes `Cross Section/`.
2. Deep reading: Read `Cross Section/WhatWorksTogether.md` for pairings, then read `ProductCreationLogic.md` from Python, Rust, TypeScript, Go, Elixir, Haskell, Swift, and Kotlin.
3. Synthesis: Identified recurring themes (type safety, glue+engine pattern, shared core pattern, scriptable extensible pattern).
4. Ideation: Generated 12 product ideas combining principles across languages.
5. Writing: Structured as `NovelProductSuggestions1.md` with summary table and common threads.

**Output:** `Artifacts/software product ideas/NovelProductSuggestions1.md`

---

## 7. Adapting to Other Research Folders

This protocol is not limited to programming languages. It can be applied to any research folder:

| Research Folder | What to Look For | Product Type |
|----------------|-----------------|--------------|
| `research/Programming Languages` | Language strengths, pairings, patterns | Software products |
| `research/Architecture` | Design patterns, structural principles | Systems/products |
| `research/Design` | User experience principles, visual patterns | Consumer products |
| `research/Science` | Scientific principles, formulas | Hardware/biotech products |
| `research/Business` | Market dynamics, economic principles | Business/service products |

The key is to extract **principles** (not just facts) and then **combine** them into product opportunities.

---

## 8. Tips

- **Read the cross-cutting files first** — They contain the highest-density insights.
- **Don't read everything** — Sample 5-8 files deeply rather than skimming all of them.
- **Look for tensions** — When two principles conflict (e.g., "Python is slow" vs. "Python has the best ML ecosystem"), that tension often sparks the best ideas.
- **Use the "DistinctProductExamples" files** — They tell you what already exists, so you can find gaps.
- **Aim for 8-15 ideas** — Enough to be comprehensive, few enough to be digestible.
- **Write for a technical audience** — Assume the reader understands programming concepts.

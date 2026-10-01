---
name: novel-product-suggestor
description: "Generates 8-15 novel product suggestions from a research folder. Use when asked to create product ideas, explore commercial opportunities, or generate a new wave of suggestions from research content (e.g., research/Programming Languages/). Applies the 5-phase process: Reconnaissance, Deep Reading, Synthesis, Product Ideation, Structuring."
version: 1.0.0
---

# Novel Product Suggestor

Generates 8-15 novel product suggestions from a research folder, grounded in the principles and patterns documented in that research. Distilled from `Rules and Regulations/Protocols/Software Experties/NovelProductSuggestor.md`.

## When to use this skill

- Generating product ideas from a research folder (e.g., `research/Programming Languages/`)
- Creating a new wave of product suggestions
- Exploring commercial opportunities from research content
- Asked to "suggest products" or "brainstorm products" from research

## Prerequisites

- The target research folder exists and contains structured content (subfolders, markdown files, or both)
- The output directory exists (e.g., `Artifacts/software product ideas/Step 1/Wave N/`)
- You have read access to all files in the research folder
- You have write access to the output directory

## The Process

### Step 1: Reconnaissance

1. List the research folder structure — identify subfolders and files
2. Identify content categories — look for recurring patterns (e.g., `Basics/`, `Products/`, `Cross Section/`)
3. Count the files — calibrate reading depth based on volume

### Step 2: Deep Reading

1. **Read cross-cutting documents first** — Files in `Cross Section/` or `Comparisons/` synthesize principles across topics
2. **Read product creation logic files** — `ProductCreationLogic.md` files describe how the subject translates into products
3. **Read basics/fundamentals files** — `Basics.md` files provide foundational context; skim for unique constraints
4. **Read examples files** — `DistinctProductExamples.md` shows existing products; use to avoid duplicates and find gaps

**For each file, extract:**
- Core design principles (e.g., "memory safety without garbage collection")
- Product creation patterns (e.g., "CLI tools with clap")
- Key constraints (e.g., "GIL limits true parallelism")
- Unique strengths (e.g., "fearless concurrency")
- Language pairings and synergies (e.g., "TypeScript + Python for full-stack")

### Step 3: Synthesis

1. **Identify recurring themes** — principles that appear across multiple files
2. **Find complementary pairings** — which subjects work well together
3. **Spot gaps** — where existing products don't cover a combination of principles
4. **Look for cross-domain applications** — how principles from one domain could apply to another

### Step 4: Product Ideation

Generate 8-15 product ideas using these techniques:
- **Combine two principles** — e.g., "type safety" + "real-time collaboration" = type-safe real-time collaborative editor
- **Apply a pattern to a new domain** — e.g., "scriptable extensible pattern" applied to data pipelines
- **Remove a constraint** — e.g., "what if we could run Python on bare metal without a runtime?"
- **Scale a strength** — e.g., "Elixir handles millions of connections — what if we built a CRDT-based editor on it?"

**For each idea, define:**
1. **Name** — A short, memorable product name
2. **Principle** — The research principle(s) it leverages
3. **Concept** — A 2-3 sentence description
4. **Why it's novel** — How it differs from existing products
5. **Languages** — Primary languages and why they're the right choice

### Step 5: Structuring and Writing

1. Write a header — title, context, and grounding statement
2. Write each product idea using the format from Step 4
3. Add a summary table (Product | Core Pattern | Primary Languages)
4. Add a common threads section identifying overarching themes
5. Review — ensure every idea traces back to a specific research principle

## Quality Gates

- [ ] 8-15 product ideas generated
- [ ] Each idea has: Name, Principle, Concept, Why it's novel, Languages
- [ ] Every idea traces to a specific research principle
- [ ] No idea duplicates an existing product (check `DistinctProductExamples.md`)
- [ ] Each idea is meaningfully different from the others
- [ ] Summary table included
- [ ] Common threads section included

## Output

A markdown file (e.g., `NovelProductSuggestions1.md`) written to the specified output directory.

## Tips

- Read the cross-cutting files first — they contain the highest-density insights
- Don't read everything — sample 5-8 files deeply rather than skimming all of them
- Look for tensions — when two principles conflict, that tension often sparks the best ideas
- Use the "DistinctProductExamples" files — they tell you what already exists
- Aim for 8-15 ideas — enough to be comprehensive, few enough to be digestible
- Write for a technical audience — assume the reader understands programming concepts

## References

- Process: `Rules and Regulations/Protocols/Software Experties/NovelProductSuggestor.md`
- Worked example: `Artifacts/software product ideas/Wave 1/Stage 1/Step 1/NovelProductSuggestions1.md`
- Evaluation: `Rules and Regulations/Protocols/Software Experties/Evaluation_of_SoftwareIDEAS.md`
- Transition to Step 2: `Rules and Regulations/Protocols/Software Experties/FromStep1toStep2.md`

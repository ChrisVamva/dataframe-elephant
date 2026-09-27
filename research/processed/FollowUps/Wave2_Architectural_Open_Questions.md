# Follow-Up Research Agenda

## Executive Summary

This research agenda was systematically formulated from the Stage 2 extraction layer (`research/raw/Stage 2/`) and the citation intelligence database (`data/citations.duckdb`), governed by `Protocols/FollowUpResearch.md`.

- **Total Research Questions Formulated:** 8
- **P1 (Immediate Priority):** 8
- **P2 (Scheduled Waves):** 0
- **P3 (Backlog / Opportunistic):** 0

---

## Priority Ranking Table

| Question ID | Title | Gap Code | Category | Score | Tier |
| --- | --- | --- | --- | ---: | --- |
| [RQ-023](#rq-023) | Source Decoupling & Comparative Evaluation: https://docs.unstructured.io/ · https:// | `GAP-OPN` | Bundled Source Disambiguation | 16.0 | **P1** |
| [RQ-024](#rq-024) | Source Decoupling & Comparative Evaluation: https://openlineage.io/docs/spec/object- | `GAP-OPN` | Bundled Source Disambiguation | 16.0 | **P1** |
| [RQ-025](#rq-025) | Source Decoupling & Comparative Evaluation: https://openai.github.io/openai-agents-p | `GAP-OPN` | Bundled Source Disambiguation | 16.0 | **P1** |
| [RQ-027](#rq-027) | Source Decoupling & Comparative Evaluation: https://www.w3.org/TR/sparql11-query/ ·  | `GAP-OPN` | Bundled Source Disambiguation | 16.0 | **P1** |
| [RQ-028](#rq-028) | Source Decoupling & Comparative Evaluation: https://docs.cloud.google.com/bigquery/d | `GAP-OPN` | Bundled Source Disambiguation | 16.0 | **P1** |
| [RQ-029](#rq-029) | Source Decoupling & Comparative Evaluation: https://docs.jupyter.org/ · https://obse | `GAP-OPN` | Bundled Source Disambiguation | 16.0 | **P1** |
| [RQ-030](#rq-030) | Alias Disambiguation for Citation 'S5' | `GAP-CON` | Unresolved Source Alias | 12.0 | **P1** |
| [RQ-031](#rq-031) | Alias Disambiguation for Citation 'S6' | `GAP-CON` | Unresolved Source Alias | 12.0 | **P1** |

---

## Formulated Research Question Dossiers

<a id="rq-023"></a>
### [RQ-023] Source Decoupling & Comparative Evaluation: https://docs.unstructured.io/ · https://

- **Priority Tier:** **P1** (Priority Score: **16.0**)
- **Gap Code:** `GAP-OPN` (Bundled Source Disambiguation)
- **Trigger Reference:** `ExtractionLog.md L001`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 1/3

#### 1. Core Research Question
> How do the distinct components in 'https://docs.unstructured.io/ · https://docs.llamaindex.ai/' differ in their evidence support, and what are their independent canonical URLs and evidence tiers?

#### 2. Scope & Boundaries
- **In Scope:** Extracting independent source entries, canonical URLs, and distinct evidence classes for each bundled entity.
- **Out of Scope:** Merging unrelated third-party blog commentary.
- **Intended Downstream Use:** Refactor Sources.md to separate bundled citations into atomic, single-URL records.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation per individual project/standard.`
- **Target Sources:**
  - https://docs.unstructured.io/
  - https://docs.llamaindex.ai/

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** Separate atomic source rows with independent URLs, publishers, and publication dates.
- **Falsifier:** Official confirmation that the bundled projects share a single unified governance and specification.

---

<a id="rq-024"></a>
### [RQ-024] Source Decoupling & Comparative Evaluation: https://openlineage.io/docs/spec/object-

- **Priority Tier:** **P1** (Priority Score: **16.0**)
- **Gap Code:** `GAP-OPN` (Bundled Source Disambiguation)
- **Trigger Reference:** `ExtractionLog.md L002`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 1/3

#### 1. Core Research Question
> How do the distinct components in 'https://openlineage.io/docs/spec/object-model/ · https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html' differ in their evidence support, and what are their independent canonical URLs and evidence tiers?

#### 2. Scope & Boundaries
- **In Scope:** Extracting independent source entries, canonical URLs, and distinct evidence classes for each bundled entity.
- **Out of Scope:** Merging unrelated third-party blog commentary.
- **Intended Downstream Use:** Refactor Sources.md to separate bundled citations into atomic, single-URL records.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation per individual project/standard.`
- **Target Sources:**
  - https://openlineage.io/docs/spec/object-model/
  - https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** Separate atomic source rows with independent URLs, publishers, and publication dates.
- **Falsifier:** Official confirmation that the bundled projects share a single unified governance and specification.

---

<a id="rq-025"></a>
### [RQ-025] Source Decoupling & Comparative Evaluation: https://openai.github.io/openai-agents-p

- **Priority Tier:** **P1** (Priority Score: **16.0**)
- **Gap Code:** `GAP-OPN` (Bundled Source Disambiguation)
- **Trigger Reference:** `ExtractionLog.md L003`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 1/3

#### 1. Core Research Question
> How do the distinct components in 'https://openai.github.io/openai-agents-python/agents/ · https://openai.github.io/openai-agents-python/tracing/ · https://docs.crewai.com/' differ in their evidence support, and what are their independent canonical URLs and evidence tiers?

#### 2. Scope & Boundaries
- **In Scope:** Extracting independent source entries, canonical URLs, and distinct evidence classes for each bundled entity.
- **Out of Scope:** Merging unrelated third-party blog commentary.
- **Intended Downstream Use:** Refactor Sources.md to separate bundled citations into atomic, single-URL records.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation per individual project/standard.`
- **Target Sources:**
  - https://openai.github.io/openai-agents-python/agents/
  - https://openai.github.io/openai-agents-python/tracing/
  - https://docs.crewai.com/

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** Separate atomic source rows with independent URLs, publishers, and publication dates.
- **Falsifier:** Official confirmation that the bundled projects share a single unified governance and specification.

---

<a id="rq-027"></a>
### [RQ-027] Source Decoupling & Comparative Evaluation: https://www.w3.org/TR/sparql11-query/ · 

- **Priority Tier:** **P1** (Priority Score: **16.0**)
- **Gap Code:** `GAP-OPN` (Bundled Source Disambiguation)
- **Trigger Reference:** `ExtractionLog.md L005`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 1/3

#### 1. Core Research Question
> How do the distinct components in 'https://www.w3.org/TR/sparql11-query/ · https://www.w3.org/TR/owl2-overview/ · https://www.w3.org/TR/shacl/' differ in their evidence support, and what are their independent canonical URLs and evidence tiers?

#### 2. Scope & Boundaries
- **In Scope:** Extracting independent source entries, canonical URLs, and distinct evidence classes for each bundled entity.
- **Out of Scope:** Merging unrelated third-party blog commentary.
- **Intended Downstream Use:** Refactor Sources.md to separate bundled citations into atomic, single-URL records.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation per individual project/standard.`
- **Target Sources:**
  - https://www.w3.org/TR/sparql11-query/
  - https://www.w3.org/TR/owl2-overview/
  - https://www.w3.org/TR/shacl/

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** Separate atomic source rows with independent URLs, publishers, and publication dates.
- **Falsifier:** Official confirmation that the bundled projects share a single unified governance and specification.

---

<a id="rq-028"></a>
### [RQ-028] Source Decoupling & Comparative Evaluation: https://docs.cloud.google.com/bigquery/d

- **Priority Tier:** **P1** (Priority Score: **16.0**)
- **Gap Code:** `GAP-OPN` (Bundled Source Disambiguation)
- **Trigger Reference:** `ExtractionLog.md L006`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 1/3

#### 1. Core Research Question
> How do the distinct components in 'https://docs.cloud.google.com/bigquery/docs/load-transform-export-intro · https://docs.snowflake.com/en/user-guide/intro-key-concepts · https://docs.databricks.com/aws/en/lakehouse/medallion' differ in their evidence support, and what are their independent canonical URLs and evidence tiers?

#### 2. Scope & Boundaries
- **In Scope:** Extracting independent source entries, canonical URLs, and distinct evidence classes for each bundled entity.
- **Out of Scope:** Merging unrelated third-party blog commentary.
- **Intended Downstream Use:** Refactor Sources.md to separate bundled citations into atomic, single-URL records.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation per individual project/standard.`
- **Target Sources:**
  - https://docs.cloud.google.com/bigquery/docs/load-transform-export-intro
  - https://docs.snowflake.com/en/user-guide/intro-key-concepts
  - https://docs.databricks.com/aws/en/lakehouse/medallion

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** Separate atomic source rows with independent URLs, publishers, and publication dates.
- **Falsifier:** Official confirmation that the bundled projects share a single unified governance and specification.

---

<a id="rq-029"></a>
### [RQ-029] Source Decoupling & Comparative Evaluation: https://docs.jupyter.org/ · https://obse

- **Priority Tier:** **P1** (Priority Score: **16.0**)
- **Gap Code:** `GAP-OPN` (Bundled Source Disambiguation)
- **Trigger Reference:** `ExtractionLog.md L007`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 1/3

#### 1. Core Research Question
> How do the distinct components in 'https://docs.jupyter.org/ · https://observablehq.com/documentation/notebooks · https://observablehq.com/plot/' differ in their evidence support, and what are their independent canonical URLs and evidence tiers?

#### 2. Scope & Boundaries
- **In Scope:** Extracting independent source entries, canonical URLs, and distinct evidence classes for each bundled entity.
- **Out of Scope:** Merging unrelated third-party blog commentary.
- **Intended Downstream Use:** Refactor Sources.md to separate bundled citations into atomic, single-URL records.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation per individual project/standard.`
- **Target Sources:**
  - https://docs.jupyter.org/
  - https://observablehq.com/documentation/notebooks
  - https://observablehq.com/plot/

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** Separate atomic source rows with independent URLs, publishers, and publication dates.
- **Falsifier:** Official confirmation that the bundled projects share a single unified governance and specification.

---

<a id="rq-030"></a>
### [RQ-030] Alias Disambiguation for Citation 'S5'

- **Priority Tier:** **P1** (Priority Score: **12.0**)
- **Gap Code:** `GAP-CON` (Unresolved Source Alias)
- **Trigger Reference:** `citations.duckdb source_alias alias_d1f71c8c09b92d708284f527`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What specific authoritative work, report, or specification does citation label 'S5' refer to in its originating document?

#### 2. Scope & Boundaries
- **In Scope:** Textual context in source document, canonical title, author, and URL for 'S5'.
- **Out of Scope:** Fuzzy or speculative attribution without textual match.
- **Intended Downstream Use:** Map the unresolved alias in source_alias to a canonical source_id.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary citation text or original referenced document bibliography.`
- **Target Sources:**
  - Originating Markdown document
  - Author/publisher official archive

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** Mapping to an unambiguous canonical URL and source_id.
- **Falsifier:** Evidence that the alias is an informal generic reference rather than a discrete citable source.

---

<a id="rq-031"></a>
### [RQ-031] Alias Disambiguation for Citation 'S6'

- **Priority Tier:** **P1** (Priority Score: **12.0**)
- **Gap Code:** `GAP-CON` (Unresolved Source Alias)
- **Trigger Reference:** `citations.duckdb source_alias alias_1f9f1fa2733550c820c5e003`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What specific authoritative work, report, or specification does citation label 'S6' refer to in its originating document?

#### 2. Scope & Boundaries
- **In Scope:** Textual context in source document, canonical title, author, and URL for 'S6'.
- **Out of Scope:** Fuzzy or speculative attribution without textual match.
- **Intended Downstream Use:** Map the unresolved alias in source_alias to a canonical source_id.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary citation text or original referenced document bibliography.`
- **Target Sources:**
  - Originating Markdown document
  - Author/publisher official archive

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** Mapping to an unambiguous canonical URL and source_id.
- **Falsifier:** Evidence that the alias is an informal generic reference rather than a discrete citable source.

---

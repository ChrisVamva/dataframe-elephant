"""Core logic for post-TransitionStage2 follow-up research question formulation.

Parses Stage 2 extraction artifacts and DuckDB citation intelligence to identify
epistemic gaps, calculates priority scores, and generates structured research dossiers.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional
import duckdb


@dataclass
class ResearchGap:
    gap_id: str
    gap_code: str  # GAP-BND, GAP-CND, GAP-EPI, GAP-FAL, GAP-OPN, GAP-CON
    target_concept: str
    category: str
    description: str
    source_reference: str
    workflow_centrality: int  # 1 - 5
    evidence_severity: int    # 1 - 5
    verification_difficulty: int  # 1 - 3
    priority_score: float = 0.0
    priority_tier: str = "P2"

    def __post_init__(self):
        self.priority_score = round(
            (self.workflow_centrality * self.evidence_severity) / self.verification_difficulty,
            2,
        )
        if self.priority_score >= 12.0:
            self.priority_tier = "P1"
        elif self.priority_score >= 6.0:
            self.priority_tier = "P2"
        else:
            self.priority_tier = "P3"


@dataclass
class FormulatedQuestion:
    rq_id: str
    title: str
    gap: ResearchGap
    core_question: str
    in_scope: str
    out_of_scope: str
    intended_use: str
    min_evidence_class: str
    target_sources: List[str]
    resolution_criteria: str
    falsifier: str


def parse_markdown_table_rows(markdown_text: str) -> List[Dict[str, str]]:
    """Parse markdown table rows into list of dictionaries mapping header -> cell text."""
    lines = markdown_text.splitlines()
    table_lines = [line.strip() for line in lines if line.strip().startswith("|")]
    if len(table_lines) < 3:
        return []

    headers = [h.strip() for h in table_lines[0].split("|")[1:-1]]
    separator = table_lines[1]
    if not re.match(r"^\|?(\s*[:-]+[-:]*\s*\|?)+$", separator):
        return []

    rows = []
    for line in table_lines[2:]:
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if len(cells) == len(headers):
            rows.append(dict(zip(headers, cells)))
    return rows


def scan_stage2_entities(stage2_dir: Path) -> List[ResearchGap]:
    """Scan Entities.md for unstated boundaries and assign priority scores."""
    entities_file = stage2_dir / "Entities.md"
    if not entities_file.is_file():
        return []

    rows = parse_markdown_table_rows(entities_file.read_text(encoding="utf-8"))
    gaps: List[ResearchGap] = []
    
    # Priority heuristics by entity concept
    critical_entities = {
        "DuckDB": (5, 4, 1),
        "MotherDuck": (4, 4, 1),
        "DuckLake": (4, 4, 2),
        "Polars": (4, 3, 1),
        "pandas": (4, 3, 1),
        "LangGraph": (4, 4, 2),
        "Microsoft Agent Framework": (4, 4, 2),
        "MCP": (5, 4, 1),
        "A2A": (4, 4, 2),
        "PROV": (4, 3, 1),
        "dbt": (4, 3, 1),
        "Semantic layer": (4, 4, 2),
    }

    for row in rows:
        eid = row.get("Entity ID", "")
        name = row.get("Canonical name", "")
        typ = row.get("Type", "")
        boundary = row.get("Boundary (what it is not)", "")

        if "[boundary not stated in source]" in boundary:
            c, s, d = critical_entities.get(name, (3, 3, 1))
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-BND-{eid}",
                    gap_code="GAP-BND",
                    target_concept=name,
                    category=f"Entity Boundary ({typ})",
                    description=f"Entity '{name}' lacks an explicit negative boundary defining what it is not.",
                    source_reference=f"Entities.md row {eid}",
                    workflow_centrality=c,
                    evidence_severity=s,
                    verification_difficulty=d,
                )
            )
    return gaps


def scan_stage2_metrics(stage2_dir: Path) -> List[ResearchGap]:
    """Scan Metrics.md for unstated measurement conditions (GAP-CND).

    Trigger per Protocols/FollowUpResearch.md: Scope/conditions column is
    ``[conditions not stated in source]``.
    """
    metrics_file = stage2_dir / "Metrics.md"
    if not metrics_file.is_file():
        return []

    rows = parse_markdown_table_rows(metrics_file.read_text(encoding="utf-8"))
    gaps: List[ResearchGap] = []

    # Benchmarks for core engine choices are workflow-critical; everything
    # else defaults to medium centrality with severe evidence risk (a bare
    # number without conditions is misleading by design).
    core_metric_keywords = ("duckdb", "polars", "pandas", "motherduck", "arrow")

    for row in rows:
        mid = row.get("Metric ID", "")
        name = row.get("Metric name", "")
        scope = row.get("Scope / conditions", "")

        if "[conditions not stated in source]" in scope:
            lowered = f"{name}".lower()
            if any(k in lowered for k in core_metric_keywords):
                c, s, d = (5, 5, 2)
            else:
                c, s, d = (3, 5, 2)
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-CND-{mid}",
                    gap_code="GAP-CND",
                    target_concept=name or mid,
                    category="Metric Condition",
                    description=(
                        f"Metric '{name}' ({mid}) is recorded without measurement "
                        f"conditions (hardware, dataset scale, software version)."
                    ),
                    source_reference=f"Metrics.md row {mid}",
                    workflow_centrality=c,
                    evidence_severity=s,
                    verification_difficulty=d,
                )
            )
    return gaps


def _centrality_for_workflow_stage(workflow_stage: str) -> int:
    """Heuristic mapping from a claim's workflow stage to centrality (1-5)."""
    lowered = (workflow_stage or "").lower()
    if any(k in lowered for k in ("storage", "execution", "engine", "schema", "provenance")):
        return 5
    if any(k in lowered for k in ("orchestrat", "agent framework", "ingest", "citation")):
        return 4
    if any(k in lowered for k in ("visual", "bi ", "semantic", "benchmark")):
        return 3
    if workflow_stage.strip():
        return 3
    return 3


def scan_stage2_claims(stage2_dir: Path) -> List[ResearchGap]:
    """Scan Claims.md for epistemic and falsification gaps (GAP-EPI, GAP-FAL).

    Triggers per Protocols/FollowUpResearch.md:
    - GAP-EPI: Confidence is ``low`` (mapped primary-source counts come from
      the DuckDB ``next_research_candidates`` view instead).
    - GAP-FAL: Falsifier column is ``[falsifier not stated]``.
    """
    claims_file = stage2_dir / "Claims.md"
    if not claims_file.is_file():
        return []

    rows = parse_markdown_table_rows(claims_file.read_text(encoding="utf-8"))
    gaps: List[ResearchGap] = []

    for row in rows:
        cid = row.get("Claim ID", "")
        text = row.get("Claim text", "")
        confidence = (row.get("Confidence", "") or "").strip().lower()
        falsifier = row.get("Falsifier", "")
        workflow_stage = row.get("Workflow stage", "")

        concept = (text[:80] + "…") if len(text) > 80 else (text or cid)
        centrality = _centrality_for_workflow_stage(workflow_stage)

        if confidence == "low":
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-EPI-{cid}",
                    gap_code="GAP-EPI",
                    target_concept=concept,
                    category="Low-Confidence Claim",
                    description=(
                        f"Claim '{cid}' is recorded at low confidence and requires "
                        f"direct primary evidence to substantiate, bound, or refute it."
                    ),
                    source_reference=f"Claims.md row {cid}",
                    workflow_centrality=centrality,
                    evidence_severity=4,
                    verification_difficulty=1,
                )
            )

        if "[falsifier not stated]" in (falsifier or ""):
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-FAL-{cid}",
                    gap_code="GAP-FAL",
                    target_concept=concept,
                    category="Missing Falsifier",
                    description=(
                        f"Claim '{cid}' states no observable condition or failure mode "
                        f"that would disprove it."
                    ),
                    source_reference=f"Claims.md row {cid}",
                    workflow_centrality=centrality,
                    evidence_severity=3,
                    verification_difficulty=1,
                )
            )
    return gaps


def scan_stage2_extraction_log(stage2_dir: Path) -> List[ResearchGap]:
    """Scan ExtractionLog.md for omissions, open questions, and conflicts.

    Triggers per Protocols/FollowUpResearch.md:
    - GAP-OPN: Decision type is ``open_question`` or ``omission``.
    - GAP-CON: Decision type is ``classification_conflict``.
    - ``boundary_absent`` / ``condition_absent`` / ``falsifier_absent`` entries
      are provenance for the Entities/Metrics/Claims scans and are not
      double-counted here.
    """
    log_file = stage2_dir / "ExtractionLog.md"
    if not log_file.is_file():
        return []

    rows = parse_markdown_table_rows(log_file.read_text(encoding="utf-8"))
    gaps: List[ResearchGap] = []

    for row in rows:
        lid = row.get("Log ID", "")
        dec_type = row.get("Decision type", "")
        desc = row.get("Description", "")
        res = row.get("Resolution", "")

        if dec_type == "omission" and "Multiple URLs found" in desc:
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-OPN-{lid}",
                    gap_code="GAP-OPN",
                    target_concept=desc.split(":", 1)[1].strip() if ":" in desc else desc,
                    category="Bundled Source Disambiguation",
                    description=f"Multiple distinct documentation URLs were bundled into a single source entry: {desc}",
                    source_reference=f"ExtractionLog.md {lid}",
                    workflow_centrality=4,
                    evidence_severity=4,
                    verification_difficulty=1,
                )
            )
        elif dec_type == "omission" and "has no URL" in desc:
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-EPI-{lid}",
                    gap_code="GAP-EPI",
                    target_concept=desc,
                    category="Missing Direct URL",
                    description=f"Source entry lacks a resolvable direct URL: {desc}",
                    source_reference=f"ExtractionLog.md {lid}",
                    workflow_centrality=3,
                    evidence_severity=3,
                    verification_difficulty=1,
                )
            )
        elif dec_type == "open_question":
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-OPN-{lid}",
                    gap_code="GAP-OPN",
                    target_concept=desc,
                    category="Carried Open Question",
                    description=f"Unresolved trade-off or omitted architectural aspect carried from Stage 1: {desc}",
                    source_reference=f"ExtractionLog.md {lid}",
                    workflow_centrality=3,
                    evidence_severity=3,
                    verification_difficulty=1,
                )
            )
        elif dec_type == "classification_conflict":
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-CON-{lid}",
                    gap_code="GAP-CON",
                    target_concept=desc,
                    category="Classification Conflict",
                    description=(
                        f"Same source recorded with conflicting evidence classifications: {desc}"
                    ),
                    source_reference=f"ExtractionLog.md {lid}",
                    workflow_centrality=4,
                    evidence_severity=4,
                    verification_difficulty=2,
                )
            )
        elif dec_type == "omission":
            # Generic omission not matching a specialised sub-case above.
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-OPN-{lid}",
                    gap_code="GAP-OPN",
                    target_concept=desc,
                    category="Extraction Omission",
                    description=f"Content deliberately excluded from Stage 2 requires follow-up: {desc}",
                    source_reference=f"ExtractionLog.md {lid}",
                    workflow_centrality=3,
                    evidence_severity=3,
                    verification_difficulty=1,
                )
            )
    return gaps


def scan_duckdb_intelligence(db_path: Path) -> List[ResearchGap]:
    """Scan DuckDB for citation warnings, unresolved aliases, and candidate gaps.

    Covers per Protocols/FollowUpResearch.md:
    - GAP-CON from ``source_alias`` rows with ``match_method = 'unresolved'``.
    - GAP-EPI from ``source`` rows lacking a canonical URL.
    - GAP-EPI from the ``next_research_candidates`` view (claims without
      primary sources or at low confidence).
    """
    if not db_path.is_file():
        return []

    gaps: List[ResearchGap] = []
    con: Optional[duckdb.DuckDBPyConnection] = None
    try:
        con = duckdb.connect(str(db_path), read_only=True)
        # Check for unresolved aliases
        aliases = con.execute(
            "SELECT alias_id, alias, document_id FROM source_alias WHERE match_method = 'unresolved'"
        ).fetchall()
        for aid, alias, doc in aliases:
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-CON-{aid[:12]}",
                    gap_code="GAP-CON",
                    target_concept=alias,
                    category="Unresolved Source Alias",
                    description=f"Local citation alias '{alias}' in document '{doc}' has no unambiguous canonical source mapping.",
                    source_reference=f"citations.duckdb source_alias {aid}",
                    workflow_centrality=4,
                    evidence_severity=3,
                    verification_difficulty=1,
                )
            )

        # Check for sources lacking URLs
        no_url_sources = con.execute(
            "SELECT source_id, title FROM source WHERE canonical_url IS NULL OR canonical_url = ''"
        ).fetchall()
        for sid, title in no_url_sources:
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-EPI-{sid[:12]}",
                    gap_code="GAP-EPI",
                    target_concept=title,
                    category="Source Lacking Canonical URL",
                    description=f"Source record '{title}' has no canonical URL recorded.",
                    source_reference=f"citations.duckdb source {sid}",
                    workflow_centrality=3,
                    evidence_severity=3,
                    verification_difficulty=1,
                )
            )

        # Check the next_research_candidates view: claims without primary
        # sources or at low confidence (GAP-EPI per protocol).
        try:
            candidates = con.execute(
                "SELECT claim_id, claim_text, workflow_stage, confidence,"
                " mapped_sources, mapped_primary_sources, research_reason"
                " FROM next_research_candidates"
            ).fetchall()
        except Exception:
            candidates = []
        for claim_id, claim_text, workflow_stage, confidence, mapped, mapped_primary, reason in candidates:
            centrality = _centrality_for_workflow_stage(workflow_stage or "")
            if reason == "no mapped sources":
                severity = 5
            elif reason == "no mapped primary evidence":
                severity = 4
            else:  # low confidence / review
                severity = 3
            concept = (claim_text[:80] + "…") if claim_text and len(claim_text) > 80 else (claim_text or claim_id)
            gaps.append(
                ResearchGap(
                    gap_id=f"GAP-EPI-{claim_id[:12] if len(claim_id) > 12 else claim_id}",
                    gap_code="GAP-EPI",
                    target_concept=concept,
                    category=f"Citation Intelligence Flag ({reason})",
                    description=(
                        f"Claim '{claim_id}' flagged by next_research_candidates: {reason} "
                        f"(confidence={confidence}, mapped_sources={mapped}, "
                        f"mapped_primary={mapped_primary})."
                    ),
                    source_reference=f"citations.duckdb next_research_candidates {claim_id}",
                    workflow_centrality=centrality,
                    evidence_severity=severity,
                    verification_difficulty=1,
                )
            )
    except Exception:
        pass
    finally:
        if con is not None:
            con.close()

    return gaps


def formulate_question_from_gap(gap: ResearchGap, index: int) -> FormulatedQuestion:
    """Generate a fully formed, falsifiable research question dossier from a ResearchGap."""
    rq_id = f"RQ-{index:03d}"

    if gap.gap_code == "GAP-BND":
        title = f"Operational Boundary & Architectural Role of {gap.target_concept}"
        core_q = (
            f"What is the precise architectural boundary and operational scope of {gap.target_concept}, "
            f"and what adjacent technologies, roles, or formats does it explicitly NOT encompass?"
        )
        in_scope = f"{gap.target_concept} core definition, API surface, execution model, and primary deployment posture."
        out_of_scope = "Unverified marketing narratives, unreleased roadmap speculation."
        intended_use = f"Update Entities.md row for {gap.target_concept} with a verifiable 'Boundary (what it is not)' definition."
        min_evidence = "Primary documentation, official technical specifications, or author codebases."
        sources = [f"Official documentation for {gap.target_concept}", "Repository README/specifications"]
        res_crit = f"A clear, 1-2 sentence negative boundary stating exactly what {gap.target_concept} is not."
        falsifier = (
            f"Evidence demonstrating that {gap.target_concept} natively implements functionality previously assumed "
            f"to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format)."
        )

    elif gap.gap_code == "GAP-CND":
        title = f"Benchmark Conditions & Measurement Scope for {gap.target_concept[:50]}"
        core_q = (
            f"Under what exact hardware, dataset-scale, software-version, and configuration "
            f"conditions was '{gap.target_concept}' measured, and what are the reproduction steps?"
        )
        in_scope = (
            f"Measurement parameters for {gap.target_concept}: hardware, dataset scale, "
            f"software version, configuration, and reproduction steps."
        )
        out_of_scope = "Decontextualised vendor headline numbers; unrelated benchmark suites."
        intended_use = (
            f"Update Metrics.md row for {gap.target_concept} with a verifiable "
            f"'Scope / conditions' value and reassess confidence per TransitionStage2 Gate 4."
        )
        min_evidence = "Primary benchmark report, official documentation, or independent reproduction."
        sources = [
            "Official benchmark report or vendor technical documentation",
            "Independent reproduction or peer-reviewed evaluation",
        ]
        res_crit = (
            f"Recorded scope/conditions (hardware, dataset scale, version) for "
            f"{gap.target_concept} sufficient to reproduce the measurement."
        )
        falsifier = (
            f"Independent reproduction under stated conditions yielding a materially different "
            f"value, or primary documentation showing the metric applies to a different configuration."
        )

    elif gap.gap_code == "GAP-FAL":
        title = f"Falsification Criterion for Claim: {gap.target_concept[:50]}"
        core_q = (
            f"What specific observable condition, measurement, or failure mode would disprove "
            f"the claim '{gap.target_concept}'?"
        )
        in_scope = (
            f"Observable disproof conditions for '{gap.target_concept}': boundary cases, "
            f"counterexamples, and failure modes within the claimed workflow stage."
        )
        out_of_scope = "Speculative future capabilities; out-of-context uses of the claim."
        intended_use = (
            "Populate the Claims.md Falsifier column so the claim becomes testable per "
            "Research-Evaluation Gate E."
        )
        min_evidence = "Primary documentation, empirical test, or peer-reviewed analysis."
        sources = ["Official specification or primary source for the claim", "Independent empirical test"]
        res_crit = "A stated, observable falsifier recorded in Claims.md."
        falsifier = (
            f"Demonstration that no observable test could distinguish the claim from its negation "
            f"(claim is untestable as stated) — which itself forces a revise decision."
        )

    elif gap.gap_code == "GAP-OPN":
        if gap.category == "Bundled Source Disambiguation":
            title = f"Source Decoupling & Comparative Evaluation: {gap.target_concept[:40]}"
            core_q = (
                f"How do the distinct components in '{gap.target_concept}' differ in their evidence support, "
                f"and what are their independent canonical URLs and evidence tiers?"
            )
            in_scope = "Extracting independent source entries, canonical URLs, and distinct evidence classes for each bundled entity."
            out_of_scope = "Merging unrelated third-party blog commentary."
            intended_use = "Refactor Sources.md to separate bundled citations into atomic, single-URL records."
            min_evidence = "Primary documentation per individual project/standard."
            sources = [u.strip() for u in gap.target_concept.split("·") if u.strip().startswith("http")]
            if not sources:
                sources = ["Official specification or project documentation"]
            res_crit = "Separate atomic source rows with independent URLs, publishers, and publication dates."
            falsifier = "Official confirmation that the bundled projects share a single unified governance and specification."
        else:
            title = f"Resolution of Open Question: {gap.target_concept[:50]}"
            core_q = (
                f"What evidence resolves the carried open question '{gap.target_concept}', "
                f"and what trade-off or omitted architectural aspect does it settle?"
            )
            in_scope = (
                f"Evidence directly addressing '{gap.target_concept}' within the originating "
                f"Stage 1 scope and workflow stage."
            )
            out_of_scope = "Adjacent trade-offs not named in the originating log entry."
            intended_use = (
                "Resolve the ExtractionLog.md open question and, where applicable, promote the "
                "finding into Entities/Claims/Metrics rows."
            )
            min_evidence = "Primary documentation, official specification, or empirical evaluation."
            sources = ["Official specification or project documentation", "Originating Stage 1 source context"]
            res_crit = "A documented answer with primary citation that closes the log entry."
            falsifier = "Primary evidence showing the presumed trade-off does not exist as framed."

    elif gap.gap_code == "GAP-CON":
        if gap.category == "Classification Conflict":
            title = f"Classification Resolution for: {gap.target_concept[:50]}"
            core_q = (
                f"Which evidence classification (primary / secondary / internal) is authoritative for "
                f"'{gap.target_concept}', and what independent authority settles the conflict?"
            )
            in_scope = (
                f"Independent authority check on the conflicting classifications for "
                f"'{gap.target_concept}': publisher, authorship, and evidence tier."
            )
            out_of_scope = "Fuzzy re-labelling without consulting an independent authority."
            intended_use = "Record a single authoritative classification in Sources.md and close the log entry."
            min_evidence = "Primary publication record or independent bibliographic authority."
            sources = ["Publisher official record", "Independent bibliographic authority"]
            res_crit = "A single agreed classification with named independent authority."
            falsifier = "Authoritative record confirming both classifications apply to distinct editions or artefacts."
        else:
            title = f"Alias Disambiguation for Citation '{gap.target_concept}'"
            core_q = (
                f"What specific authoritative work, report, or specification does citation label '{gap.target_concept}' "
                f"refer to in its originating document?"
            )
            in_scope = f"Textual context in source document, canonical title, author, and URL for '{gap.target_concept}'."
            out_of_scope = "Fuzzy or speculative attribution without textual match."
            intended_use = "Map the unresolved alias in source_alias to a canonical source_id."
            min_evidence = "Primary citation text or original referenced document bibliography."
            sources = ["Originating Markdown document", "Author/publisher official archive"]
            res_crit = "Mapping to an unambiguous canonical URL and source_id."
            falsifier = "Evidence that the alias is an informal generic reference rather than a discrete citable source."

    else:
        title = f"Evidence Validation for {gap.target_concept[:40]}"
        core_q = f"What primary evidence substantiates or refutes the claims surrounding '{gap.target_concept}'?"
        in_scope = f"Primary source documentation and empirical verification for {gap.target_concept}."
        out_of_scope = "Secondary marketing summaries."
        intended_use = "Provide direct primary citation in Sources.md and update claim confidence."
        min_evidence = "Primary official documentation or peer-reviewed publication."
        sources = ["Official vendor/foundation specification"]
        res_crit = "Direct primary URL and publication metadata."
        falsifier = "Primary source contradicting the asserted capability or metric."

    return FormulatedQuestion(
        rq_id=rq_id,
        title=title,
        gap=gap,
        core_question=core_q,
        in_scope=in_scope,
        out_of_scope=out_of_scope,
        intended_use=intended_use,
        min_evidence_class=min_evidence,
        target_sources=sources,
        resolution_criteria=res_crit,
        falsifier=falsifier,
    )


def validate_questions(questions: List[FormulatedQuestion]) -> List[str]:
    """Validate quality gates A-D from Protocols/FollowUpResearch.md §6 Step 2.

    Returns a list of defect strings; an empty list means all gates pass.
    - Gate A (Scope): In Scope, Out of Scope, Intended Use all non-empty.
    - Gate B (Falsifier): falsifier non-empty and testable (min length).
    - Gate C (Provenance): gap.source_reference non-empty.
    - Gate D (Score Coverage): centrality/severity/difficulty within range.
    """
    defects: List[str] = []
    for q in questions:
        if not q.in_scope.strip() or not q.out_of_scope.strip() or not q.intended_use.strip():
            defects.append(f"{q.rq_id}: Gate A failure — scope fields incomplete.")
        if len((q.falsifier or "").strip()) < 20:
            defects.append(f"{q.rq_id}: Gate B failure — falsifier empty or non-testable.")
        if not (q.gap.source_reference or "").strip():
            defects.append(f"{q.rq_id}: Gate C failure — missing provenance reference.")
        c, s, d = q.gap.workflow_centrality, q.gap.evidence_severity, q.gap.verification_difficulty
        if not (1 <= c <= 5 and 1 <= s <= 5 and 1 <= d <= 3):
            defects.append(f"{q.rq_id}: Gate D failure — scores out of range (C={c}, E={s}, D={d}).")
        if not (q.min_evidence_class or "").strip() or not q.target_sources:
            defects.append(f"{q.rq_id}: Gate A failure — target evidence class/sources missing.")
    return defects


def build_research_agenda_markdown(questions: List[FormulatedQuestion]) -> str:
    """Generate master ResearchAgenda.md markdown content."""
    lines: List[str] = [
        "# Follow-Up Research Agenda",
        "",
        "## Executive Summary",
        "",
        f"This research agenda was systematically formulated from the Stage 2 extraction layer (`research/raw/Stage 2/`) "
        f"and the citation intelligence database (`data/citations.duckdb`), governed by `Protocols/FollowUpResearch.md`.",
        "",
        f"- **Total Research Questions Formulated:** {len(questions)}",
        f"- **P1 (Immediate Priority):** {sum(1 for q in questions if q.gap.priority_tier == 'P1')}",
        f"- **P2 (Scheduled Waves):** {sum(1 for q in questions if q.gap.priority_tier == 'P2')}",
        f"- **P3 (Backlog / Opportunistic):** {sum(1 for q in questions if q.gap.priority_tier == 'P3')}",
        "",
        "---",
        "",
        "## Priority Ranking Table",
        "",
        "| Question ID | Title | Gap Code | Category | Score | Tier |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]

    for q in sorted(questions, key=lambda x: x.gap.priority_score, reverse=True):
        lines.append(
            f"| [{q.rq_id}](#{q.rq_id.lower()}) | {q.title} | `{q.gap.gap_code}` | {q.gap.category} | "
            f"{q.gap.priority_score:.1f} | **{q.gap.priority_tier}** |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## Formulated Research Question Dossiers",
        "",
    ])

    for q in sorted(questions, key=lambda x: x.gap.priority_score, reverse=True):
        lines.extend([
            f"<a id=\"{q.rq_id.lower()}\"></a>",
            f"### [{q.rq_id}] {q.title}",
            "",
            f"- **Priority Tier:** **{q.gap.priority_tier}** (Priority Score: **{q.gap.priority_score:.1f}**)",
            f"- **Gap Code:** `{q.gap.gap_code}` ({q.gap.category})",
            f"- **Trigger Reference:** `{q.gap.source_reference}`",
            f"- **Scoring Breakdown:** Workflow Centrality = {q.gap.workflow_centrality}/5 | Evidence Severity = {q.gap.evidence_severity}/5 | Difficulty = {q.gap.verification_difficulty}/3",
            "",
            "#### 1. Core Research Question",
            f"> {q.core_question}",
            "",
            "#### 2. Scope & Boundaries",
            f"- **In Scope:** {q.in_scope}",
            f"- **Out of Scope:** {q.out_of_scope}",
            f"- **Intended Downstream Use:** {q.intended_use}",
            "",
            "#### 3. Target Evidence & Sources",
            f"- **Minimum Evidence Class:** `{q.min_evidence_class}`",
            "- **Target Sources:**",
        ])
        for s in q.target_sources:
            lines.append(f"  - {s}")
        lines.extend([
            "",
            "#### 4. Falsification & Resolution Criteria",
            f"- **Resolution Condition:** {q.resolution_criteria}",
            f"- **Falsifier:** {q.falsifier}",
            "",
            "---",
            "",
        ])

    return "\n".join(lines)

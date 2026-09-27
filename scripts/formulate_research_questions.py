"""CLI tool to formulate follow-up research questions from Stage 2 extraction and citation database.

Writes the formulated research agenda into research/processed/FollowUps/ResearchAgenda.md.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.followup_core import (  # noqa: E402
    build_research_agenda_markdown,
    formulate_question_from_gap,
    scan_duckdb_intelligence,
    scan_stage2_entities,
    scan_stage2_extraction_log,
)


def run_formulation(
    stage2_dir: Path,
    database_path: Path,
    output_dir: Path,
) -> int:
    """Execute the post-TransitionStage2 question formulation pipeline."""
    if not stage2_dir.is_dir():
        print(f"Error: Stage 2 directory not found: {stage2_dir}", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[Follow-Up Formulation Pipeline]")
    print(f"  Stage 2 Source: {stage2_dir}")
    print(f"  Database:       {database_path}")
    print(f"  Output Dir:     {output_dir}\n")

    # 1. Collect Gaps
    print("1. Scanning Stage 2 extraction artifacts and DuckDB views...")
    entity_gaps = scan_stage2_entities(stage2_dir)
    print(f"   Found {len(entity_gaps)} entity boundary gaps (GAP-BND).")

    log_gaps = scan_stage2_extraction_log(stage2_dir)
    print(f"   Found {len(log_gaps)} extraction log gaps (GAP-OPN / GAP-EPI).")

    db_gaps = scan_duckdb_intelligence(database_path)
    print(f"   Found {len(db_gaps)} citation database gaps (GAP-CON / GAP-EPI).")

    all_gaps = entity_gaps + log_gaps + db_gaps
    if not all_gaps:
        print("No gaps identified across Stage 2 and database.")
        return 0

    print(f"\n2. Total gaps detected: {len(all_gaps)}")

    # 2. Formulate Questions
    print("3. Formulating scoped research questions & calculating priority scores...")
    questions = []
    for idx, gap in enumerate(all_gaps, start=1):
        q = formulate_question_from_gap(gap, idx)
        questions.append(q)

    # Sort descending by priority score
    questions.sort(key=lambda x: x.gap.priority_score, reverse=True)

    # Summary counts
    p1_count = sum(1 for q in questions if q.gap.priority_tier == "P1")
    p2_count = sum(1 for q in questions if q.gap.priority_tier == "P2")
    p3_count = sum(1 for q in questions if q.gap.priority_tier == "P3")

    print(f"   Prioritization summary: {p1_count} P1 (Immediate), {p2_count} P2 (Scheduled), {p3_count} P3 (Backlog)")

    # 3. Emit Markdown Outputs
    agenda_path = output_dir / "ResearchAgenda.md"
    print(f"\n4. Emitting Master Research Agenda to: {agenda_path}")
    agenda_content = build_research_agenda_markdown(questions)
    agenda_path.write_text(agenda_content, encoding="utf-8")

    # Modular Thematic Packs
    bnd_questions = [q for q in questions if q.gap.gap_code == "GAP-BND"]
    src_questions = [q for q in questions if q.gap.gap_code != "GAP-BND"]

    bnd_path = output_dir / "Wave2_Entity_Boundaries.md"
    src_path = output_dir / "Wave2_Source_Decoupling.md"

    bnd_path.write_text(build_research_agenda_markdown(bnd_questions), encoding="utf-8")
    src_path.write_text(build_research_agenda_markdown(src_questions), encoding="utf-8")

    print(f"   Emitted thematic pack: {bnd_path} ({len(bnd_questions)} questions)")
    print(f"   Emitted thematic pack: {src_path} ({len(src_questions)} questions)")

    print(f"\n[SUCCESS] Formulated {len(questions)} research questions in {output_dir}")
    print(f"  Master Agenda:    {agenda_path}")
    print(f"  Entity Pack:      {bnd_path}")
    print(f"  Source/Alias Pack:{src_path}\n")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Formulate post-TransitionStage2 follow-up research questions.")
    parser.add_argument(
        "--stage2-dir",
        type=Path,
        default=PROJECT_ROOT / "research" / "raw" / "Stage 2",
        help="Directory containing Stage 2 extraction files (default: research/raw/Stage 2)",
    )
    parser.add_argument(
        "--database",
        type=Path,
        default=PROJECT_ROOT / "data" / "citations.duckdb",
        help="Path to citations.duckdb database (default: data/citations.duckdb)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_ROOT / "research" / "processed" / "FollowUps",
        help="Directory to write formulated research questions to (default: research/processed/FollowUps)",
    )

    args = parser.parse_args()
    sys.exit(
        run_formulation(
            stage2_dir=args.stage2_dir,
            database_path=args.database,
            output_dir=args.output_dir,
        )
    )


if __name__ == "__main__":
    main()

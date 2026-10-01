"""Tier 1 prompt lint (see Commander Deck/Active/Plans/OptimalSPrompt.md §5)
and prompt-assembler tests.

Rules R1-R5 run against the real library and must return zero violations.
Each rule also gets a positive control proving the checker catches a seeded
violation, so the test fails before the fix and passes after it.
"""

from __future__ import annotations

import pytest

from scripts.assemble_prompt import assemble, build_context
from src.prompt_core import (
    PromptRenderError,
    check_bare_gates,
    check_commands,
    check_includes,
    check_paths,
    check_template_purity,
    extract_commands,
    find_bare_gates,
    looks_like_repo_path,
    parse_frontmatter,
    render,
    resolve_includes,
    template_violations,
)


# --- R1: every include target resolves ------------------------------------

def test_r1_library_includes_resolve():
    assert check_includes() == []


def test_r1_flags_missing_include(tmp_path):
    (tmp_path / "a.md").write_text(
        "<!-- include: lib/missing.md -->", encoding="utf-8")
    assert any("unresolved include" in v for v in check_includes(tmp_path))


def test_r1_include_cycle_is_rejected(tmp_path):
    (tmp_path / "a.md").write_text("<!-- include: b.md -->", encoding="utf-8")
    (tmp_path / "b.md").write_text("<!-- include: a.md -->", encoding="utf-8")
    with pytest.raises(ValueError, match="cycle"):
        resolve_includes("<!-- include: a.md -->", tmp_path)


# --- R2: qualified gate IDs only ------------------------------------------

def test_r2_library_has_no_bare_gates():
    assert check_bare_gates() == []


def test_r2_flags_bare_and_accepts_qualified():
    assert find_bare_gates("check Gate E") == ["Gate E"]
    assert find_bare_gates("Gates A-D collide") == ["Gates A"]
    assert find_bare_gates("check `FU:Gate B` and `RE:Gate F`") == []
    assert find_bare_gates("quality gates, and feedback loops") == []


def test_r2_checker_reports_seeded_violation(tmp_path):
    (tmp_path / "x.md").write_text("Gate E is falsification", encoding="utf-8")
    assert check_bare_gates(tmp_path)


# --- R3: rule blocks live in lib/ only ------------------------------------

def test_r3_templates_are_pure():
    assert check_template_purity() == []


def test_r3_flags_seeded_rule_blocks():
    assert template_violations(r"Run .venv\Scripts\python.exe x now") != []
    assert template_violations("a documented fact, a reported signal") != []
    assert template_violations("Prefer primary sources.") != []
    assert template_violations("neutral task instructions only") == []


def test_r3_claim_vocabulary_must_be_unique(tmp_path):
    tdir = tmp_path / "templates"
    tdir.mkdir()
    (tdir / "bad.md").write_text(
        "documented fact / reported signal", encoding="utf-8")
    assert any("claim-type vocabulary" in v
               for v in check_template_purity(tmp_path))


# --- R4: referenced paths exist -------------------------------------------

def test_r4_all_referenced_paths_exist():
    assert check_paths() == []


def test_r4_path_heuristics():
    assert looks_like_repo_path("research/raw/Stage 2/Entities.md")
    assert looks_like_repo_path("src/prompt_core.py")
    assert not looks_like_repo_path("Wave2_Entity_Boundaries.md")  # bare name
    assert not looks_like_repo_path("research/processed/FollowUps/<date>_wave.md")  # placeholder
    assert not looks_like_repo_path("https://example.com/docs")  # URL
    assert not looks_like_repo_path(r".venv\Scripts\python.exe")  # command


def test_r4_flags_missing_frontmatter_input(tmp_path):
    (tmp_path / "t.md").write_text(
        "---\ninputs:\n  - does/not/exist.md\n---\nbody\n", encoding="utf-8")
    assert any("frontmatter input missing" in v for v in check_paths(tmp_path))


# --- R5: commands match AGENTS.md verbatim --------------------------------

def test_r5_commands_match_agents_md():
    assert check_commands() == []


def test_r5_extracts_and_flags_unknown_command(tmp_path):
    text = r"Run `.venv\Scripts\python.exe -m pytest src/tests -q` now"
    assert extract_commands(text) == [
        r".venv\Scripts\python.exe -m pytest src/tests -q"]
    (tmp_path / "p.md").write_text(text, encoding="utf-8")
    agents = tmp_path / "AGENTS.md"
    agents.write_text("no commands documented here", encoding="utf-8")
    assert any("not verbatim" in v for v in check_commands(tmp_path, agents))


def test_r5_strips_variable_flags():
    text = (r"cmd `.venv\Scripts\python.exe scripts/assemble_prompt.py "
            r"--template x --out y` end")
    assert extract_commands(text) == [
        r".venv\Scripts\python.exe scripts/assemble_prompt.py"]


# --- assembler (Layer 2 compositor) ---------------------------------------

def test_assemble_research_brief_end_to_end():
    out = assemble("research_brief", {})
    assert "<!-- include:" not in out
    assert "Evidence class hierarchy" in out      # inlined from lib/evidence_rules
    assert "### 1. Executive synthesis" in out    # inlined from lib/deliverable_brief
    assert "RE:Gate A" in out
    assert "{{" not in out


def test_assemble_followup_dispatch_end_to_end():
    out = assemble("followup_dispatch", {})
    assert "<!-- include:" not in out
    assert "Tier 1 (Primary / Authoritative)" in out
    assert "FU:Gate A" in out
    assert "RQ-001" in out                        # dispatch data intact


def test_assemble_unknown_template_raises():
    with pytest.raises(FileNotFoundError):
        assemble("no_such_template", {})


def test_render_substitutes_and_fails_loudly():
    assert render("Hello {{name}}", {"name": "world"}) == "Hello world"
    with pytest.raises(PromptRenderError, match="missing template variables: name"):
        render("Hello {{name}}", {})


def test_build_context_merges_vars_and_json(tmp_path):
    ctx = tmp_path / "ctx.json"
    ctx.write_text('{"wave": "Wave2"}', encoding="utf-8")
    assert build_context(["tier=P1"], str(ctx)) == {"wave": "Wave2", "tier": "P1"}
    with pytest.raises(PromptRenderError):
        build_context(["novalue"], None)


def test_parse_frontmatter_scalars_and_lists():
    meta, body = parse_frontmatter(
        "---\nid: x\ninputs:\n  - a/b.md\n  - c/d.md\n---\nBody")
    assert meta["id"] == "x"
    assert meta["inputs"] == ["a/b.md", "c/d.md"]
    assert body.strip() == "Body"
    assert parse_frontmatter("no frontmatter here")[0] == {}

"""Core logic for the prompt library: assembly and Tier 1 lint.

Assembly: resolve ``<!-- include: ... -->`` markers and ``{{var}}`` placeholders.

Tier 1 lint rules (see Commander Deck/Active/Plans/OptimalSPrompt.md, section 5):

R1  every include target resolves to a file under ``prompts/``.
R2  no bare gate letters anywhere: qualified IDs only
    (``RE:Gate A``..``RE:Gate F``, ``FU:Gate A``..``FU:Gate D``, ``WB:n``).
R3  evidence-rule, claim-type, and command blocks live in ``lib/`` only, and
    the claim-type vocabulary exists in exactly one file
    (``lib/claim_taxonomy.md``).
R4  every repo path named in a prompt exists (frontmatter ``inputs``/
    ``partials`` and inline backtick paths); generated artifacts under
    ``data/`` are exempt because they are regenerable and gitignored.
R5  verification commands match ``AGENTS.md`` verbatim (interpreter + script
    path; variable ``--flags`` are ignored for matching).

Core logic lives here (``src/``); the thin CLI is
``scripts/assemble_prompt.py``; tests are ``src/tests/test_prompts.py``.
"""

from __future__ import annotations

import re
from pathlib import Path, PurePosixPath
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_ROOT = ROOT / "prompts"
AGENTS_FILE = ROOT / "AGENTS.md"

INCLUDE_RE = re.compile(r"<!--\s*include:\s*([^\s>]+)\s*-->")
VAR_RE = re.compile(r"\{\{\s*([A-Za-z_][A-Za-z0-9_-]*)\s*\}\}")
BARE_GATE_RE = re.compile(r"\bGates?\s+([A-F])\b")
QUALIFIED_GATE_RE = re.compile(r"\b(?:RE|FU):Gate\s+[A-F]\b")
COMMAND_RE = re.compile(r"\.venv[\\/]Scripts[\\/]python(?:\.exe)?[^\n`]*")
SPAN_RE = re.compile(r"`([^`\n]+)`")

CLAIM_PAIR = ("documented fact", "reported signal")
CLAIM_VOCAB_FILE = "lib/claim_taxonomy.md"
FORBIDDEN_IN_TEMPLATES = ("Prefer primary sources", "Tier 1 (Primary")
GENERATED_PREFIXES = ("data/",)
PATH_SUFFIXES = {".md", ".py", ".sql", ".json", ".jsonl", ".txt", ".yaml", ".yml", ".toml", ".ini"}
PLACEHOLDER_CHARS = set("<>{}*[]|+,")


class PromptRenderError(ValueError):
    """Raised when a template variable cannot be resolved."""


def iter_markdown(root: Path) -> List[Path]:
    """All Markdown files under root, sorted for deterministic output."""
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def parse_frontmatter(text: str) -> Tuple[Dict[str, object], str]:
    """Parse the YAML-subset frontmatter (scalars and simple string lists)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text
    meta: Dict[str, object] = {}
    list_key = None
    for raw in lines[1:end]:
        line = raw.strip()
        if not line:
            continue
        if line.startswith("- ") and list_key is not None:
            meta[list_key].append(line[2:].strip())  # type: ignore[union-attr]
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            key, value = key.strip(), value.strip()
            if value:
                meta[key] = value
                list_key = None
            else:
                meta[key] = []
                list_key = key
    return meta, "\n".join(lines[end + 1:])


def resolve_includes(text: str, prompts_root: Path = PROMPTS_ROOT,
                     stack: Tuple[Path, ...] = ()) -> str:
    """Recursively inline every include target; raise on missing or cyclic."""

    def repl(match: "re.Match[str]") -> str:
        rel = match.group(1)
        target = (prompts_root / rel).resolve()
        if not target.is_file():
            raise FileNotFoundError(f"include target not found: {rel}")
        if target in stack:
            chain = " -> ".join(str(p.name) for p in stack + (target,))
            raise ValueError(f"include cycle: {chain}")
        content = target.read_text(encoding="utf-8")
        return resolve_includes(content, prompts_root, stack + (target,))

    return INCLUDE_RE.sub(repl, text)


def render(text: str, context: Dict[str, str]) -> str:
    """Substitute ``{{name}}`` placeholders; fail loudly on missing names."""
    missing = set()

    def repl(match: "re.Match[str]") -> str:
        name = match.group(1)
        if name not in context:
            missing.add(name)
            return match.group(0)
        return str(context[name])

    out = VAR_RE.sub(repl, text)
    if missing:
        raise PromptRenderError(
            "missing template variables: " + ", ".join(sorted(missing)))
    return out


def find_bare_gates(text: str) -> List[str]:
    """Bare gate references (unqualified letters) in text — R2."""
    stripped = QUALIFIED_GATE_RE.sub("", text)
    return [m.group(0) for m in BARE_GATE_RE.finditer(stripped)]


def _display(path: Path, root: Path) -> str:
    """Repo-relative path when possible; falls back to the checker's root."""
    for base in (ROOT, root):
        try:
            return str(path.relative_to(base))
        except ValueError:
            continue
    return str(path)


def template_violations(text: str) -> List[str]:
    """Rule-block violations for template files — R3 (templates only)."""
    out: List[str] = []
    if COMMAND_RE.search(text):
        out.append("command block outside lib/ (use <!-- include: lib/verification.md -->)")
    if all(term in text for term in CLAIM_PAIR):
        out.append("claim-type vocabulary duplicated (belongs in lib/claim_taxonomy.md)")
    for phrase in FORBIDDEN_IN_TEMPLATES:
        if phrase in text:
            out.append(f"evidence-rule phrase duplicated: {phrase!r}")
    return out


def extract_commands(text: str) -> List[str]:
    """Interpreter+script commands in text; variable ``--flags`` stripped."""
    cmds: List[str] = []
    for match in COMMAND_RE.finditer(text):
        cmd = match.group(0)
        if " --" in cmd:
            cmd = cmd.split(" --", 1)[0]
        cmd = cmd.rstrip()
        if cmd and cmd not in cmds:
            cmds.append(cmd)
    return cmds


def looks_like_repo_path(span: str) -> bool:
    """True when a backtick span plausibly names a repo file or directory."""
    s = span.strip()
    if not s or s.startswith(("http://", "https://", ".")):
        return False
    if any(ch in s for ch in PLACEHOLDER_CHARS):
        return False
    if "\\" in s or ".venv" in s:
        return False
    if "/" not in s:
        return False
    if s.endswith("/"):
        return True
    return PurePosixPath(s).suffix.lower() in PATH_SUFFIXES


def path_exists_in_repo(span: str, root: Path = ROOT) -> bool:
    """Resolve against the repo root, then against prompts/ (for lib/ etc.)."""
    if span.startswith(GENERATED_PREFIXES):
        return True  # regenerable artifacts (duckdb, jsonl) — gitignored
    return (root / span).exists() or (root / "prompts" / span).exists()


def check_includes(root: Path = PROMPTS_ROOT) -> List[str]:
    """R1: every include target resolves."""
    violations: List[str] = []
    for file in iter_markdown(root):
        for rel in INCLUDE_RE.findall(file.read_text(encoding="utf-8")):
            if not (root / rel).is_file():
                violations.append(f"{_display(file, root)}: unresolved include -> {rel}")
    return violations


def check_bare_gates(root: Path = PROMPTS_ROOT) -> List[str]:
    """R2: no unqualified gate letters."""
    violations: List[str] = []
    for file in iter_markdown(root):
        found = find_bare_gates(file.read_text(encoding="utf-8"))
        for gate in found:
            violations.append(f"{_display(file, root)}: bare gate reference {gate!r}")
    return violations


def check_template_purity(root: Path = PROMPTS_ROOT) -> List[str]:
    """R3: rule blocks only in lib/, claim vocabulary exactly once."""
    violations: List[str] = []
    templates = root / "templates"
    if templates.is_dir():
        for file in iter_markdown(templates):
            for msg in template_violations(file.read_text(encoding="utf-8")):
                violations.append(f"{_display(file, root)}: {msg}")
    holders = [
        f for f in iter_markdown(root)
        if all(term in f.read_text(encoding="utf-8") for term in CLAIM_PAIR)
    ]
    expected = (root / CLAIM_VOCAB_FILE).resolve()
    if holders != [expected]:
        names = ", ".join(str(h.relative_to(root)) for h in holders) or "none"
        violations.append(
            f"claim-type vocabulary must exist only in {CLAIM_VOCAB_FILE} (found: {names})")
    return violations


def check_paths(root: Path = PROMPTS_ROOT) -> List[str]:
    """R4: frontmatter inputs/partials and inline backtick paths exist."""
    violations: List[str] = []
    for file in iter_markdown(root):
        text = file.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(text)
        rel = _display(file, root)
        for item in meta.get("inputs", []) if isinstance(meta.get("inputs"), list) else []:
            if not item.startswith(GENERATED_PREFIXES) and not (ROOT / item).exists():
                violations.append(f"{rel}: frontmatter input missing -> {item}")
        for item in meta.get("partials", []) if isinstance(meta.get("partials"), list) else []:
            if not (root / item).is_file():
                violations.append(f"{rel}: frontmatter partial missing -> {item}")
        for span in SPAN_RE.findall(text):
            if looks_like_repo_path(span) and not path_exists_in_repo(span, ROOT):
                violations.append(f"{rel}: referenced path missing -> {span}")
    return violations


def check_commands(root: Path = PROMPTS_ROOT,
                   agents_file: Path = AGENTS_FILE) -> List[str]:
    """R5: commands in prompts appear verbatim in AGENTS.md."""
    violations: List[str] = []
    agents = agents_file.read_text(encoding="utf-8")
    for file in iter_markdown(root):
        for cmd in extract_commands(file.read_text(encoding="utf-8")):
            if cmd not in agents:
                violations.append(
                    f"{_display(file, root)}: command not verbatim in AGENTS.md -> {cmd}")
    return violations


def run_all_checks(root: Path = PROMPTS_ROOT) -> List[str]:
    """Run R1..R5; returns the combined violation list (empty means clean)."""
    return (check_includes(root) + check_bare_gates(root)
            + check_template_purity(root) + check_paths(root)
            + check_commands(root))


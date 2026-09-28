"""Assemble a prompt: resolve <!-- include: --> markers and {{var}} placeholders.

Thin CLI over src/prompt_core.py. Examples (run from the repo root):

  .venv\\Scripts\\python.exe scripts/assemble_prompt.py --template research_brief
  .venv\\Scripts\\python.exe scripts/assemble_prompt.py --template followup_dispatch --out prompts/dispatch/2026-09-28_wave2.md
  .venv\\Scripts\\python.exe scripts/assemble_prompt.py --template next_research --var wave=Wave2
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.prompt_core import (  # noqa: E402
    PROMPTS_ROOT,
    PromptRenderError,
    render,
    resolve_includes,
)


def build_context(var_args: List[str], context_file: str | None) -> Dict[str, str]:
    """Merge --context FILE.json with repeated --var NAME=VALUE flags."""
    context: Dict[str, str] = {}
    if context_file:
        data = json.loads(Path(context_file).read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise PromptRenderError("context file must contain a JSON object")
        context.update({str(k): str(v) for k, v in data.items()})
    for item in var_args:
        if "=" not in item:
            raise PromptRenderError(f"--var expects NAME=VALUE, got: {item}")
        name, _, value = item.partition("=")
        context[name.strip()] = value
    return context


def resolve_template(template: str) -> Path:
    """Accept a bare template id or a path to a .md file."""
    direct = Path(template)
    if direct.is_file():
        return direct
    candidate = PROMPTS_ROOT / "templates" / f"{template}.md"
    if candidate.is_file():
        return candidate
    raise FileNotFoundError(
        f"template not found: {template!r} (tried {candidate})")


def assemble(template: str, context: Dict[str, str]) -> str:
    """Load a template, inline its includes, substitute variables."""
    path = resolve_template(template)
    text = path.read_text(encoding="utf-8")
    return render(resolve_includes(text), context)


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Assemble a prompt template into a dispatch-ready prompt.")
    parser.add_argument("--template", required=True,
                        help="template id under prompts/templates/ or a .md path")
    parser.add_argument("--var", action="append", default=[], metavar="NAME=VALUE",
                        help="template variable (repeatable)")
    parser.add_argument("--context", metavar="FILE",
                        help="JSON file with template variables")
    parser.add_argument("--out", metavar="PATH",
                        help="write here instead of stdout")
    args = parser.parse_args(argv)

    try:
        context = build_context(args.var, args.context)
        output = assemble(args.template, context)
    except (PromptRenderError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
        print(f"Wrote {out_path} ({len(output)} chars)", file=sys.stderr)
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

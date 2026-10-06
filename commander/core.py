"""Commander core: the single source of truth for the project vocabulary.

Loads places.json (the decoder table) and implements the operations both
front-ends expose — the web dashboard and the MCP server:

    resolve(place, kind, name)  -> full target path, disk untouched
    create(place, kind, name)   -> file from template, never overwrites
    compose(action, ...)        -> one coherent message for an agent
"""
from __future__ import annotations

import json
import os
import re
import threading
from datetime import date
from pathlib import Path

COMMANDER_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = COMMANDER_DIR.parent
PLACES_FILE = COMMANDER_DIR / "places.json"
TEMPLATES_DIR = COMMANDER_DIR / "templates"

ACTIONS = ("create", "read", "edit")

# Windows reserves these device names regardless of extension
_RESERVED_STEMS = {"CON", "PRN", "AUX", "NUL",
                   *(f"COM{i}" for i in range(1, 10)),
                   *(f"LPT{i}" for i in range(1, 10))}
MAX_STEM = 100


def load_vocab() -> dict:
    with open(PLACES_FILE, encoding="utf-8") as f:
        return json.load(f)


def _safe_stem(name: str) -> str:
    stem = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", name.strip()).strip(". ")
    if stem.upper() in _RESERVED_STEMS:
        stem = "-" + stem
    return stem[:MAX_STEM] or "untitled"


def _place_entry(place: str) -> tuple[str, dict]:
    vocab = load_vocab()
    code = place.strip().upper()
    entry = vocab["places"].get(code)
    if entry is None:
        known = ", ".join(vocab["places"])
        raise KeyError(f"Unknown place '{place}'. Known codes: {known}")
    return code, entry


def _kind_entry(kind: str) -> dict:
    vocab = load_vocab()
    key = kind.strip().lower()
    entry = vocab["kinds"].get(key)
    if entry is None:
        known = ", ".join(vocab["kinds"])
        raise KeyError(f"Unknown kind '{kind}'. Known kinds: {known}")
    return entry


def resolve(place: str, kind: str | None = None, name: str | None = None) -> Path:
    """Expand a code into the full target path. Does not touch the disk."""
    code, entry = _place_entry(place)
    base = Path(entry["path"])
    if not base.is_absolute():
        base = PROJECT_ROOT / base
    if kind is None:
        return base
    stem = _safe_stem(name or "untitled")
    return base / f"{stem}{_kind_entry(kind)['ext']}"


_CREATE_LOCK = threading.Lock()


def create(place: str, kind: str, name: str | None = None) -> Path:
    """Create the file from its template. Never overwrites: the target name is
    claimed atomically (O_CREAT|O_EXCL), so parallel creates of the same name
    get unique files, both within this process and across the two front-ends."""
    with _CREATE_LOCK:
        target = resolve(place, kind, name)
        target.parent.mkdir(parents=True, exist_ok=True)
        n = 2
        while True:
            try:
                fd = os.open(str(target), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                break
            except FileExistsError:
                target = target.parent / f"{target.stem}-{n}{target.suffix}"
                n += 1
        os.close(fd)
        if target.suffix == ".duckdb":
            os.unlink(target)  # connect() needs to create the db itself
            import duckdb
            duckdb.connect(str(target)).close()
        else:
            template = _kind_entry(kind).get("template")
            if template:
                body = (TEMPLATES_DIR / template).read_text(encoding="utf-8")
                body = body.replace("{{name}}", target.stem).replace("{{date}}", date.today().isoformat())
            else:
                body = ""
            target.write_text(body, encoding="utf-8")
    return target


def compose(action: str, place: str, kind: str | None = None,
            name: str | None = None, instruction: str = "") -> str:
    """Build the one coherent message an agent can execute as-is."""
    action = action.strip().lower()
    if action not in ACTIONS:
        raise KeyError(f"Unknown action '{action}'. Known actions: {', '.join(ACTIONS)}")
    code, entry = _place_entry(place)
    full = resolve(place, kind, name)
    if kind:
        msg = f"In {code} ({entry['desc']}, at {full.parent}): {action} `{full.name}`"
    else:
        msg = f"In {code} ({entry['desc']}, at {full}): {action} this directory"
    if instruction.strip():
        msg += f". Instruction: {instruction.strip()}"
    return msg

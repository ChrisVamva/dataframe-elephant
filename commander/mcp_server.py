"""Commander MCP server (FastMCP, stdio) — for goose.

Exposes the same vocabulary as the dashboard, as structured tools.
Per the house recipe: never print() to stdout (breaks JSON-RPC), return
plain strings, handle exceptions instead of raising.
"""
from __future__ import annotations

import json

from fastmcp import FastMCP

import core

mcp = FastMCP("commander")


@mcp.tool
def places() -> str:
    """Return the project decoder table: place codes -> directories (with descriptions), and the file kinds available."""
    return json.dumps(core.load_vocab(), indent=2)


@mcp.tool
def create(place: str, kind: str, name: str = "") -> str:
    """Create a new file from its template. place: a code from places(); kind: py | md | duckdb; name: file name without extension (optional). Returns the canonical expanded path. Never overwrites - uniquifies instead."""
    try:
        path = core.create(place, kind, name or None)
        return f"Created {path}"
    except Exception as exc:
        return f"Error: {exc}"


@mcp.tool
def compose(action: str, place: str, kind: str = "", name: str = "", instruction: str = "") -> str:
    """Build one coherent instruction message and return it to the user as text.
    The message is FOR THE HUMAN to send to an agent later - do NOT execute it
    yourself and do not create the files it mentions. action: create | read | edit;
    place: a code from places(); kind/name optional; instruction: the human's judgement sentence."""
    try:
        return core.compose(action, place, kind or None, name or None, instruction)
    except Exception as exc:
        return f"Error: {exc}"


if __name__ == "__main__":
    mcp.run()

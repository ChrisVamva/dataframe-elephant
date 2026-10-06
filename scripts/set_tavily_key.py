"""Inject your Tavily API key into goose's config locally.

The key never passes through any chat or cloud service: you run this script,
it prompts (hidden input), validates the key against Tavily's API, writes it
into config.yaml in place of the __TAVILY_KEY__ placeholder, and disables the
DuckDuckGo websearch fallback.

Run: double-click set_tavily_key.bat (or: python scripts/set_tavily_key.py)
"""
import getpass
import json
import re
import sys
import urllib.request
from pathlib import Path

CONFIG = Path(r"C:\Users\user\AppData\Roaming\Block\goose\config\config.yaml")
PLACEHOLDER = "__TAVILY_KEY__"


def validate_key(key: str) -> tuple[bool, str]:
    req = urllib.request.Request(
        "https://api.tavily.com/search",
        data=json.dumps({"query": "connection test", "max_results": 1}).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = json.loads(resp.read())
            n = len(body.get("results", []))
            return True, f"key works - test search returned {n} result(s)"
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            return False, "key rejected by Tavily (401/403) - check it on app.tavily.com"
        return False, f"Tavily returned HTTP {e.code}"
    except Exception as exc:
        return False, f"could not reach Tavily: {exc}"


def main() -> None:
    text = CONFIG.read_text(encoding="utf-8")
    if PLACEHOLDER not in text:
        print("Config already has a key injected (no placeholder found). Nothing to do.")
        return

    key = getpass.getpass("Paste your Tavily API key (input hidden): ").strip()
    if not key.startswith("tvly-") or len(key) < 20:
        print(f"That doesn't look like a Tavily key (expected 'tvly-...', got {len(key)} chars). Aborting - config unchanged.")
        sys.exit(1)

    ok, msg = validate_key(key)
    print("Tavily check:", msg)
    if not ok:
        print("Not writing an unvalidated key. Config unchanged.")
        sys.exit(1)

    text = text.replace(PLACEHOLDER, key)
    text, n = re.subn(r"(  websearch:\n    enabled: )true", r"\1false", text)
    CONFIG.write_text(text, encoding="utf-8")
    print(f"Done: key written to goose config, DuckDuckGo fallback disabled ({n} flag flipped).")
    print("Open a NEW goose session and web search goes through Tavily.")


if __name__ == "__main__":
    main()

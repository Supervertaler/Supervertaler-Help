"""
One-shot migration: convert GitBook hint blocks to Starlight asides.

GitBook syntax:
    {% hint style="info" %}
    Some text here.
    {% endhint %}

Starlight syntax:
    :::note
    Some text here.
    :::

Style mapping:
    info     -> note
    success  -> tip
    warning  -> caution
    danger   -> danger

Run from the repo root:
    python _migrate/convert_gitbook_hints.py
"""

from __future__ import annotations
import re
import sys
from pathlib import Path


STYLE_MAP = {
    "info": "note",
    "success": "tip",
    "warning": "caution",
    "danger": "danger",
}

# Match an entire hint block.  Captures the style name and the body.
# DOTALL so `.` matches newlines inside the body.
HINT_RE = re.compile(
    r'\{%\s*hint\s+style="([^"]+)"\s*%\}\s*\n?(.*?)\n?\{%\s*endhint\s*%\}',
    re.DOTALL,
)


def convert(text: str) -> tuple[str, int]:
    """Convert all hint blocks in `text` to Starlight asides.
    Returns (new_text, count_converted)."""
    count = [0]

    def replace(m: re.Match) -> str:
        count[0] += 1
        style = m.group(1).strip().lower()
        body = m.group(2)
        aside_kind = STYLE_MAP.get(style, "note")
        body = body.strip()
        return f":::{aside_kind}\n{body}\n:::"

    new_text = HINT_RE.sub(replace, text)
    return new_text, count[0]


def process_file(path: Path) -> int:
    """Returns the number of hint blocks converted, or -1 on error."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  ✗ {path}  read error: {e}")
        return -1

    new_text, count = convert(text)
    if count == 0:
        return 0

    try:
        path.write_text(new_text, encoding="utf-8")
    except Exception as e:
        print(f"  ✗ {path}  write error: {e}")
        return -1

    return count


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    targets = (
        list(root.glob("trados/**/*.md"))
        + list(root.glob("workbench/**/*.md"))
        + list(root.glob("trados/**/*.mdx"))
        + list(root.glob("workbench/**/*.mdx"))
        + [root / "index.mdx"]
    )

    total_files = 0
    total_blocks = 0
    errors = 0
    for path in sorted(targets):
        if not path.exists():
            continue
        n = process_file(path)
        if n > 0:
            print(f"  ✓ {path.relative_to(root)}  ({n} block{'s' if n != 1 else ''})")
            total_files += 1
            total_blocks += n
        elif n < 0:
            errors += 1

    print()
    print(f"Converted {total_blocks} hint block(s) across {total_files} file(s).")
    if errors:
        print(f"Errors: {errors}")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

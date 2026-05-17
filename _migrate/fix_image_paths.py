"""
Rewrite relative .gitbook/assets/ image references to absolute paths.

Why this exists
---------------
The .md files were authored for GitBook, which served pages at flat URLs like
``/help/features/termlens``. Image refs were written as relative paths like::

    <img src="../.gitbook/assets/Sv_TermLens.png">

That resolved correctly under GitBook's URL shape because ``..`` from the page
landed at the publishing root.

The new Astro/Starlight site serves the same content at folder-based URLs with
trailing slashes — ``/trados/termlens/``. The browser interprets ``../`` as a
URL operation (not a filesystem operation against the source path), so
``../.gitbook/assets/...`` now resolves to ``/trados/.gitbook/assets/...``,
which doesn't exist. The actual assets live at ``/.gitbook/assets/...`` (root),
copied there by ``copy-gitbook-assets.mjs`` after the Astro build.

This script rewrites every relative reference to the assets folder into an
absolute path (``/.gitbook/assets/...``), which is robust regardless of how
deeply nested the page URL is.

Run from the repo root::

    python _migrate/fix_image_paths.py

The change is idempotent — running it again is a no-op.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Matches any sequence of ../ (one or more) followed by .gitbook/assets/.
# The leading / is captured if present (means already absolute — leave alone).
# Patterns to rewrite are anything OTHER than already-absolute.
RELATIVE_RE = re.compile(r"(?P<prefix>(?:\.\./)+)(?P<rest>\.gitbook/assets/)")


def rewrite(text: str) -> tuple[str, int]:
    """Return (new_text, num_substitutions)."""
    n = 0

    def _sub(m: re.Match[str]) -> str:
        nonlocal n
        n += 1
        return "/" + m.group("rest")

    new_text = RELATIVE_RE.sub(_sub, text)
    return new_text, n


def main() -> int:
    total_files_changed = 0
    total_subs = 0

    # Walk both product trees + the index.
    candidates: list[Path] = []
    for folder in ("trados", "workbench"):
        candidates.extend((REPO_ROOT / folder).rglob("*.md"))
        candidates.extend((REPO_ROOT / folder).rglob("*.mdx"))
    for index_name in ("index.md", "index.mdx", "README.md"):
        p = REPO_ROOT / index_name
        if p.exists():
            candidates.append(p)

    for path in candidates:
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"  skip (not utf-8): {path.relative_to(REPO_ROOT)}")
            continue

        rewritten, n = rewrite(original)
        if n > 0:
            path.write_text(rewritten, encoding="utf-8")
            total_files_changed += 1
            total_subs += n
            print(f"  {n:>2}  {path.relative_to(REPO_ROOT)}")

    print()
    print(f"Rewrote {total_subs} reference(s) across {total_files_changed} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

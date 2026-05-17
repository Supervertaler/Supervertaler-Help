"""
Remove the obsolete cross-product "You are viewing help for X" disambiguation
notes from every .md page under trados/ and workbench/.

Why this exists
---------------
The notes were added during the GitBook migration because both products
shared a single flat namespace and a single search scope — a Workbench user
landing on a Trados page (e.g. via Google) couldn't otherwise tell which
product the page was about. They look like::

    :::note
    You are viewing help for 🧩 **Supervertaler for Trados** – the Trados Studio
    plugin. Looking for help with the standalone app? Visit 🖥️ [Supervertaler
    Workbench help](https://supervertaler.gitbook.io/help/get-started-1/workbench/).
    :::

On the new Astro/Starlight site the notes are redundant and actively harmful:
 - The sidebar is auto-filtered per product (Sidebar.astro), so the user
   already sees only the current product's tree.
 - URLs are unambiguous (/trados/* vs /workbench/*).
 - The custom search component (Search.astro) groups results by product and
   scopes by current section.
 - The link inside the notes still points at the decommissioning GitBook URL.

So they're noise + dead links. This script removes them.

The match is precise: only blocks whose body starts with the exact phrase
"You are viewing help for" are removed. Other :::note blocks in the same
files are untouched.

Run from the repo root::

    python _migrate/remove_disambiguation_notes.py

Idempotent — running again is a no-op once the notes are gone.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Multi-line match:
#   :::note
#   You are viewing help for ...   (single line, but allow any content)
#   :::
#   <optional trailing blank line, which we also consume so the file
#    doesn't end up with two consecutive blank lines after removal>
PATTERN = re.compile(
    r"^:::note\n"
    r"You are viewing help for [^\n]*\n"
    r":::\n"
    r"(?:\n)?",  # Optional trailing blank line — collapse it.
    re.MULTILINE,
)


def main() -> int:
    candidates: list[Path] = []
    for folder in ("trados", "workbench"):
        candidates.extend((REPO_ROOT / folder).rglob("*.md"))

    files_changed = 0
    for path in candidates:
        text = path.read_text(encoding="utf-8")
        new_text, n = PATTERN.subn("", text)
        if n > 0:
            path.write_text(new_text, encoding="utf-8")
            files_changed += 1
            if n > 1:
                # Belt-and-braces: flag if any page had more than one of these,
                # which would be unexpected — current state is exactly one per page.
                print(f"  [{n}]  {path.relative_to(REPO_ROOT)}")
            else:
                print(f"  ok   {path.relative_to(REPO_ROOT)}")

    print()
    print(f"Removed disambiguation note from {files_changed} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

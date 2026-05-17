"""
Generate src/generated/sidebar.js from SUMMARY.md.

SUMMARY.md is the GitBook-canonical navigation file, with the structure:

    ## 🧩 <Section Name>              <- section header (Trados)
    * [Label](path.md)                 <- top-level item
      * [Nested Label](path.md)        <- one level nested
        * [Deeper Label](path.md)      <- two levels nested

    ## 🖥️ <Section Name>              <- section header (Workbench)
    ...

The Workbench-side sections are tagged with 🖥️ at the start; Trados with 🧩.

We emit a Starlight sidebar config:

    [
      {
        label: '🧩 Supervertaler for Trados',
        items: [
          { label: 'Get Started', items: [...trados Get Started...] },
          { label: 'Features',    items: [...trados Features...] },
          ...
        ]
      },
      {
        label: '🖥️ Supervertaler Workbench',
        items: [
          { label: 'Get Started',           items: [...workbench Get Started...] },
          { label: 'Editor & Translation',  items: [...workbench Editor...] },
          ...
        ]
      }
    ]

The two top-level groups must include "Trados" and "Workbench" verbatim in
their labels, because src/components/Sidebar.astro filters by substring
match to hide the other product on a product page.

Run from the repo root:
    python _migrate/generate_sidebar.py

This is intended to be re-run any time SUMMARY.md changes.  The output is
checked into git so Cloudflare Pages builds don't need Python.
"""

from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Optional, Tuple


REPO_ROOT = Path(__file__).resolve().parent.parent
SUMMARY_PATH = REPO_ROOT / "SUMMARY.md"
OUTPUT_PATH = REPO_ROOT / "src" / "generated" / "sidebar.js"

# Strip product-disambiguation suffixes added by an earlier migration so the
# clean label appears in the Starlight sidebar.  The parent group already
# tells you which product you're in; the per-link suffix would be redundant.
LABEL_SUFFIX_RE = re.compile(r"\s*\((Trados|Workbench)\)\s*$")

# Lines like "* [Label](path.md)" or "  * [Label](path)" — with optional indent.
ITEM_RE = re.compile(r"^(\s*)\*\s*\[([^\]]+)\]\(([^)]+)\)\s*$")

# Section headers: "## 🧩 Foo" or "## 🖥️ Bar".
SECTION_RE = re.compile(r"^##\s*(🧩|🖥️)\s*(.+?)\s*$")


def clean_label(label: str) -> str:
    """Strip "(Trados)" / "(Workbench)" suffixes."""
    return LABEL_SUFFIX_RE.sub("", label).strip()


def md_path_to_url(md_path: str) -> str:
    """Convert ``trados/installation.md`` -> ``/trados/installation/``.

    Special cases:
      * README.md   -> directory root  (matches our content.config.ts rule)
      * index.md    -> directory root
      * The repo-root README.md becomes `/` (the welcome page).
    """
    # Strip any leading slash, fragment, etc.
    p = md_path.strip().lstrip("/")

    # Strip trailing fragments (#section) — Starlight sidebar entries are
    # whole-page links; in-page anchors aren't represented in SUMMARY.md
    # for our project.
    p = p.split("#", 1)[0]

    # Drop extension.
    if p.lower().endswith(".md"):
        p = p[:-3]
    elif p.lower().endswith(".mdx"):
        p = p[:-4]

    # README / index segments become the folder root.
    parts = p.split("/")
    if parts and parts[-1].lower() in ("readme", "index"):
        parts = parts[:-1]

    url = "/" + "/".join(parts)
    if not url.endswith("/"):
        url = url + "/"
    return url


def parse_summary(text: str) -> List[Dict]:
    """Return a list of section dicts, one per "## emoji Name" header.

    Each section dict:
        { 'product': 'Trados' | 'Workbench',
          'name': 'Get Started',
          'items': [ <recursive item tree> ] }

    Each item:
        { 'label': str, 'link': str, 'items'?: [<children>] }
    """
    sections: List[Dict] = []
    current: Optional[Dict] = None
    # Stack of (indent_width, items_list) for nested .items[].
    # The root list of the current section is at indent -1.
    stack: List[Tuple[int, List[Dict]]] = []

    for raw_line in text.splitlines():
        # Section header
        sec_m = SECTION_RE.match(raw_line)
        if sec_m:
            emoji, name = sec_m.group(1), sec_m.group(2).strip()
            product = "Trados" if emoji == "🧩" else "Workbench"
            current = {"product": product, "name": name, "items": []}
            sections.append(current)
            stack = [(-1, current["items"])]
            continue

        if current is None:
            continue

        # List item
        item_m = ITEM_RE.match(raw_line)
        if not item_m:
            continue
        indent_str, raw_label, raw_path = item_m.groups()
        indent = len(indent_str)
        label = clean_label(raw_label)
        link = md_path_to_url(raw_path)
        item: Dict = {"label": label, "link": link}

        # Pop the stack until we find a parent whose indent < this indent.
        while stack and stack[-1][0] >= indent:
            stack.pop()

        if not stack:
            # Shouldn't happen — we always seed with (-1, section.items)
            stack = [(-1, current["items"])]

        parent_indent, parent_items = stack[-1]
        parent_items.append(item)

        # Children, if any, will land here.  Pre-seed items so we can attach.
        item["items"] = []  # may stay empty
        stack.append((indent, item["items"]))

    # Clean up:
    #  1. Drop empty `items` arrays — Starlight's schema rejects them.
    #  2. Items that have BOTH a link and children must become groups.
    #     Starlight's sidebar schema requires entries to be EITHER a leaf
    #     ({label, link}) OR a group ({label, items[]}), never both.
    #     GitBook allows a parent page to have its own URL *and* children;
    #     we convert those by:
    #       - dropping the parent's `link`
    #       - prepending an "Overview" leaf item whose link is the
    #         original parent's URL, so the parent page is still
    #         reachable from the sidebar.
    def prune(items: List[Dict]) -> List[Dict]:
        for it in items:
            children = it.get("items") or []
            if children:
                prune(children)
                if children:
                    # If this item also has a link, demote: convert to a
                    # group with an "Overview" leaf that points to the
                    # original link.
                    if "link" in it:
                        overview = {"label": "Overview", "link": it["link"]}
                        it["items"] = [overview] + children
                        del it["link"]
                    else:
                        it["items"] = children
                else:
                    # children list ended up empty after pruning
                    del it["items"]
            elif "items" in it:
                del it["items"]
        return items

    for sec in sections:
        prune(sec["items"])

    return sections


def build_sidebar(sections: List[Dict]) -> List[Dict]:
    """Group sections into two top-level products with nested section folders."""
    trados_sections = [s for s in sections if s["product"] == "Trados"]
    workbench_sections = [s for s in sections if s["product"] == "Workbench"]

    def section_to_group(sec: Dict) -> Dict:
        return {
            "label": sec["name"],
            "collapsed": True,
            "items": sec["items"],
        }

    return [
        {
            "label": "🧩 Supervertaler for Trados",
            "collapsed": False,
            "items": [section_to_group(s) for s in trados_sections],
        },
        {
            "label": "🖥️ Supervertaler Workbench",
            "collapsed": False,
            "items": [section_to_group(s) for s in workbench_sections],
        },
    ]


def emit_js(sidebar: List[Dict]) -> str:
    """Render the sidebar as a JS file Starlight can import."""
    pretty = json.dumps(sidebar, ensure_ascii=False, indent=2)
    return (
        "// AUTO-GENERATED by _migrate/generate_sidebar.py from SUMMARY.md.\n"
        "// Do NOT edit this file by hand — rerun the script after editing\n"
        "// SUMMARY.md.  The script preserves SUMMARY.md as the single\n"
        "// source of truth for the docs navigation (also used by GitBook\n"
        "// during the migration window).\n"
        "/* eslint-disable */\n"
        "// @ts-nocheck\n"
        "const sidebar = " + pretty + ";\n"
        "export default sidebar;\n"
    )


def main() -> int:
    text = SUMMARY_PATH.read_text(encoding="utf-8")
    sections = parse_summary(text)
    sidebar = build_sidebar(sections)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(emit_js(sidebar), encoding="utf-8")

    n_trados = sum(1 for s in sections if s["product"] == "Trados")
    n_workbench = sum(1 for s in sections if s["product"] == "Workbench")
    print(f"Parsed {len(sections)} sections from SUMMARY.md "
          f"({n_trados} Trados, {n_workbench} Workbench).")
    print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

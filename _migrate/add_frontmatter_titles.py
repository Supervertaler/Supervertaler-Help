"""
One-shot migration script: add `title:` frontmatter to every .md / .mdx file
under trados/ and workbench/.

For each file:
  1. Parse existing YAML frontmatter (if any).
  2. If `title:` is already present, leave the file alone.
  3. Otherwise, derive the title from the first `# Heading` line in the body
     (or fall back to the filename stem if no H1).
  4. Write `title:` into the frontmatter and REMOVE the H1 from the body
     so Starlight doesn't render the title twice.

This script is idempotent: running it again is a no-op for files that have
already been migrated (they all have `title:` after the first run).

Run from the repo root:
    python _migrate/add_frontmatter_titles.py
"""

from __future__ import annotations
import re
import sys
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
H1_RE = re.compile(r"^# +(.+?)\s*$", re.MULTILINE)


def derive_title_from_filename(path: Path) -> str:
    """Convert ``find-replace.md`` -> ``Find Replace``."""
    stem = path.stem
    return stem.replace("-", " ").replace("_", " ").strip().title() or "Untitled"


def parse_frontmatter(text: str) -> tuple[dict, str, str]:
    """Return (meta_lines_as_dict, raw_yaml, body_after_frontmatter).

    Uses a minimal line-by-line YAML parse because most existing files have
    only simple ``key: "value"`` pairs.  We do NOT use PyYAML here on purpose
    so the script doesn't introduce formatting changes (re-ordering keys,
    canonicalising quotes) on files we're only updating to add ``title``.
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, "", text

    yaml_raw = m.group(1)
    meta: dict[str, str] = {}
    for line in yaml_raw.splitlines():
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith("#"):
            continue
        if ":" not in line_stripped:
            continue
        key, _, value = line_stripped.partition(":")
        meta[key.strip().lower()] = value.strip().strip('"').strip("'")
    body = text[m.end():]
    return meta, yaml_raw, body


def add_title_frontmatter(text: str, title: str) -> str:
    """Insert ``title: "..."`` into the YAML frontmatter, creating the block
    if absent.  Preserves any other frontmatter fields verbatim."""
    safe_title = title.replace('"', '\\"')
    title_line = f'title: "{safe_title}"'

    m = FRONTMATTER_RE.match(text)
    if not m:
        # No existing frontmatter — prepend a fresh block.
        return f"---\n{title_line}\n---\n\n{text.lstrip()}"

    yaml_raw = m.group(1)
    body = text[m.end():]
    new_yaml = f"{title_line}\n{yaml_raw.rstrip()}"
    return f"---\n{new_yaml}\n---\n{body}"


def strip_first_h1(body: str, title: str) -> str:
    """Remove the first ``# Heading`` line from the body if its text matches
    the title (case-insensitive, trimmed).  Leaves other H1s alone (rare,
    but technically possible) and other heading levels (##, ###) untouched.
    """
    title_norm = title.strip().lower()
    lines = body.splitlines(keepends=True)
    out: list[str] = []
    stripped_one = False
    for line in lines:
        if not stripped_one:
            match = H1_RE.match(line.rstrip("\n"))
            if match and match.group(1).strip().lower() == title_norm:
                stripped_one = True
                # Also drop a single trailing blank line after the H1.
                continue
        out.append(line)
    result = "".join(out)
    # Tidy: collapse any leading blank lines we introduced.
    return result.lstrip("\n") if stripped_one else result


def process_file(path: Path) -> str:
    """Returns one of: 'skipped' (already has title), 'updated', 'no-content'."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return f"error: {e}"

    if not text.strip():
        return "no-content"

    meta, _yaml_raw, body = parse_frontmatter(text)
    if meta.get("title"):
        return "skipped"

    # Derive title from first H1 in body, fall back to filename.
    h1_match = H1_RE.search(body)
    if h1_match:
        title = h1_match.group(1).strip()
        body = strip_first_h1(body, title)
    else:
        title = derive_title_from_filename(path)

    # Rebuild the file with title frontmatter prepended and the H1 removed.
    if meta:
        # Reconstruct frontmatter with title first, then existing fields.
        # We rebuild from `meta` to preserve key/value pairs verbatim.
        new_lines = [f'title: "{title.replace(chr(34), chr(92) + chr(34))}"']
        for k, v in meta.items():
            # Skip if duplicate of title (shouldn't happen — we checked above).
            if k == "title":
                continue
            # Quote string values for safety.
            v_quoted = f'"{v}"' if v else '""'
            new_lines.append(f"{k}: {v_quoted}")
        new_yaml = "\n".join(new_lines)
        new_text = f"---\n{new_yaml}\n---\n\n{body.lstrip()}"
    else:
        new_text = add_title_frontmatter(body, title)

    path.write_text(new_text, encoding="utf-8")
    return "updated"


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    targets = list(root.glob("trados/**/*.md")) + list(root.glob("workbench/**/*.md"))
    targets += list(root.glob("trados/**/*.mdx")) + list(root.glob("workbench/**/*.mdx"))

    stats = {"updated": 0, "skipped": 0, "no-content": 0, "error": 0}
    for path in sorted(targets):
        result = process_file(path)
        rel = path.relative_to(root)
        if result.startswith("error"):
            print(f"  ✗ {rel}  {result}")
            stats["error"] += 1
        elif result == "no-content":
            print(f"  - {rel}  (empty file, skipped)")
            stats["no-content"] += 1
        elif result == "skipped":
            stats["skipped"] += 1
        else:
            print(f"  ✓ {rel}")
            stats["updated"] += 1

    print()
    print(f"Updated:    {stats['updated']}")
    print(f"Skipped:    {stats['skipped']}  (already had title:)")
    print(f"Empty:      {stats['no-content']}")
    print(f"Errors:     {stats['error']}")
    return 0 if stats["error"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

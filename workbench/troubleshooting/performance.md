---
title: "Performance Tips"
---

Supervertaler is designed to stay responsive on large projects, but performance can vary with project size and enabled features.

## Tips

- Pick a smaller **Per page** size for very large projects (the grid shows all segments by default; projects over 1,000 segments auto-paginate at 200). See [Pagination](/workbench/editor/pagination/)
- Keep only the needed TMs and termbases enabled
- If semantic search is enabled, allow indexing to complete

## Quick wins when it feels slow

1. Disable spellcheck temporarily (Settings → View Settings)
2. Close other heavy apps (browsers with many tabs, IDE builds, etc.)
3. Restart Supervertaler and reopen the project

## Large projects

Very large files (thousands of segments) can stress any UI grid.

- Prefer pagination.
- Consider splitting source documents or using multi-file projects.

Since v1.10.373 big projects load much faster. A Trados package of 300 files and 17,000 segments, which used to freeze Supervertaler for more than ten minutes, now imports in about 11 seconds:

- the [Document Preview](/workbench/editor/preview/) is built only when you open it, not on every import;
- the grid, the file-name banners of multi-file projects and the status-bar file count no longer do work that grows with the square of the project size;
- starting Supervertaler takes about two seconds less.

If a large project still feels slow on an older version, update first.

## A slow start-up with a TM message in the log

If the log says "[TM] The full-text index cannot find its own rows… Rebuilding
it", Supervertaler is repairing the search index that fuzzy TM matches rely on
(from v1.10.371). On a large TM this takes a few seconds, about 2.6 seconds for
200,000 entries, and it happens only when the index needs it. See
[TM Matches Not Appearing](/workbench/troubleshooting/tm-matches/#3-exact-matches-appear-but-never-fuzzy-ones).

## If it feels slow

Try restarting the app and reopening the project.

If performance is still poor, note:

- Project size (segment count)
- Whether spellcheck is enabled
- Which CAT format you imported

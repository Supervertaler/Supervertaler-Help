---
title: "Filtering Segments"
---

Filtering helps you focus on the segments you need right now.

## Common uses

- Show only segments that contain a specific term
- Focus on segments that need review
- Quickly find repeated strings and fix consistency

## Filtering by text

Above the grid are two filter boxes, **Source** and **Target**. Type in one of them (or both) and press **Enter**, or click **Filter**, to show only the segments that contain that text. The filter is not case-sensitive, and the matching text is highlighted in the grid. With text in both boxes, a segment has to match both. **Clear Filters** shows every segment again.

### Regular expressions

Since v1.10.372 you can also filter with a regular expression: type the pattern between slashes in the **Source** or **Target** box.

| You type | Shows segments containing |
|----------|---------------------------|
| `/pump\s+hous(ing\|e)/` | "pump housing" and "Pump house", but not "pumphousing" |
| `/\d+\s?mm\b/` | a number followed by "mm", such as "12 mm" or "12mm" |
| `/^The /` | "The " at the very start of the segment |

- Like plain filtering, a regular expression ignores case, and exactly what it matched is highlighted.
- Anything not wrapped in slashes is filtered as plain text, exactly as before.
- If the pattern isn't a valid regular expression, it is matched as plain text instead (slashes included, so it usually finds nothing), and the status bar says what is wrong with it.
- Hover over a filter box for a reminder of the syntax.

The patterns use the same syntax as **Regex** in [Find & Replace](/workbench/editor/find-replace/#regular-expressions).

## Tip: filter on selection

A fast workflow is to select a word/phrase in the grid and use **Filter on selection**.

### Shortcut

- **Ctrl+Shift+F** toggles filtering:
	- If a filter is not active, it filters on the current selection.
	- If a filter is active, it clears the filter.

:::note
Filtering is designed to be fast even in large projects.
:::

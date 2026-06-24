---
title: "The Translation Grid"
---

The translation grid is where you spend most of your time: each row is a **segment** (usually a sentence or paragraph) with source and target text.

## Columns

The grid has five columns:

| Column | What it is |
|--------|------------|
| **#** | Segment number (row index) |
| **Type** | Segment type (depends on the file format/importer) |
| **Source** | Original text (typically read-only) |
| **Target** | Your translation (editable) |
| **Status** | Segment status (dropdown) |

## Editing behavior

- The grid is optimized for speed, but edits are intentionally lightweight.
- **Double-click** a cell to edit.
- Use **Shift+Enter** for a line break inside a cell (multi-line target).

## Confirming & status

- Use the **Status** dropdown to set the segment state.
- Keyboard confirm is supported (see [Editing & Confirming](editing-confirming.md)).

Common statuses include:

- Not started
- Translated
- Confirmed
- Proofread
- Approved

:::note
If you plan to reimport into a CAT tool, do not merge/split content across segments. Segment boundaries must stay compatible.
:::

## Visual cues

- **Tags** (CAT tool placeholders and formatting markers) are highlighted to make them hard to miss.
- **Spellcheck** (if enabled) underlines misspelled target words.
- **Termbase matches** can be highlighted in the source.

## TermLens panel placement

You can dock the TermLens panel directly above or below the grid from the **View** menu:

- **Show TermLens above grid** –places the panel between the filter bar and the grid.
- **Show TermLens below grid** –places it under the grid.

The change applies immediately, no need to reopen the project. Clicking the option that is already active hides the panel again.

## Splitting and merging segments

Right-click in a **Source** cell to **✂ Split segment here** (at the clicked position) or **🔗 Merge with next segment** — Trados/memoQ-style re-segmentation, fully undoable. See [Editing & Confirming](editing-confirming.md#splitting-and-merging-segments) for details and when it's available.

## See also

- [Navigation](navigation.md)
- [Editing & Confirming](editing-confirming.md)
- [Keyboard Shortcuts](keyboard-shortcuts.md)
- [Filtering](filtering.md)

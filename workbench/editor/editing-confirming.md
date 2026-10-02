---
title: "Editing & Confirming"
---

Translate by editing the **Target** column in the grid.

## Editing

- Double-click a Target cell and type your translation.
- Use standard editing shortcuts (undo/redo, copy/paste, find/replace).

### Multi-line target text

- Use **Shift+Enter** to insert a line break inside the cell.

### Tags are protected

Inline tags in the target cell behave as single units, the way they do in memoQ and Trados, so a slip of the keyboard can't leave half a tag behind (from v1.10.373). This covers `<b>`, `</1>`, `[2}`, `{3}`, Déjà Vu's `{00108}` and your own [inline codes](/workbench/settings/inline-codes/):

- **The cursor steps over a tag** instead of landing inside it – with the arrow keys and when you click in it.
- **Backspace just after a tag, or Delete just before it, removes the whole tag.** **Ctrl+Z** brings it back.
- **Typing, pasting or cutting over a selection that cuts into a tag takes the whole tag.** A paste made with the cursor inside a tag lands just after it.

To edit tags character by character, untick **Settings → 🏷️ Inline Codes → Protect tags and codes in the target**. **Ctrl+,** still inserts the next tag from the source.

## Confirming segments

Confirming matters for many workflows, especially when exporting back to a CAT tool.

Typical workflow:

1. Translate (manual or AI)
2. Review the target text
3. Confirm the segment

### Confirm shortcuts

- **Ctrl+Enter**: confirm the current segment (or all selected segments) and move to the next unconfirmed segment.
- **Ctrl+Shift+Enter**: confirm all selected segments.

You can also confirm by setting the segment **Status** dropdown to a confirmed status.

## Splitting and merging segments

You can re-segment a document the way Trados Studio and memoQ allow – right from the grid:

- **Split a segment:** click in the **Source** cell at the exact spot you want to divide, then right-click → **✂ Split segment here**. The existing translation stays with the first part; the second part starts empty, ready to translate.
- **Merge two segments:** right-click in the **Source** cell → **🔗 Merge with next segment**. The two sources (and targets) are joined with sensible spacing, and the merged segment takes the less-complete of the two statuses.

Both actions are fully **undoable** with **Ctrl+Z** (and redoable with **Ctrl+Y**).

**When it's available:**

- Merge is only offered when the next segment is in the **same paragraph, table cell, file, and text unit** – so you can't accidentally fuse separate paragraphs. If it isn't allowed, the menu item is greyed out with the reason.
- Split needs the cursor to land *inside* the source text, and is disabled while tags are shown in **compact** form or with **outer wrapping tags hidden** (switch to full tag view first, so the split lands in the right place).

:::note
Split and merge are available for documents Supervertaler segments itself – **DOCX, IDML, HTML, PPTX, XLSX (via Okapi), and TXT/Markdown**. They are intentionally **hidden for bilingual CAT files** (Trados sdlxliff, memoQ/Trados/Phrase/Déjà Vu bilingual tables, PO), because those files have fixed segment slots owned by the other tool – adding or removing segments would break the round-trip back to that tool. (Trados and memoQ work the same way: you re-segment in their editor, which owns the segmentation.)
:::

## Related pages

* [Segment Statuses](/workbench/editor/segment-statuses/) – full reference for workflow statuses, match origins, and how they map to Trados and memoQ
* [The Translation Grid](/workbench/editor/translation-grid/)
* [Find & Replace](/workbench/editor/find-replace/)
* [Tag Validation](/workbench/qa/tag-validation/)

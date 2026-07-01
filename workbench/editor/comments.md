---
title: "Comments"
---

The **💬 Comments** tab in Workbench's right panel is where per-segment annotations live. There are two sub-tabs:

* **📝 Segment** — comments you author while translating: context notes, queries for the client, reminders to yourself, anchored highlights on specific words.
* **✅ Proofreading** — AI-generated proofreading feedback, listed across the whole project and colour-coded by the LLM that produced it (read-only text; delete individually or all at once).

Both are stored on the segment itself and persist in the `.svproj` file. Segment comments are **exported to the final document as Word comments** (yellow comment bubbles in the right margin of the exported `.docx`), with the range highlight covering exactly the words you anchored the comment to. Proofreading comments are review-only and don't export.

## Segment comments

### Two kinds: segment-level and range-anchored

There are two kinds of segment comment:

* **Segment-level (no anchor)** — a general note about the whole segment. In the exported `.docx` the Word comment anchors to the entire paragraph.
* **Range-anchored** — attached to a specific word or phrase you selected. In the exported `.docx` the Word comment highlights exactly those characters, the same way Trados and memoQ comments do.

Both kinds coexist and you can have many of each on the same segment.

### Adding a range-anchored comment (Ctrl+M)

1. Click into the source or target cell of a segment.
2. Select the text the comment is about (e.g. `schroef`, `aangebracht`, or a multi-word phrase).
3. Press **Ctrl+M**.
4. A dialog opens showing which segment + which field (source or target) you're anchoring to, plus a snippet of your selection for confirmation. Type the comment, click **OK**.

The anchored text immediately gets a soft amber background in the editor cell so you can see at a glance which words have comments attached. The new comment also appears in the all-comments list (see below).

:::tip
**Ctrl+M** matches memoQ's "Add comment" shortcut. (Trados Studio uses **Ctrl+Shift+N** for the same action.) You can also add a comment without the keyboard: **right-click in the source or target cell → 💬 Add comment**.
:::

### Adding a segment-level (unanchored) comment

Place the cursor in the source or target cell **without selecting any text**, then press **Ctrl+M** (or right-click → **💬 Add segment comment**). The comment is attached to the whole segment rather than to a specific range. Useful for a general note, or for adding another comment to a segment without disturbing an existing one.

### The all-comments list

The Segment sub-tab shows **one entry per Comment** — not per segment. A segment with three comments shows three entries, in document order. Each entry has:

* A clickable **Segment #N** header. For anchored comments, the header reads `Segment #N  ⚓ source` or `Segment #N  ⚓ target` to tell you what kind of anchor it has.
* For anchored comments: a quoted snippet of the anchored text, so you can see what the comment is *about* without jumping to the segment.
* The full comment body.
* A small footer line with the author and timestamp, plus a `(right-click for edit/delete)` hint.

Clicking the **Segment #N** header jumps the grid to that segment (cross-page-aware — switches pagination first if needed). Conversely, **selecting a segment in the grid scrolls the list to — and highlights — that segment's comment(s)**, so the active segment's notes are always in view without hunting for them.

**Right-click** on a Segment header (or anywhere on the entry) opens a context menu with **✏️ Edit comment…** and **🗑️ Delete comment**. Edit opens a small dialog pre-populated with the existing text; saving with an empty text field deletes the comment. Delete prompts for confirmation.

The list rebuilds itself in real time as you add, edit, or remove comments.

:::note
Earlier versions had a separate "Comment on current segment" box at the bottom of the tab. It only handled a single, unanchored note and overwrote the whole comment list when edited, so it was removed in v1.10.142. All comments — anchored and segment-level — now live in the one list, and you add them with **Ctrl+M** or **right-click → 💬 Add comment** in the editor.
:::

### Editor visual cue: amber background

Anchored comment ranges show a soft amber background in the source or target cell editors. This coexists with the existing syntax highlighting (tag pink, spellcheck underlines, etc.) — the amber is applied as a background colour on the anchored characters only.

If you edit the target text after creating an anchored comment, the amber highlight stays at its original character offsets. If your edit shifts the anchor's intended target, the highlight may end up on slightly-different wording. The simplest workaround is to edit the text first, then create the anchored comment.

### Reaching a comment from the grid

You don't have to open the Comments tab first to find a comment — you can get to it straight from the segment in the grid:

* **Hover** the amber-highlighted range in a source or target cell to see the comment as a tooltip.
* **Right-click** the highlighted range and choose **💬 Open comment**. Workbench switches the right panel to the **💬 Comments → 📝 Segment** sub-tab and briefly flashes the matching entry — handy when the Match Panel (or another tab) was showing.

Segment-level comments have no highlighted range to aim at, so they're reachable two other ways:

* **Right-click anywhere** in a commented segment's source or target cell → **💬 Open comment(s)** (opens the segment's first comment).
* **Hover or right-click the Status cell** of a commented segment: the tooltip lists the segment's comments, and right-clicking offers **💬 Open comment(s)**.

The Status cell is also **colour-coded** so you can tell comment types apart at a glance: a segment with a **segment comment** shows an **amber** background, one with a **proofreading comment** shows **purple**, and a segment that has **both** shows a **split amber|purple** background.

### Comments in exported documents

When you export your project back to a Word document (**Project → Export → Export Translated Document…**), every segment comment becomes a Word comment in the output `.docx`. Behaviour per comment kind:

* **Range-anchored to target text**: the Word comment's range highlight covers exactly the anchored characters. If the anchor boundaries cut mid-run (e.g. inside a bold word), Workbench splits the run cleanly and preserves the formatting on both halves. Visually identical to a Trados or memoQ comment.
* **Range-anchored to source text**: the source text isn't in the exported (target-only) DOCX, so Workbench falls back to anchoring the comment to the whole paragraph, with the source snippet prefixed in the comment body. Example: `[Re: "schroef" (source)] translated as 'screw' based on context`. The reviewer reading the file sees the comment with the relevant source quote inline.
* **Segment-level (unanchored)**: anchors to the whole paragraph, like a paragraph-wide annotation.

The comment author defaults to the **Translator Name** field in **Settings → User Identity** — set that if you want comments attributed to your real name rather than your system username. Initials are derived automatically (multi-word names take the first letter of each word, e.g. `Michael Beijer` → `MB`; single-word names take the first two characters uppercased, e.g. `mbeijer` → `MB`).

After export, Workbench logs how many comments were attached:

```
✓ Attached 4 segment comment(s) as Word comments (2 range-anchored)
```

If any comments couldn't be matched to a paragraph (rare — usually because the target text was heavily reformatted by the Okapi merge step), the log says so and the export still completes — the comment-attach step is purely additive.

### Comments and bilingual table exports

For bilingual-table export formats (Supervertaler Bilingual Table, memoQ, CafeTran, etc.), segment comments are written to a dedicated **Notes** column rather than as Word comments. Anchored and segment-level comments are concatenated into a single string in that column; the anchor metadata is **not** carried over (these formats don't have a native concept of in-cell anchoring). Re-importing the bilingual table later preserves the comments as a single segment-level comment per segment.

If you need range-anchored comments to survive a round-trip, export as DOCX rather than as a bilingual table.

## Proofreading comments

The **✅ Proofreading** sub-tab lists AI-generated review feedback across the **whole project** — mirroring the Segment sub-tab's all-comments list, so the two tabs now behave the same way. Generate the feedback with **QA ▸ Proofreading ▸ Proofread Translation…** (proofreading moved into the new [QA menu](#the-qa-menu) in v1.10.327).

Each entry is one **(segment, model)** result:

* A clickable **Segment #N · model** header that jumps the grid to that segment (cross-page-aware).
* The proofreader's findings, shown verbatim. The text is **read-only** — you read it and decide whether to act on it.
* A **🗑️ delete** button that removes just that one comment.

**Each LLM engine gets its own colour**, so if you ran the project through more than one model (e.g. GPT *and* Claude), you can tell at a glance which model flagged what. Selecting a segment in the grid scrolls the list to — and highlights — that segment's proofreading comment(s), exactly like the Segment sub-tab.

To clear everything at once, use **QA ▸ Proofreading ▸ Delete All Proofreading Comments**. Deletion is safe: re-running **Proofread Translation** regenerates the comments.

Proofreading comments are **not** exported to the final document. They're a translator-side review tool.

### The QA menu

AI proofreading lives under the top-level **QA** menu (**QA ▸ Proofreading**), which also hosts **Delete All Proofreading Comments**. See **[AI Proofreading](../qa/proofreading.md)** for how to run a pass. QA is Workbench's home for quality-assurance features — see also [Spellcheck](../qa/spellcheck.md), [Tag Validation](../qa/tag-validation.md) and [Non-Translatables](../qa/non-translatables.md).

## Quick reference

| Action | Shortcut / How |
|---|---|
| Add a range-anchored comment to selected text | **Ctrl+M** with text selected, or right-click → **💬 Add comment** |
| Add a segment-level comment | **Ctrl+M** with no selection (cursor only), or right-click → **💬 Add segment comment** |
| Jump to a commented segment | Click its **Segment #N** header in the all-comments list |
| Open a comment from the grid | Hover the highlight for a tooltip; right-click the highlight, the cell, or the Status cell → **💬 Open comment(s)** |
| Edit a specific comment | Right-click its header → **✏️ Edit comment…** |
| Delete a specific comment | Right-click its header → **🗑️ Delete comment** |
| Generate proofreading comments | **QA ▸ Proofreading ▸ Proofread Translation…** |
| Delete one proofreading comment | **🗑️** button on its entry in the **✅ Proofreading** list |
| Delete all proofreading comments | **QA ▸ Proofreading ▸ Delete All Proofreading Comments** |
| Configure the author name for exported comments | **Settings → User Identity → Translator Name** |

## Related

* [Editing & Confirming](editing-confirming.md)
* [Keyboard Shortcuts (Workbench)](keyboard-shortcuts.md)
* [Segment Statuses](segment-statuses.md)

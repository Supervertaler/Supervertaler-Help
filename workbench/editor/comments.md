---
title: "Comments"
---

The **💬 Comments** tab in Workbench's right panel is where per-segment annotations live. There are two sub-tabs:

* **📝 Segment** — comments you author while translating: context notes, queries for the client, reminders to yourself, anchored highlights on specific words.
* **✅ Proofreading** — read-only AI-generated proofreading feedback, keyed by the LLM that produced it.

Both are stored on the segment itself and persist in the `.svproj` file. Segment comments are **exported to the final document as Word comments** (yellow comment bubbles in the right margin of the exported `.docx`), with the range highlight covering exactly the words you anchored the comment to. Proofreading comments are review-only and don't export.

## Segment comments

### Two kinds: segment-level and range-anchored

There are two kinds of segment comment:

* **Segment-level (no anchor)** — a general note about the whole segment. In the exported `.docx` the Word comment anchors to the entire paragraph.
* **Range-anchored** — attached to a specific word or phrase you selected. In the exported `.docx` the Word comment highlights exactly those characters, the same way Trados and memoQ comments do.

Both kinds coexist and you can have many of each on the same segment.

### Adding a range-anchored comment (Ctrl+Shift+M)

1. Click into the source or target cell of a segment.
2. Select the text the comment is about (e.g. `schroef`, `aangebracht`, or a multi-word phrase).
3. Press **Ctrl+Shift+M**.
4. A dialog opens showing which segment + which field (source or target) you're anchoring to, plus a snippet of your selection for confirmation. Type the comment, click **OK**.

The anchored text immediately gets a soft amber background in the editor cell so you can see at a glance which words have comments attached. The new comment also appears in the all-comments list above (see below).

:::tip
**Ctrl+Shift+M** instead of Trados's **Ctrl+M** because Workbench's **Ctrl+M** is already bound to QuickTrans. The "Shift" naturally reads as "specialised version of the M action."
:::

### Adding a segment-level (unanchored) comment

Two ways:

* **Via the bottom editor**: click into the segment, switch to the **💬 Comments → 📝 Segment** sub-tab (or press **Ctrl+N** to jump there with the editor focused), type your comment in the bottom area. Saved as you type. This works for the simple one-comment-per-segment case.
* **Via Ctrl+Shift+M with no selection**: place the cursor in the source or target cell without selecting any text, press Ctrl+Shift+M. The comment is segment-level. Useful when you want to add a second comment to a segment without disturbing an existing one.

### The all-comments list

The top half of the Segment sub-tab shows **one entry per Comment** — not per segment. A segment with three comments shows three entries, in document order. Each entry has:

* A clickable **Segment #N** header. For anchored comments, the header reads `Segment #N  ⚓ source` or `Segment #N  ⚓ target` to tell you what kind of anchor it has.
* For anchored comments: a quoted snippet of the anchored text, so you can see what the comment is *about* without jumping to the segment.
* The full comment body.
* A small footer line with the author and timestamp, plus a `(right-click for edit/delete)` hint.

Clicking the **Segment #N** header jumps the grid to that segment (cross-page-aware — switches pagination first if needed).

**Right-click** on a Segment header (or anywhere on the entry) opens a context menu with **✏️ Edit comment…** and **🗑️ Delete comment**. Edit opens a small dialog pre-populated with the existing text; saving with an empty text field deletes the comment. Delete prompts for confirmation.

The list rebuilds itself in real time as you add, edit, or remove comments. The splitter between the list and the bottom editor can be dragged to give either side more space.

### The bottom editor

The bottom editor is the legacy "one comment per segment" UI. It still works for the simple case (current segment has zero or one segment-level comment). When the current segment is more complex — multiple comments, or any anchored comment — the editor goes **read-only** with a placeholder pointing you to the all-comments list above. This prevents typing in the bottom editor from accidentally clobbering anchored or multi-line comment structures.

In practice: simple segments use the bottom editor as before; segments with anchored or multiple comments use Ctrl+Shift+M and the right-click context menu via the all-list.

### Editor visual cue: amber background

Anchored comment ranges show a soft amber background in the source or target cell editors. This coexists with the existing syntax highlighting (tag pink, spellcheck underlines, etc.) — the amber is applied as a background colour on the anchored characters only.

If you edit the target text after creating an anchored comment, the amber highlight stays at its original character offsets. If your edit shifts the anchor's intended target, the highlight may end up on slightly-different wording. The simplest workaround is to edit the text first, then create the anchored comment.

### Comments in exported documents

When you export your project back to a Word document (**File → Export → Export Translated Document…**), every segment comment becomes a Word comment in the output `.docx`. Behaviour per comment kind:

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

The **✅ Proofreading** sub-tab is read-only. It shows AI-generated feedback for the current segment, organised by which LLM produced it (so if you ran the same project through multiple proofreading passes with different models, you can compare what each model flagged).

To populate this tab, run **AI → Batch AI Proofread** on your project. Each segment that the proofreader flagged gets an entry, with the model's findings shown verbatim. There's no editing — you read the feedback, decide whether to act on it, and either change the target text or leave it alone.

Proofreading comments are **not** exported to the final document. They're a translator-side review tool.

## Quick reference

| Action | Shortcut / How |
|---|---|
| Focus the bottom comments editor (Segment sub-tab) | **Ctrl+N** |
| Add a range-anchored comment to selected text | **Ctrl+Shift+M** with text selected |
| Add a segment-level comment via dialog | **Ctrl+Shift+M** with no selection (cursor only) |
| Add a segment-level comment via inline editor | Click into the bottom editor and type |
| Jump to a commented segment | Click its **Segment #N** header in the all-comments list |
| Edit a specific comment | Right-click its header → **✏️ Edit comment…** |
| Delete a specific comment | Right-click its header → **🗑️ Delete comment** |
| Configure the author name for exported comments | **Settings → User Identity → Translator Name** |

## Related

* [Editing & Confirming](editing-confirming.md)
* [Keyboard Shortcuts (Workbench)](keyboard-shortcuts.md)
* [Segment Statuses](segment-statuses.md)

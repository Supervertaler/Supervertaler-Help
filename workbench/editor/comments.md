---
title: "Comments"
---

The **💬 Comments** tab in Workbench's right panel is where per-segment annotations live. There are two sub-tabs:

* **📝 Segment** — comments you author while translating (context notes, queries for the client, reminders to yourself, etc.).
* **✅ Proofreading** — read-only AI-generated proofreading feedback, keyed by the LLM that produced it.

Both are stored on the segment itself and persist in the `.svproj` file. Segment comments are **exported to the final document as Word comments** (yellow comment bubbles in the right margin of the exported `.docx`); proofreading comments are review-only and don't export.

## Segment comments

### Adding a comment

1. Click into a segment in the editor.
2. Switch to the **💬 Comments** tab in the right panel (or press **Ctrl+N** to jump straight to it with the editor focused).
3. Type your comment in the bottom editor area (under *"✏️ Comment on current segment"*).
4. The comment is saved immediately as you type — no Save button needed.

The presence of a comment is indicated visually on the segment's row (small marker in the Status column) and in its tooltip, so you can see at a glance which segments have annotations.

### The all-comments list

The top half of the Segment sub-tab shows **every segment in the project that has a comment**, in document order. Each entry has:

* A clickable **Segment #N** header.
* The full comment text below.
* A faint horizontal rule separating it from the next entry.

Clicking the **Segment #N** header jumps the grid to that segment. This works across pagination — if the target segment is on a different page, Workbench switches to that page first, then selects the row.

This list rebuilds itself in real time as you edit. Add or remove a comment, and the list updates instantly.

The splitter between the list and the editor can be dragged to give either side more space. The default split is roughly 60% list / 40% editor.

### Editing or removing a comment

There's no separate "edit comment" dialog. To change a comment:

1. Click the **Segment #N** header in the all-comments list (or just click that segment in the grid). The editor below populates with that segment's current comment.
2. Edit the text. Changes are saved as you type.
3. To remove a comment entirely, clear all the text in the editor. The segment drops out of the all-comments list once the field is empty.

### Comments in exported documents

When you export your project back to a Word document (**File → Export → Export Translated Document…**), every segment comment becomes a Word comment in the output `.docx`. The comment bubble appears in the right margin of Word, anchored to the paragraph where the segment lives.

The comment author defaults to the **Translator Name** field in **Settings → User Identity** — set that if you want comments attributed to your real name rather than your system username. Initials are derived automatically (multi-word names take the first letter of each word, e.g. `Michael Beijer` → `MB`; single-word names take the first two characters uppercased, e.g. `mbeijer` → `MB`).

After export, Workbench logs how many comments were attached:

```
✓ Attached 4 segment comment(s) as Word comments
```

If any comments couldn't be matched to a paragraph (rare — usually because the target text was heavily reformatted by the Okapi merge step), the log says so and the export still completes — the comment-attach step is purely additive.

### Comments and bilingual table exports

For bilingual-table export formats (Supervertaler Bilingual Table, memoQ, CafeTran, etc.), segment comments are written to a dedicated **Notes** column rather than as Word comments. This is the convention these formats already use, and re-importing the bilingual table later preserves the comments correctly.

## Proofreading comments

The **✅ Proofreading** sub-tab is read-only. It shows AI-generated feedback for the current segment, organised by which LLM produced it (so if you ran the same project through multiple proofreading passes with different models, you can compare what each model flagged).

To populate this tab, run **AI → Batch AI Proofread** on your project. Each segment that the proofreader flagged gets an entry, with the model's findings shown verbatim. There's no editing — you read the feedback, decide whether to act on it, and either change the target text or leave it alone.

Proofreading comments are **not** exported to the final document. They're a translator-side review tool.

## Quick reference

| Action | Shortcut |
|---|---|
| Focus the comments editor (Segment sub-tab) | **Ctrl+N** |
| Add a comment to the current segment | Click into the editor and type |
| Jump to a commented segment | Click its **Segment #N** header in the all-comments list |
| Configure the author name for exported comments | **Settings → User Identity → Translator Name** |

## Related

* [Editing & Confirming](editing-confirming.md)
* [Keyboard Shortcuts (Workbench)](keyboard-shortcuts.md)
* [Segment Statuses](segment-statuses.md)

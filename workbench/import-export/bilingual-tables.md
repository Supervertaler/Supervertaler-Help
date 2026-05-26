---
title: "Supervertaler Bilingual Table"
---

The **Supervertaler Bilingual Table** is a branded Word (DOCX) export that lays
your project out as a side-by-side table — handy for reviewing, proofreading, or
handing off to someone who doesn't use a CAT tool. Its defining feature: one
variant can be edited and **re-imported** to pull the changes straight back into
your project.

## When to use it

- A proofreading round-trip in Word: export, edit the targets, re-import.
- Sharing with a reviewer who doesn't use your CAT tool.
- Client delivery or archiving (the formatted version).

## Columns

| Column | Description |
|--------|-------------|
| **#** | Segment number |
| **Source** | Source text |
| **Target** | Target text (edit this when proofreading) |
| **Status** | Segment status |
| **Comments** | Segment comments — edit, add, or clear; changes round-trip on re-import |

A header above the table shows the project name, language pair, segment count, and export date.

## Two variants

**Project → Export** offers two versions:

- **Supervertaler Bilingual Table — With Tags (DOCX)** — formatting tags stay visible as markup. This is the **re-importable** version: edit the Target cells, save, and bring the changes back in (see below). Don't change the segment numbers (#) or the source text.

<figure><img src="/.gitbook/assets/Supervertaler-Workbench-Bilingual-Table-With-Tags.png" alt=""><figcaption><p>The <strong>With Tags</strong> variant: formatting shown as visible markup, with a notice that segment numbers and source text must stay unchanged so the file can be re-imported after proofreading.</p></figcaption></figure>

- **Supervertaler Bilingual Table — Formatted (DOCX)** — inline formatting (bold, italic, underline) is rendered instead of shown as tags. This version is for **client delivery or archiving** and **cannot be re-imported**.

<figure><img src="/.gitbook/assets/Supervertaler-Workbench-Bilingual-Table-Formatted.png" alt=""><figcaption><p>The <strong>Formatted</strong> variant: inline formatting rendered for client delivery or archiving — not re-importable.</p></figcaption></figure>

## Round-trip (proofread and re-import)

1. Export the **With Tags** version.
2. Edit in Word — leave the **#** and **Source** columns untouched:
   - The **Target** column for translation edits.
   - The **Comments** column to edit, add, or clear segment comments. New comments added to segments that had none in Workbench are also round-tripped.
3. Back in Workbench: **Project → Import → Bilingual Table (DOCX) – Update Project**.
4. Supervertaler diffs the file against your project and shows a preview before applying. Target changes set the segment back to "Not Started" so you can re-confirm; comment changes replace the segment's existing comments verbatim with the proofreader's text (no `[Review: …]` wrapping or appending — round-trip in, round-trip out).

:::note
Re-imports written by Workbench v1.10.182 and earlier had a bug where comments-only edits were silently discarded — only segments whose target text *also* changed had their comments updated. Fixed in v1.10.183: a comment edit on its own is now picked up, and a comment cleared in the bilingual file clears it on the segment.
:::

## Other bilingual tables

To round-trip back into a **CAT tool**, use that tool's own bilingual format (memoQ, CafeTran, Phrase, Trados Bilingual Review) rather than the Supervertaler table — see [CAT Tool Overview](../cat-tools/overview.md).

## Related

- [Supported File Formats](formats.md)
- [Exporting Translations](exporting.md)

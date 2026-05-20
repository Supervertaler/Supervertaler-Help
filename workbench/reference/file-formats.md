---
title: "Supervertaler Bilingual Table"
---

The **Supervertaler Bilingual Table** is a branded Word (DOCX) export that lays
your project out as a side-by-side table — handy for reviewing, proofreading, or
handing off to someone who doesn't use a CAT tool. One variant can be edited and
**re-imported** to pull the changes back into your project.

## Columns

The table has five columns:

| Column | Description |
|--------|-------------|
| **#** | Segment number |
| **Source** | Source text |
| **Target** | Target text (edit this when proofreading) |
| **Status** | Segment status |
| **Notes** | Segment comments |

A header above the table shows the project name, language pair, segment count, and export date.

## Two variants

**File → Export** offers two versions:

- **Supervertaler Bilingual Table — With Tags (DOCX)** — formatting tags stay visible as markup. This is the **re-importable** version: edit the Target cells, save, and bring the changes back in (see below). Don't change the segment numbers (#) or the source text.
- **Supervertaler Bilingual Table — Formatted (DOCX)** — inline formatting (bold, italic, underline) is rendered instead of shown as tags. This version is for **client delivery or archiving** and **cannot be re-imported**.

## Round-trip (proofread and re-import)

1. Export the **With Tags** version.
2. Edit the **Target** column (and **Notes**, if you like) in Word — leave the **#** and **Source** columns untouched.
3. Back in Workbench: **File → Import → Bilingual Table (DOCX) – Update Project**.
4. The edited targets (and notes) are matched back to your segments by number.

## Related

- [Bilingual Tables](../import-export/bilingual-tables.md) — overview of side-by-side exports
- [Supported File Formats](../import-export/formats.md) — everything Workbench can import and export
- [Exporting Translations](../import-export/exporting.md)

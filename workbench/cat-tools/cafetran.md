---
title: "CafeTran Workflow"
---

Supervertaler supports CafeTran bilingual table DOCX workflows.

## Export from CafeTran

1. Open your project in CafeTran
2. Go to **Project → Export → Bilingual Table**
3. Choose **DOCX** format

## Import to Supervertaler

1. In Supervertaler: **Project → Import → CafeTran → Bilingual Table (DOCX)…** and select the exported DOCX
2. Check the language pair in the **Confirm language pair** prompt and click **OK** (see below)
3. Translate and review in the grid
4. Confirm segments when ready (`Ctrl+Enter`)

### The language pair

A CafeTran bilingual table doesn't name its languages, so Supervertaler asks.
The prompt is pre-filled from the languages Word stores on the source and target
columns, or from the column headers if they are language codes. Check both
before you click **OK**: TM matches are looked up for this pair.

:::caution
Before v1.10.372, **every CafeTran project was created as English → Dutch**,
whatever its real languages – and a project with the wrong pair finds no TM
matches at all. If you have an older CafeTran project in another language pair,
export it back to a bilingual table and import that file again with the right
languages; your translations come along.
:::

## Export back to CafeTran

1. In Supervertaler: **Project → Export → CafeTran → Bilingual Table - Translated (DOCX)…**
2. Save the file

## Reimport to CafeTran

1. In CafeTran: **Project → Import** and select the bilingual table
2. Choose merge options as needed

## Notes

- Preserve pipe-style markers and any CAT tags.
- Don’t change the bilingual table structure in Word.

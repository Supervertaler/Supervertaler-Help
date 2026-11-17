---
title: "Phrase (Memsource) Workflow"
---

Supervertaler works with Phrase (formerly Memsource) jobs in two formats:

| Format | When to use it |
|--------|----------------|
| **MXLIFF** (`.mxliff`) | Recommended. The file Phrase itself uses for a job. Existing translations, their status and locked segments come in with it, and the export changes only what you changed. New in v1.10.377. |
| **Bilingual DOCX** | When you only have Phrase's bilingual Word file. |

Both are under **Project → Import → Phrase (Memsource)** and **Project → Export → Phrase (Memsource)**.

## MXLIFF

### Import

1. In Phrase, download the job as a bilingual MXLIFF file.
2. In Supervertaler: **Project → Import → Phrase (Memsource) → MXLIFF (.mxliff)…** and pick the file.

The source and target languages are read from the file. If Supervertaler doesn't recognise one of them, the **Confirm language pair** prompt asks you.

What comes in with each segment:

| In Phrase | In Supervertaler |
|-----------|------------------|
| Confirmed | **Confirmed** |
| Machine translation, not confirmed | **MT** |
| Translation memory match, not confirmed | **Pre-translated**, with its match percentage |
| Any other translation, not confirmed | **Draft** |
| No translation | **Not started** |
| Locked | Locked, and never written to on export |

When the import finishes, a summary tells you how many segments have a translation, how many are confirmed and how many are locked. Reading 20,000 segments takes about 1.5 seconds.

A file that isn't a Phrase MXLIFF is refused, with the reason (for example, not an XLIFF 1.2 file, or no segments found). So is an MXLIFF that isn't UTF-8.

### Phrase's tags

Phrase's inline tags, such as `{b>…<b}` and `{1}`, stay in the text exactly as Phrase wrote them. Keep them as they are, as you would in Phrase.

In **WYSIWYG** view, they show as the formatting they stand for:

| Tag | Shows as |
|-----|----------|
| `{b>…<b}` | **bold** |
| `{i>…<i}` | *italic* |
| `{u>…<u}` | underlined |
| `{bi>…<bi}` and other combinations | both at once |
| `{sup>…<sup}`, `{sub>…<sub}` | superscript, subscript |
| `{1}`, `{2}`, … | a small grey marker |

When you edit such a segment in WYSIWYG view, it is saved with Phrase's own tags, never Supervertaler's `<b>`, so the file still goes back to Phrase correctly. **Tags** and **Compact** view show the tags themselves. The same applies to projects imported from a Phrase bilingual DOCX.

### Export

1. **Project → Export → Phrase (Memsource) → MXLIFF - Translated (.mxliff)…**
2. Save the file. Supervertaler suggests the original name with `_translated` added.
3. In Phrase, upload this file to the same job to bring the translation in.

If Supervertaler can't find the original MXLIFF (for example, it has been moved), it asks you to pick it.

The export changes only two things in each segment: the translation, and the confirmed flag. A segment that is **Confirmed**, **Proofread** or **Approved** in Supervertaler is confirmed in Phrase; any other status is not. Everything else in the file stays exactly as Phrase wrote it: its MT and TM suggestions, timestamps and the preview. A file exported without changes is identical to the original.

Some segments are always left as they are:

- a segment whose translation is empty in Supervertaler: an empty segment never removes a translation from the file;
- a locked segment;
- a segment whose translation and confirmed flag haven't changed.

The confirmation tells you how many segments were changed.

:::caution
Don't split or join segments in an MXLIFF project. The export pairs each segment with its unit in the file, so it refuses, and writes nothing, if the number of segments no longer matches the file, or if a segment's source text doesn't match. The same happens if you pick a different MXLIFF from the one you imported.
:::

## Bilingual DOCX

### Export from Phrase

1. In Phrase Editor, go to **Document → Export → Bilingual DOCX**
2. Save the file

### Import to Supervertaler

1. In Supervertaler: **Project → Import → Phrase (Memsource) → Bilingual (DOCX)…** and select the bilingual DOCX
2. Translate (AI or manual) and review in the grid
3. Confirm segments when ready (`Ctrl+Enter`)

### Export back to Phrase

1. In Supervertaler: **Project → Export → Phrase (Memsource) → Bilingual - Translated (DOCX)…**
2. Save the file

The project remembers its DOCX when you save and reopen it, so the export doesn't ask you to find the file again. Before v1.10.377 it did, every time you reopened the project.

### Reimport to Phrase

Import the bilingual DOCX back into Phrase to update the document.

### Notes

- Keep any tags/placeholders exactly as-is.
- Don't change the table structure in Word.

:::caution
Don't merge or split segments if you plan to reimport. A project imported from a Phrase bilingual DOCX doesn't allow it.
:::

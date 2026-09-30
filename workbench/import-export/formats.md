---
title: "Supported File Formats"
---

Supervertaler can import and export several formats depending on your workflow.

## Standard documents

- **DOCX** (Microsoft Word): import a document, translate in the grid, export a translated DOCX.
- **TXT** / **MD** (plain text and Markdown): each line becomes a segment, or each sentence if you tick **Split lines into sentences**. See [Importing Text Files](/workbench/import-export/txt-import/).

## Adding more source text to a project

A client often sends a few more sentences after you've started. If you created
the project from pasted text (**📝 Paste Text** in New Project), from a plain-text
or Markdown file, or with **⭐ Start Empty**, you can add them to the project you
already have, with no need to make a text file and import it (from v1.10.372):

1. Choose **Edit → ➕ Add Source Text…**
2. Paste or type the new text and click **Add Segments**.

The text is split into sentences the same way as when a project is created
(following your [Segmentation Rules](/workbench/settings/segmentation-rules/)),
and added as new segments at the end of the project. The grid jumps to the first new segment, and
**Ctrl+Z** takes the whole addition back out.

Each line you paste becomes its own paragraph, so a plain-text export puts the
added text on new lines rather than gluing it onto the last one.

:::note
**Add Source Text** isn't available for DOCX, Okapi (IDML, HTML, XLIFF, PO, XLSX,
PPTX) or bilingual CAT-tool projects, and says so if you try. Those projects are
exported back into their original file, which has no place for new text. If the
grid is sorted, switch back to **Document Order** (Sort menu) first.
:::

## Other formats via Okapi

The bundled **Okapi sidecar** lets Supervertaler round-trip a wider set of formats. Pick a file in any of the following types via **Project → Import → Import Document…**, translate in the grid, then **Project → Export → Export Translated Document…** to write a translated file back in the same format:

| Format | Extension(s) | Notes |
|---|---|---|
| **Adobe InDesign Markup** | `.idml` | Drop in, translate, drop out – no need to round-trip via Trados/memoQ first. Inline tags appear as `<g1>...</g1>` markers in the grid; preserve them in the translation. |
| **HTML** | `.html`, `.htm` | Anchors, images, buttons, and other inline elements are exposed as `<gN>...</gN>` / `<xN/>` tags. The translated HTML reconstructs the original markup byte-perfectly. |
| **XLIFF 1.2** | `.xliff`, `.xlf` | The industry-standard bilingual interchange format. Useful for files exported from any CAT tool that doesn't have its own dedicated entry. |
| **gettext PO** | `.po` | Source strings are translated; `msgctxt` and plural forms are preserved. |
| **Microsoft Excel** | `.xlsx` | Cells, formulas, and styling round-trip via the Office Open XML filter. |
| **Microsoft PowerPoint** | `.pptx` | Slides and slide notes are extracted; layout and master slides round-trip. |

### How it works

Okapi extracts the translatable content from the source file plus a *skeleton* file that preserves the original structure. You translate the extracted content; the merge step combines your translation with the skeleton to reconstruct the original format with the new text in place.

:::note
**Tag handling**: when you see `<g1>` / `</g1>` / `<x2/>` markers in the source segment, leave them in the translation in the same positions. They map back to inline elements like links, buttons, or formatting runs in the original file.
:::

## CAT tool exchange formats

Use these formats when you need to round-trip back into a CAT tool.

- **memoQ**
  - Bilingual DOCX
  - XLIFF (memoQ export)
- **Trados Studio**
  - Packages: `.sdlppx` import → `.sdlrpx` return (recommended)
  - Bilingual Review DOCX (special workflow)
- **Phrase (Memsource)**
  - Bilingual DOCX
- **CafeTran Espresso**
  - Bilingual DOCX table

## Multi-file projects

- **Folder import (Multiple Files)**: import a folder containing DOCX/TXT files into a single multi-file project.

:::caution
For CAT tool round-trips, always import and export the matching CAT format. Mixing formats can break tags/statuses on reimport.
:::

## Related pages

- [Importing DOCX Files](/workbench/import-export/docx-import/)
- [Importing Text Files](/workbench/import-export/txt-import/)
- [Multi-File Projects](/workbench/import-export/multi-file/)
- [Exporting Translations](/workbench/import-export/exporting/)
- [Bilingual Tables](/workbench/import-export/bilingual-tables/)

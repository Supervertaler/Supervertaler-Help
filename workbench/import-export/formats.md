---
title: "Supported File Formats"
---

:::note
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
:::

Supervertaler can import and export several formats depending on your workflow.

## Standard documents

- **DOCX** (Microsoft Word): import a document, translate in the grid, export a translated DOCX.
- **TXT** (plain text): each line becomes a segment.

## Other formats via Okapi

The bundled **Okapi sidecar** lets Supervertaler round-trip a wider set of formats. Pick a file in any of the following types via **File → Import → Other format via Okapi…**, translate in the grid, then **File → Export → Original format via Okapi…** to write a translated file back in the same format:

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

- [Importing DOCX Files](docx-import.md)
- [Importing Text Files](txt-import.md)
- [Multi-File Projects](multi-file.md)
- [Exporting Translations](exporting.md)
- [Bilingual Tables](bilingual-tables.md)

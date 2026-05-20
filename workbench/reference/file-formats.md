---
title: "File Format Reference"
---

This page summarises the **Supervertaler project data** export — a bilingual,
six-column layout available as either a Word table (DOCX) or tab-separated
values (TSV). Use it for review, archiving, spreadsheet analysis, or scripted
processing of a project's segments.

For the full technical specification, see the [repository copy](https://github.com/Supervertaler/Supervertaler-Workbench/blob/main/docs/specifications/SUPERVERTALER_DATA_FORMAT.md).

## Columns

| Column | Description |
|--------|-------------|
| **ID** | Segment identifier |
| **Status** | Translation status (e.g. not started, pre-translated, draft, confirmed, locked) |
| **Source** | Source text |
| **Target** | Target text |
| **Paragraph** | Original paragraph ID |
| **Notes** | Translator / proofreader comments (optional) |

## The two formats

- **DOCX** — a Word table with the six columns above. Best for review, printing, or Word-based workflows.
- **TSV** — tab-separated, UTF-8, with a header row. Best for opening in a spreadsheet or processing with scripts.

## Exporting

**File → Export → Supervertaler project data**, then choose DOCX or TSV.

## Related

- [Supported File Formats](../import-export/formats.md) — everything Workbench can import and export
- [Bilingual Tables](../import-export/bilingual-tables.md) — bilingual round-trip with memoQ / CafeTran / Trados
- [Exporting Translations](../import-export/exporting.md)

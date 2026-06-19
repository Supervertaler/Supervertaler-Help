---
title: "Exporting Translations"
---

When you’re done translating, export in a format that matches your workflow.

## Export steps

1. Go to **Project → Export**
2. Choose an export type (for example DOCX, bilingual table, or a CAT return format)
3. Pick a destination and save

:::tip
For **Export Translated Document** (and Simple Text), the Save dialog opens in
your project's `target/` folder by default, so finished translations land
alongside their sources. You can still browse elsewhere — see
[The Project Folder](project-folder.md).
:::

## CAT tool round-trips

If you started from a CAT exchange format (memoQ/Trados/Phrase/CafeTran), export the matching return format.

### Important rules for round-trips

- **Segment count must match**: don’t merge or split segments.
- **Keep tags balanced**: for example `<b>text</b>` (not `<b>text`).
- **Don’t “pretty edit” bilingual tables**: changing the table structure in Word can break reimport.
- Run your CAT tool’s QA after reimport.

:::caution
Don’t merge or split segments in Supervertaler when you plan to reimport into a CAT tool.
:::

## Choosing the right export

- For CAT tool workflows, use the matching CAT export:
	- memoQ bilingual DOCX
	- Trados return package (SDLRPX) when you imported SDLPPX
	- Phrase bilingual DOCX
	- CafeTran bilingual table DOCX
- For review-only delivery, consider [Bilingual Tables](bilingual-tables.md).

## Checking the export

After every DOCX export, Supervertaler automatically compares the word count of the exported file against your translated segments and warns you if text looks like it was dropped. See [Export Verification (Word-Count Check)](export-verification.md).

## Related pages

- [Supported File Formats](formats.md)
- [Export Verification (Word-Count Check)](export-verification.md)
- [Bilingual Tables](bilingual-tables.md)
- [CAT Tool Overview](../cat-tools/overview.md)

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
alongside their sources. You can still browse elsewhere – see
[The Project Folder](/workbench/import-export/project-folder/).
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
- For review-only delivery, consider [Bilingual Tables](/workbench/import-export/bilingual-tables/).

## Checking the export

After you export a translated document – DOCX, and since v1.10.372 also PPTX, XLSX, IDML, HTML, XLIFF and PO – Supervertaler automatically compares the word count of the exported file against your translated segments and warns you if text looks like it was dropped. See [Export Verification (Word-Count Check)](/workbench/import-export/export-verification/).

## Backing up all your TMs and termbases

**Project → Export → 📦 Back Up All TMs & Termbases…** writes every translation memory and termbase in your Supervertaler database to open files, in one go (from v1.10.372). Choose a folder, and Supervertaler creates a `Supervertaler resources <date time>` folder inside it with:

- a `TMs` folder – one **TMX** file per translation memory;
- a `Termbases` folder – one tab-separated **TSV** file per termbase;
- a `README.txt` listing what was written and how many entries each file holds.

When it's done, a summary shows how many TMs, entries, termbases and terms were backed up, with an **Open Folder** button. If one TM or termbase can't be written, the others still are, and the summary lists the problem.

Unlike the database file itself, these files open in any CAT tool, and you can import them back into Supervertaler if you ever need to rebuild: the TMX files through **📥 Import TMX** in the **💾 TMs** tab (see [Importing TMX Files](/workbench/translation-memory/importing-tmx/)), the TSV files as termbases (see [Importing Terms](/workbench/termbases/importing/)).

- **TMX entries keep their details** – each entry's own language pair (a TM can hold entries in both directions), its dates, author and note.
- **Large TMs are no problem** – they're written out in a stream rather than loaded into memory.
- **The files always open** – characters that XML forbids, such as a stray control character that crept into a TM, are left out.
- **Non-translatables survive the trip** – the termbase TSV files have a **Non-translatable** column, and the TSV import reads it back, so a restored termbase keeps its non-translatables instead of turning them into ordinary terms.

:::tip
Your TMs and termbases all live in one database file, `supervertaler.db` (see [User Data Folder](/workbench/reference/data-folder/)), which other CAT tools can't open. This backup gives you the same data as open files that you can check, archive or take to another tool. Project files have their own safeguards: see [Backup](/workbench/settings/backup/).
:::

## Related pages

- [Supported File Formats](/workbench/import-export/formats/)
- [Export Verification (Word-Count Check)](/workbench/import-export/export-verification/)
- [Bilingual Tables](/workbench/import-export/bilingual-tables/)
- [CAT Tool Overview](/workbench/cat-tools/overview/)

---
title: "Import/Export Errors"
---

This page covers common problems when importing or exporting files.

## “Cannot read file” / import fails

**Common causes:**

- The file is open in Word (or another app)
- The file is read-only or in a protected location
- The file format doesn’t match the workflow

**Fix:**

1. Close the file everywhere (Word, CAT tool editors, preview panes)
2. Copy it to a simple path (for example `C:\Temp\`) and try again
3. Re-export from the CAT tool using the recommended bilingual/package format

## memoQ bilingual shows no segments

**Cause:** Export format doesn’t contain the expected bilingual table.

**Fix:**

- Re-export from memoQ as **Bilingual DOCX** in a **two-column table** format.
- Open the DOCX in Word and confirm it really contains a Source/Target table.

## Import fails with “No module named 'PySide6'”

**Cause:** a memoQ bilingual DOCX or memoQ XLIFF file whose language pair couldn’t be read from the file. Supervertaler is meant to ask you for the pair then, but before v1.10.372 that prompt couldn’t open and the import stopped with this error.

**Fix:** update to v1.10.372 or later. The **Confirm language pair** prompt then opens, and you pick the source and target language yourself.

## The project was created with the wrong language pair

**Symptom:** the grid looks fine, but no TM matches ever appear, although the TM itself looks complete.

**Cause:** older versions guessed the language pair of some bilingual files without telling you. Most notably, **every CafeTran project was created as English → Dutch** before v1.10.372, whatever its real languages.

**Fix:**

- Update. Since v1.10.372, the Trados bilingual review DOCX, CafeTran and Déjà Vu X3 imports show the language pair they found for you to confirm, and the memoQ imports ask when they can’t read it from the file. See [CAT Tool Integration Overview](/workbench/cat-tools/overview/#the-language-pair).
- Import the file again and choose the right languages. If you’ve already translated in the old project, export the bilingual file first and import that one, so your translations come along.

More on this in [TM Matches Not Appearing](/workbench/troubleshooting/tm-matches/#2-does-the-project-have-the-right-language-pair).

## Trados SDLPPX fails to extract

**Common causes:**

- Corrupt/partial package
- Unsupported package structure

**Fix:**

- Ask for a fresh export from Trados Studio.
- Ensure the package includes all required files.

## Garbled characters / encoding issues

**Cause:** Text encoding problems coming from the source file or export.

**Fix:**

- Re-export from the source tool with a modern Unicode/UTF-8-friendly path when possible.
- For Latin-1/Windows-1252 mojibake (e.g. "Ã©" appearing where "é" should be), open the file in a text editor that supports re-interpreting the encoding (Notepad++ has *Encoding → Convert to UTF-8*) or run `ftfy` on it from the command line.

## Segments don’t match on reimport

**Cause:** Segment structure changed.

**Fix:**

- Don’t merge or split segments in Supervertaler
- Export using the matching CAT format
- Avoid deleting placeholder/tag-only segments

## “Source file not found” during export

**Cause:** The original source file/folder was moved after import.

**Fix:**

- Use **Project → Export → 🔗 Relocate Source Folder** and point it to the new location.
- If the original source is gone, re-import the project from the correct source.

## “Possible Missing Text in Export” warning

**Cause:** the exported file contains noticeably fewer words than your segments. This check runs after exporting DOCX, PPTX, XLSX, IDML, HTML, XLIFF and PO files.

**Fix:** open the exported file and check it before delivering. If the difference is expected, the check can be tuned or switched off. See [Export Verification (Word-Count Check)](/workbench/import-export/export-verification/).

## “Failed to create TM metadata” when importing a TMX

**Cause:** in versions before v1.10.372, importing a TMX under a TM name that was already taken (for example the same file a second time) ended with this error.

**Fix:** update, or choose a different name. Current versions suggest a free name and tell you if the one you type is taken. See [Importing TMX Files](/workbench/translation-memory/importing-tmx/).

## Exported file has no translations

**Cause:** Targets are empty or the wrong export format was chosen.

**Fix:**

- Verify the Target column contains translations.
- Export the matching format for the workflow you imported.

## Formatting lost on reimport

**Cause:** Tags not preserved.

**Fix:**

- Verify tags are balanced (for example `<b>text</b>`)
- Don’t delete CAT placeholder tags
- Re-export using the correct CAT workflow

## Bilingual table reimport fails

**Cause:** Bilingual tables are great for review, but not always suitable for CAT tool reimport.

**Fix:**

- Prefer the dedicated CAT exchange formats (memoQ/Trados/Phrase/CafeTran).
- If you must use a bilingual table, don’t edit the table structure in Word.

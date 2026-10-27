---
title: "SuperCleaner"
---

:::caution[Not released yet]
SuperCleaner is under construction. This page describes how it will work, so you can see what is coming; the details may still change before it ships. The safety check described below is already built and tested.
:::

<!--
  Written ahead of the code from the design (Plugin Core: docs/design/docx-tag-cleaner.md
  and docx-tag-cleaner-user-notes.md), and published early with the notice above.
  When SuperCleaner ships, remove the notice and settle:
  - the version it ships in (add "(from v18/19.20.xxx)" to the CHANGELOG entry);
  - where the switch lives and its exact wording ("Settings → SuperCleaner → Clean Word
    files as they are added to a project" is the working name);
  - the names of the OCR clean-up options as they appear in the dialog;
  - where the per-file report appears (planned: Trados's Messages for the conversion);
  - tracked changes: accepted first, or such documents left as they are;
  - a screenshot of the settings and of a report line;
  - links from Getting Started, Import/Export and Troubleshooting.
-->

SuperCleaner tidies up Word documents **before Trados turns them into segments**, so you get fewer tags in the editor. It joins pieces of text that Word has split up for no visible reason, and removes Word's internal bookkeeping. The finished translation looks exactly like the original document.

It is meant for the documents that fill a segment with tags: files converted from PDF (ABBYY FineReader, Acrobat, Word's own PDF import) and documents that have been edited by many people.

## Why Word files have so many tags

Word stores text in pieces called *runs*, and a new run starts wherever anything about the formatting changes, or where Word merely noted that an edit happened. A paragraph that looks perfectly uniform can be stored as dozens of runs that differ only in things you cannot see: a character spacing of 0.1 pt, a different editing-session number, a font size of 11.5 instead of 11. Trados shows every one of those boundaries as a tag pair.

SuperCleaner removes the invisible boundaries. A sentence that came in as twenty runs goes into Trados as one.

## Turning it on

In Supervertaler's **Settings**, open **SuperCleaner** and tick **Clean Word files as they are added to a project**. It is off until you turn it on.

From then on SuperCleaner runs by itself whenever Trados converts a Word file: when you create a project, use **Open Document**, or add files to an existing project. There is nothing to click per file, and you don't need a project open first. Supervertaler's panes can stay closed.

It works in Trados Studio 2022, 2024 and 2026.

## What happens to your file

1. You add a Word file to a project as usual.
2. SuperCleaner makes a cleaned copy in a temporary folder and checks it against your original (see below).
3. Trados reads the cleaned copy instead of the original. It stores the cleaned copy in the project, and builds your translated document from it when you save the target.
4. The temporary copy is deleted.

**Your original file is never changed.** The translated document you deliver is the cleaned document, translated – it looks the same as the original, but with tidier formatting underneath.

## What it cleans

**Invisible clean-up – always on.** Only changes that cannot alter how the document looks or prints:

- pieces of text with identical formatting are joined into one;
- Word's editing-session numbers and spelling-check markers are removed.

This is where most of the tag savings come from.

**OCR clean-up – each option off until you tick it.** For documents converted from PDF, where the formatting is often meaningless anyway. These options *do* change the formatting, slightly and on purpose:

- reset character spacing, scaling, kerning and raised/lowered position;
- remove text and paragraph shading;
- remove text highlighting;
- change black text to *automatic* (skipped where the text sits on a dark background, where *automatic* would turn it white);
- remove bookmarks that nothing refers to;
- use one font, size or colour per paragraph when the differences are tiny;
- turn Symbol and Wingdings characters into ordinary Unicode characters;
- turn superscript 2 and 3 into ² and ³.

Leave them off for documents that were written in Word: the invisible clean-up is all those need.

## Why it can't damage your document

Before Trados ever sees the cleaned copy, SuperCleaner **compares it with your original, character by character**: the same text, the same formatting on every character, and the same paragraphs, tables, images, footnotes, fields, bookmarks and links. Headers, footers, footnotes, comments and text boxes are all included. Everything else in the file – styles, numbering, images – must be identical.

**If anything differs that you did not ask for, SuperCleaner throws the cleaned copy away and Trados gets your original, unchanged.** The same happens if a document cannot be read completely – a damaged or password-protected file, for example. Either way the file still goes into your project; SuperCleaner never stops you working.

This check was tested before release on more than 9,000 real Word documents from translation jobs, with more than 20,000 deliberately damaged copies. It caught every change, down to a single letter moved out of a bold word.

## Checking the result yourself

You don't have to, but you can:

- In the Trados editor, open **View → Preview**: it shows the document as Trados now holds it.
- **File → Save Target As** before you translate saves a copy you can open in Word next to the original.

## What you see afterwards

For every Word file, SuperCleaner reports what it did, for example:

> SuperCleaner: 1,240 text pieces joined into 310; 45 bookmarks removed.

If it used your original instead, the report says so and why.

## Notes

- **Word 2007 and later only** (.docx, .docm, .dotx, .dotm). Old .doc files are not cleaned: Trados converts those internally, past the point where SuperCleaner runs.
- **Files already in a project are not cleaned again.** SuperCleaner runs when Trados converts a file, so turning it on affects files you add from then on.
- **A handful of unusual files are left as they are.** Some programs write Word files in a way that SuperCleaner cannot prove it has understood exactly. It leaves those untouched rather than guess. In tests that was fewer than two files in a thousand.
- In **memoQ**, SuperCleaner runs from the Supervertaler for memoQ editor instead, before you import the file.
- **Background.** Translators have cleaned up Word files like this for a long time. Dave Turner's CodeZapper macros were the first that many translators used, and TransTools' Document Cleaner came later; both run in Word, so the file is cleaned there before it goes into the CAT tool. Some CAT tools also have a setting for reducing tags in Word files – in Trados, the Word file type can skip advanced font formatting such as tracking and kerning. SuperCleaner does the job as the file goes into Trados, and checks the result against your original before Trados sees it.

---

## See Also

- [Getting Started](/trados/getting-started/)
- [Import/Export](/trados/import-export/)
- [Batch Translate](/trados/batch-translate/)
- [Troubleshooting](/trados/troubleshooting/)

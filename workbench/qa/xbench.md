---
title: "Open in Xbench"
---

[ApSIC Xbench](https://www.xbench.net/) is the QA tool many translators already run next to memoQ and Trados. **QA → 🔬 Open in Xbench…** opens the current project in it, the way memoQ and Trados can (from v1.10.373).

## What Supervertaler writes

The files go into the project's `qa/xbench/` folder, next to its `source/` and `target/` folders. If the project hasn't been saved yet, they go into a temporary folder instead.

| File | What it is | In Xbench |
| --- | --- | --- |
| `<project>.xlf` | Every segment, as XLIFF | The **ongoing translation** – the file the QA checks run on |
| `<project> - key terms.txt` | The terms of the glossaries switched on (**Read**) for the project, one `source<TAB>target` line each | **Key terms**, for the *Key Term Mismatch* check |
| `<project>.xbp` | An Xbench project listing the two files | Opening it starts Xbench with both loaded |

A few details:

- **Segment numbers** are the XLIFF units' IDs, so Xbench's results point to the same segment numbers as the grid.
- **Statuses** carry over: confirmed segments are *translated*, approved and proofread ones are *signed off*, untranslated ones are marked as such, and locked segments are marked not to translate.
- **Inline tags** stay in the text as Supervertaler shows them.
- **Forbidden terms are left out** of the key terms, because Xbench would then demand them in the translation. A non-translatable term is written with itself as its translation. A glossary made the other way round (Dutch → English for an English → Dutch project) is flipped.

## Working with it

1. Choose **QA → 🔬 Open in Xbench…**. Xbench opens with the project loaded.
2. Run the checks in Xbench (**QA** tab → **Check Ongoing Translation**).
3. Fix what it finds in Supervertaler.
4. Choose **Open in Xbench…** again to write the files anew, then press **F5** in Xbench to reload them.

If Xbench isn't installed, or Windows has no program for `.xbp` files, Supervertaler says so and offers to open the `qa/xbench/` folder instead.

## See also

- [QA Checks](/workbench/qa/qa-checks/) – Supervertaler's own saved checks and its tags & codes check
- [Check with LanguageTool](/workbench/qa/languagetool/) – grammar and spelling
- [The Project Folder](/workbench/import-export/project-folder/)

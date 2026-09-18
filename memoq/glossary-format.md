---
title: "Importing and exporting termbases"
---

Termbases live in Supervertaler's shared database and are managed in the [Termbases window](/memoq/terminology/#the-termbases-window). This page is about the files that go in and out of it.

### What Import… and Add to… read

Two shapes of file, and the difference is decided by looking at the file, not by you:

**A delimited file with a header row** – what memoQ, Excel and Supervertaler for Trados export. Tab, semicolon or comma, whichever the header uses; cells may be quoted the way Excel quotes them. The two language columns are recognised by their headings – a language name such as *Dutch* or *English*, a code such as *nl* or *en-GB*, or a name with the code in brackets, *Dutch (nl)*. A column headed *Forbidden* (or *Status*) marks forbidden terms; one headed *Notes* (or *Definition*, *Comment*) is kept as the note.

```
Dutch (nl)	English (en)	Forbidden	Notes
elektrische module	electric module
elektrische module	electrical module	forbidden
koppelmechanisme	coupling mechanism		see claim 4
```

**A Supervertaler glossary file** – the tab-separated format older versions of Supervertaler for memoQ used, and still what Export… writes when you ask for it. No header row; instead a `#` line naming the glossary and a `#!` line declaring its languages, then `source`, `target` and an optional third cell reading `forbidden`.

```
# Client (case) v3
#! source=dut-NL target=eng-GB
elektrische module	electric module
elektrische module	electrical module	forbidden
```

A file with neither a header row nor a `#!` line is taken to run the termbase's own way round, and Add to… says so before writing.

### Direction

A termbase is stored one way round – Dutch → English, say – and so is a file. When Add to… finds the file runs the other way from the termbase, each pair is turned as it is written, and the report afterwards says so. Import… takes the file's own direction for the new termbase, shown for correction before anything is written.

### Duplicates

A pair the termbase already holds is skipped – matched without regard to case, and either way round, so *method → werkwijze* is the same pair as *werkwijze → method*. The report says how many were skipped. This is the same rule Supervertaler for Trados applies to its own import, so the same file through either product leaves the same termbase, and re-importing a file is always safe.

### What Export… writes

Two shapes, chosen in the save dialog:

- **Supervertaler glossary (.txt)** – the `#`-header format above. Re-imports into Supervertaler for memoQ exactly.
- **Tab-separated with a header row (.tsv)** – the first shape above, for a spreadsheet or for Supervertaler for Trados, whose importer expects a header row and does not skip `#` lines.

Every row is exported, notes included. A term marked non-translatable in another product is exported too; re-imported, it is simply a term whose translation is itself.

### From a prompt

A prompt drafted by AutoPrompt ends in a locked-terms table. **memoQ → Termbase from this prompt's terms…** turns that table into a termbase directly, with no file in between. See [the prompt editor](/memoq/prompt-editor/#termbase-from-this-prompts-terms).

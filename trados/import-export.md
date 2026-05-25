---
title: "Import/Export"
---

The **Import/Export** tab in the Supervertaler panel exports the active Trados document's segments to a proofreader-friendly file (Word DOCX, Markdown, or HTML), then re-imports the proofreader's edits back into Trados with a confirmation diff.

![The Import/Export tab in the Supervertaler panel, showing format and layout pickers, the multi-file file list with per-file segment counts, output mode radios, and the Recent exports list.](/.gitbook/assets/Supervertaler-for-Trados-Import-Export.png)

This is the workflow you'd use for:

* **External review** — send a bilingual DOCX to a colleague who doesn't have Trados, get it back with edits, apply.
* **Quick AI proofreading via web LLM** — copy the bilingual text into ChatGPT/Claude/Gemini, paste the corrected version back, re-import.
* **Multi-file project review** — export every file in a merged project into one combined DOCX with section breaks between each source file.

## Formats

| Format | When to use |
|---|---|
| **Word document (.docx)** | The default. A round-trippable bilingual table the proofreader edits in Word. |
| **Markdown (.md)** | Same data in plain-text Markdown — friendly for diffing, version control, or piping into an LLM. |
| **HTML (.html)** | Client-facing read-only report. Cannot be re-imported. |

## Layouts

| Layout | Shape |
|---|---|
| **Supervertaler Bilingual Table** (default) | 5-column table — `#`, source, target, status, notes. Identical to the Workbench's bilingual-table export, so files can move between both products. |
| **Stacked source-on-top** | Source paragraph, target paragraph, segment-by-segment. Easier to read for proofreaders skimming long paragraphs. |
| **Stacked target-on-top** | Same as above with source and target swapped. |
| **Bracketed `[SEGMENT NNNN]`** (Markdown only) | AI-friendly compact format that matches the Supervertaler Workbench's "AI-readable" export style. One block per segment with 2-letter ISO language codes labelling each line — some LLMs handle this more reliably than a markdown table. |

All four layouts are **re-importable**: the Bilingual Table uses the `#` column for anchors, the stacked layouts use `## Segment N` headings, and the bracketed layout uses the `[SEGMENT NNNN]` heading. DOCX and HTML exports fall back to *Stacked source-on-top* when the bracketed layout is selected (it only makes sense as plain text).

The bracketed layout looks like this:

```
[SEGMENT 0001]
EN: <b>MASHUP APPLICATION PROCESSING SYSTEM</b>
NL: <b>MASHUP-APPLICATIEVERWERKINGSSYSTEEM</b>

[SEGMENT 0002]
EN: <b>FIELD OF THE INVENTION</b>
NL: <b>GEBIED VAN DE UITVINDING</b>
```

## Inline formatting markers

Source and target cells use semantic placeholders for inline formatting so the proofreader can move them around without breaking Trados:

* `<b>...</b>` — bold pair
* `<i>...</i>` — italic pair
* `<u>...</u>` — underline pair
* `<bi>...</bi>` — bold + italic pair
* `<t1>...</t1>`, `<t2/>`, … — numbered placeholders for everything else (field codes, page numbers, custom format pairs)

In the DOCX, the markers render in red and the text between a semantic pair is shown in matching bold / italic / underline so the proofreader can see what the formatting will look like.

**Round-trip rules:**

* Semantic markers (`<b>` / `<i>` / `<u>` / `<bi>`) can be freely **added, removed, or reordered** in the target — they only affect cosmetic rendering and don't drive Trados QA.
* Numbered structural markers (`<t1>`, `<t2/>`, …) **must round-trip exactly**. Adding a `<t1>` the source doesn't have, or dropping one the source requires, would break the Trados file. The importer counts numbered markers on both sides and skips any segment whose count has changed (with a per-segment log entry).

The **"Refuse to apply edits that drop source-required tags"** checkbox enables this strict check. Leave it on unless you know what you're doing.

## Multi-file projects

When the active Trados editor view contains more than one file merged (common when the Trados project was prepared with file merging), the tab grows extra controls:

### Files to export

A checkbox list of every file in the active document, each with its segment count. Quick-select buttons:

* **Active only** — checks only the file your cursor is currently in
* **All** — checks every file
* **None** — unchecks every file (Segments: 0)

The **Segments: N** label tracks the current selection live.

### Output mode

* **Combine into one DOCX** (default) — produces a single bilingual file containing all selected files joined together. The table grows a 6th **File** column, and a yellow-highlighted "📄 File: `<name>`" section-break row appears between each file's segments so the proofreader can see file boundaries at a glance.
* **Separate DOCX per file** — asks for a folder and writes one bilingual file per selected source file.

Single-file documents see no change — the file list, output radio, and per-file UI are all hidden.

**Markdown exports get the same multi-file affordance** in both layouts:

* **Table layout**: 6-column table (`#`, source, target, **File**, status, notes) with a section-break row (`| | **📄 File: <name>** | | | | |`) prefacing each new file's segments.
* **Stacked layouts**: a `## 📄 File: <name>` heading appears before the first segment of each new file.

Re-import auto-detects whether the Markdown table is 5- or 6-column and parses accordingly.

## Locked segments

Trados segments can be **locked** (read-only in the editor) independently of their confirmation level — so a segment can be both `ApprovedTranslation` and locked, or `Draft` and locked. On large projects with a lot of locked-approved content, sending those segments to a proofreader is usually noise: any edits they make there can't be written back to Trados anyway.

A dedicated checkbox controls how the export handles them:

> **Include locked segments (🔒 marked in Status column)** — default ON.

* **ON (default)** — locked segments are exported alongside everything else, and every locked row gets a **🔒** prefix in the Status column (e.g. `🔒 ApprovedTranslation`). The proofreader can see at a glance which rows aren't editable round-trippable, and the re-import will refuse to overwrite them.
* **OFF** — locked segments are skipped entirely. The exported file only contains rows that are actually still editable. Useful on multi-thousand-segment projects where the bulk of the work is already locked.

The checkbox lives right under the **"Refuse to apply edits that drop source-required tags"** option on the tab.

**On re-import**, locked segments are honoured regardless of the export-side setting: edits made to a locked row are reported as a *locked-segment* item in the re-import summary's "other issues" count, and **not** written back to Trados. To genuinely change a locked segment, unlock it in Trados first, then re-import.

The locked flag also lives in the sidecar manifest (`is_locked: true` / `false` per segment) so the source of truth for which segments were locked at export time is preserved.

## Filtering by confirmation status

Just below the locked-segments option is a **Statuses to include in export** group of six checkboxes — one per Trados confirmation level:

* **Unspecified** — not yet translated (the initial state of a fresh segment)
* **Draft** — in progress
* **Translated** — confirmed by the translator
* **Approved (translation)** — first-pass approval
* **Approved (sign-off)** — final approval
* **Rejected** — marked for rework

All six are checked by default — no filter, every segment is included. Untick any subset to narrow the export to just those statuses. Common use-cases:

* **Tick only Translated** — send a draft pass to a proofreader.
* **Tick only Approved (translation)** — send near-final material out for a sign-off review.
* **Untick Approved (sign-off)** — exclude locked-down rows the client has already signed off on, so the proofreader only sees what's still in play.
* **Tick only Draft + Unspecified** — generate a worklist of what's still unfinished.

This filter composes orthogonally with the **Include locked segments** option and the multi-file **Files to export** list — every segment must pass all three filters to make it into the bilingual file.

## Re-import workflow

Click **📥 Re-import…**, pick the round-tripped file. Supervertaler:

1. Loads the file's sidecar manifest (the `.svexport.json` written alongside the export).
2. For each row in the file, looks up the matching segment in Trados via the manifest's `(ParagraphUnitId, SegmentId)` mapping.
3. Compares the file's target text against the current Trados target — same serialisation pipeline on both sides, so only real edits register as changes.
4. Counts up: **changes to apply**, **unchanged**, **tag-mismatch** (will be skipped under strict mode), and **other issues** (segment missing, **locked**, source text was tampered with).
5. Shows you a summary dialog with **OK** / **Cancel**.

Click **OK** and Supervertaler writes the accepted changes back via the same code path the batch AI translator uses — confirmation level is preserved, and **locked segments are skipped automatically** (the writeback queries `IsLocked` on every segment, so a lock toggled in Trados between export and re-import is also respected).

## Recent exports

At the bottom of the tab, a list tracks every export from this session with:

* **Open file** — opens the bilingual file in its default app
* **Open folder** — opens the containing folder
* **Re-import this** — same as the main Re-import button, pre-pointed at this file

## Sidecar manifest

Every export writes a small `.svexport.json` file alongside the bilingual file. It contains:

* Project name, source filename, language pair, export timestamp, tool version
* Per-segment `(number → ParagraphUnitId / SegmentId)` mapping
* A SHA-256 prefix of the source text for tamper detection
* For multi-file exports: per-segment source file id + name
* Per-segment `is_locked: true | false` flag (snapshot at export time)

The manifest is what lets re-import find the exact Trados segments even if the proofreader accidentally reorders rows. If the manifest goes missing, re-import falls back to current-document mapping (which loses source-tamper protection but still works).

## See Also

* [Batch Operations](batch-operations.md) — for AI-driven proofreading directly in Trados
* [AI Proofreader](ai-proofreader.md) — in-Trados proofreading mode

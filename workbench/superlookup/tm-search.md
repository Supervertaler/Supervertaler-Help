---
title: "TM Search (Concordance)"
---

SuperLookup’s **TMs** tab lets you do fast concordance searches in your Translation Memories ("find where I translated this before").

## Open it

- **In Supervertaler:** press `Ctrl+K` (opens SuperLookup with the current selection, if any).
- **From any application:** press `Ctrl+Alt+L` – a true system-wide hotkey (registered natively on Windows; no AutoHotkey required).

## How to search

1. Type (or paste) text into the search box.
2. Press `Enter` (or click **🔍 Search**).
3. Optional filter: **From / To** limits the search to a language pair (leave as **Any** to use all languages). **↔** swaps the two.

SuperLookup finds the TM entries that contain your search text, in the source or the target, and highlights it in the results.

## Views

At the top of the **📖 TMs** tab you can switch between:

- **Horizontal (Table):** Source and Target side by side, plus the TM each hit came from. Click a column header to sort.
- **Vertical (List):** stacked Source/Target entries (classic concordance layout).

### Text size

The **Text size** box next to the view switch makes the results larger or smaller (7 to 24 pt), without a trip to Settings. It applies to both views at once, the table rows grow to fit, and the size is remembered. Until you change it, the results keep their usual size.

## Actions

- **Double-click** a result to copy the target text.
- **📋 Copy Target** copies the selected target.
- **📥 Insert Target** copies the target and prompts you to paste with `Ctrl+V` in your active application.
- **💾 Export Results…** saves the hits – see below.

## Exporting the results

**💾 Export Results…** saves every hit for the current search, with its source, target and the TM it came from, as an Excel workbook (`.xlsx`) or a CSV file. This is handy for documenting inconsistencies in a client's TM, or for keeping a cross-TM overview of how a term has been translated.

- The rows are written in the order the table shows them, so sort by a column first if you want the file sorted.
- The Excel workbook also has a small **Search** sheet with the search term, the number of hits and the time of the export. TM text that starts with `=` stays text rather than turning into a formula.
- The CSV file is UTF-8 with a byte-order mark, so Excel opens accented letters correctly.

## TM selection

SuperLookup searches every TM that has its **🔍 SuperLookup** box ticked on the main **💾 TMs** tab. New TMs are included by default. This is independent of the **Read** box, so a TM can stay out of your project's matches and still be searched here.

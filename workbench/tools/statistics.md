---
title: "Statistics (Analyse Against TM)"
---

The **Statistics** tool analyses the document you have open against one or more of your translation memories and produces a match breakdown — the same kind of report you get from the "Analyze Files" step in Trados Studio or memoQ. It tells you, before you start, how much of the job is already covered by your TMs and how much is genuinely new, so you can scope the work and quote accurately.

## Where to find it

- Open the **Tools menu** → **📊 Statistics (Analyse Against TM)…**

You need a project open with segments. Press **F1** (or the **?** in the top-right of the dialog) to return to this page at any time.

## How to use it

1. Tick one or more translation memories to analyse against. The TMs already activated for the current project are ticked for you.
   - **Leave every TM unticked** to get a plain word count plus internal repetitions only (no TM lookup).
2. Choose a **Matching depth** (see below).
3. Click **Analyse**. The analysis runs in the background — you can cancel it at any time. Results appear per TM as each one finishes.
4. Optionally click **Export…** to save the report as **HTML**, **Excel (.xlsx)**, or **CSV**.

## Matching depth

The fuzzy-match pass is the slow part on a large TM, so you can trade thoroughness for speed:

| Depth | What it does |
| --- | --- |
| **Standard** | Exact matches plus fuzzy matches down to 75%. The default — fast and covers almost all reusable material. |
| **Thorough** | Exact plus fuzzy down to 50%. Fills the lower fuzzy bands; a little slower. |
| **Exact matches only** | Skips the fuzzy pass entirely. Near-instant, even on a TM with hundreds of thousands of entries. |

Behind the scenes the fuzzy search uses the TM's full-text index to look only at the most relevant candidates (no sub-segment/fragment search), which is conceptually the same as Trados Studio's "Optimized Performance" option.

## What the match types mean

| Type | Meaning |
| --- | --- |
| **Repetitions** | Source text that repeats earlier in the document. The first occurrence is counted under a match band; the repeats land here (translate once, reuse). |
| **101% (Context Match)** | An exact match whose surrounding context also matches the TM — the safest reuse, normally needs no editing. |
| **100%** | An exact match of the source text in the TM (context not checked). |
| **95%–99%** | Very high fuzzy match — usually a tiny edit. |
| **85%–94%** | High fuzzy match — minor editing expected. |
| **75%–84%** | Medium fuzzy match — noticeable editing expected. |
| **50%–74%** | Low fuzzy match — often faster to retranslate than to fix. |
| **No match** | No usable TM match — translate from scratch. |

Each row reports the number of **segments**, **words**, **characters** (tags excluded), **tags**, and the **percentage** of total words. The exported report includes this legend and the project name.

## Related

- [Translation memory](../translation-memory/basics.md)
- [Fuzzy matching](../translation-memory/fuzzy-matching.md)
- [Managing TMs](../translation-memory/managing-tms.md)

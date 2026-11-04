---
title: "Termbase Basics"
---

Termbases help ensure consistent terminology across your translations.

## What is a Termbase?

A termbase is a database of terms with their translations:

| Source (EN) | Target (NL) | Domain | Notes |
|-------------|-------------|--------|-------|
| software | software | IT | Don't translate |
| click | klikken | IT | Verb |
| machine learning | machinaal leren | AI | Official term |

## Why Use Termbases?

1. **Consistency**: Same term = same translation every time
2. **Efficiency**: Don't look up the same term twice
3. **Quality**: Use approved terminology
4. **Client requirements**: Follow style guides

## Termbase Features in Supervertaler

### Automatic Highlighting

Terms from termbases with **Read** ticked are highlighted in the source text:
- Semibold green text by default (a pastel green background or a dotted underline are the alternatives)
- Hover to see the translation
- Terms from the project termbase are a darker green than those from background termbases
- Forbidden terms are marked differently (dark red text in the default style)

### Multiple Termbases

Maintain separate termbases for:
- Different clients
- Different domains (legal, medical, IT)
- Different projects

### Project and Background Termbases

Each project has one **Project termbase** – the highest-priority one, marked **📌 Project** and shown in pink in the Termbases tab and in TermLens. Tick the **Project** column in the **🏷️ Termbases** tab to make a termbase the project termbase. All other termbases with **Read** ticked are **Background** termbases.

The two quick-add shortcuts follow the same split: **Alt+Up** adds the selected term pair to the project termbase, **Alt+Down** to the first background termbase with **Write** ticked.

### Forbidden and Non-Translatable Terms

- Tick **Forbidden** on a term to flag a translation that must **not** be used. Forbidden terms are marked in the grid and in TermLens, and the AI is told not to use them.
- To keep a word untranslated (a brand or product name, say), tick **Non-translatable (keep source text in target)** in the term entry editor instead, or use **🚫 Add to Non-Translatables** (**Ctrl+Alt+N**) from the right-click menu.

## Creating Your First Termbase

1. Go to the **🏷️ Termbases** tab
2. Click **+ Create New**
3. Enter a name (e.g., "Client ABC Terminology")
4. Enter the source and target language codes (e.g. `en`, `nl`)
5. Choose the scope: **Global (all projects)** or **Project-specific**
6. Click **Create**

## The Terms Window

The **🏷️ Termbases** tab lists your termbases. To see a termbase's terms, right-click it and choose **📝 Edit Terms…** (from v1.10.376). The terms open in a window of their own, titled with the termbase's name (*Terms – Client ABC Terminology*, say). If you open another termbase, its terms replace them in the same window.

In the terms window you can:

- type in **Filter terms...** to show only the terms whose source or target contains what you typed
- choose how many terms a page shows (**Show:**) and the order (**Sort:**, or click a column header), and move between pages with the arrow buttons
- double-click a cell to change the source or target term, Domain, Notes, Project or Client. The change is saved as soon as you leave the cell.
- tick **Forbidden**
- delete a term with 🗑
- add a term with **+ Add Term** (see below)

The source and target columns take up the spare width but never shrink so far that the terms can't be read. In a narrow window, the list scrolls sideways instead.

The **Synonyms** column lists each term's source and target synonyms, for example `MEKO → MEKO`. It is read-only: edit synonyms in the term entry editor (right-click the term in TermLens → **Edit Termbase Entry…**).

## Adding Terms

### Manually

1. In the **🏷️ Termbases** tab, right-click the termbase and choose **📝 Edit Terms…**
2. In the terms window, click **+ Add Term**. The **Add Term to Termbase** dialog opens.
3. Type the term in both languages. The two boxes are labelled with the termbase's own languages, for example **English (source)** and **Dutch (target)**, so each term goes in the right column even when your project translates the other way.
4. Optionally add abbreviations, synonyms, a definition, domain, notes, URL, client or project, or tick **Non-translatable** or **Forbidden term**
5. Click **💾 Save**

The terms window then opens the page that holds the new term, in your sort order, with the term selected. If the filter would hide the term, it is cleared.

- While either term is empty, **Save** asks you to type it, and the dialog stays open with what you typed. For a non-translatable term, the target is filled in from the source.
- A term that is already in the termbase (the same source and target, ignoring capitals) is not added again. Workbench tells you so and selects the existing entry.
- If the database is locked by another program, or is read-only, Workbench says so and nothing is saved.

:::note
Up to v1.10.375, **+ Add Term** saved an empty term straight away and put the cursor on an existing term, so whatever you typed next replaced that term. If you used it, sort the terms window by **Source term (A→Z)**: the empty terms are the blank rows at the top of page 1. Delete them with 🗑.
:::

### From Selection

1. Select the term in the source cell
2. Select its translation in the target cell
3. Right-click → **📖 Add to Termbase** (or press **Ctrl+Alt+T**)
4. In the dialog, choose which termbase(s) to add to and add any details

See [Creating Termbases](/workbench/termbases/creating/) for the quick-add shortcuts.

### Import from File

1. Go to the **🏷️ Termbases** tab and select the termbase to import into
2. Click **📥 Import**
3. Select a TSV file (tab-separated, with a header row – see [Importing Terms](/workbench/termbases/importing/))
4. Choose whether duplicates are skipped or updated
5. Watch the progress dialog

## Termbase Settings

### Activation

Termbases must be activated to show matches. Each termbase has a row of tick boxes in the **🏷️ Termbases** tab:
- ✅ **Read**: Terms are highlighted and shown in lookups
- ✅ **Write**: New terms can be added during translation
- ✅ **Project**: This is the project termbase (see above)
- ✅ **AI**: Matching terms are sent to the AI – see [Sending Terms to the AI](/workbench/termbases/ai-injection/)
- ✅ **🔍 SuperLookup**: The termbase is searched by SuperLookup

### Highlight Style

Choose how terms appear in the grid:
- **Semibold Text** (default): Slightly bolder text in a green tint
- **Background Color**: Pastel green background
- **Dotted Underline**: Subtle dotted line below the term, in a colour you choose

Go to **Settings → 🔍 View Settings → 🏷️ Termbase Highlight Style**.

---

## See Also

- [Creating Termbases](/workbench/termbases/creating/)
- [Importing Terms](/workbench/termbases/importing/)
- [Term Highlighting](/workbench/termbases/highlighting/)
- [Sending Terms to the AI](/workbench/termbases/ai-injection/)
- [TermLens (Inline Terminology)](/workbench/termbases/termlens/)
- [Term Extraction](/workbench/termbases/extraction/)

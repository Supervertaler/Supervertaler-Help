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

## Adding Terms

### Manually

1. Click on your termbase in the list
2. Click **+ Add Term** – a new, empty row appears in the terms table
3. Type the source term and target term
4. Optionally fill in Domain, Notes, Project and Client, or tick Forbidden

Each change is saved as soon as you leave the cell.

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
- ✅ **🎤 Voice**: The termbase's target terms help voice dictation recognise your terminology – see [Voice](/workbench/voice/overview/)
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

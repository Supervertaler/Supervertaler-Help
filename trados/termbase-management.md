---
title: "Termbase Management"
---

Supervertaler for Trados uses the same SQLite termbase format as Supervertaler Workbench. You manage your termbases through the Settings dialogue.

## Accessing termbase settings

1. Click the **gear icon** in the TermLens panel, or go to **Settings** in the plugin ribbon
2. Switch to the **TermLens** tab

## Database file

The plugin stores all termbases in a single `.db` file (SQLite database).

- Click **Browse** to select an existing database file
- Click **Create New** to create a fresh, empty database

:::note
The `.db` file uses the same Supervertaler SQLite format as the standalone application. On Windows, you can share the same termbase file between both tools by pointing them to the same data folder. On a Mac with Parallels, see the note below.
:::

## MultiTerm termbases

If your Trados project has MultiTerm termbases (`.sdltb` files) attached, they appear automatically at the bottom of the termbase list with a **[MultiTerm]** label and green background. These termbases are read-only in TermLens –to manage their terms, use Trados's built-in MultiTerm interface. See [MultiTerm Support](/trados/multiterm-support/) for full details.

## Termbase list

Once a database is loaded, the termbase list shows all Supervertaler termbases it contains, plus any detected MultiTerm termbases. Each Supervertaler termbase has three toggles:

| Toggle | Purpose |
|--------|---------|
| **Read** | Load terms from this termbase for matching in TermLens |
| **Write** | New terms added via [quick-add shortcuts](/trados/termlens/adding-terms/) go into this termbase |
| **Project** | Designate as the project termbase (terms shown in pink, prioritised in matching) |

:::caution
Only one termbase can be marked as **Project** at a time. Setting a new project termbase clears the flag from the previous one.
:::

## Creating a new termbase

1. Click **Add Termbase**
2. Enter a **name** for the termbase
3. Select the **source language** and **target language**
4. Click **OK**

The new termbase appears in the list, ready for use.

## Import from TSV

You can import terminology from a tab-separated values file:

1. Select the target termbase in the list
2. Click **Import from TSV**
3. Select your `.tsv` file
4. A confirmation dialog shows the filename, row count, termbase name, and language pair -- check that you are importing into the right termbase
5. A progress bar tracks the import (useful for large termbases with thousands of terms)

**File format:**

The first row must be a header row. Recognised column headers (case-insensitive):

| Column | Required | Recognised headers |
|--------|----------|-------------------|
| **Source** | Yes | `Source`, `Source Term`, `Src`, or a language name (e.g., `English`) |
| **Target** | Yes | `Target`, `Target Term`, `Tgt`, or a language name (e.g., `Dutch`) |
| Term UUID | No | `Term UUID`, `UUID`, `Term ID`, `ID` |
| Priority | No | `Priority`, `Prio`, `Rank` |
| Domain | No | `Domain`, `Subject`, `Field`, `Category` |
| Notes | No | `Notes`, `Note`, `Definition`, `Comment` |
| Project | No | `Project` |
| Client | No | `Client`, `Customer` |
| Forbidden | No | `Forbidden`, `Do not use` |

For terms with multiple synonyms, use pipe-delimited values: `main|synonym1|synonym2`. Forbidden synonyms are wrapped as `[!term]`.

**Example:**

```
Source	Target	Domain	Notes
database	databank|gegevensbank		
software	software		Non-translatable
user interface	gebruikersinterface|gebruikersomgeving	IT	
```

:::note
TSV files exported from Supervertaler (both the Trados plugin and Workbench) can always be reimported without any changes. Files from other tools are also supported as long as they have recognisable column headers.
:::

## Export

To export all terms from a termbase:

1. Select the termbase in the list
2. Click **Export**
3. Pick the format in the save dialog, then choose a location

Three formats, for three different purposes.

### TSV – the one that comes back unchanged

Tab-separated columns with a header row: `Term UUID`, `Source`, `Target`, `Priority`, `Domain`, `Notes`, `Project`, `Client`, `Forbidden`. Synonyms are pipe-delimited and forbidden synonyms are marked with `[!term]`. UTF-8 with BOM, for Excel compatibility.

Use it for a backup, for editing in a spreadsheet, or for moving terms between Supervertaler termbases – it reimports here with nothing lost.

:::note
Terms whose own text contains a `|` or a `\` are escaped from v18.20.177. A TSV written by an **earlier** build cannot be repaired: in it, a delimiter and a literal pipe are the same character. If you have such a file and the terms matter, re-export it.
:::

### MultiTerm XML – for Trados

The format MultiTerm and Glossary Converter import. This is how you get terms *out* of Supervertaler and into a Trados termbase:

- **For a `.sdltb`**: convert the XML with Glossary Converter, or import it in MultiTerm.
- **For a `.ttb`** (Studio 2026): in Studio's **Termbases** view, create a termbase and use **Import Terms**.

Carries source and target terms with their synonyms, plus definition, domain, notes, context, part of speech, URL, client, project and the forbidden flag – more than the TSV export, which has no column for several of those.

### TBX – for everything else

TBX-Basic (ISO 30042), the standard interchange format. MultiTerm reads it and so do most other CAT tools, so it is the better choice if your terminology has to travel beyond Trados.

:::note
**Supervertaler cannot write a `.sdltb` or `.ttb` directly.** Those are a Microsoft Access database and an undocumented SQLite format respectively; producing one means guessing at a file layout that is not published, and a termbase Studio only half-accepts would be worse than one it refuses outright. Both formats above are documented and Trados imports them, at the cost of one conversion step you perform yourself.
:::

### What a round trip keeps, and what it doesn't

Terms, synonyms and the descriptive fields survive a full circle out to a Trados termbase and back. The *structure* does not: a MultiTerm entry is concept-oriented and can hold many languages, while a Supervertaler termbase is bilingual rows – so one conversion handles one language pair, and concepts flatten to pairs with any extra terms in a language becoming synonyms.

## Import from a Trados termbase

**Import .sdltb/.ttb…** copies terms *out of* a Trados termbase and *into* a Supervertaler one. You choose the language pair, whether to create a new Supervertaler termbase or add to an existing one, and which of the Trados descriptive fields map to definition, domain, notes and so on.

The Trados termbase is only ever read, never modified.

An AI assistant connected through the [MCP server](/trados/mcp-server/) can do the same in one step with `import_project_termbase`, including a dry run that reports what would be imported before anything is written.

## Termbase Editor

For full editing capabilities, double-click a termbase in the list to open the **Termbase Editor**. From here you can:

- **Search** for terms by source or target text
- **Edit** individual term entries
- **Delete** terms
- Perform **bulk operations** (e.g. bulk delete, bulk reverse)

### Right-click menu

Right-clicking any row in the grid opens a context menu with the following actions:

- **Copy cell** – copies the content of the clicked cell to the clipboard.
- **Edit term…** – opens the full term entry editor for the clicked row.
- **Reverse source/target** – swaps the source and target for the selected rows (see below).
- **Delete term** – deletes the selected rows after confirmation.

Multi-row selection is preserved: if you select several rows first and then right-click on one of them, the selection stays intact so actions apply to all selected entries. If you right-click on a row that wasn't already selected, the selection collapses to just that row.

### Reversing source/target

If you have term entries that ended up in the wrong direction – for example, English text in the Dutch column when the termbase is declared English → Dutch – you can correct them with **Reverse source/target**:

1. Select one or more rows in the grid (Shift-click or Ctrl-click for multi-select).
2. Right-click → **Reverse source/target (N entries)**.
3. Confirm.

The operation swaps the source and target text, language tags, abbreviations, and flips the direction of every linked synonym. It runs in a single database transaction, so a partial failure leaves the termbase untouched.

This action is mostly for repairing legacy entries created or edited under v4.19.24 or earlier, when the term entry editor could write values into the wrong DB columns in projects whose direction was the inverse of the termbase's. From v4.19.25 onwards the editor guards against that, so new entries should not need this repair.

:::note
**Add and Edit dialog fields are always in termbase direction.** The dialog labels and values both reflect the termbase's declared direction – English on the left when the termbase is declared EN→NL, regardless of the current Trados project's direction. From v4.19.25 the values are guaranteed to align with the labels: the Edit dialog re-reads the entry from the database, and the Add dialog swaps the pre-fills internally when the project direction is the inverse of the termbase. Earlier versions could silently write reversed entries in inverse-direction projects – use **Reverse source/target** above to repair any pre-v4.19.25 damage.
:::

## Sharing termbases

:::tip
**Tip:** Keep the `.db` file on a network drive or cloud-synced folder (OneDrive, Dropbox, Google Drive) to share termbases across machines and with colleagues. Since both the Trados plugin and Supervertaler Workbench use the same format, everyone can work from the same terminology.
:::

:::caution
**Mac users (Parallels):** On a Mac, Supervertaler Workbench runs natively on macOS while the Trados plugin runs inside Parallels (Windows). The two products cannot share the same `.db` file directly because the Trados plugin must store its data on the Windows side (`C:\Users\...`) – not on the Mac-side shared folder (`\\Mac\Home\...`). To keep your termbases in sync, export from one side and import on the other after making changes. This is a limitation of Parallels' virtual network filesystem, not of the termbase format itself.
:::

---

## See Also

- [MultiTerm Support](/trados/multiterm-support/)
- [TermLens Settings](/trados/settings/termlens/)
- [Adding & Editing Terms](/trados/termlens/adding-terms/)
- [Data Folder](/trados/data-folder/)

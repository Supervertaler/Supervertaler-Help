---
title: "Importing Terms"
---

You can import terminology from a tab-separated text file (TSV). Excel and Google Sheets can both save a sheet in this format.

## Import steps

1. Open the **🏷️ Termbases** tab
2. Select the termbase to import into (create one first with **+ Create New** if needed)
3. Click **📥 Import** and select your `.tsv` or `.txt` file
4. Choose how duplicates are handled: **Skip duplicates (keep existing terms)** or **Update duplicates (overwrite existing terms)**
5. Click **Import** and follow the progress in the import log

## File format

- The first row is a header with the column names; the columns are separated by tabs.
- **Source Term** and **Target Term** (or simply **Source** and **Target**) are required. Two language names as headers (for example `Dutch` and `English`) also work: the first is taken as the source, the second as the target.
- Optional columns: **Domain**, **Notes**, **Project**, **Client**, **Forbidden** and **Non-translatable** (`TRUE`/`FALSE` or `1`/`0`; the Non-translatable column is read from v1.10.372).
- Separate synonyms with `|` in the source or target column: the first term is the main term, the rest become its synonyms. A synonym written as `[!…]` is imported as forbidden.

A termbase exported with **📤 Export** uses the same format, so an exported termbase can be imported again as it is. Leave **Include all metadata (project, client, forbidden)** ticked when exporting to keep the Project, Client, Forbidden and Non-translatable columns.

:::tip
To back up all your termbases (and TMs) in one go, use **File → Export → 📦 Back Up All TMs & Termbases…** (from v1.10.372). It writes one TSV file per termbase, ready to import again.
:::

## Tips

- Clean your source file (consistent columns) before importing.
- Import before batch translation so AI can follow your terminology.

:::note
If you don’t see terms highlighting in the grid, ensure the termbase is enabled (Read/active) in the **Termbases** tab.
:::

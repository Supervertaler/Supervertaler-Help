---
title: "Importing TMX Files"
---

TMX is the common exchange format for translation memories.

## Import steps

1. Open the **💾 TMs** tab.
2. Click **📥 Import TMX** and select your `.tmx` file.
3. Choose **Create new TM from this TMX**, or **Add to existing TM** and pick the
   TM from the list. Click **Import**.
4. For a new TM, enter a name (see [TM names](#tm-names) below). The
   **Select Language Pair** dialog then opens: check the source and target
   language (see [Language direction](#language-direction) below) and click
   **OK**. When you add to an existing TM, its own language pair is used.

:::note
Import your TM(s) before batch translation to maximize reuse. A new TM only
gives matches in a project once its **Read** box is ticked for that project –
see [Creating & Managing TMs](/workbench/translation-memory/managing-tms/).
:::

## Language direction

The **Select Language Pair** dialog lists the languages found in the TMX file.
Since v1.10.372 it pre-selects as **Source** the language the TMX file itself
declares as its source language, and says which one that is ("The file says its
source language is en-GB."). The other language is pre-selected as **Target**.

Check the pair before you click **OK**, and use **🔄 Swap** to turn it round if
needed. If the file doesn't declare a source language, the languages are offered
in alphabetical order, so look twice.

:::caution
Earlier versions always offered the alphabetically first language as the
source, so an English (en-GB) → German (de-DE) TMX was offered as German →
English. If you imported TMX files with an older version, check the
**Languages** column in the **💾 TMs** tab.
:::

When you **add to an existing TM**, the TMX languages must match the TM's
languages. If they differ only in the regional variant (for example `en-GB`
in the file, `en-US` in the TM), you're asked whether to import by matching
the base languages.

## TM names

TM names must be unique. The name box suggests the TMX file name, or a free
variant of it such as "client (2)" if that name is already taken – for example
when you import the same file a second time. If you type a name that is already
in use, Supervertaler tells you so and lets you pick another. To add the entries
to the TM that already has that name, choose **Add to existing TM** instead.

## Tips

- Import TMs before batch translation to maximize reuse.
- If matches don't show up, see
  [TM Matches Not Appearing](/workbench/troubleshooting/tm-matches/).

## Troubleshooting

### "Failed to create TM metadata"

Versions before v1.10.372 showed this bare error when you imported a TMX under a
name that was already taken. Update, or choose a different name.

The same versions could also put the imported entries into the wrong TM when the
new name differed from an existing one only in spaces, hyphens or capitals (for
example "Client TM" and "client-tm"): the new TM was created, but the entries
went into the older one. If a TM's entry count looks wrong, check both TMs.

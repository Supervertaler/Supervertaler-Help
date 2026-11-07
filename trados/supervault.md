---
title: "SuperVault"
---

SuperVault is **one translation memory for every language variant, in both directions**, built into Supervertaler for Trados. You add it to a project like any TM, and it serves every project in a language pair it holds. One Dutch–English memory serves nl-BE > en-US, nl-NL > en-GB, en-GB > nl-BE and en-US > nl-NL alike. There are no reversed copies to make and nothing to add per variant.

You fill it by importing TMX files and Studio TMs. It needs no other program.

Despite the name, SuperVault isn't encrypted or locked storage. It is your own lifetime translation memory: one ordinary database on your own PC, in your Supervertaler data folder (see [Where it lives](#where-it-lives)). Keep it safe as you would your other TMs.

*(From v18.20.206 / v19.20.206. In this first version SuperVault offers lookups and concordance search; segments you confirm in Studio are not yet stored in it.)*

## What you get

- **Matches in Translation Results**, with a match % and the differences from your segment highlighted, as for any TM.
- **Analyze and Pre-translate** count and use SuperVault matches like any TM's.
- **Concordance search** on the source and on the target, with the words you searched for highlighted. Concordance results show the text without its formatting.
- **Formatting comes along.** Where a stored unit has the same formatting as your segment, the match carries your document's own tags in the right places. When the tags can't be placed with confidence – the stored unit has a different number of tags than your segment, for example – the match comes as plain text, with your project's formatting penalty, just as a Studio TM's would.

## Your own TMs always come first

SuperVault never lowers a match from your project TMs.

This matters because of how Studio treats two TMs that disagree. When two TMs give different 100% translations for a segment, Studio marks *every* 100% match down to 99% (its **multiple translations** penalty), including the one from the TM you trust. SuperVault avoids that: its matches always rank after another TM's match of the same score.

- Where only SuperVault has the segment, its match shows as 100%.
- Where your TM has a 100% or Context Match, that match stays exactly as it was, is listed first, and is the one Pre-translate uses. SuperVault's match is listed after it.
- If SuperVault holds the very same translation, you may see it twice: once from your TM, listed first, and once from SuperVault, below it. Neither is marked down.
- If two of *your* TMs disagree, Studio penalises them as it always has.

## Setting it up

1. Open **Project Settings** (or **File > Options** for your default settings), go to **Language Pairs > All Language Pairs > Translation Memory and Automated Translation**, and click **Use > SuperVault...**.
2. Fill SuperVault: click **Import TMX...** or **Import Studio TM...** and choose one or more files. The import runs in the background, so you can click **Add** and keep working; Studio starts using the new units as soon as SuperVault has updated its search index.
3. Tick **Lookup** and **Concordance** for SuperVault in the list, as for any TM. SuperVault has no **Update** yet.

To import more later, see what SuperVault holds, or rebuild its index, select SuperVault in the list and click **Settings...**.

## Importing

| Import | What it takes |
| --- | --- |
| **Import TMX...** | Any TMX file, of any size. A unit in more than two languages gives one unit per pair of languages. Formatting tags are kept. |
| **Import Studio TM...** | A Studio file-based TM (`.sdltm`), read through Studio itself, formatting tags included. A TM with a password can't be imported: export it to TMX in Studio and import that. |
| **Import from Workbench** | Shown only if you have Supervertaler Workbench: adds the units in its memory. Workbench's database is only read, never changed. |

- **Duplicates are stored once.** A unit counts as the same when its text and formatting are the same, whatever its direction, language variants or tag numbers. Importing the same TM twice, or an en-GB > nl-NL TM after its nl-BE > en-US twin, adds nothing new; the summary after the import says how many units were added and how many were already there.
- **Left out:** units with no text once the tags are removed, units with the same language on both sides, and a known kind of broken unit from public software corpora, where a menu label ran into the next one (*AndereSearch in:" "All Categories*).
- **An import that fails or that you stop adds nothing**: the memory and the index stay as they were.
- Variants count as one language (nl-BE and nl-NL are both Dutch); different scripts don't (Chinese Simplified and Traditional, Serbian Latin and Cyrillic are kept apart).

## Where it lives

Everything is in `supervault` in your [Supervertaler data folder](data-folder.md):

| What | File |
| --- | --- |
| The memory itself | `supervault.db` |
| Its search index | the `gen-…` folder, rebuilt from the memory after every import |

The index can always be rebuilt from the memory, so it needs no backing up. Back up `supervault.db` with the rest of your data folder.

## Keeping the index healthy

SuperVault updates its index after every import. Studio keeps using the previous index while the new one is built, and switches over when it is complete. It takes about 6 minutes and 365 MB for 1.5 million units.

If the index is damaged, or was built by another version of Supervertaler, Studio shows SuperVault as unavailable, with a message; your other TMs work as usual. Click **Rebuild index** in SuperVault's settings to put it right.

## Speed

A lookup takes about 20 ms in Studio 2024 and 35 ms in Studio 2026 with 1.5 million units. Analyze and Pre-translate look up every segment this way.

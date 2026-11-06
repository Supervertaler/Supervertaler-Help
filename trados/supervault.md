---
title: "SuperVault"
---

SuperVault brings your **Supervertaler Workbench memory into Trados Studio as a translation memory**. You add it to a project like any TM, and it serves every project in a language pair your Workbench database holds: **all language variants, in both directions**. One Dutch–English memory serves nl-BE > en-US, nl-NL > en-GB, en-GB > nl-BE and en-US > nl-NL alike. There are no reversed copies to make and nothing to add per variant.

*(From v18.20.206 / v19.20.206. In this first version SuperVault offers lookups and concordance search; segments you confirm in Studio are not yet stored in it.)*

## What you get

- **Matches in Translation Results**, with a match % and the differences from your segment highlighted, as for any TM.
- **Analyze and Pre-translate** count and use SuperVault matches like any TM's.
- **Concordance search** on the source and on the target.
- **Formatting comes along.** Where a stored unit has formatting (bold, a tag pair such as `<pt x="1">…</pt>`, a memoQ `[1}…{1]` pair), the match carries your document's own tags in the right places. When the tags can't be placed with confidence – the stored unit has a different number of tags than your segment, for example – the match comes as plain text, with your project's formatting penalty, just as a Studio TM's would.

## Your own TMs always come first

SuperVault never lowers a match from your project TMs.

This matters because of how Studio treats two TMs that disagree. When two TMs give different 100% translations for a segment, Studio marks *every* 100% match down to 99% (its **multiple translations** penalty), including the one from the TM you trust. SuperVault avoids that: its matches always rank after another TM's match of the same score.

- Where only SuperVault has the segment, its match shows as 100%.
- Where your TM has a 100% or Context Match, that match stays exactly as it was, is listed first, and is the one Pre-translate uses. SuperVault's match is listed after it.
- If SuperVault holds the very same translation, tags included, Studio shows it once, as your TM's match.
- If two of *your* TMs disagree, Studio penalises them as it always has.

## Setting it up

1. Open **Project Settings** (or **File > Options** for your default settings), go to **Language Pairs > All Language Pairs > Translation Memory and Automated Translation**, and click **Use > SuperVault...**.
2. The first time, click **Build index**. SuperVault reads your Workbench database and builds a search index of its own. This runs in the background, so you can click **Add** and keep working; Studio starts using SuperVault as soon as the index is ready. It takes about 6 minutes for 1.5 million units.
3. Tick **Lookup** and **Concordance** for SuperVault in the list, as for any TM. SuperVault has no **Update** yet.

To see the index, rebuild it or stop a build, select SuperVault in the list and click **Settings...**.

## Where it lives

| What | Where |
| --- | --- |
| Your Workbench database (read, never changed) | `resources\supervertaler.db` in your [Supervertaler data folder](data-folder.md) |
| SuperVault's index | `supervault` in your Supervertaler data folder |

The index can always be built again from the database: deleting the `supervault` folder loses nothing. It takes about 365 MB per 1.5 million units.

## Keeping it up to date

Units you add in Workbench reach SuperVault when you click **Rebuild index** in SuperVault's settings. Studio keeps using the old index while the new one is built, and switches over when it is complete. If a build fails or you stop it, the old index stays in use, unchanged.

If the index is damaged, or was built by another version of Supervertaler, Studio shows SuperVault as unavailable, with a message; your other TMs work as usual. Click **Rebuild index** to put it right.

## Which units SuperVault serves

- **Language pairs:** every pair of two different languages your Workbench database holds. Variants count as one language (nl-BE and nl-NL are both Dutch); different scripts don't (Chinese Simplified and Traditional, Serbian Latin and Cyrillic are kept apart).
- **Left out:** units with no text once the tags are removed, and a known kind of broken unit from public software corpora, where a menu label ran into the next one (*AndereSearch in:" "All Categories*).

## Speed

A lookup takes about 35 ms with 1.5 million units. Analyze and Pre-translate look up every segment this way, so they take about 35 ms longer per segment with SuperVault added.

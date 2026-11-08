---
title: "SuperVault"
---

SuperVault is **one translation memory for every language variant, in both directions**, built into Supervertaler for Trados. You add it to a project like any TM. One Dutch–English memory serves nl-BE > en-US, nl-NL > en-GB, en-GB > nl-BE and en-US > nl-NL alike. There are no reversed copies to make and nothing to add per variant.

You fill it by importing TMX files and Studio TMs, and **it learns from the segments you confirm**. It needs no other program.

Supervertaler remembers in two ways: **SuperMemory** holds what you've *learned* – your notes for the AI about a client or subject – and **SuperVault** holds what you've *translated*: every segment pair from your TMs. See [SuperMemory](/trados/ai-assistant/super-memory/) for the notes.

Despite the name, SuperVault isn't encrypted or locked storage. It is your own lifetime translation memory: one ordinary database on your own PC, in your Supervertaler data folder (see [Where it lives](#where-it-lives)). Keep it safe as you would your other TMs.

*(From v18.20.206 / v19.20.206.)*

## What you get

- **Matches in Translation Results**, with a match % and the differences from your segment highlighted, as for any TM.
- **Analyze and Pre-translate** count and use SuperVault matches like any TM's.
- **Concordance search** on the source and on the target, with the words you searched for highlighted. Concordance results show the text without its formatting.
- **Formatting comes along.** Where a stored unit has the same formatting as your segment, the match carries your document's own tags in the right places. When the tags can't be placed with confidence – the stored unit has a different number of tags than your segment, for example – the match comes as plain text, with your project's formatting penalty, just as a Studio TM's would.
- **It learns as you work.** With its **Update** box ticked, every segment you confirm goes into SuperVault (see [Learning as you work](#learning-as-you-work)).

## Your own TMs always come first

SuperVault never lowers a match from your project TMs.

This matters because of how Studio treats two TMs that disagree. When two TMs give different 100% translations for a segment, Studio marks *every* 100% match down to 99% (its **multiple translations** penalty), including the one from the TM you trust. SuperVault avoids that: its matches always rank after another TM's match of the same score.

- Where only SuperVault has the segment, its match shows as 100%.
- Where your TM has a 100% or Context Match, that match stays exactly as it was, is listed first, and is the one Pre-translate uses. SuperVault's match is listed after it.
- If SuperVault holds the very same translation, you may see it twice: once from your TM, listed first, and once from SuperVault, below it. Neither is marked down.
- If two of *your* TMs disagree, Studio penalises them as it always has.
- If SuperVault itself holds two different translations of a sentence – one you imported and one you confirmed later, say – Studio shows both at 99%, as it would for any TM with two translations.

## Setting it up

1. Open **Project Settings** (or **File > Options** for your default settings), go to **Language Pairs > All Language Pairs > Translation Memory and Automated Translation**, and click **Use > SuperVault...**. You can add it to a project in any language pair, also one it holds nothing for yet.
2. Fill SuperVault: click **Import TMX...**, **Import Studio TM...** or **Import from Workbench** (see [Importing](#importing)). The import runs in the background, so you can click **Add** and keep working; Studio starts using the new units as soon as SuperVault has updated its search index. You can also start empty and let SuperVault fill up as you work.
3. Tick **Lookup** and **Concordance** for SuperVault in the list, as for any TM, and tick **Update** if you want it to learn from the segments you confirm. When you add SuperVault, Studio ticks Update for you only if no other TM in the project has Update ticked.

To import more later, see what SuperVault holds, or rebuild its index, select SuperVault in the list and click **Settings...**.

## Learning as you work

With SuperVault's **Update** box ticked in the project's TM settings, every segment you confirm is added to SuperVault, and so is a batch **Update Main Translation Memories**. Your project TMs are updated as usual: SuperVault learns alongside them.

- **Found at once.** A segment you confirm is offered straight away when the same sentence comes up again in that Studio. Its fuzzy matches follow a second or two later, and another Studio finds it within a few seconds. Nothing is rebuilt.
- **Stored like an import:** once per language pair, whatever its direction and variants, with its formatting.
- **Correcting replaces.** Change a segment's translation and confirm it again, and SuperVault replaces what it learned from that segment rather than adding a second translation.
- **Imported units are never changed.** If you confirm a different translation of a sentence you imported, SuperVault keeps both, as a TM would.
- **Confirming is never slowed down.** SuperVault does its work in the background. If it can't store something – a full disk, a drive that isn't there – its window says so and it tries again; your confirmation in Studio is unaffected.
- **Several Studios at once.** You can run Studio 2022, 2024 and 2026 side by side on one SuperVault. While one Studio imports or rebuilds the index, segments confirmed in the others wait safely and are stored as soon as it has finished, also if you close that Studio in the meantime.

SuperVault's window (**Settings...**) shows what happened since Studio started, for example *"Since Studio started, 12 confirmed: 9 added, 2 replaced, 1 already in SuperVault"*, and how many segments are waiting, if any.

Install the same version in every Studio you use with SuperVault: an older version still finds the units, but doesn't see newly learned ones until its index is rebuilt.

## Importing

| Import | What it takes |
| --- | --- |
| **Import TMX...** | Any TMX file, of any size. A unit in more than two languages gives one unit per pair of languages. Formatting tags are kept. |
| **Import Studio TM...** | A Studio file-based TM (`.sdltm`), read through Studio itself, formatting tags included. A TM with a password can't be imported: export it to TMX in Studio and import that. |
| **Import from Workbench** | Shown only if you have Supervertaler Workbench. First lists Workbench's TMs, each with its language pairs and number of units: tick the ones you want (**Select all** / **Select none**) and click **Import**. SuperVault remembers the TMs you left unticked; a TM added to Workbench later starts ticked. Workbench's database is only read, never changed. |

- **Duplicates are stored once.** A unit counts as the same when its text and formatting are the same, whatever its direction, language variants or tag numbers. Importing the same TM twice, or an en-GB > nl-NL TM after its nl-BE > en-US twin, adds nothing new; the summary after the import says how many units were added and how many were already there.
- **Left out:** units with no text once the tags are removed, units with the same language on both sides, and a known kind of broken unit from public software corpora, where a menu label ran into the next one (*AndereSearch in:" "All Categories*).
- **An import that fails or that you stop adds nothing**: the memory and the index stay as they were.
- Variants count as one language (nl-BE and nl-NL are both Dutch); different scripts don't (Chinese Simplified and Traditional, Serbian Latin and Cyrillic are kept apart).

## What SuperVault keeps

For each unit, SuperVault keeps the source and target text with their formatting, the language pair it first came with (nl-BE > en-US, say), where it came from (the TMX or TM file's name, "workbench", or "studio" for a segment you confirmed) and when it went into SuperVault.

It does **not** keep the rest of a unit's information: TMX properties and notes, a Studio TM's fields (client, subject, project and so on), who created or changed a unit and when, usage counts, or Workbench's project and context. So SuperVault matches can't be filtered by client or subject, and client details stay out of SuperVault. Because a unit is stored once, a sentence that is in several TMs keeps the origin of the first one imported.

## Where it lives

Everything is in `supervault` in your [Supervertaler data folder](data-folder.md):

| What | File |
| --- | --- |
| The memory itself | `supervault.db` |
| Its search index | the `gen-…` folder |
| Confirmed segments waiting to be stored | `inbox.db` (usually empty) |
| The Workbench TMs you left unticked | `workbench-unticked.txt` |

The index can always be rebuilt from the memory, so it needs no backing up. Back up `supervault.db` with the rest of your data folder.

## Keeping the index healthy

Segments you confirm and small imports are added to the index in place, in seconds. A large import – more than a quarter of what SuperVault already holds – rebuilds the whole index instead: about 6 minutes and 365 MB for 1.5 million units. Studio keeps using the previous index while the new one is built, and switches over when it is complete.

If the index is damaged, or was built by another version of Supervertaler, Studio shows SuperVault as unavailable, with a message; your other TMs work as usual. Click **Rebuild index** in SuperVault's settings to put it right. An empty SuperVault is not an error: it gives no matches and fills up as you import or confirm.

## Speed

A lookup takes about 20 ms in Studio 2024 and 35 ms in Studio 2026 with 1.5 million units. Analyze and Pre-translate look up every segment this way. Confirming a segment adds no noticeable delay, and a batch of 20,000 segments is stored in about 20 seconds.

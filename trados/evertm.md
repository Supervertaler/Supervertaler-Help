---
title: "EverTM"
---

:::caution[Not released yet – coming in 18.20.206]
EverTM is not in any released version of Supervertaler for Trados yet. It comes with version 18.20.206 / 19.20.206. This page describes how it will work, so you can see what is coming; the details may still change before it ships.
:::

EverTM is **one translation memory for every language variant, in both directions**, built into Supervertaler for Trados. You add it to a project like any TM. One Dutch–English memory serves nl-BE > en-US, nl-NL > en-GB, en-GB > nl-BE and en-US > nl-NL alike. There are no reversed copies to make and nothing to add per variant. (Each translation unit still remembers its own variant; see [Keeping language variants apart](#planned) for what is planned for those who want them kept separate.)

You fill it by importing TMX files and Studio TMs, and **it learns from the segments you confirm**. It needs no other program.

Supervertaler remembers in two ways: **SuperMemory** holds what you've *learned* – your notes for the AI about a client or subject – and **EverTM** holds what you've *translated*: every segment pair from your TMs. See [SuperMemory](/trados/ai-assistant/super-memory/) for the notes.

EverTM isn't encrypted or locked storage. It is your own lifetime translation memory: one ordinary database on your own PC, in your Supervertaler data folder (see [Where it lives](#where-it-lives)). Keep it safe as you would your other TMs.

## Why EverTM

With Studio's AnyTM, every reversed or variant copy of a TM piles up: one TM for Dutch to English, another for English to Dutch, more for each language variant. The same translations end up stored many times, in TMs you have to keep apart and keep up to date.

EverTM is one memory that serves every language variant in both directions. There are no copies. Each translation is stored once, with where it came from and when, and it serves every project in that language pair.

## What you get

- **Matches in Translation Results**, with a match % and the differences from your segment highlighted, as for any TM.
- **Analyze and Pre-translate** count and use EverTM matches like any TM's.
- **Concordance search** on the source and on the target, with the words you searched for highlighted. Concordance results show the text without its formatting.
- **Formatting comes along.** Where a stored unit has the same formatting as your segment, the match carries your document's own tags in the right places. When the tags can't be placed with confidence – the stored unit has a different number of tags than your segment, for example – the match comes as plain text, with your project's formatting penalty, just as a Studio TM's would.
- **It learns as you work.** With its **Update** box ticked, every segment you confirm goes into EverTM (see [Learning as you work](#learning-as-you-work)).

## What's coming

EverTM is meant to become the one place for everything you have ever translated: not only a memory that gives matches, but one you can sort, filter and look after. The order and the details below may still change.

### Built and being tested now

- **Your TMs' information is kept.** Each translation unit keeps its fields – Project, Client, End client, Subject, Document, Source and Note – and who created and last changed it, and when. This comes from TMX files, Studio TMs and Workbench, and Studio shows it with every EverTM match.
- **The newest translation wins.** When a sentence has been translated in more than one way, EverTM gives the newest translation (in your exact language variant first). Older translations are kept and hidden, never deleted.
- **Re-importing fills in what was missing.** Importing a TM again adds its fields and dates to the translation units EverTM already holds, without storing anything twice.
- **AI Batch Translate uses EverTM.** Its TM matches, which it sends to the AI with each segment, include EverTM's.
- **Export to TMX includes the fields, dates and users.**

### Planned

- **EverTM Matches, a pane of its own in Studio's Editor**, next to TermLens. It shows EverTM's matches with the differences highlighted, and a one-line summary under each match (client, project, date), so you can tell matches apart at a glance. Below them, the selected match's full details: every field, its dates and users, and its older translations. You can remove a wrong translation from EverTM there, with Undo and a list to restore it from. It can take the place of Studio's Translation Results for EverTM.
- **A manager for EverTM.** Browse what EverTM holds by client, end client, project, subject or where it came from, with the number of translation units in each. Export just the part you need – all patent work for one client, say – to a TMX file.
- **A profile per project.** Tell EverTM what a project is – its client and subject – and it tags the translations you confirm with them. The same profile limits EverTM's matches to work that fits: patents only, for example, or never medical texts. It applies everywhere EverTM is used – Translation Results, Analyze, Pre-translate, Batch Translate and EverTM Matches. Translation units without any information always pass, and a switch shows the matches that were left out. Projects made from the same Studio template share a profile.
- **Keeping language variants apart, if you want to.** Each translation unit remembers the language variant it came with (nl-BE, en-GB and so on), but EverTM mixes the variants when it looks for matches: one memory serves them all. That suits translators who adapt UK or US spelling at the end anyway. For those who would rather keep variants apart, as with separate Studio TMs, a **Language variants** setting will offer three choices: mix them (as now, and the default), mark matches from another variant down by a penalty you choose (an en-US match showing 98% in an en-GB project, say), or offer only matches in the project's exact variant. It can be set per project.
- **Re-tagging in bulk**, for translation units that came in without information.
- **Context matches**, where the previous segment matches too.
- **Cleaning up and editing:** finding near-duplicates, and correcting a translation unit or its information.

## Your own TMs always come first

EverTM never lowers a match from your project TMs.

This matters because of how Studio treats two TMs that disagree. When two TMs give different 100% translations for a segment, Studio marks *every* 100% match down to 99% (its **multiple translations** penalty), including the one from the TM you trust. EverTM avoids that: its matches always rank after another TM's match of the same score.

- Where only EverTM has the segment, its match shows as 100%.
- Where your TM has a 100% or Context Match, that match stays exactly as it was, is listed first, and is the one Pre-translate uses. EverTM's match is listed after it.
- If EverTM holds the very same translation, you may see it twice: once from your TM, listed first, and once from EverTM, below it. Neither is marked down.
- If two of *your* TMs disagree, Studio penalises them as it always has.
- If EverTM itself holds two different translations of a sentence – one you imported and one you confirmed later, say – Studio shows both at 99%, as it would for any TM with two translations.

## Setting it up

1. Open **Project Settings** (or **File > Options** for your default settings), go to **Language Pairs > All Language Pairs > Translation Memory and Automated Translation**, and click **Use > EverTM...**. You can add it to a project in any language pair, also one it holds nothing for yet.
2. Fill EverTM: click **Import TMX...**, **Import Studio TM...** or **Import from Workbench** (see [Importing](#importing)). The import runs in the background, so you can click **Add** and keep working; Studio starts using the new units as soon as EverTM has updated its search index. You can also start empty and let EverTM fill up as you work.
3. Tick **Lookup** and **Concordance** for EverTM in the list, as for any TM, and tick **Update** if you want it to learn from the segments you confirm. When you add EverTM, Studio ticks Update for you only if no other TM in the project has Update ticked.

To import more later, see what EverTM holds, or rebuild its index, select EverTM in the list and click **Settings...**.

## Learning as you work

With EverTM's **Update** box ticked in the project's TM settings, every segment you confirm is added to EverTM, and so is a batch **Update Main Translation Memories**. Your project TMs are updated as usual: EverTM learns alongside them.

- **Found at once.** A segment you confirm is offered straight away when the same sentence comes up again in that Studio. Its fuzzy matches follow a second or two later, and another Studio finds it within a few seconds. Nothing is rebuilt.
- **Stored like an import:** once per language pair, whatever its direction and variants, with its formatting.
- **Correcting replaces.** Change a segment's translation and confirm it again, and EverTM replaces what it learned from that segment rather than adding a second translation.
- **Imported units are never changed.** If you confirm a different translation of a sentence you imported, EverTM keeps both, as a TM would.
- **Confirming is never slowed down.** EverTM does its work in the background. If it can't store something – a full disk, a drive that isn't there – its window says so and it tries again; your confirmation in Studio is unaffected.
- **Several Studios at once.** You can run Studio 2022, 2024 and 2026 side by side on one EverTM. While one Studio imports or rebuilds the index, segments confirmed in the others wait safely and are stored as soon as it has finished, also if you close that Studio in the meantime.

EverTM's window (**Settings...**) shows what happened since Studio started, for example *"Since Studio started, 12 confirmed: 9 added, 2 replaced, 1 already in EverTM"*, and how many segments are waiting, if any.

Install the same version in every Studio you use with EverTM: an older version still finds the units, but doesn't see newly learned ones until its index is rebuilt.

## Importing

| Import | What it takes |
| --- | --- |
| **Import TMX...** | Any TMX file, of any size. A unit in more than two languages gives one unit per pair of languages. Formatting tags are kept. |
| **Import Studio TM...** | A Studio file-based TM (`.sdltm`), read through Studio itself, formatting tags included. A TM with a password can't be imported: export it to TMX in Studio and import that. |
| **Import from Workbench** | Shown only if you have Supervertaler Workbench. First lists Workbench's TMs, each with its language pairs and number of units: tick the ones you want (**Select all** / **Select none**) and click **Import**. EverTM remembers the TMs you left unticked; a TM added to Workbench later starts ticked. Workbench's database is only read, never changed. |

- **Duplicates are stored once.** A unit counts as the same when its text and formatting are the same, whatever its direction, language variants or tag numbers. Importing the same TM twice, or an en-GB > nl-NL TM after its nl-BE > en-US twin, adds nothing new; the summary after the import says how many units were added and how many were already there.
- **Left out:** units with no text once the tags are removed, units with the same language on both sides, and a known kind of broken unit from public software corpora, where a menu label ran into the next one (*AndereSearch in:" "All Categories*).
- **An import that fails or that you stop adds nothing**: the memory and the index stay as they were.
- Variants count as one language (nl-BE and nl-NL are both Dutch); different scripts don't (Chinese Simplified and Traditional, Serbian Latin and Cyrillic are kept apart).

## Exporting

To take your memory elsewhere – another CAT tool, a colleague, a backup you can read – select EverTM in the project's TM list, click **Settings...** and then **Export TMX...**.

- **Choose what to export.** The window lists what EverTM holds by where it came from (each TMX or TM file, "workbench", "studio" for segments you confirmed), with the number of units. Choose a language pair or **All language pairs**, tick the sources you want (**Select all** / **Select none**), click **Export...** and pick where to save the TMX file.
- **What the file holds.** A standard TMX 1.4 file. Each unit is written in the direction and language variants it was first stored with, with its formatting tags, the date it went into EverTM and where it came from.
- **Keep working.** The export runs in the background; you can go on translating, in that Studio and in others. About a million units take some 25 seconds.
- **Stop leaves nothing.** Click **Stop** and the half-written file is removed: you never end up with a partial TMX.

## What EverTM keeps

For each unit, EverTM keeps the source and target text with their formatting, the language pair it first came with (nl-BE > en-US, say), where it came from (the TMX or TM file's name, "workbench", or "studio" for a segment you confirmed) and when it went into EverTM.

It does **not** keep the rest of a unit's information: TMX properties and notes, a Studio TM's fields (client, subject, project and so on), who created or changed a unit and when, usage counts, or Workbench's project and context. So EverTM matches can't be filtered by client or subject, and client details stay out of EverTM. Because a unit is stored once, a sentence that is in several TMs keeps the origin of the first one imported.

This changes with the next step, now being tested: EverTM will keep each unit's fields, and who created and changed it, and when. See [What's coming](#whats-coming).

## Where it lives

Everything is in `evertm` in your [Supervertaler data folder](/trados/data-folder/):

| What | File |
| --- | --- |
| The memory itself | `evertm.db` |
| Its search index | the `gen-…` folder |
| Confirmed segments waiting to be stored | `inbox.db` (usually empty) |
| The Workbench TMs you left unticked | `workbench-unticked.txt` |

The index can always be rebuilt from the memory, so it needs no backing up. Back up `evertm.db` with the rest of your data folder.

EverTM was called SuperVault in early test builds. If you used one, the first Studio you start with this version renames the `supervault` folder to `evertm` for you, and projects that had SuperVault keep working. Install the new version in every Studio you use before you start any of them.

## Keeping the index healthy

Segments you confirm and small imports are added to the index in place, in seconds. A large import – more than a quarter of what EverTM already holds – rebuilds the whole index instead: about 6 minutes and 365 MB for 1.5 million units. Studio keeps using the previous index while the new one is built, and switches over when it is complete.

If the index is damaged, or was built by another version of Supervertaler, Studio shows EverTM as unavailable, with a message; your other TMs work as usual. Click **Rebuild index** in EverTM's settings to put it right. An empty EverTM is not an error: it gives no matches and fills up as you import or confirm.

## Speed

A lookup takes about 20 ms in Studio 2024 and 35 ms in Studio 2026 with 1.5 million units. Analyze and Pre-translate look up every segment this way. Confirming a segment adds no noticeable delay, and a batch of 20,000 segments is stored in about 20 seconds.

**Size limit in Studio 2024.** Studio 2024 is a 32-bit program, with less memory to work in. There, EverTM refuses an import or index rebuild that would take it past 10 million units: it says so and changes nothing. Segments you confirm are never refused, lookups and export work at any size, and Studio 2026 imports beyond that.

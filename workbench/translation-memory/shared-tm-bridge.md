---
title: "Shared TM Bridge with Trados"
---

The Shared TM Bridge lets you attach Workbench's translation memories directly inside Trados Studio – no TMX export/import dance, no separate copy. The Trados side reads from the same `supervertaler.db` SQLite file Workbench writes, so a TU added in Workbench appears in Trados on the next lookup, and vice versa once write-back ships in a later phase.

Both halves of the feature are off by default. You opt-in TM by TM, so freelancers with multi-client TM libraries don't accidentally surface client A's memory inside a Trados project for client B.

## Half one: tick a TM as "Bridge" in Workbench

1. Open the **TMs** tab.
2. Find the TM you want to expose to Trados.
3. Tick the **Bridge** column for that row. (The column shows an orange checkmark when on.)

That's the entire Workbench side. The TM is now eligible to appear inside Trados Studio.

You can flip the flag at any time. Un-ticking it does NOT delete data – it just hides the TM from the Trados-side picker. Any Trados projects that already attached the bridge will start showing an "offline" status pill for it until you tick it again.

:::note
The **Bridge** column is independent from the **Read** and **Write** flags. Those control whether the TM participates in Workbench's *own* match panel and segment-confirm pipeline. Bridge is purely about exposure to Trados Studio.
:::

## Half two: attach the bridged TM inside Trados

You need the **Supervertaler for Trados** plugin installed (`v4.20.26` or newer) and Trados Studio open on a project with the right language pair.

1. In Trados Studio, open your project's **Project Settings** → **Language Pairs** → **All Language Pairs** → **Translation Memory and Automated Translation**.
2. Click **Add** → **Supervertaler TM**.
3. The picker dialogue lists every TM you've ticked as Bridge in Workbench, filtered to those whose language pair matches the current project's pair (with loose matching – bare `nl` matches `nl-NL`, `en` matches `en-GB`).
4. Tick one or more TMs to attach. Click **OK**.

The TM now shows up alongside any SDLTMs you've attached, with its full name (e.g. *Supervertaler TM: BRANTS (URSU-008-BE-EP)*).

## What you get in this release

- **Exact matches (100%)** – pulled into Trados's TM-results pane the same way a regular SDLTM would.
- **Concordance search** – source-side AND target-side, via the FTS5 index Workbench already maintains. Works in both Trados's built-in Concordance window and the SuperSearch tab.
- **Multiple TMs attached at once** – the per-hit origin strip identifies which bridged TM produced each match (e.g. *Supervertaler: BRANTS (URSU-008-BE-EP)* vs *Supervertaler: PATENTS*).

## What's NOT in this release

- **Write-back from Trados.** Currently read-only. Edits you make to a segment in Trados are confirmed to your normal SDLTM, not to the bridged TM. Bridge support for write-back will land in a later phase.
- **Fuzzy matches.** Only 100% matches are returned. Sub-100 fuzzies fall through to any other providers attached to the project. Fuzzy matching against bridged TMs will also land in a later phase.

## Diagnostics

If a bridged TM isn't showing up where you expect, the easiest first checks are:

- **Bridge ticked in Workbench?** TMs tab → confirm the orange checkmark is on.
- **Language pair matches?** The bridge does loose matching (`nl` matches `nl-NL`) but it still has to match. A TM stored as `en` won't show up for a `fr-FR → de-DE` project.
- **Bridge log.** The Trados plugin writes a diagnostic log to `%TEMP%\supervertaler-tm-bridge.log` every time it talks to a bridged TM. If a lookup is failing, this log usually points straight at the cause.

## See also

- [Translation Memory Basics](basics.md) – the rest of how TMs work in Workbench.
- The matching Trados-side help page lives at [Shared TM Bridge with Workbench](/trados/shared-tm-bridge/).

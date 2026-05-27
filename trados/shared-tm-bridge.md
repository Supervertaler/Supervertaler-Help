---
title: "Shared TM Bridge with Workbench"
---

The Shared TM Bridge attaches your Supervertaler Workbench translation memories directly inside Trados Studio as a translation provider. No TMX export, no scheduled sync – Trados reads from the same `supervertaler.db` SQLite file Workbench writes, so a TU you confirmed in Workbench five minutes ago shows up in Trados the next time it queries the TM.

It's the same feature on both sides. This page covers the Trados half; the Workbench half lives at [Shared TM Bridge with Trados](/workbench/translation-memory/shared-tm-bridge/).

## Prerequisites

- **Supervertaler for Trados** `v4.20.32` or newer installed.
- **Supervertaler Workbench** `v1.10.212` or newer (introduces the per-TM Bridge flag).
- Both products writing to the same data folder. Default is `D:\Supervertaler\` (or wherever you've configured the Workbench data path).
- At least one TM ticked as **Bridge** in Workbench's TMs tab.

## Attaching a bridged TM

1. Open the project in Trados Studio.
2. **Project Settings** → **Language Pairs** → **All Language Pairs** → **Translation Memory and Automated Translation**.
3. Click **Add** → **Supervertaler TM**.
4. The picker dialogue lists every TM you've ticked as Bridge in Workbench, filtered to those whose language pair matches your project. Loose matching applies – a TM stored as bare `nl → en` will show up for an `nl-NL → en-GB` project.
5. Tick the TM(s) you want and click **OK**.

Multiple bridged TMs can be attached to the same project. Each will show up as a separate row in the Translation Memory list, named e.g. *Supervertaler TM: BRANTS (URSU-008-BE-EP)*.

## What you get

- **Exact (100%) matches** in the Translation Results pane, alongside any SDLTMs you have attached.
- **Concordance search** – source-side AND target-side – through both Trados's built-in Concordance window and the SuperSearch tab. Backed by the FTS5 index Workbench maintains.
- **Per-hit TM attribution.** With several bridges attached, each match's origin strip identifies the specific TM it came from – *Supervertaler: BRANTS (URSU-008-BE-EP)* vs *Supervertaler: PATENTS* – so you can tell at a glance which memory contributed which hit.
- **Live updates from Workbench.** Confirming a segment in Workbench writes to the same DB Trados reads, so the new TU appears on the next lookup. No sync step.

## What's NOT in this release

- **Write-back from Trados.** The bridge is read-only. When you confirm a segment in Trados, the update goes to your normal SDLTM, not back to the bridged Workbench TM. Round-trip write support will land in a later phase.
- **Fuzzy matching.** Only 100% matches are returned from bridged TMs. Sub-100 fuzzies need to come from another provider attached to the project (e.g. your main SDLTM). Bridge-side fuzzy matching will also land later.

## Diagnostics

If the bridge isn't behaving as expected, the plugin writes a verbose diagnostic log to:

```
%TEMP%\supervertaler-tm-bridge.log
```

Every search, every method call from Trados, every error – it's all in there with timestamps. If you file a bug, attaching that log makes it much easier to diagnose.

Common issues:

- **Bridged TM doesn't show up in the picker.** Check that the TM is still ticked as Bridge in Workbench's TMs tab, and that its language pair matches the project. The picker filters to compatible pairs only.
- **Bridge attached but matches don't appear.** Make sure the TM actually contains TUs for your source segments. Workbench's own match panel is a good sanity check – if Workbench doesn't find the TU there, Trados won't either.
- **"This TM is offline" pill.** The TM is still referenced in `.sdlproj` but the Bridge flag has been un-ticked in Workbench. Re-tick it, restart Trados, and the project will pick it back up.

## See also

- The matching Workbench-side help page lives at [Shared TM Bridge with Trados](/workbench/translation-memory/shared-tm-bridge/).

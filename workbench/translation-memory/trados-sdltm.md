---
title: "Trados Sdltm"
---

:::note
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
:::

You can attach a Trados Studio Translation Memory (`.sdltm` file) directly to Supervertaler and consult it for matches – without exporting it to TMX first, and without closing Trados.

## When to use this

The typical scenario: you're translating a project in Trados Studio with a working TM. You'd like to consult that same TM from inside Supervertaler – maybe to use its concordance, run AI translations against it, or work on a different project that shares terminology with the Trados project. Rather than exporting to TMX every few minutes, you point Supervertaler at the `.sdltm` directly and let it stay in sync.

## Attach a Trados TM

1. Open **TMs → TM List**.
2. Click **🔗 Attach Trados TM** (next to **📥 Import TMX**).
3. Pick the `.sdltm` file.
4. Confirm the dialog – it shows the TM's languages, name, and translation-unit count.
5. Optionally edit the display name (defaults to the full filename including `.sdltm` so it's easy to spot in the TM list).
6. Watch the progress dialog as Supervertaler mirrors the TUs (≈ 5 seconds for a 13 K-TU TM).

The TM is created **read-only** by default. Supervertaler never writes back to your `.sdltm`; that file remains the source of truth and stays under Trados's exclusive control for writes.

## How sync works

Once attached, the mirror **stays in sync with the live `.sdltm`**. Every 5 seconds Supervertaler checks the file's modification time. When Trados saves a new or modified TU and the file timestamp changes, Supervertaler pulls in just the delta – not a full re-read – and updates the TM's entry count automatically. The mtime check itself is essentially free, so idle ticks cost nothing.

You can keep working in Trados; new TUs you confirm there appear in Supervertaler within a few seconds.

## Tag preservation

Trados-style inline tags are preserved as Supervertaler's `<N>...</N>` markers on the way in:

| Trados                  | Supervertaler |
|-------------------------|---------------|
| Start tag, ID 116       | `<116>`       |
| End tag, ID 116         | `</116>`      |
| Standalone tag, ID 12   | `<12/>`       |

This is the same format Supervertaler uses when it imports SDLXLIFF segments directly, so a TM hit drops cleanly into the editor grid alongside your working segments.

The tag IDs in the TM hit won't necessarily match the IDs in the segment you're translating – TM `<116>` might be your current `<11>`. Structure (start/end pairs, count) is preserved, but you'll still need to renumber tags on insertion if the IDs differ.

## Refreshing manually

If you'd rather refresh on demand than rely on the 5-second timer, click **🔗 Attach Trados TM** again on the same `.sdltm`. You'll be asked "TM already attached – replace?"; click **Yes** and Supervertaler wipes the existing entries and re-mirrors from disk in one go.

## Limitations

- **Read-only**: Supervertaler never writes back to the `.sdltm`. New translations you confirm in the Workbench go to your normal Supervertaler TMs, not back into the Trados file.
- **Tag IDs differ**: as noted above, the numeric IDs on tags in TM hits may differ from the IDs in your current segment. Tag *structure* is preserved.
- **Match scores differ slightly**: Supervertaler uses Python's SequenceMatcher; Trados uses its own token-aligned algorithm. Ranking of matches is similar; exact percentages can be a few points apart.
- **Concurrent use is safe**: opening the `.sdltm` while Trados has it open is fine – Supervertaler reads via SQLite's URI read-only mode, and Trados uses WAL.

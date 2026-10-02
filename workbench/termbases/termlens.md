---
title: "TermLens"
---

TermLens is Supervertaler's inline terminology display. It shows the source text of the current segment word by word, with termbase translations directly underneath each matched term.

## How it works

When you select a segment, TermLens analyses the source text against all active termbases and displays the result in a visual layout:

- **Matched words** appear with their termbase translation underneath
- **Unmatched words** are shown in light text so you can read the full source sentence in context
- **Project termbase** matches appear in pink; **Background termbase** matches appear in blue
- **Non-translatable** terms (if configured) are shown in a distinct style

This gives you an at-a-glance overview of every term in the segment that has a termbase entry – without having to hover or click anything.

### Synonyms get their own chip

A **source synonym** found in the segment is shown where it occurs, even when the entry's main term is in the same sentence (from v1.10.373). Take an entry *methyl-ethylketoxime* → *methyl ethyl ketoxime* with the synonym *MEKO* on both sides. In "…op basis van methyl-ethylketoxime (MEKO) en…", TermLens shows the main term under "methyl-ethylketoxime" **and** **MEKO** under "(MEKO)", each with its own number.

A synonym's chip suggests the matching **target synonym** when the entry has one (MEKO → MEKO), otherwise the main target term, and offers the other forms as alternatives. The grid highlights the synonym too.

## Where to find it

TermLens appears in two places:

1. **Below the grid** – the "TermLens" tab in the bottom panel (toggle with **View → TermLens Under Grid**)
2. **In the Match Panel** – the right-side panel that also shows TM matches

Both instances update simultaneously when you navigate to a new segment.

## Inserting terms

You can insert a termbase translation from TermLens into your target text in three ways:

### Click to insert

Click any translation shown under a source word. The translation is inserted at the cursor position in the target field.

### Keyboard shortcuts (Alt+1 through Alt+9)

Each matched term in TermLens is assigned a numbered badge. Press **Alt+1** to insert the first match, **Alt+2** for the second, and so on.

**Double-tap** for terms 10 and above: press **Alt+1, Alt+1** quickly to insert term 11, **Alt+2, Alt+2** for term 22, etc.

> **Note:** TermLens numbering starts at 1. **Alt+0** inserts the TM match shown in the Match Panel's **✅ TM Target** box.

### Right-click menu

Right-click a term in TermLens to:
- **Insert** the translation
- **Edit** the termbase entry
- **Delete** the termbase entry

## On-demand views (popup & picker)

In addition to the always-visible panels, two on-demand views show the same matches in a more focused layout. Use them when the docked panel is hidden, on small screens, or when you want a keyboard-only insertion flow.

| View                                                | Trigger        | Best for                                                                    |
| --------------------------------------------------- | -------------- | --------------------------------------------------------------------------- |
| [**TermLens popup**](/workbench/termbases/termlens-popup/)             | **Ctrl** tap   | Floating mirror of the docked panel; cycle chips with arrow keys, insert with Enter or 1–9. |
| [**TermPicker**](/workbench/termbases/termpicker/)                     | **Ctrl+Shift+P** | Modal tabular grid with #/Source/Target/Termbase columns and expandable synonym sub-rows. |

Both pull from the same data the docked panel uses, so the chips / rows you see are identical – just laid out differently.

## Font settings

You can customise the TermLens font independently from the grid font:

1. Go to **Settings → View Settings → TermLens Font Settings**
2. Choose font family, size (6–16 pt), and bold/normal weight
3. Changes apply immediately to both TermLens instances

## Tips

- Press **F5** to force a refresh if matches appear to be missing.
- TermLens respects termbase activation – only terms from activated termbases are shown.
- If you have many termbases, designate one as the **Project termbase** (shown in pink) to make its terms stand out.

## TermLens in Trados Studio

TermLens is also part of **Supervertaler for Trados**, where it shows terminology matches directly inside the Trados editor. It reads the same SQLite termbase format, so a termbase made in Workbench works there too.

→ [TermLens in Supervertaler for Trados](/trados/termlens/)

---

## See Also

- [TermLens popup](/workbench/termbases/termlens-popup/) – on-demand floating mirror of the panel (Ctrl tap)
- [TermPicker](/workbench/termbases/termpicker/) – tabular grid view of the same matches (Ctrl+Shift+P)
- [Termbase Basics](/workbench/termbases/basics/)
- [Term Highlighting](/workbench/termbases/highlighting/)
- [Keyboard Shortcuts](/workbench/editor/keyboard-shortcuts/)

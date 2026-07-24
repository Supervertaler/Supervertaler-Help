---
title: "TermLens popup"
---

The **TermLens popup** is a borderless floating version of the docked TermLens panel for the active segment. Designed for keyboard-only term selection on small screens – and for translators who want to insert terms without ever reaching for the mouse.

<figure><img src="/.gitbook/assets/Supervertaler-for-Trados-TermLens-Popup.png" alt=""><figcaption><p>The TermLens popup with the current match highlighted (amber ring on the source word)</p></figcaption></figure>

### When to use it

* **Small screens / laptops** – keeping the docked TermLens panel always-visible can cost too much vertical space, especially for longer source sentences. The popup gives you the same view on demand and disappears when you're done.
* **Pure-keyboard workflows** – Ctrl-tap, cycle, Enter, back to typing. No mouse, no menu hunting.

### Opening and closing

| Key                     | Action                                           |
| ----------------------- | ------------------------------------------------ |
| **Ctrl** (tap)          | Toggle the popup (open if closed, close if open) |
| **Escape**              | Close without inserting                          |
| Click outside the popup | Close without inserting                          |

The popup has no second default shortcut – the Ctrl-tap is its trigger. (Earlier versions listed **Ctrl+Alt+G** as an alternative; that key now belongs to [AutoTagger](../autotagger.md). You can assign your own key to the popup in **File → Options → Keyboard Shortcuts** if you'd like one.)

A "Ctrl tap" is a press-and-release of the Ctrl key on its own – no other key in between, and held for less than 400 ms. The same memoQ-style trigger that older versions of Supervertaler used to open TermPicker.

### Cycling between matches

When the popup opens, the first match has an amber ring around its source word – that is the **current match** that Enter will insert.

| Key                               | Action                                             |
| --------------------------------- | -------------------------------------------------- |
| **Right** / **Down** / **Tab**    | Move the current-match highlight to the next match |
| **Left** / **Up** / **Shift+Tab** | Move it to the previous match                      |

Cycling wraps: from the last match, Right takes you back to the first.

### Inserting

| Key / action       | Result                                                                                             |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| **Enter**          | Insert the current match into the target segment, close the popup, return focus to the target cell |
| **Click any chip** | Insert that match into the target segment, close the popup, return focus to the target cell        |

Both paths share the same insertion logic – there is no difference between picking by keyboard and picking by mouse.

### Editing a match

Press **E** while a match is highlighted to open the term-entry editor for that entry. The popup closes first so the editor opens with clean focus. The editor is the same dialogue the docked panel's right-click "Edit Term…" menu uses, including the multi-termbase editing case for entries that exist in more than one termbase.

:::note
**MultiTerm matches are read-only** in TermLens. Pressing E on a green MultiTerm chip flashes a hint instead – edit those entries in **Trados → Termbase Viewer**.
:::

### Visuals

The popup uses the same chip rendering, colour scheme, and metadata indicators as the docked TermLens panel – pink for project termbase terms, blue for regular Supervertaler terms, yellow for non-translatable, green for MultiTerm. See the [TermLens overview](../termlens.md) for the full colour key.

### TermLens popup vs TermPicker

Both show the same matches for the active segment. Pick whichever fits your style:

|          | TermLens popup (Ctrl tap)                              | [TermPicker](termpicker.md) (Ctrl+Shift+P)              |
| -------- | ------------------------------------------------------ | ------------------------------------------------------- |
| Layout   | Source segment with chips underneath each matched word | Sortable, scrollable table                              |
| Best for | Skimming matches in segment context                    | Many matches that benefit from sorting / typing-to-jump |
| Keyboard | Arrow / Tab cycles a highlighted match                 | 0–9 jumps directly; Up / Down navigate                  |
| Modality | Modeless – click outside to dismiss                    | Modal – Escape or Cancel to close                       |

***

### See Also

* [TermLens overview](../termlens.md)
* [TermPicker](termpicker.md)
* [Keyboard shortcuts](../keyboard-shortcuts.md)

---
title: "TermPicker"
---

**TermPicker** shows all matched terms for the current segment as a sortable, keyboard-navigable list. It is useful when [TermLens](/trados/termlens/) shows many matches and you want a quick overview without scrolling – and it is available either as a popup at your cursor or as a permanently docked pane.

<figure><img src="/.gitbook/assets/Supervertaler-for-Trados-Term-Picker.png" alt=""><figcaption><p>TermPicker with all matched terms for the current segment</p></figcaption></figure>

### Two views, two placements

TermLens and TermPicker are sibling surfaces: both show the terminology matches for the current segment, drawn from the same termbases, but they present them differently. Each is available in both placements, so you can choose the **view** you prefer independently of **where** you want it:

|               | Docked pane                    | Popup at the cursor      |
| ------------- | ------------------------------ | ------------------------ |
| **TermLens**  | TermLens panel                 | tap **Ctrl**             |
| **TermPicker**| TermPicker pane                | **Alt+P**                |

* **TermLens** shows matches *in context* – the source sentence with terms highlighted in place. Best for reading and scanning.
* **TermPicker** shows the same matches as a flat sortable list. Best for quick insertion and for seeing every synonym at once.

### Opening TermPicker

**As a popup:** press **Alt+P**. It appears above the editor with every synonym group already expanded, so you can see all alternatives at a glance. **Escape** closes it.

**As a docked pane:** open it from Studio's **View** tab → **TermPicker**. The pane stays visible and updates as you move through the document, in step with the TermLens panel. Drag it wherever suits you – Studio remembers the position. A layout that works well is the Translation Results window at the top right with the TermPicker pane directly below it.

:::note
When the pane is open, **Alt+P moves the keyboard focus into it** rather than opening the popup on top of it – so the same shortcut always gets you to the list, wherever you keep it. With no pane in your layout, Alt+P opens the popup as usual.
:::

### Colour-coded rows

Each row in TermPicker is colour-coded by termbase type:

| Colour     | Meaning                             |
| ---------- | ----------------------------------- |
| **Pink**   | Project termbase term               |
| **Blue**   | Regular Supervertaler termbase term |
| **Yellow** | Non-translatable term               |
| **Green**  | MultiTerm termbase term (`.sdltb`)  |

This lets you instantly see where each term comes from and how it should be handled.

### Expandable synonyms

Terms with multiple translations open **already expanded**, with their alternatives listed as sub-rows beneath the term, so nothing is hidden behind a marker. Press **Left arrow** to collapse a group (the indicator changes to **▸**) and **Right arrow** to expand it again.

### Keyboard navigation

TermPicker is designed for fast keyboard use, and the keys are identical in the popup and the pane:

| Key           | Action                                                          |
| ------------- | --------------------------------------------------------------- |
| **Up / Down** | Navigate between rows (wraps around)                            |
| **Right**     | Expand synonyms for the selected term                           |
| **Left**      | Collapse synonyms                                               |
| **0-9**       | Jump directly to that term number                               |
| **I**         | Show the term's details – definition, domain, notes, URL, synonyms |
| **E**         | Open the term editor for the selected term                      |
| **Enter**     | Insert the selected term                                        |
| **Escape**    | Close the popup without inserting                               |

Navigation wraps around: pressing **Down** on the last row jumps to the first, and **Up** on the first jumps to the last.

:::note
**I** and **E** work the same way here as in the [TermLens popup](/trados/termlens/termlens-popup/). Press **I** again to dismiss the details popup. MultiTerm terms cannot be edited – those termbases are read-only in Supervertaler; edit them in Trados's own MultiTerm interface.
:::

### Inserting a term

You can insert a term in two ways:

* **Double-click** any row to insert that term at the cursor position in the target field
* **Press Enter** on the selected row

From the popup, inserting also closes it; from the docked pane, the list stays open so you can insert several terms in a row.

Like the TermLens chips, the picker displays and inserts terms with the capitalisation of the segment occurrence (the first occurrence when a term appears more than once) rather than the stored capitalisation – see [Adapt term capitalisation](/trados/settings/termlens/#adapt-term-capitalisation).

***

### See Also

* [TermLens](/trados/termlens/)
* [TermLens popup](/trados/termlens/termlens-popup/)
* [Adding & Editing Terms](/trados/termlens/adding-terms/)
* [Keyboard Shortcuts](/trados/keyboard-shortcuts/)
* [Termbase Management](/trados/termbase-management/)

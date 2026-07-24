---
title: "Keyboard Shortcuts"
---

All keyboard shortcuts available in Supervertaler for Trados, with Mac equivalents for users running Trados in Parallels.

:::note
**Mac users (Parallels):** Ctrl = Control, Alt = Option on Mac keyboards. Check **Parallels → Preferences → Shortcuts** if your modifier key mapping differs.
:::

## First-time setup: free up Trados shortcuts

Trados Studio ships with its own default bindings on several of the key combinations Supervertaler uses – and the Trados binding wins. If a Supervertaler shortcut does nothing, this is almost always why. Go to **File → Options → Keyboard Shortcuts**, search for the Trados action named below, and delete (or reassign) its binding:

| Shortcut | Trados default action (delete its binding) | Supervertaler action that needs it |
|---|---|---|
| `Ctrl+Alt+T` | Insert TM Symbol (™) | Add term entry (full editor) |
| `Ctrl+Alt+N` | New Cloud Project | Quick-add non-translatable term |
| `Ctrl+Alt+G` | Open GroupShare Project | Auto-tag active segment (AutoTagger) |
| `Alt+Up` | Focus Previous Row | Quick-add term to project termbase |
| `Ctrl+Q` | View Internally Source | Open QuickLauncher |

:::note
The same applies to any other Supervertaler shortcut that appears dead: search **File → Options → Keyboard Shortcuts** for that key combination and clear the Trados binding. You only need to do this once per Trados installation – but repeat it after reinstalling or resetting Trados Studio.
:::

## Terminology

| Shortcut (Windows) | Shortcut (Mac) | Action |
|---------------------|----------------|--------|
| `Alt+Down` | `Option+Down` | Quick-add term to write termbases |
| `Alt+Up` | `Option+Up` | Quick-add term to project termbase |
| `Ctrl+Alt+T` | `Control+Option+T` | Add term entry (opens full editor with definition, domain, notes, URL, client, project, and synonyms) |
| `Ctrl+Alt+N` | `Control+Option+N` | Quick-add non-translatable term |
| `Ctrl` (tap) | `Control` (tap) | Toggle the floating **TermLens popup** (open / close) |
| `Ctrl+Shift+P` | `Control+Shift+P` | Open **TermPicker** (list-based) |
| `Alt+1` ... `Alt+9` | `Option+1` ... `Option+9` | Insert term 1–9 by badge number |

## AI Translation

| Shortcut (Windows) | Shortcut (Mac) | Action |
|---------------------|----------------|--------|
| `Ctrl+Q` | `Control+Q` | Open QuickLauncher prompt menu |
| `Alt+T` | `Option+T` | Translate the active segment (uses Batch Translate settings) |

:::note
**Why `Alt+T` and not `Ctrl+T`?** `Ctrl+T` is a Trados factory default ("Apply Translation Result"). Binding *both* to one key made a single press fire both commands, which raced on the same segment and could freeze Studio – so the default moved to the collision-free `Alt+T` (in plugin v18/19.20.119). If you upgraded from an earlier version and still have it on `Ctrl+T`, reassign it to `Alt+T` (or any free key) in **File → Options → Keyboard Shortcuts**; Studio keeps your existing binding across updates.
:::

## QuickLauncher Shortcuts

| Shortcut (Windows) | Shortcut (Mac) | Action |
|---------------------|----------------|--------|
| `Ctrl+Alt+1` ... `Ctrl+Alt+9` | `Control+Option+1` ... `Control+Option+9` | Run QuickLauncher prompt assigned to slot 1–9 |
| `Ctrl+Alt+0` | `Control+Option+0` | Run QuickLauncher prompt assigned to slot 10 |

:::note
Assign prompts to slots in **Settings → Prompts**. Select a QuickLauncher prompt and choose a shortcut from the dropdown in the detail pane. If no slots are assigned, the shortcuts default to menu position order.
:::

## SuperMemory

| Shortcut (Windows) | Shortcut (Mac) | Action |
|---------------------|----------------|--------|
| `Ctrl+Alt+M` | `Control+Option+M` | Quick Add – add a term or correction to the active memory bank |

## SuperSearch

| Shortcut (Windows) | Shortcut (Mac) | Action |
|---------------------|----------------|--------|
| `Alt+S` | `Option+S` | Open SuperSearch -- searches for the selected source/target text across all project files |

## AutoTagger

| Shortcut (Windows) | Shortcut (Mac) | Action |
|---------------------|----------------|--------|
| `Ctrl+Alt+G` | `Control+Option+G` | Auto-tag the active segment – places the source segment's inline tags in the target |

## Navigation and Display

| Shortcut (Windows) | Shortcut (Mac) | Action |
|---------------------|----------------|--------|
| `F1` | `F1` | Context-sensitive help |
| `F2` | `F2` | Expand selection to word boundaries |
| `F5` | `F5` | Force-reload Supervertaler termbases from disk and refresh TermLens display (does not reload MultiTerm termbases) |

## Shortcuts for Terms 10+

When a segment has more than 9 matched terms, you can still insert terms by number using Alt+digit. TermLens offers two shortcut styles – choose the one you prefer in **Settings > TermLens > Term shortcuts**.

### Sequential (default)

Type the term number digit by digit. Each badge shows the plain term number (10, 11, 12, ...).

| Shortcut (Windows) | Shortcut (Mac) | Inserts |
|---------------------|----------------|---------|
| `Alt+10` | `Option+10` | Term 10 |
| `Alt+23` | `Option+23` | Term 23 |
| `Alt+45` | `Option+45` | Term 45 |

After the first digit, TermLens waits briefly for a possible second (or third) digit. If no further digit is pressed, the single-digit term is inserted.

### Repeated digit

Press the **same digit key** multiple times. Each badge shows the repeated digit (11, 222, 3333, ...).

| Presses | Windows | Mac | Badge | Terms |
|---------|---------|-----|-------|-------|
| 1x | `Alt+1` ... `Alt+9` | `Option+1` ... `Option+9` | **1** – **9** | 1–9 |
| 2x | `Alt+11` ... `Alt+99` | `Option+11` ... `Option+99` | **11** – **99** | 10–18 |
| 3x | `Alt+111` ... `Alt+999` | `Option+111` ... `Option+999` | **111** – **999** | 19–27 |
| 4x | `Alt+1111` ... `Alt+9999` | `Option+1111` ... `Option+9999` | **1111** – **9999** | 28–36 |
| 5x | `Alt+11111` ... `Alt+99999` | `Option+11111` ... `Option+99999` | **11111** – **99999** | 37–45 |

:::note
In both modes, when a segment has 9 or fewer matches, pressing Alt+N inserts immediately with no delay.
:::

:::note
Terms beyond 45 have no keyboard shortcut. Use the **TermLens popup** (tap `Ctrl`) or **TermPicker** (`Ctrl+Shift+P`) to insert them.
:::

---

## See Also

- [TermLens](termlens.md)
- [Supervertaler](ai-assistant.md)
- [SuperSearch](supersearch.md)
- [AutoTagger](autotagger.md)
- [Batch Translate](batch-translate.md)
- [SuperMemory](ai-assistant/super-memory.md)

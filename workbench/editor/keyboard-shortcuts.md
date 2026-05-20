---
title: "Keyboard Shortcuts"
---

Master these shortcuts to work faster in Supervertaler. The exact keys are configurable in **Settings → Keyboard Shortcuts**; the tables below list the defaults.

## Navigation

| Shortcut | Action |
|----------|--------|
| `↑/↓` | Previous/next segment when cursor is at the first/last line of the cell |
| `Ctrl+Up` | Previous segment (always) |
| `Ctrl+Down` | Next segment (always) |
| `Ctrl+G` | Go to segment number |
| `Page Up` / `Page Down` | Previous / next page (when paginated) |
| `Shift+Page Up` / `Shift+Page Down` | Extend selection up / down by a screenful |
| `Ctrl+Home` | First segment |
| `Ctrl+End` | Last segment |

## Editing

| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` | Confirm current (or selected) segment(s) and go to the next |
| `Ctrl+Shift+Enter` | Confirm selected segments |
| `Ctrl+Z` | Undo |
| `Ctrl+Y` | Redo |
| `Ctrl+C` / `Ctrl+V` / `Ctrl+X` | Copy / paste / cut |
| `Ctrl+A` | Select all (in cell) |
| `Shift+Enter` | Insert line break inside a cell |
| `Tab` | Cycle between the source and target cells |
| `Ctrl+Tab` | Insert a literal tab character |
| `Ctrl+,` | Insert next tag / wrap selection with a tag pair (when available) |
| `Ctrl+Shift+S` | Copy source text to target |
| `Ctrl+M` | Add a comment to the selected source/target text (or a segment-level comment if nothing is selected) |
| `Alt+D` | Add the word at the cursor to the custom dictionary |

## Translation

| Shortcut | Action |
|----------|--------|
| `Ctrl+T` | Translate current segment with AI |
| `Ctrl+Shift+T` | Translate multiple segments |
| `Ctrl+Space` | Insert the currently selected match from the grid |
| `Alt+1…9` | Insert TermLens term #1…#9 (double-tap for #11…#99) |
| `Ctrl+Alt+Q` | QuickTrans instant-translation popup (works system-wide) |
| `Ctrl+Q` | Open QuickLauncher (AI prompt actions) |

## Find & Replace

| Shortcut | Action |
|----------|--------|
| `Ctrl+F` | Open Find & Replace dialog |
| `Ctrl+H` | Open Find & Replace on the Replace tab |
| `Enter` (in the Find box) | Find next match |

## Filtering

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+F` | Filter on selected text (toggle) |

## Lookup

| Shortcut | Action |
|----------|--------|
| `Ctrl+K` | Open SuperLookup (concordance) for the selection |
| `Ctrl+Alt+L` | SuperLookup as a system-wide hotkey (works from any application) |

## View

| Shortcut | Action |
|----------|--------|
| `Ctrl+Plus` | Increase grid font size |
| `Ctrl+Minus` | Decrease grid font size |
| `Ctrl+Shift+=` / `Ctrl+Shift+-` | Increase / decrease results-pane font size |
| `Ctrl+Shift+H` | Toggle tag view |

## Resources & Tools

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+M` | TM Manager (separate window) |
| `F5` | Force-refresh matches (clear cache) |
| `Ctrl+Alt+C` | Open the Clipboard manager (system-wide) |

## File Operations

| Shortcut | Action |
|----------|--------|
| `Ctrl+S` | Save project |
| `Ctrl+O` | Open project |
| `Alt+F4` | Quit the application |

## Termbase / Glossary

| Shortcut | Action |
|----------|--------|
| `Ctrl+Alt+T` | Add the selected term pair to a termbase (opens the entry dialog) |
| `Alt+Up` (or `Ctrl+Shift+1`) | Quick-add the selected term pair to the project termbase |
| `Alt+Down` (or `Ctrl+Shift+2`) | Quick-add the selected term pair to the background termbase |
| `Ctrl+Alt+N` | Add the selection to Non-Translatables |

## Voice (if enabled)

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+Space` | Voice dictation / push-to-talk (default — configurable) |
| `Ctrl+Alt+A` | Toggle Always-On listening |

---

## Customising shortcuts

You can view and customise every shortcut in **Settings → Keyboard Shortcuts**, and export a printable cheatsheet (HTML) or the raw definitions (JSON) from there.

:::note
Some shortcuts match memoQ and Trados conventions (like `Ctrl+Enter` to confirm) to help translators who switch between tools.
:::

## Tips

### memoQ-style navigation

The arrow keys work like memoQ:
- Press `↓` at the **last line** of a cell to move to the next segment
- Press `↑` at the **first line** of a cell to move to the previous segment
- Cursor column position is preserved when moving between segments

### Quick filtering

1. Select text in any segment
2. Press `Ctrl+Shift+F` to filter
3. Only segments containing that text are shown
4. Press `Ctrl+Shift+F` again to clear the filter

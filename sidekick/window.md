---
title: "The window and the palette"
---

There are two ways into Sidekick. The **window** is for browsing: clipboard on the left, the menu as a tree on the right. The **palette** is for finding: one search box over everything. Both capture whatever text you had selected when they opened, so the thing you act on is the thing you were looking at.

### The window – `` ` ``

Press `` ` `` (backtick) in any application and the window opens with the clipboard history focused, because that is what gets used most. The menu is on the right as a tree of sections – snippet library, bookmarks, AI, text conversions, searches – that you open and close.

| Key | Does |
|---|---|
| `↑` `↓` | move through the list you are in |
| `→` | cross from the clipboard into the menu; open a folder |
| `←` | close a folder, walk up, and cross back to the clipboard |
| `Enter` | use the selected clip or run the selected menu entry |
| `Tab` | switch between the two panes |
| typing | filters both panes at once; `Ctrl+F` jumps to the search box |
| `Alt+1`–`9` | jump straight to the first, second, third… menu section |
| `Ctrl+↑` `Ctrl+↓` | step from section to section |
| `Home` `End` | first and last entry |
| `Ctrl+C` | copy the selected clip without pasting it |
| `Ctrl+Tab`, `Ctrl+1`, `Ctrl+2` | switch between the Clipboard and QuickTrans tabs |
| `Esc` | close |

Using a clip pastes it into the window you came from and ticks it in the list, so a list of terms can be worked through top to bottom without losing your place. See [Clipboard history](/sidekick/clipboard/).

The second tab of the same window is [QuickTrans](/sidekick/quicktrans/). The menu stays beside it, so you can translate something, insert it, and run a menu action without changing windows.

:::tip
On US-International keyboards, common for anyone who types Dutch, French or German, the backtick is a dead key waiting to compose à, è and ù, and claiming it breaks accented typing. Change the key in **Settings → Keyboard shortcuts…**; `Win+Space` and `Ctrl+Alt+Space` are good, rarely taken choices. See [Keyboard shortcuts](/sidekick/keyboard-shortcuts/).
:::

### The palette – `Ctrl+Alt+Space`

The palette is one searchable list of everything Sidekick knows: clipboard history, snippets, searches, AI prompts, bookmarks and conversions in a single window. Type a few letters and it narrows; `↑` and `↓` move, `PgUp` and `PgDn` move ten at a time, `Enter` runs the entry, `Esc` closes.

Use it when you know what you want. Use the window when you want to browse a category you cannot name yet.

### The classic popup menu – Ctrl + backtick

The menu on its own, as a small popup at the mouse pointer, without the clipboard pane. Everything is reachable in two keystrokes: the shortcut, then the accelerator letter underlined in the entry.

### The menu's sections

What the menu contains is entirely yours to change – see [Snippets, bookmarks and conversions](/sidekick/library/). The starter set has these sections:

- **Snippet library** – HTML fragments, special characters, regex patterns
- **Bookmarks** – online and local
- **AI** – prompts that run over the selection, and QuickTrans
- **Text conversions** – case, quotes, brackets, soft hyphens, HTML bold
- **Local searches** – the desktop, and a terminology tool if you have one
- **Web searches** – terminology sources one at a time, or a whole batch
- **Settings** – the Library Editor, keyboard shortcuts, text expansions, AI providers and keys, pausing clipboard capture, and reloading

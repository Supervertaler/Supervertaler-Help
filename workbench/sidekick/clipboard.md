{% hint style="info" %}
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
{% endhint %}

The Clipboard Manager in Supervertaler Workbench captures everything you copy and keeps a persistent history that survives application restarts. Click any item to paste it; trigger a snippet or text conversion to paste the transformed result back to whichever app you came from.

| How | Shortcut |
| --- | --- |
| Open Clipboard from any application | **Ctrl+Alt+C** (⌘⌥C on macOS) |
| Open Clipboard tab manually | Click **📋 Clipboard** in the Workbench tab bar |

When you summon the Clipboard tab via **Ctrl+Alt+C** from another app (e.g. Trados), Workbench automatically sends Ctrl+C in the source app *before* opening the tab. So you don't need a separate "copy first" keystroke – the current selection lands at the top of the clipboard history the moment the tab opens.

![](../../.gitbook/assets/Supervertaler-Workbench-Sidekick-Clipboard.png)

***

## Three columns

The tab is split into three side-by-side panels:

* **📝 Text (left)** – plain text, rich text, and any other text copied from any application
* **🖼 Images (middle)** – raster images (screenshots, copied graphics, etc.)
* **📑 Menu (right)** – a tree of actions to apply to whatever's currently on the clipboard: Personal Snippets, Special Characters, Text Conversions, and your QuickLauncher Prompts

Each column has its own count in its header (e.g. *Text (37)*, *Images (8)*). A draggable splitter lets you resize the three panels.

The column header whose widget currently holds keyboard focus is **highlighted in blue with an underline**, so it's always obvious which column the arrow keys are steering.

***

## How clips are captured

The Clipboard Manager monitors the system clipboard in the background. Every time you copy something in any application – a word in Trados, a URL, a code snippet, a screenshot – it is added to the top of the relevant list automatically.

Duplicate copies of identical content are deduplicated (the existing item moves to the top instead of a new entry appearing).

**Capacity limits:**

| Kind | Maximum items |
| --- | --- |
| Text | 200 |
| Images | 50 |

When a list is full, the oldest item is removed to make room.

***

## Pasting a clip

Click any item in the Text or Images list to paste it. What happens:

1. The item is placed on the system clipboard.
2. Workbench is hidden to the system tray.
3. `Ctrl+V` is sent to whichever window was active before the Clipboard tab opened.

After pasting, the item is marked as used and appears greyed out. This makes it easy to track which clips you have already inserted in a session.

{% hint style="info" %}
**Latest clip is highlighted on open.** Every time you switch to the Clipboard tab, the most recent text clip (top of the list) is selected automatically – press **Enter** to paste it without touching the mouse. If you'd rather paste an older clip, arrow up/down to it first.
{% endhint %}

## The Menu column

The third column gives you actions to apply to whatever's on the clipboard. Expand a category by clicking its arrow or pressing **Right** with the category focused.

### 📌 Personal Snippets

Your own text snippets (e.g. phone numbers, email signatures, boilerplate paragraphs). Snippets are loaded from `.md` files inside your user-data folder – see [Personal Snippets](../../trados/text-transforms.md) for the file format.

Activating a snippet (click or Enter) copies its body to the clipboard and pastes it into the source app via the same hide-and-paste flow used for clipboard clips.

### ✨ Special Characters

Quick-insert symbols, arrows, primes, dashes, quotes, currency signs, legal symbols, mathematical operators, and bullet characters. Activate one to paste the character into the source app.

### 🔁 Text Conversions

Transform whatever text is on the clipboard. The conversions are computed against the *current* clipboard contents – so the typical flow is: select text in another app → **Ctrl+Alt+C** to open the Clipboard tab (current selection auto-copies) → navigate to a conversion → Enter to paste the converted text back over your selection.

| Conversion | Result |
| --- | --- |
| Uppercase | SELECTED TEXT |
| Lowercase | selected text |
| Title Case | Selected Text |
| Sentence case | Selected text |
| Single curly quotes | 'Selected text' |
| Double curly quotes | "Selected text" |
| Round brackets | (Selected text) |
| Square brackets | \[Selected text] |
| Remove soft hyphens | Strips invisible U+00AD characters |
| Double to single quotes | Replaces " with ' |
| Make bold | Wraps in `<b>…</b>` HTML tags |

### 💬 QuickLauncher Prompts

Your custom AI prompts from the Prompt Manager, grouped by folder. Activating a prompt copies its body to the clipboard.

## Deleting clips

**Single item** – right-click any entry in the Text or Images list and choose **🗑 Delete**, or select it and press the **Delete** key.

**All clips** – click **Clear all** in the top-right corner of the Clipboard tab, or right-click any entry and choose **Clear all**. This removes the entire history from both the Text and Images lists and cannot be undone. (The Menu column is unaffected – it's not history.)

***

## Keyboard navigation

| Key | Action |
| --- | --- |
| **Up / Down** | Move through items in the focused column |
| **Right** | Move focus rightwards (Text → Images → Menu) |
| **Left** | Move focus leftwards (Menu → Images → Text) |
| **Right** on a Menu category | Expand the category |
| **Left** on an expanded Menu category | Collapse it |
| **Enter** | Paste the selected item / activate the selected action |
| **Delete** | Remove the selected clip from history (Text / Images lists only) |
| **Esc** | Hide Workbench to the system tray (when focus isn't in a text input) |

***

## Empty state

When a column contains no clips, a centred placeholder message is shown:

* Text column: *No text yet – copy any text to start*
* Image column: *No images yet – copy any image to start*

***

## Persistence

The full clip history is stored in your [user data folder](../reference/faq.md) in a shared SQLite database. Items are available the next time you open Supervertaler Workbench.

***

## Related pages

* [Companion Tabs Overview](overview.md)
* [Voice](voice.md)
* [Trados-aware Chat](trados-aware-chat.md)
* [Keyboard Shortcuts](../settings/shortcuts.md)

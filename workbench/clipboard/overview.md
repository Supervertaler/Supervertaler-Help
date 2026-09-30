---
title: "Clipboard Manager"
---

The Clipboard Manager in Supervertaler Workbench captures everything you copy and keeps a persistent history that survives application restarts. Click any item to paste it; trigger a snippet or text conversion to paste the transformed result back to whichever app you came from.

| How | Shortcut |
| --- | --- |
| Open Clipboard Manager from any application | **Ctrl+Alt+C** (⌘⌥C on macOS) |
| Open Clipboard Manager tab manually | Click **📋 Clipboard Manager** in the Workbench tab bar |

When you summon the Clipboard Manager via **Ctrl+Alt+C** from another app (e.g. Trados), Workbench automatically sends Ctrl+C in the source app *before* opening the tab. So you don't need a separate "copy first" keystroke – the current selection lands at the top of the clipboard history the moment the tab opens.

On Windows, AltGr counts as Ctrl+Alt. Since v1.10.372, if AltGr+C types a character on your keyboard layout (**ć** on a Polish keyboard, for example), you get the character rather than the Clipboard Manager – use the left Ctrl and left Alt keys for the hotkey.

:::note
The tab was renamed from "📋 Clipboard" to "📋 Clipboard Manager" in v1.10.47 to match what the widget actually does – it has been more than a clipboard history for several versions (Snippets, Text Conversions, QuickLauncher Prompts, plus the clipboard history columns).
:::

![](/.gitbook/assets/Supervertaler-Workbench-Sidekick-Clipboard.png)

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

## Privacy: controlling what gets captured

Because the Clipboard Manager captures *everything* you copy while Workbench is running, it will also capture the username and password you copy out of your password manager, licence keys, and anything else you would rather it did not keep. Since **v1.10.369** there are three controls for this, in **Settings → 📋 Clipboard**. They can be combined, and every one of them saves and takes effect immediately – there is no Save button and no restart.

| Control | What it does |
| --- | --- |
| **Capture clipboard history** | Master switch. Off = nothing is captured at all. |
| **Forget clipboard entries after a set time** | Deletes entries older than the window you set (1 minute – 7 days). |
| **Never capture from these applications** | Ignores copying while a named application has the focus. Windows only. |

### The master switch

Unticking **Capture clipboard history** stops capture completely. The check happens *before* Workbench reads the clipboard, so the content is never read, never hashed, never displayed and never written to the database – it does not enter Workbench's memory at all.

While capture is off, the Clipboard tab shows a red **⏸ Capture off** badge in its header, so an empty history is never mistaken for a fault.

:::note
Switching capture off does **not** delete what is already there – existing clips stay in the history and can still be pasted. Use **Clear all** (see [Deleting clips](#deleting-clips)) if you want them gone.
:::

### Automatic deletion

Tick **Forget clipboard entries after a set time** and choose a window. Entries older than that are **deleted from the database**, not merely hidden from the lists.

The sweep runs about once a minute, and also once when Workbench starts – so if Workbench was closed for three hours with a one-hour window set, the expired clips are gone before the list is ever drawn, rather than appearing briefly and then vanishing.

### Excluding particular applications

Add process names exactly as they appear in Task Manager – `keepass.exe`, `1password.exe`, `bitwarden.exe` and so on. While one of those applications has the focus, copying is ignored entirely.

The **Add common password managers** button fills in a dozen widely used ones in a single click. Matching is case-insensitive and the `.exe` is optional, so `KeePass` and `keepass.exe` both work.

:::caution
This control is **Windows only** – identifying which application currently has the focus requires the Windows API. On macOS and Linux the list is saved but has no effect; use the master switch or automatic deletion instead. The Settings page says so on those platforms.
:::

:::note
**Why isn't the exclusion list filled in by default?** Because exclusions are silent by design. If you copied a URL out of KeePass and it simply never appeared in your history, that would look like a bug rather than a feature. So the list starts empty and the password managers are one click away, chosen deliberately by you.
:::

### Defaults

Capture is **on**, automatic deletion is **off**, and the exclusion list is **empty**. An installation that never visits this page behaves exactly as it did before v1.10.369.

***

## Pasting a clip

Click any item in the Text or Images list to paste it. What happens:

1. The item is placed on the system clipboard.
2. Workbench is hidden to the system tray.
3. `Ctrl+V` is sent to whichever window was active when you pressed **Ctrl+Alt+C**.

If you pressed Ctrl+Alt+C inside Workbench itself, it switches back to the tab you were on and pastes there instead. If you opened the tab by clicking it, there is no window to return to, so the item is simply put on the clipboard for you to paste yourself.

After pasting, the item is marked as used and appears greyed out. This makes it easy to track which clips you have already inserted in a session.

:::note
**Apps that ignore Ctrl+V.** Terminals and some other programs don't accept a pasted Ctrl+V. Right-click a text clip and choose **⌨ Paste by typing** to have the text typed out instead, or set the **Paste method** for all pastes (see [Right-clicking a clip](#right-clicking-a-clip)). On Windows, if the target program runs as administrator and Workbench doesn't, Windows blocks the paste; Workbench tells you so, and running Workbench as administrator too solves it.
:::

:::note
**Latest clip is highlighted on open.** Every time you switch to the Clipboard tab, the most recent text clip (top of the list) is selected automatically – press **Enter** to paste it without touching the mouse. If you'd rather paste an older clip, arrow up/down to it first.
:::

### Image preview

The thumbnails in the Images column are small, so near-identical screenshots are hard to tell apart. Move through the Images column with the arrow keys and pause on an item for a moment: a larger preview appears to the left of the column. It follows you as you move on, never takes the focus, and disappears when you leave the column, paste a clip or press Esc.

### Right-clicking a clip

Right-click an entry in the Text or Images list for these options:

| Option | What it does |
| --- | --- |
| **🗑 Delete** | Remove this clip from the history |
| **⌨ Paste by typing** | Text clips only: paste this clip by typing it out, for a program that ignores Ctrl+V |
| **📇 Save to Personal Snippets…** | Text clips only: turn the clip into a permanent snippet in the Menu column. A small dialog lets you change the label first. |
| **✨ Save to Special Characters…** | The same, but into the Special Characters category |
| **Clear all** | Remove the entire history (see [Deleting clips](#deleting-clips)) |
| **Paste method** | How clips are pasted from now on: **Auto – type into terminals, else Ctrl+V** (the default), **Always Ctrl+V**, or **Always type the text**. The choice is remembered. |

## The Menu column

The third column gives you actions to apply to whatever's on the clipboard. Expand a category by clicking its arrow or pressing **Right** with the category focused.

### 🔄 Refresh button

The Menu column header has a small **🔄 Refresh** button on the right. Click it after editing any snippet `.md` file under `<user_data>/snippet_library/` (rename a snippet, change a snippet body, add a new snippet, delete one) or any QuickLauncher prompt `.md` file in the shared prompt library. Refresh rebuilds the entire Menu tree from disk in one click – before v1.10.47 there was no way to pick up external file edits short of restarting Workbench.

Refresh reloads three sources: the unified prompt library (via `UnifiedPromptLibrary.load_all_prompts()`), the snippet library (re-scans `<user_data>/snippet_library/` with a fresh `SnippetLibrary` instance), and the Text Conversions table (in-code, but rebuilt for symmetry).

### 📌 Personal Snippets

Your own text snippets (e.g. phone numbers, email signatures, boilerplate paragraphs). Activating a snippet (click or Enter) copies its body to the clipboard and pastes it into the source app via the same hide-and-paste flow used for clipboard clips.

**Managing snippets.** Right-click in the Menu column:

* on a snippet: **✏ Edit snippet…** (change its label or text) or **🗑 Delete snippet**;
* on a category, or on a snippet inside it: **➕ New snippet in "…"…**;
* on empty space: **➕ New Personal Snippet…**;
* anywhere: **📂 Open snippets folder**.

The quickest way to create one is from a clip: right-click it in the Text list and choose **📇 Save to Personal Snippets…**.

**On disk.** Each snippet is one `.md` file under `snippet_library/` in your [user data folder](/workbench/reference/data-folder/). The file name is the label shown in the Menu, the file's content is the text that gets inserted, and the top-level folder is the category (**Personal Snippets**, **Special Characters**, or any folder you create). Subfolders inside a category show up as collapsible folders in the Menu, to any depth. After editing the files outside Workbench, click **🔄 Refresh**.

### ✨ Special Characters

Quick-insert symbols, arrows, primes, dashes, quotes, currency signs, legal symbols, mathematical operators, and bullet characters. Activate one to paste the character into the source app. These are snippets too, so you can edit, add and delete them in the same way as Personal Snippets.

### 🔁 Text Conversions

Transform whatever text is on the clipboard. The conversions are computed against the *current* clipboard contents – so the typical flow is: select text in another app → **Ctrl+Alt+C** to open the Clipboard Manager (current selection auto-copies) → navigate to a conversion → Enter to paste the converted text back over your selection.

#### The shipped defaults

Eleven conversions ship out of the box: **Uppercase**, **Lowercase**, **Title Case**, **Sentence case**, **Single curly quotes**, **Double curly quotes**, **Round brackets**, **Square brackets**, **Remove soft hyphens (U+00AD)**, **Double quotes → single quotes**, **Make `<b>bold</b>`**.

#### Adding your own

Since v1.10.48, every text conversion is a `.md` file under `<user_data>/text_conversion_library/`. The folder structure on disk is organisational – move files between folders to re-organise; the parent folder name becomes the conversion's category.

Drop a new `.md` file in the right folder, click **🔄 Refresh** on the Menu column, and the new conversion appears. Each file declares one conversion via YAML frontmatter at the top, with an optional human-readable notes section below:

```yaml
---
type: wrap
label: Mark as translator's comment ⟦TC: …⟧
prefix: " ⟦TC: "
suffix: "⟧"
---

Optional notes here. Workbench ignores everything below the closing ---.
```

The four supported `type` values cover most needs without arbitrary-code execution:

| `type` | What it does | Required fields | Optional fields |
| --- | --- | --- | --- |
| `case` | Change case of the whole text | `mode` (one of `upper`, `lower`, `title`, `sentence`, `swap`, `camel`, `snake`, `kebab`) | – |
| `wrap` | Glue a prefix and suffix around the text | `prefix`, `suffix` | – |
| `regex_replace` | Find/replace, literal or regex | `find`, `replace` | `regex` (default `true`), `case_sensitive` (default `true`) |
| `strip_chars` | Remove every occurrence of any listed character | `chars` | – |

Common optional metadata:

* `label` – the display label shown in the Menu. Defaults to the filename stem if omitted (useful when the label contains characters that can't be in filenames, like `:` or `"`).
* `category` – overrides the folder-derived category. Set to an empty string to surface the conversion at the top level.
* `enabled` – defaults to `true`. Set to `false` to hide without deleting (useful for project-specific conversions you might want back later).

#### Concrete examples

A wrap conversion for HTML emphasis:

```yaml
---
type: wrap
label: HTML <em>
prefix: <em>
suffix: </em>
---
```

A strip-chars conversion that removes several invisible characters in one go (uses YAML's `\u` escape inside double quotes):

```yaml
---
type: strip_chars
label: Strip invisible spaces (NBSP + figure space + narrow NBSP)
chars: "   "
---
```

A regex find/replace for em-dash-to-en-dash:

```yaml
---
type: regex_replace
label: "Em dash (—) → en dash (–)"
find: "—"
replace: "–"
regex: false
---
```

A regex find/replace using capture groups for UK → US "-our" → "-or" endings:

```yaml
---
type: regex_replace
label: "UK → US: drop the 'u' from -our endings"
find: "([Cc]olo|[Ff]avo|[Hh]ono|[Ll]abo|[Nn]eighbo|[Bb]ehavio|[Ff]lavo|[Oo]do|[Rr]umo)u(r)"
replace: "\\1\\2"
regex: true
---
```

(Note the doubled backslashes in `replace` – `\\1` in YAML is needed to produce `\1` in the actual regex replacement string.)

#### Things that DON'T work (and why)

The four `type` values are deliberately limited – no arbitrary Python execution from user-data files, no shell commands, no network calls. If you have a transformation that genuinely needs Python (multi-step pipelines that produce intermediate state, calls to an external library, etc.), open a GitHub issue describing the use case and we'll consider adding a `python_file` type with appropriate safeguards.

Broken conversions (invalid `type`, bad regex, missing required field) are silently skipped on load and logged to the Workbench log – the clipboard flow never breaks on a typo. Fix the file, click 🔄 Refresh, and the conversion comes back.

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

The full clip history is stored in your user data folder in a shared SQLite database. Items are available the next time you open Supervertaler Workbench.

Because the history is written to disk and survives restarts, it is worth deciding what you want captured in the first place – see [Privacy: controlling what gets captured](#privacy-controlling-what-gets-captured).

***

## Related pages

* [Voice Commands & Dictation](/workbench/voice/overview/)
* [Chat (AI conversation panel)](/workbench/ai-translation/chat/)
* [Keyboard Shortcuts](/workbench/settings/shortcuts/)

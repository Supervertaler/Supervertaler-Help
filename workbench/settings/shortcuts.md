---
title: "Shortcuts"
---

:::note
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
:::

Supervertaler has one keyboard shortcut per action. The same combination works whether Supervertaler is the focused application or whether you trigger it from another app – there's no longer a separate "Global" entry to keep in sync with the in-app one.

## Managing shortcuts

Open **Settings → Keyboard Shortcuts**. Each row is one action. Click a row to edit, press the new combination, hit OK. Changes apply immediately – no restart needed.

Rows whose action label starts with 🌍 also register as an OS-level global hotkey, so they fire from any application. The rest are in-app only (e.g. segment navigation, match insertion).

## Default shortcuts that work everywhere

The 🌍 actions and their out-of-the-box bindings:

| Action | Default | Notes |
|---|---|---|
| Open Clipboard | **Ctrl+Alt+C** (Win/Linux) / **⌘⌥C** (macOS) | Auto-copies the current selection, then opens Workbench's Clipboard tab |
| Open SuperLookup | **Ctrl+Alt+L** / **⌘⌥L** | Auto-copies the current selection, then opens Workbench's SuperLookup tab with the text pre-filled and the search auto-fired |
| QuickTrans | **Ctrl+Alt+Q** / **⌘⌥Q** | Instant translation popup; auto-copies the selection |
| Voice dictation / push-to-talk | **Ctrl+Shift+Space** / **⌘⇧Space** | Toggles recording; a "🎤 Listening…" toast confirms the mic is live |
| Voice Always-On (toggle) | **Ctrl+Alt+A** / **⌘⌥A** | Continuous listening on/off |

:::note
**Ctrl+Alt+K** used to summon a floating Supervertaler Sidekick window through v1.10.3. Sidekick was retired in v1.10.4 and the chord is now unbound by default. The companion tabs (Clipboard, Voice, SuperLookup) are reachable via the dedicated hotkeys above; Chat lives in Workbench's right panel.
:::

Rebind any of these in **Settings → Keyboard Shortcuts** by clicking the row and pressing a new combination.

## macOS vs Windows: symbols and modifier names

The two platforms use different conventions for naming and drawing modifier keys. Supervertaler shows the platform-native symbols in the UI, but it's useful to know what each one means:

| Symbol | macOS name | Windows / Linux name | Physical key |
|---|---|---|---|
| **⌘** | Command (Cmd) | – | The key with the Apple/Command glyph |
| **⌃** | Control (Ctrl) | Ctrl | The Control key |
| **⌥** | Option (Opt) | Alt | The Alt key (top of the Option key on Mac) |
| **⇧** | Shift | Shift | The Shift key |

So a shortcut shown as **⌃⌘L** on macOS is read "Control + Command + L". See the next section for how Supervertaler stores that internally and why the stored name doesn't always match the Mac symbol.

## What "Ctrl" means inside Supervertaler

Internally, shortcuts are stored in Qt's cross-platform format, which uses **Ctrl**, **Alt**, **Shift**, and **Meta** as labels. Qt swaps **Ctrl** and **Meta** on macOS so that the same shortcut string works on every platform. The mapping:

| Stored as… | …means on Windows / Linux | …means on macOS |
|---|---|---|
| `Ctrl` | Ctrl | **Cmd** (⌘) |
| `Alt` | Alt | **Option** (⌥) |
| `Shift` | Shift | **Shift** (⇧) |
| `Meta` | Windows key | **Control** (⌃) |

You only ever see this if you export shortcuts to JSON or look at the cheatsheet HTML – the UI itself always shows you platform-native symbols on macOS and plain names on Windows. The default for Superlookup is therefore stored as `Ctrl+Alt+L` and displayed as **Ctrl+Alt+L** on Windows and **⌘⌥L** on macOS, both of which fire the same physical chord on each platform.

## Per-platform notes

**macOS**

Global hotkeys require Accessibility permission on whichever binary launched Python:

- Bundled `Supervertaler.app` → add **Supervertaler** in System Settings → Privacy & Security → Accessibility
- Launched from `Terminal.app` → add **Terminal.app** instead
- Launched from iTerm2 → add **iTerm2.app** instead

Also requires the `pyobjc-framework-Cocoa` Python package (`pip install pyobjc-framework-Cocoa`); the bundled `.app` ships with it.

The Status indicator on the right-hand side of Settings → Keyboard Shortcuts shows **Active (via NSEvent)** when global hotkeys are working on macOS.

**Windows**

Global hotkeys are registered via the native `RegisterHotKey` API, which consumes the keystroke at the OS level. The combination is reserved for Supervertaler whenever it's running. If another app has already claimed the same combination, Supervertaler logs a `failed_hotkeys` warning and that one combination won't fire – re-bind to something free in Settings → Keyboard Shortcuts.

**Linux**

Global hotkeys go through `pynput`, which uses XGrabKey under X11. If hotkeys silently don't fire, your user may need to be in the `input` group (`sudo usermod -aG input $USER`, then log out and back in).

## Companion-tab keyboard navigation

When you've summoned the Clipboard, SuperLookup, or Voice tab via a global hotkey, these shortcuts work straight away – no clicking around to land your focus first:

| Shortcut | Action |
|---|---|
| **Esc** | Hide Workbench to the system tray (quick-lookup tabs only – Editor / Settings / etc. keep the natural Esc) |
| **↑ / ↓** | Navigate within the focused column (e.g. clipboard text history, snippet list) |
| **← / →** | Move focus between columns in the Clipboard tab (Text → Images → Menu) |
| **Enter** | Activate the selected item (paste clip, run snippet, fire conversion) |

## Editor shortcuts

The editor (translation grid) has its own set of shortcuts for navigation, match insertion, term operations, and so on. See [Editor Keyboard Shortcuts](../editor/keyboard-shortcuts.md) for the full list.

## Exporting a printable cheatsheet

The settings page has an **Export Cheatsheet (HTML)** button on the right-hand panel. It writes a self-contained HTML file showing every shortcut grouped by category, with the platform-native symbols already substituted in. Print it or save it as PDF.

## Related pages

- [Editor Keyboard Shortcuts](../editor/keyboard-shortcuts.md)
- [Voice](../sidekick/voice.md)
- [Companion Tabs Overview](../sidekick/overview.md)

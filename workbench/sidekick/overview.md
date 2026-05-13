{% hint style="info" %}
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
{% endhint %}

Supervertaler Workbench includes four **companion surfaces** that sit alongside the translation grid: SuperLookup, Clipboard, Voice, and Chat. They cover the lookup-and-capture tasks you reach for dozens of times a day while translating – concordance searches, clipboard history, voice commands, AI conversation – without making you leave the editor or the app you're in.

Three of them are top-level tabs in Workbench (next to Editor, TMs, Termbases, AI, Settings); the fourth, Chat, sits as a side panel next to the editor so you can keep an AI conversation visible while you translate.

{% hint style="info" %}
**Where did Sidekick go?** Through v1.10.3, these four surfaces lived inside a separate always-on-top floating window called Supervertaler Sidekick. It was retired in v1.10.4 and the tabs were promoted into Workbench itself. The companion surfaces below behave exactly as they did inside Sidekick – they're just hosted differently now, with proper taskbar / Alt+Tab presence and access via top-level tabs instead of a separate window. The global hotkey **Ctrl+Alt+K** that used to summon Sidekick has been unbound.
{% endhint %}

### 🔍 SuperLookup

Simultaneous search across your translation memories, glossaries, machine-translation engines, and web resources – all in one panel. Select text anywhere on your computer, press **Ctrl+Alt+L**, and Workbench's SuperLookup tab opens with the selected text pre-filled and the search auto-fired.

→ [SuperLookup Overview](../superlookup/overview.md)

### 📋 Clipboard

A persistent clipboard manager that captures everything you copy – text and images – from any application, plus a third "Menu" column with snippets, special characters, text conversions, and your QuickLauncher prompts. Press **Ctrl+Alt+C** anywhere on your computer to grab the current selection and open the Clipboard tab in one keystroke.

→ [Clipboard Manager](clipboard.md)

### 🎤 Voice

Voice commands and push-to-talk dictation. Create commands that press keyboard shortcuts, run scripts, or call Workbench functions – then speak them while working in Trados, memoQ, Word, or any other app. **Ctrl+Alt+A** toggles always-on listening from anywhere.

→ [Voice](voice.md)

### 💬 Chat

The AI assistant panel, mounted in Workbench's right panel next to the editor (one click on the 💬 Chat tab). Ask questions about terminology, get translation suggestions, attach files for the AI to read, and – when Supervertaler for Trados is also running – pick up the active Trados project context automatically.

→ [Trados-aware Chat](trados-aware-chat.md)

***

### Opening the companion tabs

| How | Shortcut | Notes |
| --- | --- | --- |
| SuperLookup from any application | **Ctrl+Alt+L** (⌘⌥L on macOS) | Auto-copies the current selection and opens SuperLookup with the text pre-filled and the search fired |
| Clipboard manager from any application | **Ctrl+Alt+C** (⌘⌥C on macOS) | Auto-copies the current selection so the just-copied text lands at the top of the history |
| QuickTrans popup from any application | **Ctrl+Alt+Q** (⌘⌥Q on macOS) | Opens an always-on-top popup with translations from every enabled provider; see [QuickTrans Popup](quicktrans-popup.md) |
| Voice always-on (toggle) | **Ctrl+Alt+A** (⌘⌥A on macOS) | Starts / stops continuous voice-command listening |
| Push-to-talk dictation | **Ctrl+Shift+Space** | Records one utterance and types the transcript at the cursor |
| Open Chat | Click the **💬 Chat** tab in the right panel | Right panel sits next to the editor on the Editor tab |

All of these hotkeys can be customised in **Settings → Keyboard Shortcuts**.

### Pressing Esc dismisses Workbench to the tray

When you're on SuperLookup, Clipboard, or Voice – the surfaces summoned via global hotkeys – pressing **Esc** hides Workbench back to the system tray. Useful when you're using Workbench as a popup utility from another app: hotkey to summon, Esc to dismiss.

* **On SuperLookup**: Esc unconditionally hides Workbench, even when the cursor is in the search box. The dominant use of SuperLookup is a one-shot query, so there's nothing worth keeping if you change your mind.
* **On Clipboard and Voice**: Esc hides Workbench *unless* the focused widget is a text input (search field, command editor, etc.) – in those cases Esc behaves the way it does in any other app (clears the field, closes a dropdown, etc.).
* **On Editor, TMs, Termbases, AI, Settings**: Esc keeps its natural editor / dialog / combo-box behaviour. Workbench is never hidden by accident from the surfaces where you actually do work.

### Tray quick-jump menu

Right-click the Workbench tray icon (the orange Sv) for a menu with **Show Workbench**, **Open SuperLookup**, **Open Clipboard**, **Open Voice**, **Open Settings**, plus toggles for **Close to tray** and **Start with computer**.

***

### Related pages

* [SuperLookup Overview](../superlookup/overview.md)
* [Clipboard Manager](clipboard.md)
* [Voice](voice.md)
* [Trados-aware Chat](trados-aware-chat.md)
* [QuickTrans Popup](quicktrans-popup.md)
* [Keyboard Shortcuts](../settings/shortcuts.md)

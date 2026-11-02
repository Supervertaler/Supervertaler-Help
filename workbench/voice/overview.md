---
title: "Voice"
---

**Voice** lets you control Workbench – and Trados, memoQ, Word or anything else in the foreground – with spoken **commands**: "next segment", "confirm", "copy source", "undo", and any commands you add yourself. It runs offline, on your own computer.

Open it via the **🎤 Voice** top tab in Workbench or the tray icon's **🎤 Open Voice** entry, or press **Ctrl+Alt+O** to switch listening on or off from anywhere on your computer.

:::note[Commands only – use a dictation tool for running text]
Voice does not write your translation. For running text, use a dictation tool such as Windows voice typing (**Win+H**), [Wispr Flow](https://wisprflow.ai/) or Dragon. Voice keeps listening for commands while you dictate with it. This is the same approach as SuperVoice in [Supervertaler for Trados](/trados/voice-commands/).

Workbench used to have its own push-to-talk dictation (Ctrl+Shift+Space). It was removed in v1.10.374.
:::

***

## Listening

Voice listens until you switch it off. When you speak, it detects the start and end of what you say from the sound level, and hands the recording to **Vosk**, the offline speech recogniser Voice uses.

Vosk only knows the phrases in your command list – anything else comes out as `[unk]`. Speech that matches no command is never typed: the status bar just says **No command matched**. So you can leave Voice on, talk to colleagues or take phone calls, and only your command phrases trigger anything.

**To start:** click **▶️ Start Always-On** in the Voice tab, press **Ctrl+Alt+O** from any application, or click the microphone icon in the system tray.

**To stop:** the same again – **⏹️ Stop Always-On**, **Ctrl+Alt+O**, the tray icon – or say **"stop listening"**.

The tray icon is grey while Voice is off and red while it is listening; right-click it for **▶ Start Always-On** and **🎤 Open Voice**.

**Commands are spoken in English**, whatever your project's languages. The first time you start listening, the small English speech model (about 40 MB) downloads to the `vosk-models` folder in your data folder.

**Focus matters:** commands that press keys go to whichever window is in front. After switching listening on, click into Trados, memoQ or Word before you speak.

### What I heard

Under the listening controls, **What I heard** lists the last 50 things Voice heard, newest first, and what happened:

- green – a command ran, e.g. *“undo” → ✓ Undo last action*
- red – a command matched but failed, e.g. a key it couldn't send
- grey – *no command matched*

If a command didn't fire, this is where you see why. The list is cleared when Workbench closes.

***

## Voice commands

Voice commands run an action when you speak their phrase. They can call a Workbench action, press keys in the program in front, or run AutoHotkey code.

### How a phrase is matched

- A command fires when you say its phrase (or one of its aliases) on its own. Capitals don't matter.
- A phrase of **two or more words** also fires when Voice hears it inside a longer utterance.
- A **one-word** command fires only when you say it on its own – never from the middle of a sentence.
- Near misses don't count: Voice never fires the "closest" command.

:::caution[Choose distinctive phrases]
Voice keeps listening while you dictate with another tool, so an everyday word could fire mid-sentence. Prefer two or three words – "next segment", not "next"; "confirm segment", not "okay". The built-in commands follow this rule.
:::

### The commands table

The commands table (right side of the Voice tab) lists all your configured commands.

| Column | Description |
| --- | --- |
| ☑ | Enable/disable checkbox – uncheck to silence a command without deleting it |
| Phrase | The primary trigger word or phrase |
| Aliases | Alternative phrases that also trigger the command |
| Type | Command / Keystroke / AHK Script / AHK Inline |
| Action | What happens when the phrase is recognised |
| Category | Organisational label (Navigation, Editing, etc.) |

### Enabling and disabling commands

- **Single command** – click the checkbox in the first column
- **All commands** – click the checkbox column header to toggle all at once (enables any disabled, or disables all if all are already active)
- **Multiple commands** – select rows with **Shift+Click** or **Ctrl+Click**, then right-click and choose **✅ Activate** or **⬜ Deactivate**

Disabled commands are greyed out and are skipped during recognition. Their settings are preserved.

### Editing a command

Double-click any row to open the Edit Voice Command dialog. You can change the phrase, aliases, action type, and action value.

You can also select a row and click the **✏️ Edit** button below the table.

### Adding a command

Click **➕ Add** below the table. Choose a command type:

- **Command** – calls an internal Workbench action (confirm segment, next segment, etc.)
- **Keystroke** – sends a key combination to the active window. Click into the **Keystroke** field and press the keys you want to send (e.g. press Ctrl+Enter); the field shows the platform-native symbols (⌘⇧⌥⌃ on macOS, Ctrl+Shift+Alt elsewhere) so you don't have to translate between platforms. Keystroke commands don't need AutoHotkey.
- **AHK Script** – runs an AutoHotkey v2 script file
- **AHK Inline** – runs a short AutoHotkey v2 snippet directly

The Edit Voice Command dialog includes a **context-sensitive cheat sheet** below the Action field that updates with the Type dropdown – it explains the press-to-capture editor for Keystroke commands, lists common AHK patterns for AutoHotkey Code, names the available internal actions, etc. So you don't need to memorise the full reference up front.

:::note
**Keystroke commands are cross-platform.** A command captured as **Ctrl+S** on Windows is stored in Qt's portable format and fires **⌘S** automatically on macOS – the macOS dispatcher swaps Ctrl ↔ Cmd internally to match what every Mac app does. So you can build your command list once and it works on whichever machine Supervertaler is running on. Under the hood, Windows uses `SendInput` (compatible with WPF apps like Trados Studio) and macOS uses AppleScript via `osascript`.
:::

### Removing a command

Select the row and click **🗑️ Remove**, or select multiple rows and remove them together. **🔄 Reset** restores the default command list.

### Edits take effect immediately

Adding / editing / removing / disabling a command immediately rebuilds Vosk's list of phrases in the background – you don't have to stop and restart listening to "teach" Vosk a new phrase. The next thing you say uses the new list.

***

## Settings

All Voice settings are in the left half of the **🎤 Voice** tab. They are saved as soon as you change them.

### Microphone

The **Microphone** dropdown picks the input device. **System default** follows whatever microphone your operating system has selected. If a chosen microphone is unplugged, Voice falls back to the system default.

### 🎤 Voice commands

- **▶️ Start Always-On** / **⏹️ Stop Always-On**, with a status line (**⚪ Not active**, **⏳ Starting…** while the speech model loads – or downloads, the first time – **🟢 Listening for speech…**, **🔴 Recording…**, **⏳ Processing…**). If listening stops by itself (say, the microphone is unplugged), Voice shows an error and goes back to **⚪ Not active**.
- **On/off hotkey** – shows the hotkey (**Ctrl+Alt+O** by default). Click **Change in Settings → Keyboard Shortcuts** to give it another key – any key works, for example numpad **+**.
- **Mic sensitivity** – the sound level that counts as speech:
  - **Low (noisy)** – raises the threshold; ignores quiet background sounds but may miss soft speech
  - **Medium (normal)** – default; works well in a typical home office
  - **High (quiet)** – lowers the threshold; captures quiet voices but may trigger on background noise

***

## AutoHotkey integration

AutoHotkey v2 is only needed for **AHK Inline** and **AHK Script** commands. Supervertaler checks for it automatically and shows the result under the commands table: **✅ AutoHotkey detected** or **⚠️ AutoHotkey not found**.

Click **📂 Scripts folder** to open the folder where standalone AHK script files are stored.

***

## Using Voice with Trados Studio

Voice sends input at the Win32 hardware-input level (equivalent to physical keystrokes), which is fully compatible with Trados Studio's WPF editor. Useful commands to add:

| Phrase | Type | Action |
| --- | --- | --- |
| "confirm segment" | Keystroke | `ctrl+enter` |
| "next segment" | Keystroke | `alt+down` |
| "previous segment" | Keystroke | `alt+up` |
| "go to top" | Keystroke | `ctrl+home` |
| "undo" | Keystroke | `ctrl+z` |

After creating a command, start listening, click into Trados Studio, and speak the phrase. If you work in Trados most of the time, Supervertaler for Trados has its own voice commands, [SuperVoice](/trados/voice-commands/), which work inside Studio.

***

## Global hotkeys

| Shortcut | Action |
| --- | --- |
| **Ctrl+Alt+O** (⌘⌥O on macOS) | Switch listening on or off |

Global hotkeys work on macOS too (via the NSEvent monitor), but require Accessibility permission for whichever binary launched Python – see [Keyboard Shortcuts](/workbench/settings/shortcuts/#per-platform-notes) for setup. All hotkeys can be customised in **Settings → Keyboard Shortcuts**.

On Windows, AltGr counts as Ctrl+Alt. Since v1.10.372, if AltGr+O types a character on your keyboard layout, you get the character rather than the Voice hotkey – use the left Ctrl and left Alt keys for the hotkey.

:::note
**Always-On moved from Ctrl+Alt+A to Ctrl+Alt+O in v1.10.368.** Supervertaler for Trados now uses Ctrl+Alt+A for "Add term with abbreviation", and because Always-On is a *global* hotkey it fires whichever application is in front – so a single press in Trados would have triggered both. If you had customised it to Ctrl+Alt+A yourself, it has been returned to the new default; you can set it back, but it will keep clashing while both products are running.
:::

***

## Related pages

- [Clipboard Manager](/workbench/clipboard/overview/)
- [Keyboard Shortcuts](/workbench/settings/shortcuts/)
- [General Settings](/workbench/settings/general/)

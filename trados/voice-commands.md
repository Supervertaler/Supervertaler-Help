---
title: "Voice Commands"
---

Control Trados Studio hands-free with spoken commands: confirm segments, navigate, insert TermLens matches, apply translation results, add terms and more – without touching your keyboard. Designed to pair with dictation tools such as Wispr Flow or Dragon: they type your translation, Supervertaler handles the commands.

### Starting and stopping

Two ways to toggle voice commands:

* Click the **🎤 microphone button** in the TermLens panel header (next to the ↻ refresh button)
* Press **Ctrl+Alt+V** (also available in the editor right-click menu)

<figure><img src="/.gitbook/assets/Supervertaler-for-Trados_Voice-commands-button.png" alt="The microphone button in the TermLens header, green while listening"><figcaption>The 🎤 button in the TermLens header – green while listening</figcaption></figure>

The microphone button shows the state at a glance:

| Colour | Meaning |
| ------ | ------- |
| **Grey** | Off – click to start |
| **Orange** | Starting (or downloading the voice runtime on first use) |
| **Green** | Listening |

Each command you speak flashes briefly in the TermLens status label (e.g. `🎤 "confirm"`), so you always know what was heard.

:::note
**First activation** downloads the offline voice engine and a small English model (~50 MB, one-time) – progress is shown in the status label. Every later activation is instant.
:::

If the TermLens panel isn't open, a small floating status strip appears instead (bottom-right). You can drag it anywhere – the position is remembered.

### Default commands

Everything works out of the box – no configuration needed. Most commands also respond to an alias, so you can use whichever phrasing comes naturally:

| Say | Or | Action |
| --- | -- | ------ |
| "confirm" | "confirm segment" | Confirm segment and move to next unconfirmed |
| "next segment" | "go down" | Move to the next segment (without confirming) |
| "previous segment" | "go up" | Move to the previous segment |
| "go to the top" | "go to top" | Jump to the first segment (Ctrl+Home) |
| "go to the bottom" | "go to bottom" | Jump to the last segment (Ctrl+End) |
| "copy source" | "copy from source" | Copy source to target |
| "clear target" | | Clear the target segment |
| "term one" … "term nine" | | Insert TermLens match 1–9 (with [capitalisation adaptation](termlens.md#automatic-capitalisation)) |
| "match one" … "match nine" | | Apply Translation Results match 1–9 (Ctrl+1–9) |
| "term picker" | "pick term" | Open [TermPicker](termlens/termpicker.md) |
| "term popup" | "show terms" | Open the [TermLens popup](termlens/termlens-popup.md) |
| "add term" | "new term" | Quick-add the selection to your write termbases (Alt+Down) |
| "add project term" | "project term" | Quick-add the selection to the project termbase (Alt+Up) |
| "translate" | "translate segment" | AI-translate the active segment |
| "concordance" | "search memory" | Concordance search on the selection (F3) |
| "zoom in" | "bigger font" | Increase the editor font size (see setup below) |
| "zoom out" | "smaller font" | Decrease the editor font size (see setup below) |
| "escape" | "close window" | Close the focused popup or dialog |
| "stop listening" | "voice off" | Turn voice commands off |

### One-time setup for "zoom in" / "zoom out"

Trados Studio's font-size actions ship **without a default keyboard shortcut**, so these two commands need a one-time binding:

1. Go to **File > Options > Keyboard Shortcuts > Editor**
2. Scroll down to the actions named simply **Increase** and **Decrease** (note: the Keyboard Shortcuts page has no search box – you have to scroll)
3. Set **Increase** to `Ctrl+Alt+PgUp` and **Decrease** to `Ctrl+Alt+PgDn`
4. Click **OK**

From then on, "zoom in" and "zoom out" control the editor font size hands-free. (Make sure **Adapt font sizes** is enabled under File > Options > Editor > Font Adaptation.)

### Safety and privacy

* **Fully offline** – recognition runs locally on your machine (Vosk engine); no audio is ever sent anywhere.
* **Grammar-constrained** – the recogniser listens *only* for your command phrases, which is what makes commands fast and reliable. Normal speech and dictation are ignored.
* **Foreground guard** – commands only execute while Trados Studio is the active window. Speaking in another app can't trigger anything ("stop listening" is the one exception – it always works).

### Customising commands

Right-click the 🎤 button (or click ⚙ on the floating strip) to open the **Voice command settings** dialog (also reachable via the **?** in its title bar and **F1** for this help page):

<figure><img src="/.gitbook/assets/Supervertaler-for-Trados_Voice-command-settings.png" alt="The Voice command settings dialog with the full command grid"><figcaption>Voice command settings – every phrase, alias and action is editable</figcaption></figure>

* Enable/disable individual commands
* Edit spoken phrases and add aliases
* Add your own commands, mapped to either:
  * a **keystroke** chord sent to Studio (e.g. `ctrl+enter`, `alt+up`, `f3`) – any Studio or Supervertaler shortcut works
  * an **internal** plugin action: `insert_term_1`…`insert_term_9`, `term_picker`, `termlens_popup`, `navigate_next`, `navigate_previous`, `stop_listening`

:::note
The recogniser only listens for the phrases in your command list, so keep phrases short and distinct from each other. After saving, the recogniser updates immediately – no restart needed.
:::

Commands are stored in `trados/settings/voice_commands.json` in your Supervertaler data folder, in the same format as Supervertaler Workbench's voice commands – so you can exchange command sets between the two products.

Default commands added in plugin updates are **merged into your saved set automatically** – your customisations are never touched. Because of this, if you want to get rid of a default command, **untick it rather than delete it** (a deleted phrase would come back if a later update re-ships it). **Restore defaults** replaces everything with the built-in set, discarding your customisations.

### Troubleshooting

* **"Voice commands could not start"** – check that a microphone is available in Windows sound settings, and that the first-run download completed (an interrupted download can be retried by simply starting voice commands again).
* **A command isn't recognised** – speak the phrase on its own, at normal pace. If a phrase never triggers, give it a more distinctive alias in Voice command settings.
* **Corrupt model** – delete the `trados/voice/models` folder in your Supervertaler data folder; the next activation re-downloads it.

### See Also

* [Keyboard Shortcuts](keyboard-shortcuts.md)
* [TermLens](termlens.md)
* [TermPicker](termlens/termpicker.md)

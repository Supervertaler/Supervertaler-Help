---
title: "SuperVoice"
---

**SuperVoice** is voice control for Trados Studio – spoken commands, hands-free selection (beta), and a hand-off to your dictation tool. Control Trados Studio hands-free with spoken commands: confirm segments, navigate, insert TermLens matches, apply translation results, add terms and more – without touching your keyboard. Designed to pair with dictation tools such as Wispr Flow or Dragon: they type your translation, Supervertaler handles the commands.

:::note
Selecting and replacing words you have just dictated – and handing the microphone to a dictation tool and back – has a page of its own: **[Dictation](/trados/voice-commands/dictation/)**.
:::

### The SuperVoice pane

**View > SuperVoice** opens SuperVoice's own dockable pane: the microphone button, its state, and a list of what has been heard – newest at the top, each utterance beside what happened to it.

| Row colour | Meaning |
| ---------- | ------- |
| **Green** | A command ran, or words were selected |
| **Amber** | Understood but declined, with the reason – an ambiguous phrase, a word inside another word |
| **Red** | A command that tried and failed |
| **Grey** | Ordinary speech that matched no command – not an error |

The pane opens on the right beside Translation Results, as a tab. That suits how it is used: the microphone's state is already visible all the time in the TermLens header, and the pane holds the *history*, which you look at when something did not do what you expected. Drag it anywhere and Studio remembers. Sized to a few rows it always shows the last thing that happened; make it taller to see more.

### Starting and stopping

Three ways to toggle voice commands:

* Click the **🎤 microphone button** in the SuperVoice pane
* Click the **🎤 microphone button** in the TermLens panel header (next to the ↻ refresh button)
* Press **Ctrl+Alt+D** (also available in the editor right-click menu)

<figure><img src="/.gitbook/assets/Supervertaler-for-Trados_Voice-commands-button.png" alt="The microphone button in the TermLens header, green while listening"><figcaption>The 🎤 button in the TermLens header – green while listening</figcaption></figure>

The microphone button shows the state at a glance:

| Colour | Meaning |
| ------ | ------- |
| **Grey** | Off – click to start |
| **Orange** | Starting (or downloading the voice runtime on first use) |
| **Green** | Listening |

Each command you speak flashes briefly in the TermLens status label (e.g. `🎤 "confirm"`), and is kept in the SuperVoice pane.

:::note
**First activation** downloads the offline voice engine and a small English model (~50 MB, one-time) – progress is shown in the status label. Every later activation is instant.
:::

If neither the SuperVoice pane nor the TermLens panel is open, a small floating status strip appears instead (bottom-right). You can drag it anywhere – the position is remembered. It does not appear while the SuperVoice pane is open.

### Default commands

Everything works out of the box – no configuration needed. Most commands also respond to an alias, so you can use whichever phrasing comes naturally:

| Say | Or | Action |
| --- | --- | ------ |
| "select …" | "choose …" | **Beta, off by default.** Select those words in the target – see [Dictation](/trados/voice-commands/dictation/) |
| "delete that" | "delete this", "remove that" | Delete whatever is selected in the target |
| "undo that" | "scratch that", "undo" | Undo the last change (Ctrl+Z) |
| "select source …" | "source select …" | **Beta, off by default.** Select those words in the **source** segment – see [Dictation](/trados/voice-commands/dictation/) |
| "dictate" | "start dictating" | Hand over to an external dictation tool (**off by default** – see [Dictation](/trados/voice-commands/dictation/)) |
| "stop now" | "stop dictating" | Take dictation back (**off by default**) |
| "confirm" | "confirm segment" | Confirm segment and move to next unconfirmed |
| "next segment" | "go down" | Move to the next segment (without confirming) |
| "previous segment" | "go up" | Move to the previous segment |
| "go to the top" | "go to top" | Jump to the first segment (Ctrl+Home) |
| "go to the bottom" | "go to bottom" | Jump to the last segment (Ctrl+End) |
| "copy source" | "copy from source" | Copy source to target |
| "select all" | "select everything" | Select all the text in the active segment (Ctrl+A) |
| "numbers" | "show numbers", "number words" | Number the words of the target, then say **"select 12"** or **"select 12 to 14"** – see [Select by number](/trados/voice-commands/dictation/#select-by-number) |
| "source numbers" | "number source words" | The same for the **source** segment |
| "clear target" | | Clear the target segment |
| "term one" … "term nine" | | Insert TermLens match 1–9 (with [capitalisation adaptation](/trados/termlens/#automatic-capitalisation)) |
| "match one" … "match nine" | | Apply Translation Results match 1–9 (Ctrl+1–9) |
| "term picker" | "pick term" | Open [TermPicker](/trados/termlens/termpicker/) |
| "term popup" | "show terms" | Open the [TermLens popup](/trados/termlens/termlens-popup/) |
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
* **Editor guard** – a keystroke command spoken while the cursor is in one of Supervertaler's own text boxes (the Assistant's chat box, say) is refused, and the SuperVoice pane says *put the cursor in the editor*. Studio's own boxes are not gated: Studio dispatches its shortcuts application-wide, so "confirm" with the cursor in Concordance search confirms the segment, exactly as pressing Ctrl+Enter there would.

### Customising commands

Click ⚙ in the SuperVoice pane, or right-click the 🎤 button in the TermLens header, to open the **SuperVoice settings** dialog (also reachable via the **?** in its title bar and **F1** for this help page):

<figure><img src="/.gitbook/assets/Supervertaler-for-Trados_Voice-command-settings.png" alt="The SuperVoice settings dialog with the full command grid"><figcaption>SuperVoice settings – every phrase, alias and action is editable</figcaption></figure>

* Enable/disable individual commands
* Edit spoken phrases and add aliases
* Add your own commands, mapped to either:
  * a **keystroke** chord sent to Studio (e.g. `ctrl+enter`, `alt+up`, `f3`) – any Studio or Supervertaler shortcut works
  * an **internal** plugin action: `insert_term_1`…`insert_term_9`, `term_picker`, `termlens_popup`, `navigate_next`, `navigate_previous`, `stop_listening`, `select_phrase`, `select_source_phrase`, `delete_selection`, `dictate_on`, `dictate_off`

A phrase containing `{phrase}` – as in `select {phrase}` – takes the words you say after it as its argument, rather than matching exactly. Only `select_phrase` and `select_source_phrase` use this.

:::note
After saving, the recogniser updates immediately – no restart needed.
:::

#### Choosing words for a command

The recogniser works from a closed vocabulary: your command phrases, plus the words of the segment you are in. It has no option to return nothing, so it always picks the best match from that list – which means **every word you add competes for that sound in every segment**, including against the words of your own translation.

The number of commands barely matters: a long list of distinctive phrases costs nothing. What costs you is a single command built from a short, everyday word.

* **Prefer distinctive words.** "insert tracked change" is free. A command called "to" or "for" is expensive, because it competes with those words wherever they appear in your text.
* **Untick what you do not use.** Disabled commands are removed from the vocabulary entirely, so turning off the "term …" or "match …" numbers you never reach makes the rest more reliable.
* **Watch for one word that will not select.** If [selecting](/trados/voice-commands/dictation/) a particular word keeps failing, the cause is usually a command phrase that sounds like it.

Homophones are the trap, not spelling. The built-in "term eight" and "match eight" commands put *eight* into the vocabulary of every segment, and *eight* sounds exactly like the article *a* – so for a while, "select a further" could not be made to work at all. Supervertaler now resolves the number words that have common homophones (*a/eight*, *to/two*, *for/four*, *one/won*) back to the word your segment actually contains, but a custom command can reintroduce the problem with a different word.

Commands are stored in `trados/settings/voice_commands.json` in your Supervertaler data folder, in the same format as Supervertaler Workbench's voice commands – so you can exchange command sets between the two products.

Default commands added in plugin updates are **merged into your saved set automatically** – your customisations are never touched. Because of this, if you want to get rid of a default command, **untick it rather than delete it** (a deleted phrase would come back if a later update re-ships it). **Restore defaults** replaces everything with the built-in set, discarding your customisations.

### Troubleshooting

* **"Voice commands could not start"** – check that a microphone is available in Windows sound settings, and that the first-run download completed (an interrupted download can be retried by simply starting voice commands again).
* **A command isn't recognised** – speak the phrase on its own, at normal pace. If a phrase never triggers, give it a more distinctive alias in Voice command settings.
* **Corrupt model** – delete the `trados/voice/models` folder in your Supervertaler data folder; the next activation re-downloads it.

### See Also

* [Dictation](/trados/voice-commands/dictation/)
* [Keyboard Shortcuts](/trados/keyboard-shortcuts/)
* [TermLens](/trados/termlens/)
* [TermPicker](/trados/termlens/termpicker/)

---
title: "SuperVoice"
---

**SuperVoice** is voice control for Trados Studio. It does three things, and they are one feature:

* **Commands** – "confirm", "next segment", "term three", "add term": drive Studio without touching the keyboard.
* **Selecting words** in the target or the source – by saying them, or by saying their **number** – so you can delete, replace, look up or add to a termbase whatever you just chose.
* **Handing the microphone to your dictation tool and back** – "dictate" … "stop now".

What SuperVoice does *not* do is write your translation. That is what a dictation tool is for – [Wispr Flow](https://wisprflow.ai/), Dragon, Windows Voice Access – and SuperVoice is built to work alongside one: it selects, deletes, undoes, hands over, takes back, and gets out of the way.

:::note[Commands are spoken in English]
Whatever languages your project is in, the commands themselves are English – "confirm", "select twelve", "source numbers" – and the recogniser is an English one. That is deliberate: one command language means one reliable command vocabulary, and the phrases are short and few. You can rename any command in SuperVoice settings, but the words you choose still have to be ones an English recogniser can hear. Command sets in other languages may follow if users ask for them.
:::

### Why a separate dictation tool

The two jobs need opposite things from a recogniser.

**Commands** need a closed vocabulary. SuperVoice's recogniser is given a short list of phrases and hears nothing else, which is what makes "confirm" fire instantly and reliably, and what stops your prose from triggering anything. It runs offline, on your machine – no audio ever leaves it.

**Prose** needs the opposite: an open vocabulary, punctuation, capitalisation, and – for most of us – a second language. That is a different kind of engine, and dictation tools already do it well.

So SuperVoice does not try to transcribe your translation. It stands on either side of the dictation: choosing what to replace before, cleaning up and confirming after.

### The SuperVoice pane

**View > SuperVoice** opens SuperVoice's own dockable pane: the microphone button, its state, and a list of what has been heard – newest at the top, each utterance beside what happened to it.

<figure><img src="/.gitbook/assets/Supervertaler-for-Trados_SuperVoice-pane.jpg" alt="The SuperVoice pane: microphone, state, and a list of utterances with what happened to each – selections in green, refusals in amber, ordinary speech in grey"><figcaption>The SuperVoice pane – what was heard, and what happened to it</figcaption></figure>

| Row colour | Meaning |
| ---------- | ------- |
| **Green** | A command ran, or words were selected |
| **Amber** | Understood but declined, with the reason – an ambiguous phrase, a word the model cannot hear |
| **Red** | A command that tried and failed |
| **Grey** | Ordinary speech that matched no command – not an error |

The pane opens on the right beside Translation Results, as a tab. The microphone's state is also always visible in the TermLens header; the pane holds the *history*, which you look at when something did not do what you expected. Drag it anywhere and Studio remembers. Sized to a few rows it always shows the last thing that happened; make it taller to see more.

### Starting and stopping

Three ways to toggle SuperVoice:

* Click the **🎤 microphone button** in the SuperVoice pane
* Click the **🎤 microphone button** in the TermLens panel header (next to the ↻ refresh button)
* Press **Ctrl+Alt+D** (also available in the editor right-click menu)

<figure><img src="/.gitbook/assets/Supervertaler-for-Trados_Voice-commands-button.png" alt="The microphone button in the TermLens header, green while listening"><figcaption>The 🎤 button in the TermLens header – green while listening</figcaption></figure>

| Colour | Meaning |
| ------ | ------- |
| **Grey** | Off – click to start |
| **Orange** | Starting (or downloading the voice runtime on first use) |
| **Green** | Listening |

:::note
**First activation** downloads the offline voice engine and a small English model (~50 MB, one-time) – progress is shown in the status label. Every later activation is instant.
:::

If neither the SuperVoice pane nor the TermLens panel is open, a small floating status strip appears instead (bottom-right). You can drag it anywhere – the position is remembered.

### Commands

Everything works out of the box – no configuration needed. Most commands also respond to an alias, so you can use whichever phrasing comes naturally:

| Say | Or | Action |
| --- | --- | ------ |
| "confirm" | "confirm segment" | Confirm segment and move to next unconfirmed |
| "next segment" | "go down" | Move to the next segment (without confirming) |
| "previous segment" | "go up" | Move to the previous segment |
| "go to the top" | "go to top" | Jump to the first segment (Ctrl+Home) |
| "go to the bottom" | "go to bottom" | Jump to the last segment (Ctrl+End) |
| "copy source" | "copy from source" | Copy source to target |
| "select all" | "select everything" | Select all the text in the active segment (Ctrl+A) |
| "clear target" | | Clear the target segment |
| "select …" | "choose …" | **Beta, off by default.** Select those words in the target – see [Selecting words](#selecting-words-by-saying-them) |
| "select source …" | "source select …" | **Beta, off by default.** Select those words in the **source** segment |
| "numbers" | "show numbers", "number words" | Number the words of the target, then say **"select 12"** or **"select 12 to 14"** – see [Select by number](#select-by-number) |
| "source numbers" | "number source words" | The same for the **source** segment |
| "delete that" | "delete this", "remove that" | Delete whatever is selected in the target |
| "undo that" | "scratch that", "undo" | Undo the last change (Ctrl+Z) |
| "dictate" | "start dictating" | Hand over to your dictation tool (**off by default** – see [Handing over](#handing-over-to-your-dictation-tool)) |
| "stop now" | "stop dictating" | Take dictation back (**off by default**) |
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
| "escape" | "close window" | Close the focused popup or dialog (and the number popup) |
| "stop listening" | "voice off" | Turn SuperVoice off |

#### One-time setup for "zoom in" / "zoom out"

Trados Studio's font-size actions ship **without a default keyboard shortcut**, so these two commands need a one-time binding:

1. Go to **File > Options > Keyboard Shortcuts > Editor**
2. Scroll down to the actions named simply **Increase** and **Decrease** (note: the Keyboard Shortcuts page has no search box – you have to scroll)
3. Set **Increase** to `Ctrl+Alt+PgUp` and **Decrease** to `Ctrl+Alt+PgDn`
4. Click **OK**

From then on, "zoom in" and "zoom out" control the editor font size hands-free. (Make sure **Adapt font sizes** is enabled under File > Options > Editor > Font Adaptation.)

### Selecting words by saying them

"select" is followed by the words you want, not by a fixed phrase: **"select the duty cycle"**, **"select sealing ring"**. While a segment is open, every word of its target is added to the recogniser's vocabulary, so it can hear the words that are actually in front of you. Then "delete that" deletes the selection, "undo that" puts it back, and "dictate" types over it.

:::caution[Selecting by saying the word is in beta]
Saying a word only works if the voice model knows the word – and in technical text, many of the words you most want are ones it does not know (on a real patent, about a third of the longer words). SuperVoice tells you when that is the case, and the fix is one step away: **[say the number](#select-by-number)**, which always works. Because of this, `select {phrase}` and `select source {phrase}` ship **switched off**; turn them on in SuperVoice settings when you want to try them.
:::

A few things worth knowing, because they explain what you will see:

* **Dropped words are tolerated.** Unstressed function words often do not survive recognition – "comprises at most" comes back as "comprises most". The selection widens to the segment's own text, so you still get *comprises at most*.
* **Whole words only.** Saying "select the" selects the standalone *the*, never the three letters inside *further*.
* **Say it again for the next one.** Where a phrase occurs more than once, the first is selected and the pane says **2 of 4 – say again for the next**. Repeating the same phrase steps to the next occurrence, and wraps round at the end. Naming more words works too.
* **"select" searches the target; "select source" searches the source.** Other segments and the termbase are never candidates.
* **When it cannot, it says why.** `"adsorbent" cannot be heard – not in the voice model's vocabulary`, or `"the" is inside another word – say more words`. A selection in a place you did not name would be worse than none, because "delete that" would act on it – so it never guesses.

:::note
"delete that" removes the space before the deleted words as well, where that is unambiguous, so deleting a word from the middle of a sentence does not leave a double space behind.
:::

#### Selecting in the source

`select source …` does the same thing in the **source** segment – useful for looking a term up, running a concordance, or adding a source/target pair to a termbase without touching the keyboard:

**"select source cockpitdisplay"** → **"select cockpit display"** → **"add term"**

It is **off by default**, because the source is usually in another language and needs a voice model for it. Tick **`select source {phrase}`** in SuperVoice settings; the first time you use it, the model for your project's source language downloads in the background (~40 MB, once) and the pane tells you when it is ready. Dutch is available today; other languages follow.

:::note
Source selection is **read-only**. "delete that" refuses a source selection, and so does starting dictation – deleting source text would damage the segment, its translation-memory match and the document's alignment. Everything genuinely useful on a source selection (lookup, concordance, add a term) reads rather than writes.
:::

**Long compounds.** In Dutch, German and other compounding languages, the word you want is often one the recogniser has never seen: these languages build words on demand, so no dictionary contains them all. SuperVoice offers the recogniser the *parts* of every long word in the segment and accepts any part as naming the whole, so **"select source bescherming"** selects `beschermingsperiode`. A word with no recognisable part at all still cannot be said – and that is what the numbers are for.

### Select by number

The words the voice model cannot hear are, in a technical text, most of the ones you want. For those you say a **number** instead of the word:

1. Say **"numbers"**. A small popup shows the target segment as it reads, each word followed by a small number – a hyphenated compound counts as one word – with the words the model cannot hear marked in yellow. **"source numbers"** does the same for the source.
2. Say **"select 12"** to select word 12, or **"select 12 to 14"** for the span from 12 to 14 – it keeps whatever lies between. The popup closes.
3. **"cancel"**, **"escape"**, the Escape key, or the × closes it without selecting.

The popup also opens **by itself** when a selection fails because the word is not in the model's vocabulary – the pane says *"…" cannot be heard*, and the numbers appear with that reason as their title. Say the number. (It does not open while you are dictating, or while Studio is not the active window.)

**Yellow means: say the number. Everything else: say the word or the number, as you like.** Either way the popup closes once the selection lands.

Two layouts, switched from the link in the popup's own corner and remembered: **sentence** (the segment as continuous text, numbers as footnotes – the default) and **chips** (number then word, on a grid). The popup never takes focus, so the caret stays in the editor. The number words are only in the recogniser's vocabulary while it is open. Words are numbered past 99, but only 1–99 can be said.

### Handing over to your dictation tool

Two commands: **"dictate"** starts your dictation tool and stands aside while you talk; **"stop now"** takes it back. They are separate on purpose – saying either one twice is harmless, whereas a single toggle would silently start dictation when you meant to stop it. Both ship **switched off**, because they drive a tool most installations do not have – switch them on in SuperVoice settings once you have done the setup below.

While dictation is running, SuperVoice ignores every command except the way back out (and "stop listening", which always works). This is the part a general-purpose macro tool cannot do: because it was *your command* that started the dictation, SuperVoice knows you are in it, and a translation containing the word "confirm" cannot fire a command into your document mid-sentence.

:::tip
Dictating into Studio *without* saying "dictate" first works too – but then every command is live while you talk, and prose containing "select" or "confirm" will do exactly that. If you are about to dictate at length, say "dictate" first.
:::

#### Setup, with Wispr Flow as the example

Everything here works with any dictation tool. [Wispr Flow](https://wisprflow.ai/) is the one the feature was built and tested against, so it is used for the worked example, but Dragon, Windows Voice Access and the rest follow the same three steps.

**1. Give the dictation tool a hands-free shortcut.** The "dictate" command is shipped expecting **Ctrl+Win+Space**, which is one of Wispr Flow's own hands-free defaults, so there is usually nothing to change. Push-to-talk will not do – it needs a key held down, and the point here is not to touch the keyboard.

**2. Teach it to write a marker for your stop phrase.** When you say "stop now", the dictation tool is still listening, so the word lands in your text. Rather than trying to guess and delete it, have the tool write a fixed marker instead:

* In Wispr Flow, open **Dictionary** and add an entry mapping **stop now** to **ZZEND**.

SuperVoice waits for `ZZEND` to appear and removes it, along with the space before it. A marker is used rather than an empty replacement for two reasons: most tools will not map a phrase to nothing, and a marker is far more reliable – spoken, your stop word arrives formatted, capitalised and punctuated (`. Stop now.`), and every one of those variants collapses into one fixed string.

**3. Switch both commands on.** Click ⚙ in the SuperVoice pane → tick **dictate** and **stop now**.

If your tool uses a different shortcut, or a different marker, edit the command's action rather than any settings screen: it reads `dictate_on:ctrl+win+space:ZZEND` on the start command and `dictate_off:ctrl+win+space:ZZEND` on the stop command – trigger first, marker second. `middleclick` is accepted as a trigger for a tool that listens for a middle click.

### Putting it together

A correction, hands-free, start to finish:

1. **"select the duty cycle"** – the words highlight in the target (or **"numbers"** … **"select 7 to 8"** if the model cannot hear them)
2. **"dictate"** – your dictation tool starts listening
3. *"the duty factor"* – it types over the selection
4. **"stop now"** – it stops, the marker is cleaned up
5. **"confirm"** – segment confirmed, on to the next

If step 3 comes out wrong, **"undo that"** puts it back.

### Safety and privacy

* **Fully offline** – recognition runs locally on your machine (Vosk engine); no audio is ever sent anywhere.
* **Grammar-constrained** – the recogniser listens *only* for your command phrases and the words of the open segment, which is what makes commands fast and reliable. Speech that matches nothing is ignored.
* **Foreground guard** – commands only execute while Trados Studio is the active window. Speaking in another app can't trigger anything ("stop listening" is the one exception – it always works).
* **Editor guard** – a keystroke command spoken while the cursor is in one of Supervertaler's own text boxes (the Assistant's chat box, say) is refused, and the pane says *put the cursor in the editor*. Studio's own boxes are not gated: Studio dispatches its shortcuts application-wide, so "confirm" with the cursor in Concordance search confirms the segment, exactly as pressing Ctrl+Enter there would.

### Customising commands

Click ⚙ in the SuperVoice pane, or right-click the 🎤 button in the TermLens header, to open the **SuperVoice settings** dialog (also reachable via the **?** in its title bar and **F1** for this help page):

<figure><img src="/.gitbook/assets/Supervertaler-for-Trados_Voice-command-settings.png" alt="The SuperVoice settings dialog with the full command grid"><figcaption>SuperVoice settings – every phrase, alias and action is editable</figcaption></figure>

* Enable/disable individual commands
* Edit spoken phrases and add aliases
* Add your own commands, mapped to either:
  * a **keystroke** chord sent to Studio (e.g. `ctrl+enter`, `alt+up`, `f3`) – any Studio or Supervertaler shortcut works
  * an **internal** plugin action: `insert_term_1`…`insert_term_9`, `term_picker`, `termlens_popup`, `navigate_next`, `navigate_previous`, `stop_listening`, `select_phrase`, `select_source_phrase`, `delete_selection`, `number_words`, `number_source_words`, `dictate_on`, `dictate_off`

A phrase containing `{phrase}` – as in `select {phrase}` – takes the words you say after it as its argument, rather than matching exactly. Only `select_phrase` and `select_source_phrase` use this.

:::note
After saving, the recogniser updates immediately – no restart needed.
:::

#### Choosing words for a command

The recogniser works from a closed vocabulary: your command phrases, plus the words of the segment you are in. It has no option to return nothing, so it always picks the best match from that list – which means **every word you add competes for that sound in every segment**, including against the words of your own translation.

The number of commands barely matters: a long list of distinctive phrases costs nothing. What costs you is a single command built from a short, everyday word.

* **Prefer distinctive words.** "insert tracked change" is free. A command called "to" or "for" is expensive, because it competes with those words wherever they appear in your text.
* **Untick what you do not use.** Disabled commands are removed from the vocabulary entirely, so turning off the "term …" or "match …" numbers you never reach makes the rest more reliable.
* **Watch for one word that will not select.** If selecting a particular word keeps failing, the cause is usually a command phrase that sounds like it.

Homophones are the trap, not spelling. The built-in "term eight" and "match eight" commands put *eight* into the vocabulary of every segment, and *eight* sounds exactly like the article *a* – so for a while, "select a further" could not be made to work at all. SuperVoice now resolves the number words that have common homophones (*a/eight*, *to/two*, *for/four*, *one/won*) back to the word your segment actually contains, but a custom command can reintroduce the problem with a different word.

Commands are stored in `trados/settings/voice_commands.json` in your Supervertaler data folder, in the same format as Supervertaler Workbench's voice commands – so you can exchange command sets between the two products.

Default commands added in plugin updates are **merged into your saved set automatically** – your customisations are never touched. Because of this, if you want to get rid of a default command, **untick it rather than delete it** (a deleted phrase would come back if a later update re-ships it). **Restore defaults** replaces everything with the built-in set, discarding your customisations.

### Limitations

* **The stop phrase must be distinct from your prose.** It is a word your dictation tool is listening for, so choosing a word you dictate often will bite you.
* **A word buried in an earlier word, at the very end of a segment, cannot be selected by saying it.** There is nothing after it to tell the two apart. Say two words, or its number.
* **Selection follows the active segment.** Move to another segment and the vocabulary – and the number popup – change with it.
* **A word the recogniser has never seen cannot be selected by saying it.** Say its number.

### Troubleshooting

* **"Voice commands could not start"** – check that a microphone is available in Windows sound settings, and that the first-run download completed (an interrupted download can be retried by simply starting SuperVoice again).
* **A command isn't recognised** – speak the phrase on its own, at normal pace. If a phrase never triggers, give it a more distinctive alias in SuperVoice settings.
* **A word won't select** – look at the pane: it says why. If it says the word cannot be heard, say **"numbers"** and its number.
* **Corrupt model** – delete the `trados/voice/models` folder in your Supervertaler data folder; the next activation re-downloads it.

### See Also

* [Keyboard Shortcuts](/trados/keyboard-shortcuts/)
* [TermLens](/trados/termlens/)
* [TermPicker](/trados/termlens/termpicker/)

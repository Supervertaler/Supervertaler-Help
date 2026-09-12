---
title: "Dictation"
---

:::note
This page builds on **[Voice Commands](/trados/voice-commands/)** – start there for turning voice on, the microphone button, the full command list and how to customise commands.
:::

Voice commands drive Trados Studio. A dictation tool writes your translation. This page is about the seam between the two – selecting words you have just dictated, replacing them, and handing the microphone back and forth without touching the keyboard.

Everything here works with any dictation tool. [Wispr Flow](https://wisprflow.ai/) is the one the feature was built and tested against, so it is used for the worked example, but Dragon, Windows Voice Access and the rest follow the same three setup steps.

### Why two tools at all

The two jobs need opposite things from a recogniser.

**Commands** need a closed vocabulary. Supervertaler's recogniser is given a short list of phrases and hears nothing else, which is what makes "confirm" fire instantly and reliably, and what stops your prose from triggering anything. It runs offline, on your machine.

**Prose** needs the opposite: an open vocabulary, punctuation, capitalisation, and – for most of us – a second language. That is a different kind of engine, and dictation tools already do it well.

So Supervertaler does not try to transcribe your translation. It selects, deletes, undoes, and gets out of the way.

### Editing what you just dictated

Three commands, all on by default:

| Say | Or | Action |
| --- | --- | ------ |
| "select …" | "choose …" | Select those words in the target segment |
| "select source …" | "source …" | Select those words in the **source** segment (off by default – see below) |
| "delete that" | "delete this", "remove that" | Delete whatever is selected |
| "undo that" | "scratch that", "undo" | Undo the last change (Ctrl+Z) |

"select" is followed by the words you want, not by a fixed phrase: **"select the duty cycle"**, **"select sealing ring"**. While a segment is open, every word of its target is added to the recogniser's vocabulary, so it can hear the words that are actually in front of you.

A few things worth knowing, because they explain what you will see:

* **Dropped words are tolerated.** Unstressed function words often do not survive recognition – "comprises at most" comes back as "comprises most". The selection widens to the segment's own text, so you still get *comprises at most*.
* **Whole words only.** Saying "select the" selects the standalone *the*, never the three letters inside *further*.
* **Say it again for the next one.** Where a phrase occurs more than once, the first is selected and the status strip says **2 of 4 – say again for the next**. Repeating the same phrase steps to the next occurrence, and wraps round at the end. Naming more words works too.
* **It only searches the target.** Source text, other segments and the termbase are not candidates.

If a phrase cannot be selected, the status strip says why rather than doing nothing – `no "confirm" in this segment`, or `"the" is inside another word – say more words`. A selection in a place you did not name would be worse than none, because "delete that" would act on it.

:::note
"delete that" removes the space before the deleted words as well, where that is unambiguous, so deleting a word from the middle of a sentence does not leave a double space behind.
:::

### Selecting in the source

`select source …` does the same thing in the **source** segment – useful for looking a term up, running a concordance, or adding a source/target pair to a termbase without touching the keyboard:

**"select source cockpitdisplay"** → **"select cockpit display"** → **"add term"**

It is **off by default**, because the source is usually in another language and needs a voice model for it. Tick **`select source {phrase}`** in Voice command settings; the first time you use it, the model for your project's source language downloads in the background (~40 MB, once) and the status strip tells you when it is ready.

:::note
Source selection is **read-only**. "delete that" refuses a source selection, and so does starting dictation – deleting source text would damage the segment, its translation-memory match and the document's alignment. Everything genuinely useful on a source selection (lookup, concordance, add a term) reads rather than writes.
:::

#### Long compounds

In Dutch, German and other compounding languages, the word you want is often one the recogniser has never seen: languages like these build words on demand, so no dictionary contains them all. `beschermingsperiode` and `infraroodtouchscreens` are not in any Vosk Dutch model, large or small – this is a property of the language, not a limitation to be fixed with a bigger download.

Supervertaler works around it by offering the recogniser the *parts* of every long word in the segment, and accepting any part as naming the whole word. So **"select source bescherming"** selects `beschermingsperiode`, and saying the compound naturally works too, because whichever part is heard is enough.

A word with no recognisable part at all – a foreign loanword, typically – still cannot be selected. Name a neighbouring word instead.

### Handing over to a dictation tool

The **"dictate"** command starts your dictation tool, stands aside while you talk, and stops it when you say "dictate" again. It ships **switched off**, because it drives a tool most installations do not have – switch it on in Voice command settings once you have done the setup below.

While dictation is running, Supervertaler ignores every command except the way back out (and "stop listening", which always works). This is the part a general-purpose macro tool cannot do: because it was *your command* that started the dictation, Supervertaler knows you are in it, and a translation containing the word "confirm" cannot fire a command into your document mid-sentence.

#### Setup, with Wispr Flow as the example

**1. Give the dictation tool a hands-free shortcut.** The "dictate" command is shipped expecting **Ctrl+Win+Space**, which is one of Wispr Flow's own hands-free defaults, so there is usually nothing to change. Push-to-talk will not do – it needs a key held down, and the point here is not to touch the keyboard.

**2. Teach it to write a marker for your stop phrase.** When you say "dictate" to stop, the dictation tool is still listening, so the word lands in your text. Rather than trying to guess and delete it, have the tool write a fixed marker instead:

* In Wispr Flow, open **Dictionary** and add an entry mapping **dictate** to **ZZEND**.

Supervertaler waits for `ZZEND` to appear and removes it, along with the space before it. A marker is used rather than an empty replacement for two reasons: most tools will not map a phrase to nothing, and a marker is far more reliable – spoken, your stop word arrives formatted, capitalised and punctuated (`. Dictate.`), and every one of those variants collapses into one fixed string you can search for.

**3. Switch the command on.** Right-click the 🎤 button → **Voice command settings** → tick **dictate**.

If your tool uses a different shortcut, or a different marker, edit the command's action rather than any settings screen: it reads `dictate_toggle:ctrl+win+space:ZZEND` – trigger first, marker second. `dictate_toggle:middleclick` is accepted for a tool that listens for a middle click.

### Putting it together

A correction, hands-free, start to finish:

1. **"select the duty cycle"** – the words highlight in the target
2. **"dictate"** – your dictation tool starts listening
3. *"the duty factor"* – it types over the selection
4. **"dictate"** – it stops, the marker is cleaned up
5. **"confirm"** – segment confirmed, on to the next

If step 3 comes out wrong, **"undo that"** puts it back.

### Limitations

* **The stop phrase must be distinct from your prose.** It is a word your dictation tool is listening for, so choosing a word you dictate often will bite you.
* **A word buried in an earlier word, at the very end of a segment, cannot be selected.** There is nothing after it to tell the two apart. Say two words instead.
* **Selection follows the active segment.** Move to another segment and the vocabulary changes with it.
* **A word the recogniser has never seen cannot be selected**, and nor can a compound none of whose parts it knows. Name a word next to it instead.
* **The status strip is the feedback channel.** Keep the TermLens panel open, or use the floating strip, so you can see what was heard and what happened.

### See Also

* [Voice Commands](/trados/voice-commands/)
* [Keyboard Shortcuts](/trados/keyboard-shortcuts/)
* [TermLens](/trados/termlens/)

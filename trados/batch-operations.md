---
title: "Batch Operations"
---

The **Batch Operations** tab in the Supervertaler Assistant panel provides two AI-powered modes for processing multiple segments at once:

| Mode | Description |
|------|-------------|
| **[Batch Translate](/trados/batch-translate/)** | Translate segments using AI with customisable prompts |
| **[AI Proofreader](/trados/ai-proofreader/)** | Check translations for errors, inconsistencies, and style issues |

Switch between modes using the **Mode** dropdown at the top of the Batch Operations tab.

Both modes share the same prompt selector, provider/model configuration, and scope options. Prompts are filtered by mode – Translate prompts appear in Translate mode, Proofread prompts appear in Proofread mode. You can click the **provider/model label** to quickly switch AI models via a flyout menu – the same menu available in the Chat tab.

### Clipboard Mode

Both Translate and Proofread modes support **[Clipboard Mode](/trados/clipboard-mode/)** – an alternative workflow that lets you use any web-based AI (ChatGPT, Claude, Gemini, etc.) without an API key. Tick the **Clipboard Mode** checkbox to switch from API-based processing to a manual copy/paste workflow. See [Clipboard Mode](/trados/clipboard-mode/) for full details.

### Preview prompt

Next to the action button, the **👁 Preview prompt** link opens a read-only dialog showing **exactly what would be sent to the AI** for the current configuration: the assembled system prompt (including the active custom prompt, termbase entries, language-specific checks, and the full bilingual document context for proofread), followed by the numbered segment list. No LLM call is made.

This is useful for:

* **Sanity-checking before an expensive call** – see what the model will actually receive (including how many tokens of context, whether your termbase is being included, whether the right segments are in scope) before clicking Translate / Proofread.
* **Debugging unexpected output** – if the AI produces an odd suggestion, the preview shows you the exact prompt the model was answering, so you can see whether the issue is in your custom prompt, the termbase, the document context, or the segment list.
* **Manually pasting into a web LLM** – the dialog has its own *Copy to clipboard* button, so you can use it as a one-shot "send this to ChatGPT/Claude/Gemini" path without toggling Clipboard Mode.

The preview works in both **API mode** and **Clipboard Mode** without switching, and is available for both Translate and Proofread.

### SuperBench

Next to Preview prompt, the **⚖ SuperBench…** link (from v18.20.187) translates the first segments of the document with three models under exactly these batch settings and has a judge compare them blind, with a recommendation for this project. Nothing is written to the document. See [SuperBench](/trados/superbench/).

### List numbering as structure context

Word's claim numbers, lettered steps and bullets are not segment text, so the AI used to never see them. Since v18.20.188 (always on from v18.20.189; see [AI Settings](/trados/settings/ai-settings/#list-numbering-as-structure-context-from-v1820188-always-on-from-v1820189)), Batch Translate prefixes the first segment of each numbered paragraph with its marker inside a sentinel – `[#e)]`, `[#9.]` – and tells the model it is structure, never to be reproduced. The log reports how many markers were found, and any marker the model echoes back is removed before the target is written. Preview prompt shows the markers as they will be sent.

### Reference numbers in the text

Technical documents – patents, manuals, specifications – point at parts of a drawing with numbers in brackets: "the valve (12) is connected to the pipe (3a)". The **№ Reference numbers in the text** link lists every such number in the open document, how often it is used, and the sentence that first mentions it. It reads the whole document regardless of the Scope setting, makes no AI call, and opens the list in the Chat tab. A document without such numbers simply says so. Useful for spotting a number that is cited once and never explained, or a part that changes number halfway through.

### Images (from v18.20.189)

The images that belong to a document are often not in the file you translate – a manual's diagrams in a separate file, a patent's drawings in a "figures as filed" document beside the project – and what each one shows exists only as pixels. The **▣ Images…** link opens a panel for that pipeline:

* **Folder** – the reference images folder for this project, remembered per Trados project. **Browse…** to set it.
* **Found** – the Word documents beside the project, how many images each holds, how many carry a figure label, and how the labels were established (paired by position and checked, taken from nearby text, or withheld when they could not be verified).
* **Extract images to folder** – writes the images into the folder, named for their figures (`Figure 01.png`, zero-padded so they sort). Free, no AI call. Re-running overwrites.
* **Analyse with AI** – shows each image to the AI together with what the document says about it, compares the reference signs it reads against the signs the text cites, and writes the result to `figures.md` in the active memory bank. Costs one AI request per image; the button says how many and to which provider before you click. Asks before replacing an existing `figures.md`, and refuses to start a second run while one is going.
* **Write figures.md** – writes the inventory from the document's own text alone, without looking at the drawings. Free. Useful before any AI pass, and the column that needs a model to look at the drawings is named as missing rather than left to look complete.
* The last line says when `figures.md` was last written, how many figures it holds and whether the AI has looked at them yet. It sits at the memory bank's root, so it is read into every prompt.

Buttons that cannot run yet say why: no folder set, no images found, or no active memory bank. The **Document images report** link at the bottom opens the full per-image listing in the Chat tab. **Reference numbers in the text** stays a separate link above, because it is a check on the text, not part of this pipeline.

### AutoPrompt

The Batch Operations tab also includes an **[AutoPrompt](/trados/generate-prompt/)** link that uses AI to create a comprehensive, domain-specific translation prompt based on your project's content, terminology, and TM data.

## See Also

* [Clipboard Mode](/trados/clipboard-mode/)
* [SuperBench](/trados/superbench/)
* [AutoPrompt](/trados/generate-prompt/)
* [Prompts](/trados/settings/prompts/)
* [AI Settings](/trados/settings/ai-settings/)
* [Keyboard Shortcuts](/trados/keyboard-shortcuts/)

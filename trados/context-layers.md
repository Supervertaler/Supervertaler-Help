---
title: "Context layers"
description: "The ten layers of context Supervertaler for Trados puts in front of the AI, what each one adds, and how to control them."
---

A translation engine that sees only the sentence in front of it will translate that sentence well and the document badly. Supervertaler's design is the opposite: every time you send a chat message, translate a batch of segments, or ask AutoPrompt to draft a prompt, it assembles a fresh snapshot of your work and hands the whole thing to the AI.

That snapshot is built in **layers**. Some come from Trados, some from your own knowledge, and two of them come from parts of the document that no CAT tool normally shows you at all. They stack, and each one that is present removes a class of mistake the AI would otherwise make.

This page is the single place that lists every layer. Each section is a short overview with a link to the feature's own page.

## The ten layers

| # | Layer | Where it comes from | On by default |
|---|-------|---------------------|---------------|
| 1 | Project and file information | Trados | always |
| 2 | Current segment | Trados | always |
| 3 | Surrounding segments | Trados | always |
| 4 | Full document content | Trados | yes |
| 5 | A translation memory match | your TMs | yes, outside batch |
| 6 | Termbase terms | your termbases | yes |
| 7 | SuperMemory | what you have recorded about the client | yes, when a bank is active |
| 8 | List numbering | the Word file inside the sdlxliff | yes, from v18.20.189 |
| 9 | Figure descriptions | the images in your documents | after two clicks in FigureLens |
| 10 | Attached files | you, per chat turn | when you attach something |

Layers 1 to 8 need no work from you at all (layer 5 only where Studio has already put a TM hit in the segment). Layer 9 is two clicks per project. Layer 10 is deliberate.

### 1. Project and file information

Which project and file you are in, the language pair (e.g. Dutch → English), and your position in the document ("Segment 42 of 318"). Always included; no toggle.

### 2. Current segment

The source text you are translating and any target you have already entered. Always included – the minimum context for most AI operations.

### 3. Surrounding segments

Two segments before and two after, with their translations where available. This is what lets the AI resolve a pronoun the way the previous sentence resolved it, or continue a clause that began in the segment above. Always included; the window is fixed.

### 4. Full document content

All source segments in the current document, so the assistant can judge what kind of document it is – legal, medical, technical, marketing, financial, scientific – and let that inform its terminology and register.

Very long documents are truncated to a configured maximum (default 500 segments), keeping the first 80 % and the last 20 % so the beginning and the end both survive.

**Toggle:** AI Settings → *Include full document content*.

### 5. A translation memory match

Where Studio has already put a TM hit in the segment – a pre-translated or auto-propagated row – its source, its target and its match percentage go to the AI as reference material from your own past work, so it can stay consistent with how you rendered that phrase last time.

Two limits worth knowing, because they are easy to assume away:

- It is the **one** match Studio left on the segment, not a search of your TMs for the best few. A segment with no TM origin contributes nothing here.
- It applies to **Chat, QuickLauncher and AutoPrompt**. Batch Translate does not send it; there, consistency with your past work comes from the termbase, SuperMemory and the document itself.

**Toggle:** AI Settings → *Include TM matches*.

### 6. Termbase terms

Matched terms from your active termbases, with approved translations and synonyms, and optionally definitions, domains and usage notes. Non-translatable and forbidden terms are flagged so the AI respects them.

Both Supervertaler termbases and MultiTerm `.sdltb` termbases attached to the project contribute. See [TermLens](/trados/termlens/) and [MultiTerm Support](/trados/multiterm-support/).

**Toggles:** AI Settings → *Include termbase terms* / *Include term metadata* / the per-termbase contribution list.

### 7. SuperMemory

[**SuperMemory**](/trados/ai-assistant/super-memory/) is where you record the things about a client that cannot be looked up. If a bank is active, its files go out with every AI call:

- `brief.md` – who the client is and anything standing
- `terminology.md` – term decisions, one table
- `style.md` – prose rules and approved boilerplate

The `_shared` bank is sent alongside as house defaults, and the active bank is marked as overriding it where the two disagree.

Where a termbase gives the AI flat pairs of terms, SuperMemory gives it the **reasoning** behind them: the decisions, the caveats, the client-specific overrides. Only the active bank is used (plus `_shared`), so switch to the right one before translating.

**Toggles:** AI Settings → *Include memory bank context* / *Use memory bank in AutoPrompt*.

### 8. List numbering

Word numbers claims, letters steps and bullets lists as paragraph properties, not as text – so the segment grid never contains the `a)` or the `9.`, and neither did anything the AI received. On a real patent that produced a model reading six unlettered steps, translating "steps a. to f." faithfully, and then flagging it as a possible defect in the source: a note that would have reached the client.

Batch Translate, Translate Segment, Clipboard Mode and SuperBench now prefix the first segment of each numbered paragraph with the marker Word renders, inside a sentinel – `[#e)]`, `[#9.]`, `[#•]` – and a rule in Supervertaler's own preamble tells the model it is structure, to be used for cross-references and parallelism and never reproduced. Anything the model echoes back is stripped before the target is written.

The markers are read from the original Word file Studio keeps inside the sdlxliff and computed for the whole document at once, so a list restarting at claim 11 reads `11.` and lettered steps that continue across claims keep counting, exactly as Word shows them. Always on from v18.20.189; see [Batch Operations](/trados/batch-operations/#list-numbering-as-structure-context).

### 9. Figure descriptions

The AI reads your text and cannot see your pictures. [**FigureLens**](/trados/batch-operations/#figurelens-from-v1820189) closes that gap: it takes the images out of the project's Word documents into a folder, shows each one to the AI together with what the document says about it, and saves a description – what it shows, which figure it is, which parts and reference numbers appear on it – as `figures.md` in the active memory bank.

From then on it rides along with layer 7 and is read with every request, so the model knows that the "valve (12)" in the sentence is the thing at the top right of Figure 3. Vector drawings (EMF, WMF – what a drawing placed from CAD usually is) are rendered to PNG on the way out, because no AI can read a metafile.

Two clicks per project, then it is automatic. One AI request per image; the button says how many and to which provider before you click, and **Describe from the text only** is a free alternative that uses what the document itself says about each figure.

### 10. Attached files

Files you attach to a chat turn – images by paste, drag-drop or browse, and documents (DOCX, PDF, PPTX, XLSX, CSV, TMX, SDLXLIFF, TBX, TXT, Markdown, HTML and more). Images go through each provider's vision API; documents are text-extracted and appended.

Attachments apply only to the turn you attached them on. See [File Attachments](/trados/ai-assistant/file-attachments/).

## Stacking the layers

All ten combine freely, and the default composition – everything above except the two that need a click – is a strong baseline and the one to start from.

More context is not automatically better, though. The context window is finite, and a large project with a rich termbase and a mature memory bank can push a prompt into the 50 000–100 000-token range. At some point:

- adding **TM matches** on top of a memory bank that already knows the client's preferred wordings may add noise rather than signal;
- including **full document content** for a very long document may leave too little room for the memory bank to load;
- layering **three overlapping sources** (TM + termbase + memory bank) on the same concept may produce contradictions the AI has to reconcile on the fly.

:::note
**Composing tip:** for a client where you have a well-built memory bank, try a small batch with TM matches disabled and compare it to a run with everything enabled. The cleaner prompt often gives more consistent terminology, because the bank already knows which wording the client prefers and the TM matches add nothing it does not say better. For unfamiliar domains or one-off jobs, keep everything on – the TM and termbase are carrying the weight there.
:::

The four layers that describe the *document* rather than the *client* – 3, 4, 8 and 9 – behave differently: they are cheap, they never contradict each other, and there is no case yet found where turning one off improved a translation.

:::caution
We have not published composition presets (e.g. "Mature client – memory bank only", "Unfamiliar domain – TM + termbase"). Until we do, leave everything enabled and experiment per project. If you find a configuration that works well, say so in [GitHub Discussions](https://github.com/orgs/Supervertaler/discussions).
:::

## Seeing and controlling the layers

To see exactly what is being sent, click **👁 Preview prompt** next to the Translate button on the Batch Operations tab. It opens a read-only dialog with the assembled prompt – every layer, in the order the model receives it – and makes no AI call.

To change what is sent, open the settings dialog's **AI Settings** tab, where you can toggle document content, TM matches, term metadata and memory bank context, and choose which termbases contribute.

## See Also

- [Supervertaler Assistant](/trados/ai-assistant/) – overview
- [Batch Operations](/trados/batch-operations/) – Preview prompt, FigureLens, list numbering
- [AI Settings](/trados/settings/ai-settings/) – the toggles
- [SuperMemory](/trados/ai-assistant/super-memory/) – the client decisions you record by hand
- [SuperMemory → AI Integration](/trados/ai-assistant/super-memory/ai-integration/) – the loading algorithm and token budget
- [File Attachments](/trados/ai-assistant/file-attachments/) – add images and documents to a chat turn
- [TermLens](/trados/termlens/) – how termbase terms are matched and loaded

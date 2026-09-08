---
title: "Context layers"
description: "The layers of context Supervertaler for memoQ puts in front of the AI, what each one adds, where memoQ lets it come from, and how to control them."
---

A translation engine that sees only the sentence in front of it will translate that sentence well and the document badly. Supervertaler's design is the opposite: every time memoQ asks it for a translation, it assembles a fresh snapshot of your work and hands the whole thing to the AI.

That snapshot is built in **layers**. Some come from memoQ, some from your own recorded knowledge, and two of them come from parts of the document that no CAT tool normally shows you at all. They stack, and each one that is present removes a class of mistake the AI would otherwise make.

This page is the single place that lists every layer. Supervertaler for Trados has [its own version of this page](/trados/context-layers/); the ideas are the same and the sources differ, because memoQ hands a plugin a different set of things.

## The layers

| # | Layer | Where it comes from | Needs work from you |
|---|-------|---------------------|---------------------|
| 1 | Project and job information | memoQ, with each request | no |
| 2 | The segment being translated | memoQ | no |
| 3 | Segments you have confirmed | your own confirmed rows | one setting, once |
| 4 | The closest translation memory match | your TMs, routed by you | one setting, once |
| 5 | Whether the row was rejected | memoQ | no |
| 6 | Glossary terms and forbidden terms | your glossary | a glossary |
| 7 | SuperMemory memory banks | what you have recorded about the client | a bank per client |
| 8 | List numbering | the original Word file | the live document link |
| 9 | Figure descriptions | the images in your documents | two clicks in FigureLens |
| 10 | The whole document | the live document link | for AutoPrompt only |

### 1. Project and job information

The client, domain and subject recorded in memoQ's project, the language pair, and which document the segment is in. memoQ sends these with every translation request, so they need no setting – but they are only as good as what the project manager filled in. An empty *Client* field in memoQ is an empty line in the prompt.

**Toggle:** Translation settings → *Send surrounding segments and project metadata to the model*.

### 2. The segment being translated

The source text, with its inline tags preserved so they can be put back in the right places. Always included; there is nothing to configure.

### 3. Segments you have confirmed

Every segment you confirm is recorded, and the most lexically similar ones are shown to the model when it translates later segments of the same document. Confirm *electric module* once and the rest of the document follows.

This is memoQ's answer to a layer Trados gets for free. A Trados plugin is handed the segments surrounding the one it is translating; a memoQ MT plugin is not – memoQ reserves that channel for its own AGT engine – so Supervertaler builds the equivalent out of your confirmed work instead. It is arguably the better trade: every example is one you approved, rather than merely one that happens to be nearby.

memoQ only sends confirmations to an engine selected under **Self-learning MT**, so that box must be ticked as well as the engine being chosen for translation. Until it is, nothing is captured and the [Activity window](/memoq/prompt-editor/#the-activity-window) says so. See [Self-learning](/memoq/self-learning/).

**Toggle:** Translation settings → *Send surrounding segments and project metadata to the model*.

### 4. The closest translation memory match

memoQ can forward the best fuzzy match for a segment to an MT engine, and when you route it to Supervertaler that match goes into the prompt ahead of everything else – presented as the thing to adapt rather than as background reading, because a human wrote and approved it for a nearly identical source.

Set it in memoQ under **Edit machine translation settings → Send best fuzzy TM match to → Supervertaler**. It is deliberately *not* governed by the document-context toggle: a match you went out of your way to route here should not disappear because you turned off surrounding context.

Two things to know about its shape. It is **one** match per segment – memoQ forwards the single best one, which is what its own setting says – rather than a set to choose among. And memoQ hands over the two segments without a match rate, so the prompt cannot tell the model *how* close the match is; it is described as the closest approved rendering, and the model judges the difference from the text itself. The match is forwarded for every segment memoQ asks about, batches included.

### 5. Whether the row was rejected

memoQ tells the plugin each row's translation state. When you have rejected a previous translation of a segment, the prompt says so and instructs the model to reconsider the terminology, structure and register rather than paraphrase what you refused. No setting; it simply happens on a row you marked rejected.

### 6. Glossary terms and forbidden terms

Terms matched in the segment, with their approved renderings, and any terms marked forbidden. Forbidden terms are enforced rather than merely displayed.

Worth being precise about the source, because the setting's wording is optimistic: these come from **Supervertaler's own glossary** – the tab-separated file the [terminology plugin](/memoq/terminology/) reads – not from memoQ's term bases. memoQ passes termbase hits to an MT plugin only through the rich lookup channel it reserves for its own engine, so a third-party plugin never receives them. Your memoQ term bases still work normally in the grid; they just do not reach the model. [Export glossary](/memoq/prompt-editor/#export-glossary-the-prompts-terms-as-the-project-glossary) is the bridge: it turns a drafted prompt's locked terms into a glossary Supervertaler does read.

While an AutoPrompt-drafted prompt is selected, its own locked-terms table is the authority and the glossary's preferred renderings are held back – forbidden terms always travel.

**Toggle:** Translation settings → *Send memoQ's termbase hits and forbidden terms to the model*.

### 7. SuperMemory memory banks

A bank of Markdown articles – `brief.md`, `terminology.md`, `style.md`, and any others you add – goes out with every request, up to about 32,000 tokens, and to AutoPrompt up to 40,000.

Where a glossary gives the model flat pairs of terms, a memory bank gives it the **reasoning**: the decisions, the caveats, the client-specific overrides. The `_shared` bank travels alongside as house defaults.

Banks are remembered per memoQ project, and a project you have never chosen one for uses none rather than inheriting the last – a bank carries one client's terminology, and the wrong one is worse than none. See [Memory banks](/memoq/mcp-server/#memory-banks).

### 8. List numbering

Word numbers claims, letters steps and bullets lists as paragraph properties, not as text, so memoQ's grid never contains the `a)` or the `9.` and neither did anything the model received. Shown six unlettered steps and then *"steps a. to f."*, a model will flag the reference as a possible defect in the source – a note that would have reached the client.

Supervertaler reads the numbering out of the original `.docx`, counted over the whole document exactly as Word renders it, and sends each paragraph's marker in front of its first segment as `[#e)]`, declared as structure to use and never to reproduce. Anything echoed back is stripped before it reaches the document.

On by default, with no switch – but it needs the [live document link](/memoq/mcp-server/#the-live-document-link) connected, because that is what names the file memoQ imported. On a project checked out from a server that file is on the project manager's machine, not yours; locate it once in [FigureLens](/memoq/prompt-editor/#where-the-documents-come-from) and the numbering is read from your copy. See [List numbering](/memoq/prompt-editor/#list-numbering-reaches-the-model-as-structure).

### 9. Figure descriptions

The AI reads your text and cannot see your pictures. [**FigureLens**](/memoq/prompt-editor/#figurelens-what-the-figures-show) closes that gap: it takes the images out of your documents into the memory bank's `figures\` folder, shows each one to the AI together with what the document says about it, and saves a description – what it shows, which figure it is, which reference signs appear on it – as `figures.md` in the bank.

From then on it rides along with layer 7 and is read with every request, so the model knows that the *valve (12)* in the sentence is the thing at the top right of Figure 3. Vector drawings – EMF and WMF, which is what a drawing placed from CAD usually is – are rendered to PNG on the way out, because no AI can read a metafile.

Reference signs the model reads in a drawing that appear nowhere in the text are listed for you, because that is a defect worth raising with the client before filing.

Two clicks per project, then it is automatic. One AI request per image; the panel says how many and to which provider before you click, and **Describe from the text only** is a free alternative that uses what the document itself says about each figure.

### 10. The whole document

Not a translation layer: memoQ hands an MT plugin about ten segments at a time and never the document, so a per-segment prompt cannot contain it.

What does get the whole document is [**AutoPrompt**](/memoq/prompt-editor/#autoprompt-drafting-a-prompt-for-the-open-project), which reads it through the live document link to classify the job and draft a prompt for it. That prompt then carries the document's character into every subsequent request – which is the point: the document is read once, expensively, and its conclusions ride along cheaply thereafter.

Where memoQ shows several files merged into one view, AutoPrompt offers **All N documents memoQ is showing** so the prompt is drafted from all of them rather than whichever file you happened to pick.

## What memoQ does not give a plugin

Worth stating plainly, because the Trados page lists them and the difference is not a fault in either product:

- **Surrounding segments.** memoQ passes neighbouring segments only through the rich lookup channel reserved for its own AGT engine. Layer 3 exists because of this.
- **Term base hits.** The same channel, the same result. See layer 6.
- **Attached files.** memoQ has no equivalent; there is nothing to attach a file to.

None of these can be unlocked by a setting on your side. They are consequences of the plugin model, measured rather than assumed – and where one bites, the layer above it says what stands in for it.

## Stacking the layers

The default composition – everything above except the ones that need a click – is a strong baseline and the one to start from.

More context is not automatically better. The context window is finite, and a mature memory bank plus a rich glossary can push a prompt into the tens of thousands of tokens. The cost is smaller than it looks, because the stable half of every request is identical from batch to batch and is cached: on one 370-segment run, caching turned roughly $10 into roughly $4. But token count is not the only cost — three overlapping sources describing the same term can contradict each other, and the model then has to reconcile them on the fly.

The layers that describe the **document** rather than the **client** – 5, 8 and 9 – are cheap, never contradict each other, and there is no case yet found where switching one off improved a translation.

## Seeing what is being sent

The [Activity window](/memoq/prompt-editor/#the-activity-window) in the prompt editor logs every request with its token counts – regular, cached, written, output – so a layer that is not arriving shows up as a number that does not move. It also says, once per document, whether list numbering was available and why not when it was not, and which memory bank is in force.

AutoPrompt's **Preview context…** button shows exactly what would be sent before anything is sent, and makes no AI call.

## See also

- [Prompt library and editor](/memoq/prompt-editor/) – AutoPrompt, FigureLens, list numbering, the settings
- [Self-learning](/memoq/self-learning/) – how confirmed segments are captured and fed back
- [Terminology](/memoq/terminology/) – the glossary the model reads
- [MCP server and the live document link](/memoq/mcp-server/) – memory banks, and the channel layers 8 to 10 depend on
- [Context layers in Supervertaler for Trados](/trados/context-layers/) – the same idea, a different host

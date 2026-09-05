---
title: "Prompt Library & Editor"
---

Supervertaler for memoQ translates with the instructions you give it. Those instructions can be typed straight into the settings dialog, or chosen from the **shared Supervertaler prompt library** – the same folder of prompts the Trados plugin uses, so a prompt tuned in one tool is available in the other.

memoQ gives an add-in no window of its own, so the library cannot be a panel inside memoQ. Instead there is a small **Prompt Library editor**, opened from the settings dialog, that runs alongside memoQ.

## Choosing a prompt

In **Resource console → MT settings → Supervertaler → Configure plugin**, the **Prompt** dropdown lists every translation prompt in the library, grouped by folder. Pick one and its text appears (read-only) in the **Instructions** box below.

Choose **(instructions below)** instead to type your own; the box becomes editable.

The dropdown stores *which* prompt you chose, not its text. Edit the prompt anywhere – in the editor, in the Trados plugin, in a text editor – and memoQ uses the new version on the next segment.

Only prompts in the library's **Translate** folder are offered. Proofreading and QuickLauncher prompts exist for other tasks and would produce commentary where a translation belongs.

## The editor

Press **Edit…** beside the Prompt dropdown.

<!-- screenshot: the editor with the tree on the left, a prompt open on the right -->

- **Left:** the library as a tree, folders and prompts. Select one to open it.
- **Right:** name, description, which product it is for, sort order, and the prompt text with Markdown headings and `{{PLACEHOLDERS}}` highlighted.
- **Toolbar, left:** New, Save, Placeholder, AutoPrompt.
- **Toolbar, right:** whether Pre-translate goes to Claude Desktop, the [Activity window](#the-activity-window), and Translation settings. Everything else is on the **File**, **memoQ**, **Settings** and **Help** menus.

The **Claude Desktop** button on the right is a switch, not a command, and its caption says which mode is *on* rather than what pressing it would do. It decides whether Pre-translate spends your API key or hands the segments to the chat, so it is worth a glance before a long run. It is the same setting as **Settings → Pre-translate via Claude Desktop**, and as the checkbox in memoQ’s own dialog – change it anywhere and all three follow.

Save with **Ctrl+S**. A prompt marked read-only in the library (the built-in defaults) can be read but not overwritten; make a copy under a new name instead.

Any settings the file carries that the editor does not have a field for – tags, favourites, QuickLauncher flags set by the Trados plugin – are preserved untouched on save. The status line under the description says which ones the file has.

### What memoQ is using

Under the toolbar, three things memoQ will apply to every translation:

**Prompt**, **Glossary** and **Memory bank**. Click any of them to change it. Prompt and Memory bank open a list with a filter box rather than a dropdown menu, because both grow with the work – a prompt library reaches forty entries quickly, and a bank per client does the same. Glossary opens a file dialog, because a glossary is a file and can live anywhere.

These are the choices that change between jobs, which is why they are here rather than in Translation settings: they are what the model knows before it is shown a segment. Each is also the same setting memoQ’s own dialog shows, so either place can change it.

The memory bank is remembered **per project**. Choose one while working on a job and it comes back when you return to that job – and a project you have never chosen one for uses *no* bank rather than inheriting the last one, because a bank carries one client’s terminology and the wrong one is worse than none. See [Memory banks](/memoq/mcp-server/#memory-banks) for where they live.

### Placeholders

Prompts use `{{SOURCE_LANGUAGE}}` and `{{TARGET_LANGUAGE}}` rather than naming languages, so one prompt serves every language pair. memoQ fills them in per project.

**Insert placeholder** lists the ones memoQ can fill. A placeholder memoQ cannot fill – `{{SOURCE_SEGMENT}}`, say, which only the Trados plugin provides – is shown in red, and the editor warns that it will reach the model as empty text. Do not use those in a prompt meant for memoQ.

### Which product a prompt is for

**Available in** can be *both*, *trados* or *memoq*. memoQ's dropdown hides prompts marked for Trados only. Leave it on *both* unless a prompt genuinely depends on something one product cannot supply.

A prompt tied to one product says so in its **filename**: `Patent claims EN-NL [memoQ].md`, `Define [Trados].md`. Prompts available to both carry no marker, so the absence of one is itself readable – which is the point, because in Explorer the metadata header is not visible and every prompt otherwise looks alike.

The marker is written from the **Available in** field on every save and stripped again on every read, so it is a label rather than a setting. Renaming the file in Explorer does not change which product a prompt is for, and the next save puts the old marker back: change the field, not the filename. The editor’s tree and the Prompt dropdown show the same thing in words.

## Where the library lives

`C:\Users\<you>\Supervertaler\prompt_library\` – one Markdown file per prompt, with a small metadata header. **Open folder** in the editor takes you there. The files are plain text; nothing stops you editing them directly, and a folder synced between machines carries the whole library with it.

## AutoPrompt: drafting a prompt for the open project

Press **AutoPrompt…** in the editor’s toolbar, or choose it from the **memoQ** menu. Supervertaler reads the document you are translating, your glossary hits in it and anything you have already confirmed, and has the AI write a prompt tailored to that job – domain, register, a locked glossary, the lot. The result is saved under **Translate** and opened for you to review; then pick it from memoQ's **Prompt** dropdown.

Before it runs you choose the document (if several are captured), and can add a briefing – client, audience, style, what to avoid – which the AI treats as authoritative.

**Preview context…** shows you exactly what will be sent, before anything is sent: the extract from your document, the glossary hits, the segments you have confirmed, the briefing you typed, and the instructions the AI is given about writing a prompt for memoQ. It makes no API call and costs nothing, and the briefing box stays open behind it – so the loop is look, add what is missing, look again, then generate.

Three things to know:

- **memoQ must be running with a Supervertaler engine active**, and the document must have been captured – one Pre-translate does it (free, with the [Claude Desktop box](/memoq/mcp-server/#the-checkbox) ticked). The plugin only sees what memoQ has sent it.
- **It uses the provider, model and API key from your Supervertaler settings.** Two calls: a short one to classify the document, then a long one to write the prompt. Expect a minute or two.
- **The prompt is written for memoQ, not copied from the Trados recipe.** Single-segment lookups are handled as well as batches; tag markers must be reproduced exactly; translations you have confirmed outrank the prompt's own glossary; and it is kept to 1,500–3,000 words because memoQ re-sends the whole prompt with every ten-segment request.

Draft it again later in the job and it gets better: by then it can see what you have confirmed, which is stronger evidence of how you want *this* document translated than the source text alone.

### Translator comments

Where a note is genuinely necessary – an ambiguity in the source, a term that could go two ways, a probable defect in the original – a drafted prompt has the AI put it inline at the end of the target as a `[[TC: …]]` marker. Supervertaler for Trados uses the same form, so a prompt written for one product reads correctly in the other.

Nothing extracts these for you, and that is deliberate. You read them in the grid as you review, decide which are worth keeping, turn those into real memoQ comments on the segment, and delete the marker from the text. Search for `[[TC:` to find them all.

## Export glossary: the prompt's terms as the project glossary

An AutoPrompt draft ends with a locked-terms table – a dozen or so renderings chosen for this document. That table is exactly what the [terminology plugin](/memoq/terminology/) and the `check_terminology` QA tool should work from: a general glossary flags *application → aanvrage* in every paragraph of a software patent, a project glossary knows better.

Choose **memoQ → Export this prompt’s terms as a glossary** with the prompt open. Supervertaler reads every table in it that names a source and a target column, turns notes of the form *never "apparatus"* into forbidden entries, and writes a tab-separated glossary file to `C:\Users\<you>\Supervertaler\memoq\glossaries\<prompt name>.txt`. Answer yes when it asks and that file becomes the active glossary immediately, whether or not memoQ is running.

The file is plain text – edit it freely; the plugin re-reads it whenever it changes. Any prompt with a table laid out the same way works, not only AutoPrompt's.

### Settings

**Settings → Translation settings** holds how Supervertaler translates: provider, model, endpoint, parallel requests, segments per request, and whether termbase hits and surrounding segments are sent to the model. These are the same settings as memoQ’s own Supervertaler dialog, reading and writing the same file, so either place can change them and both show the same values.

The **Model** list is filled from the provider’s own catalogue, so new models appear without an update to Supervertaler: choose the provider and its models are listed under their proper names. The list is fetched once and kept for a day. It stays typeable, so a gateway, a private deployment or a model the provider has not yet published can be entered by hand.

**Segments per request** can only lower what memoQ does, not raise it – memoQ hands a plugin about ten segments at a time during Pre-translate, however high this is set. Lowering it is still worth doing if a model keeps returning fewer translations than it was sent.

**Settings → Pre-translate via Claude Desktop (MCP)** is on the menu itself, and on the right of the toolbar, because it is the one that gets flipped between jobs rather than set once. See [MCP server](/memoq/mcp-server/).

The **API key** is here too. If you also run Supervertaler for Trados, leave it alone: Trados keeps its keys in the same data folder, this reads them, and the box tells you so. Rotating a key there is then the only change you need to make. Type a key here only to override that, and clear the box to go back to the shared one.

## The Activity window

memoQ’s Pre-translate dialog is modal and says only *Processing*, for as long as the run takes: no engine, no model, no count, and no sign when something is wrong. **memoQ → Activity…**, or **Ctrl+L**, opens a window that shows what Supervertaler is actually doing.

<!-- screenshot: the activity window during a pre-translate run -->

It is a window of its own rather than a panel so that it can sit over memoQ while that dialog holds the screen. Tick **Keep on top** and you can watch a Pre-translate run from the first batch to the last.

What it shows: the engine and model each project starts with, the glossary as it loads and how many terms came out of it, warnings when the selected prompt or glossary faces the opposite language pair, every batch with the segments sent, the segments returned and the glossary terms matched, AutoPrompt drafts, and anything that failed. A batch that comes back short is called out rather than logged flatly, because that is the failure that quietly shifts every translation after it.

**Show everything** un-hides the per-request diagnostics – memoQ’s capability probes, lookup sessions, single-segment translations – which are what you want when something is wrong and noise the rest of the time.

The window reads the plugin’s own log, `C:\Users\<you>\AppData\Local\Supervertaler.memoQ\plugin.log`, rather than being fed by the plugin. So it shows what happened before you opened it, it works whether or not memoQ is running, and closing it costs nothing. Its position and size are remembered.

## Drafting prompts with Claude

If you use the [MCP server](/memoq/mcp-server/), Claude can write into this library: *"Draft a translation prompt for this project and save it."* It reads the captured document, your confirmed segments and your glossary, saves the result as a new prompt, and you pick it from the dropdown. The editor is where you review and tune what it wrote.

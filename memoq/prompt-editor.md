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
- **Toolbar:** New prompt, New folder, Delete, Save, Insert placeholder, Reload from disk, Open folder.

Save with **Ctrl+S**. A prompt marked read-only in the library (the built-in defaults) can be read but not overwritten; make a copy under a new name instead.

Any settings the file carries that the editor does not have a field for – tags, favourites, QuickLauncher flags set by the Trados plugin – are preserved untouched on save. The status line under the description says which ones the file has.

### Placeholders

Prompts use `{{SOURCE_LANGUAGE}}` and `{{TARGET_LANGUAGE}}` rather than naming languages, so one prompt serves every language pair. memoQ fills them in per project.

**Insert placeholder** lists the ones memoQ can fill. A placeholder memoQ cannot fill – `{{SOURCE_SEGMENT}}`, say, which only the Trados plugin provides – is shown in red, and the editor warns that it will reach the model as empty text. Do not use those in a prompt meant for memoQ.

### Which product a prompt is for

**Available in** can be *both*, *trados* or *memoq*. memoQ's dropdown hides prompts marked for Trados only. Leave it on *both* unless a prompt genuinely depends on something one product cannot supply.

## Where the library lives

`C:\Users\<you>\Supervertaler\prompt_library\` – one Markdown file per prompt, with a small metadata header. **Open folder** in the editor takes you there. The files are plain text; nothing stops you editing them directly, and a folder synced between machines carries the whole library with it.

## AutoPrompt: drafting a prompt for the open project

Press **AutoPrompt…** in the editor’s toolbar, or choose it from the **memoQ** menu. Supervertaler reads the document you are translating, your glossary hits in it and anything you have already confirmed, and has the AI write a prompt tailored to that job – domain, register, a locked glossary, the lot. The result is saved under **Translate** and opened for you to review; then pick it from memoQ's **Prompt** dropdown.

Before it runs you choose the document (if several are captured), and can add a briefing – client, audience, style, what to avoid – which the AI treats as authoritative.

Three things to know:

- **memoQ must be running with a Supervertaler engine active**, and the document must have been captured – one Pre-translate does it (free, with the [Claude Desktop box](/memoq/mcp-server/#the-checkbox) ticked). The plugin only sees what memoQ has sent it.
- **It uses the provider, model and API key from your Supervertaler settings.** Two calls: a short one to classify the document, then a long one to write the prompt. Expect a minute or two.
- **The prompt is written for memoQ, not copied from the Trados recipe.** Single-segment lookups are handled as well as batches; tag markers must be reproduced exactly; translations you have confirmed outrank the prompt's own glossary; and it is kept to 1,500–3,000 words because memoQ re-sends the whole prompt with every ten-segment request. Inline translator comments work as in Trados, with one difference: a genuinely necessary note appears in the target as a `[[TC: …]]` marker – double square brackets rather than Trados's `⟦ ⟧`, because those glyphs are missing from Tahoma, Verdana and Calibri and show as empty boxes in memoQ's grid. Search for `[[TC:` to find them while reviewing.

Draft it again later in the job and it gets better: by then it can see what you have confirmed, which is stronger evidence of how you want *this* document translated than the source text alone.

## Export glossary: the prompt's terms as the project glossary

An AutoPrompt draft ends with a locked-terms table – a dozen or so renderings chosen for this document. That table is exactly what the [terminology plugin](/memoq/terminology/) and the `check_terminology` QA tool should work from: a general glossary flags *application → aanvrage* in every paragraph of a software patent, a project glossary knows better.

Choose **memoQ → Export this prompt’s terms as a glossary** with the prompt open. Supervertaler reads every table in it that names a source and a target column, turns notes of the form *never "apparatus"* into forbidden entries, and writes a tab-separated glossary file to `C:\Users\<you>\Supervertaler\memoq\glossaries\<prompt name>.txt`. Answer yes when it asks and that file becomes the active glossary immediately, whether or not memoQ is running.

The file is plain text – edit it freely; the plugin re-reads it whenever it changes. Any prompt with a table laid out the same way works, not only AutoPrompt's.

### Settings

**Settings → Translation settings** holds how Supervertaler translates: provider, model, endpoint, parallel requests, segments per batch, and whether termbase hits and surrounding segments are sent to the model. These are the same settings as memoQ’s own Supervertaler dialog, reading and writing the same file, so either place can change them and both show the same values.

**Settings → Pre-translate via Claude Desktop (MCP)** is on the menu itself as well, because it is the one that gets flipped between jobs rather than set once. See [MCP server](/memoq/mcp-server/).

The **API key** is here too. If you also run Supervertaler for Trados, leave it alone: Trados keeps its keys in the same data folder, this reads them, and the box tells you so. Rotating a key there is then the only change you need to make. Type a key here only to override that, and clear the box to go back to the shared one.

## Drafting prompts with Claude

If you use the [MCP server](/memoq/mcp-server/), Claude can write into this library: *"Draft a translation prompt for this project and save it."* It reads the captured document, your confirmed segments and your glossary, saves the result as a new prompt, and you pick it from the dropdown. The editor is where you review and tune what it wrote.

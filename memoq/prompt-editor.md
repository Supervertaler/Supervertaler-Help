---
title: "Prompt Library & Editor"
---

Supervertaler for memoQ translates with the instructions you give it. Those instructions can be typed straight into the settings dialog, or chosen from the **shared Supervertaler prompt library** — the same folder of prompts the Trados plugin uses, so a prompt tuned in one tool is available in the other.

memoQ gives an add-in no window of its own, so the library cannot be a panel inside memoQ. Instead there is a small **Prompt Library editor**, opened from the settings dialog, that runs alongside memoQ.

## Choosing a prompt

In **Resource console → MT settings → Supervertaler → Configure plugin**, the **Prompt** dropdown lists every translation prompt in the library, grouped by folder. Pick one and its text appears (read-only) in the **Instructions** box below.

Choose **(instructions below)** instead to type your own; the box becomes editable.

The dropdown stores *which* prompt you chose, not its text. Edit the prompt anywhere — in the editor, in the Trados plugin, in a text editor — and memoQ uses the new version on the next segment.

Only prompts in the library's **Translate** folder are offered. Proofreading and QuickLauncher prompts exist for other tasks and would produce commentary where a translation belongs.

## The editor

Press **Edit…** beside the Prompt dropdown.

<!-- screenshot: the editor with the tree on the left, a prompt open on the right -->

- **Left:** the library as a tree, folders and prompts. Select one to open it.
- **Right:** name, description, which product it is for, sort order, and the prompt text with Markdown headings and `{{PLACEHOLDERS}}` highlighted.
- **Toolbar:** New prompt, New folder, Delete, Save, Insert placeholder, Reload from disk, Open folder.

Save with **Ctrl+S**. A prompt marked read-only in the library (the built-in defaults) can be read but not overwritten; make a copy under a new name instead.

Any settings the file carries that the editor does not have a field for — tags, favourites, QuickLauncher flags set by the Trados plugin — are preserved untouched on save. The status line under the description says which ones the file has.

### Placeholders

Prompts use `{{SOURCE_LANGUAGE}}` and `{{TARGET_LANGUAGE}}` rather than naming languages, so one prompt serves every language pair. memoQ fills them in per project.

**Insert placeholder** lists the ones memoQ can fill. A placeholder memoQ cannot fill — `{{SOURCE_SEGMENT}}`, say, which only the Trados plugin provides — is shown in red, and the editor warns that it will reach the model as empty text. Do not use those in a prompt meant for memoQ.

### Which product a prompt is for

**Available in** can be *both*, *trados* or *memoq*. memoQ's dropdown hides prompts marked for Trados only. Leave it on *both* unless a prompt genuinely depends on something one product cannot supply.

## Where the library lives

`%USERPROFILE%\Supervertaler\prompt_library\` — one Markdown file per prompt, with a small metadata header. **Open folder** in the editor takes you there. The files are plain text; nothing stops you editing them directly, and a folder synced between machines carries the whole library with it.

## AutoPrompt: drafting a prompt for the open project

Press **Draft for memoQ project…** in the editor's toolbar. Supervertaler reads the document you are translating, your glossary hits in it and anything you have already confirmed, and has the AI write a prompt tailored to that job — domain, register, a locked glossary, the lot. The result is saved under **Translate** and opened for you to review; then pick it from memoQ's **Prompt** dropdown.

Before it runs you choose the document (if several are captured), and can add a briefing — client, audience, style, what to avoid — which the AI treats as authoritative.

Three things to know:

- **memoQ must be running with a Supervertaler engine active**, and the document must have been captured — one Pre-translate does it (free, with the [Claude Desktop box](/memoq/mcp-server/#the-checkbox) ticked). The plugin only sees what memoQ has sent it.
- **It uses the provider, model and API key from memoQ's Supervertaler settings.** Two calls: a short one to classify the document, then a long one to write the prompt. Expect a minute or two.
- **The prompt is written for memoQ, not copied from the Trados recipe.** Single-segment lookups are handled as well as batches; tag markers must be reproduced exactly; translations you have confirmed outrank the prompt's own glossary; and it is kept to 1,500–3,000 words because memoQ re-sends the whole prompt with every ten-segment request. Inline translator comments work as in Trados: a genuinely necessary note appears in the target as a `⟦TC: …⟧` marker for you to find and deal with while reviewing.

Draft it again later in the job and it gets better: by then it can see what you have confirmed, which is stronger evidence of how you want *this* document translated than the source text alone.

## Drafting prompts with Claude

If you use the [MCP server](/memoq/mcp-server/), Claude can write into this library: *"Draft a translation prompt for this project and save it."* It reads the captured document, your confirmed segments and your glossary, saves the result as a new prompt, and you pick it from the dropdown. The editor is where you review and tune what it wrote.

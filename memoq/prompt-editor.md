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

## Drafting prompts with Claude

If you use the [MCP server](/memoq/mcp-server/), Claude can write into this library: *"Draft a translation prompt for this project and save it."* It reads the captured document, your confirmed segments and your glossary, saves the result as a new prompt, and you pick it from the dropdown. The editor is where you review and tune what it wrote.

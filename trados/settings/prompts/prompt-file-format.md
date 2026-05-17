---
title: "Prompt File Format"
---

:::note
You are viewing help for 🧩 **Supervertaler for Trados** – the Trados Studio plugin. Looking for help with the standalone app? Visit 🖥️ [Supervertaler Workbench help](https://supervertaler.gitbook.io/help/get-started-1/workbench/).
:::

Prompts are stored as `.md` files (Markdown with YAML frontmatter). This is the same format used by Supervertaler Workbench, so prompts are automatically shared between both applications via the shared `prompt_library` folder. Legacy `.svprompt` files are still loaded for backward compatibility.

```yaml
---
type: prompt
description: Patent and IP translation with strict terminology rules
category: Translate
---

You are an expert {{SOURCE_LANGUAGE}} to {{TARGET_LANGUAGE}} patent translator...
```

The example file above would be saved as e.g. `My Patent Prompt.md` and would appear in the prompt tree as **My Patent Prompt**.

### Naming: filename is authoritative

The **on-disk filename** (without the `.md` extension) is the display name shown in the prompt selector. Renaming `My Patent Prompt.md` to `Client X – Patent EN.md` in Windows Explorer is all you need to do to change how the prompt appears in the tree – click **Refresh** in the Prompts tab to pick up the change.

:::note
**The YAML `name:` field is ignored on read.** It used to be the authoritative display name, but that created a confusing split: renaming the file in Explorer didn't update the tree unless you also edited the YAML inside. Filename is now the single source of truth. Old prompts with a `name:` field in their YAML continue to load fine – the field is silently ignored, and is dropped from the file the next time the prompt is saved through the UI. No action required for existing prompts.
:::

| YAML field            | Description                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `type`                | Document type – always `prompt` for prompt files                                                                         |
| `description`         | Optional summary shown under the prompt name in the detail pane                                                          |
| `category`            | `Translate`, `Proofread`, or `QuickLauncher` – controls where the prompt appears                                         |
| `quicklauncher_label` | Short label for the QuickLauncher menu (optional, falls back to the filename)                                            |
| `default`             | `true` for shipped prompts (managed by the plugin)                                                                       |
| `sort_order`          | Numeric order within folder (lower values first). Set automatically by the ▲/▼ buttons.                                  |
| `name`                | Ignored on read (legacy field, kept for backward compatibility). The filename is the display name.                       |

:::note
Older prompts using the `domain` key instead of `category` are still supported for backward compatibility.
:::

### System prompt

The plugin automatically prepends a system prompt to every AI call. This system prompt includes language pair information, termbase terms (based on your [AI Context settings](../ai-settings.md)), and TM matches when enabled. The content you write in a prompt `.md` file is the **user prompt** – it is sent after the system prompt.

### Creating and editing prompts

#### New prompt

1. Optionally select a target folder (e.g. `Translate` or `Proofread`) in the tree before clicking **New** – the new prompt's **Category** will be pre-filled from the selected folder.
2. Click **New** in the Prompts tab.
3. Fill in Name, Description, Category, and Content.
4. Click **Save**.

:::note
**Category matters for Batch Translate.** The Batch Translate dropdown filters by category: Translate mode only shows prompts whose Category is `Translate`, and Proofread mode only shows `Proofread` prompts. If you click **New** without first selecting a folder, the category defaults to `Translate` so the new prompt is immediately visible in the Batch Translate dropdown. Prompts with an empty or unrelated category will not appear in either Batch mode – move them into a `Translate` or `Proofread` folder (or edit the Category field) to make them selectable.
:::

#### Edit a prompt

1. Select a prompt in the list
2. Click **Edit**
3. Modify as needed and click **Save**

#### Inserting variables

While editing prompt content, press **Ctrl+,** to open the variable picker menu. This lists all available variables with a short description. Select a variable to insert it at the cursor position. If text is selected in the editor, it is replaced by the inserted variable.

:::note
**Ctrl+,** mirrors the variable insertion shortcut used in the Trados Studio editor.
:::

#### Delete a prompt

1. Select a custom prompt
2. Click **Delete** and confirm

Built-in prompts cannot be deleted. Click **Restore** to recreate any built-in prompts you have removed.

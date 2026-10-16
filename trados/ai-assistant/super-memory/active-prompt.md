---
title: "Active Prompt"
description: "Per-project prompt that Quick Add appends terminology to"
---

Each Trados project can have an **active prompt** – the prompt that Quick Add appends terminology to. This is also the prompt that is auto-selected in the [Batch Translate](/trados/batch-translate/) dropdown when you open the project.

## Setting the active prompt

1. Open **Settings → Prompts**
2. Right-click any prompt in the tree
3. Choose **Set as active prompt for this project**

The active prompt is shown with a pin icon and bold blue text in the Prompt Manager, and a checkmark appears next to its name in the Batch Translate dropdown. The Batch Translate dropdown updates **live** – you do not have to close the Settings dialog for the change to take effect. Cancelling the dialog reverts the change; clicking OK persists it.

To clear the active prompt, right-click it again and choose the same menu item (it toggles).

### When no prompt is set as active *(from v18/19.20.200)*

Until you set or choose a prompt, Batch Translate and Translate active segment (Alt+T) use the shipped **Default Translation Prompt**, and Proofread the **Default Proofreading Prompt** – so the Prompt Manager shows that default prompt as the active one, with the pin. Clearing the active prompt now means **(Built-in instructions only)**: Supervertaler's own instructions with no prompt from your Library, remembered as your choice, the same as picking that item in the Batch Operations dropdown. Before v18/19.20.200, no active prompt meant the built-in instructions alone, and the default prompts were used only if you picked them.

Quick Add appends terminology only to a prompt you have set as active yourself, never to a default prompt: Supervertaler refreshes the shipped default prompts when it updates, so a term added there would not last.

:::note
The active prompt works for any prompt regardless of folder or category. Even if a prompt's `Category` is not `Translate` (for example, a prompt at the root of the tree with no category set), it will still appear and be pre-selected in the Batch Translate dropdown once you mark it as active.
:::

:::note
The active prompt is saved [per project](/trados/settings/project-settings/). Different Trados projects can have different active prompts.
:::

## See Also

* [Quick Add](/trados/ai-assistant/super-memory/quick-add/)
* [Batch Translate](/trados/batch-translate/)
* [Prompts](/trados/settings/prompts/)
* [Per-Project Settings](/trados/settings/project-settings/)

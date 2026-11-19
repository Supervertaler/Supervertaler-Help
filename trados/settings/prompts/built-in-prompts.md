---
title: "Built In Prompts"
---

The plugin ships with default prompts organised into three categories:

| Category          | Prompts                                                                                                                                                                      | Used in              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| **Translate**     | Default Translation Prompt                                                                                                                                                   | Batch Translate mode |
| **Proofread**     | Default Proofreading Prompt                                                                                                                                                  | Batch Proofread mode |
| **QuickLauncher** | Assess translation, Define, Explain (in general), Explain (within project context), Translate segment using fuzzy matches, Translate selection in context of current project | QuickLauncher menu   |

:::note
The Default Translation Prompt is a general-purpose starting point. For domain-specific projects, use **[AutoPrompt](/trados/generate-prompt/)** to automatically create a comprehensive prompt tailored to your document – or duplicate the default prompt in the Prompt Manager and customise it manually.
:::

### The System Prompt and the fixed output rules

At the top of the list in **Settings → Library** is the **System Prompt**: Supervertaler's base instructions for AI translation (the language pair, inline tags, number formatting). It is sent first in every translation request; the prompt you choose from the Library is **added after it**, never put in its place. You can change it with **Edit System Prompt**, and **Reset to Default** brings back the shipped text. Proofreading does not use it: its base instructions are fixed in the plugin.

*(From v18/19.20.209)* Under the System Prompt, on a pale yellow background, the Library also shows the **output rules** Batch Translate adds at the very end of every request: return translations only, keep every tag, and put any remark in a `[[TC: ...]]` note. They come last so that no prompt, not even an edited System Prompt, can switch them off, and they cannot be edited.

Choosing **(System Prompt only)** in the Batch Operations prompt list sends exactly these two, with no Library prompt between them, plus the context you have switched on (document, translation memory matches, termbase, memory bank). **Preview prompt** on the Batch Operations tab shows the complete request.

### About the Default Proofreading Prompt

The Default Proofreading Prompt is intentionally short. Most of the structure proofreading needs – persona, the five quality categories (accuracy / completeness / terminology / grammar / number formatting), the output format, the "no full corrected translations" rule, language-specific checks for Dutch / German / French – is **already in the hardcoded base** that every Batch Proofread uses, so the prompt itself only adds what the base doesn't have:

* **Default to OK** – raise an issue only when there's a specific, demonstrable problem in the translation, never speculative concerns.
* **Citation discipline** – terminology consistency claims must cite specific source segment numbers in the **Evidence:** field, against the full bilingual document context that's auto-included.
* **Source query distinction** – source-side errors (typos, duplications, internal inconsistencies) get prefixed with "Source query:" rather than triggering target changes.
* **Explicit boundaries** – the AI doesn't re-engineer the source, propose alternative terminology without a citation, flag stylistic preferences, or flag empty target lines.

These behaviours target the false-positive patterns most users encounter: the AI fabricating "term X used elsewhere" claims, second-guessing the source's substantive claims, and treating stylistic preferences as errors. See [AI Proofreader](/trados/ai-proofreader/) for the full picture, including the Evidence field on issue cards.

:::note
**To customise:** clone the default in the Prompt Manager and edit your copy. Defaults are read-only and get refreshed when the plugin updates – your clone keeps all your changes regardless. When the Prompt Library writes the default to disk, it includes a `default: true` flag in the YAML frontmatter; clones get `default: false` and are never touched by future updates.
:::

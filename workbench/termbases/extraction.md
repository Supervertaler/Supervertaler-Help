---
title: "Term Extraction"
---

**Term extraction** sends your project's source text to your configured AI model and returns a proposed **bilingual project glossary** – source terms paired with translations – which you review, edit, and turn into a project termbase in one step.

:::note
**Requires Workbench v1.10.357 or later.** Earlier versions used a mechanical frequency-based extractor (monolingual, no translations); it has been retired. Extraction now uses the same AI provider and model as your translations, configured under **AI → Settings**.
:::

### Opening the extraction dialogue

Go to the **Termbases** tab and click **🔍 Extract Terms** in the button bar beneath the termbase list, next to **+ Create New**.

Extraction reads the source segments of the open project, so open a project first – clicking with none open just tells you to.

### Choosing the source text

The dialogue offers two sources:

* **Use project segments** (default) – extracts from all source segments in the loaded project.
* **Paste text manually** – enables the text box below, so you can extract from arbitrary text. Useful for a reference document or a client's style guide.

### Extraction settings

| Setting | Default | What it does |
| ------- | ------- | ------------ |
| **Source Language** | the project's source language | Tells the model what language the text is in. Free text – any language works. |
| **Target Language** | the project's target language | The language the model translates each term into. |
| **Domain / Subject** | blank | Optional hint, e.g. `mechanical engineering` or `sewing machines`. Leave blank and the model infers the domain from the text itself. |

Click **🤖 Extract Terms with AI**. Small texts return in seconds; a full-length document (e.g. a complete patent application) takes a minute or so. The dialogue stays responsive while it runs.

:::note
**Your source text is sent to the configured AI provider** – the same one that handles your translations, so this adds no exposure beyond translating the project. If a project must not leave your machine, use a local model (Ollama) as your provider.
:::

### Reviewing the results

Results fill a table of term pairs:

| Column | Meaning |
| ------ | ------- |
| **Select** | Tick box controlling whether the pair is added. Every row starts ticked. |
| **Source** | The term, in its canonical (dictionary) form. **Editable** – click to correct. |
| **Target** | The model's translation. **Editable.** May be empty where the model was unsure – fill it in or untick the row. |
| **Note** | Optional context from the model, such as a domain label or a caveat. |

Edit cells directly to fix anything before committing – your edits are what gets saved, not the model's original answer.

To tick or untick many rows at once, select them (Shift/Ctrl+click) and **right-click** → *Untick selected* / *Tick selected*.

On very large projects only the first portion of the text (roughly 8–9k words) is analysed, and the results label says so explicitly – nothing is truncated silently.

### Creating the project termbase

Click **Create Project Termbase**, then give it a name. The default is `<Project name> Terminology`.

Supervertaler creates a project-scoped **bilingual** termbase containing every ticked pair and makes it the **Project termbase** – it appears in the Termbases tab with the pink **Project** tick and **Read** enabled, so terms with targets immediately produce [TermLens](termlens.md) suggestions. Empty-target entries can be completed later – see [Creating termbases](creating.md).

:::note
**One project termbase per project.** If the project already has one, you are asked what to do (v1.10.358+): make the new termbase the project termbase (the existing one is kept as a regular termbase), save the new one as a regular termbase alongside, or cancel. Nothing is deleted in any case.
:::

### Tips

- The model's output is a proposal, not a verdict – review it as you would any AI suggestion, especially target translations of ambiguous terms.
- A one-word domain hint noticeably improves precision on specialised texts.
- If you build prompts with **AutoPrompt**, note that it already performs glossary extraction as part of prompt generation – the two are complementary: this feature produces a *termbase* you can edit, share, and reuse across sessions.

***

### See Also

* [Termbase Basics](basics.md)
* [Creating termbases](creating.md)
* [Importing termbases](importing.md)
* [AI injection](ai-injection.md)
* [TermLens overview](termlens.md)

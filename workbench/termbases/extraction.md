---
title: "Term Extraction"
---

**Term extraction** scans your project's source segments and proposes a ranked list of candidate terms, which you can then turn into a project termbase in one step. It is a fast way to seed terminology for a technical document before you start translating.

:::note
**Extraction is monolingual.** It produces a list of *source* terms with empty targets – it does not suggest translations. You fill in the target side afterwards, by hand or with [AI injection](ai-injection.md). Think of it as building the left-hand column of your termbase.
:::

### Opening the extraction dialogue

Go to the **Termbases** tab and click **🔍 Extract Terms** in the button bar beneath the termbase list, next to **+ Create New**.

Extraction reads the source segments of the open project, so open a project first – clicking with none open just tells you to.

:::note
**On Workbench v1.10.351 and earlier, this button is permanently greyed out** and the feature cannot be reached at all, regardless of whether a project is open. Fixed in **v1.10.352**.
:::

### Choosing the source text

The dialogue offers two sources:

* **Use project segments** (default) – extracts from all source segments in the loaded project.
* **Paste text manually** – enables the text box below, so you can extract from arbitrary text without importing it. Useful for a reference document or a client's style guide.

### Extraction parameters

| Parameter | Range | Default | What it does |
| --------- | ----- | ------- | ------------ |
| **Source Language** | en, nl, de, fr, es | en | Selects the stop-word list used to filter out common words. Also becomes the new termbase's source language. |
| **Min Frequency** | 1–20 | 2 | How many times a candidate must occur to be considered. Raise it on long documents to cut noise; lower it to 1 on short ones. |
| **Max N-gram** | 1–5 | 3 | Longest multi-word term to consider. 1 finds single words only; 3 finds up to three-word phrases. |
| **Max Terms** | 10–1000 | 100 | Caps how many candidates appear in the results table, keeping the highest-scoring ones. |

Only these five languages have stop-word lists. Extracting from another language still works, but common function words will not be filtered out, so expect more noise and consider raising **Min Frequency**.

### Reviewing the results

Click **🔍 Extract Terms** inside the dialogue to run the extraction. Results fill a table with four columns:

| Column | Meaning |
| ------ | ------- |
| **Select** | Tick box controlling whether the term is added. Every row starts ticked. |
| **Term** | The candidate term. |
| **Frequency** | How many times it occurs in the source text. |
| **Score** | Ranking score – see below. Rows are sorted highest first. |

If nothing comes back, Supervertaler suggests lowering the minimum frequency – that is usually the right fix on short documents.

Untick anything you do not want before continuing. Reviewing matters here: extraction is statistical, not semantic, so it will happily propose frequent-but-useless phrases alongside genuine terminology.

#### How the score is calculated

The score ranks candidates by how term-like they look:

* **Frequency** contributes on a logarithmic scale, so the tenth occurrence adds far less than the second.
* **Multi-word terms get a bonus** proportional to their length, since a recurring three-word phrase is usually more valuable than a common single word.
* **Terms containing `-`, `_`, `.` or `/`** get a bonus, as these often mark technical identifiers and compounds.

Anything falling below **Min Frequency** scores zero and is dropped entirely.

:::note
**Extracted terms arrive lowercased.** Text is normalised to lower case before candidates are counted, so `Supervertaler Workbench` is extracted as `supervertaler workbench`. Fix the casing when you edit the entries – it matters for terms whose capitalisation is meaningful, such as product names and abbreviations.
:::

### Creating the project termbase

Click **Create Project Termbase**, then give it a name. The default is `<Project name> Terminology`.

Supervertaler creates a project-scoped termbase containing every ticked term, with the target side left empty, and refreshes the termbase list.

:::note
**One project termbase per project.** If the project already has one, creation fails with an error rather than merging into it. To extract again, rename or delete the existing project termbase first.
:::

Because entries land with empty targets, they will not produce useful [TermLens](termlens.md) suggestions until you fill the target side in. See [Creating termbases](creating.md) for editing entries.

### Limitations

* Monolingual – no translation suggestions.
* Stop-word filtering covers five languages only.
* Purely statistical: frequency and shape, no linguistic analysis and no lemmatisation, so inflected forms of one term count as separate candidates.
* One project termbase per project, with no merge into an existing one.

***

### See Also

* [Termbase Basics](basics.md)
* [Creating termbases](creating.md)
* [Importing termbases](importing.md)
* [AI injection](ai-injection.md)
* [TermLens overview](termlens.md)

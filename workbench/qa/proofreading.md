---
title: "AI Proofreading"
---

**AI Proofreading** asks an LLM to review your finished translation for accuracy, completeness, terminology and style, and records what it finds as **proofreading comments** on each segment. It's a translator-side review pass — nothing is changed automatically; you read the feedback and decide what to act on.

Proofreading lives under the top-level **QA** menu:

* **QA ▸ Proofreading ▸ Proofread Translation…** — run a proofreading pass.
* **QA ▸ Proofreading ▸ Delete All Proofreading Comments** — clear every proofreading comment in the project.

## Running a proofreading pass

Open **QA ▸ Proofreading ▸ Proofread Translation…**. The dialog has three things to set:

### 1. Which segments

| Scope | What it checks |
|---|---|
| **✅ Confirmed only** *(default)* | Only segments you've confirmed. |
| **📝 Translated + Confirmed** | Draft *and* confirmed segments. |
| **🔹 Selected** | The rows you've selected in the grid (select rows first to enable this). |
| **🌐 All segments** | Every segment, regardless of status. |

### 2. Which model

Proofreading uses your **currently-active AI provider and model** (set in **AI Settings**) — the dialog shows which one, e.g. `📊 Using: Openai (gpt-5.5)`. To proofread with a *different* model, switch the active provider in AI Settings and run the pass again (see [Multiple models](#multiple-models) below).

### 3. Which prompt

* **Default (built-in)** runs the standard four-point check:
  1. **Accuracy** — does the target correctly convey the source meaning?
  2. **Completeness** — is anything missing or added?
  3. **Terminology** — are technical terms correct and consistent?
  4. **Grammar & Style** — is the text natural and error-free?
* Or pick a **custom proofreading prompt** from the dropdown — any prompt you've saved under the **Bulk Operations/** folder of your [Prompt Library](../ai-translation/prompt-library.md) appears here.
* Or **type a one-off prompt** straight into the box.

Click **Proofread** to start. A progress dialog shows how many segments have been checked, how many issues were found, and how many came back clean; you can cancel partway through.

## Where the results appear

Findings land in the **✅ Proofreading** sub-tab of the **💬 Comments** panel — an all-project list of every proofreading comment, one entry per (segment, model). See [Comments → Proofreading comments](../editor/comments.md#proofreading-comments) for the full rundown. In short:

* Each entry has a clickable **Segment #N · model** header that jumps to the segment.
* Selecting a segment in the grid **scrolls and highlights** the list to that segment's comments.
* A **🗑️** button deletes a single comment; **QA ▸ Proofreading ▸ Delete All Proofreading Comments** clears them all.
* In the grid, a segment with a proofreading comment shows a **purple** Status-cell background (versus **amber** for a segment comment, and a **split** when it has both).

## Multiple models

Results are stored **keyed by model**, so passes with different models *accumulate* rather than overwrite: proofread once with GPT and once with Claude, and each segment keeps both sets of findings. In the Proofreading list **each engine gets its own colour**, so you can compare at a glance what each model flagged. Running the same model again replaces only that model's note.

## Good to know

* **Proofreading comments are ephemeral review notes.** They're stored in the `.svproj` project file but are **not exported** to your final document or bilingual tables — unlike [segment comments](../editor/comments.md), which do export as Word comments. Deleting them is safe: another proofreading pass regenerates them.
* Proofreading is **read-only feedback** — it never edits your target text for you.
* Cost scales with scope and model. Proofreading every segment with a premium model on a large project is a real API spend; the **Confirmed only** default keeps a first pass focused. See [Usage & Costs](../ai-translation/usage-costs.md).

## Related

* [Comments](../editor/comments.md) — where proofreading comments are listed and managed
* [Spellcheck](spellcheck.md) · [Tag Validation](tag-validation.md) · [Non-Translatables](non-translatables.md)
* [Prompt Library](../ai-translation/prompt-library.md) — save custom proofreading prompts
* [Usage & Costs](../ai-translation/usage-costs.md)

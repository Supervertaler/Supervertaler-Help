---
title: "Reports"
---

The **Reports** tab in the Supervertaler Assistant panel is where the assistant collects structured output from its AI operations. Two kinds of thing land here: **proofreading results** and an optional **log of AI calls**.

## Proofreading results

When you run the **AI Proofreader** (the Proofread mode of [Batch Operations](/trados/batch-operations/)), each issue the AI finds is shown here as a clickable card. See [AI Proofreader](/trados/ai-proofreader/) for the full workflow and what each card contains.

Since v18.20.187 every completed run is also written to `trados\reports` in your data folder as Markdown, and **Save report…** next to **Clear** writes a copy wherever you choose. The button is enabled only while a proofreading report is showing.

## AI operation log

When **Log prompts and responses to Reports tab** is enabled in [AI Settings](/trados/settings/ai-settings/), AI calls – Chat, Batch Translate, Batch Proofread and AutoPrompt – are recorded here together with the prompt, the response, the model used and the token/cost figures. It is the place to audit exactly what was sent to the AI provider and to review cost after the fact.

From v18/19.20.198:

* **A request that fails is recorded too.** It shows as **ERROR**, and opening it shows the provider's message – an overloaded server, an invalid key, a model name the provider does not recognise. Before, a Batch Translate or Translate active segment request that failed left no entry at all, and the reason appeared only in the Batch Translate log.
* **A one-segment request shows what it sent besides the system prompt:** the segment and the termbase terms that went with it.
* **A memory bank selection has an entry of its own**, named **Memory bank selection**: the one small request per document that picks which notes of a large bank go with it. See [SuperMemory – AI Integration](/trados/ai-assistant/super-memory/ai-integration/#a-large-bank-sends-only-what-each-document-needs).
* **A model that is not in the price list shows "up to $X"** instead of "unknown": the tokens used, priced at the dearest rates in the list. See [Usage costs](/trados/usage-costs/#custom-and-self-hosted-models).

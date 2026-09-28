---
title: "Reports"
---

The **Reports** tab in the Supervertaler Assistant panel is where the assistant collects structured output from its AI operations. Two kinds of thing land here: **proofreading results** and an optional **log of AI calls**.

## Running cost

*(From v18/19.20.198.)* A line under the tab's header shows what your AI calls from Trados have cost, for example:

```
AI cost: $1.23 this session (since 09:14)  ·  $4.56 today
```

It counts every AI call Supervertaler makes in Trados – Batch Translate and Proofread, Translate active segment (Alt+T), the AI Assistant chat, QuickLauncher, AutoPrompt and the memory bank selection – whether or not **Log prompts and responses** is on, and it updates as each call finishes.

* **This session** counts from when Studio started.
* **Today** comes from the [usage log](/trados/usage-costs/), so it also includes earlier sessions today and the other Studio version if you run both. It needs the usage log, which is on unless you have switched it off in AI Settings; without it, only the session figure is shown.
* Costs use the token counts your AI provider reports, where it reports them. **Up to** means a model without a price was used: its calls are counted at the most they can have cost.
* Supervertaler for memoQ keeps its own log and is not included.

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

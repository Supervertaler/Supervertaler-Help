---
title: "Reports"
---

The **Reports** tab in the Supervertaler Assistant panel is where the assistant collects structured output from its AI operations. Two kinds of thing land here: **proofreading results** and an optional **log of AI calls**.

## Proofreading results

When you run the **AI Proofreader** (the Proofread mode of [Batch Operations](/trados/batch-operations/)), each issue the AI finds is shown here as a clickable card. See [AI Proofreader](/trados/ai-proofreader/) for the full workflow and what each card contains.

Since v18.20.187 every completed run is also written to `trados\eports` in your data folder as Markdown, and **Save report\…** next to **Clear** writes a copy wherever you choose. The button is enabled only while a proofreading report is showing.

## AI operation log

When **Log prompts and responses to Reports tab** is enabled in [AI Settings](/trados/settings/ai-settings/), AI calls – Chat, Batch Translate, Batch Proofread and AutoPrompt – are recorded here together with the prompt, the response, the model used and the token/cost figures. It is the place to audit exactly what was sent to the AI provider and to review cost after the fact.

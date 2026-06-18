---
title: "Token Usage & Costs"
---

Supervertaler Workbench keeps a persistent log of the AI tokens and cost of every operation, plus a built-in **Usage & Costs** report to total and export it. Use it to answer *"how much did this project cost?"*, *"how many tokens did we use this month?"*, or *"what should I bill this client for AI?"* — across every provider, including local and custom models.

The log uses the **same format as the Supervertaler for Trados plugin**, so if you use both, their logs merge into a single analysis.

:::note
The log records **metadata only** — model, token counts, cost, project, file and language pair — and **never the prompt or response text**. That keeps the file small and safe to share.
:::

### The usage log file

Every AI call appends one line to a monthly file:

```
…\Supervertaler\workbench\usage\usage-2026-06.jsonl
```

It is **JSONL** (one JSON object per line) — open it in Excel, or parse it with a script. A line looks like:

```json
{"ts":"2026-06-18T16:07:03Z","product":"workbench","task":"BatchTranslate",
 "provider":"claude","model":"claude-sonnet-4-6","project":"My Patent Job",
 "file":"","src_lang":"English","tgt_lang":"Dutch","in_regular":654,
 "in_cache_read":0,"in_cache_write":27843,"out":808,"source":"actual",
 "cost_usd":0.11849325,"cost_known":true,"duration_s":24.9,"ok":true}
```

It is **on by default**. Turn it off in **Settings → AI Settings → AI Cost Monitoring**.

### The Usage & Costs report

Open **Tools → 💰 Token Usage & Costs…**. The window totals your usage and lets you slice it:

* **Range** — This month, Last 3 months, This year, or All time.
* **Group by** — Project, Client, Model, Provider, Task, Day or Month.

Each row shows calls, input/output tokens, cost, and a **% actual** column (the share backed by provider-reported figures rather than estimates). The footer shows the range total and your month-to-date spend against your budget.

### Exporting

**Export CSV…** and **Export Excel…** write the detailed ledger (one row per call) for the selected range — ready for invoicing or analysis.

### Settings & budget

**Settings → AI Settings → AI Cost Monitoring** has:

* **Keep a persistent token-usage log** — the on/off switch.
* **Monthly budget (USD)** — a soft monthly limit (cents allowed; `0` disables). Once this month's logged spend reaches it, starting a batch translation shows a warn-and-continue prompt. It is advisory and **never blocks**.

### Pricing custom / self-hosted models

Costs come from a single price list, `pricing.json`, shared with the Trados plugin. To price a custom or self-hosted model — or override any rate for both products at once — copy the bundled `modules/pricing.json` to `…\Supervertaler\pricing.json` and add an entry keyed by the exact model id:

```json
{ "models": { "my-university-llama": { "input": 0.0, "output": 0.0 } } }
```

Until a rate is set, a custom model's **tokens are still logged**, with the cost marked unknown rather than guessed. Local models ([Ollama](ollama.md)) are priced at `0`.

### How accurate are the figures?

Every record is flagged **`actual`** or **`estimated`** in its `source` field — and the difference matters.

* **`actual`** (the usual case): the token counts are the **exact numbers the provider's API reported** for that call — the same numbers it bills you against. These are as accurate as it gets. This covers OpenAI, Claude, Gemini, Mistral, DeepSeek and OpenRouter, including the cached-token breakdown.
* **`estimated`**: a fallback used only when the provider returned no usage data — currently **local models (Ollama)** and the occasional unparseable response. The estimate is a simple **characters ÷ 4** heuristic. It's reasonable for English but can be well off for other content: scripts such as Chinese, Japanese, Korean, Arabic and Cyrillic pack a different number of characters per token, so the estimate often *under*-counts them. Ollama is free, so for local models only the token *count* is approximate — there is no cost involved.

For **cost**, an `actual` record's figure is the exact token count × the per-model rate from `pricing.json`, with **cached tokens priced at each provider's cache discount** (e.g. Claude cache reads at 10% of the input rate and cache writes at 125%, OpenAI cache reads at 50%, Gemini 2.5+/3 at 25%). This matches how the Supervertaler for Trados plugin computes cost, so the two products agree. The one thing that can make it differ slightly from your provider's bill:

* The price list can **lag** a provider's recent rate change. The model id and the token counts are still exact — only the unit price might be a little behind.

For the definitive bill, your **provider's own usage dashboard** is authoritative. The ledger is built for tracking trends, attributing usage to projects and clients, and capacity planning — where the exact, provider-reported token counts are precisely what you want.

### See also

* [Batch Translation](batch-translation.md) — the main driver of token usage
* [Supported LLM Providers](providers.md) — which providers report usage
* [Using Local LLMs (Ollama)](ollama.md) — free, locally-run models
* [General Settings](../settings/general.md) — where AI Cost Monitoring lives

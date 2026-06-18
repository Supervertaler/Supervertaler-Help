---
title: "Token Usage & Costs"
---

Supervertaler keeps a **persistent log of the AI tokens and cost** of every operation, and a built-in **Usage & Costs report** to total and export it. This is the place to answer questions like *"how much did this project cost me?"*, *"how many tokens did we use this month?"*, or *"what should I bill this client for AI?"* — and it works for every provider, including custom and self-hosted models.

It complements the **[Reports](reports.md)** tab (which shows each call live, as you work) and the **[AI Cost Guide](ai-cost-guide.md)** (which explains how costs work). The usage log is the durable, after-the-fact record.

:::note
The usage log records **metadata only** — model, token counts, cost, project, file and language pair — and **never the prompt or response text**. That keeps the file small and safe to open in a spreadsheet or hand to an institution's monitoring team.
:::

*Added in v4.20.56.*

### The usage log file

Every AI call appends one line to a monthly file in your [Supervertaler data folder](data-folder.md):

```
…\Supervertaler\trados\usage\usage-2026-06.jsonl
```

The file is **JSONL** (one JSON object per line), so you can open it directly in Excel, parse it with a script, or load it into a notebook. A single line looks like this:

```json
{"ts":"2026-06-18T16:07:03Z","product":"trados","task":"BatchTranslate",
 "provider":"claude","model":"claude-sonnet-4-6","project":"Example project (patent, en-nl)",
 "file":"US8312383.docx.sdlxliff","client":"","src_lang":"English (United States)",
 "tgt_lang":"Dutch (Belgium)","in_regular":654,"in_cache_read":0,"in_cache_write":27843,
 "out":808,"source":"actual","cost_usd":0.11849325,"cost_known":true,"duration_s":24.9,"ok":true}
```

A few things worth knowing:

* **Every flow is covered** — Translate, Batch Translate, Quick Launcher, AutoPrompt, Proofread and Chat. A batch run is recorded as **one** line (the whole job), not one line per segment.
* **`source`** is `actual` when the figures are the real token counts reported by the provider's API, or `estimated` when they fall back to the chars/4 heuristic (see [Estimates vs actual cost](ai-cost-guide.md#estimates-vs-actual-cost)). Cache reads/writes are broken out (`in_cache_read` / `in_cache_write`).
* **`cost_known`** is `false` when the model isn't in the price list — the **tokens are still logged**, the cost just shows as unknown until you add a rate (see [Custom and self-hosted models](#custom-and-self-hosted-models)).
* It's **on by default**. Turn it off any time in **Settings → AI Settings → "Keep a persistent token-usage log"**.

### The Usage & Costs report

Open **Settings → AI Settings → "Usage & Costs report…"**. The window totals your logged usage and lets you slice it:

* **Range** — This month, Last 3 months, This year, or All time.
* **Group by** — **Project**, **Client**, **Model**, **Provider**, **Task** (Translate / Batch / Quick Launcher / …), **Day** or **Month**.

Each row shows the number of calls, input and output tokens, total tokens, cost, and a **% actual** column — the share of that group backed by provider-reported figures rather than estimates. The footer shows the **range total** and your **month-to-date spend** (against your budget, if set).

:::note
**Per-client billing.** Grouping by **Client** is only useful once each project has a client name. There is currently no in-app field for this — set it by adding a `"client": "Acme Ltd"` line to the project's file under `…\Supervertaler\trados\projects\`. Projects without one are grouped under `(none)`.
:::

### Exporting

The report's **Export CSV…** and **Export Excel…** buttons write the **detailed ledger** (one row per call, every column) for the selected range — ready for invoicing or analysis in any spreadsheet. CSV is written as UTF-8 (with a BOM, so Excel detects it correctly); Excel export produces a native `.xlsx`.

Because both Supervertaler products write the **same columns**, an LSP can concatenate the CSV/JSONL from several translators — and from both Trados and Workbench — into one analysis.

### Monthly budget

Set a soft monthly limit in **Settings → AI Settings → "Monthly budget (USD)"** (cents are allowed, e.g. `25.50`; `0` disables it).

It is **advisory and never blocks**: once this month's logged spend reaches the budget, starting a **Batch Translate** shows a *"Monthly budget reached — start anyway?"* prompt, so a large run can't slip past unnoticed. Your month-to-date spend versus the budget is also shown in the Usage & Costs report.

### Custom and self-hosted models

Costs are computed from a single price list, **`pricing.json`**, shared with Supervertaler Workbench. The bundled copy covers the built-in models. To price a **custom or self-hosted model** (or to override any rate for **both** Supervertaler products at once):

1. Copy the bundled `pricing.json` to `…\Supervertaler\pricing.json` (the shared data root), or create it there.
2. Add an entry under `models` keyed by the **exact model id** you use, with the input/output price per 1,000,000 tokens:

   ```json
   {
     "models": {
       "my-university-llama": { "input": 0.0, "output": 0.0 }
     }
   }
   ```

3. Restart Supervertaler. Its cost now appears in the log and report; until then, its **tokens are still logged** with the cost marked unknown.

Local models (Ollama) are priced at `0` — their token counts are still recorded, which is useful for capacity planning.

### See also

* [AI Cost Guide](ai-cost-guide.md) — how AI costs work, estimates vs. actual, provider dashboards
* [Reports](reports.md) — live, per-call token counts and cost as you work
* [AI Settings](settings/ai-settings.md) — where the toggle, budget and report button live
* [Batch Translate](batch-translate.md) — the main driver of token usage
* [Data folder](data-folder.md) — where the usage log and project files live

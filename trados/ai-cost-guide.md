---
title: "AI Cost Guide"
---

:::note
You are viewing help for 🧩 **Supervertaler for Trados** – the Trados Studio plugin. Looking for help with the standalone app? Visit 🖥️ [Supervertaler Workbench help](https://supervertaler.gitbook.io/help/get-started-1/workbench/).
:::

This page explains how AI costs work in Supervertaler for Trados and how to keep them under control. It deliberately avoids quoting exact per-model prices – those change often, and Supervertaler already shows you the **real, current cost** of every operation in the **Reports** tab. For exact figures, see [Estimates vs actual cost](#estimates-vs-actual-cost) below.

:::note
AI provider costs are **separate** from your Supervertaler licence. You pay the AI provider directly for the tokens your requests consume. Supervertaler does not add any markup.
:::

### Estimates vs actual cost

The **Reports** tab shows **real billed token counts and cost** as reported by your provider's API – with cache-hit tokens broken out (e.g. `830,000 in (720,000 cached) / 32,000 out · $1.36`). When the cost has no `~` prefix, that's the actual amount your provider will charge. **This is the single best place to see what you're actually spending** – it's live, per-operation, and provider-reported.

The number is cache-aware:

* **Anthropic (Claude) native + OpenRouter → Claude**: real usage from `usage.input_tokens` + `cache_creation_input_tokens` + `cache_read_input_tokens`. Cache reads are billed at 0.1× the input rate, cache writes at 1.25×.
* **OpenAI**: real `prompt_tokens` and `completion_tokens` plus `prompt_tokens_details.cached_tokens` for the auto-cache discount (50% off cached input).
* **DeepSeek**: real `prompt_tokens` / `completion_tokens` with auto-cache (90% off cached input).
* **Gemini 2.5+**: real `usageMetadata` with implicit cache (75% off cached input).

For these providers the in-app number is the authoritative billable figure (modulo any account-level credits or monthly minimums you may have).

The chars/4 estimate is still used as a fallback when the provider didn't return usage info – this affects Ollama (local, free anyway), some provider edge cases, and any response shape we couldn't parse. In those cases the cost still appears with a `~` prefix to flag it as an estimate.

If you want to cross-check against your provider's own dashboard:

| Provider                | Where to look                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| **Anthropic (Claude)**  | [platform.claude.com – Cost](https://platform.claude.com/workspaces/default/cost)         |
| **OpenAI (GPT)**        | [platform.openai.com – Usage](https://platform.openai.com/settings/organization/usage)    |
| **Google (Gemini)**     | [console.cloud.google.com – Billing reports](https://console.cloud.google.com/billing/)   |
| **xAI (Grok)**          | [console.x.ai – Usage](https://console.x.ai/team/default/usage)                           |
| **Mistral AI**          | [console.mistral.ai – Usage](https://console.mistral.ai/usage)                            |
| **OpenRouter**          | [openrouter.ai – Activity](https://openrouter.ai/activity)                                |
| **DeepSeek**            | [platform.deepseek.com – Usage](https://platform.deepseek.com/usage)                      |
| **Ollama**              | Free – local execution, no provider console.                                              |

The in-app number and the provider dashboard should agree to within rounding for any given run. If you see a meaningful gap, the most likely causes (in order) are: a provider-side credit or volume discount the in-app calculator can't see; the in-app pricing table being a little behind a recent rate change; or, for fallback (estimate) cases, the chars/4 heuristic over- or under-counting tokens for that particular language and content type.

### How costs are calculated

AI providers charge per **token** – a unit of text roughly equal to ¾ of a word. Costs depend on:

* **Input tokens** – the text you send (source segment, system prompt, terminology context)
* **Output tokens** – the text the model returns (translated segment, proofread text, generated prompt)

Because Supervertaler translates **segment by segment**, the system prompt and terminology context are included with every segment. For a typical 5,000-word document (\~250 segments), the token usage works out roughly like this:

| Task                | Input tokens | Output tokens |
| ------------------- | ------------ | ------------- |
| **Batch Translate** | \~125,000    | \~8,000       |
| **AI Proofreader**  | \~140,000    | \~8,000       |
| **AutoPrompt**      | \~10,000     | \~2,000       |

These are estimates for a representative document – actual usage varies with segment length, terminology context size, and prompt complexity. Token counts like these are fairly stable; what changes is the **price per token**, which is why this guide points you to live figures rather than quoting them.

### How much will it cost?

There's a wide spread between models. As a rough mental model:

* **Local models (Ollama)** are **free** – they run on your own computer, with no API charges at all. The trade-off is that quality depends on your hardware, and they're generally less capable than cloud-hosted models. If you have a computer with 8+ GB of RAM, TranslateGemma 12B delivers surprisingly good results for free.
* **Budget cloud models** – the "Mini", "Flash-Lite" and "Small" tier from each provider (e.g. GPT-5.4 Mini, Gemini 3.1 Flash-Lite, Mistral Small, Claude Haiku 4.5) – typically cost a small fraction of a cent per segment. They're excellent for routine, high-volume translation.
* **Flagship models** – Claude Opus 4.7, GPT-5.5, Gemini 3.1 Pro and the like – can run roughly 10–50× the price of the budget tier. Reserve them for specialised content where the quality difference earns its keep.

To see what a model **actually** costs for your work, run one operation and check the **Reports** tab – it shows the real billed cost. For OpenRouter, expect the underlying provider's rate plus a small platform fee.

### Our recommendation

:::tip
**If you could only pick one model for everything – translation, proofreading, and chat – we would recommend Claude Sonnet 4.6.** It follows translation instructions precisely, handles terminology constraints well, is fast enough for batch operations, and delivers consistently high quality across legal, technical, and general content – at a cost that works out to a small fraction of a cent per segment.
:::

For budget-conscious batch work, **GPT-5.4 Mini** or **Gemini 3.1 Flash-Lite** offer excellent quality at a fraction of the price. For the absolute highest quality on specialised content, **Claude Opus 4.7** or **GPT-5.5** are worth the premium.

### Token pricing

Supervertaler's in-app cost figures come from a built-in per-token pricing table. Because provider prices change regularly, that table is occasionally a little behind a recent rate change – the **Reports** tab's provider-reported figures are always the authoritative ones. For the definitive current rates, check the provider's own pricing page:

[OpenAI](https://openai.com/api/pricing/) · [Anthropic](https://www.anthropic.com/pricing#anthropic-api) · [Google Gemini](https://ai.google.dev/gemini-api/docs/pricing) · [xAI](https://docs.x.ai/developers/models) · [Mistral](https://mistral.ai/technology/) · [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/) · [OpenRouter](https://openrouter.ai/models)

### Tips for managing costs

* **Start with a budget model** – GPT-5.4 Mini, Gemini 3.1 Flash-Lite, or Mistral Small are excellent for routine translation at a fraction of the cost of a flagship.
* **Use premium models selectively** – reserve GPT-5.5, Claude Opus 4.7, or Gemini 2.5 Pro for specialised content (legal, medical, patents) where the quality difference justifies the cost.
* **Try Ollama for zero cost** – if you have a computer with 8+ GB of RAM, TranslateGemma 12B delivers surprisingly good results for free.
* **Check your usage** – the **Reports** tab in Supervertaler Assistant lists every AI call with its token count and cost, and your provider's own console (see the [Estimates vs actual cost](#estimates-vs-actual-cost) table above) shows the authoritative billable figure.

### Built-in cost protection

Supervertaler includes several safeguards to help you avoid unexpected costs:

#### QuickLauncher prompts are standalone

When you run a prompt from the QuickLauncher menu (Ctrl+Q), only the prompt itself is sent to the AI – **not the chat history**. This means a simple terminology query costs only what it needs to, even if you have a long conversation in the chat window.

#### Chat token budget

Regular chat messages include recent conversation history so the AI can follow your discussion. However, Supervertaler automatically trims older messages when the history grows too large (\~50,000 tokens). This prevents costs from spiralling when previous messages contained large context blocks (e.g. full document content).

#### Cost warning

If a request is estimated to cost more than $0.50 in input tokens, a confirmation dialogue appears showing the estimated token count and cost. You can cancel before the expensive request is sent.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

:::note
**Keep an eye on the cost indicators.** Every AI response in the chat shows the estimated token count and cost. You can also review all prompts and their costs in the **Reports** tab.
:::

#### Choosing the right model

For everyday work – chat queries, terminology questions, QuickLauncher prompts – use **GPT-5.4 Mini** or another budget model. Reserve premium models like **GPT-5.5** or **Claude Opus 4.7** for AutoPrompt and complex tasks where the quality difference justifies the cost.

### See also

* [AI Settings](settings/ai-settings.md) – configure your API keys and choose a model
* [Batch Translate](batch-translate.md) – translate segments in bulk
* [AI Proofreader](ai-proofreader.md) – proofread translated segments
* [AutoPrompt](generate-prompt.md) – generate translation prompts
* [Licensing & Pricing](licensing.md) – Supervertaler subscription plans

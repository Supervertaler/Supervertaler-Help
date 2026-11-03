---
title: "Providers"
---

Supervertaler supports multiple AI providers so you can choose what fits your workflow and budget. You only need one to get started.

## Cloud providers

### OpenAI

Models: **GPT-6 Astra**, **GPT-6.1 Sol**, **GPT-6 Luna**

Get an API key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys). GPT-6.1 Sol is the recommended default: close to Astra's quality at a fifth of its price. GPT-6 Astra is OpenAI's most capable model, for the hardest work; GPT-6 Luna is the cheapest, for high-volume work.

### Anthropic (Claude)

Models: **Claude Sonnet 5.5**, **Claude Opus 5.5**, **Claude Fable 5.1**

Get an API key at [console.anthropic.com](https://console.anthropic.com). Claude Sonnet 5.5 is the recommended default. Opus 5.5 gives the highest quality for hard legal and technical work; Fable 5.1 is Anthropic's most capable model overall, at 2.5 times Opus's price.

### Google (Gemini)

Models: **Gemini 3.1 Flash-Lite**, **Gemini 3.5 Flash**, **Gemini 2.5 Pro**, **Gemini 3.1 Pro (Preview)**, **Gemini 4 Argon**, **Gemma 4 26B MoE**

Get an API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey). Gemini 3.1 Flash-Lite offers a generous free tier and is a strong choice for high-volume work. Gemini 4 Argon (from v1.10.375) is Google's most capable model.

### Mistral AI

Models: **Mistral Large**, **Mistral Small**

Get an API key at [console.mistral.ai](https://console.mistral.ai). Particularly strong on European languages.

### DeepSeek

Models: **DeepSeek V4 Pro**, **DeepSeek V4 Flash**

Get an API key at [platform.deepseek.com](https://platform.deepseek.com). DeepSeek offers competitive pricing and strong multilingual quality. V4 Flash is the fast, cost-effective option for high-volume work.

## Gateway providers

### OpenRouter

[OpenRouter](https://openrouter.ai) is an API gateway that gives you access to 200+ models from OpenAI, Anthropic, Google, DeepSeek, Mistral, Meta, and many others – all through a **single API key**.

The model dropdown includes a curated selection for translation, and you can also type any OpenRouter model ID directly. Browse all models at [openrouter.ai/models](https://openrouter.ai/models).

From v1.10.375 the dropdown offers the same models as Supervertaler for Trados and for memoQ, with Claude Sonnet 5.5 as the default. If the model you chose has left the list, Settings shows it as "your current model" and keeps it. Providers of free models, such as Qwen 3.8 27B (Free), may keep what you send, so don't use them for confidential work.

Get an API key at [openrouter.ai/keys](https://openrouter.ai/keys).

:::note
OpenRouter adds a 5.5% platform fee on top of the underlying provider's price. For most translation jobs this adds only a few cents.
:::

## Local providers

### Ollama

Run models entirely on your own machine – no API key and no internet required.

See [Ollama Setup](/workbench/ai-translation/ollama/) for download and configuration instructions.

## Custom (OpenAI-compatible)

For any provider that exposes an OpenAI-compatible API (Azure OpenAI, together.ai, local inference servers, etc.), select **Custom (OpenAI-compatible)** and enter the endpoint URL, model name, and API key.

---

## Related pages

- [Setting Up API Keys](/workbench/get-started/api-keys/)
- [Ollama Setup](/workbench/ai-translation/ollama/)
- [AI Translation Overview](/workbench/ai-translation/overview/)

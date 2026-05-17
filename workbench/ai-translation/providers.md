---
title: "Providers"
---

:::note
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
:::

Supervertaler supports multiple AI providers so you can choose what fits your workflow and budget. You only need one to get started.

## Cloud providers

### OpenAI

Models: **GPT-5.5**, **GPT-5.4 Mini**

Get an API key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys). GPT-5.4 Mini is a good starting point – fast, affordable, and high quality for most translation tasks. GPT-5.5 is the flagship for the most demanding work.

### Anthropic (Claude)

Models: **Claude Sonnet 4.6**, **Claude Haiku 4.5**, **Claude Opus 4.7**

Get an API key at [console.anthropic.com](https://console.anthropic.com). Claude Sonnet 4.6 is the recommended default. Haiku 4.5 is the fastest and cheapest option; Opus 4.7 is the most capable.

### Google (Gemini)

Models: **Gemini 3.1 Flash-Lite**, **Gemini 2.5 Pro**, **Gemini 3.1 Pro (Preview)**, **Gemma 4 26B MoE**

Get an API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey). Gemini 3.1 Flash-Lite offers a generous free tier and is a strong choice for high-volume work.

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

Get an API key at [openrouter.ai/keys](https://openrouter.ai/keys).

:::note
OpenRouter adds a 5.5% platform fee on top of the underlying provider's price. For most translation jobs this adds only a few cents.
:::

## Local providers

### Ollama

Run models entirely on your own machine – no API key and no internet required.

See [Ollama Setup](ollama.md) for download and configuration instructions.

## Custom (OpenAI-compatible)

For any provider that exposes an OpenAI-compatible API (Azure OpenAI, together.ai, local inference servers, etc.), select **Custom (OpenAI-compatible)** and enter the endpoint URL, model name, and API key.

---

## Related pages

- [Setting Up API Keys](../get-started/api-keys.md)
- [Ollama Setup](ollama.md)
- [AI Translation Overview](overview.md)

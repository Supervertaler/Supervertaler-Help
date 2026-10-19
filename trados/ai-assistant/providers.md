---
title: "Providers"
---

The Supervertaler Assistant supports multiple AI providers. You only need one to get started.

## Switching Models

The current provider and model are shown in the status area at the bottom of the chat panel. You can switch models in two ways:

* **Quick switch** – click the provider/model label directly. A dropdown menu appears with all available models grouped by provider. The current model is marked with a tick. Select a different model to switch instantly.
* **Settings** – open the settings dialogue (gear icon) and switch to the **AI Settings** tab for full configuration including API keys, endpoints, and advanced options.

## Supported Providers

| Provider | Models |
| -------- | ------ |
| **OpenAI** | GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna |
| **Anthropic** | Claude Sonnet 5.5, Claude Opus 5.5, Claude Fable 5.1 |
| **Google** | Gemini 3.8 Flash, Gemini 3.5 Flash-Lite, Gemini 3.1 Pro (Preview) |
| **Grok** | Grok 4.3 |
| **Mistral** | Mistral Large, Mistral Small |
| **DeepSeek** | DeepSeek V4 Pro, DeepSeek V4 Flash |
| **OpenRouter** | Claude, GPT, Gemini, DeepSeek, and 200+ others via a single API key |
| **Ollama** | TranslateGemma, Qwen 3, Aya Expanse (local, no API key needed) |
| **Custom** | Any OpenAI-compatible API endpoint |

:::note
If you want privacy or offline use, try **Ollama** with a local model. No API key or internet connection needed. Ollama models whose names end in `-cloud` are the exception: they run on Ollama's servers, so your text leaves your computer.

If you prefer a single account that covers many providers, **OpenRouter** gives you access to 200+ models with one key.
:::

## Local models: what to expect

A local model keeps every word on your computer, but expect less than from the large cloud models. In a test on a published Dutch patent, Gemma 4 31B, about the largest model a well-equipped PC can run, wrote fluent and mostly accurate English, but its terminology drifted from one batch to the next, which broke the consistency of the claims. Models of 7 to 8 billion parameters were not good enough for patent work at all. Claude Opus 5.5 stayed consistent throughout.

- **Speed:** without a graphics card a local model is slow. Reading Supervertaler's instructions before the first segment can take 10 to 15 minutes; a model of about 30 billion parameters needs around 24 GB of graphics memory to run at a usable speed.
- **What narrows the gap:** termbases ticked for AI, and house rules in [SuperMemory](/trados/ai-assistant/super-memory/). In the same test, a local model applied six patent conventions it had been getting wrong as soon as they were in the shared memory bank.
- **Test it on your own work:** [SuperBench](/trados/superbench/) translates the same segments with three models and has a fourth judge them.

The full test, with every paragraph side by side, is on supervertaler.com: [Can a local AI model translate a patent?](https://supervertaler.com/articles/local-ai-patent-test/)

## Choosing a Model

For everyday translation questions, a smaller and cheaper model like **GPT-6 Luna**, **Gemini 3.5 Flash-Lite**, or **DeepSeek V4 Flash** works well. For complex tasks like document analysis, prompt generation, or when you need the highest quality suggestions, use a larger model like **Claude Sonnet 5.5**, **GPT-6 Astra**, or **DeepSeek V4 Pro**.

Some features are provider-specific:

| Feature | Availability |
| ------- | ------------ |
| [Studio Tools](/trados/ai-assistant/studio-tools/) | All providers except Ollama. GPT-6.1 Sol only with your own OpenAI key, not through OpenRouter (from v18/19.20.201; in v18/19.20.199 and 200, not GPT-6.1 Sol at all) |
| Image attachments | All providers with vision support |
| Document attachments | All providers |
| [Memory bank](/trados/ai-assistant/super-memory/ai-integration/) context | All providers |

## See Also

* [Supervertaler](/trados/ai-assistant/) – Overview
* [AI Settings](/trados/settings/ai-settings/) – API keys, endpoints, advanced options
* [AI Cost Guide](/trados/ai-cost-guide/) – Token pricing and cost estimates

---
title: "Using Local LLMs (Ollama)"
---

Ollama lets you run LLMs locally for privacy and offline translation.

## Install Ollama

1. Download and install from https://ollama.ai
2. Start Ollama
3. Pull a model (example):

```bash
ollama pull llama3
```

## Use in Supervertaler

Once Ollama is installed and running, Supervertaler can use it as a provider. In **Settings → 🤖 AI Settings**, choose **🖥️ Local LLM (Ollama - runs on your computer)** under **🤖 LLM Provider Selection**. If Ollama runs somewhere other than the usual `http://localhost:11434`, enter its address under **🔑 LLM API Keys → Ollama Endpoint**.

:::note
Local models vary a lot in quality. For best results, test a few models on your typical content.
:::

## Advanced settings

**Settings → 🤖 AI Settings → 🖥️ Local LLM (Ollama) Advanced Settings** has two options:

- **Keep model warm (prevent unloading)** – Ollama normally unloads a model after 5 minutes without use, so the next translation has to wait for it to load again. With this ticked, Supervertaler pings Ollama every 4 minutes to keep the model in memory. The drawback is that the model keeps using RAM even when you aren't translating.
- **Request timeout** – how long Supervertaler waits for Ollama to answer a single request. On **Automatic** (the default) that is 3 to 10 minutes, depending on the model's size and the length of the prompt. A local model on a computer without a dedicated GPU can need much longer than that for one batch request, so you can set anything from 1 minute to 1440 minutes (24 hours). The timeout applies to every Ollama request: batch and single-segment translation, the [Chat](/workbench/ai-translation/chat/) assistant and QuickTrans.

Like every Settings page, these save themselves a moment after you change them, and a new timeout takes effect straight away.

:::tip
If a translation stops with "Ollama request timed out", raise the **Request timeout** – the error message points you to the setting. A smaller model also helps.
:::

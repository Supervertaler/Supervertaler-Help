---
title: "Custom MT endpoint"
---

A **Custom MT endpoint** lets you add your own OpenAI-compatible machine-translation service to QuickTrans, alongside the built-in engines (Google, DeepL, Microsoft, …). It is most useful for a **local MT proxy** – a small server that exposes several free MT engines behind a single OpenAI-compatible API – so you can query them all from Workbench without per-engine API keys.

It is deliberately separate from the **AI custom endpoint** used for the AI Assistant chat, so you can run an MT proxy for quick lookups *and* point the AI chat at a different custom LLM at the same time.

## When to use it

- You run (or have access to) an OpenAI-compatible endpoint that returns translations, e.g. a local MT proxy that maps a `model` name to a specific engine (`google`, `sogou`, `cnpat`, …).
- You want fast, free MT in QuickTrans without configuring each engine's official API key.
- You want more than one such endpoint – for example a general proxy and a patent-specific one – each appearing as its own QuickTrans result.

## Set it up

1. Open **Workbench Settings → ⚡ QuickTrans**.
2. Under **MT engines**, tick **Custom MT endpoint (OpenAI-compatible)**.
3. Click **+** next to *Profile* and give the profile a name (e.g. `Local proxy`).
4. Fill in:
   - **Endpoint URL** – the OpenAI-compatible base URL, e.g. `http://127.0.0.1:1234/v1`
   - **Model / engine** – the model (or, for a multi-engine proxy, the engine name, e.g. `google`)
   - **API key** – only if your endpoint requires one; leave blank otherwise
   - **Show this profile in QuickTrans** – tick to include this profile as a QuickTrans result; untick to keep it configured but hidden
5. Click **💾 Save QuickTrans Settings**.

Each profile that is enabled (**Show this profile in QuickTrans** ticked) and has an endpoint appears as its own result in the QuickTrans popup (summoned with **Ctrl+Alt+Q**). Add more profiles with **+** to expose several engines at once; remove one with **−**.

:::note
The "Custom MT endpoint" checkbox is the master on/off for the whole feature; the per-profile "Show this profile in QuickTrans" checkbox lets you pick which of your saved profiles actually appear, so you can keep several configured but show only the ones you want.
:::

:::note
The endpoint must be OpenAI **chat-completions** compatible (it receives a `POST` to `/v1/chat/completions` with `messages` and a `model`, and returns the translation as the assistant message). Workbench sends a strict "translate only" prompt, so the endpoint should return just the translated text.
:::

## Example: a local multi-engine MT proxy

A common pattern is a small Python proxy that wraps free web MT engines and presents them as OpenAI "models". Run it locally (e.g. on `http://127.0.0.1:1234`), then add a Custom MT profile per engine you want, setting **Model / engine** to the engine name the proxy expects.

:::note
Free, unofficial web MT services are best-effort: availability and quality can vary, and they may rate-limit without notice. A proxy keeps that handling outside Workbench. Use each service in line with its own terms, and prefer an official provider API for production work.
:::

## Free Dutch ↔ English engines (via a multi-engine proxy)

If your proxy exposes several engines as "models", set **Model / engine** to the engine's key. For Dutch ↔ English, these work well:

| Model / engine | Notes |
|---|---|
| `google` | Reliable, fast. |
| `microsoft_builtin` | Reliable; good Dutch. |
| `modernmt_builtin` | Reliable. |
| `lingvanex_builtin` | Works; quality varies. |
| `deepl_builtin` | Free DeepL — excellent quality **when available**, but the free endpoint rate-limits aggressively (HTTP 429), so it may intermittently fall back to another engine. |

China-focused engines (`sogou`, `transmart`, `niutrans`) and the patent engine `cnpat` are not recommended for Dutch ↔ English.

:::note
These are free, best-effort services and their availability and quality vary; `deepl_builtin` in particular can be throttled. For dependable, production-grade DeepL, use the official DeepL engine (with an API key) built into Workbench's MT settings.
:::

## Custom MT vs the AI custom endpoint

| | Custom MT endpoint | AI custom endpoint |
|---|---|---|
| Lives in | QuickTrans ▸ MT engines | AI Settings ▸ AI/LLM Providers |
| Used for | Fast MT results in QuickTrans | AI Assistant chat & AI translation |
| Independent? | Yes – configure both at once | Yes |
| Profiles | Multiple, each a QuickTrans result | Multiple, one active at a time |

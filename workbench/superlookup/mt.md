---
title: "Mt"
---

:::note
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
:::

Machine translation is delivered by the **QuickTrans Popup** – an always-on-top popup window with translations from every enabled provider, summoned independently of the SuperLookup tab. See [QuickTrans Popup](../sidekick/quicktrans-popup.md) for the full reference.

## Opening QuickTrans

| How | Notes |
|-----|-------|
| **Ctrl+Alt+Q** (⌘⌥Q on macOS) | Opens the QuickTrans always-on-top popup and starts the MT fan-out immediately on the selected text. Auto-copies the current selection so you don't need a separate Ctrl+C first. |
| **Ctrl+M** | Same popup, but uses the current Workbench grid-cell text (no selection needed). |
| Editor right-click → ⚡ QuickTrans | Right-click menu in the editor. |
| **🔍 Run in SuperLookup** button in the popup header | After you've seen the QuickTrans results, click 🔍 to hand the same query off to Workbench's SuperLookup tab for a richer concordance / termbase / web look-up. |

## Providers

QuickTrans supports these MT providers (subject to your API keys and per-provider on/off flags):

- DeepL
- Google Translate
- Microsoft Translator
- Amazon Translate
- ModernMT
- MyMemory (free)

Plus optional LLM-based "translation as suggestion" from Claude, OpenAI, Gemini, Mistral, DeepSeek, and a custom OpenAI-compatible endpoint or local Ollama model.

## Configure providers

QuickTrans's provider list and LLM model selectors live in **Workbench Settings → ⚡ QuickTrans**. Click the ⚙ cog icon in the QuickTrans popup header to jump there in one click.

Per-provider on/off + LLM model choices persist in `general_settings.json` under `mt_quick_lookup`.

## Language behaviour

- QuickTrans uses the active project's language pair by default.
- The popup has its own From / To dropdowns – override per-query without affecting your project settings.

## Performance

Provider calls run in parallel (each with a 5 s timeout, overall batch capped at 6 s) so total wall-clock is roughly the slowest single provider, not the sum. Results appear in the popup as they arrive – the first to finish is auto-selected so you can hit Enter without waiting for the slow providers.

## Copying results

- Successful results show a **📋 copy button**.
- You can also **double-click** a result row to copy the translation.
- Number keys **1**–**9** select the corresponding result (1 = first, 2 = second, etc.).

:::note
If a provider call fails, QuickTrans shows the error message in red. Failed providers don't block the others.
:::

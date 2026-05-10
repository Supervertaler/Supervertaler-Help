{% hint style="info" %}
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
{% endhint %}

Machine translation in SuperLookup is delivered by the **QuickTrans** sub-tab. QuickTrans queries multiple MT providers (and optionally LLM providers) in parallel and shows the results side by side, ranked by provider.

## Opening QuickTrans

| How | Notes |
|-----|-------|
| **Ctrl+Alt+Q** | Opens Sidekick directly to the QuickTrans sub-tab and starts the MT fan-out immediately on the selected text. |
| **Ctrl+Alt+L** then click the QuickTrans sub-tab | Or set QuickTrans as your default landing tab in **SuperLookup Settings → "Ctrl+Alt+L lands on"**. |

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

QuickTrans's provider list and LLM model selectors live in **SuperLookup Settings → ⚡ QuickTrans** sub-sub-tab inside the Sidekick. Earlier versions kept this page in **Workbench Settings → ⚡ QuickTrans**; that location is now a stub with an **Open in Sidekick** button that takes you to the new place in one click.

Per-provider on/off + LLM model choices persist in `general_settings.json` under `mt_quick_lookup`.

## Language behaviour

- If **From / To** are set in SuperLookup's language dropdowns, QuickTrans uses that language pair.
- If **From / To = Any**, QuickTrans falls back to the active project's language pair.

## Performance

QuickTrans is deferred unless your Ctrl+Alt+L landing tab is QuickTrans. If you land on Termbases (the default), MT only fires when you actually navigate to the QuickTrans sub-tab, so you don't pay for HTTP calls whose results you may never look at. Press Ctrl+Alt+Q for the dedicated "fire immediately" path.

Provider calls run in parallel (each with a 5 s timeout, overall batch capped at 6 s) so total wall-clock is roughly the slowest single provider, not the sum.

## Copying results

- Successful results show a **📋 copy button**.
- You can also **double-click** a result row to copy the translation.
- Number keys **1**–**9** select the corresponding result (1 = first, 2 = second, etc.).

{% hint style="info" %}
If a provider call fails, QuickTrans shows the error message in red. Failed providers don't block the others.
{% endhint %}

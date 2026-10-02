---
title: "Machine Translation"
---

Machine translation is delivered by **QuickTrans** – an always-on-top popup (and dockable panel) with translations from every enabled provider. See [QuickTrans](/workbench/quicktrans/overview/) for the full reference.

## Opening QuickTrans

| How | Notes |
|-----|-------|
| **Ctrl+Alt+Q** (⌘⌥Q on macOS) | Opens the QuickTrans always-on-top popup and starts the MT fan-out immediately on the selected text. Auto-copies the current selection so you don't need a separate Ctrl+C first. |
| Grid cell right-click → **⚡ QuickLauncher** → **⚡ QuickTrans** | Right-click menu in the editor. |
| **🔍 Run in SuperLookup** button in the popup | After you've seen the QuickTrans results, click 🔍 to hand the same query off to Workbench's SuperLookup tab for a richer concordance / termbase / web look-up. |

## Providers

QuickTrans supports these MT providers (subject to your API keys and per-provider on/off flags):

- DeepL
- Google Translate
- Microsoft Translator
- Amazon Translate
- ModernMT
- MyMemory (free)
- Your own OpenAI-compatible MT service – see [Custom MT endpoint](/workbench/quicktrans/custom-mt-endpoint/)

Plus optional AI "translation as suggestion" from Claude, OpenAI, Gemini, Mistral, DeepSeek, OpenRouter, a custom OpenAI-compatible endpoint or a local Ollama model.

The MT engines' API keys are entered in **Settings → 🌐 MT Settings**; the AI providers reuse the keys in **Settings → 🤖 AI Settings**.

### DeepL keys

DeepL gives out two kinds of key, and from v1.10.373 both work in the **DeepL** field:

- **A DeepL API key** (API Free or API Pro), from [deepl.com/pro-api](https://www.deepl.com/pro-api).
- **The authentication key for CAT tools** that comes with a **DeepL Pro Advanced or Ultimate** subscription. You find it in your DeepL account under **Account → Authentication key for CAT tools**.

DeepL accepts the CAT-tool key only on an older version of its interface. When DeepL refuses a key, Supervertaler tries that version and, if the key works there, uses it for that key from then on. Before v1.10.373, only API keys worked, and a CAT-tool key gave an authorization error.

## Configure providers

QuickTrans's provider list and LLM model selectors live in **Workbench Settings → ⚡ QuickTrans**. Click the ⚙️ cog icon in the QuickTrans popup to jump there in one click.

There's no Save button: since v1.10.372 each change is saved a moment after you make it, together with the rest of Workbench's settings in `settings.json`. The same page also decides whether the popup fetches AI providers automatically or shows a **Fetch** button for each – see [QuickTrans](/workbench/quicktrans/overview/#ai-providers-automatic-or-on-request).

## Language behaviour

- QuickTrans uses the active project's language pair by default (or the default pair in **Settings → 🌐 Language Pair** when no project is open).
- Text in the project's target language is detected and translated back into the source language.
- The popup's **Languages:** row has its own source and target dropdowns and a **⇄** swap button. Changing them fetches the translations again, without affecting your project settings. The choice sticks for later popups until the project's (or the default) language pair changes.

## Performance

Provider calls run in parallel, so the total wait is roughly the slowest single provider, not the sum. Results appear in the popup as they arrive – the first successful one is auto-selected so you can hit Enter without waiting for the slow providers.

## Using a result

- **Click** a result, or press **Enter** on the selected one, to insert it.
- Number keys **1**–**9** insert the corresponding result (1 = first, 2 = second, etc.).
- From another application, the chosen translation is pasted over your selection there; inside Workbench it goes into the current segment's target.

:::note
If a provider call fails, QuickTrans shows the error message in red. Failed providers don't block the others.
:::

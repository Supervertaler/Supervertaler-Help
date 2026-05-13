{% hint style="info" %}
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
{% endhint %}

The **QuickTrans Popup** is a small always-on-top window that shows machine translations of the currently-selected text from every enabled provider, all at once. Select text anywhere on your computer, press the QuickTrans hotkey, and the popup appears with translations streaming in as each provider responds.

It's a single-purpose surface – just translations, no chat – and it stays on top of every other window until you press 1–9 / Enter / click to pick a result, or Esc to dismiss.

## Opening QuickTrans

| Method | Shortcut | Notes |
| --- | --- | --- |
| Global, from any application | **Ctrl+Alt+Q** (⌘⌥Q on macOS) | Auto-copies the current selection; popup appears with translations |
| In-app, from a Workbench grid cell | **Ctrl+Alt+Q** | Same chord – Ctrl+Alt+Q is registered both as a system-wide global hotkey *and* as an in-app QShortcut, so it works wherever you are |
| Editor right-click → ⚡ QuickTrans | Right-click menu | Uses the selected text in the cell (or the full cell text if no selection) |

After selecting a translation from the global path (Ctrl+Alt+Q from another app), the popup hides itself, returns focus to the source application, and pastes the result over your selection. When invoked in-app, selecting a translation inserts it at the cursor position in the focused grid cell.

## The popup header

A row of three controls runs along the top of the popup:

* **⚡ Supervertaler QuickTrans** – title
* **🔍 Run in SuperLookup** – closes the popup and opens Workbench's SuperLookup tab with the same query pre-filled and the search auto-fired. Useful when you've translated a phrase via QuickTrans and then think "actually, I want to look this up in my TMs / termbases / web resources too" – one click instead of dismissing the popup and pasting the query again
* **⚙ Settings** – opens Workbench Settings → ⚡ QuickTrans so you can enable / disable providers and pick LLM models

## Translation results

Results arrive as they complete from each provider and are displayed in a numbered list. The first result to arrive is automatically selected, so for the typical "fast provider → press Enter" flow you don't need to wait for the slow ones.

| Method | Action |
| --- | --- |
| **Press 1–9** | Insert the numbered translation immediately |
| **Arrow keys + Enter** | Navigate and select |
| **Click** | Insert the translation |
| **Esc** | Dismiss the popup without inserting |

Each translation row shows the provider name on the left and the translated text on the right.

## Supported providers

QuickTrans queries up to eleven providers in parallel. Each one is independently enabled / disabled in **Workbench Settings → ⚡ QuickTrans**.

**Machine translation engines** (each row needs an API key for that service, except MyMemory):

| Engine | API key required? |
| --- | --- |
| Google Translate | Yes |
| DeepL | Yes |
| Microsoft Translator | Yes |
| Amazon Translate | Yes |
| ModernMT | Yes |
| MyMemory | No (free, rate-limited) |

**LLM providers** (each row needs an API key for that service; reuses the keys configured in Settings → AI Settings):

| Provider | Notes |
| --- | --- |
| Claude | Pick the model in Settings → ⚡ QuickTrans (e.g. claude-haiku-4-5 vs claude-sonnet-4-6) |
| OpenAI | Pick the model (e.g. gpt-4o-mini vs gpt-4o) |
| Gemini | Pick the model |
| Ollama | Local-only; uses the active Ollama model |
| Custom | One configurable OpenAI-compatible endpoint (URL + model) |

The LLM providers are **disabled by default** – tick them in Settings → ⚡ QuickTrans if you want LLM-based "translation as suggestion" alongside the MT engines. (Ticking all eleven makes for a slow popup; most users keep three or four MT engines plus one LLM.)

## Language pair

QuickTrans uses **the active project's source and target language**. There's no per-query language override in the popup itself – set the language pair at the project level and QuickTrans inherits it.

If no project is open, QuickTrans falls back to English → Dutch (the default for unconfigured installs).

## Configuring providers

Open **Workbench → Settings → ⚡ QuickTrans** (or click the ⚙ cog in the popup header) to enable / disable individual providers and pick LLM models. The settings live in `general_settings.json` under the `mt_quick_lookup` key and persist across restarts.

Tick a provider, save, then trigger Ctrl+Alt+Q again – the popup picks up the new provider list the next time it opens.

## Tips

* **Ctrl+Alt+Q is the fastest way to translate** – select text anywhere, press the shortcut, results appear instantly. The synthetic Ctrl+C happens internally, so you don't need to copy first.
* **Use the 🔍 Run in SuperLookup hand-off** for terminology questions. QuickTrans is great for "how does this phrase translate?", SuperLookup is great for "have I translated this term before? what does it mean? is it in a glossary?".
* **The popup lives on top of every other window**, so you can summon it from a browser, a PDF reader, your CAT tool, or anywhere – it overlays whatever's foreground.
* **Different from Chat.** QuickTrans gives you N parallel translations from N providers; the Chat tab in Workbench's right panel is a conversational AI assistant. Use QuickTrans when you want options, Chat when you want a conversation.

## Customising the hotkey

The QuickTrans chord can be rebound in **Settings → Keyboard Shortcuts**. The action is called *QuickTrans (instant translation popup)*, default **Ctrl+Alt+Q**. The same chord registers as both an in-app QShortcut and an OS-level global hotkey, so changing it once changes both.

## Related pages

* [Companion Tabs Overview](overview.md)
* [Trados-aware Chat](trados-aware-chat.md)
* [SuperLookup Overview](../superlookup/overview.md)
* [Machine Translation in SuperLookup](../superlookup/mt.md)
* [Keyboard Shortcuts](../settings/shortcuts.md)

{% hint style="info" %}
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
{% endhint %}

The **QuickTrans Popup** is a small always-on-top window that shows machine translations of the currently-selected text from every enabled provider (Google Translate, DeepL, Microsoft, MyMemory, plus Claude, OpenAI, Gemini, Ollama, and any custom provider) all at once. Select text anywhere on your computer, press the QuickTrans hotkey, and the popup appears with translations streaming in as each provider responds.

It's a single-purpose surface – just translations, no chat – and it stays on top of every other window until you press 1–9 / Enter / click to pick a result, or Esc to dismiss.

## Opening QuickTrans

| Method | Shortcut | Notes |
| --- | --- | --- |
| Global, from any application | **Ctrl+Alt+Q** (⌘⌥Q on macOS) | Auto-copies the current selection; popup appears with translations |
| In-app, from a Workbench grid cell | **Ctrl+M** | Same popup; uses the text in the current cell |
| Editor right-click → ⚡ QuickTrans | Right-click menu | Uses the selected text in the cell |

After selecting a translation, the popup hides itself, returns focus to the source application, and pastes the result over your selection.

## The popup header

A row of three controls runs along the top of the popup:

* **⚡ Supervertaler QuickTrans** – title
* **🔍 Run in SuperLookup** – closes the popup and opens Workbench's SuperLookup tab with the same query pre-filled and the search auto-fired. Useful when you've translated a phrase via QuickTrans and then think "actually, I want to look this up in my TMs / termbases / web resources too" – one click instead of dismissing the popup and pasting the query again
* **⚙ Settings** – opens Workbench Settings → ⚡ QuickTrans so you can enable / disable providers

## Translation results

Results arrive as they complete from each provider and are displayed in a numbered list with provider icons. The first to finish is automatically selected (highlighted in blue) so you can hit Enter to insert it without waiting for slower providers.

| Method | Action |
| --- | --- |
| **Press 1–9** | Insert the numbered translation immediately |
| **Arrow keys + Enter** | Navigate and select |
| **Click** | Insert the translation |
| **Esc** | Dismiss the popup without inserting |

Each translation row shows the provider name (Google Translate, Gemini, OpenAI, etc.) on the left and the translated text on the right.

## Configuring providers

Open **Workbench → Settings → ⚡ QuickTrans** (or click the ⚙ cog in the popup header) to enable / disable individual providers. The settings live in the same place as the rest of Workbench's settings; the popup picks up changes the next time it opens.

You can also configure:

* **Maximum providers** – cap on how many results to fetch at once (saves API calls)
* **Language pair** – defaults to your project's source / target; can be overridden per-query
* **Per-provider model / endpoint** – for the AI providers, choose which model to call (e.g. `gpt-4o-mini` vs `gpt-4o`, `claude-haiku-4-5` vs `claude-sonnet-4-6`)

## Tips

* **Ctrl+Alt+Q is the fastest way to translate** – select text anywhere, press the shortcut, results appear instantly. The synthetic Ctrl+C happens internally, so you don't need to copy first.
* **Use the 🔍 Run in SuperLookup hand-off** for terminology questions. QuickTrans is great for "how does this phrase translate?", SuperLookup is great for "have I translated this term before? what does it mean? is it in a glossary?".
* **The popup lives on top of every other window**, so you can summon it from a browser, a PDF reader, your CAT tool, or anywhere – it overlays whatever's foreground without stealing focus from the source app for the typing-back step.
* **Different from Chat.** QuickTrans gives you N parallel translations from N providers; the Chat tab in Workbench's right panel is a conversational AI assistant. Use QuickTrans when you want options, Chat when you want a conversation.

## Customising the hotkeys

You can change the default keyboard shortcuts in **Settings → Keyboard Shortcuts**:

| Default shortcut | Action |
| --- | --- |
| **Ctrl+Alt+Q** (⌘⌥Q on macOS) | Open QuickTrans (global, from any app) |
| **Ctrl+M** | QuickTrans (in-app, from a grid cell) |

## Related pages

* [Companion Tabs Overview](../sidekick/overview.md)
* [SuperLookup Overview](../superlookup/overview.md)
* [Trados-aware Chat](../sidekick/trados-aware-chat.md)
* [Keyboard Shortcuts](../settings/shortcuts.md)

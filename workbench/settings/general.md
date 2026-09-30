---
title: "General"
---

## Where to find settings

Open **Settings** from the main toolbar or the **View** menu. Settings are organised into tabs across the top of the settings panel.

## Changes are saved automatically

Since v1.10.372 there are no Save buttons on the Settings pages. Each change is saved a moment after you make it, so you can leave a page at any time without losing what you changed. Where a page used to have a Save button, it now shows the note **✓ Changes on this page are saved automatically** instead, and a short **✓ Settings saved** appears in the status bar after each save.

- **Typing** – saving waits for a short pause while you type, and anything still pending is saved as soon as you leave the field. A system prompt you are editing is therefore saved before you switch to another prompt.
- **Only real changes are saved** – buttons that just *do* something, such as opening a folder or exporting the debug log, don't write the page's settings.
- **Loading doesn't save** – opening a project never changes your settings; only your own clicks and edits do.

## AI Settings

**Settings → 🤖 AI Settings** is where you choose the AI that translates:

- **🤖 LLM Provider Selection** – OpenAI, Anthropic Claude, Google Gemini, Mistral AI, DeepSeek, 🌐 OpenRouter (200+ models), 🖥️ Local LLM (Ollama) or 🔌 Custom (OpenAI-Compatible API)
- **📦 Model Selection** – the model for the chosen provider, used for AI translation and the Chat assistant; for a custom provider, the endpoint profile
- **🔑 LLM API Keys** – a key for each provider, saved automatically and stored locally in your user data folder
- **✅ Enable/Disable LLM Providers** – which providers are offered elsewhere in Workbench
- **🌐 HTTP Proxy Settings** – for networks that reach the internet through a proxy
- **🖥️ Local LLM (Ollama) Advanced Settings** – request timeout and keeping the model loaded; see [Using Local LLMs (Ollama)](/workbench/ai-translation/ollama/)
- **⚙️ AI Translation Preferences** – how many surrounding segments go along with a single-segment translation (Ctrl+T), the batch size and context window for batch translation, and **AI Cost Monitoring** (see [Token Usage & Costs](/workbench/ai-translation/usage-costs/))

See [Setting Up API Keys](/workbench/get-started/api-keys/) for step-by-step instructions.

## Language pair

**Settings → 🌐 Language Pair** sets the source and target language used when no project is open, for example by QuickTrans and SuperLookup. Opening or creating a project switches to that project's languages.

## Voice settings

The [🎤 Voice top tab](/workbench/voice/overview/) contains all voice command and dictation settings (engine, model, sensitivity, push-to-talk mode). They are not duplicated here – open the Voice tab directly to configure them.

## Related pages

- [Setting Up API Keys](/workbench/get-started/api-keys/)
- [AI Translation Overview](/workbench/ai-translation/overview/)
- [Theme (Light/Dark Mode)](/workbench/settings/theme/)
- [Keyboard Shortcuts](/workbench/settings/shortcuts/)

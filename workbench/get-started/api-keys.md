---
title: "Api Keys"
---

To use AI translation you need an API key from at least one provider. Enter your key in **Settings → AI Settings**.

## Supported providers

| Provider | Where to get a key |
|----------|--------------------|
| **OpenAI** | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| **Anthropic (Claude)** | [console.anthropic.com](https://console.anthropic.com) |
| **Google (Gemini)** | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |
| **Mistral AI** | [console.mistral.ai](https://console.mistral.ai) |
| **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com) |
| **OpenRouter** (200+ models, one key) | [openrouter.ai/keys](https://openrouter.ai/keys) |
| **Ollama** | No key needed – runs locally |

## Entering a key

1. Open **Settings → 🤖 AI Settings**
2. Choose your provider under **🤖 LLM Provider Selection**, and its model under **📦 Model Selection**
3. Paste your API key into the provider's field under **🔑 LLM API Keys** (click **Show** to check what you pasted)

There is no Save button: like every [Settings page](/workbench/settings/general/), AI Settings saves itself a moment after you make a change, and "✓ Settings saved" appears in the status bar. To check that the key works, translate a segment with **Ctrl+T** – the sample project under **Help → 🎓 Open Sample Project** is handy for this.

Keys are only ever sent to the provider's own API endpoint.

## One key for all Supervertaler products

Workbench uses the same API keys as Supervertaler for Trados, Supervertaler for memoQ and Sidekick: one key per provider, for all of them. A key you enter in any of them works in all of them, and a key changed in one is changed in all. That goes for the machine-translation keys in **Settings → 🌐 MT Settings** too (DeepL, Google Translate, Microsoft Translator, ModernMT).

The first time you start a version of Workbench that shares keys, it adds its own keys where the other products had none for that provider – it never overwrites one. If your Workbench key for a provider was different from the one the other products use, theirs is used from then on, and the status bar says once which providers that was. To use your Workbench key after all, paste it into the provider's box again.

## Where your keys are kept

On Windows each key is kept in your Windows profile, locked by Windows so that it opens only for your Windows account:

```
C:\Users\<you>\AppData\Roaming\Supervertaler\api-keys.locked.json
```

On a Mac, keys go into your Keychain. If you move between the Mac app and the version installed with pip, macOS asks once whether the other may use Supervertaler's Keychain item: click **Always Allow**. If a Mac has no Keychain Workbench can use – or a Linux computer has no secret store – Workbench says so once and keeps your keys in its settings file as before.

For now each key is also still written to `api-keys.json` in your data folder's `settings` folder, and to Workbench's own settings, so that older versions keep working. A later version will stop keeping keys in the data folder. There is nothing to do.

## "Can't be read on this computer"

A key that Windows will not unlock for you – one saved under another Windows sign-in, or one stored before an administrator reset your Windows password – is never shown as if there were none. Under its box in **Settings → 🤖 AI Settings** (or **🌐 MT Settings**) Workbench says:

> Your Anthropic key can't be read on this computer – it was saved under another Windows sign-in, or your Windows password was reset. Paste the key in again; nothing else is affected.

An action that needs the key stops with "Can't use your Anthropic key – it can't be read on this computer…" instead of calling the provider. Paste the key in again. Until you do, the unreadable copy is kept – leaving the box empty does not remove it – because some causes pass by themselves, such as a company network that can't be reached yet after a password reset.

If the file holding the locked keys is ever damaged, Workbench keeps a copy of it beside the original (`api-keys.locked.damaged-…json`) and says so in the status bar, asking you to paste your keys in again. While `api-keys.json` still holds your keys, they are locked again from there when Workbench starts, so in practice only a key that an action reports as missing needs pasting.

## Switching providers

You can configure keys for multiple providers in the same settings panel. Switch between them without re-entering credentials – the key for each provider is remembered independently.

## Using Ollama (no key required)

Ollama runs models entirely on your machine. No API key or internet connection is needed.

See [Ollama Setup](/workbench/ai-translation/ollama/) for download and configuration instructions.

## Using OpenRouter (one key for everything)

If you prefer not to manage multiple accounts, OpenRouter lets you access 200+ models from all major providers with a single API key. Create an account at [openrouter.ai](https://openrouter.ai) and paste your key into the **OpenRouter** provider slot.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Invalid API key" | Double-check the key; ensure no leading or trailing spaces |
| "Can't be read on this computer" | Paste the key in again – see [above](#cant-be-read-on-this-computer) |
| "Rate limit exceeded" | Wait a moment, or upgrade your API plan |
| "Model not found" | Check the model name in settings; it may have been updated |
| No response | Check your internet connection and that the provider's service is up |

---

## Next steps

- [Create your first project](/workbench/get-started/first-project/)
- [Supported LLM Providers](/workbench/ai-translation/providers/)
- [AI Translation Overview](/workbench/ai-translation/overview/)

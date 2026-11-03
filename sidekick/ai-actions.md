---
title: "AI actions"
---

An AI action runs a prompt of your own over whatever text you have selected, in any application, and shows the answer. The prompts are ordinary menu entries, so they sit beside your snippets and searches, are edited in the same [Library Editor](/sidekick/library/#the-library-editor), and can have keyboard shortcuts attached.

The starter set covers the everyday ones: ask a question in any language, explain, proofread, rephrase with five options, make it sound better, summarise and expand. For translation there is [QuickTrans](/sidekick/quicktrans/), at the top of the same section. Every one of them is a few lines you can change.

### Writing one

In the Library Editor, add an entry of kind **AI** and give it a prompt:

```json
{
  "kind": "ai",
  "label": "Translate (Dutch to English)",
  "prompt": "Give ten possible translations, technical to general.",
  "effort": "high"
}
```

The selection is appended to the prompt. Optional per-entry overrides: `system` (a system prompt), `provider`, `model`, `effort` (`low`, `medium`, `high`, `xhigh`, `max` – Anthropic only) and `maxtokens`. Anything not set comes from the `[AI]` section of `settings.ini`, where the provider and model are the ones chosen in the window below.

### Providers

Open **Settings → AI providers & keys…**. The line at the top, **AI menu actions use:**, picks which provider and model answer your AI actions: Claude (Anthropic), OpenAI, Gemini, Mistral, DeepSeek or OpenRouter, and a model. The model list is the one that provider's row further down has – the few models worth recommending, and everything your key can use once **Models** or **Show all models** has asked. Leave the model blank for the provider's default; the empty box says which that is. A model you typed by hand stays as you typed it.

Click **Save** and the next AI action uses your choice – there is no need to reload Sidekick. The provider needs a key: if it has none, or its key can't be read on this computer, the window says so and keeps the provider you had, so your AI actions don't stop working. Paste the key into that provider's row and click **Save** again. Keys live in the shared key file – see [Installation](/sidekick/installation/#4-add-api-keys).

An AI action whose entry names its own `provider` or `model` keeps it, whatever the window says.

Requests do not block. The rest of Sidekick keeps working while an answer is on its way.

### Sharing prompts with the Trados plugin

Supervertaler for Trados keeps its prompts in a [library](/trados/settings/prompts/) with [QuickLauncher](/trados/quicklauncher/) shortcuts. Sidekick's AI actions are the same idea outside the CAT tool, and today they are a separate list. Letting the two share one prompt library, so a prompt written for the Trados editor is also on the Sidekick menu, is planned.

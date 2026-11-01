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

The selection is appended to the prompt. Optional per-entry overrides: `system` (a system prompt), `provider`, `model`, `effort` (`low`, `medium`, `high`, `xhigh`, `max` – Anthropic only) and `maxtokens`. Anything not set comes from the `[AI]` section of `settings.ini`.

### Providers

The default provider and model are set under `[AI]` in `settings.ini`; keys live in the shared key file and are entered through **Settings → AI providers & keys…** – see [Installation](/sidekick/installation/#4-add-api-keys). Anthropic and OpenAI are supported as AI-action providers; the request and response shapes for each live in one place in the code, so a further provider is one entry rather than a rewrite.

Requests do not block. The rest of Sidekick keeps working while an answer is on its way.

### Sharing prompts with the Trados plugin

Supervertaler for Trados keeps its prompts in a [library](/trados/settings/prompts/) with [QuickLauncher](/trados/quicklauncher/) shortcuts. Sidekick's AI actions are the same idea outside the CAT tool, and today they are a separate list. Letting the two share one prompt library, so a prompt written for the Trados editor is also on the Sidekick menu, is planned.

### The answer

The answer opens in a window of its own, formatted: headings, **bold** and *italic* text, bullet and numbered lists, tables, code, and sub- and superscript (H₂O, m²) appear as the AI meant them, rather than as Markdown's `#`, `**` and `-` marks. Error messages are shown exactly as they arrive.

- **Copy** puts the whole answer on the clipboard in two forms: as plain text without the Markdown marks – what Trados, memoQ, a browser or Notepad paste – and formatted, which is what Word pastes.
- **Insert & close** types the answer, as plain text, where your selection was.
- **Retry** asks again; **Close** or Esc closes the window.
- To copy part of the answer, select it with the mouse and press Ctrl+C. Right-click for **Copy**, **Select all** and **Copy as Markdown** – the answer exactly as the AI wrote it, marks and all, for when the marks belong in the text (when you are translating a Markdown file, say).

In the plain text, bullets become • (◦ one level in), numbered lists keep their numbers, and a table's cells are separated by " | ".

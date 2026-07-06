---
title: "Sending Terms to the AI"
---

Supervertaler can send your termbase entries to the AI as reference during translation, so the model uses your approved terminology instead of guessing. This is on a per-termbase basis and takes one click to enable.

## How to enable it

Each termbase in the **Termbase Manager** has an **AI** checkbox (the orange/purple tick), separate from the Read/Write activation checkboxes.

1. Open the **Termbases** tab.
2. Find the termbase whose terms you want the AI to use.
3. Tick its **AI** checkbox.

That's the only setup step. From then on, matching terms are automatically included in every translation prompt for the current project.

:::note
The **AI** checkbox is independent per termbase. You might, for example, feed a small client-approved glossary to the AI while keeping a large general reference termbase for lookups only.
:::

## What happens during translation

When you translate a segment, Supervertaler:

1. Scans the source text of that segment.
2. Finds any terms from your AI-enabled termbases that actually appear in it.
3. Adds them to the prompt sent to the AI under a **TERMBASE** heading, instructing the model to use those approved terms.

The section added to the prompt looks like this:

```
# TERMBASE

Use these approved terms in your translation:

- machine learning → machinaal leren
- click → klikken
- widget → ⚠️ DO NOT USE: widget
```

### Only relevant terms are sent

Supervertaler sends **only the terms that appear in the current segment**, not your entire termbase. Matching is whole-word for spaced languages and substring-based for CJK/Thai. This keeps each prompt focused, avoids diluting the AI with irrelevant terminology, and saves tokens.

### Forbidden terms

If you mark a term as **forbidden** in the termbase, the AI is explicitly told **DO NOT USE** that translation. This is useful for steering the model away from a wrong-but-tempting rendering, or away from an old term a client has since replaced.

## Tips

- **Keep AI-enabled termbases focused.** Very large termbases trigger a warning, because sending a lot of terminology can dilute translation quality. Thanks to per-segment filtering this rarely bites in practice, but a tight, curated glossary gives the best results.
- **Works everywhere.** Term injection applies to single-segment translation, batch translation, and keyboard-shortcut translation alike.
- **Combine with TM.** Fuzzy TM matches are injected alongside termbase terms, so the AI gets both your approved terminology and your existing translations as reference.

## See Also

- [Termbase Basics](basics.md)
- [Importing Terms](importing.md)
- [AI Translation Overview](../ai-translation/overview.md)
- [Prompts](../ai-translation/prompts.md)

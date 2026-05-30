---
title: "AutoCorrect while typing"
---

Supervertaler can automatically convert straight quotes, three-dot ellipses, and double-hyphen dashes to the correct typographic forms **as you type in the target field**. Quote shapes follow the **target language** — German targets get `„…"`, French targets get `« … »`, Russian targets get `«…»`, English targets get `"…"`, and so on.

This feature was requested in [discussion #211](https://github.com/orgs/Supervertaler/discussions/211) and ships from **v1.10.230**.

## Where to find it

**Settings → ✍️ AutoCorrect** (its own tab in the Settings sidebar, just below General).

The master switch enables or disables all rules at once. Each rule below it can also be toggled individually.

This tab **saves automatically** — there is no Save button. Every toggle is written to your settings the moment you click it and takes effect on the **very next keystroke** — no app restart, no grid reload.

## Rules

| Rule | Behaviour | Default |
|---|---|---|
| Smart double quotes | `"foo"` → language-correct typographic pair | on |
| Smart single quotes / apostrophes | `'foo'` → typographic single pair · `don't` → `don't` | on |
| Ellipsis | `...` → `…` | on |
| En-dash | `word-- word` → `word– word` | on |
| Em-dash | `word--- word` → `word— word` | **off** (the project uses en-dashes) |
| French typographic spacing | Insert a narrow non-breaking space before `:` `;` `!` `?` | on for `fr-*` targets |

## Quote shapes by target language

The smart-quote rule reads your project's target language and picks the appropriate shape:

| Languages | Open | Close |
|---|---|---|
| English, Dutch, Portuguese, Turkish, Romanian, Danish | `"` | `"` |
| German, Czech, Slovak, Slovenian, Croatian, Hungarian, Polish *(close uses `"`)* | `„` | `"` / `"` |
| French | `« ` (with NNBSP) | ` »` (with NNBSP) |
| Spanish, Italian, Russian, Ukrainian, Norwegian | `«` | `»` |
| Swedish, Finnish | `"` | `"` |

The engine decides between "open" and "close" shape from what immediately precedes the typed quote — whitespace or an opening bracket → open shape; a letter, digit or closing bracket → close shape. Tag markers (`{1}`, `<seg>`, `[2}`) are treated as transparent, so a quote opened straight after an inline tag still gets the opening shape.

## Backspace cancels the last conversion

If AutoCorrect converts something you actually wanted to leave alone, press **Backspace immediately**. One Backspace restores your literal typing (the straight quote, the three dots, the double hyphen, etc.) — exactly as it works in Word and memoQ. The next keystroke clears that one-shot undo memory, so the safety net is only available for the conversion you just made.

## What AutoCorrect does *not* touch

- **Inside tag markers** (`{1}`, `[2}`, `<seg>`). Auto-correcting inside a tag would corrupt the boundaries and break the round-trip back to your source format, so the engine skips these.
- **Paste**. Pasting a block of text never triggers any rule — only single typed characters do. If you want the engine to clean up pasted text, do it explicitly with Find & Replace.
- **Programmatic content** (loaded translations, MT/TM insertions, Copy Source → Target). Same reason — these aren't user keystrokes.
- **Dictation**. Voice-typed content arrives via a different input path and is not auto-corrected.
- **The source column**. AutoCorrect is target-only.

## Turning a single rule off temporarily

Use the per-rule toggles on the **Settings → ✍️ AutoCorrect** tab. Because the tab saves automatically, both the master switch and the per-rule checkboxes are honoured on the next keystroke without clicking anything else. There's no per-segment override yet — if you want one in a future version, please open an issue.

## See also

- [Settings → General](general.md)
- Tracking issue: [#213 — Typographic auto-convert / AutoCorrect-while-typing system](https://github.com/Supervertaler/Supervertaler-Workbench/issues/213)
- Original request: [Discussion #211](https://github.com/orgs/Supervertaler/discussions/211)

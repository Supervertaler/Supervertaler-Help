---
title: "Tag Validation"
---

When working with formatted documents or CAT tool files, **tags must be preserved**.

## Why tags matter

Tags represent formatting or placeholders. If tags are missing or unbalanced, reimporting into your CAT tool can fail or formatting may be lost.

## Tag display modes

Supervertaler supports two ways of viewing formatting:

- **WYSIWYG mode**: shows *bold/italic/underline* as formatting
- **Tag view**: shows the raw markup (for example `<b>...</b>`)

Use **Tag view** when you are preparing to export/reimport and you want to verify the raw tags.

## Supported formatting tags

These tags are commonly used in Supervertaler projects:

| Tag | Meaning |
|-----|---------|
| `<b>...</b>` | Bold |
| `<i>...</i>` | Italic |
| `<u>...</u>` | Underline |
| `<bi>...</bi>` | Bold + Italic |
| `<sub>...</sub>` | Subscript |
| `<sup>...</sup>` | Superscript |

## CAT tool placeholder tags

CAT tools use placeholders/tags that must be preserved exactly:

| CAT tool | Examples |
|----------|----------|
| memoQ | `{1}`, `[2}...{2]`, `{MQ}`, `{tspan}` |
| Trados Studio | `<1>`, `</1>`, `<2/>` |
| Phrase (Memsource) | `{1}`, `{2}` |

## Your own inline codes

Software strings and game files are full of placeholders that must reach the translation unchanged, such as `{playerName}`, `%s` or `\n`, but that no CAT tool has tagged. Describe them with patterns under **Settings → 🏷️ Inline Codes** and Supervertaler treats them like tags: they're coloured like tags in the grid, **Ctrl+,** inserts the next one the target is still missing, and the tag check below reports them. See [Inline Codes](/workbench/settings/inline-codes/).

## Checking tags across the project

**QA → 🔎 Run QA Checks…** has a **Tags & codes match the source** option. It lists every tag or code that a translated segment has lost, and every one it has although its source doesn't. Double-click a finding to go to the segment. See [QA Checks → Tags & codes](/workbench/qa/qa-checks/#tags--codes), which also says which kinds of tag it recognises.

## Tips

- Keep tags balanced (for example `<b>text</b>`, not `<b>text`).
- If you’re unsure, switch to Tag View and verify the raw tags.
- Don’t change tag numbers or names (for example `{1}` → `{2}`), even if the translation “looks fine”.
- If you insert a TM match, double-check that tags/placeholders still match the source.
- Before you deliver, run **QA → 🔎 Run QA Checks…** with **Tags & codes match the source** ticked to catch any tag you missed.

:::caution
For CAT tool workflows, don’t delete or edit placeholder tags unless you know exactly what they represent.
:::

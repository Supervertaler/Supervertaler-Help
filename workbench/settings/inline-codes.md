---
title: "Inline Codes"
---

Software strings and game files are full of placeholders and bits of markup that must reach the translation unchanged: `{playerName}`, `%s`, `%1$d`, `\n`, `<color=#ff0000>` and the like. A CAT tool would normally have turned them into tags, but in these files nobody has, so to Supervertaler they are just text.

**Settings → 🏷️ Inline Codes** lets you describe them with regular expressions (from v1.10.372). Anything that matches is then treated like an inline tag.

## What Supervertaler does with codes

- **The grid** colours codes like tags, in both the source and the target.
- **Insert next tag (Ctrl+,)** inserts the next code from the source that the target is still missing, just as it does for ordinary tags.
- **QA → 🔎 Run QA Checks…** has a **Tags & codes match the source** option. It lists codes, and ordinary inline tags, that a translation has lost, or has although its source doesn't. See [QA Checks](/workbench/qa/qa-checks/#tags--codes).
- **AI translation**, of single segments and in batches, lists the segment's codes in the prompt and tells the AI to keep them exactly as written. They may move to fit the word order.
- **TM matches that differ only in their codes are adapted.** Say your TM has `{PK}{MN} can't be the same.` → `{PK}{MN} muszą być różne.`, and your segment reads `{PKMN} can't be the same.`. The match you are offered is then `{PKMN} muszą być różne.`. The Match Panel's **TM Source** comparison shows `{PK}{MN}` → `{PKMN}` as one code replaced.

The codes themselves stay ordinary text in the segment: nothing in your file is converted, so they are exported exactly as they appear in the target.

## The patterns table

Each row of the **Code patterns** table is one kind of code:

- **On** – untick to switch a pattern off without deleting it.
- **Pattern (regular expression)** – what the code looks like.
- **Comment** – a note for yourself.

Click **➕ Add pattern** to add an empty row and type your pattern, or **Remove** to delete the selected one. A pattern that can't be used is marked in red; hover over it to see why. That includes a pattern that would also match empty text. Where two patterns could match at the same place, the one higher in the list wins.

## Common patterns

You don't have to write regular expressions for the usual cases. **➕ Common patterns ▾** adds a ready-made one in one click:

| Menu entry | Finds, for example |
|---|---|
| `{placeholder}` | `Hello {playerName}!` |
| `%s, %d, %1$s (printf)` | `%d items for %s` |
| `%NAME%` | `Welcome, %USER%` |
| `\n \t (escaped line breaks)` | `Line one\nLine two` |
| `<color=…> game tags` | `<color=#ff0000>Red</color>` |
| `$VARIABLE$` | `Costs $PRICE$` |
| `${var} and {{var}}` | `Hi {{name}}, ${count} new` |
| `[[double brackets]]` | `Press [[KEY_JUMP]]` |

The menu entry becomes the pattern's comment. A pattern that is already in the table isn't added twice.

## The Test box

The **Test** box shows what your patterns find. Type or paste a few lines from your file, and every code found is marked below it, with a count such as "4 codes found". It updates as you type and as you change the patterns.

:::tip
Try a pattern on real text from the job before you start translating. A pattern that is too broad, such as one that also catches ordinary words in brackets, turns normal text into codes.
:::

## Changes apply immediately

There is no Save button on this page. Each change is saved at once, and the grid is re-coloured with the new patterns straight away. The patterns are a program setting, so they apply to every project you open.

## Related

- [Tag Validation](/workbench/qa/tag-validation/)
- [QA Checks](/workbench/qa/qa-checks/)
- [Editor Keyboard Shortcuts](/workbench/editor/keyboard-shortcuts/)
- [Fuzzy Matching](/workbench/translation-memory/fuzzy-matching/)

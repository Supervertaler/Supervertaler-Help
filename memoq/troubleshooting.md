---
title: "Troubleshooting"
---

### Supervertaler does not appear at all

Check `Supervertaler.MemoQ.dll` is in memoQ's `Addins` folder, and that you answered **Yes** to the unsigned-plugin prompt on startup — its default button is *No*.

If memoQ was recently upgraded to a new major version, the add-ins need copying into the new program folder. See [Installation](installation.md).

### It translates, but never learns

**Self-learning MT** is not set. Resource console → MT settings → your resource → **Settings** tab → **Self-learning MT** → *Supervertaler*, then restart memoQ.

Advertising the capability only makes the engine eligible; memoQ does not send confirmations until it is actually selected there.

### Terminology is not showing

Three things must all be true, under **Options → Terminology plugins**:

1. **Perform terminology plugin lookups while working in the translation grid** is ticked
2. **Supervertaler terms** does not read *Not configured* — i.e. a glossary file is set
3. **Enable plugin** is ticked for it

### The glossary loads no terms

Almost always spaces where tabs should be. The glossary options dialog reports how many terms it parsed; if that reads zero with a file selected, open the file in an editor with whitespace visible and check the separators.

### The log

Supervertaler writes a diagnostic log to:

```
%TEMP%\Supervertaler-memoQ.log
```

It records what memoQ asked for and what was sent — segment sizes, how many glossary terms matched, how many remembered segments were used, and any errors. It does not contain the text of your translations.

A typical healthy line:

```
translate: 199 src chars, 0 tag(s) -> 239 target chars, 0 tag(s) | recall: used 2 of 7 held | terms: 7
```

meaning: a 199-character segment; two remembered segments and seven glossary terms sent with it; a 239-character translation returned.

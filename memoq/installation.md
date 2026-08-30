---
title: "Installation"
---

### Requirements

- **memoQ 12** (translator pro or project manager)
- An API key for Anthropic, OpenAI or Google
- Administrator rights on the machine, once, to place the files

### Installing

Supervertaler for memoQ ships as two files:

```
Supervertaler.MemoQ.dll         the AI translation engine
Supervertaler.MemoQ.Terms.dll   the terminology provider
```

Both belong in memoQ's `Addins` folder, inside the memoQ program directory — typically:

```
C:\Program Files\memoQ\memoQ-12\Addins\
```

Copy both files there and restart memoQ.

:::note[Why two files]
memoQ loads exactly one add-in per DLL, so the translation engine and the terminology provider cannot share one. They are halves of the same product and are designed to be installed together — but the terminology half is optional if you only want AI translation.
:::

### The unsigned plugin warning

The first time memoQ starts after installation it will say it has detected one or more unsigned plugins, and ask whether to load them.

**Answer Yes.** The default button is *No*, so a stray Enter keypress will decline it.

Supervertaler is not yet signed by memoQ. Signing is a review process memoQ runs for plugins with proven demand; until then, this prompt appears whenever the files change.

### Where the program directory is version-stamped

memoQ's install folder carries its version number (`memoQ-12`, `memoQ-13`, …). A memoQ major upgrade creates a **new folder**, and the add-ins are not carried across — they will need to be copied again.

If Supervertaler disappears after a memoQ update, this is almost always why.

### Uninstalling

Close memoQ, delete the two DLLs from the `Addins` folder, and restart.

To remove what Supervertaler has stored on your computer as well, use **Forget stored context** in the plugin's options dialog before uninstalling — see [Self-learning translation](self-learning.md#what-is-stored-and-where).

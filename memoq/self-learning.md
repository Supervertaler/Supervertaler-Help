---
title: "Self-learning Translation"
---

Supervertaler remembers the segments you confirm, and shows the most relevant ones to the model when it translates later segments in the same document.

This is what makes the second half of a document read like the first. Settle on a rendering once, confirm it, and everything that follows is translated with your choice in front of the model rather than against a blank slate.

### Turning it on

**Resource console → MT settings → your resource → Settings tab → Self-learning MT → Supervertaler.**

Then restart memoQ. Until this is set, memoQ never passes confirmed segments to the plugin, and Supervertaler translates without memory.

### What gets remembered

Only segments **you confirm**. Not the AI's raw output.

That distinction is deliberate. Feeding a machine its own guesses compounds its mistakes; the value of these examples is precisely that a human approved them.

For each confirmation Supervertaler stores the source text and the target text, and nothing else — no tags, no formatting, no metadata. Re-confirming a segment replaces the earlier version, so your latest decision is the one that counts.

### How much is sent to the AI

Not all of it. For each new segment, Supervertaler picks the **five** stored pairs sharing the most vocabulary with it. A pair with no words in common is never sent.

So a document with hundreds of confirmed segments still contributes only a few short examples per request — the ones most likely to matter.

### What is stored, and where

Memory is kept per document *and* language pair, and written to:

```
%LocalAppData%\Supervertaler.memoQ\document-memory\
```

It survives closing memoQ, so picking a job back up the next morning keeps yesterday's decisions. Limits: 500 pairs per document, 200 documents, and anything untouched for 60 days is discarded.

:::caution[This is client text on your disk]
These files contain source and target segments from real work. They are stored under your own user profile, are not synced anywhere, and never leave your computer.

The plugin's options dialog shows how many documents and how much space are held, with a **Forget stored context** button that deletes all of it. Your translations in memoQ are not affected.
:::

### What it is not

This is not adaptive machine translation in the sense that ModernMT or Lara mean it. No model is trained or fine-tuned, and nothing is sent to Supervertaler — the examples are simply included in the request to the AI provider you chose, alongside the segment.

The practical differences: it works within a document rather than across your whole history, it is lost if you clear it, and it is entirely inspectable. Nothing happens that you cannot see in the prompt.

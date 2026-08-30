---
title: "Supervertaler for memoQ"
---

Supervertaler for memoQ brings AI translation and your own terminology into **memoQ 12**, as two add-ins that work together.

Unlike the Trados plugin, which docks its own panels into the editor, memoQ gives an add-in no window of its own. Supervertaler therefore works through memoQ's existing surfaces — the machine-translation engine and the terminology pane — rather than adding new ones. In practice that turns out to suit it: the results appear exactly where you already look for them.

### What it does

**AI translation.** An LLM machine-translation engine using Anthropic, OpenAI or Google, with your own API key and your own instructions. It works segment by segment as you translate, and in bulk through **Pre-translate**. Inline tags survive the round trip.

**It learns as you work.** Every segment you confirm is remembered, and the most relevant ones are shown to the model when it translates later segments in the same document. Settle on a term once and the rest of the document follows it — no configuration, no retraining, just your own approved choices fed forward. See [Self-learning translation](/memoq/self-learning/).

**Your terminology, twice over.** A glossary you point Supervertaler at appears as a memoQ terminology provider — matched terms highlighted in the source, entries listed in Translation results — *and* is sent to the model as required or forbidden terminology. Forbidden terms are enforced, not merely displayed. See [Terminology](/memoq/terminology/).

### What it does not do

memoQ does not let a plugin read its own term bases, so terms defined in a memoQ term base are not visible to the AI. Supervertaler reads its own glossary file instead, which it can also display alongside memoQ's own term base hits.

There is no chat panel, no prompt library window and no document-wide search inside memoQ. Those live in [Supervertaler for Trados](/trados/), and in time in a companion application.

### Where to start

- [Installation](/memoq/installation/) — putting the add-ins in place
- [Getting started](/memoq/getting-started/) — a first translation
- [Terminology](/memoq/terminology/) — using a glossary

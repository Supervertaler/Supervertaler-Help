---
title: "Supervertaler for memoQ"
---

Supervertaler for memoQ brings AI translation and your own terminology into **memoQ 12**, as two add-ins that work together.

Unlike the Trados plugin, which docks its own panels into the editor, memoQ gives an add-in no window of its own. Supervertaler therefore works through memoQ's existing surfaces — the machine-translation engine and the terminology pane — rather than adding new ones. In practice that turns out to suit it: the results appear exactly where you already look for them.

### What it does

**AI translation.** An LLM machine-translation engine using Anthropic, OpenAI or Google, with your own API key and your own instructions. It works segment by segment as you translate, and in bulk through **Pre-translate**. Inline tags survive the round trip.

**It learns as you work.** Every segment you confirm is remembered, and the most relevant ones are shown to the model when it translates later segments in the same document. Settle on a term once and the rest of the document follows it — no configuration, no retraining, just your own approved choices fed forward. See [Self-learning translation](/memoq/self-learning/).

**Your terminology, twice over.** A glossary you point Supervertaler at appears as a memoQ terminology provider — matched terms highlighted in the source, entries listed in Translation results — *and* is sent to the model as required or forbidden terminology. Forbidden terms are enforced, not merely displayed. See [Terminology](/memoq/terminology/).

**Translate with Claude Desktop.** Through the [Supervertaler MCP Server](/memoq/mcp-server/), Claude reads the document you are translating, your confirmed segments and your glossary, and stages translations that flow into the grid when you press Pre-translate. Tokens are billed to your Claude subscription rather than an API key, and every write into your document goes through your own hands. See [MCP Server](/memoq/mcp-server/).

**A prompt library, shared with Trados.** Translation instructions come from the same library the Trados plugin uses, chosen from a dropdown and edited in a small companion [editor](/memoq/prompt-editor/). Claude can draft prompts into it too.

### What it does not do

memoQ does not let a plugin read its own term bases or translation memories, so terms defined in a memoQ term base are not visible to the AI. Supervertaler reads its own glossary file instead, which it can also display alongside memoQ's own term base hits.

There is no chat panel, no document-wide search and no cursor control inside memoQ: a plugin can answer when asked for a translation, and that is all. The chat lives in Claude Desktop; the prompt library lives in its own editor; and Claude's translations reach the grid only when you Pre-translate. [MCP Server → What it can and cannot do](/memoq/mcp-server/#what-it-can-and-cannot-do) has the full comparison with the Trados plugin.

### Where to start

- [Installation](/memoq/installation/) — putting the add-ins in place
- [Getting started](/memoq/getting-started/) — a first translation
- [Terminology](/memoq/terminology/) — using a glossary
- [MCP Server](/memoq/mcp-server/) — translating with Claude Desktop
- [Prompt Library & Editor](/memoq/prompt-editor/) — choosing and writing instructions

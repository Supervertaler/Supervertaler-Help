---
title: "Getting Started"
---

This walks through a first translation, assuming the add-ins are [installed](/memoq/installation/).

### 1. Set up the translation engine

Open the **Resource console** → **MT settings**. Create or edit an MT settings resource, and on the **Services** tab tick **Supervertaler**.

Click **Configure plugin** and fill in:

| | |
|---|---|
| **Provider** | Anthropic, OpenAI or Google |
| **Model** | e.g. `claude-opus-5` |
| **API key** | your own key for that provider. If you run Supervertaler for Trados as well, its key is picked up automatically and you can leave this empty |
| **Endpoint** | leave blank unless you are using a local model or a gateway |
| **Segments per request** | how many segments go into one request during Pre-translate (memoQ hands the plugin about 10 at a time, so values above 10 make no difference) |
| **Prompt** | a prompt from the shared library, or *(instructions below)* to type your own – see [Prompt Library & Editor](/memoq/prompt-editor/) |
| **Pre-translate via Claude Desktop (MCP)** | leave **unticked** unless you translate through Claude Desktop – see [MCP Server](/memoq/mcp-server/). Also in the prompt editor under Settings |

Press **Test connection**. It translates a short sentence for real, so it exercises the key, the model name and the endpoint together – a green result means everything works.

### 2. Turn on learning

Still in the MT settings resource, go to the **Settings** tab and set **Self-learning MT** to **Supervertaler**.

This is what makes memoQ hand Supervertaler each segment as you confirm it. Without it the engine still translates, but it will not learn from your work. See [Self-learning translation](/memoq/self-learning/).

:::caution
Changing this takes effect when memoQ next builds a translation engine. Restart memoQ after setting it.
:::

### 3. Translate

Open a document. With **Translation results** set to *Always*, landing on a segment fetches a translation automatically; it appears in the Translation results pane, labelled with the provider and model it came from.

To translate in bulk, use **Preparation → Pre-translate** with *Use machine translation* enabled.

### 4. Confirm as you go

Confirm segments as you normally would. Each confirmation is remembered, and later segments that resemble it are translated with your wording in front of the model.

The effect is most visible on a document with recurring phrasing: settle a term in segment 3 and segment 40 will use it.

### Next

- [Terminology](/memoq/terminology/) – add a glossary, including forbidden terms
- [Self-learning translation](/memoq/self-learning/) – what is remembered, and for how long

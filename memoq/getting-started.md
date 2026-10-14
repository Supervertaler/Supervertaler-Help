---
title: "Getting Started"
---

This walks through a first translation, assuming Supervertaler is [installed and switched on in memoQ](/memoq/installation/#switching-it-on-in-memoq).

### 1. Choose a provider and model

Open **Supervertaler for memoQ** from the Start menu and choose **Settings → Translation settings…**. memoQ's own dialog holds the same settings – **Configure plugin** on Supervertaler in an MT settings resource – and either place can change them; both read and write the same file.

Fill in:

| | |
|---|---|
| **Provider** | Anthropic, OpenAI or Google, or a model on your own computer through Ollama or an OpenAI-compatible server – see [Local and cloud models](/memoq/local-models/) |
| **Model** | a short list of the models worth recommending for that provider, with a line on each saying what it is for. **Fetch list** asks the provider for its full catalogue and **Show all models** adds it underneath – that is where to look for a model released after your copy of Supervertaler was built. The box also takes anything typed, for a gateway or a local model |
| **API key** | your own key for that provider. All Supervertaler products share one key file at `C:\Users\<you>\Supervertaler\settings\api-keys.json`, so a key you have already set in Supervertaler for Trados or Sidekick is picked up here and you can leave this empty – see [The Supervertaler editor](/memoq/prompt-editor/#api-keys-live-in-one-file) |
| **Endpoint** | only for Ollama and OpenAI-compatible servers; for Ollama on this computer, leave it blank |
| **Parallel requests** | how many requests go to the model at once. Saved separately for cloud providers and for local servers: **4** suits a cloud provider, **1** a model on your own computer – see [Local and cloud models](/memoq/local-models/#parallel-requests) |
| **Segments per batch** | how many segments go into one request during Pre-translate (memoQ hands the plugin about 10 at a time, so values above 10 make no difference). Called *Segments per request* before version 0.1.20 |
| **Prompt** | a prompt from the shared library, or *(instructions below)* to type your own – see [The Supervertaler editor](/memoq/prompt-editor/). The editor chooses it from the panel at the top left |
| **Pre-translate via Claude Desktop (MCP)** | leave **unticked** unless you translate through an AI assistant such as Claude Desktop, ChatGPT desktop or Claude Code – see [AI assistants](/memoq/mcp-server/). Staged translations are used either way; the setting only decides whether Pre-translate sends the other rows to your API key. Also the switch at the top right of the editor |

In memoQ's dialog, **Test connection** translates a short sentence for real, so it exercises the key, the model name and the endpoint together – a green result means everything works.

### 2. Turn on learning

In memoQ, open the MT settings resource Supervertaler is ticked in – **Options → Default resources → MT settings**, or **Project home → Settings → MT settings** for a project you already have – and on its **Settings** tab set **Self-learning MT** to **Supervertaler**.

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

- [Terminology](/memoq/terminology/) – termbases, including forbidden terms
- [Self-learning translation](/memoq/self-learning/) – what is remembered, and for how long

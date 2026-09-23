---
title: "Installation"
---

### Requirements

- **memoQ 12** – translator pro or project manager edition
- An API key for Anthropic, OpenAI or Google, or Claude Desktop or ChatGPT desktop if you would rather [translate through an assistant](/memoq/mcp-server/)
- Administrator rights on the computer, once, while installing
- *Optional:* memoQ's free **PDF Preview tool**, which the [live document link](/memoq/mcp-server/#the-live-document-link) needs. Everything else works without it.

A 14-day free trial starts by itself the first time Supervertaler runs. See [Licensing](/memoq/licensing/).

### Installing

1. **Download the installer** from [supervertaler.com/memoq](https://supervertaler.com/memoq/).
2. **Close memoQ.** memoQ keeps its add-ins open while it runs, so they cannot be replaced underneath it. The installer checks and says so if memoQ is still open.
3. **Run the installer.** Windows asks for administrator rights, because memoQ keeps its add-ins under Program Files. The installer finds memoQ by itself; there is nothing to choose.

What it puts where:

| | |
|---|---|
| memoQ's `Addins` folder, for example `C:\Program Files\memoQ\memoQ-12\Addins\` | the translation engine, the terminology provider, the [Supervertaler editor](/memoq/prompt-editor/) and the Claude Desktop extension |
| `C:\Program Files\Supervertaler for memoQ\` | the [live document link](/memoq/mcp-server/#the-live-document-link) |
| The Start menu | **Supervertaler for memoQ**, which opens the editor |

### Switching it on in memoQ

memoQ does not use a new add-in until you tell it to. The installer's last page lists the same two steps; after that, restart memoQ once.

1. **Terminology.** **Options → Terminology plugins**: tick **Perform terminology plugin lookups while working in the translation grid**, find **Supervertaler terms** in the list and tick **Enable plugin**.
2. **Translation.** **Options → Default resources → MT settings**: tick **Supervertaler** and answer **Yes** to all languages. Every new project then uses it. For a project you already have, choose it in **Project home → Settings → MT settings** instead.

Then [Getting started](/memoq/getting-started/) takes you through choosing a provider and a first translation.

### The unsigned plugin warning

memoQ may say, the first time it starts, that it has found one or more unsigned plugins, and ask whether to load them.

**Answer Yes.** The default button is *No*, so a stray Enter keypress declines it.

Supervertaler is not yet signed by memoQ. Signing is a process memoQ runs with a plugin's author, and until it is complete this prompt can appear after an install or an update.

### Updating

Close memoQ and run the new installer. It replaces the files in place; your settings, prompts, termbases, memory banks and licence are kept, because none of them live in the program folders.

### After a memoQ upgrade

memoQ's program folder carries its version number (`memoQ-12`, `memoQ-13`, …), and a major upgrade installs into a **new** folder, without the add-ins. If Supervertaler disappears after a memoQ upgrade, this is almost always why: run the Supervertaler installer again. It always installs into the newest memoQ it finds.

### Installing by hand

For an IT department that deploys centrally, or if the installer cannot run: the download is also available as a zip that holds the installer and the loose files. Copy `Supervertaler.MemoQ.dll`, `Supervertaler.MemoQ.Terms.dll` and `Supervertaler.PromptEditor.exe` into memoQ's `Addins` folder, then switch it on as above.

Installed this way there is no Start menu entry and no Claude Desktop extension beside the editor; [AI assistants](/memoq/mcp-server/#setting-it-up) explains the alternative.

### Uninstalling

Close memoQ, then remove **Supervertaler for memoQ** in Windows **Settings → Apps → Installed apps**.

Your own files stay where they are: prompts, termbases and memory banks in `C:\Users\<you>\Supervertaler\`, which Supervertaler for Trados shares. To remove what the plugin has learned from your documents as well, use **Forget stored context** in memoQ's Supervertaler options before uninstalling – see [Self-learning translation](/memoq/self-learning/#what-is-stored-and-where).

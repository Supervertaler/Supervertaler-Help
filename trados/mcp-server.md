---
title: "Supervertaler MCP Server"
---

The Supervertaler MCP Server connects AI assistants – Claude Desktop, ChatGPT's desktop app, Claude Code and other MCP-capable apps – **directly to your live Trados Studio session**. You chat in the AI app's own window, and it answers from your real project data: the document open in the editor, your translation memories, and your termbases. It can also make changes for you, always under your supervision.

MCP ([Model Context Protocol](https://modelcontextprotocol.io/)) is the open standard that lets AI applications securely call tools exposed by other programs. The Supervertaler MCP Server is the first MCP server that talks to a **live** Trados Studio editor session – other Trados-related MCP servers work on project files on disk, not the document you are working on.

<figure><img src="/.gitbook/assets/Supervertaler_MCP_Server.png" alt="An AI assistant asked to read the project open in Trados Studio and produce an English-Dutch glossary, answering with a term table grounded in the live document and the user's termbase"><figcaption>Asking the AI for a glossary drawn from the live Trados Studio project – it reads the open document and checks the user's termbase, then answers in chat.</figcaption></figure>

## What you can ask

With Trados Studio open and a document in the editor, you can ask your AI assistant things like:

* "What's the status of my Trados project? How many segments are left?"
* "How many times does the word *doekrol* appear in my project, and did I translate it consistently?"
* "Find all Draft segments containing *flange* and show me the translations."
* "How did I translate this phrase before?" (searches your Supervertaler TMs)
* "What does my termbase say for *sluitkracht*?"
* "Draft translations for the untranslated segments and set them to Draft so I can review them."
* "We agreed *draagarm* = *support arm* – add it to my termbase."

Unlike the [AI-friendly bilingual export](import-export.md) workflow, there is no export/re-import cycle: the AI reads the live document on demand, and changes it makes appear in Studio while you chat.

## What the AI can do

The server exposes these tools to the AI app:

| Tool | What it does |
| --- | --- |
| `get_active_project` | Project name, language pair, active file, segment counts per confirmation status |
| `get_segments` | List segments, with filters (status, contains-text) and paging |
| `get_active_segment` | The segment you are editing right now, with TM matches and termbase hits |
| `search_tm` | Search your Supervertaler translation memories |
| `lookup_term` | Look up a term in your termbases (exact first, then substring matching) |
| `update_segments` | Write translations and/or set confirmation statuses (see safety rails below) |
| `add_term` | Add a source/target pair to your Write termbases |
| `insert_into_active_segment` | Insert text into the active segment's target (like Apply-to-target) |

### Safety rails on write actions

* Translations written by the AI are set to **Draft** status unless it explicitly sets another status – so you can filter for them in Studio and review everything.
* **Locked segments are never touched.**
* Updates are limited to 200 segments per call; larger jobs are processed in reported batches.
* Changes land in the open document but are **not saved** – you decide when to save in Studio.
* The AI is instructed to only make changes you asked for, and to report exactly what it changed.

## Setting it up

1. In Trados Studio, open **Supervertaler Settings → AI Settings** and click **Connect AI assistant…** at the bottom. The dialog shows your current connection status.

<figure><img src="/.gitbook/assets/Supervertaler_MCP_Server_settings.png" alt="The Supervertaler Settings dialog, AI Settings tab, with the External AI assistants (MCP) section and its Connect AI assistant button highlighted at the bottom"><figcaption>The External AI assistants (MCP) section at the bottom of the AI Settings tab.</figcaption></figure>
2. **Claude Desktop** (easiest): click **Download extension (.mcpb)**, then double-click the downloaded `Supervertaler-MCP-Server.mcpb` file. Claude Desktop installs it as an extension. Restart Claude Desktop.
3. **Other AI apps**: click **Copy config snippet** and paste it into the app's MCP configuration, adjusting the path to where you saved `SupervertalerMcpServer.exe`.

Then open a project document in the Trados editor, and ask your AI app: *"What's the status of my Trados project?"*

Install the extension **or** use a manual config entry – not both, or every tool will appear twice in the AI app. The Connect dialog warns you if it detects this.

## Privacy and security

Everything stays on your computer:

* The connection between the AI app and Trados runs over **localhost only** – nothing is exposed to your network or the internet.
* Every Trados session uses a **fresh access token**; only programs on your own machine that hold the token can connect.
* Your project data goes to an AI model only when *you* ask the AI a question about it, through the AI app you chose – exactly as if you had pasted the text yourself. The MCP server itself sends nothing anywhere.

## Requirements

* Supervertaler for Trados with an active licence or trial (the bridge is part of the AI Assistant).
* An MCP-capable AI app. Note that this means the **desktop** apps – the claude.ai *website* cannot reach a local MCP server.
* Windows (the MCP server is a self-contained exe; no additional runtimes needed).

## Troubleshooting

* **The AI says it can't reach Trados** – make sure Trados Studio is running and a document is open in the editor (the bridge starts with the editor). The Connect dialog's status lines show whether the bridge is up.
* **Tools appear twice in Claude Desktop** – you have both the extension and a manual config entry; remove one (see above).
* **Term lookups return nothing** – check that your termbase/database path is set correctly in the Supervertaler settings (the same path TermLens uses).
* The bridge writes a diagnostic log to `<your data folder>\trados\runtime\bridge.log`.

Development of this feature is tracked publicly in [issue #44](https://github.com/Supervertaler/Supervertaler-for-Trados/issues/44) – feedback and use-case ideas are very welcome.

---
title: "Supervertaler MCP Server"
---

The Supervertaler MCP Server connects **Claude Desktop** directly to your live Trados Studio session. You chat in Claude's own window, and it answers from your real project data: the document open in the editor, your translation memories, and your termbases. It can also make changes for you, always under your supervision.

> **Which AI apps work?** Claude Desktop is fully supported and is the recommended app. Other MCP clients that run **local (STDIO) MCP servers on your own machine** – such as Claude Code – also work. **ChatGPT's desktop app is not supported**: it runs MCP servers in a cloud environment rather than on your computer, so it cannot reach the Supervertaler bridge, which is local to your machine by design (your project never leaves your PC). This is a difference in how the two apps are built, not something the plugin can change.

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
| `get_segments` | List segments, with filters (status, contains-text, file) and paging |
| `get_files` | The files of a merged multi-file document, with per-file segment counts *(v18.20.95)* |
| `get_active_segment` | The segment you are editing right now, with TM matches and termbase hits |
| `get_project_statistics` | Analysis bands and per-file confirmation statistics – word counts, progress *(v18.20.95)* |
| `search_studio_tm` | Concordance-search the Trados TMs attached to the project (.sdltm and GroupShare) *(v18.20.95)* |
| `search_tm` | Search your Supervertaler (Workbench-bridged) translation memories |
| `lookup_term` | Look up a term in your termbases (exact first, then substring matching) |
| `find_inconsistencies` | Repeated source segments whose translations differ *(v18.20.95)* |
| `check_numbers` | Translated segments whose numbers differ between source and target *(v18.20.95)* |
| `check_tags` | Translated segments with missing or extra inline tags *(v18.20.95)* |
| `check_terminology` | Translated segments that don't use the termbase's expected translation *(v18.20.95)* |
| `list_resources` | The TMs and termbases attached to your project and Supervertaler setup *(v18.20.95)* |
| `update_segments` | Write translations and/or set confirmation statuses (see safety rails below) |
| `add_term` | Add a source/target pair to your Write termbases |
| `insert_into_active_segment` | Insert text into the active segment's target (like Apply-to-target) |

### Safety rails on write actions

* Translations written by the AI are set to **Draft** status unless it explicitly sets another status – so you can filter for them in Studio and review everything.
* **Locked segments are never touched.**
* Updates are limited to 200 segments per call; larger jobs are processed in reported batches.
* Changes land in the open document but are **not saved** – you decide when to save in Studio.
* The AI is instructed to only make changes you asked for, and to report exactly what it changed.

## Prompt cookbook

You talk to the AI in plain language – there are no commands to memorise. The AI decides which tools to call from what you say. This section lists, per task, the kinds of things you can say, so you know the full range of what's possible. Mix and combine freely ("find X, then fix Y").

### Project status and progress

* "What's the status of my Trados project?"
* "How many segments are left to translate?"
* "Which file am I working on, and what's the language pair?"
* "How many words are still untranslated?" / "Give me the analysis statistics – fuzzies, repetitions, new words." *(from v18.20.95)*
* "How far along is each file in this project?" *(from v18.20.95)*

### Finding and reading segments

* "Show me all untranslated segments."
* "Show me the Draft segments so I can see what the AI wrote earlier."
* "Find all segments containing *flange*."
* "How many times does *doekrol* appear in this project? Is it translated consistently?"
* "Show me segments 50 to 100." (paging)
* "List the files in this merged document." / "Only show me segments from the contract file." *(from v18.20.95)*

### Terminology

* "What does my termbase say for *sluitkracht*?"
* "Look up *support arm* – do I have an established translation?"
* "Go through the project and make me a glossary of the key terms."
* "We agreed *draagarm* = *support arm* – add it to my termbase."
* "Extract the recurring technical terms from this document and add the ones I approve to my termbase."

### Translation memory

* "How did I translate this sentence before?" *(searches the Trados TMs attached to your project – from v18.20.95)*
* "Search my TM for *scherminrichting*."
* "Search only the target side of my TMs for *roller blind*." *(from v18.20.95)*
* "Before translating, check my TM and termbase and follow what you find."

### The segment I'm working on

* "Translate this segment." / "Explain this sentence."
* "What do my TM and termbase say about the current segment?"
* "Give me three alternative translations for this segment, then insert the one I pick."

### Writing translations (always reviewable)

* "Draft translations for all untranslated segments – I'll review them in Studio."
* "Translate the segments containing *warranty*, use my termbase, set them to Draft."
* "Redo segment 14 – too literal, make it flow better, then update it."
* "Set all my Draft segments to Translated." (status-only changes work too)

Everything the AI writes lands as **Draft** unless you say otherwise, locked segments are never touched, and nothing is saved until you save in Studio.

### Quality and consistency

* "Find segments where the source and target numbers don't match." *(from v18.20.95)*
* "Check my tags – any segments missing formatting?" *(from v18.20.95)*
* "Check my translated segments against the termbase and list violations." *(from v18.20.95)*
* "Find all repeated sentences that I translated differently." *(from v18.20.95)*
* "Run all your QA checks and give me a report."
* "…then align them all to the best version." (pairs with the write tools)

### Resources

* "Which TMs and termbases is this project using?" *(from v18.20.95)*

### Working across sources

Because the AI has all tools in one conversation, the most powerful prompts combine them:

* "Compare how I translated *closing force* in this project vs my TM – if they differ, tell me which is more common and align the project."
* "Draft the remaining segments, but first build a glossary from the segments I already translated and stick to it."
* "Review my Draft segments against the source: flag mistranslations, fix typos directly, and list anything you weren't sure about."

Items marked *(from v18.20.95)* require the next plugin version; everything else works from v18.20.94.

## Setting it up

<figure><img src="/.gitbook/assets/Supervertaler_MCP_Server_settings.png" alt="The Supervertaler Settings dialog, AI Settings tab, with the External AI assistants (MCP) section and its Connect AI assistant button highlighted at the bottom"><figcaption>The External AI assistants (MCP) section at the bottom of the AI Settings tab.</figcaption></figure>

1. In Trados Studio, open **Supervertaler Settings → AI Settings** and click **Connect AI assistant…** at the bottom. The dialog shows your current connection status.
2. **Claude Desktop** (easiest): click **Download extension (.mcpb)** to get `Supervertaler-MCP-Server.mcpb`. Then in Claude Desktop open **Settings → Extensions**, scroll to **Advanced settings**, click **Install extension…**, and choose the downloaded file. (If your system opens `.mcpb` files with Claude Desktop, double-clicking the file also works – many systems don't and will ask what app to open it with; just cancel and use the Install extension button.) Confirm the install, then restart Claude Desktop.
3. **Other MCP clients (Claude Code, etc.)**: click **Copy config snippet** and paste it into the app's MCP configuration, adjusting the path to where you saved `SupervertalerMcpServer.exe`. This works for clients that support local STDIO MCP servers in their normal chat (see the note at the top about ChatGPT).

Then open a project document in the Trados editor, and ask your AI app: *"What's the status of my Trados project?"*

> **Tip.** The connection starts automatically as soon as you have a document open in the Trados editor – you don't need to open the Supervertaler Assistant panel. (On plugin versions before 18.20.99 / 19.20.99 you had to click the Assistant panel once per session to start it; on current versions it's automatic.)

Install the extension **or** use a manual config entry – not both, or every tool will appear twice in the AI app. The Connect dialog warns you if it detects this.

## Privacy and security

Everything stays on your computer:

* The connection between the AI app and Trados runs over **localhost only** – nothing is exposed to your network or the internet.
* Every Trados session uses a **fresh access token**; only programs on your own machine that hold the token can connect.
* Your project data goes to an AI model only when *you* ask the AI a question about it, through the AI app you chose – exactly as if you had pasted the text yourself. The MCP server itself sends nothing anywhere.

## Requirements

* Supervertaler for Trados with an active licence or trial (the bridge is part of the AI Assistant).
* Claude Desktop (recommended), or another MCP client that runs local STDIO servers on your own machine. Note that this means a **desktop** app that executes the server locally – the claude.ai *website* and ChatGPT's desktop app cannot reach a local MCP server (see the note at the top of this page).
* Windows (the MCP server is a self-contained exe; no additional runtimes needed).

## Troubleshooting

* **Double-clicking the `.mcpb` file asks which app to open it with** – your system has no `.mcpb` association. Cancel the dialog and instead use Claude Desktop's **Settings → Extensions → Advanced settings → Install extension…** button. (Dragging the file onto the page does not work.)
* **The Extensions page is stuck on "Loading extensions…"** – the page needs to reach Anthropic's extension directory once before it renders; we've seen it hang on the Microsoft Store build of Claude Desktop. Fully quit Claude Desktop (including the system tray icon) and reopen it; check your internet connection. If it keeps hanging, there's a universal fallback that skips the Extensions page entirely: download `Supervertaler-MCP-Server-exe.zip` instead, unzip it somewhere permanent, and use the **Copy config snippet** button in the plugin's Connect dialog to add the server manually to `claude_desktop_config.json` (Claude Desktop → Settings → Developer → Edit Config).
* **The AI says it can't reach Trados** – make sure Trados Studio is running with a **document open in the editor** (the connection starts automatically once a document is open, not just when Studio is running). The Connect dialog's status lines show whether the connection is up. On older plugin versions (before 18.20.99 / 19.20.99) you also had to click the Supervertaler Assistant panel once per session – updating the plugin removes that step.
* **Tools appear twice in Claude Desktop** – you have both the extension and a manual config entry; remove one (see above).
* **Term lookups return nothing** – check that your termbase/database path is set correctly in the Supervertaler settings (the same path TermLens uses).
* The bridge writes a diagnostic log to `<your data folder>\trados\runtime\bridge.log`.

Development of this feature is tracked publicly in [issue #44](https://github.com/Supervertaler/Supervertaler-for-Trados/issues/44) – feedback and use-case ideas are very welcome.

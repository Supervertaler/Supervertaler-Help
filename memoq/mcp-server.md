---
title: "MCP Server (Claude Desktop)"
---

Supervertaler for memoQ can connect **Claude Desktop** — or any AI app that runs a local MCP server — to your live memoQ project. You chat in Claude's window; Claude reads the document you are translating, your confirmed segments and your glossary, and translates for you. The tokens are billed to your Claude subscription, not to an API key.

It is the same [Supervertaler MCP Server](/trados/mcp-server/) the Trados plugin uses. What differs is what memoQ lets a plugin do — which is a good deal less than Trados — so read [What it can and cannot do](#what-it-can-and-cannot-do) before you expect Trados behaviour.

> **Which AI apps work?** The same answer as for Trados: any app that runs a **local (STDIO) MCP server on your own machine** — Claude Desktop, ChatGPT's desktop app, Claude Code. Cloud-hosted clients (the claude.ai and chatgpt.com websites) have no route to a bridge that lives on your PC.

## The one thing to understand first

**memoQ never lets a plugin write into the grid.** A plugin cannot move your cursor, edit a segment or confirm anything. It can only *answer when memoQ asks it for a translation*.

So Claude does not write translations into memoQ. It **stages** them. They wait inside the plugin until you run **Pre-translate** (or land on the segment), at which point memoQ asks Supervertaler for a translation and receives Claude's. Every write into your document goes through your own hands — which is not a limitation so much as a built-in review step.

The other half: a plugin only *sees* what memoQ sends it. Claude cannot read your document until Supervertaler has been shown it. One Pre-translate pass does that.

## The workflow

With everything set up (below), a chat-driven job looks like this:

1. **Open the project** in memoQ and tick **Pre-translate via Claude Desktop (MCP)** in Supervertaler's settings (see [The checkbox](#the-checkbox)).
2. **Pre-translate** with Supervertaler as the MT engine. It is instant and free: the grid stays empty, but Supervertaler now holds every source segment.
3. **In Claude Desktop:** *"Read my memoQ project and translate it into Dutch."* Claude reads the segments, checks your glossary, and stages translations. Nothing has changed in memoQ yet.
4. **Pre-translate again.** The grid fills. Each row is marked `Claude (staged via Supervertaler MCP)` in Translation results.
5. **Confirm as you go.** If [Self-learning](/memoq/self-learning/) is on, each confirmation is visible to Claude too — *"what have I confirmed so far?"* — so a mid-job conversation about terminology is grounded in your actual choices.

Rows Claude has not staged still get a live suggestion from the model as you land on them, exactly as before. The checkbox only changes what **Pre-translate** does.

## The checkbox

In **Resource console → MT settings → Supervertaler → Configure plugin**:

> ☐ **Pre-translate via Claude Desktop (MCP) instead of the API key above**
> *Pre-translate then only hands the segments to the chat and inserts the translations it sends back; nothing is charged to the API key. Suggestions as you move through segments still use the API key.*

Both paths call an AI model. The checkbox decides **which one pays and who drives**: unticked, this plugin translates through the API key you entered; ticked, Pre-translate leaves the translating to the chat app, billed to that subscription.

| | Pre-translate | Landing on a segment |
|---|---|---|
| **Unticked** (default) | This plugin translates every segment through your API key. Staged translations are used first where they exist. | Live suggestion from the model; staged first if present. |
| **Ticked** | Hands the segments to the chat and inserts what it sends back. Nothing charged to the API key. | Unchanged — live suggestion from the model. |

Two consequences worth knowing:

- **You never have to toggle it mid-job.** Ticked is right for the whole of a chat-driven job: the capture pass is free, the delivery pass is free, and walking the document afterwards still gives you live suggestions for anything Claude did not cover.
- **Staged translations come through in either state.** Ticking the box is never a way to lose Claude's work; unticking it is never a way to block it. It only decides whether *Pre-translate* spends API money on rows nothing was staged for.

Leave it unticked if you use Supervertaler as an ordinary MT engine with no chat involved. That is the default, and it is what most memoQ users will want.

## Setting it up

The memoQ plugin does not yet ship a one-click Claude Desktop extension. You add one entry to Claude Desktop's configuration by hand.

1. Install the [Supervertaler MCP Server](/trados/mcp-server/#setting-it-up) if you have not already — the same `SupervertalerMcpServer.exe` serves both plugins.
2. Open Claude Desktop's config file: **Settings → Developer → Edit Config** (it is `%APPDATA%\Claude\claude_desktop_config.json`).
3. Add a server entry that points the exe at memoQ's handshake file:

```json
"mcpServers": {
  "supervertaler-memoq": {
    "command": "C:\\path\\to\\SupervertalerMcpServer.exe",
    "args": [],
    "env": {
      "SUPERVERTALER_BRIDGE_FILE": "C:\\Users\\<you>\\Supervertaler\\memoq\\runtime\\bridge.json"
    }
  }
}
```

   The `SUPERVERTALER_BRIDGE_FILE` variable is what makes this a *memoQ* connection: it pins the server to the handshake memoQ's plugin writes, instead of letting it look for Trados. If your Supervertaler data folder is somewhere other than `%USERPROFILE%\Supervertaler`, adjust the path.

4. Quit Claude Desktop fully (from the system tray) and start it again.
5. In memoQ, open a project and click into any segment with Supervertaler selected as the MT engine. That creates the engine, which starts the bridge and writes the handshake.
6. In Claude: *"What's in my memoQ project?"* If it answers with your language pair and segment count, you are connected.

If you also use the Trados plugin, both connections coexist: Trados through its extension, memoQ through this entry. Claude shows them as two servers.

## What it can and cannot do

Everything the Trados server can do that memoQ *cannot* comes down to one fact: memoQ has no project API, no editor API and no cursor for plugins. The table is the honest map.

| Tool | memoQ | Notes |
| --- | :---: | --- |
| `help` | ✓ | A menu of what you can ask, memoQ edition |
| `get_project` | ✓ | Language pair, client/domain/subject, captured documents, what is staged |
| `get_segments` | ✓ | The source segments Supervertaler has been shown — the whole document after one Pre-translate |
| `get_confirmed_pairs` | ✓ | Segments you have confirmed, via [Self-learning](/memoq/self-learning/) |
| `lookup_term` / `add_term` | ✓ | Your Supervertaler [glossary](/memoq/terminology/), not memoQ's term bases |
| `stage_translations` | ✓ | **The write channel.** Translations wait until you Pre-translate |
| `get_staged` / `clear_staged` | ✓ | Inspect and reset the staging area |
| `list_prompts` / `get_prompt` / `save_prompt` | ✓ | The shared [prompt library](/memoq/prompt-editor/) |
| `go_to_segment` | ✗ | No cursor control for plugins |
| `update_segments`, `insert_into_active_segment` | ✗ | No editor access — use `stage_translations` + Pre-translate |
| `get_active_segment` | ✗ | The plugin is not told which row you are on |
| `search_tm`, `search_studio_tm`, `compare_document_to_tm` | ✗ | memoQ's TMs are not readable by plugins; confirmed pairs are the substitute |
| `check_numbers`, `check_tags`, `find_inconsistencies`, `run_verification` | ✗ | Need the target text of every row, which memoQ never sends |
| `get_files`, `get_project_statistics`, `export_target` | ✗ | No project or file API |
| `pretranslate` | ✗ | You press Pre-translate; that is the design |
| SuperMemory tools | ✗ | Not yet wired for memoQ |

**Reading is nearly complete; writing goes through you.** In practice the chat-driven workflow above covers most of what people use the Trados server for. What you give up is Claude driving the editor — jumping to segments, editing rows in place, running QA on the target text — and there is no route to those in memoQ's SDK.

## Two channels for seeing the document

Supervertaler captures segments in two ways, and it helps to know which is which when Claude reports what it can see:

- **Translation requests** — every segment memoQ sends to Supervertaler as the MT engine. One Pre-translate captures the whole document, with its identity and metadata. This is the normal route.
- **Terminology lookups** — every row your cursor lands on, through the [terminology plugin](/memoq/terminology/), *regardless of which MT engine is selected*. So a document you pre-translated with Google or from TM alone still becomes visible to Claude one visited row at a time. memoQ does not tell the terminology plugin which document a row belongs to, so these land in a per-language-pair bucket rather than under the document.

`get_project` labels each captured document with its origin.

## Troubleshooting

**"Handshake file not found."** memoQ has not created a Supervertaler engine yet in this session. Open a project and click into a segment with Supervertaler selected as the MT engine.

**Claude says the project is empty.** Nothing has been captured yet. Run Pre-translate once, or visit some segments.

**Staged translations do not appear after Pre-translate.** They are matched by exact source text. If you edited a source segment after Claude read it, the match fails — ask Claude to re-read and re-stage that segment. Also check that Supervertaler is the selected MT engine for the Pre-translate run.

**`get_confirmed_pairs` is always empty.** Self-learning is not on. See [Self-learning translation](/memoq/self-learning/).

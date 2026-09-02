---
title: "MCP Server (Claude Desktop)"
---

Supervertaler for memoQ can connect **Claude Desktop** – or any AI app that runs a local MCP server – to your live memoQ project. You chat in Claude's window; Claude reads the document you are translating, your confirmed segments and your glossary, and translates for you. The tokens are billed to your Claude subscription, not to an API key.

It is the same [Supervertaler MCP Server](/trados/mcp-server/) the Trados plugin uses. What differs is what memoQ lets a plugin do – which is a good deal less than Trados – so read [What it can and cannot do](#what-it-can-and-cannot-do) before you expect Trados behaviour.

> **Which AI apps work?** The same answer as for Trados: any app that runs a **local (STDIO) MCP server on your own machine** – Claude Desktop, ChatGPT's desktop app, Claude Code. Cloud-hosted clients (the claude.ai and chatgpt.com websites) have no route to a bridge that lives on your PC.

## The one thing to understand first

**memoQ never lets a plugin write into the grid.** A plugin cannot move your cursor, edit a segment or confirm anything. It can only *answer when memoQ asks it for a translation*.

So Claude does not write translations into memoQ. It **stages** them. They wait inside the plugin until you run **Pre-translate** (or land on the segment), at which point memoQ asks Supervertaler for a translation and receives Claude's. Every write into your document goes through your own hands – which is not a limitation so much as a built-in review step.

The other half: a plugin only *sees* what memoQ sends it. Claude cannot read your document until Supervertaler has been shown it. One Pre-translate pass does that.

## The workflow

With everything set up (below), a chat-driven job looks like this:

1. **Open the project** in memoQ and tick **Pre-translate via Claude Desktop (MCP)** in Supervertaler's settings (see [The checkbox](#the-checkbox)).
2. **Pre-translate** with Supervertaler as the MT engine. It is instant and free: the grid stays empty, but Supervertaler now holds every source segment.
3. **In Claude Desktop:** *"Read my memoQ project and translate it into Dutch."* Claude reads the segments, checks your glossary, and stages translations. Nothing has changed in memoQ yet.
4. **Pre-translate again.** The grid fills. Each row is marked `Claude (staged via Supervertaler MCP)` in Translation results.
5. **Confirm as you go.** If [Self-learning](/memoq/self-learning/) is on, each confirmation is visible to Claude too – *"what have I confirmed so far?"* – so a mid-job conversation about terminology is grounded in your actual choices.

Rows Claude has not staged still get a live suggestion from the model as you land on them, exactly as before. The checkbox only changes what **Pre-translate** does.

## The checkbox

Either in the [prompt editor](/memoq/prompt-editor/), under **Settings**, which needs no project open and no memoQ running, or in memoQ under **Resource console → MT settings → Supervertaler → Configure plugin**:

> ☐ **Pre-translate via Claude Desktop (MCP) instead of the API key above**
> *Pre-translate then only hands the segments to the chat and inserts the translations it sends back; nothing is charged to the API key. Suggestions as you move through segments still use the API key.*

Both paths call an AI model. The checkbox decides **which one pays and who drives**: unticked, this plugin translates through the API key you entered; ticked, Pre-translate leaves the translating to the chat app, billed to that subscription.

| | Pre-translate | Landing on a segment |
|---|---|---|
| **Unticked** (default) | This plugin translates every segment through your API key. Staged translations are used first where they exist. | Live suggestion from the model; staged first if present. |
| **Ticked** | Hands the segments to the chat and inserts what it sends back. Nothing charged to the API key. | Unchanged – live suggestion from the model. |

Two consequences worth knowing:

- **You never have to toggle it mid-job.** Ticked is right for the whole of a chat-driven job: the capture pass is free, the delivery pass is free, and walking the document afterwards still gives you live suggestions for anything Claude did not cover.
- **It is one switch for the whole installation, not a project setting.** It says how you are working at this moment, so the editor and memoQ show the same state and either can change it.
- **Staged translations come through in either state.** Ticking the box is never a way to lose Claude's work; unticking it is never a way to block it. It only decides whether *Pre-translate* spends API money on rows nothing was staged for.

Leave it unticked if you use Supervertaler as an ordinary MT engine with no chat involved. That is the default, and it is what most memoQ users will want.

## Setting it up

**Claude Desktop:** install the extension.

1. Download `Supervertaler-for-memoQ-MCP-Server.mcpb` (it ships with the plugin).
2. In Claude Desktop, open **Settings → Extensions → Advanced settings** and click **Install extension…** (double-clicking the file also works if `.mcpb` is associated with Claude; drag-and-drop does not).
3. In memoQ, open a project and click into any segment with Supervertaler selected as the MT engine. That creates the engine, which starts the bridge.
4. In Claude: *"What's in my memoQ project?"* If it answers with your language pair and segment count, you are connected.

If you also use the Trados plugin, both extensions coexist – Claude shows them as two servers – and they are in fact the same server exe: the memoQ one carries a single setting, `SUPERVERTALER_HOST=memoq`, which tells it to look for memoQ's connection instead of Trados's.

**Other MCP clients** (ChatGPT desktop, Claude Code, anything that runs a local STDIO server): unzip the server exe somewhere permanent and register it with that one environment variable set:

```json
"supervertaler-memoq": {
  "command": "C:\\path\\to\\SupervertalerMcpServer.exe",
  "args": [],
  "env": { "SUPERVERTALER_HOST": "memoq" }
}
```

The exe finds memoQ's connection file in your Supervertaler data folder (`C:\Users\<you>\Supervertaler\memoq\runtime\bridge.json`, or wherever you moved that folder). If you ever need to point it somewhere else, `SUPERVERTALER_BRIDGE_FILE` with a full path overrides it.

## The live document link

memoQ's MT plugin interface never shows a plugin the target text, the row you are on, or even the document's name. memoQ's **Preview SDK** – the interface its own PDF and video preview tools use – shows all three, live. So Supervertaler ships a small preview tool, `Supervertaler.MemoQ.Preview.exe`, which registers with memoQ exactly as the PDF preview does and forwards what memoQ sends it to the plugin.

With it running, Claude sees your document as it actually is: every row's current target, memoQ's own row order, the document's real name, and the row your cursor is on – and it can ask memoQ to **jump to a segment**.

**Setting it up (once):**

1. Run `C:\Users\<you>\Supervertaler\memoq\preview\Supervertaler.MemoQ.Preview.exe` – inside your Supervertaler data folder, where the plugin's deploy puts it. A tray icon appears.
2. In memoQ, accept the **Preview tool connection request** for *Supervertaler*, leaving *Auto-start with memoQ* ticked. From then on memoQ starts the tool itself.
3. The tray icon reads *memoQ: connected · plugin: connected* once you click into a segment (that is what starts the plugin's bridge).

It appears under **Options → External preview tools** alongside any other preview tools; it can be disabled there like any of them. It draws nothing on screen – it is a link, not a preview.

One thing to know: memoQ's Preview SDK works in **paragraphs**, not segments. A paragraph that memoQ splits into three grid rows arrives as one unit with the whole paragraph's source and target. The active-segment tool still reports the exact sentence your cursor is on, and jumps can target a sentence within a paragraph. Without the tool running, the tools below fall back to what the plugin captured from translation requests, and the two cursor tools say so rather than guessing.

## What it can and cannot do

Everything the Trados server can do that memoQ *cannot* comes down to one fact: memoQ has no project API and no editor API for plugins. The live document link recovers the reading half of that; writing into the document still goes through you. The table is the honest map.

| Tool | memoQ | Notes |
| --- | :---: | --- |
| `help` | ✓ | A menu of what you can ask, memoQ edition |
| `get_project` | ✓ | Language pair, client/domain/subject, captured and live documents, what is staged |
| `get_segments` | ✓ | With the live link: rows in memoQ's order with source, **target**, and the active row marked. Without: the source segments captured from translation requests |
| `get_active_segment` | ✓ | The row your cursor is on, with what is selected – needs the live link |
| `go_to_segment` | ✓ | Asks memoQ to select a row – needs the live link |
| `get_confirmed_pairs` | ✓ | Segments you have confirmed, via [Self-learning](/memoq/self-learning/) |
| `lookup_term` / `add_term` | ✓ | Your Supervertaler [glossary](/memoq/terminology/), not memoQ's term bases |
| `stage_translations` | ✓ | **The write channel.** Translations wait until you Pre-translate |
| `get_staged` / `clear_staged` | ✓ | Inspect and reset the staging area |
| `list_prompts` / `get_prompt` / `save_prompt` | ✓ | The shared [prompt library](/memoq/prompt-editor/) |
| `update_segments`, `insert_into_active_segment` | ✗ | No write access to the editor – use `stage_translations` + Pre-translate |
| `search_tm`, `search_studio_tm`, `compare_document_to_tm` | ✗ | memoQ's TMs are not readable by plugins; confirmed pairs are the substitute |
| `check_numbers`, `check_tags`, `check_nbsp`, `check_terminology` | ✓ | QA over the live document, paragraph by paragraph – needs the live link. `check_terminology` runs against the active Supervertaler glossary, so give it a project one: [Export glossary](/memoq/prompt-editor/#export-glossary-the-prompts-terms-as-the-project-glossary) from an AutoPrompt draft |
| `find_inconsistencies` | ✓ | Repeated source paragraphs translated differently – needs the live link |
| `run_verification` | ✗ | memoQ's own QA cannot be run by a plugin; use memoQ's Run QA |
| `get_files`, `get_project_statistics`, `export_target` | ✗ | No project or file API |
| `pretranslate` | ✗ | You press Pre-translate; that is the design |
| SuperMemory tools | ✗ | Not yet wired for memoQ |

**Reading is complete with the live link; writing goes through you.** What you give up compared with Trados is Claude editing rows in place – and in memoQ the alternative, staging plus one Pre-translate, is a review step rather than a loss.

## Two channels for seeing the document

Supervertaler captures segments in two ways, and it helps to know which is which when Claude reports what it can see:

- **Translation requests** – every segment memoQ sends to Supervertaler as the MT engine. One Pre-translate captures the whole document, with its identity and metadata. This is the normal route.
- **Terminology lookups** – every row your cursor lands on, through the [terminology plugin](/memoq/terminology/), *regardless of which MT engine is selected*. So a document you pre-translated with Google or from TM alone still becomes visible to Claude one visited row at a time. memoQ does not tell the terminology plugin which document a row belongs to, so these land in a per-language-pair bucket rather than under the document.

`get_project` labels each captured document with its origin.

## Troubleshooting

**"Handshake file not found."** memoQ has not created a Supervertaler engine yet in this session. Open a project and click into a segment with Supervertaler selected as the MT engine.

**Claude says the project is empty.** Nothing has been captured yet. Run Pre-translate once, or visit some segments.

**Staged translations do not appear after Pre-translate.** They are matched by exact source text. If you edited a source segment after Claude read it, the match fails – ask Claude to re-read and re-stage that segment. Also check that Supervertaler is the selected MT engine for the Pre-translate run.

**`get_confirmed_pairs` is always empty.** Self-learning is not on. See [Self-learning translation](/memoq/self-learning/).

---
title: "Supervertaler MCP Server (Workbench)"
---

Supervertaler Workbench can connect **Claude Desktop** – or another AI app that runs a local MCP server – to the project you have open. You chat in the assistant's window, and it answers from your real project: the segments with their source and target, the segment you are in, your termbases and your translation memories. The tokens are billed to your Claude or ChatGPT subscription, not to an API key.

It is the same [Supervertaler MCP Server](/trados/mcp-server/) that the Trados and memoQ plugins use, pointed at Workbench.

> **This is a first step: the assistant can look, but not change.** It reads the project and can move your cursor to a segment. It cannot write a translation, change a status, add a term or touch a TM. Writing comes in a later version. See [What it can and cannot do](#what-it-can-and-cannot-do).

> **Windows only for now**, and it needs Workbench 1.10.382 or later.

## What you can ask

With Workbench running and a project open:

* "Using Supervertaler Workbench, which project do I have open, and how far along am I?"
* "In Workbench, show me segments 40 to 60."
* "In Workbench, list the segments that are still not started and contain *valve*."
* "In Workbench, which segment am I in? Is the translation accurate?"
* "Take me to segment 212 in Workbench."
* "What do my termbases say about the terms in this sentence?"
* "How did I translate *sluitkracht* before?" (searches your translation memories)
* "Read through segments 1 to 100 in Workbench and list anything that looks wrong, with segment numbers."
* "Check the numbers in my Workbench project." / "Are any tags missing?" / "Did I translate anything inconsistently?"
* "What do the comments on segment 18 say?"
* "List my Workbench prompts, and show me the patent one."

Say **Workbench** in your request if you also use the Trados or memoQ extension. Several tools have the same names in all three, and the assistant otherwise has to guess which program you mean.

## Setting it up

### Claude Desktop

1. Download [`Supervertaler-Workbench-MCP-Server.mcpb`](https://github.com/Supervertaler/Supervertaler-Workbench/releases/latest/download/Supervertaler-Workbench-MCP-Server.mcpb). It is attached to every Workbench release on [GitHub](https://github.com/Supervertaler/Supervertaler-Workbench/releases/latest).
2. In Claude Desktop, open **Settings → Desktop app**, scroll down to **Extensions** and click **Manage**. On the Extensions page, click **Advanced settings → Install extension** and pick the file. (Dragging the file onto the Extensions page works too. In Claude Desktop before late 2026 the same page was directly under **Settings → Extensions**.)
3. Confirm the install. It appears as **Supervertaler Workbench – MCP Server**.

Double-clicking the `.mcpb` file works on some computers and not on others; the route above works everywhere.

If you also use the Trados or memoQ extension, they sit side by side as separate servers and do not affect each other.

### Checking it works

Start Workbench, open a project, and ask in a new chat: *"Using Supervertaler Workbench, which project do I have open?"* If the assistant names your project and its languages, you are connected. Claude Desktop asks your permission the first time it uses each tool.

### ChatGPT desktop and other apps

Any app that can run a **local (STDIO) MCP server on your own PC** can use it: the server is one program, `SupervertalerMcpServer.exe`, started with one setting, `SUPERVERTALER_HOST=workbench`. So far it has been confirmed with Claude Desktop only.

To get the program, rename a copy of the `.mcpb` file to `.zip`, open it, and copy `server\SupervertalerMcpServer.exe` somewhere **permanent**, for example `C:\Users\<you>\Supervertaler\workbench\mcp\`. Then register it in your app. For apps that use a JSON settings file:

```json
"supervertaler-workbench": {
  "command": "C:\\Users\\<you>\\Supervertaler\\workbench\\mcp\\SupervertalerMcpServer.exe",
  "args": [],
  "env": { "SUPERVERTALER_HOST": "workbench" }
}
```

For ChatGPT desktop, which reads `%UserProfile%\.codex\config.toml` (see the [Trados page](/trados/mcp-server/#setting-it-up) for how to find and edit that file):

```toml
[mcp_servers.supervertaler-workbench]
type = "stdio"
command = 'C:\Users\<you>\Supervertaler\workbench\mcp\SupervertalerMcpServer.exe'
args = []
env = { SUPERVERTALER_HOST = "workbench" }
enabled = true
```

Cloud-hosted clients (the claude.ai and chatgpt.com websites) cannot reach a program on your PC.

## What it can and cannot do

| Tool | What it does |
| --- | --- |
| `help` | A menu of what you can ask |
| `get_active_project` | The open project: name, languages, project file, unsaved changes, segment counts per status, an approximate source word count, and the segment you are in |
| `get_files` | The project's files with their segment counts, and which one you are in |
| `get_segments` | Segments with source, target, status and locked flag. Filter by status, number range, file or text. At most 500 per call; the assistant pages through longer projects |
| `get_active_segment` | The segment your cursor is in, with the two before and after it |
| `go_to_segment` | Moves Workbench's cursor to a segment. Changes no text |
| `lookup_term` | The terms your termbases have for a piece of text, matched as [TermLens](/workbench/termbases/termlens/) matches them. Only the termbases ticked for the project |
| `list_tms` | Your translation memories, and which are ticked for the project |
| `search_tm` | Searches your TMs for a word or phrase, in source or target (a concordance search, not a fuzzy match on a whole segment). The TMs ticked for the project by default; all of them on request |
| `check_numbers` | Translated segments whose numbers differ from the source. Separators are set aside, so 1.234,56 matches 1,234.56 |
| `check_tags` | Translated segments with a tag or inline code missing from the target, or one in the target that is not in the source. The same check as **Tools → QA Checks** |
| `check_nbsp` | Translated segments with fewer non-breaking spaces than their source |
| `find_inconsistencies` | Repeated source segments translated in more than one way, compared with tags and spacing set aside |
| `get_comments` | The comments on a segment |
| `list_prompts` / `get_prompt` | Your [prompt library](/workbench/ai-translation/prompt-library/) |

Not available yet: writing or changing translations and statuses, find and replace, adding or changing terms, adding comments, saving, pre-translation and export. Do these in Workbench itself.

**The checks only look at translated segments**, and a finding is not always an error: a number written out as a word, a unit that was converted, formatting that rightly differs. The assistant lists what it found; you decide, and correct in Workbench. Ask it to take you to a segment and your cursor is there.

**Segment numbers** are the numbers in the first column of Workbench's grid, so a number the assistant cites is one you can find.

**A filter in the grid** can hide the segment the assistant wants to take you to. It then says it could not move there, rather than claiming it did; clear the filter and ask again.

**Two Workbench windows open at once:** the assistant is told that more than one is running and which one answered. To address the other, name its project: *"in the Acme project in Workbench, …"*.

## Privacy and security

Everything stays on your PC. Workbench only accepts connections from the same computer, and each one must present a password that Workbench makes anew every time it starts. What the assistant reads from your project does go to the AI service you are chatting with (Anthropic for Claude, OpenAI for ChatGPT), as anything you paste into a chat would: bear that in mind for confidential work.

## Troubleshooting

**"Supervertaler Workbench is not running."** Start Workbench. If it is running, it is older than this feature: update it.

**"No project is open in Supervertaler Workbench."** Open a project. The connection itself works as soon as Workbench has started.

**"Supervertaler Workbench is busy and did not answer in time."** Workbench was in the middle of something long, such as an import or a batch translation. Wait until it has finished and ask again.

**The assistant answers about your Trados or memoQ project instead.** Say *Workbench* in your request, or switch the other extension off for that chat.

**`lookup_term` finds nothing.** Only termbases ticked for the open project are searched. Tick them in the **Termbases** tab.

**The assistant does not know a tool this page lists.** The tool list comes from Workbench itself and is read when your AI app starts. Start Workbench first, then start (or fully restart) the AI app. New tools arrive with a Workbench update; the extension does not need reinstalling for them.

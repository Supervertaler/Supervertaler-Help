---
title: "Supervertaler MCP Server"
---

The Supervertaler MCP Server connects **Claude Desktop** directly to your live Trados Studio session. You chat in Claude's own window, and it answers from your real project data: the document open in the editor, your translation memories, and your termbases. It can also make changes for you, always under your supervision.

> **Which AI apps work?** Any app that can run a **local (STDIO) MCP server on your own machine**. Claude Desktop is the easiest, because the plugin ships a one-click extension for it. **ChatGPT's desktop app works too** *(confirmed August 2026)*, as do Claude Code and other clients with local MCP support — see [Setting it up](#setting-it-up) for each. What cannot work is anything that runs the server in the cloud rather than on your PC, including the claude.ai and chatgpt.com **websites**: the Supervertaler bridge is local by design, so your project never leaves your machine, and a cloud-hosted client has no route to it.
>
> *Earlier versions of this page said ChatGPT desktop could not be used. That was true when written and is no longer: the desktop app has since added support for local STDIO servers.*

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

Unlike the [AI-friendly bilingual export](/trados/import-export/) workflow, there is no export/re-import cycle: the AI reads the live document on demand, and changes it makes appear in Studio while you chat.

## What the AI can do

The server exposes these tools to the AI app:

| Tool | What it does |
| --- | --- |
| `help` | A curated menu of what you can ask – shown when you say *"what can I do?"* *(v18.20.106)* |
| `session_report` | How many bytes of tool results this session has sent the AI, per tool, biggest first – so you can see which tools are filling (and re-billing) the conversation *(v18.20.158)* |
| `get_active_project` | Project name, language pair, active file, segment counts per confirmation status |
| `get_segments` | List segments, with filters (status, contains-text, file) and paging – or fetch exact segments by the grid number(s) you see in Studio (`fromNumber`/`toNumber`) *(grid numbers v18.20.114)* |
| `get_files` | The files of a merged multi-file document, with per-file segment counts *(v18.20.95)* |
| `get_active_segment` | The segment you are editing right now, with TM matches and termbase hits |
| `get_project_statistics` | Analysis bands and per-file confirmation statistics – word counts, progress *(v18.20.95)* |
| `search_studio_tm` | Concordance-search the Trados TMs attached to the project (.sdltm and GroupShare) *(v18.20.95)* |
| `search_tm` | Search your Supervertaler (Workbench-bridged) translation memories |
| `lookup_term` | Look up a term in your termbases (exact first – against source and target terms alike – then substring matching); hits report which column matched and are never reoriented *(v18.20.153)* |
| `find_inconsistencies` | Repeated source segments whose translations differ *(v18.20.95)* |
| `compare_document_to_tm` | Every segment where your translation differs from what the TM already holds for the same source – the pre-delivery consistency check *(v18.20.148)* |
| `check_numbers` | Translated segments whose numbers differ between source and target *(v18.20.95)* |
| `check_tags` | Translated segments with missing or extra inline tags – compares underlying tag ids as well as counts, so two tags sharing one id are caught *(ids from v18.20.157)* |
| `check_terminology` | Translated segments that don't use the termbase's expected translation – longest-match-wins, ranked by signal rather than raw count, restrictable to a curated termbase *(overhauled v18.20.157)* |
| `check_nbsp` | Translated segments that lost a non-breaking space the source had – invisible on screen, so nothing else catches it *(v18.20.148)* |
| `get_coverage` | Which segments have been neither written nor explicitly reviewed this session, per TM match band – so "the fuzzy band was read" becomes checkable instead of remembered *(v18.20.157)* |
| `mark_reviewed` | Record that segments were read source-against-target and deliberately left unchanged – session-scoped, never written to the file *(v18.20.157)* |
| `get_tracked_changes` | The document's tracked changes as (before, after) pairs per segment – how you corrected the drafts – optionally saved into the active SuperMemory bank's reference folder for future projects *(v18.20.158)* |
| `list_resources` | The TMs and termbases attached to your project and Supervertaler setup – per termbase with its Read/Write ticks and whether it is the Project termbase *(roles from v18.20.159)* |
| `list_projects` | Every project registered in Trados Studio – across Studio 2026/2024/2022 – with status and paths *(v18.20.111)* |
| `get_project` | Details of any registered project by name, without opening it *(v18.20.111)* |
| `list_tms` | The file TMs on this machine (Studio folders + project references) *(v18.20.111)* |
| `list_project_templates` | Your Trados project templates *(v18.20.111)* |
| `update_segments` | Write translations and/or set confirmation statuses (see safety rails below) |
| `add_term` | Add a term pair to your Write termbases – direction-aware per termbase, with optional definition/domain/notes, termbase targeting by name or by role (project vs background – see below), and a per-termbase echo of exactly what was stored; duplicates echo the existing entry they matched *(scope + duplicate echo v18.20.159)* |
| `update_term` | Fix an existing entry in your Write termbases – exact-match; can change the term pair and, from v18.20.159, also the entry's notes, definition and domain – only the fields you name change, everything else is preserved |
| `delete_term` | Remove an entry from your Write termbases – destructive, so the AI confirms first *(v18.20.113)* |
| `import_project_termbase` | Copy the Trados termbase attached to the open project (`.sdltb` / `.ttb`) into a Supervertaler termbase in one step – the same job as the *Import .sdltb/.ttb…* button. Ask for a dry run first and it reports the entry count, language pair and field mapping before writing anything; running it twice adds nothing the second time. An existing destination must be Write-enabled, a new name is created for you, and your Trados termbase is only ever read *(v18.20.175)* |
| `insert_into_active_segment` | Insert text into the active segment's target (like Apply-to-target) |
| `save_document` | Save the open document (Ctrl+S) – only when you ask or approve *(v18.20.115)* |
| `go_to_segment` | Move the Studio editor to a specific segment (by grid number or id) |
| `find_and_replace` | Find & replace across the target text – tag-safe, with a preview before applying |
| `get_comments` | Read the Trados comments in the document |
| `add_comment` | Add a Trados comment to a segment (flag a source issue, leave a review note) |
| `update_comment` | Edit an existing Trados comment – its text, its severity, or both *(severity from v18.20.159)* |
| `delete_comment` | Remove a Trados comment (or all of a segment's) – destructive, so the AI confirms first *(v18.20.116)* |
| `run_verification` | Run Studio's Verify Files (QA Checker) and return the findings per segment – flagged as stale if the AI has unsaved edits *(stale flag v18.20.148)* |
| `analyze_files` | Run **Analyse Files** – computes the perfect/exact/fuzzy/new/repetition leverage breakdown *(v18.20.106)* |
| `pretranslate` | Run **Pre-translate Files** – fill untranslated segments with their TM matches |
| `update_tm` | Run **Update Main Translation Memories** – write confirmed segments to the project TM |
| `export_target` | Run **Generate Target Translations** – write out the translated target files |
| `get_task_status` | Check a background batch task's progress (analyse, pre-translate, …) *(v18.20.104)* |
| `list_prompts` | Browse your Supervertaler prompt library, optionally filtered by folder or search term *(v18.20.101)* |
| `get_prompt` | Read the full text of one of your prompts *(v18.20.101)* |
| `save_prompt` | Create a new prompt, or update one of your own – built-in defaults are protected *(v18.20.101)* |
| `get_prompt_context` | Everything the AI needs to write a translation prompt tailored to your open project – source text, domain, terms, TM examples *(v18.20.109)* |
| `get_supermemory_context` | The active [SuperMemory](/trados/ai-assistant/super-memory/) bank for this project – its brief, terminology table and style rules, plus the `_shared` bank of house defaults that the client bank overrides *(three-file banks from v18.20.169)* |
| `search_supermemory` | Search your active memory bank **and `_shared`** by keyword – *"what did I decide about this term, and why?"*. Each hit says which bank it came from *(v18.20.146; `_shared` included from v18.20.172)* |
| `list_supermemory_banks` | Your memory banks and which one is active. `_shared` is labelled as the always-loaded layer rather than listed as an ordinary bank *(v18.20.146; roles from v18.20.172)* |

> The four batch tasks (`analyze_files`, `pretranslate`, `update_tm`, `export_target`) run in the **background** and return immediately – the AI polls `get_task_status` and tells you when they finish, so a long analysis never stalls the chat.
>
> This list grows over time. For the current set on your installed version, just ask the AI *"what can I do?"* (the `help` tool).

### Safety rails on write actions

* Translations written by the AI are set to **Draft** status unless it explicitly sets another status – so you can filter for them in Studio and review everything.
* **Locked segments are never touched.**
* **Find & replace keeps each segment's confirmation status** *(from v18.20.148)*. Editing a segment's content normally demotes it to Draft, which meant a single consistency sweep over a finished file could quietly leave thousands of segments unconfirmed. The AI can still ask for a specific status when you want one.
* Updates are limited to 40 segments per call; larger jobs are processed in reported batches. *(Lowered from 200 in v18.20.148: bigger batches could outlast the connection timeout, and because the write had already gone through, the AI couldn't tell success from failure.)*
* Changes land in the open document but are **not saved automatically** – saving stays your decision. From v18.20.115 the AI can run the save for you (`save_document`, same as Ctrl+S), but only when you ask or approve – *"save and run the analysis"* is one instruction, silent saving is not allowed.
* The AI is instructed to only make changes you asked for, and to report exactly what it changed.

### Direction-aware termbase writes *(from v18.20.153)*

Termbases have a declared language direction, and yours don't all point the same way – a main termbase might be en→nl while a project termbase is nl→en. From v18.20.153 `add_term` handles this per termbase:

* **The AI states which language each side of the pair is in** (`sourceLang`/`targetLang`), and every termbase written to stores the pair according to **its own** declared direction. One request fills an en→nl and an nl→en termbase correctly at the same time – each entry the mirror of the other.
* **Ambiguity refuses instead of guessing.** If the languages can't be established – no document open, or a termbase whose language pair doesn't match – the write is refused with an explanation rather than performed silently. There is deliberately no language detection: technical term pairs are routinely identical in both languages (*radar*, *transponder*), so a detector would guess, and a wrong entry that *looks* fine is worse than a refusal.
* **The response proves what happened.** Every targeted termbase reports back individually: added (echoing exactly what was stored, in stored order, with a flag when the pair was reoriented), already present, or refused with the reason. `lookup_term` returns entries exactly as stored – never reoriented – and says which column your query matched, so a write can always be independently verified.
* **Entries can carry their context.** `add_term` accepts a definition, domain and notes alongside the pair, and can be told to write to specific termbases only instead of all Write-enabled ones.

### Project vs background termbases *(from v18.20.159)*

A common setup is two Write-enabled termbases with different roles: a large personal **background** termbase that accumulates terminology across all clients, and a per-job **project** termbase (the one with the **Project** tick in the Supervertaler Termbases settings – the same tick that renders its hits pink in TermLens). Before v18.20.159 a plain "add this term" wrote to both, indiscriminately. Now the roles are first-class:

* **The AI can target a role instead of a name.** *"Add this to my project termbase"* writes only to the Project-ticked termbase; *"add this to my background termbase"* writes only to the Write-enabled ones without the tick. Job-specific decisions no longer silently pollute your general glossary. Asking for the project termbase when none is ticked is refused with an explanation, never silently redirected.
* **Every result names its role.** Each termbase in an `add_term` response reports whether it is `project` or `background`, and `lookup_term` hits carry the flag too – so the AI can weight your curated project decisions above general-glossary entries when they conflict.
* **Duplicates show what they matched.** When a termbase refuses a pair as already present, the response now includes the existing entry (its id and exact stored pair) instead of a bare "duplicate" – no more guessing what it collided with.
* **Stale project termbases are flagged.** If the Project-ticked termbase's name shares no word with the open project's name – the classic sign of a tick left over from a previous job – the `add_term` response says so, before weeks of terms land in the wrong client's termbase.

## Prompt cookbook

You talk to the AI in plain language – there are no commands to memorise. The AI decides which tools to call from what you say. This section lists, per task, the kinds of things you can say, so you know the full range of what's possible. Mix and combine freely ("find X, then fix Y").

> **Not sure where to start? Just ask *"What can I do?"*** (or *"what can you do?"*) and the assistant shows a grouped menu of everything below – so you don't have to read this page first.

<figure><img src="/.gitbook/assets/Supervertaler_MCP_what_can_I_do.png" alt="Claude Desktop showing the answer to 'What can I do?' – a grouped, bulleted menu of example phrasings under headings such as Project &#38; progress, Find &#38; read segments, and Translation memory &#38; terminology"><figcaption>Ask <em>"What can I do?"</em> and the assistant lists what you can ask it, grouped by task.</figcaption></figure>

### Project status and progress

* "What's the status of my Trados project?"
* "How many segments are left to translate?"
* "Which file am I working on, and what's the language pair?"
* "How many words are still untranslated?" / "Give me the analysis statistics – fuzzies, repetitions, new words." *(from v18.20.95)*
* "How far along is each file in this project?" *(from v18.20.95)*
* "What projects do I have?" / "When did I create the ACME job, and where is it on disk?" *(all Studio versions' registries – from v18.20.111)*
* "Which TMs and project templates are on this machine?" *(from v18.20.111)*

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
* "That pair is outdated – replace it with the official MDR term in both termbases." *(update, exact-match, audited in chat – from v18.20.113)*
* "Delete that junk entry the QA keeps flagging." *(Write-enabled termbases only; the AI confirms before deleting – from v18.20.113)*
* "Only consult my **active** termbases for this lookup." *(restricts to termbases with Read ticked; otherwise inactive hits are flagged – from v18.20.113)*
* "Add *commandovoering* = *command and control* to my termbases – with the NATO definition and a usage note." *(direction-aware per termbase, with definition/domain/notes – from v18.20.153)*
* "Add this pair to the BRANTS termbase only." *(write to named termbases instead of all Write-enabled ones – from v18.20.153)*
* "Add this to my **project** termbase only." / "Put that one in my **background** termbase, it's not client-specific." *(role-based targeting via the Project tick – from v18.20.159)*
* "Extend the usage note on *eenzelfde* with a warning about the split spelling." *(edit an entry's notes, definition or domain in place, without touching the pair – from v18.20.159)*

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
* "Check whether I've lost any non-breaking spaces." *(from v18.20.148)*
* "Put a non-breaking space between every value and its unit." *(from v18.20.148)*
* "Where does my translation differ from the client's reference TM?" *(from v18.20.148)*
* "Run all your QA checks and give me a report."
* "…then align them all to the best version." (pairs with the write tools)

Comparing against the TM is worth a note of its own, because it answers a different question from concordance search. Searching the TM tells you whether a phrase *you already suspect* was translated before – one query at a time, for things you thought to look up. `compare_document_to_tm` goes the other way: it reads the attached TMs once and checks **every** segment whose source appears in them, then reports only where your wording differs. That surfaces the cases you had no reason to check, which is exactly where an established client rendering gets missed.

Two things to keep in mind. A difference is not automatically a mistake – on a real job most of them are deliberate improvements, and an improvement is indistinguishable from an error here, so the assistant is instructed to present the list for you to judge rather than align anything itself. And only segments whose source matches the TM word for word are compared, so a clean result means "nothing contradicts the TM", not "the whole document agrees with it".

Non-breaking spaces deserve a note of their own. They are invisible everywhere – in Studio, in the AI's view of your segments, in any report – so a lost one usually surfaces only when the client rejects the file. That matters if your style guide asks for one between a value and its unit (230 V, 3,5 mm, 50 %) or before a figure reference. `check_nbsp` compares each translated segment against its source and lists the ones that came out with fewer.

Inserting them used to be the harder half. A non-breaking space typed straight into a tool call survives the trip only sometimes: depending on the AI client and the individual call, it either arrives intact or is normalised to an ordinary space on the way, and because the write itself succeeds, nothing tells you which happened. Escape codes don't help either – the AI client decodes them into the character first, and then the character is what gets flattened. Being intermittent makes it worse rather than better: it works when you try it, and fails on the job.

From v18.20.148 the AI can write the character as the HTML entity `&nbsp;`, which Supervertaler turns into a real non-breaking space at the Trados end. Plain ASCII travels intact, so nothing en route can mangle it. This works for both writing translations and find & replace, and searching, so *"put a non-breaking space between every value and its unit"* fixes a whole document in one pass – and because find & replace preserves confirmation status, doing that to a finished file leaves it finished. It is deliberately opt-in, so a document that genuinely contains the text `&nbsp;` (an HTML manual, say) is never silently rewritten.

### Resources

* "Which TMs and termbases is this project using?" *(from v18.20.95)*
* "Are any of my termbases actually switched on for this project?" *(from v18.20.148)* – termbases are enabled per project, so a project with all of them off looks exactly like one with no terminology at all. The AI is now warned when nothing is read-enabled instead of silently finding no terms.

### Your memory bank *(from v18.20.146)*

Your [SuperMemory](/trados/ai-assistant/super-memory/) memory bank holds the reasoning behind your decisions – why a term was chosen, what a client insists on, what you rejected last time – which is exactly what a TM or termbase cannot tell an AI. From this version the AI can read it over MCP, not just inside the Supervertaler chat panel:

* "Read my memory bank for this project before we start."
* "What did I decide about *inrichting* for this client, and why?"
* "Check this translation against my style guide and terminology notes."
* "Which memory bank are you using?"

The AI cites the articles it drew from by path, so you can open them in Obsidian and check its reasoning. Retrieval is read-only – nothing is written back to the bank over MCP. If you have turned memory-bank context off under Settings → AI Settings, these tools stay quiet too.

### Your prompt library *(from v18.20.101)*

The AI can read and improve the Markdown prompts in your Supervertaler prompt library – the same ones you use in the QuickLauncher and Batch Translate (and shared with the Supervertaler Workbench):

* "List my prompts." / "Show me the prompts in my Translate folder."
* "Show me my Default Translation Prompt."
* "Look at my Default Translation Prompt and suggest improvements for patent work, then save it as a new prompt."
* "Turn what we just worked out into a prompt and save it as *Client X house style*."
* "Look at my open project and write me a translation prompt tailored to it." *(from v18.20.109 – the AI reads the source text, detected domain, relevant terms, and TM examples via `get_prompt_context`, then drafts and saves the prompt. How much source it sees is set under Settings → AI Settings → "Prompt context – source segments"; 0 = the whole document.)*

Built-in default prompts are protected – the AI saves your version under a new name rather than overwriting them.

### Working across sources

Because the AI has all tools in one conversation, the most powerful prompts combine them:

* "Compare how I translated *closing force* in this project vs my TM – if they differ, tell me which is more common and align the project."
* "Draft the remaining segments, but first build a glossary from the segments I already translated and stick to it."
* "Review my Draft segments against the source: flag mistranslations, fix typos directly, and list anything you weren't sure about."

Version tags like *(from v18.20.111)* show the plugin version a capability first shipped in – if the AI doesn't offer it, update the plugin. New tools appear in your AI app automatically after a plugin update; no extension reinstall is needed.

## Setting it up

<figure><img src="/.gitbook/assets/Supervertaler_MCP_Server_settings.png" alt="The Supervertaler Settings dialog, AI Settings tab, with the External AI assistants (MCP) section and its Connect AI assistant button highlighted at the bottom"><figcaption>The External AI assistants (MCP) section at the bottom of the AI Settings tab.</figcaption></figure>

1. In Trados Studio, open **Supervertaler Settings → AI Settings** and click **Connect AI assistant…** at the bottom. The dialog shows your current connection status.
2. **Claude Desktop** (easiest): click **Download extension (.mcpb)** to get `Supervertaler-MCP-Server.mcpb`. Then in Claude Desktop open **Settings → Extensions** and **drag the `.mcpb` file onto the page** – it shows a *"Drag .MCPB or .DXT files here to install"* target. (Prefer a file picker? Scroll to **Advanced settings** and use the **Install extension…** button instead.) Confirm the install. Double-clicking the `.mcpb` only works if your system has associated that file type with Claude Desktop; many don't and will ask which app to use – just cancel and drag-and-drop instead.
3. **ChatGPT desktop** *(Windows)*: ChatGPT desktop can run the server, but it has no drag-and-drop installer, so this is a short manual step. It takes about two minutes.

    **a. Get the server.** In the **Connect AI assistant…** dialog click **Download server (.zip)** (or take `Supervertaler-MCP-Server-exe.zip` from any [GitHub release](https://github.com/Supervertaler/Supervertaler-for-Trados/releases/latest)). Unzip it and move `SupervertalerMcpServer.exe` somewhere **permanent** — for example `C:\Users\<you>\Supervertaler\mcp\`. Do not leave it in Downloads: the path goes into a config file, and moving or clearing the file later breaks the connection.

    **b. Open the config file.** ChatGPT desktop reads its MCP servers from the same file as Codex CLI:

    ```
    %UserProfile%\.codex\config.toml
    ```

    Paste that path into File Explorer's address bar to jump straight to the folder. If the file or the `.codex` folder does not exist yet, create them — a config with only the block below in it is perfectly valid.

    **c. Add the server.** Append this to the end of the file, replacing the path with where you actually put the exe:

    ```toml
    [mcp_servers.supervertaler]
    type = "stdio"
    command = 'C:\Users\<you>\Supervertaler\mcp\SupervertalerMcpServer.exe'
    args = []
    enabled = true
    ```

    Use **single quotes** around the path, as shown. In TOML that makes it a literal string, so Windows backslashes are taken exactly as typed. With double quotes you would have to write every backslash twice.

    **d. Restart ChatGPT desktop properly.** Closing the window is not enough — it keeps running in the notification area. Right-click its icon there and quit, then start it again.

    **e. Check it.** With Trados Studio running, ask ChatGPT: *"What Trados project is open?"* It should name your project, and `SupervertalerMcpServer` should appear under **Sources** in the reply.

    > **If nothing happens**, work through these in order: is Trados Studio actually running? Does the path in `config.toml` point at a file that exists? Did you fully quit ChatGPT from the notification area? And is the rest of the file still valid TOML — a stray character anywhere in it can stop *every* server loading, not just this one.

4. **Other MCP clients (Claude Code, etc.)**: click **Copy config snippet** and paste it into the app's MCP configuration, adjusting the path to where you saved `SupervertalerMcpServer.exe`. The snippet is in Claude's JSON format; clients that use a different format need the same two facts — the transport is STDIO, and the command is the path to that exe.

Then open a project document in the Trados editor, and ask your AI app: *"What's the status of my Trados project?"*

> **Tip.** The connection starts automatically **as soon as Trados Studio is running** – no document or panel needed, so machine-wide questions ("what projects do I have?") work straight from the Projects view. (History: on 18.20.99–18.20.111 the connection started when you opened a document in the editor; before 18.20.99 you had to click the Supervertaler Assistant panel once per session.)

Install the extension **or** use a manual config entry – not both, or every tool will appear twice in the AI app. The Connect dialog warns you if it detects this.

## Privacy and security

Everything stays on your computer:

* The connection between the AI app and Trados runs over **localhost only** – nothing is exposed to your network or the internet.
* Every Trados session uses a **fresh access token**; only programs on your own machine that hold the token can connect.
* Your project data goes to an AI model only when *you* ask the AI a question about it, through the AI app you chose – exactly as if you had pasted the text yourself. The MCP server itself sends nothing anywhere.

## Requirements

* Supervertaler for Trados with an active licence or trial (the bridge is part of the AI Assistant).
* An MCP client that runs local STDIO servers on your own machine: Claude Desktop (recommended, one-click install), ChatGPT desktop, Claude Code, or similar. This means a **desktop** app that executes the server locally — the claude.ai and chatgpt.com *websites* run any server in the cloud and cannot reach a local one.
* Windows (the MCP server is a self-contained exe; no additional runtimes needed).

## Keeping it up to date

**The MCP server is a separate component and does not update with the plugin.** Updating Supervertaler for Trados through the App Store updates the half that lives inside Studio; the `.mcpb` extension (or the unzipped exe) is installed in your AI app and stays exactly as it was until you replace it. The two halves talking to each other across a version gap is the single most common source of odd behaviour.

After a plugin update that mentions the MCP server in its release notes, reinstall the extension: download the current `.mcpb` from the [latest release](https://github.com/Supervertaler/Supervertaler-for-Trados/releases/latest), install it the same way you did the first time, and restart your AI app. Installing over the existing extension is enough; there is nothing to uninstall first.

Good news first: **the list of tools is not baked into it.** The server asks Studio for the current tool list every time it starts, so tools and options added by a plugin update work with an older server — provided Studio was running when your AI app started. What *is* fixed at install time is the server's own behaviour, and the one symptom worth recognising is:

* **Errors mentioning a timeout of 30 seconds.** That limit was raised to 5 minutes in v18.20.148, so if you still see it, the installed server predates that release and should be replaced.

## Troubleshooting

* **The AI doesn't know about a tool or option the release notes describe** – this is almost never a stale download. The tool list is read from Studio once, when your AI app starts, and kept for that whole session, so an option added by a plugin update is missing simply because the AI app was already running (or started while Studio was closed) — a new option is then dropped from the call silently rather than reported as an error. The fix is order, not reinstallation: **start Trados Studio first, then start (or fully restart) your AI app.**
* **Double-clicking the `.mcpb` file asks which app to open it with** – your system has no `.mcpb` association. Cancel the dialog and instead either **drag the `.mcpb` onto the Extensions page**, or use Claude Desktop's **Settings → Extensions → Advanced settings → Install extension…** button. (Drag-and-drop works once the Extensions page has finished loading – if it's stuck on "Loading extensions…", see the next point first.)
* **The Extensions page is stuck on "Loading extensions…"** – the page needs to reach Anthropic's extension directory once before it renders; we've seen it hang on the Microsoft Store build of Claude Desktop. Fully quit Claude Desktop (including the system tray icon) and reopen it; check your internet connection. If it keeps hanging, there's a universal fallback that skips the Extensions page entirely: download `Supervertaler-MCP-Server-exe.zip` instead, unzip it somewhere permanent, and use the **Copy config snippet** button in the plugin's Connect dialog to add the server manually to `claude_desktop_config.json` (Claude Desktop → Settings → Developer → Edit Config).
* **The AI says it can't reach Trados** – make sure Trados Studio is running; from v18.20.112 the connection starts with Studio itself (on 18.20.99–18.20.111 you additionally needed a document open in the editor, and before that a click on the Supervertaler Assistant panel – updating the plugin removes those steps). The Connect dialog's status lines show whether the connection is up. Tools that read the open document still need one open, and will say so.
* **Tools appear twice in Claude Desktop** – you have both the extension and a manual config entry; remove one (see above).
* **Term lookups return nothing** – check that your termbase/database path is set correctly in the Supervertaler settings (the same path TermLens uses).
* The bridge writes a diagnostic log to `<your data folder>\trados\runtime\bridge.log`.

Development of this feature is tracked publicly in [issue #44](https://github.com/Supervertaler/Supervertaler-for-Trados/issues/44) – feedback and use-case ideas are very welcome.

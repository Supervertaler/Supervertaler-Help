---
title: "SuperMemory"
description: ">-"
---

**SuperMemory** is where you write down the things about a client that you cannot look up: which term they insist on, which wording they rejected last time, how they want dates written, what the previous reviewer changed and why. A translation memory gives the AI your previous wordings and a termbase gives it approved pairs; SuperMemory gives it the *reasoning* — and reasoning is exactly what an AI cannot derive from the source text, so getting it wrong is a real error rather than a stylistic difference.

Knowledge lives in **memory banks**: one folder per client, domain, or job, which you switch between from the Supervertaler Assistant toolbar. SuperMemory is one of several [context sources](/trados/ai-assistant/context-awareness/) the assistant consults, alongside termbases, translation memories, document content and segment metadata.

## A bank is three files

Every bank contains the same three Markdown files, plus a folder for source material:

| File | What goes in it |
| --- | --- |
| `brief.md` | Who the client is and anything standing: language pair, register, house preferences, how far to trust the rest |
| `terminology.md` | Term decisions, **one table**, one row each |
| `style.md` | Prose rules and approved boilerplate — how things are phrased, rather than which term is used |
| `reference/` | Source material, unmodified: style guides, PDFs, glossaries. Never sent to the AI |

That is the whole structure. You are meant to open these files and edit them by hand — the **📂 Open folder** button in the toolbar is there for exactly that.

### Why terminology is a table

A table is the format in which a *wrong* entry is findable. You can scan a hundred rows in half a minute and spot the one that says the wrong thing; you cannot do that with a hundred files. Since the only reason to keep notes is that you can check them, the format that makes checking possible is the one that matters.

```markdown
| Source | Target | Scope | Note |
|---|---|---|---|
| voorkeursvorm | preferred embodiment | domain | Not "preferred form" — term of art |
| drager | wearer | project | **Never** "carrier" |
```

**Scope** says how far a row travels — `project`, `client`, or `domain`. It doubles as a promotion queue: a row that turns out to hold for a *second* client belongs in the shared bank.

### `reference/` is the audit trail

Everything in the three files is *derived* from something — a style guide, a review round, a conversation. Keeping the original in `reference/` is what lets you check a rule that looks wrong and find out whether it was mis-derived or the source really does say that. Nothing reads this folder automatically, and that is deliberate.

## The `_shared` bank

Alongside whichever bank is active, Supervertaler always loads a bank called **`_shared`**. It holds the defaults that are true of *your* work rather than of any one client: house style, domain conventions, jurisdictional rules.

**Where they disagree, the active bank wins.** That is what a client bank is for — `_shared` says how you normally translate, and the client says how this one insists on it being done. The AI is told which layer is which, so it can apply the override rather than average the two.

A rule earns its place in `_shared` once it has held across more than one client. Until then it stays in the bank where you found it, tagged in the Scope column. Promote by *moving* the row, not copying it, or the two drift apart.

Create `_shared` like any other bank; the leading underscore keeps it at the top of the list and out of the way of client names.

## Banks

### Where they live

```
D:\Supervertaler\memory-banks\
├── _shared\          ← always loaded, alongside the active bank
│   ├── brief.md
│   ├── terminology.md
│   └── style.md
├── acme-legal\
│   ├── brief.md
│   ├── terminology.md
│   ├── style.md
│   └── reference\
└── pharma\
    └── …
```

### Switching

The **Memory Bank** dropdown lists every bank it finds. Switching is immediate — the next chat turn and the next batch translation both use the new bank, no restart, and your chat history is preserved. The choice persists across Trados sessions.

### Creating

Pick **+ New memory bank…** at the bottom of the dropdown, give it a short name (lowercase letters, digits, hyphens, underscores), and it is created with the three files already in place, each carrying its headings and a line explaining what belongs in it.

### Renaming and deleting

Not yet available from inside the plugin. Close Trados and rename or delete the folder under `memory-banks\` directly.

## Filling a bank

**Write in it.** Open the folder, edit `brief.md`, add rows to the table. This is the normal way, and there is no processing step between what you write and what the AI reads.

**[Quick Add](/trados/ai-assistant/super-memory/quick-add/) (Ctrl+Alt+M)** captures a decision without leaving the segment you are on. It appends one row to `terminology.md`.

**Drop source material into `reference/`** — a client style guide, a PDF, a glossary. Nothing happens to it automatically. When you want it in the bank, read it and write the parts that matter into the three files, or paste it into the chat and ask the assistant to draft the rows for you to check.

That last point is the design in one line: **the AI proposes, you decide what gets written.**

## The Report button

**☰ Report** tells you what the bank actually contributes: which files exist and how big, how many rows the terminology table has, **how many tokens get added to a prompt**, whether `_shared` is being applied, and warnings for things that are quietly wrong — a missing brief, a terminology file that is still prose rather than a table, files sitting in the bank root that are never sent to the AI.

It reads the files directly, so it is instant and costs nothing.

## Converting a bank from the old layout

Banks created before **v18.20.160** used a different structure: seven numbered folders and one file per fact. Those banks are **not read** by the current version — a bank with no `brief.md`, `terminology.md` or `style.md` contributes nothing to a prompt.

You will not be left guessing: when the active bank is on the old layout, an amber **⚠ Convert this bank** button appears in the toolbar. Converting folds the old articles into the three files and moves the originals to `reference/_legacy`. **Nothing is deleted.**

The conversion copies text across as-is; it does not tidy it up. Expect to read through the result and prune it — particularly the terminology, which arrives as prose and reads far better rewritten as a table. That work is yours on purpose: deciding which of a hundred old decisions still hold is judgement, and a machine that guesses confidently there is how the old system filled up with material nobody could check.

## Why this changed

Earlier versions organised a bank as a self-organising wiki: seven folders, one Markdown article per fact, YAML metadata on each, and AI features (Process Inbox, Distill, Health Check) that filed and maintained it for you.

It did not survive contact with real use. A single bank reached 136 terminology files — for what is a 136-row table — with a 97-file backlog nobody had processed. About 15% of articles had malformed metadata that silently excluded them from the very filtering the folders existed to enable: they were in the bank, and they were not reaching the AI. Nothing about that was visible from the outside, and by then the bank was far past the point where a human could read it and tell.

The lesson was not that automation is bad, but that **knowledge you cannot audit is not knowledge you can rely on**. Three files can be read start to finish in a few minutes. If a rule in there is wrong, you will see it — which is the only mechanism by which it ever gets fixed.

Process Inbox, Distill and Health Check are gone. They existed to manage complexity the new structure does not have.

## Working with a bank outside Trados

The active bank is exposed over the [Supervertaler MCP server](/trados/mcp-server/), so Claude Desktop, Claude Code or any other MCP client can read it: `get_supermemory_context` for the current picture, `search_supermemory` to look a decision up, `list_supermemory_banks` to see what exists. Access is read-only.

Beyond that, a bank is a folder of Markdown files. Edit it in any text editor, search it with ordinary tools, version-control it with Git, keep it in a synced folder so it follows you between machines. [Obsidian](https://obsidian.md/) works nicely if you like it, though with three files per bank you no longer need it to find your way around.

Supervertaler Workbench does not use memory banks. That remains a genuine gap rather than a setting you have missed.

## Features

| Feature | Description |
| --- | --- |
| [**Quick Add**](/trados/ai-assistant/super-memory/quick-add/) | Capture a term decision while translating (Ctrl+Alt+M) |
| [**Active Prompt**](/trados/ai-assistant/super-memory/active-prompt/) | Per-project prompt that Quick Add can also append terminology to |
| [**AI Integration**](/trados/ai-assistant/super-memory/ai-integration/) | What gets sent to the AI, and in what order |
| [**Obsidian Setup**](/trados/ai-assistant/super-memory/obsidian-setup/) | Optional: installing Obsidian and the Web Clipper |

## Related

* [**Context Awareness**](/trados/ai-assistant/context-awareness/) — the full menu of context sources, with SuperMemory as one of them
* [**AI Settings**](/trados/settings/ai-settings/) — toggles for enabling or disabling SuperMemory context

---
title: "memoQ and Trados Compared"
---

Supervertaler for memoQ and Supervertaler for Trados share one licence, one prompt library, one set of termbases and the same memory banks. What they can do inside the CAT tool is not the same, because memoQ gives a plugin much less access than Trados does: no window of its own, no way to edit the grid, and no access to memoQ's own translation memories or term bases.

This page lists the differences in one place. **✓** means the plugin can do it, **✗** means it cannot, and the last column says what to do in memoQ instead.

## Feature by feature

### Translating with AI

| What you want to do | Trados | memoQ | In memoQ instead |
|---|:---:|:---:|---|
| Get an AI suggestion for the segment you are on | ✓ | ✓ | – |
| Translate a whole file in one go | ✓ | ✓ | memoQ's own **Pre-translate**, with Supervertaler as the MT engine |
| Proofread a finished translation with AI | ✓ | ✗ | Ask an [AI assistant](/memoq/mcp-server/) to review the document, then fix the rows yourself |
| Chat with the AI inside the CAT tool | ✓ | ✗ | Chat in Claude Desktop or ChatGPT, connected to memoQ through the [AI assistant link](/memoq/mcp-server/) |
| One-click prompts on the current segment (QuickLauncher) | ✓ | ✗ | – |
| Put missing tags back into a translation (AutoTagger) | ✓ | ✗ | – |
| Voice control (SuperVoice) | ✓ | ✗ | – |

### Terminology

| What you want to do | Trados | memoQ | In memoQ instead |
|---|:---:|:---:|---|
| See termbase hits while you translate | ✓ | ✓ | Shown in memoQ's own terminology pane and Translation results, not in a Supervertaler panel |
| Have your Supervertaler termbases sent to the AI | ✓ | ✓ | – |
| Have the AI read the CAT tool's own term bases | ✓ | ✗ | Keep the job's terms in a Supervertaler termbase |
| Add a term from an AI assistant | ✓ | ✓ | – |
| Edit or delete a term from an AI assistant | ✓ | ✗ | Edit the termbase yourself |

### Translation memories

| What you want to do | Trados | memoQ | In memoQ instead |
|---|:---:|:---:|---|
| Have the AI read the CAT tool's translation memories | ✓ | ✗ | The segments you confirm are fed to the AI instead – see [Self-learning](/memoq/self-learning/) |
| Have the AI write to a translation memory | ✓ | ✗ | Confirm rows in memoQ; memoQ updates its TM itself |
| Search across all files and TMs in a project (SuperSearch) | ✓ | ✗ | memoQ's own concordance and find |

### Working with an AI assistant (Claude Desktop, ChatGPT)

| What you want to do | Trados | memoQ | In memoQ instead |
|---|:---:|:---:|---|
| Let the assistant read the document | ✓ | ✓ | Needs the [live document link](/memoq/mcp-server/#the-live-document-link) |
| Let the assistant write translations into rows | ✓ | ✗ | It **stages** them, and they go in when you run Pre-translate – see [The workflow](/memoq/mcp-server/#the-workflow) |
| Let the assistant change confirmed or locked rows | ✓ | ✗ | It stages a correction; you unlock the row, open it and accept the suggestion |
| Let the assistant confirm rows or change their status | ✓ | ✗ | Confirm them yourself |
| Let the assistant read and add comments | ✓ | ✗ | Add comments yourself |
| Let the assistant read tracked changes | ✓ | ✗ | – |
| Let the assistant find and replace across the document | ✓ | ✗ | memoQ's own Find and replace |
| Let the assistant check numbers, tags, non-breaking spaces, terminology and consistency | ✓ | ✓ | – |
| Let the assistant run the CAT tool's own QA | ✓ | ✗ | Run memoQ's **Run QA** yourself |
| Let the assistant start Pre-translate | ✓ | ✗ | Press Pre-translate yourself |
| Let the assistant save the document or export the target file | ✓ | ✗ | Save and export in memoQ |
| Let the assistant list projects and read file statistics | ✓ | ✗ | – |
| Let the assistant read your memory banks | ✓ | ✓ | – |
| Let the assistant update your memory banks | ✓ | ✗ | Edit the files yourself, in Obsidian or any text editor |

The full tool-by-tool list is under [AI assistants → What it can and cannot do](/memoq/mcp-server/#what-it-can-and-cannot-do).

## What memoQ would need to provide

Almost every ✗ above comes from one of a few missing doors into memoQ. Supervertaler could offer each of the following if memoQ made it available to plugins:

| What memoQ would provide | What it would make possible |
|---|---|
| **Write access to the grid**: set a row's target text and status (confirm, unlock, lock) | Assistants writing translations and corrections straight into rows, including locked ones, without a Pre-translate pass |
| **Read access to memoQ's translation memories and term bases** | TM matches and memoQ term base entries sent to the AI, as in Trados |
| **Read and write access to comments** | Translator's queries and source-defect notes added where they belong, on the row |
| **Access to projects and documents**: list them, read statistics, save, export | Assistants that can work across a whole project, not just the open document |
| **A way to start Pre-translate and Run QA, and read the QA results** | Assistants that can finish a job end to end and check their own work in memoQ's terms |
| **A panel or window inside the memoQ editor** | A chat, proofreading results, QuickLauncher and voice control without leaving memoQ |

If you know of a memoQ feature or API that already covers one of these, please [get in touch](/trados/support/).

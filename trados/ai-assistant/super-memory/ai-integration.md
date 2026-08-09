---
title: "AI Integration"
description: "What SuperMemory sends to the AI, and in what order"
---

When you translate a segment, run a batch translation, or ask the chat a question, Supervertaler builds the prompt from several context sources. This page covers what SuperMemory contributes.

## What gets sent

Two banks, in this order:

1. **`_shared`** — your house defaults, labelled as such.
2. **The active bank** — labelled as overriding the defaults above.

Within each, the three files are sent whole: `brief.md`, then `terminology.md`, then `style.md`. There is no selection step and no filtering — whatever is in those files is what the AI sees.

`reference/` is never sent. It holds the source material the three files were derived from, and a superseded draft answering as if it were current is precisely the failure it exists to prevent.

## Precedence

The prompt states plainly that the client section overrides the house defaults. That instruction only works because the two layers are kept separate rather than merged, so the AI can tell which rule came from where.

In practice: `_shared` might say *voorkeursvorm → preferred embodiment*, and a client bank might insist on *preferred form*. The client wins, and the override belongs in that client's bank — not as an edit to `_shared`, which would change the default for everyone.

## The bank is the selection

Earlier versions tried to work out which parts of a bank were relevant: matching your project name against client-profile filenames, detecting the document's domain, preferring one style guide over another, then loading whichever articles scored highest.

None of that happens now. **You pick the bank from the toolbar, and its contents are used** — because you already know which client you are working for, and a detection step could only get that wrong. It also means what reaches the AI is exactly what you would see by opening the folder, with nothing silently excluded.

## Token cost

A bank is small enough to send whole. Three files for a single client typically come to a few thousand tokens.

The **☰ Report** button tells you the exact figure for the active bank, including what `_shared` adds. Worth checking if you translate in large batches, where the context is re-sent for every call.

If a bank does grow past the budget, the shared layer is dropped before the client layer — the client bank was chosen deliberately and overrides the defaults anyway — and terminology is dropped last on each, being the densest content and the hardest for a model to guess.

## How SuperMemory compares with other context sources

SuperMemory does not replace your termbases or translation memories — it complements them, adding the reasoning that flat data cannot carry.

| Context source | What it provides | What SuperMemory adds |
|---|---|---|
| **Termbases** (Supervertaler + MultiTerm) | Term pairs: A = B | The *why*: reasoning, rejected alternatives, client-specific overrides |
| **Translation memories** | Previous wordings to anchor style | Rules that hold across segments, and which past work to trust |
| **Document content** | What this document is | Conventions and pitfalls the AI cannot read off the page |
| **AutoPrompt** | AI-drafted translation instructions | Client and domain context, so the draft starts from what you actually do |

For when stacking all of them is or is not optimal, see **Composing the context** in [Context Awareness](/trados/ai-assistant/context-awareness/#composing-the-context).

## Memory-aware chat

With SuperMemory context enabled, the chat can answer from your own decisions rather than from general knowledge:

- "What register should I use for this client?"
- "Does this client prefer *whilst* or *while*?"
- "What's the usual translation for *furtherance* here, and why?"

If the bank does not cover it, the assistant falls back to general knowledge and says so.

Because the banks are also readable over the [MCP server](/trados/mcp-server/), you can ask the same questions from Claude Desktop or Claude Code while Trados is open.

## Enabling and disabling

Toggled in [AI Settings](/trados/settings/ai-settings/):

- **Include memory bank in AI context** — for translations and chat.
- **Use memory bank when generating prompts (AutoPrompt)** — when AutoPrompt drafts a translation prompt.

Both are **off by default**. Turning them off does not delete anything — the files stay on disk.

## See Also

- [SuperMemory](/trados/ai-assistant/super-memory/) — how a bank is structured
- [Context Awareness](/trados/ai-assistant/context-awareness/) — the full menu of context sources
- [AI Settings](/trados/settings/ai-settings/) — the toggles
- [Batch Translate](/trados/batch-translate/) — batch translation with full context

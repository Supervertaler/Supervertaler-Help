---
title: "AI Integration"
description: "What SuperMemory sends to the AI, and in what order"
---

When you translate a segment, run a batch translation, or ask the chat a question, Supervertaler builds the prompt from several context sources. This page covers what SuperMemory contributes.

## What gets sent

Two banks, in this order:

1. **`_shared`** – your house defaults, labelled as such.
2. **The active bank** – labelled as overriding the defaults above.

Within each, the three files are sent: `brief.md`, then `terminology.md`, then `style.md`, followed by any other Markdown file you have put at the top of the bank (such as `figures.md`), under its own filename. A small bank goes whole. Two things narrow it, both described below: a large bank sends a translation only the part the document needs, and a note you have marked for the assistants stays out of translation.

`reference/` is never sent. It holds the source material the three files were derived from, and a superseded draft answering as if it were current is precisely the failure it exists to prevent.

## A large bank sends only what each document needs

*From v18/19.20.198.* Once the active bank and `_shared` together come to more than about 8,000 tokens, a translation no longer sends all of it with every request. The first time you translate a document – with Batch Translate, Translate active segment (Alt+T), **Preview prompt** or SuperBench – Supervertaler makes a selection for that document:

* **Terminology:** only the table rows whose term occurs in the document. Both columns are checked, so a Dutch–English table still serves an English–Dutch job.
* **Other notes:** your AI model is shown the start of the document and asked, once, which of the bank's other notes (such as `figures.md`) matter for it.
* **Always sent:** the brief and the style guide, of both the active bank and `_shared`.

The selection is kept for that document until you change a file in the bank, so every request of the job carries exactly the same text, and a provider that caches prompts keeps charging the cached rate. Opening a document sends nothing to the model; the selection is made only when you translate. If the question fails or times out, every note is sent, as it would be without selection. A bank of 8,000 tokens or less is sent whole, as before, and costs no extra request.

**Nothing is left out without a trace.** What was sent for each document, what was left out and why, is written to a file in the `trados\bank-extracts\` folder of your [data folder](/trados/data-folder/), one per document. The Batch Translate log names that file and gives the figures, for example:

```
SuperMemory: sending 12,910 tokens of the bank's 15,723 tokens, selected for this document.
  Left out as notes for the assistants only (audience: assistant): _shared/method.md.
  Terminology (_shared/terminology.md): 0 of 34 rows occur in this document.
  Articles: 0 of 1 chosen as relevant to this document by claude-opus-5-5; left out: figures.md.
  What was sent, and why: …\trados\bank-extracts\report.docx - 8fa68730.md
```

If a translation seems to have missed something you wrote down, that file is the place to look. The chat and the AI tools connected through the [MCP server](/trados/mcp-server/) do not use the selection: they read the bank as before.

## Notes for the assistants only

*From v18/19.20.198.* Some notes are about how to work a job – what to check before delivery, how to verify a termbase – and help an AI assistant rather than a sentence being translated. Put this at the very top of such a note:

```
---
audience: assistant
---
```

It is then left out of every translation: Batch Translate, Translate active segment, Preview prompt, SuperBench and AutoPrompt. The AI Assistant chat and the AI tools connected through the MCP server still read it – they are who it is written for. A note without the marker is sent as always. The Batch Translate log lists anything left out this way, as do the per-document file (for a large bank) and the **☰ Report** button.

## Precedence

The prompt states plainly that the client section overrides the house defaults. That instruction only works because the two layers are kept separate rather than merged, so the AI can tell which rule came from where.

In practice: `_shared` might say *voorkeursvorm → preferred embodiment*, and a client bank might insist on *preferred form*. The client wins, and the override belongs in that client's bank – not as an edit to `_shared`, which would change the default for everyone.

## The bank is the selection

Earlier versions tried to work out which parts of a bank were relevant: matching your project name against client-profile filenames, detecting the document's domain, preferring one style guide over another, then loading whichever articles scored highest.

None of that happens now. **You pick the bank from the toolbar, and its contents are used** – because you already know which client you are working for, and a detection step could only get that wrong. It also means what reaches the AI is what you would see by opening the folder. The one exception, a large bank narrowed for each document, never touches the brief or the style guide and writes down everything it leaves out (see [above](#a-large-bank-sends-only-what-each-document-needs)).

## Token cost

Three files for a single client typically come to a few thousand tokens, small enough to send whole. `_shared` adds to that, and a mature `_shared` can easily be the larger of the two.

The **☰ Report** button tells you the figure for the active bank, including what `_shared` adds. From v18/19.20.198 it gives what a *translation* sends; for a bank over the 8,000-token mark it gives the most a translation can send, since each document gets its own selection. Worth checking if you translate in large batches, where the context is re-sent for every call. The selection itself costs one small request per document, which appears in the [Reports tab](/trados/reports/) as **Memory bank selection** and in the usage log under SuperMemory.

A translation sends at most 24,000 tokens from the banks. If what is left after selection is still larger, the shared layer is dropped before the client layer – the client bank was chosen deliberately and overrides the defaults anyway – and terminology is dropped last on each, being the densest content and the hardest for a model to guess. From v18/19.20.198, when a terminology table would have to go, the rows the document uses least go first rather than the whole table.

## How SuperMemory compares with other context sources

SuperMemory does not replace your termbases or translation memories – it complements them, adding the reasoning that flat data cannot carry.

| Context source | What it provides | What SuperMemory adds |
|---|---|---|
| **Termbases** (Supervertaler + MultiTerm) | Term pairs: A = B | The *why*: reasoning, rejected alternatives, client-specific overrides |
| **Translation memories** | Previous wordings to anchor style | Rules that hold across segments, and which past work to trust |
| **Document content** | What this document is | Conventions and pitfalls the AI cannot read off the page |
| **AutoPrompt** | AI-drafted translation instructions | Client and domain context, so the draft starts from what you actually do |

For when stacking all of them is or is not optimal, see **Stacking the layers** in [Context layers](/trados/context-layers/#stacking-the-layers).

## Memory-aware chat

With SuperMemory context enabled, the chat can answer from your own decisions rather than from general knowledge:

- "What register should I use for this client?"
- "Does this client prefer *whilst* or *while*?"
- "What's the usual translation for *furtherance* here, and why?"

If the bank does not cover it, the assistant falls back to general knowledge and says so.

Because the banks are also readable over the [MCP server](/trados/mcp-server/), you can ask the same questions from Claude Desktop or Claude Code while Trados is open.

## Enabling and disabling

Toggled in [AI Settings](/trados/settings/ai-settings/):

- **Include memory bank in AI context** – for translations and chat.
- **Use memory bank when generating prompts (AutoPrompt)** – when AutoPrompt drafts a translation prompt.

Both are **off by default**. Turning them off does not delete anything – the files stay on disk.

## See Also

- [SuperMemory](/trados/ai-assistant/super-memory/) – how a bank is structured
- [Context layers](/trados/context-layers/) – the full menu of context sources
- [AI Settings](/trados/settings/ai-settings/) – the toggles
- [Batch Translate](/trados/batch-translate/) – batch translation with full context

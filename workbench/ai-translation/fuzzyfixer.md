---
title: "FuzzyFixer"
---

FuzzyFixer adapts an existing fuzzy TM match to the current source segment instead of translating it from scratch. When an 80–95% match is sitting right next to a segment, FuzzyFixer feeds that match into the AI prompt and asks the model to make only the edits the source change requires – keeping the existing wording, terminology, and tags wherever the source is unchanged.

This is useful for repetitive, lightly-revised content (updated manuals, contract variants, new product revisions) where translating cold throws away a near-perfect human translation that is already in your TM.

> Inspired by a suggestion from David Turnbull.

## Why use it

By default the AI never sees a segment's fuzzy TM match – it translates from the source alone, even when a high match is available. FuzzyFixer closes that gap: the model starts from the TM target and revises it minimally, so the result stays closer to your approved style and terminology than a fresh translation would.

## Running it on a single segment

1. Move to a segment that has a fuzzy match in range (see **Match range** below).
2. Run FuzzyFixer one of three ways:
   - Click the **🔧 FuzzyFixer** button on the Match Panel's **TM Source** box (it is enabled only when the shown match is in range).
   - Choose **Translate → 🔧 Fuzzy Fix Current Segment**.
   - Press **Ctrl+Alt+F**.

After it runs, the **TM Target** box shows a **track-changes view** of what the AI changed: the original TM target with the AI's insertions underlined and removed words struck through, so you can see the edit at a glance before confirming.

## Using it in batch translation

In the **Batch Translate** dialog, tick **🔧 Use FuzzyFixer**. When enabled:

- The AI pass runs **per segment** (no batching), so each segment gets its own in-range fuzzy match injected into the prompt.
- Segments **without** an in-range match are translated normally.
- The toggle is remembered between sessions.

Because it disables batching, FuzzyFixer batch mode is slower and costs more per segment than ordinary batch translation – use it on jobs that are genuinely revision-heavy.

## Configuring it

### Match range

Settings → **AI Settings** → **🔧 FuzzyFixer**. FuzzyFixer only acts on matches inside a percentage range (default **75%–99%**). 100% exact matches are **never** altered. Lower the floor to catch looser matches, or raise it to limit FuzzyFixer to very close matches only.

### Instruction template

Settings → **System Prompts** → **FuzzyFixer Instruction**. This editable template tells the model how aggressively to revise. In addition to the usual `{{SOURCE_TEXT}}`, it supports these placeholders:

| Placeholder | Meaning |
| ------------- | ------- |
| `{{TM_SOURCE}}` | The matched TM entry's source text |
| `{{TM_TARGET}}` | The matched TM entry's target text (the translation being adapted) |
| `{{MATCH_PCT}}` | The match percentage |
| `{{TM_NAME}}` | The name of the TM the match came from |
| `{{SOURCE_TEXT}}` | The current segment's source text |

## Tracking cost

FuzzyFixer's AI calls are logged under their own **"FuzzyFixer"** task in [Token Usage & Costs](usage-costs.md). Group the usage table by Task to see them broken out from ordinary translation.

---

## See Also

- [Fuzzy Matching](../translation-memory/fuzzy-matching.md)
- [AutoTagger](autotagger.md)
- [Batch Translation](batch-translation.md)
- [Prompts](prompts.md)
- [Token Usage & Costs](usage-costs.md)

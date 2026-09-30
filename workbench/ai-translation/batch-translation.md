---
title: "Batch Translation"
---

Translate multiple segments at once with AI.

## Starting Batch Translation

1. **Select segments** to translate:
   - Click first segment, Shift+click last for a range
   - Or use **Edit → Select All** (`Ctrl+A`)
   
2. **Start batch**:
   - Go to **Translate → Batch Translate** and choose which segments to translate, for example **Translate selected not-started segments**
   - Or press `Ctrl+Shift+T` for **Translate all not-started & pre-translated**

## The Batch Translate dialog

The dialog asks how the segments should be translated. Tick one of:

- **📖 TM (Translation Memory)** – pre-translate from the TMs switched on for the project (exact matches and fuzzy matches from 75%). Tick **⚡ Exact matches only** to use 100% matches only, which is fastest.
- **🤖 LLM (AI)** – translate with AI (the default). The provider and model are the ones chosen in **Settings → AI Settings**; the dialog shows which one under **📊 Current LLM**.
- **🌐 MT (Machine Translation)** – use the MT providers you have set up in **Settings → MT Settings**.

### Options

- **🔄 Retry until all segments are translated (recommended)** – see [Retry Feature](#retry-feature) below.
- **✔ Auto-confirm 100% TM matches** – with TM selected, exact matches are confirmed straight away instead of getting the TM 100% status.
- **🔧 Use FuzzyFixer (adapt fuzzy TM matches with AI)** – see [FuzzyFixer](/workbench/ai-translation/fuzzyfixer/). Segments are then sent one at a time.

Click **Start Translation** to begin.

### The cost estimate

With **🤖 LLM (AI)** ticked, the dialog shows what the run is likely to cost before you start, for example:

```
💰 Estimated cost: ~$0.42 · ~120,000 tokens in / ~35,000 out in 12 call(s)
```

- The estimate uses your actual prompt and glossary, your **Batch size** (Settings → AI Settings) and the same price list as the [usage log](/workbench/ai-translation/usage-costs/). When the prompt is long enough for the provider to cache it, batches 2 onwards are priced at the cheaper cached rate, as they will be billed.
- It updates when you tick **🔧 Use FuzzyFixer**, which sends one call per segment and so costs more.
- It is hidden when **📖 TM** or **🌐 MT** is ticked.
- A local (Ollama) model shows as free. A model that isn't in the price list shows "unknown" rather than pretending to be free.
- The amount is shown in dollars or euros, whichever you chose in [Token Usage & Costs](/workbench/ai-translation/usage-costs/#showing-costs-in-euros).

It is an estimate (token counts are worked out at about 4 characters per token); the actual cost of every call is logged in **Tools → 💰 Token Usage & Costs**.

## Progress Tracking

During translation:
- Progress bar shows completion
- Per-segment status updates
- Can cancel anytime

## Retry Feature

**🔄 Retry until all segments are translated** is on by default. It will:
- Automatically detect empty translations
- Retry failed segments (up to 5 passes)
- Ensure all segments get translated

## Tips

### Optimal Batch Size

- 50-100 segments per batch works well
- Very large batches may timeout
- Split by page if needed

### Quality vs Speed

- Claude Sonnet 4.6: Good all-round balance of speed and quality
- GPT-5.5 / Claude Opus 4.8: Highest quality, slower and more expensive
- GPT-5.4 Mini / Gemini 3.1 Flash-Lite: Fastest, lower cost

### Post-Edit Strategy

After batch translation:
1. Review each segment
2. Fix any obvious errors
3. Confirm with `Ctrl+Enter`

---

## See Also

- [AI Translation Overview](/workbench/ai-translation/overview/)
- [Creating Prompts](/workbench/ai-translation/prompts/)
- [Single Segment Translation](/workbench/ai-translation/single-segment/)
- [Token Usage & Costs](/workbench/ai-translation/usage-costs/)

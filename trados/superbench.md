---
title: "SuperBench"
description: "Translate the same text with three models under identical settings, and have a judge say which to use for this project."
---

Which model should you use for this project? SuperBench answers that with evidence from the document in front of you rather than from a benchmark of somebody else's text. Available from v18.20.187.

## What it does

1. You pick **three models**, one per slot – any provider each. The defaults are Claude Opus 5, GPT-5.6 Sol and Gemini 3.1 Pro.
2. You pick a **judge** – Claude Fable 5.1 by default – and how many segments of the open document to use. Twenty is a good start.
3. Each model translates those segments through the batch pipeline itself. The selected prompt, the termbase terms that occur in the text, the document context, SuperMemory and the batch size are exactly what a real Batch Translate would send; only the model changes. **Nothing is written to the document.**
4. The judge reads the source and the three translations **blind** – labelled A, B and C in a shuffled order, so no brand name colours the verdict – together with the same approved terms and instructions, and writes a short report: a ranked verdict, the significant errors per candidate with segment numbers, how each handled terminology and tags, and a recommendation for this project.
5. The translations appear side by side above the report, with each model's cost and time. The whole thing is saved as Markdown in `trados\reports` inside your data folder, and **Save report…** writes a copy wherever you like.

<figure><img src="/.gitbook/assets/Supervertaler-for-Trados-SuperBench.jpg" alt="The SuperBench window after a run: three model slots and a judge at the top, the source and three translations side by side in a table, and the judge's report below with its legend"><figcaption>A finished run on the inline-formatting test document: Claude Opus 5, GPT-5.6 Sol and Gemini 3.1 Pro side by side, judged by Claude Fable 5.1. The legend above the report maps the judge's letters to the models.</figcaption></figure>

## Running it

1. Open the document and set up the Batch Operations tab as you would for a real run: the prompt, and the termbases ticked for AI on the Termbases tab.
2. Click **⚖ SuperBench…** next to **Preview prompt**.
3. Choose the three models, the judge and the number of segments. The line under the segment count shows the estimated cost of the three runs and the judge's call.
4. Click **Run SuperBench**. The status line follows the runs; **Cancel** stops after the current call.

## Reading the report

The legend at the top of the report maps the judge's letters to the models. The judge's own text uses only the letters.

- **Verdict** – the best candidate for this text, and a ranked list.
- **Errors** – the significant errors per candidate, each with the segment number and the words in question. "None found" means the judge looked and found nothing.
- **Terminology** and **Tags** – whether the approved terms were used and the inline tags kept.
- **Recommendation** – which to use for this project, and whether the difference is worth paying for.

A judge is a model too. Treat the report as a well-informed second opinion: read the segments it names before deciding, and run it again on a different stretch of the document if the verdict is close.

## Cost

Three batches of twenty segments plus one judge call costs a few cents with the default models; the estimate is shown before you run, and the actual cost per model is in the report. Every call is logged like any other AI call, so it appears in the Reports tab and the usage ledger.

---
title: "Duet Review"
---

From v1.10.373, a **Duet review** lets two different AI models review a translation prompt together, for example Claude and GPT. They take turns checking each other's points against your project, and when they agree, one of them writes the improved prompt. You get the improved prompt as a **new version** in your library, next to the original, and a full transcript of the discussion.

Two models catch problems that neither finds alone: a wrong term, an instruction that contradicts the glossary, a rule that would break your TM matches. They also reject each other's bad "improvements", as long as they are made to check each other's claims. The review is built around that.

## Starting a review

1. Open the **✨ AI** tab and go to the **Prompt Manager**.
2. Right-click a prompt in the library and choose **🎭 Duet review…**.
3. Choose the two models:
   - **Model A** and **Model B**: a provider and its model. The list shows the providers you have an API key for in **Settings → 🤖 AI Settings**. Two *different* models work best.
   - **Round limit** (default 4): in one round, each model has one turn.
   - **Max output tokens per turn** (default 4000).
   - **Source sample**: how many segments of the document to show the models.
   - **Opens** and **Writes the result**: which model goes first and which writes the final prompt.
4. Check the estimate below the options, then click **▶ Start review**.

The models see the prompt and the open project:
- the language pair;
- the first segments of the document;
- your confirmed translations (or, before you've confirmed any, TM matches for the first segments);
- the terms of the glossaries switched on for the project.

Open the project you want the prompt for before you start.

## What the models are asked to do

Two models left to chat agree far too soon. So every turn has to follow these rules:

- **Check before agreeing.** A model checks every claim the other made against the attached material and quotes the evidence. What the material doesn't support is rejected.
- **Keep a register.** Each turn carries a numbered list of **OPEN ISSUES**. An issue is closed only by stating how it was resolved.
- **Protect validated terminology.** Terms that your confirmed translations, TM matches or glossary support stay as they are, unless a model quotes evidence that they are wrong.
- **End with a verdict.** Every turn ends with `VERDICT: CONTINUE` or `VERDICT: AGREED`. AGREED is only allowed with an empty register, and only after at least three real problems have been raised and resolved.

When both models say AGREED one after the other, the chosen model writes the improved prompt, followed by a list of anything still disputed. If the round limit is reached first, it writes the best version both models accepted and lists the remaining disagreements.

You can follow the discussion turn by turn in the dialog, and **■ Stop** ends it after the current turn.

## The result

When the review is finished, the dialog shows:

- **Improved prompt**: you can still edit it.
- **Unresolved (for you to decide)**: what the models didn't agree on. These are decisions only you can make, such as house style or client preferences.

Click **💾 Save as new version** to save the prompt to the library, next to the original, as *&lt;name&gt; (duet v2)*. A later review of that version becomes *(duet v3)*. The original prompt is never changed. The new version's description says which models reviewed it, whether they agreed, how many points are unresolved, and where the transcript is.

## The transcript

The whole discussion is saved as a Markdown file in the project's **`reports/duet/`** folder, or in `workbench/duet/` in your data folder if the project hasn't been saved. The file is written after every turn, so nothing is lost if something goes wrong halfway. **📄 Open transcript** opens it.

Keep it with the project: it records why the prompt says what it says.

## Cost

The whole discussion so far is sent again on every turn, so the cost grows quickly with the number of rounds. Before you start, the dialog shows how many characters go to each model per turn. It also shows the tokens and the approximate cost if all rounds run, in the currency set for [Token Usage & Costs](/workbench/ai-translation/usage-costs/).

To keep it affordable:

- give the models a **sample**: lower **Source sample**, rather than sending a whole document;
- start with 3–4 rounds; most reviews agree within that.

If a provider returns an error, Supervertaler waits 15 seconds and tries again, then 30 seconds. After a third failure the review stops, and the transcript so far is kept.

## One segment at a time

The same debate can settle a single contested translation: right-click a segment in the grid and choose **🎭 Arbitrate This Segment (two AI models)…**. See [Cross-model Review → Arbitrate This Segment](/workbench/qa/cross-model-review/#arbitrate-this-segment).

## See also

- [Prompt Manager](/workbench/ai-translation/prompt-library/)
- [Cross-model Review](/workbench/qa/cross-model-review/), where a second model reviews translations
- [AutoPrompt](/workbench/ai-translation/autoprompt/), which writes a first prompt that a Duet review can then improve
- [Supported LLM Providers](/workbench/ai-translation/providers/)

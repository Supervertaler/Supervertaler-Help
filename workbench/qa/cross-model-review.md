---
title: "Cross-model Review"
---

From v1.10.373, a **cross-model review** has a second AI model check translations made by another one. For example, Claude reviews what GPT translated. A model easily overlooks its own mistakes, but a different model with different blind spots catches many of them. Translation agencies call this *translate–edit–proofread*.

The reviewer checks every translation against its source, and against the instructions the translating model followed: your project's prompt and glossary. It answers each segment with *pass* or a **flag**: what is wrong, and how to fix it. It never changes a translation. The flags appear in the Proofreading comments tab, marked **XR**.

## Running a review

There are two ways:

- **After a batch translation.** In the Batch Translate dialog, tick **🔀 Then have a second AI model review the translations (cross-model review)**. When the batch is finished, the review of the new translations starts at once. The option is remembered.
- **At any time.** Choose **QA ▸ Proofreading ▸ 🔀 Cross-model Review…**, and choose the segments:
  - **Translations not yet confirmed** (the default);
  - **All translations**;
  - **Selected segments**: select rows in the grid first.

In the dialog, set:

- **Reviewed by**: the reviewing provider and model. The dialog shows which model translated, or after a batch, which one did. If you choose the same model, it warns you: a different model catches more.
- **The reviewer also gets**:
  - **The project's translation prompt**: your custom prompt and the prompts attached to it, as the translating model got them;
  - **The glossary terms found in the segments**, from the glossaries switched on for the project. Forbidden terms are included, so the reviewer can flag them.

Check the estimate below the options, then click **▶ Start review**. The segments are sent in batches of 20, and **■ Stop** ends the review after the current batch. Flags received so far are kept.

## The results

- **Flags** become proofreading comments named **XR · *model***, for example *XR · claude-sonnet-5-5*. In the grid, the segment's Status cell turns purple, as for any proofreading comment.
- When the review finishes, the **💬 Comments ▸ ✅ Proofreading** list shows only the XR flags. Use **Show:** at the top of the list to switch between **All comments**, **AI proofreading**, **Cross-model review (XR)** and **Translator comments (TC)**.
- If you review again with the same model, a segment that now passes loses its earlier flag. A segment that is flagged again gets the new flag.
- A **report** of the review goes to the project's **`reports/cross-review/`** folder: who translated, who reviewed, with which prompt, and every flag with its source and translation. **📄 Open report** opens it.

Settle a flag by editing the translation, or ask two models to settle it with **Arbitrate This Segment** (below). Then delete the flag with its 🗑️ button.

## Translator comments (⟦TC⟧)

A prompt made with [AutoPrompt](/workbench/ai-translation/autoprompt/) tells the AI to correct obvious mistakes in the source silently, and to mark each such segment with a comment at the end of the translation, such as `⟦TC: "verzekerd" corrected to "verzekert"⟧`. Those comments are in the target text, so they would end up in your exported document.

**QA ▸ Proofreading ▸ ⟦TC⟧ Move Translator Comments out of the Target Text** moves them into proofreading comments named **TC · translator**, and leaves the translation clean:

- the list then shows the TC comments;
- the reviewer's XR flags stay apart from them, so you can tell who said what;
- **Ctrl+Z** puts the comments back in the text;
- locked segments are left alone.

The reviewer sees ⟦TC⟧ comments that are still in the text. It checks that the correction was right, and doesn't flag the comment itself.

## Arbitrate This Segment

When you can't decide on a flagged or doubtful translation, two models can debate it. Right-click the segment in the grid and choose **🎭 Arbitrate This Segment (two AI models)…**. This works for one segment at a time only, on purpose.

The models follow the rules of a [Duet review](/workbench/ai-translation/duet-review/): each must check the other's claims and quote evidence, keep a register of open issues, and end every turn with a verdict. They see:

- the source and the current translation;
- **What's contested**: the segment's review comments are filled in. You can add your question, for example "which term is right here?";
- the two segments before and after it;
- the project's prompt;
- the glossary terms in the segment;
- TM matches of 70% and more.

Choose **Model A**, which opens, and **Model B**, which writes the result. By default A is the model in your AI Settings, and B is the reviewer of your last cross-model review, or another provider. Then click **▶ Start**. The default round limit is 3.

When they agree, or at the round limit, model B writes the final translation, and anything still disputed is listed under **Unresolved**. Nothing changes until you click **✔ Use this translation**, and you can edit the proposal first. **Ctrl+Z** undoes it. If the models keep the current translation, the button stays off.

The debate is saved in the project's **`reports/arbitration/`** folder, as *Segment N – date.md*.

## Cost

- A **cross-model review** costs about as much as translating the same segments again with the reviewer. Your prompt and the glossary terms are sent with every batch of 20 segments.
- An **arbitration** is a short Duet. The dialog shows the worst case, when all rounds run.

Both dialogs show an estimate in your currency before you start (see [Token Usage & Costs](/workbench/ai-translation/usage-costs/)).

## See also

- [AI Proofreading](/workbench/qa/proofreading/)
- [Comments](/workbench/editor/comments/#proofreading-comments)
- [Duet Review](/workbench/ai-translation/duet-review/)
- [Batch Translation](/workbench/ai-translation/batch-translation/)

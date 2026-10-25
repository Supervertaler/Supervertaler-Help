---
title: "Ai Proofreader"
---

The AI Proofreader checks your translated segments for errors using AI. It identifies issues such as mistranslations, omissions, grammar problems, and inconsistencies, and presents the results as clickable issue cards in the **Reports** tab. From v18/19.20.200 you can [apply its fixes](#applying-fixes-from-v181920200) to the segments from there, one at a time or all at once.

## Starting a Proofreading Run

1. Open the **Supervertaler Assistant** panel (View > Supervertaler Assistant)
2. Switch to the **Batch Operations** tab
3. Select **Proofread** (instead of Translate)
4. Optionally tick **Translation only (no source)** for a quick final read of the translation alone – see [Checking the translation only](#checking-the-translation-only-from-v181920201)
5. Choose a **scope** from the dropdown
6. Optionally select a proofreading **prompt** from the prompt selector
7. Click **Proofread**

## Scope

The scope dropdown controls which segments are checked:

| Scope                              | Description                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------- |
| **Translated only**                | Checks only segments with Translated status                                     |
| **Draft only** *(from v18/19.20.200)* | Checks only segments with Draft status – the status Batch Translate and the [MCP server](/trados/mcp-server/) leave AI translations in |
| **Translated + approved/signed-off** | Checks segments with Translated, Approved, or Signed-off status              |
| **All segments**                   | Checks every segment that has target text                                       |
| **Filtered segments**              | Checks only segments visible after applying a Trados display filter             |
| **Filtered (translated only)**     | Checks translated segments within the current filter                            |

## Checking the translation only (from v18/19.20.201)

A full check sends every segment with its source, so the AI can compare the two. After post-editing, when the translation has already been checked against the source, a last read for slips is often all that is left – and for that the source is not needed. Tick **Translation only (no source)** on the Batch Operations tab, in Proofread mode, and the proofreader is sent the translation alone.

It checks what can be seen in the translation on its own:

* **Spelling and typos**
* **Editing leftovers** – words doubled, left behind or half replaced while the text was edited, so that a sentence no longer runs
* **Grammar** – agreement, verb forms, word order, articles and prepositions
* **Punctuation and spacing**
* **Number formatting** – numbers, dates and measurements as the target language writes them
* **Consistency** – the same word or name spelled, capitalised or hyphenated differently in different segments
* the **language-specific checks** for Dutch, German and French targets
* your **memory bank**, with SuperMemory on: its language and style rules, and any term decision that can be judged from the translation alone, such as a word the client never wants used

What it cannot check without the source is whether the translation says what the source says: **accuracy, omissions, additions and terminology**. The AI is told so, and not to guess at what the source might say. No termbase is sent either, not even its forbidden terms: whether a term is right depends on the source term it translates – a word forbidden for one source term can be the right one for another. There are no source queries.

Leaving the source out takes roughly half off the segments and the document context sent with them. Your instructions and the memory bank are sent either way, so on a fully translated document a run costs roughly a third to a half less – the most when the memory bank is small. Segments not yet translated are left out of the document context altogether: on the example project, where only a fifth of the segments are translated, a run took 10,000 input tokens instead of the full check's 20,800. Your proofreading prompt is still sent; where it asks for something that needs the source, such as source queries or source segment citations, the AI is told to leave that part out and follow the rest.

* **Findings work as in a full check.** Each comes with a correction you can [apply](#applying-fixes-from-v181920200), with the same safeguards: a correction that would lose a formatting tag or a line break is not applied, and nor is one for a segment that has changed since the check. Supervertaler still compares against the source on your computer before writing; it is only not sent to the AI.
* **The report says what was checked.** The Reports tab footer reads *translation only*, and the saved report has a line saying the check was made without the source.
* **The box is not remembered.** Every time Trados Studio starts, Proofread starts with the full check, so a box left ticked never skips the accuracy check on your next job by accident.
* **It works in Clipboard Mode too**: the copied prompt then carries the translation only.
* **Preview prompt** shows exactly what is sent.

The box takes the place of **Send TM matches to the AI** and **Retry segments left empty**, which apply to Batch Translate and are hidden in Proofread mode.

## Prompt Selection

When in Proofread mode, the prompt dropdown shows only prompts with the **Proofread** category. This keeps the list focused – translation prompts are hidden. The prompts that come with Supervertaler are listed first, straight under **(Built-in instructions only)**, and hovering over the dropdown summarises what each kind of item means.

Until you choose a proofreading prompt, for the project or overall, Proofread uses the **Default Proofreading Prompt** *(from v18/19.20.200; before that, it started on no prompt at all)*. To proofread with Supervertaler's built-in instructions alone – accuracy, completeness, terminology, grammar and number formatting, without the default prompt's rules – choose **(Built-in instructions only)** at the top of the list. That choice is remembered, as is turning off the active proofreading prompt in the Prompt Manager.

:::note
You can create custom proofreading prompts in the [Prompt Manager](/trados/settings/prompts/). Set the category to **Proofread** so they appear in the dropdown when proofreading.
:::

### Default Proofreading Prompt

The shipped **Default Proofreading Prompt** is deliberately slim. The hardcoded base of every Batch Proofread already includes the persona, the five quality categories (accuracy / completeness / terminology / grammar / number formatting), the output format, and language-specific checks for Dutch, German, and French – so the prompt itself only needs to add what's missing from the base.

What the default prompt *does* add:

* **Default to OK.** Raise an ISSUE only when a specific, demonstrable problem can be pointed to in the translation – never speculative or hypothetical concerns.
* **Citation discipline.** When flagging a terminology consistency issue, the AI must cite specific source segment numbers in the **Evidence:** field – e.g. *"`'trekriem'` rendered as `'pull belt'` in `[SEGMENT 0031]`, `'draw strap'` in `[SEGMENT 0084]`"*. Inconsistency claims without concrete citations are not allowed.
* **Source query distinction.** If the source itself contains an error (typo, duplication, missing word, internal inconsistency), the AI prefixes the Issue line with **"Source query:"** and notes whether the translation handled it correctly. A faithful rendering of a flawed source is not a translation error.
* **Explicit boundaries.** The AI does not re-engineer the source, propose alternative terminology without a citation, flag stylistic preferences as errors, or flag empty target lines (those mean the segment hasn't been translated yet).

:::note
**If you want to customise:** clone the default in the [Prompt Manager](/trados/settings/prompts/) and edit your copy. The default itself is read-only and gets refreshed when the plugin updates. Your clone keeps all your changes.
:::

### The answer format is fixed *(from v18/19.20.198)*

The format every verdict must follow – `[SEGMENT 0001] OK`, or `ISSUE` followed by the **Issue:**, **Evidence:** and **Suggestion:** lines – is now stated once, in a fixed **output contract** at the very end of the instructions, after your prompt and the document. A custom proofreading prompt can add checks of its own but cannot change the format by accident, which is what the Reports tab reads. **Preview prompt** shows it.

The contract also sets how a **source query** is written. When the problem is in the source rather than the translation – a typo, a missing word, a contradiction – the Issue line starts with *Source query:* and the rest is written as your comment to the client: 5 to 20 words, stating the problem and the fix, with no reasoning, ready to pass on as it stands. The Suggestion line says whether the translation needs to change. It is the same register as the `[[TC: …]]` comments [Batch Translate](/trados/batch-translate/#translator-comments) writes.

From v18/19.20.200 the contract asks for one more line on every issue, last: **Corrected:**, the segment's whole translation with the fix made and nothing else changed – every other word, space and formatting tag as it was. That is what [Apply](#applying-fixes-from-v181920200) writes into the segment. A source query whose translation can stay as it is has no Corrected line. Until v18/19.20.199 the contract said the opposite – describe the fix, never return a corrected translation – so a custom proofreading prompt that repeats that old rule should drop it.

## Reports Tab

Proofreading results appear in the **Reports** tab of the Supervertaler Assistant panel. Each issue is shown as a clickable card containing:

* **Segment number** – the actual per-file segment number as shown in the Trados editor grid. In a document made of several files, where Trados Studio numbers every file from 1, the card also names the file – **Segment 3 of Acme - Text.docx** – and the cards are listed file by file *(from v18/19.20.201)*
* **Issue description** – what the AI found wrong
* **Evidence** *(when applicable)* – specific source segment numbers the AI cites to back up the claim, shown in italic grey between the issue and the suggestion. Required for terminology consistency claims (see *Default Proofreading Prompt* below) so you can verify the inconsistency yourself by jumping to the cited segments.
* **Suggestion** – the AI's recommended fix (if available)
* **Correction** *(from v18/19.20.200)* – the whole translation with the fix made, in green, exactly as **Apply** would write it. Formatting tags show as numbered placeholders, such as `<t1>WARNING!</t1>`: the same tag numbers as in the source.

Right-click any card to copy the issue, the evidence, the suggestion, the correction, or the whole card to the clipboard.

### Navigating to Issues

Click any issue card to navigate directly to that segment in the Trados editor. This works correctly in multi-file projects – the plugin uses the segment's internal identifiers to find the exact segment.

### Dismissing Issues

Each issue card has a checkbox. Tick it to dismiss the issue and remove it from the list. This lets you work through the results one by one, keeping track of which issues you have already addressed. When all issues have been dismissed, the Reports tab shows "All issues addressed – well done!"

### Applying fixes (from v18/19.20.200)

A card with a correction has an **Apply** button. Click it to write the correction into the segment; the card then goes, as a ticked-off one does. **Apply all**, at the top of the Reports tab, does the same for every card you have not ticked off – so read through the cards first and tick off the ones you disagree with.

* **The segment is set to Draft**, so the fix still goes through your normal review.
* **Track Changes follows the document.** With Track Changes on, the fix is recorded as tracked changes, word by word: only the words that changed are struck out and inserted, so you or a reviewer can see exactly what the AI changed and accept or reject it. With Track Changes off, the fix is written as a plain edit.
* **Formatting tags are kept.** The proofreader is shown each segment with its tags, and its correction comes back with them, so bold, links and other inline tags stay where they were.
* **Non-breaking spaces are kept.** An AI writes ordinary spaces, so Supervertaler puts the translation's own non-breaking spaces and hyphens back wherever the correction leaves the text around them alone – "0,4 mm" keeps its non-breaking space when only the number is corrected.
* **Nothing is written over newer work.** Before writing, Supervertaler checks that the segment still reads exactly as it did when it was proofread. If you or anyone else has changed it since, the card stays and says **Not applied: the segment has changed since it was checked**: proofread it again, or fix it by hand.
* **The reason can go with the fix** *(from v18/19.20.201)*. With **Also add issues as Trados comments** ticked on Batch Operations, each fix you apply also gets its issue as a Trados comment, so a reviser who accepts or rejects the tracked change can see why it was made. See [Adding Issues as Trados Comments](#adding-issues-as-trados-comments-from-v181920201).

Some corrections cannot be applied at all, and the card says why instead of showing an **Apply** button – a correction that would lose or add a formatting tag, or drop a line break, for example. A locked segment is never written. A source query whose translation can stay as it is has no correction.

A segment that still holds tracked changes nobody has accepted or rejected cannot be written while Track Changes is off: Trados Studio protects them. Its card stays and says so *(from v18/19.20.201; before that, Apply could report it as applied while the segment stayed as it was)*. Accept or reject those changes, or switch Track Changes on, and apply again.

Apply all works through the cards a few at a time, so Trados Studio stays responsive while it runs. The button reads **Stop (12/80)** meanwhile: click it to stop after the segment in hand. It also stops if you switch documents, clear the report or start a new proofreading run. When it finishes, the footer says how many fixes were applied and how many were not; the cards of those not applied stay, each with its reason.

Apply writes to the open document like an edit of your own: save the document to keep the changes.

### Saving the report (from v18.20.187)

Every completed proofreading run is written to disk automatically, as a Markdown file in `trados\reports` inside your Supervertaler data folder – one section per segment with the issue, suggestion, evidence, source and target, and from v18/19.20.200 the correction. The footer of the Reports tab names the file (hover it for the full path), and the Batch Operations log shows the path too. So a report that has been cleared, or lost when Studio refreshes the panel, is never gone.

To keep a copy somewhere else – a client folder, an email attachment – click **Save report…** next to **Clear**. It writes the same Markdown to a location of your choice, and it is only enabled while a proofreading report is showing.

### The report stays until you are finished (from v18.20.187)

The report also stays in the Reports tab until you clear it. Close Studio and reopen the document, or switch to another document and back, and the report is put back as you left it: the issues you had ticked off or applied stay that way, a correction you have not applied can still be applied, and clicking a card still takes you to the segment. A report is only ever restored for the document it was made on. Press **Clear** when you are done with it.

### Clearing Results

Click the **Clear** button at the top of the Reports tab to remove all results and start fresh. The automatic copy on disk is unaffected.

### Run Summary

After a proofreading run, the Reports tab shows:

* Total number of issues found and segments checked
* Run timestamp and duration in the footer, followed by *translation only* when the run [checked the translation alone](#checking-the-translation-only-from-v181920201)

## Adding Issues as Trados Comments (from v18/19.20.201)

Tick **Also add issues as Trados comments** on the Batch Operations tab before you start the run. It is shown in Proofread mode, and not in Clipboard Mode. When the run ends, each issue is added to its segment as a Trados comment, with its suggestion, so you – or a reviser you send the file to – can read the issues in the editor and in Studio's Comments window, without the Reports tab:

```
AI proofreader (Claude Opus 5.5): "nadat" (after) contradicts the source "before opening any panel".
Suggestion: Replace "nadat" with "voordat".
```

* **The correction is not in the comment.** The comment says what is wrong and what to do about it; the corrected translation is what [Apply](#applying-fixes-from-v181920200) writes into the segment.
* **The label names the model** that found the issue, so the comment cannot be taken for a colleague's. To leave the label out, untick **Start Proofread comments with "AI proofreader (model):"** in [AI Settings](/trados/settings/ai-settings/).
* **Apply follows the same box.** With it ticked, **Apply** and **Apply all** also add the issue as a comment when they write the fix. With Track Changes on, a reviser then sees each tracked change with its reason beside it, and accepts or rejects it. This also works for a report you ran without the box: tick it before you apply.
* **One comment per segment.** A segment that already has a comment from the proofreader is left alone. So running the check again – which words the same issue differently every time – or applying a fix the run already commented on does not add a second. A different issue found on that segment later is shown on the Reports tab only. With the label switched off, Supervertaler cannot tell its own comments from a colleague's, so only an identical comment is left out.
* **The segment's status is not changed** by a comment. A fix you apply still sets it to Draft.
* **Comments go in a few at a time**, so Trados Studio stays responsive. Trados Studio takes up to a fifth of a second over each, so a few hundred issues can take a minute: the Reports tab footer shows how far it has got, and unticking the box stops it. Switching documents, clearing the report or starting a new run stops it too. When it finishes, the Batch Operations log says how many were added and names any segment that could not take one.

Comments are part of the document's unsaved changes: save the document to keep them. They travel with the bilingual file, so delete any you do not want a client to see before you deliver.

Until v18/19.20.200 the box was there but did nothing.

## AI Context in Proofreading

Batch Proofread builds a richer context than Batch Translate – it has to, because verifying whether a term is rendered consistently across the document is exactly the kind of question the AI needs the whole document to answer.

* **Full bilingual document context** – when **Include document context** is enabled in [AI Settings](/trados/settings/ai-settings/), every segment in the document is included with both source AND target text, with no truncation. This is what makes target-side consistency verifiable: the AI can check "this term is rendered as X in [SEGMENT 0031] and Y in [SEGMENT 0084]" against the actual document, not against a guess. Segment numbers in the document context match the `[SEGMENT XXXX]` numbers the AI sees in the batch it's reviewing, so citations cross-reference both ways. In a document made of several files, each request holds the segments of one file only and says which, so a number in the request names exactly one segment *(from v18/19.20.201)*. With [Translation only](#checking-the-translation-only-from-v181920201) ticked, the document context is the translation alone, without the segments not yet translated.
* **Termbase terms** – terminology from enabled termbases is checked against the translations, including term definitions and domains when that option is enabled. Forbidden terms are flagged with a `⚠️ DO NOT USE` marker so the AI knows to flag them as issues if it sees them in the translation. No termbase is sent with [Translation only](#checking-the-translation-only-from-v181920201) ticked.
* **Language-specific checks** – Dutch, German, and French targets get auto-included quality checks (compound spelling, dt-errors, de/het articles for Dutch; capitalisation and case system for German; accents and punctuation spacing for French). These come from the hardcoded base and don't need to be in your custom prompt.
* **Formatting tags** *(from v18/19.20.200)* – each segment in the batch is shown with its inline tags as numbered placeholders (`<t1>…</t1>`, `<t2/>`), as Batch Translate shows them, and a tag in the target carries the number of the source tag it stands for. The proofreader is told that tags are formatting, not words, and to report one only when it is missing or wraps the wrong words. Until v18/19.20.199 the batch was plain text, although the document context already showed the tags.
* **Custom prompts** – the selected proofreading prompt provides domain-specific quality checks on top of all of the above.
* **SuperMemory** *(from v18/19.20.200)* – when **Include SuperMemory knowledge base in AI context** is on in [AI Settings](/trados/settings/ai-settings/#supermemory-context), the active [memory bank](/trados/ai-assistant/super-memory/) and `_shared` are sent too, exactly as for a translation of the same document. The proofreader treats them as the client's instructions: a translation that departs from a term decision, style rule or client preference recorded in the bank is reported as an issue, even where it would otherwise pass as a matter of style, and the **Issue:** line names the rule it breaks. A point the bank says nothing about is never flagged on its account. Notes marked `audience: assistant` stay out, and a large bank is narrowed to what the document needs, using the same selection as a translation of the document ([how](/trados/ai-assistant/super-memory/ai-integration/#a-large-bank-sends-only-what-each-document-needs)). The Batch Operations log says what was sent, and **Preview prompt** shows it. Clipboard Mode sends no memory bank.

TM matches and surrounding segments are **not** included in proofreading – these are Chat & QuickLauncher features only. See the [AI Settings](/trados/settings/ai-settings/) page for a full comparison table.

:::caution
**Token cost:** Sending the full bilingual document roughly doubles the context size compared to source-only. For typical patent / legal / technical jobs (under ~500 segments) this is a minor cost increase – usually a few extra cents per batch on Sonnet-class models. For very long documents the cost scales linearly; if you proofread a 5,000-segment book you may want to disable Include document context and rely on per-batch context only.
:::

## Clipboard Mode

If you prefer to use a web-based AI (ChatGPT, Claude, Gemini, etc.) instead of an API, tick the **Clipboard Mode** checkbox. Supervertaler builds a complete proofreading prompt with both source and target text for each segment – or the target alone, with [Translation only](#checking-the-translation-only-from-v181920201) ticked – and copies it to your clipboard. See [Clipboard Mode](/trados/clipboard-mode/) for full details.

## Tips

### Start with Confirmed Segments

Use the **Confirmed Only** scope to check segments you consider finished. This avoids noise from segments that are still being worked on.

### Check Against the Client's Instructions

With SuperMemory on and the client's memory bank active, a Proofread run checks the translation against what you have recorded for that client. Use it to check segments that came from 100% matches against the client's current terminology and style, or as a final check after post-editing: departures from the bank come back as issues that name the rule. There is no need to copy the bank's rules into a proofreading prompt.

### Use Domain-Specific Proofreading Prompts

Create custom proofreading prompts tailored to your domain. For example, a medical proofreading prompt can check for correct use of clinical terminology, while a legal proofreading prompt can verify that defined terms are used consistently.

### Review After AI Translation

The AI Proofreader pairs well with [Batch Translate](/trados/batch-translate/). After translating a batch of segments with AI, run the proofreader to catch any issues before final review.

### Combine with Display Filters

Use Trados display filters to isolate specific segments (e.g., segments containing a certain term), then proofread only those filtered segments for targeted quality checks.

---

## See Also

* [Clipboard Mode](/trados/clipboard-mode/)
* [Batch Translate](/trados/batch-translate/)
* [Prompts](/trados/settings/prompts/)
* [Supervertaler](/trados/ai-assistant/)
* [Keyboard Shortcuts](/trados/keyboard-shortcuts/)

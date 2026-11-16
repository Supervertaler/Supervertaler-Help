---
title: "Batch Translate"
---

Batch Translate lets you translate multiple segments at once using AI. It is located in the **Supervertaler Assistant** panel, on the **Batch Operations** tab.

:::note
The Batch Operations tab also supports **Proofread** mode for AI-powered quality checking. See [AI Proofreader](/trados/ai-proofreader/) for details.
:::

<figure><img src="/.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### Starting a Batch Translation

1. Open the **Supervertaler Assistant** panel (View > Supervertaler Assistant)
2. Switch to the **Batch Translate** tab
3. Choose a **scope** from the dropdown
4. Choose a **prompt** from the prompt selector
5. Click **Translate**

### Scope

The scope dropdown controls which segments are translated:

| Scope                        | Description                                                            |
| ---------------------------- | ---------------------------------------------------------------------- |
| **Empty Segments Only**      | Translates segments that have no target text                           |
| **All Segments**             | Translates every segment in the file                                   |
| **All unfinished segments**  | Translates every segment that isn't Translated, Approved or Signed off – drafts and rejected segments included |
| **Filtered Segments**        | Translates only the segments currently visible after applying a filter |
| **Filtered Empty Only**      | Translates empty segments within the current filter                    |

:::note
**Locked segments are never sent to the AI**, in any scope – batch translation and batch proofreading both skip them, and the segment counters above the Translate button exclude them. *(From v18.20.154; earlier versions incorrectly included locked segments in batch runs.)*
:::

### Repetitions get one translation (from v18/19.20.201)

The AI translates every segment on its own, so a sentence that occurs twice in a run could come back worded two ways – *the cover is fitted* in one place, *the cover is mounted* in another. Batch Translate now gives every occurrence of a sentence the same translation:

* **Every later occurrence gets the translation of the first one**, across all the files in the run – open several files together to cover them all. The tags go in the same places, using each segment's own tags, and a `[[TC: …]]` note goes with the translation. If the AI left the first occurrence empty, the first one it did translate counts, and the empty one is filled from it.
* **A segment the run does not overwrite keeps its translation**, and that translation is the one its empty repetitions get. With **Empty Segments Only**, for example, a segment Trados filled from your translation memory, or one you translated yourself, decides how its empty repetitions are translated. Locked segments are never changed.
* **If such segments already disagree with each other, nothing is changed.** The log lists them under *Different existing translations*, naming the segments, so you can decide which is right.
* **A repetition the AI left empty is filled** from its first occurrence, without waiting for **Retry segments left empty**.
* **Nothing sent to the AI changes.** Every segment is still translated, in the same batches and with the same context, so a run costs what it did before. Only what is written for a later repetition is different.

**What counts as a repetition:** the same source text exactly – the same capitals, the same spaces and the same tags in the same order; only the tag numbers may differ. A non-breaking space is not an ordinary one, so *5 %* written with each is two different sentences. Near-matches are not repetitions. Segments that are similar but not the same – a passage repeated inside a longer sentence, or a sentence that differs in a word or a number – are handled by [short-term memory](#short-term-memory-repeated-passages-across-batches-from-v181920207) *(from v18/19.20.207)*.

**What you see:** the log ends with a line such as *Repetitions: 586 segments – 130 repetitions aligned to their first occurrence (12 worded differently by the AI, 2 in place of a failed translation)*. The [backup TMX](#backup-tmx) keeps the AI's own wording of each repetition it replaced.

It is on by default. To switch it off, untick **Keep repetitions consistent in Batch Translate** in [AI Settings](/trados/settings/ai-settings/#keep-repetitions-consistent-in-batch-translate-from-v181920201): every segment then keeps the AI's own translation, as before. Translate active segment (Alt+T) and Batch Proofread are not affected.

### Short-term memory: repeated passages across batches (from v18/19.20.207)

A long document often says the same thing twice in slightly different places: a clause that comes back in a later article of a contract, a warning repeated in every chapter of a manual, two rows of a table that differ in one number. Batch Translate sends the document to the AI in batches, and the AI does not remember an earlier batch. So the same passage could come out in two different wordings, one per batch.

Short-term memory closes that gap. Think of it as a translation memory for the run itself: a temporary one, which the AI uses during the batch translation and which is gone when the run ends. In CAT-tool terms it works at **sub-segment** level: it matches a passage inside a longer segment, where a translation memory matches whole segments.

**How it works**

* While a run is going, Supervertaler keeps the segments it has translated so far.
* When a segment in a later batch repeats a passage of **eight words or more** from one of them, that earlier segment and its translation are sent along with the request, the way a translation memory match is. The AI is told to word the repeated passage the same way.
* Two segments that are **almost the same** (at least four in five words shared) are shown whole, like a fuzzy match, with the words in which they differ pointed out. The AI is told to take every number from its own segment and never from the earlier one.
* A phrase that turns up all over the document (in more than six segments) is treated as boilerplate and is not sent.
* A request carries at most 20 earlier translations.

There is nothing to switch on, and nothing is stored after the run. It works in **Batch Translate** only, for any kind of document.

**What you see**

At the end of a run the log says how many segments were shown an earlier translation, and lists any repeated passages that were still translated differently, by segment number:

```
Repeated passages: 17 segments were shown an earlier translation of a passage they repeat.
Repeated passages: 2 translated differently (listed).
Repeated passages: Translated differently: segment 71 and segment 96 – source “lamphouder voor het bevestigen van een lamp aan …” (64 words the same)
```

Nothing is changed for you: the list is there so you can look at those segments yourself.

**What it does and does not do**

* On a 105-segment test document, translated by Claude Opus 5.5 in batches of 10, the repeated passages that came out the same went from 12 of 22 without short-term memory to 20 of 22 with it, with every number correct.
* It keeps **passages** consistent, not single **terms**. If one word can be translated two ways, the AI may still pick one in one batch and the other in the next. A [termbase](/trados/termlens/) entry is the way to fix a term.
* Identical segments are a separate matter and are handled by [Repetitions get one translation](#repetitions-get-one-translation-from-v181920201) above.
* A **larger batch size** helps as well, because segments in the same request see each other. Use the **Batch size** box on the Batch Operations tab, as far as your Trados Studio and your AI model allow; Trados Studio 2024 and 2022 take at most 10. Short-term memory is what keeps a document consistent when it does not fit in one request.
* The earlier translations are extra text in the request, so a run with many repeated passages costs a little more. In the test above it was about 6,600 tokens over the whole run.

### Prompt Selection

Choose a prompt to guide the AI translation style and domain. The prompt selector shows, from the top:

* **(Built-in instructions only)** – no prompt from your library: Supervertaler's own translation instructions alone (inline tags, numbers, the output contract), with your termbase, translation memory matches and memory bank as set in AI Settings.
* **Default Translation Prompt** – a general-purpose prompt that works well for most content types. Use it as-is or duplicate it in the Prompt Manager and customise it for your domain. *From v18/19.20.200 this is what Batch Translate and Alt+T use until you choose another prompt;* before that, they started on the built-in instructions alone.
* **Custom prompts** – your own prompts created in the Prompt Manager

Choosing **(Built-in instructions only)**, or turning off the active prompt in the Prompt Manager, is remembered as your choice. Hover over the prompt selector for a summary of what each kind of item means.

The **active prompt** for the current project is marked with a checkmark in the dropdown. When you open a project that has an active prompt set, it is automatically selected. See [Memory banks – Active Prompt](/trados/ai-assistant/super-memory/active-prompt/) for how to set the active prompt.

:::tip
**Tip:** If you save a prompt with the same name as your Trados project, the dropdown will auto-select it whenever you open that project. For example, a prompt called "PROJ-001" will be auto-selected when working in a project called PROJ-001.
:::

:::note
For specialised fields (medical, legal, patent, etc.), create a custom prompt with domain-specific terminology rules and instructions. A tailored prompt is the single most effective way to improve translation quality.
:::

### Provider and Model

The current AI provider and model are displayed below the prompt selector. Click the provider/model label to open a flyout menu where you can switch models instantly – the same menu available in the Chat tab. Alternatively, open the settings dialogue (gear icon in the TermLens header) and go to the **AI Settings** tab.

Your **custom OpenAI-compatible profiles** (institutional gateways, self-hosted endpoints) appear at the bottom of the same menu under *Custom (OpenAI-compatible)*, each showing its configured model, with the active profile ticked – so switching between custom endpoints is one click, no trip to Settings. *(From v18.20.154.)*

### Progress and Logging

During translation:

* A **progress bar** shows overall completion
* A **real-time log** displays the status of each segment as it is translated
* The **Stop** button aborts the batch at any time – segments already translated are kept

You can switch to another document while a run is going. From v18/19.20.201 the run writes only into the document it was started in; before, it wrote each translation into whichever document was active at that moment.

#### The progress window, and which pane is in front (from v18/19.20.208)

While a run writes its translations, Trados Studio brings its own **Translation Results** pane to the front. Studio does this by design and has no setting to switch it off. If the Supervertaler Assistant pane shares a window group with Translation Results – the two are tabs in the same part of the screen – the Assistant pane therefore goes behind it during a run.

* **Supervertaler leaves it alone during the run.** Before v18/19.20.208 it pulled its own pane back after every batch, so the two panes kept trading places for the whole run.
* **The Supervertaler Assistant pane comes back once**, when the run has finished. The Batch Operations log keeps updating throughout.
* **A run has a small progress window of its own**, titled **Supervertaler – Batch Translate**, at the bottom right of Studio's window. It shows the batch being translated and a progress bar, so you can follow the run while the pane is behind Translation Results.
* **Its Stop button** does the same as **Stop** on the Batch Operations tab: the run stops at once. The batch being translated at that moment is dropped, and the segments already written to the document are kept.
* **The window closes by itself** when the run ends.
* **The project is saved once**, at the end of the run.

:::tip
To avoid the switching altogether, drag the Supervertaler Assistant pane into a different window group from Translation Results – beside it or below it, say, instead of as a tab next to it. Both panes then stay in view during a run, and Studio remembers the layout.
:::

### Translate Active Segment (Alt+T)

Press **Alt+T** to translate the active segment instantly. This uses the same provider, model, and prompt as Batch Translate, so you can switch prompts or providers and immediately use them for single segments with Alt+T.

Alt+T is also available via right-click in the editor ("Translate active segment").

:::caution[Alt+T does nothing?]
Trados also puts one of its own commands on `Alt+T` (**Toggle between Source and Target in Translation Results View**), and the Trados binding wins. Clear it once in **File → Options → Keyboard Shortcuts** and `Alt+T` works. See [Keyboard shortcuts](/trados/keyboard-shortcuts/#first-time-setup-free-up-trados-shortcuts).
:::

:::note
Older installs may still have this on `Ctrl+T` – the default moved to `Alt+T` in v18/19.20.119 because `Ctrl+T` collides with a Trados factory shortcut. See [Keyboard shortcuts](/trados/keyboard-shortcuts/) for how to reassign it.
:::

#### How it works

1. The active segment's source text is sent to the AI provider configured in AI Settings
2. The selected prompt (from the Batch Translate tab) is applied, along with termbase terms
3. The same document context and SuperMemory context as a batch run is included *(from v18/19.20.149 – earlier versions sent the segment on its own, which is why single segments used to translate noticeably worse than a batch)*
4. The translation is written directly into the target cell
5. Inline tags (bold, italic, field codes, etc.) are preserved in the translation

In short: a single segment now gets everything a batch run gets, minus the other segments – same prompt, same terminology, same document context. On versions before 18/19.20.149, batch translating even small ranges gave better results than going segment by segment; from 18/19.20.149 the two are equivalent.

#### What changed for Alt+T in v18/19.20.208

* **The Supervertaler Assistant pane stays where it is.** Before, when the Assistant pane shared a window group with Translation Results, every Alt+T pulled the Assistant pane in front of Translation Results when the translation arrived. Now it does not.
* **The document is not saved after each Alt+T.** Studio's own AutoSave takes care of saving. Before, Supervertaler saved the whole document after every single segment, which could make Studio pause briefly on a large document. A Batch Translate run still saves the project once, at the end.
* **It sends the same context whether or not the Supervertaler Assistant pane has been opened.** Before, if the pane had not been set up in the session, Alt+T sent the document, the termbase and a prompt, but never the memory bank, also with **Include SuperMemory knowledge base in AI context** ticked. It now always sends the memory bank of the open project with `_shared` and the files for the target language, the prompt chosen for the project, and the list numbers in the document context. Studio normally sets the pane up shortly after it starts, without showing it, so most sessions never met the difference.
* **Without the pane there is no Batch Translate log.** What was sent from the memory bank is then written to `trados\runtime\bridge.log` in your [data folder](/trados/data-folder/). A memory bank that cannot be read never stops the translation.
* **Its requests have their own name.** On the [Reports](/trados/reports/) tab an Alt+T request is headed **Translate active segment**, and the [usage log](/trados/usage-costs/) and its export list it under the task `Translate`, so you can see what Alt+T costs apart from your Batch Translate runs. Before, both counted it as Batch Translate.

**Cost when you go segment by segment** *(from v18/19.20.198)*. Everything that is the same for every segment – the instructions, the SuperMemory context and the document content – is sent identically each time, and only the segment and its own termbase terms change. Providers that cache prompts therefore store that shared part on the first segment and read it back on the next ones: on Claude, from the second segment on, it costs a tenth of its normal price or less, as long as each segment follows the last within an hour *(from v18/19.20.208; within five minutes before)*. On a typical job that makes every segment after the first many times cheaper than the first. Before 20.198 the segment's terms sat in the middle of the shared part, so it was never reused. See [Prompt caching](/trados/ai-cost-guide/#prompt-caching).

**What the Batch Translate log shows for Alt+T** *(from v18/19.20.198)*. How many of your AI-enabled termbase terms occur in the segment and go with it, and a warning when terms are loaded but no termbase has its **AI** column ticked in Settings → Termbases – in that case no terms are sent at all. A request that fails is reported there and, if you log AI calls to the [Reports](/trados/reports/) tab, recorded there too.

### AI Context in Batch Translate

Batch Translate uses several context sources from your [AI Settings](/trados/settings/ai-settings/) to improve translation quality:

* **Document content** – when **Include full document content in AI context** is ticked on the [Batch Operations tab](/trados/batch-operations/#include-full-document-content-in-ai-context-from-v181920208) *(from v18/19.20.208; before, this was a tick box in AI Settings)*, all source segments are included in the system prompt so the AI can determine the document type (legal, medical, technical, etc.) and adapt its style accordingly. This is shared across all batches.
* **Termbase terms** – terminology from enabled termbases is injected into the prompt, including term definitions and domains when that option is enabled.
* **Custom prompts** – the selected prompt provides domain-specific translation instructions.
* **SuperMemory** – when enabled, the active memory bank and `_shared`. From v18/19.20.208, `_shared` is also sent when the project has no bank of its own. From v18/19.20.198 a large bank is narrowed to the part the document needs, the first time you translate it, and the log says what was sent and names a file listing what was left out. See [SuperMemory – AI Integration](/trados/ai-assistant/super-memory/ai-integration/#a-large-bank-sends-only-what-each-document-needs).
* **Translation memory matches** – Batch Translate searches the project's translation memories for each segment and sends the closest match, together with the source sentence it was made for, so the AI can see which words differ instead of assuming the wording fits. From v18/19.20.198 a match is offered as a reference to check, not as wording to follow: a memory can hold translations made for other documents, products or clients, and they can be wrong, even at 100%. The AI reuses a match only where it is correct for the segment, lets the termbase and the document take precedence, and translates from the source when in doubt. Matches at or above **Lowest TM match to send** in [AI Settings](/trados/settings/ai-settings/#lowest-tm-match-to-send) are sent, 70% by default. This works on empty segments too, not only ones Trados has pre-translated. **Send TM matches to the AI** on the Batch Operations tab turns it off for a job whose memory you do not trust, and **👁 Preview prompt** shows the matches – it shows the whole prompt exactly as it is sent, with its line breaks. *(From v18/19.20.190; in [Clipboard Mode](/trados/clipboard-mode/#translation-memory-matches) from v18/19.20.198.)* From v18/19.20.206, the matches also come from [EverTM](/trados/evertm/#ai-batch-translate), when it is in the project's TMs with **Lookup** ticked. A project TM's match of the same score wins. From v18/19.20.208 only memories that are switched on in the project are searched; see [Which translation memories are searched](#which-translation-memories-are-searched-from-v181920208) below.
* **Same sentence, different numbers** *(from v18/19.20.206)* – a match is called 100% only when the sentence stored in the memory is identical to your segment. Studio also scores a sentence as 100% when it differs only in its numbers – "claim 3" in the memory, "claim 7" in your segment – because it replaces the numbers itself. Such a match is now labelled **same sentence, different numbers** instead of 100%. Your segment's text is shown above the memory's, so the AI can compare them, and the AI is told to use your segment's numbers. Supervertaler does not change any number in the memory's translation itself; where [EverTM](/trados/evertm/#when-only-a-number-differs) has already put your segment's number into its translation, the match says so. An identical sentence in another TM wins over one with other numbers. With **Lowest TM match to send** at 100, these matches are not sent. The same goes for Translate active segment (Alt+T), and **👁 Preview prompt** shows it all.

Surrounding segments are **not** included in Batch Translate – that is a Chat & QuickLauncher feature. See the [AI Settings](/trados/settings/ai-settings/) page for a full comparison table.

#### Which translation memories are searched (from v18/19.20.208)

With **Send TM matches to the AI** ticked, Batch Translate searches a translation memory only when it is switched on for the project. In **Project Settings → Language Pairs → Translation Memory and Automated Translation**, both its **Enabled** box and its **Lookup** box must be ticked. That is the rule Trados Studio itself applies. Before v18/19.20.208, Batch Translate searched every memory named in the project, also one whose **Enabled** or **Lookup** box you had unticked.

* **Which list counts.** The language pair's own list, when **Use different translation providers for this language pair** is ticked for that pair; otherwise the list under **All Language Pairs**.
* **[EverTM](/trados/evertm/#ai-batch-translate)** in the project's list follows the same rule.
* **The log says so, once per run, when memories were left out.** For example: `TM matches: 1 of 2 project TMs searched; 1 is switched off or has Lookup unticked in Project Settings.` Machine translation providers in the list are not counted as TMs.
* **A `.sdltm` file in the project's `Tm` folder that is not in the project's list is no longer searched.** Before v18/19.20.208 it was.
* **Clipboard Mode and Preview prompt use the same rule**: **Copy to Clipboard** and **👁 Preview prompt** show matches from the same memories a run would search.
* **Not changed:** the **TMs** button in [SuperSearch](/trados/supersearch/), and the [MCP tools](/trados/mcp-server/) `search_studio_tm`, `compare_document_to_tm` and `list_resources`, still offer every memory attached to the project, because there you choose what to search.

### What the AI may send back

*(From v18/19.20.198.)* Every translation request ends with a fixed **output contract**, whichever prompt is selected: the reply is the translation and nothing else – no preamble, no notes, no explanations, no alternatives, no markdown, every tag kept. A prompt can add to it but cannot switch it off by accident, because it comes last, after the prompt, the terminology, SuperMemory and the document. **Preview prompt** shows it at the end of the system prompt. Supervertaler for memoQ sends the same contract, so a prompt written for one product reads correctly in the other.

Every reply is checked against it before anything is written. A reply that carries more than the translation – a note after it, the model explaining its own choices, a remark about the translation memory, markdown or a line break the source does not have, a second `[[TC: …]]` marker – is asked for once more, with the contract restated. If the second answer does the same, **nothing is written**: the segment is left empty, and the Batch Translate log names it and gives the reason. **Retry segments left empty** does not send it a third time. An empty segment costs you one segment to translate yourself; a note in the target could reach your client. The same check applies to Translate active segment (Alt+T).

The check looks for signs of commentary that the source itself does not have, so a source that really does contain a label such as "Note:" or markdown is translated as usual. Text written in the first person passes too: *Ik verklaar dat ik dit document heb vertaald* can become *I declare that I have translated this document*, because the source has its own word for "I" and the translation adds no sentence to it. One case can still be refused wrongly: a source that leaves the pronoun out, as Spanish and Italian can (*He traducido…*, *Ho tradotto…*), translated into English. If the log gives *the model writing about its own choices* for a segment like that, translate it by hand.

#### Translator comments

Where a note is genuinely needed – a defect in the source, a real ambiguity, an error the AI corrected in a 100% translation memory match, a deliberate departure from the termbase – the contract gives the AI one place for it: a single `[[TC: …]]` marker at the very end of that segment's translation, 5 to 20 words, written as your comment to the client, in English unless your prompt says otherwise. For example: `[[TC: "100 000 miljoen euro" means EUR 100 billion. Please check.]]`

Where it ends up is your choice, in **Settings → AI Settings → Add the AI's [[TC: …]] notes as Trados comments**:

* **Unticked (the default):** the marker stays at the end of the target, where you see it while you review. Decide whether it is worth keeping, add it as a Trados comment on the words it is about, and delete it from the target before you confirm the segment. Search the target for `[[TC:` to find them all.
* **Ticked:** the marker is taken out of the target and added to the segment as a Trados comment. If Studio refuses the comment, the marker is written at the end of the target instead, so no flag is lost.

This applies to Batch Translate, Translate active segment (Alt+T) and [Paste from Clipboard](/trados/clipboard-mode/#what-is-checked-when-you-paste).

The **Default Translation Prompt** used to tell the AI it could "add a brief explanation in parentheses" when a term had no established equivalent, which a model can take as licence to explain itself in the target. From 20.198 it asks for a `[[TC: …]]` marker instead. Your copy is updated automatically unless you have edited it; an edited copy is left alone.

### Backup TMX

The **Auto-backup translations to TMX** checkbox is ticked by default. When enabled, Supervertaler writes every translated segment to a TMX file as it arrives from the AI. If Trados crashes mid-run, you can recover the completed translations without re-running the batch.

The TMX files are also useful outside of crash recovery – you can import them into any TM in Trados, memoQ, Wordfast, or any other CAT tool that accepts standard TMX.

Click **Open folder…** next to the checkbox to open the backup folder directly in Windows Explorer.

To disable backups for a particular run, simply untick the checkbox before clicking Translate.

#### How it works

* A new `.tmx` file is created at the start of each batch run.
* Every **10 translated segments**, the file is rewritten in full – so at most 10 segments are lost in a crash.
* The file is written atomically (via a temp file + rename) so it is always a valid, complete TMX – never a partial or corrupt file.
* At the end of a completed or cancelled run, the file is flushed one final time.
* A [repetition](#repetitions-get-one-translation-from-v181920201) is backed up with the translation it was given. Where the AI had worded it differently, the entry carries a note with the AI's own version: *Repetition: written with its first occurrence's translation. The AI's own: …* *(From v18/19.20.201.)*

#### Where the files are saved

```
C:\Users\<YourName>\Supervertaler\trados\batch_backups\
```

Files are named by timestamp and project name, for example:

```
batch_2026-04-10_14-23-01_PROJ-001.tmx
```

The exact path is also printed to the **Batch Translate log** at the start of each run.

#### Recovering after a crash

1. Reopen Trados Studio and your project.
2. Open your TM in **Trados Translation Memories** (or via the project's TM settings).
3. Use **Import** → browse to the backup `.tmx` file → import.
4. Run **Pre-translate** on your project to apply the recovered translations from the TM.

:::note
Backup files are **not deleted automatically**. Tidy up the `batch_backups` folder occasionally if disk space is a concern, or keep them as a translation archive.
:::

### Clipboard Mode

If you prefer to use a web-based AI (ChatGPT, Claude, Gemini, etc.) instead of an API, tick the **Clipboard Mode** checkbox. This replaces the Provider and Translate button with **Copy to Clipboard** and **Paste from Clipboard** buttons. Supervertaler builds a complete, ready-to-use prompt – including your selected prompt, terminology, document context, and numbered bilingual segments – and copies it to your clipboard. See [Clipboard Mode](/trados/clipboard-mode/) for full details.

### Tips

#### Translate Empty Segments First

Start by translating only the empty segments (scope: **Empty Segments Only**). Review the results, then fix any issues. This avoids overwriting segments you have already edited.

#### Generate a Domain-Specific Prompt Automatically

Click **AutoPrompt…** next to the prompt dropdown. Supervertaler analyses your entire document, detects the domain, and uses AI to generate a comprehensive translation prompt with terminology rules, style guidelines, and anti-truncation controls – all tailored to your specific project. See [AutoPrompt](/trados/generate-prompt/) for details.

#### Create Domain-Specific Prompts Manually

For specialised content, you can also duplicate the Default Translation Prompt in the Prompt Manager and add domain-specific instructions (terminology rules, style preferences, formatting requirements). A tailored prompt is the single most effective way to improve translation quality.

#### Combine with TM

If your project has a translation memory, TM matches are shown alongside AI translations. You can pre-translate with TM first (using Trados's built-in batch tasks), then use Batch Translate to fill in the remaining empty segments with AI.

#### Review After Batch

AI translation is a first draft. After a batch run:

1. Review each translated segment
2. Fix any terminology or style issues
3. Confirm segments with **Ctrl+Enter** (Trados default)

***

### See Also

* [Clipboard Mode](/trados/clipboard-mode/)
* [AutoPrompt](/trados/generate-prompt/)
* [AI Proofreader](/trados/ai-proofreader/)
* [Supervertaler](/trados/ai-assistant/)
* [TermLens](/trados/termlens/)
* [SuperMemory](/trados/ai-assistant/super-memory/)
* [Keyboard Shortcuts](/trados/keyboard-shortcuts/)

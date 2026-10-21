---
title: "Add segments to SuperMemory"
description: "Use the part of a document you have reviewed as the reference for the rest"
---

Some documents have a part that settles the wording of everything after it: the definitions of a contract, the claims of a patent, the interface strings of a manual. Translate and review that part first, then copy it into a memory bank. From then on, Batch Translate and Translate active segment (Alt+T) follow its approved wording for the rest of the job.

*New in v18/19.20.201.*

## How to use

1. Translate and review the part you want to use. Confirm the segments as you go: only confirmed segments are taken, unless you say otherwise.
2. In the editor, select those rows – click the first row's number, then Shift+click the last – and right-click: **Add segments to SuperMemory**. Without a selection, the range starts at the active segment, and you type the numbers you want.
3. In the dialogue:
   * **Save to memory bank** – the active bank is preselected. A translation reads only the active bank (and `_shared`), so the dialogue tells you when you pick another one.
   * **From** and **To** – the segment numbers Trados Studio shows. In a document made of several files, where each file is numbered from 1, choose the file as well. A range can run from one file into the next.
   * **Only confirmed segments** – leaves out Draft and Not Translated segments, so nothing unreviewed is passed on as approved wording. A segment without a translation is always left out.
   * **What will be written** – exactly the text that will go into the bank.
4. Click **Add**.

The next translation from that bank carries the segments, and so does every one after it.

## What gets written

The segments go into the bank's `brief.md`, under a **## Reference translations** heading, each with its number, its source and its translation:

```markdown
## Reference translations

Reviewed translations from this job (segments 1–12 of PROJ-001 agreement.docx), added with Add segments to SuperMemory on 2026-10-21. They are approved wording: where the text you translate repeats or refers to one of these passages, follow its translation and terminology. Adding segments to this bank again replaces this section.

### PROJ-001 agreement.docx

**1**
- Dutch (NL): In deze overeenkomst wordt verstaan onder "Diensten": de werkzaamheden die Acme voor de Klant verricht.
- English (GB): In this Agreement, "Services" means the work Acme performs for the Client.
```

The text comes without tags, with any tracked changes accepted. The file heading appears only in a document made of several files.

**Why `brief.md`.** It is the one bank file a translation always sends whole. A large bank is narrowed down for each document – `terminology.md` keeps only the rows whose term occurs in the document, and other files are put to a short AI check – and either would leave whole segments out (see [AI Integration](/trados/ai-assistant/super-memory/ai-integration/#a-large-bank-sends-only-what-each-document-needs)). The rest of your brief is left exactly as it was.

**Adding again replaces the section.** A bank holds one client's material, so a job's reference translations would otherwise go with that client's next job too. When the job is done, delete the section – **Settings → Library → SuperMemory →** your bank **→ brief.md → Edit** – or leave it to be replaced next time.

## What it costs

Everything in the section goes with every translation request from the bank. Before anything is written, the dialogue shows how many tokens that is and what the bank comes to afterwards.

* **Above 4,000 tokens it warns you.** For scale: 4,000 tokens on every request of a 400-segment document, translated in batches of 20, is 80,000 tokens. A provider that caches prompts charges less for it after the first request, since the section is the same on every request of a job.
* **It refuses a range that would take the bank's own files past 24,000 tokens**, the most a translation sends from a bank. Beyond that, parts of the bank would be cut from every prompt. `_shared` is not counted: it is narrowed down for each document, and it is the first thing cut.
* **It tells you when the bank passes 8,000 tokens**, the point from which translations narrow a bank down for each document. That costs one small AI request per document, the first time it is translated.

## Nothing is overwritten

* The rest of `brief.md` is kept byte for byte, line endings included.
* The previous version is saved in your data folder, under `backups\memory-banks\`, and the confirmation names the file.
* If `brief.md` was changed after the dialogue opened – in Obsidian, say, or by a colleague in a [team folder](/trados/data-folder/#sharing-memory-banks-and-prompts-with-a-team-folder) – nothing is written. The dialogue reads the file again, and you click **Add** again.
* When the team folder cannot be reached this session, the dialogue says so: the segments would go into your own copy of the bank, which the rest of your team does not see.
* Writing to `_shared` asks first, because `_shared` goes with every client's jobs.

## Related

* [**SuperMemory**](/trados/ai-assistant/super-memory/) – how a bank is structured
* [**Quick Add**](/trados/ai-assistant/super-memory/quick-add/) – one term decision at a time
* [**AI Integration**](/trados/ai-assistant/super-memory/ai-integration/) – what gets sent to the AI, and in what order

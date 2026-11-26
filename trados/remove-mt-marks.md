---
title: "Removing MT Marks"
---

Trados Studio remembers which segments were filled by machine translation. An unedited one shows **AT** next to it; one you edited afterwards shows a faded **AT**. For an AI engine, such as AI Bridge for Trados Studio, Studio shows **AI** instead, and a faded AI after editing. Your client sees the same marks in the files you deliver.

Once you have reworked a segment, the translation is yours. The batch task **Supervertaler - Remove MT marks** takes the marks out of the files, so those segments read like any you typed yourself.

:::note[Coming in v18/19.20.210]
Remove MT marks is not released yet: it comes with Supervertaler for Trados v18/19.20.210.
:::

Segments that Supervertaler writes itself (Batch Translate, Translate active segment, an AI assistant through the [MCP server](/trados/mcp-server/)) already read as your own edit, since version 18/19.20.201. This task is for machine translation from the engines in your project – DeepL, Language Weaver, Google, an AI engine and so on – and for files from before 201.

:::caution[Before you run it]
- **Check your agreement with the client.** Some clients require you to say when machine translation was used, and some pay for post-editing at a different rate. That is why this is a batch task you choose to run, never a setting.
- **It can't be undone.** Studio's batch tasks have no undo. Keep a copy of the project, or of the files, until your client has accepted the delivery.
:::

### Removing the marks

Do this when the translation is finished, just before you deliver.

1. **Save your work.** Documents open in the Editor can stay open: Studio closes them while the task runs and opens them again afterwards.
2. **Select the files.** In **Projects**, select the project to clean every file in it; or in **Files**, select the files you want.
3. **Run the task.** Right-click and choose **Batch Tasks → Supervertaler - Remove MT marks** (or **Home → Batch Tasks**), then click **Finish**.
4. **Check.** Open a document: no segment shows AT or AI any more. The task's report is in the **Reports** view.
5. **Deliver** as usual: create the return package, or send the files.

You can also add the task to a task sequence of your own, in front of **Finalize**. For a return package, run the task first, then click **Create Return Package** on the **Home** ribbon, or right-click the project in **Projects** and choose it there.

### What it removes, and what it leaves

It removes the machine translation record from every segment that has one, whichever engine it came from: classic, neural and adaptive machine translation, AI engines included.

- An unedited machine translation (**AT** or **AI**) becomes an ordinary edited segment.
- A segment edited after machine translation (the faded mark) loses the machine translation from its history. If the machine translation had replaced a TM match, that TM match stays in the history.

Everything else stays exactly as it was:

- the translation, its tags, comments and tracked changes;
- the segment's status (Draft, Translated, Approved and so on), so the confirmation statistics don't change;
- who created and last changed each segment, and when;
- TM matches, segments you typed yourself, and your translation memories.

**Locked segments** are left as they are, even with a machine translation mark: a lock usually means the segment isn't yours to change. The report counts them.

**A file with no machine translation marks** isn't opened at all, so it stays exactly as it was. That also means running the task a second time changes nothing.

### The report

For each file, the report says how many segments were cleaned (unedited, and edited after machine translation), how many locked ones were left, and which engines' records were removed. A file with nothing to remove says so.

### Large projects

Studio reads and writes each file once, as for any batch task that changes files. In our tests a 100,000-segment file took about a minute, almost all of it Studio reading and writing the file. A file without machine translation is checked in about a second and skipped.

### Compared with RWS's Trados Batch Anonymizer

The Batch Anonymizer also changes where a segment came from, but it leaves a *Before Interactive Editing* record that still shows which segments were machine translation. Remove MT marks leaves no such record.

### Questions

**Does it remove the AI mark too?** Yes. Studio stores an AI engine's translations as neural machine translation, with the engine's name, so they are removed like any AT.

**I ran it and a segment still shows AT or AI.** Is the segment locked? Locked segments are left as they are. Otherwise, check the task's report in the **Reports** view to see whether the file was finished.

**Can I undo it?** No. Go back to your copy of the project.

**Which Studio versions?** Trados Studio 2022, 2024 and 2026.

**I use memoQ.** Supervertaler for memoQ removes the marks from a Trados return package: see [Removing MT Marks (memoQ)](/memoq/remove-mt-marks/#trados-return-packages).

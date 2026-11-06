---
title: "Showing Your Changes as Tracked Changes"
---

Sometimes a client asks you to change a translation that is already in memoQ – a revised source, a new term, a round of review comments – and wants to *see* what you changed. Edits made in the grid don't show up that way, and neither do corrections that an [AI assistant](/memoq/mcp-server/) stages for Pre-translate.

There is a way round this in memoQ itself. Export the document as a bilingual file, make your changes in that file, and bring it back with **Update From Bilingual**. On the way in, memoQ can record the differences as tracked changes. Every changed row then shows its old and new text, just as in a reviewed document, and the client can accept or reject each change.

### Step by step

1. **Export.** In **Project home → Translations**, select the document and choose **Documents → Export → Export Bilingual**. Pick **Two-column RTF**, and save the file into a folder of your choice.
2. **Make your changes** in the target column of the exported file. Change only the text: leave the source column, the segment IDs and the tags as they are. You can do this in Word, or in [Supervertaler Workbench](/workbench/cat-tools/memoq/), which opens memoQ bilingual files and writes them back in the same format – with its AI translation, terminology and QA to hand.
3. **Update the document.** Back in memoQ, choose **Documents → Import → Update From Bilingual** and select the edited file. memoQ recognises which document it belongs to: the **Document import options** window lists it as **Table RTF** with the action **Update**.
4. **Turn on tracked changes.** At the bottom of that window, under **Table RTF update**, tick **Import edits as tracked changes**. Leave **Do not update if source segment is different** ticked, so a row whose source was changed in the file is skipped rather than overwritten. Click **OK**.
5. **Check.** Open the document: the rows you changed show your edits as tracked changes.

:::caution[Do the round trip in one go]
Anything you change in memoQ itself between the export and the update is overwritten by the file. Make all your changes in the exported file, then update.
:::

### Where it works

- **Local projects:** yes.
- **memoQ server (online) projects:** yes, in your local copy of the project, if the project manager allows it. Two project settings matter: whether users may check out the project (create a local copy), and whether they may export documents. Both are under the online project's **Settings → General → Project options** ([memoQ's help on these settings](https://docs.memoq.com/current/en/Workspace/memoq-online-project-s-general.html)). If **Export** or **Update From Bilingual** isn't available to you, ask the project manager.

### See also

- [Removing MT Marks](/memoq/remove-mt-marks/) – another job done with a bilingual export and import
- [memoQ workflow in Supervertaler Workbench](/workbench/cat-tools/memoq/)

---
title: "Showing Your Changes as Tracked Changes"
---

Sometimes a client asks you to change a translation that is already in memoQ – a revised source, a new term, a round of review comments – and wants to *see* what you changed. Edits made in the grid don't show up that way, and neither do corrections that an [AI assistant](/memoq/mcp-server/) stages for Pre-translate.

There is a way round this in memoQ itself. Export the document as a bilingual file, make your changes in that file, and import it back. On the way in, memoQ offers to record the differences as tracked changes. Every changed row then shows its old and new text, just as in a reviewed document, and the client can accept or reject each change.

### Step by step

1. **Export.** In **Project home → Translations**, select the document and choose **Documents → Export → Export Bilingual**. Pick <!-- TODO Michael: "Bilingual DOC/RTF" or "Two-column RTF"? --> **Two-column RTF**, and save the file into a folder of your choice.
2. **Make your changes** in the target column of the exported file. Change only the text: leave the source column, the segment IDs and the tags as they are. You can do this in Word, or in [Supervertaler Workbench](/workbench/cat-tools/memoq/), which opens memoQ bilingual files and writes them back in the same format – with its AI translation, terminology and QA to hand.
3. **Import.** Back in memoQ, choose **Documents → Import** and select the edited file. memoQ recognises it as an update of the existing document and asks <!-- TODO Michael: exact wording of memoQ's question, ideally with a screenshot --> whether to show the differences as tracked changes. Say yes.
4. **Check.** Open the document: the rows you changed show your edits as tracked changes.

:::caution[Do the round trip in one go]
Anything you change in memoQ itself between the export and the import is overwritten by the file. Make all your changes in the exported file, then import it.
:::

### Where it works

- **Local projects:** yes.
- **memoQ server (online) projects:** yes, as long as the project lets you import bilingual files. <!-- TODO Michael: did it need any special permission from the project manager? --> If memoQ refuses the import, ask the project manager to allow it.

### See also

- [Removing MT Marks](/memoq/remove-mt-marks/) – another job done with a bilingual export and import
- [memoQ workflow in Supervertaler Workbench](/workbench/cat-tools/memoq/)

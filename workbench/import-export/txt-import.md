---
title: "Importing Text Files"
---

Text import is the simplest workflow: **each line becomes one segment** – or, if you prefer, one segment per sentence.

## Import steps

1. Go to **Project → Import → Text / Markdown File (TXT, MD)…**
2. Select your `.txt` file
3. Choose the **source** and **target** languages
4. Optionally tick **Split lines into sentences** (see below)

## Splitting lines into sentences

With **Split lines into sentences** ticked, long lines are split into one segment per sentence. Each line of the file still stays a paragraph of its own, and on export the sentences of each line are joined back into one line, with the same spacing as in the original. Your choice is remembered for the next import.

Where lines are split is set in **Settings → 📏 Segmentation Rules**: extra abbreviations, rules that split at a delimiter such as `<>` or `|`, and more. See [Segmentation Rules](/workbench/settings/segmentation-rules/).

In Markdown files, links, code spans and URLs are protected while lines are split.

## Tips

- Keep one sentence (or one logical unit) per line for best results.
- If your file has encoding issues (weird characters), try saving it as UTF-8.

## Export

Text projects can be exported as:

- Translated TXT
- DOCX
- Bilingual table

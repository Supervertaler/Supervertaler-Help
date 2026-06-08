---
title: "Export Verification (Word-Count Check)"
---

Whenever you export a translated **DOCX**, Supervertaler runs an automatic safeguard that checks whether any text was lost on the way out of the document. It is a safety net against the rare case where the round-trip drops content that is present and confirmed in the grid.

## What it does

After writing the file, Supervertaler:

1. Counts the words it **expected** to write – the target text of every segment, falling back to the source text for any untranslated segment.
2. Counts the words **actually present** in the exported DOCX (document body, headers, footers, and foot/endnotes).
3. Compares the two. If the exported file contains noticeably fewer words than expected, it shows a warning.

Tags, numbers, and punctuation are counted the same way on both sides, so a genuine loss of text shows up as a clear shortfall while incidental formatting differences stay within tolerance.

## When it runs

- Automatically, on **every DOCX export** – single-file and multi-file, whether the file is built through the Okapi merge or the standard exporter.
- Multi-file projects produce a **single combined warning** listing each affected file, rather than one dialog per file.

## The warning

If a file falls short, you’ll see a **Possible Missing Text in Export** dialog naming the file(s) and roughly how many words appear to be missing. The same result is written to the log, for example:

```
🔢 Export word-count check [Manual.docx]: 4065/4060 words (100%; threshold 95%)
```

or, when text looks lost:

```
⚠️ Possible dropped text in export: Manual.docx has only 85% of the expected words — review before delivery.
```

When you see the warning, open the file and check it before delivering.

:::note
The check is deliberately **coarse**. It reliably catches a material loss (for example a whole paragraph or many segments going missing), but a single very short segment dropping out can stay within the tolerance band and won’t trigger a warning. It’s a backstop, not a substitute for a final read-through.
:::

## Adjusting or turning it off

The check is configured in your `settings.json` file, under an `"export"` section:

| Key | Default | Meaning |
| --- | --- | --- |
| `word_count_check_enabled` | `true` | Set to `false` to turn the check off entirely. |
| `word_count_check_threshold` | `0.95` | Warn when the exported file has fewer than this fraction of the expected words. Raise it (e.g. `0.99`) for more sensitivity, lower it to tolerate larger differences. |

```json
{
  "export": {
    "word_count_check_enabled": true,
    "word_count_check_threshold": 0.95
  }
}
```

If your documents legitimately differ a lot from the segment word count – for example they contain many numbers, or comments that aren’t part of the translation – you may prefer to lower the threshold slightly to avoid false alarms.

:::caution
The check currently applies to **DOCX exports only**. Other Okapi formats (IDML, HTML, XLIFF, PPTX, XLSX, PO) are not yet verified this way.
:::

## Related pages

- [Exporting Translations](exporting.md)
- [Multi-File Projects](multi-file.md)
- [Supported File Formats](formats.md)

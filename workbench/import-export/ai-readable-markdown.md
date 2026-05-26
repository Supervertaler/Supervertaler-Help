---
title: "AI-Readable Markdown Export"
---

The **AI-Readable Markdown** export turns your project into plain text laid out
for AI chat tools (ChatGPT, Claude, Gemini, and the like). Use it when you want
to ask an AI about a translation as a whole — for a second opinion, a
consistency check, or a bulk review — rather than going segment by segment.

Find it under **Project → Export → 📄 AI-Readable Markdown**, which offers two
layouts.

## Two layouts

### Markdown Table

A bilingual table with one row per segment. It renders neatly in any AI chat
interface and is easy to skim by eye.

```
| # | Source | Target |
|---|--------|--------|
| 37 | FIG. 3 toont een vooraanzicht van de inrichting. | FIG. 3 shows a front view of the device. |
| 38 | FIG. 7 toont een achteraanzicht van de inrichting. | FIG. 7 shows a rear view of the device. |
| 39 | FIG. 8 toont de as. | FIG. 8 shows the shaft. |
```

### Labelled Segments

A block per segment, with the source and target on their own
language-labelled lines under a `[SEGMENT NNNN]` header.

```
[SEGMENT 0037]
NL: FIG. 3 toont een vooraanzicht van de inrichting.
EN: FIG. 3 shows a front view of the device.

[SEGMENT 0038]
NL: FIG. 7 toont een achteraanzicht van de inrichting.
EN: FIG. 7 shows a rear view of the device.

[SEGMENT 0039]
NL: FIG. 8 toont de as.
EN: FIG. 8 shows the shaft.
```

## Which one to choose

- **Markdown Table** is best when *you* want to read the result — short, clean
  segments that line up tidily.
- **Labelled Segments** is more robust for handing a whole translation to an AI
  agent. Because each line is labelled rather than separated by `|` columns, it
  doesn't break when a segment contains pipe characters, line breaks, or long
  sentences, the source and target roles stay unambiguous over long inputs, and
  the numbered blocks round-trip cleanly.

:::note
Both layouts read **live grid state**, so any in-progress edit is included even
if you haven't confirmed the segment yet.
:::

## Options

The **Labelled Segments** dialog lets you set:

- **Language codes** — the labels used per line (defaults to your project's
  language pair, e.g. `NL` / `EN`).
- **Segment numbering** — the start number and zero-padding (e.g. `0001`).
- **Content** — bilingual, source only (for AI translation), or target only.
- **Segment filter** — all segments, untranslated only, or translated only.

## Related

- [Exporting Translations](exporting.md)
- [Supervertaler Bilingual Table](bilingual-tables.md)
- [Supported File Formats](formats.md)

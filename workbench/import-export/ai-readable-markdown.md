---
title: "AI-Readable Markdown Export"
---

The **AI-Readable Markdown Table** export turns your project into a plain-text
bilingual table laid out for AI chat tools (ChatGPT, Claude, Gemini, and the
like). Use it when you want to ask an AI about a translation as a whole — for a
second opinion, a consistency check, or a bulk review — rather than going
segment by segment.

Find it under **Project → Export → 📄 AI-Readable Markdown Table (read-only)**.

```
| # | Source | Target |
|---|--------|--------|
| 37 | FIG. 3 toont een vooraanzicht van de inrichting. | FIG. 3 shows a front view of the device. |
| 38 | FIG. 7 toont een achteraanzicht van de inrichting. | FIG. 7 shows a rear view of the device. |
| 39 | FIG. 8 toont de as. | FIG. 8 shows the shaft. |
```

It renders neatly in any AI chat interface and is easy to skim by eye.

:::note
This export is **read-only** — it's for *reading* a translation, not for feeding
edits back in. If you want to send the translation out for editing (by a
proofreader or an LLM) and pull the changes back into your project, use
[Supervertaler Re-importable Text (AI-friendly)](bilingual-text.md)
instead. It adds a `.svexport.json` sidecar and a safe re-import path, and it
read **live grid state** so in-progress edits are included.
:::

## Options

The dialog lets you set the content (bilingual, source only, or target only) and
a segment filter (all, untranslated only, or translated only).

## Related

- [Supervertaler Re-importable Text (AI-friendly)](bilingual-text.md)
- [Exporting Translations](exporting.md)
- [Supervertaler Re-importable Table (DOCX)](bilingual-tables.md)
- [Supported File Formats](formats.md)

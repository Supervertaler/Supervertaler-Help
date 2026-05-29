---
title: "Import Options (File Types)"
---

When you import an Office document (Word, Excel or PowerPoint), Supervertaler uses the bundled **Okapi sidecar** to decide which parts of the file become translatable segments. The **File Types** options let you control that – so you can pull in (or leave out) things like comments, hidden text, headers and footers, and speaker notes.

## Where to set them

There are two places, and they work together:

- **Settings → 📄 File Types** – your **defaults**, applied to every import. Tick a box, and it's saved straight away. Use **Restore defaults** to go back to the recommended set.
- **The import dialog** – when you import a single document or a folder, the same options appear there, pre-filled from your defaults. Any change you make applies to **that import only**, overriding the default without changing it.

:::note
These options apply to Okapi-based imports (DOCX, XLSX, PPTX). Plain text and Markdown files, and CAT-tool bilingual formats, are unaffected.
:::

## Word (DOCX)

| Option | What it does |
| --- | --- |
| **Comments** | How to handle Word review comments. **Skip** (default) leaves them out. **Import as comments** brings them in as real comments – anchored to the relevant segment where possible (otherwise to the top of the document), tagged with the original reviewer's name so they're easy to tell from your own. These are shown for context and are *not* re-exported (the originals stay in the file). **Import as translatable text** brings each comment in as a segment to translate (labelled "Cmt" in the Type column); those *are* written back on export. |
| **Import hidden text** | Include text formatted as hidden. Off by default. |
| **Import headers & footers** | Include page headers and footers. On by default. |
| **Import document properties** | Include title, author, keywords and similar metadata. Off by default. |
| **Skip drawing/shape names** | Leave out the auto-generated object names Word gives every shape and group (for example *Shape 16*, *Group 574248*). On by default – these are not real content and would otherwise clutter the grid. |
| **Accept tracked changes** | Use the final, accepted text of any tracked changes. On by default. |

## Excel (XLSX)

| Option | What it does |
| --- | --- |
| **Import hidden rows/columns/sheets** | Include content that is hidden in the workbook. Off by default. |
| **Import sheet (tab) names** | Include the worksheet tab names. Off by default. |
| **Import text in shapes/text boxes** | Include text drawn on the sheet. On by default. |

## PowerPoint (PPTX)

| Option | What it does |
| --- | --- |
| **Import speaker notes** | Include the notes beneath each slide. Off by default. |
| **Import comments** | Include review comments. Off by default. |
| **Import hidden slides** | Include slides marked hidden. Off by default. |
| **Import slide masters / layouts** | Include text on masters and layouts. On by default. |

## How imported parts are labelled

Anything that isn't ordinary body text is tagged in the grid's **Type** column so you can tell at a glance where it came from:

- **Cmt** – a comment
- **Hdr** / **Ftr** – a header or footer
- **Prop** – a document property
- **Note** – a PowerPoint speaker note

## Round-trip on export

The options you import with are remembered with the project and reused when you export. That keeps the document structure aligned, so the translated file comes back out cleanly – there's nothing extra to set at export time.

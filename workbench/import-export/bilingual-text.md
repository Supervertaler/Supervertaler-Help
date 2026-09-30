---
title: "Supervertaler Re-importable Text (AI-friendly)"
---

The **Re-importable Text** round-trip lets you send a whole translation out as a
plain-text file – for a proofreader or an LLM to edit – and then pull the edits
straight back into the same project. It's the plain-text sibling of the
[Re-importable Table (DOCX)](/workbench/import-export/bilingual-tables/), ported from the Supervertaler
for Trados plugin. Added in v1.10.231.

:::note
**Why "Text" and not "Markdown"?** The file is deliberately plain text. Its
segment blocks rely on line breaks being preserved, and a Markdown renderer
collapses single line breaks – which would scramble the structure. AI agents
read the raw characters when you paste a file into a chat, so plain text is both
safe and maximally readable.
:::

## Exporting

**Project → Export → 🔁 Supervertaler Re-importable → Bilingual Text (AI-friendly)…**

You'll get a small options dialog (include locked segments; which statuses to
include) with two ways out:

- **Save to File…** – opens a save dialog and writes the text file (see below).
- **📋 Copy to Clipboard** – copies the same text instead, ready to paste into an
  AI chat. No file is written. See
  [Working without files](#working-without-files-copy-and-paste).

When you save to a file, two files are written side by side:

- `MyProject_bilingual.txt` – the editable text file.
- `MyProject_bilingual.txt.svexport.json` – a **sidecar** that records, per
  segment, a stable id, a source hash, and the status. Keep the two files
  together; the sidecar is what makes a safe re-import possible.

The file opens with a short header that lists exactly which statuses you may set.
Each segment is one block:

```
[SEGMENT 0001]
EN: The <b>quick</b> brown fox {1}
NL: De <b>snelle</b> bruine vos {1}
Status: Confirmed
Comment: Verify the shade of "brown"
```

- The `EN:` line is the **source** – leave it alone. It stays on **one line**, and
  a `[newline]` in it marks where the original source broke across two lines (e.g.
  a subtitle cue). The source is read-only and never written back to your project,
  so these tokens are just there to show its structure – handy for spotting a
  target that's missing a break the source has.
- The `NL:` line is the **target** – edit it freely, but **keep it on one line**.
  Where the target needs a hard line break – for example to split a subtitle
  across two lines – write the literal token `[newline]`:

  ```
  NL: Welkom bij dit webinar[newline]over de waardeketenanalyse
  ```

  On re-import `[newline]` is turned back into a real line break, so the two-line
  layout is preserved on export. *(Introduced in v1.10.255; files exported before
  that – with the target genuinely wrapped over several lines – still re-import
  unchanged.)*
- The `Comment:` line is always present (blank when the segment has no comment)
  so you can see the field exists. **Edit it, fill the blank one, or clear it** – 
  the change re-imports into the segment's comments. It too may span several lines.
- `<b>…</b>`, `<i>…</i>`, `<u>…</u>` are **cosmetic formatting** – add or remove
  them as you like.
- `{1}`, `[1}`, `<92>` and similar are **structural tags** – keep them; dropping
  one will flag the segment on re-import (see below).

A real file looks like this – note the single-line sources and the `[newline]`
token marking where each target splits across two lines:

![A Supervertaler Re-importable Text file: the header lists the project details and the editing rules, the NL: source lines each sit on one line, and two EN: targets show the [newline] token highlighted where a subtitle is split across two lines.](/.gitbook/assets/SUPERVERTALER-RE-IMPORTABLE-TEXT-newlines.png)

## Editing with an LLM

Hand the `.txt` to ChatGPT, Claude, Gemini, etc. with an instruction such as
*"edit only the `NL:` lines; keep each one on a single line, using the literal
token `[newline]` for any line break; leave the `[SEGMENT …]` markers, the `EN:`
lines, and the `{…}` tags untouched."* Because each field is one labelled line
(not a table column), it survives pipe characters and long inputs without the
source/target roles getting confused, and keeping targets to one line stops an
agent from accidentally reflowing them.

## Re-importing

**Project → Import → 🔁 Supervertaler Re-importable → Bilingual Text (AI-friendly) - Update Project…**

Pick the edited `.txt` (its sidecar is found automatically). A preview dialog
shows how many segments will be updated, how many are unchanged, and how many
are skipped – and why. Nothing is applied until you click **Apply changes**.

### Safety guards

- **Source-tamper detection** – if a segment's source line was changed, that
  segment is skipped (its hash no longer matches the sidecar).
- **Structural-tag integrity** – if the edited target dropped a required tag,
  the segment is flagged. With **"Refuse to apply edits that drop required
  tags"** ticked (the default), such segments are skipped; untick it to apply
  them anyway. Cosmetic `<b>`/`<i>`/`<u>` changes never trip this.
- **Locked segments** are never modified.
- **Blocks that match nothing** – when a block can't be matched to a segment
  of the open project, the preview lists it as **MISSING** and it is never
  written anywhere.

### Status

- If you (or the AI) deliberately change a `Status:` line to a different value,
  that status is applied.
- Otherwise, any segment whose target you edited is marked **Draft** – a
  translated-but-unconfirmed state, ready for you to review and confirm.

### Comments

- Existing segment comments are written out as a `Comment:` line. Edit it, add a
  new one to a segment that had none, or delete it – the change re-imports into
  the segment's comments. A comment-only edit (target left alone) is applied on
  its own and shows up in the import preview.

## Working without files: copy and paste

If you work on the text in an AI chat, you don't need a file in either
direction (from v1.10.372). This is the Workbench counterpart of Clipboard Mode
in Supervertaler for Trados.

1. **Project → Export → 🔁 Supervertaler Re-importable → Bilingual Text
   (AI-friendly)…**, choose your options and click **📋 Copy to Clipboard**.
2. Paste the text into your AI chat, with your instructions (see
   [Editing with an LLM](#editing-with-an-llm)).
3. Copy the AI's reply and press **Ctrl+Shift+V** in Supervertaler, or choose
   **Project → Import → 🔁 Supervertaler Re-importable → Bilingual Text
   (AI-friendly) - Update from Pasted Text…**
4. The **Update from Pasted Text** box opens. If the clipboard already holds
   `[SEGMENT NNNN]` text, it is filled in for you; otherwise paste it in. Click
   **Preview Changes…**.
5. You get the same preview and the same safeguards as the file import (tag
   check, locked segments skipped). Click **Apply changes** to update the
   translations, comments and statuses.

The reply doesn't have to be tidy: a line of chat before or after the blocks,
or the whole text wrapped in a code block, is fine.

### How pasted blocks find their segments

Pasted text has no sidecar, so the blocks are matched to your segments by their
**source line**, not by their `[SEGMENT NNNN]` number. The number can't be
trusted on its own: an export filtered by status numbers its blocks from 1
wherever they sit in the project, and an AI may reorder or drop blocks. The
source line is reliable, because it is read-only.

- **Leave the source lines exactly as they were.** A block whose source matches
  no segment is listed in the preview as not found and skipped.
- **Repeated sources** – when the same source text occurs more than once, the
  blocks are paired with those segments in document order.
- **Same session** – if you exported or copied this project earlier in the same
  session, that export's exact mapping is used first.

:::tip
**Ctrl+Shift+V** works only while Supervertaler is the active window, so it
doesn't interfere with other applications. You can change it in
**Settings → ⌨️ Keyboard Shortcuts**.
:::

## Tips

- Export reads **live grid state**, so in-progress edits are included even if
  the segment isn't confirmed.
- If the sidecar is missing, you can still re-import the file. Segments are then
  matched by their source text, exactly as for
  [pasted text](#how-pasted-blocks-find-their-segments), so edits still reach
  the right segments even if the export was filtered by status.

## Related

- [Supervertaler Re-importable Table (DOCX)](/workbench/import-export/bilingual-tables/)
- [Exporting Translations](/workbench/import-export/exporting/)

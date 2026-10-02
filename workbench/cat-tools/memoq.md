---
title: "memoQ Workflow"
---

This guide covers working with memoQ bilingual files in Supervertaler.

## Export from memoQ

### Bilingual DOCX (Recommended)

1. In memoQ, open your project
2. Go to **Documents** view
3. Right-click your document → **Export Bilingual...**
4. Choose **Bilingual DOC/RTF/DOCX**
5. Select **Table format** (two columns)
6. Export the file

:::note
The table format with source and target columns works best with Supervertaler.
:::

### XLIFF Export

1. In memoQ, go to **Documents** view
2. Right-click → **Export Bilingual...**
3. Choose **memoQ XLIFF bilingual**
4. Save the `.mqxliff` file

A memoQ **view** can be exported the same way. Its `.mqxliff` holds every document in the view, and from v1.10.373 Supervertaler imports all of them. Earlier versions read only the first document, so a view came in with just a few segments.

## Import to Supervertaler

1. Go to **Project → Import → memoQ → Bilingual Table (DOCX)…**
   - Or **Project → Import → memoQ → Bilingual Table (RTF)…**
   - Or **Project → Import → memoQ → XLIFF (.mqxliff)…**
2. Select your exported file
3. The segments appear in the translation grid

### The language pair

Supervertaler reads the language pair from the bilingual table's header row
(or, for XLIFF, from the file itself). In a bilingual DOCX, language codes such
as `IT` or `it-IT`, names in other languages such as *Italiano* or *Deutsch*, and
regional forms such as *English (United Kingdom)* are all understood.

If the pair can't be read, the **Confirm language pair** prompt asks you for it
rather than guessing. Pick the right languages: TM matches are looked up for this
pair, and a project with the wrong one finds no TM matches at all.

:::note
Before v1.10.372, that prompt couldn't open, and the import stopped with the
error "No module named 'PySide6'". Update if you see it.
:::

### What Gets Imported

- ✅ Source text
- ✅ Target text (if any)
- ✅ Inline formatting tags (`{1}`, `[2}`, etc.)
- ✅ Segment status

### memoQ XLIFF: tags, statuses and locked segments

From v1.10.373, a `.mqxliff` import brings in memoQ's inline codes as numbered tags, the same way as Trados SDLXLIFF files:

| In memoQ | In Supervertaler |
|---|---|
| A formatting pair, such as bold or italic | `<1>`…`</1>` |
| A placeholder, such as a cross-reference, field or tab | `<2/>` |

Keep the tags in your translation, as in memoQ. On export, each tag becomes the memoQ code it stands for again, so the formatting and placeholders go back where you put them. Before v1.10.373, the contents of a placeholder could appear in the segment as text, for example `(<x id="1164" mq:catalogvalue="…"/>)`.

memoQ's segment statuses come in too:

| memoQ | Supervertaler |
|---|---|
| Not started | Not started |
| Pre-translated, assembled from fragments | Pre-translated |
| Machine translated | Machine translated |
| Edited | Draft |
| Confirmed | Confirmed |
| Reviewer 1 confirmed | Proofread |
| Reviewer 2 confirmed | Approved |
| Rejected | Rejected |

Segments locked in memoQ stay locked.

### memoQ Tag Handling

memoQ uses special tag formats:

| Tag Style | Example | Purpose |
|-----------|---------|---------|
| Curly | `{1}` | Inline tag |
| Mixed | `[2}` or `{3]` | Start/end tags |
| Named | `{MQ}`, `{tspan}` | Formatting tags |

These tags are highlighted in dark red in the grid (matching memoQ's color).

## Translate in Supervertaler

1. Navigate through segments
2. Use AI translation (`Ctrl+T`) or translate manually
3. Confirm each segment (`Ctrl+Enter`)
4. Save your project regularly (`Ctrl+S`)

### Tips for memoQ Projects

- **Preserve tags**: Keep all `{1}`, `[2}` tags in your translation
- **Use SuperLookup**: Press `Ctrl+K` for TM and termbase searches
- **Batch translate**: Select multiple segments and press `Ctrl+Shift+T`

## Export from Supervertaler

1. Go to **Project → Export → memoQ → Bilingual Table - Translated (DOCX)…**
   - Or **Project → Export → memoQ → XLIFF - Translated (.mqxliff)…** for a project imported from memoQ XLIFF
2. Choose a filename
3. The bilingual table (or XLIFF) is recreated with your translations

The export writes the translations in document order, even when the grid is sorted.

A memoQ XLIFF export changes only the segments whose translation or status you changed. Those get the matching memoQ status: *Confirmed* for a confirmed segment, *Reviewer 1* or *Reviewer 2 confirmed* for a proofread or approved one, and *Edited* for anything else. Untranslated segments and segments you left alone keep memoQ's own status.

## Import Back to memoQ

1. In memoQ, go to **Documents** view
2. Right-click your original document
3. Select **Import/Update Translation...**
4. Choose **From bilingual DOC/RTF/DOCX file**
5. Select the file exported from Supervertaler
6. Click **Import**

### Verify the Import

- Check that translations appear in memoQ
- Confirm status shows as "Translated" or "Edited"
- Run memoQ's QA to check for issues

## Complete Workflow

```
memoQ: Export Bilingual DOCX
         ↓
Supervertaler: Import memoQ Bilingual
         ↓
Supervertaler: Translate (AI + manual)
         ↓
Supervertaler: Export memoQ Bilingual
         ↓
memoQ: Import/Update Translation
         ↓
memoQ: QA + Delivery
```

## Troubleshooting

### Tags appear as plain text

Make sure you exported as **Bilingual DOCX** (not "Export without tags").

### Formatting lost on re-import

This can happen if:
- Tags were deleted or modified during translation
- The bilingual table structure was changed

**Solution**: Always keep tags exactly as they appear.

### Status not updating in memoQ

memoQ's import may not change segment status. You can:
- Use memoQ's filtering to find imported segments
- Manually confirm segments in memoQ if needed

---

## See Also

- [CAT Tool Overview](/workbench/cat-tools/overview/)
- [Voice (commands and dictation in memoQ)](/workbench/voice/overview/)

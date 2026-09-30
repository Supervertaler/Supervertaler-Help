---
title: "CAT Tool Integration Overview"
---

Supervertaler is designed to work alongside professional CAT (Computer-Assisted Translation) tools, not replace them. Use it as a **companion tool** for AI-powered translation within your existing workflow.

## Supported CAT Tools

| CAT Tool | Import Format | Export Format |
|----------|--------------|---------------|
| **memoQ** | Bilingual DOCX or RTF, XLIFF | Bilingual DOCX or RTF, XLIFF |
| **Trados Studio** | SDLPPX packages | SDLRPX return packages |
| **Phrase (Memsource)** | Bilingual DOCX | Bilingual DOCX |
| **CafeTran Espresso** | Bilingual table DOCX | Bilingual table DOCX |
| **Déjà Vu X3** | Bilingual RTF | Bilingual RTF |

## Why Use Supervertaler with CAT Tools?

### AI Translation Power

CAT tools have limited AI integration. Supervertaler lets you:
- Use multiple LLM providers (GPT-4, Claude, Gemini)
- Create custom translation prompts
- Batch translate with context awareness

### Workflow Flexibility

- Translate offline with Ollama
- Work on files while others are locked in the CAT tool
- Quick review and post-editing without heavy software

## Typical Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR CAT TOOL                            │
│  (memoQ, Trados, Phrase, CafeTran)                         │
│                                                             │
│  1. Receive project from client                            │
│  2. Set up TM, termbases in CAT tool                       │
│  3. Export bilingual file or package                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    SUPERVERTALER                            │
│                                                             │
│  4. Import bilingual file                                  │
│  5. AI translate + post-edit                               │
│  6. Use SuperLookup for research                           │
│  7. Export bilingual file                                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    YOUR CAT TOOL                            │
│                                                             │
│  8. Import translations back                               │
│  9. Run QA checks                                          │
│  10. Deliver to client                                     │
└─────────────────────────────────────────────────────────────┘
```

## Key Concepts

### Preserving Formatting

Supervertaler preserves CAT tool formatting tags:
- memoQ: `{1}`, `[2}`, `{MQ}` inline tags
- Trados: `<1>`, `</1>` numbered tags
- Tags are highlighted in the grid for visibility

### Segment Status

Segment statuses map between tools:
- **Draft** → Trados *Draft* / memoQ *Edited*
- **Confirmed** → Trados *Translated* ✓ / memoQ *Confirmed*
- **Approved** → Trados *Sign-off Approved* / memoQ *Reviewer 2 confirmed*

See [Segment Statuses](/workbench/editor/segment-statuses/) for the full reference.

### The language pair

Every project has a source and a target language, and TM matches are looked up
for exactly that pair – a project with the wrong pair finds no TM matches at all,
even though the TM looks fine. How Supervertaler gets the pair depends on the
file you import:

| Import | Language pair |
|--------|---------------|
| **Trados** package (SDLPPX) or SDLXLIFF | Read from the file. |
| **memoQ** bilingual DOCX, RTF or XLIFF | Read from the table's column headers (DOCX), its header row (RTF) or the file itself (XLIFF). In the DOCX headers, codes such as `IT` or `it-IT`, names in other languages such as *Italiano*, and regional forms such as *English (United Kingdom)* are all understood. If the pair can't be read, the **Confirm language pair** prompt asks you. |
| **Phrase** bilingual DOCX | Read from the file; the **Select Languages** dialog opens pre-filled for you to confirm. |
| **Trados** bilingual review DOCX | The file has no language header, but Word stores a language on the source text and on the target text. The **Select Languages** dialog opens pre-filled from those ("Auto-detected from file: German → French. Confirm or change below."). If both columns carry the same language, nothing is assumed. |
| **CafeTran** bilingual DOCX | The **Confirm language pair** prompt opens, pre-filled the same way from the Word languages of the two columns, or from the column headers if they are language codes. |
| **Déjà Vu X3** bilingual RTF | The **Confirm language pair** prompt shows the pair Supervertaler worked out from the language codes in the file. If you correct it, the export tags the translations with the corrected language too. |

The pre-filled and confirmed pairs for Trados review DOCX, CafeTran and Déjà Vu
X3 files are new in v1.10.372. Before that, CafeTran projects were always
created as English → Dutch, and Déjà Vu projects fell back to Dutch → Spanish
when no languages were found. If an older project of yours gets no TM matches,
see [TM Matches Not Appearing](/workbench/troubleshooting/tm-matches/#2-does-the-project-have-the-right-language-pair).

### Round-Trip Compatibility

Files exported from Supervertaler can be imported back into the CAT tool with:
- All translations preserved
- Status information maintained
- Formatting intact

## Choosing the Right Workflow

| Scenario | Recommended Workflow |
|----------|---------------------|
| **Full project in memoQ** | [memoQ Bilingual DOCX](/workbench/cat-tools/memoq/) |
| **Trados Studio package** | [SDLPPX/SDLRPX](/workbench/cat-tools/trados/) |
| **Phrase/Memsource project** | [Phrase Bilingual DOCX](/workbench/cat-tools/phrase/) |
| **CafeTran external view** | [CafeTran DOCX](/workbench/cat-tools/cafetran/) |
| **Standalone DOCX** | Direct import, no CAT tool needed |

---

## Tool-Specific Guides

<table data-view="cards">
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>memoQ</strong></td>
<td><a href="memoq.md">memoQ workflow guide →</a></td>
</tr>
<tr>
<td><strong>Trados Studio</strong></td>
<td><a href="trados.md">Trados workflow guide →</a></td>
</tr>
<tr>
<td><strong>Phrase</strong></td>
<td><a href="phrase.md">Phrase workflow guide →</a></td>
</tr>
<tr>
<td><strong>CafeTran</strong></td>
<td><a href="cafetran.md">CafeTran workflow guide →</a></td>
</tr>
</tbody>
</table>

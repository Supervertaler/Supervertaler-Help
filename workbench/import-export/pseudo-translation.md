---
title: "Pseudo-translation (Export Test)"
---

**Pseudo-translation** fills your targets with deliberately stress-tested
placeholder text so you can export the document and check that it comes out with
correct formatting, layout, fonts and tags — **before** you invest any time in
real translation. It's a pre-flight check borrowed from desktop CAT tools.

Find it under **Bulk Operations → 🧪 Pseudo-translate (Export Test)…**.

## Why not just copy source to target?

Copying source into target and exporting tests the *plumbing* — does the file
merge and export, do the inline tags survive — but it misses the problems that
actually bite at the end of a job:

- **Length stays identical**, so overflowing text boxes, clipped table cells,
  fixed-width fields, reflow and truncation never show up. Real translations
  change length.
- **Characters are never exercised** — the source already renders fine in the
  document's fonts and encoding, so copying it tells you nothing about whether
  the *target* language's characters will.
- **Dropped or merged segments stay invisible**, because target text that equals
  the source still looks correct.

Pseudo-translation addresses all three at once.

## What it does

For every segment in the chosen scope it rewrites the target so that:

1. **Inline tags are preserved exactly.** Formatting tags (`<b>`, `<i>`, …),
   Trados/SDLXLIFF numeric tags (`<410>`) and memoQ tags are kept verbatim and
   in order — only the words between them are changed. This is what makes the
   test trustworthy: the tag round-trip you're checking isn't disturbed.
2. **The text is length-expanded** by a ratio you choose, to surface overflow
   and layout breaks.
3. **Characters are optionally accented** (`werkwijze` → `wéřkwíjžé`) to test
   diacritics, encoding and font coverage.
4. **Each segment is wrapped in `⟦ ⟧` markers** so a dropped, merged or
   misplaced segment is obvious in the exported file.

A segment like

```
De uitvinding betreft een <b>werkwijze</b> voor het sorteren.
```

becomes something like

```
⟦Dé úítvíñdíñğ bétřéft ééñ lorem <b>wéřkwíjžé lorem</b> vóóř hét šóřtéřéñ. lorem⟧
```

## Options

| Option | What it controls |
|--------|------------------|
| **Apply to** | All segments (default), the filtered/visible set, or just your selection. |
| **Length expansion** | 0% (structure only), +30% (typical), up to +200% (max stress). |
| **Characters** | *Accented* (tests encoding/fonts) or *Plain words* (length + markers only). |
| **Boundary markers** | Wrap each segment in `⟦ ⟧`. On by default. |

## Workflow

1. Open the project and run **Bulk Operations → 🧪 Pseudo-translate (Export Test)…**.
2. Pick your options and confirm.
3. Export the document the way you normally would (**Project → Export → Export
   Translated Document**, or any bilingual/CAT export) and open the result.
4. Check for clipped text, broken tables, missing glyphs, reordered or missing
   `⟦ ⟧`-marked segments, or tag errors.
5. **Edit → Undo** restores your real (usually empty) targets — the whole
   operation is recorded as a single reversible step.

:::note
Pseudo content overwrites existing targets (Undo restores them). If you'd rather
keep your working project untouched, run the test on a **copy** of the project.
:::

## Related

- [Export Verification (Word-Count Check)](export-verification.md)
- [Exporting Translations](exporting.md)
- [Re-importable Table (DOCX)](bilingual-tables.md)

---
title: "Fuzzy Matching"
---

Fuzzy matching finds similar segments (not just exact duplicates).

## How to use it

- As you navigate, Supervertaler searches your TMs for similar source text.
- Matches are scored by similarity.

## When to trust a match

- **High scores** are often safe to insert as a starting point.
- **Mid/low scores** can still be useful, but should be treated as suggestions.

## Fragment matches

From v1.10.373, the Match Panel also finds TM entries when the TM and your
document are **segmented differently**. A fuzzy match compares whole segments,
so it misses these:

- **The segment is part of a TM sentence.** The TM holds *Which heading do you
  want to read?*, but your document has it as two segments, *Which heading* and
  *do you want to read?*. On either segment, you see the TM's whole sentence and
  its translation. The TM Source box shows which part is yours: the rest is
  struck through.
- **A TM sentence is part of the segment.** The TM holds *Close the valve.*,
  and your segment is *Close the valve. Then open the tap.* You see *Close the
  valve.* with its translation.

These matches are marked **✂ fragment**. Their percentage is not a similarity
score: it says how much of the longer text the shorter one covers. Insert the
match and keep the part you need, or use [FuzzyFixer](/workbench/ai-translation/fuzzyfixer/)
to have the AI adapt it to your segment.

The words have to match in an unbroken run. Case, punctuation and tags are
ignored, and a fragment has at least two words; for single words, use a
glossary. Fragment matches only fill the places the fuzzy matches leave free,
are never inserted automatically, and don't play the fuzzy-match sound. They
aren't looked up for Chinese, Japanese or Korean text yet.

To switch them off, untick **Show fragment matches from the TM** on
**Settings → ⚙️ General**, in the **📂 TM settings** box.

## Tips

- Always review fuzzy matches before inserting.
- For formatted text, preserve tags when inserting matches.
- If you only ever get 100% matches and never fuzzy ones, see [TM Matches Not Appearing](/workbench/troubleshooting/tm-matches/#3-exact-matches-appear-but-never-fuzzy-ones).

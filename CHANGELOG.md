# Changelog

The documentation at [docs.supervertaler.com](https://docs.supervertaler.com).
Cloudflare Pages builds on every push to `main`, so there are no releases and no
version numbers – the headings are dates.

This file starts on 2026-09-16. Anything before the entries below is in the git
history rather than here, because reconstructing it after the fact would be
guesswork.

## 2026-09-18

- **memoQ: terminology is termbases now, not a glossary file.** The Terminology page is rewritten around the Termbases window – Read, Project, CS and AI, and what each decides – the Terms window, and making, importing, exporting and deleting termbases from memoQ; it also records what memoQ told us in September 2026 about why a plugin cannot read memoQ's own term bases, and when that may change. *Glossary Format* becomes *Importing and exporting termbases* at the same address, describing both file shapes Import reads and Export writes and how direction and duplicates are handled. The prompt editor page describes the four rows of the context bar, including the new Termbases summary, and *Export glossary* becomes *Termbase from this prompt's terms*. Every other mention of the glossary file across the memoQ pages is updated or removed.

## 2026-09-13

### Added

- **Supervertaler Sidekick is a documented product**, alongside Trados, memoQ and
  Workbench: its own tree in the sidebar, its own search scope, its own llms.txt
  subset.
- **Language packs** – the search sources that belong to one language pair, as one
  submenu inside Web searches, named by the pair.

### Changed

- **The voice feature is SuperVoice** throughout the Trados pages.
- **Trados MCP**: `get_comments` reports its scope and `add_comment` takes a range.

## 2026-09-12

### Added

- **Dictation and voice editing** on the Trados side: what makes a good command
  word and why, the alias column, document source selection, and the hand-off
  between dictation and voice commands. Dictation is two commands now rather than
  a toggle.

## 2026-09-11

### Changed

- **FigureLens is shown in two readable screenshots** instead of one composite. The
  single image put the Batch Operations tab and the FigureLens panel side by side,
  so both were at about half the width they need to be read, and the three numbered
  markers were the only way in. Split along the seam the numbering already implies.

## 2026-09-10

### Added

- **The docs have a favicon.** Starlight had always linked `/favicon.svg` but no
  such file existed, so every docs tab showed the browser's blank-page icon. The
  product site's three icon files are carried here, including the SVG that inverts
  itself on a dark tab strip.

### Changed

- **The landing cards carry the Supervertaler mark** in each product's colour,
  where they had a puzzle-piece emoji for Trados and memoQ's own orange logo for
  memoQ – one generic, one somebody else's brand.

## 2026-09-09

### Changed

- **En dashes throughout.** 359 literal em dashes across 46 pages, and 60 more
  that were typed as `--` and turned into em dashes by Starlight's smartypants at
  build time – so the source read clean while the site did not. The one em dash
  left is on the clipboard autocorrect page, where the rule being documented is
  the one that converts em dashes to en dashes.

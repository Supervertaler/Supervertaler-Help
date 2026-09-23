# Changelog

The documentation at [docs.supervertaler.com](https://docs.supervertaler.com).
Cloudflare Pages builds on every push to `main`, so there are no releases and no
version numbers – the headings are dates.

This file starts on 2026-09-16. Anything before the entries below is in the git
history rather than here, because reconstructing it after the fact would be
guesswork.

## 2026-09-23

- **memoQ: ready for the installer.** *Installation* is rewritten around it: what it puts where, the two settings that switch Supervertaler on inside memoQ, updating, reinstalling after a memoQ upgrade, installing by hand from the zip, and uninstalling from Windows Settings. It used to describe copying two DLLs into Program Files.
- **memoQ: a Licensing page.** The 14-day trial, one licence for Trados and memoQ, where the key goes, two computers with both plugins counting once, what pauses when a licence lapses (only AI translation) and the two different fixes for the two ways it lapses.
- **memoQ: the AI assistants page covers ChatGPT desktop**, and is renamed *AI Assistants (Claude Desktop, ChatGPT)*. Setting up is now the editor's **Connect AI assistant** window – a button for ChatGPT, and for Claude Desktop a button that shows the extension the installer put in place. The live document link names memoQ's PDF Preview tool as its prerequisite and the folder the installer uses.
- **memoQ: the editor page is *The Supervertaler Editor*.** It opened with "Prompt Library & Editor", which confused anyone who arrived from the editor's own Help menu, since the window does a good deal more than prompts. It now says how to open it from the Start menu and what it is for. The FigureLens section's address is `#figurelens`, which the editor's FigureLens help link has always pointed at.
- **memoQ: the sidebar lists the editor, the AI assistants and Licensing.** The first two pages existed but were reachable only through links.
- Getting started, the memoQ overview and Troubleshooting follow the above, including an entry for "AI translation is paused".

## 2026-09-19

- **memoQ: adding a term from the grid is a keyboard shortcut now.** Alt+Up, twice – once on the word, once on its translation – the same key Supervertaler for Trados uses. The Terminology page leads with it: that the order does not matter, what the note by the cursor is for, that a half-finished pair is forgotten after two minutes, where the off switch is, and that the shortcut is live only while memoQ is in front, so Alt+Up still opens the parent folder in Explorer. The right-click route through Translation results is kept as the other way in, with the reason it is not the first one offered.

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

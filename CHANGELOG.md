# Changelog

The documentation at [docs.supervertaler.com](https://docs.supervertaler.com).
Cloudflare Pages builds on every push to `main`, so there are no releases and no
version numbers – the headings are dates.

This file starts on 2026-09-16. Anything before the entries below is in the git
history rather than here, because reconstructing it after the fact would be
guesswork.

## 2026-09-29

- **memoQ: house rules are judged rule by rule.** The editor page no longer says the style rules always go. The client bank's brief, style guide and domain notes do; each house rule in `_shared` is judged in the job's one question by its **Scope:** line, and everything goes when the question cannot be asked (from v0.1.0). The bank-extracts path is now given as `C:\Users\<you>\Supervertaler\…`, not the author's own drive.
- **memoQ: installing from the direct download.** Step 1 of the installation page links `supervertaler.com/download/memoq`, which now starts the download of the latest installer. The requirements say that versions of memoQ before 12 have not been tested.
- **Trados: what the usage statistics ping sends.** The Usage Statistics page listed five items, and the notice in the plugin four, but the ping also sends the product, whether Windows runs in a virtual machine, the processor architecture, the Windows display scaling and text size, and the Supervertaler UI scale. The page now lists every item, says why the scaling figures are collected, and shows the notice as it reads from v18/19.20.198, no longer cut off at the bottom.

## 2026-09-28

- **Trados: the running AI cost.** The Reports page describes the new line under the tab's header - this session's and today's AI cost - what it counts, where today's figure comes from, and what "up to" means (from v18/19.20.198).
- **Trados: Claude Sonnet 5.5.** The AI Settings provider table lists the Claude short list as it now is: Sonnet 5.5 (the default), Opus 5.5 and Fable 5.1 (from v18/19.20.198).
- **Trados: what the AI may send back** (from v18/19.20.198). Batch Translate has a new section on the output contract every translation request now ends with, the check each reply passes before it is written, what happens to a reply that fails it twice, and the one case the check can refuse wrongly. *Translator comments* explains `[[TC: …]]` and the choice between keeping it in the target (the default) and a Trados comment; AI Settings documents the new checkbox. Clipboard Mode says what is checked on paste and why such a segment is left out. The AI Proofreader page describes the fixed answer format and how a source query is now written.
- **Trados: house defaults are judged rule by rule** (from v18/19.20.198). SuperMemory's AI Integration page explains that each rule of `_shared/style.md`, and each terminology section without a table, is now part of the once-per-document selection, and that a rule's **Scope:** line is what decides it. The brief and style guide of the active bank still always go.
- **Trados: two new voice commands** (from v18/19.20.198). The SuperVoice command table lists "super search" (SuperSearch, Alt+S) and "web search" / "search the web" (Alt+W). The keyboard shortcuts page no longer says the TermLens popup opens with a tap of `Ctrl`; it is `Alt+L`.
- **Trados: a broken path on the AI Proofreader page.** `trados\reports` had its `\r` turned into a line break, as on the Reports page before.
- **Trados: a large memory bank sends only what each document needs** (from v18/19.20.198). SuperMemory's AI Integration page explains the selection, what always goes, what it costs, and the `trados\bank-extracts\` file listing what each document got; Batch Translate, Reports, Context layers and the data folder page point to it.
- **Trados: notes for the assistants only.** The SuperMemory pages explain `audience: assistant`, which keeps a memory bank note out of translation while the chat and the MCP tools still read it (from v18/19.20.198).
- **Trados: extra files in a bank are read.** The SuperMemory page no longer implies a bank is only its three files, and the Report button's description drops the warning that such files are never sent – untrue since v18/19.20.183.

## 2026-09-24

- **memoQ: notes for the assistants only.** The editor page explains `audience: assistant`, which keeps a memory bank note out of translation while the AI assistants still read it.
- **memoQ: the live document link starts by itself** the first time memoQ loads Supervertaler; the AI assistants page no longer tells you to run it from Program Files.
- **memoQ: a large memory bank sends only what the job needs.** The editor page explains the selection, what always goes, and where the file listing each job's selection is.
- **memoQ: the memory bank can be switched off**, under Translation settings, and single rows are cached like Pre-translate. The editor page says both, and what *not sent* on the Bank row means.
- **memoQ: what the model may send back.** The editor page describes the built-in output contract – translation only, and anything worth flagging in one `[[TC: …]]` marker at the end, written to the client – the check every reply now passes before it reaches the grid, what happens to a reply that fails it twice, and that rows with nothing to translate are copied rather than sent. The Activity window's new Rows and Reply lines are explained, and Troubleshooting has an entry for a row left empty with "Supervertaler left this segment for you".

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

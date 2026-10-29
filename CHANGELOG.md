# Changelog

The documentation at [docs.supervertaler.com](https://docs.supervertaler.com).
Cloudflare Pages builds on every push to `main`, so there are no releases and no
version numbers – the headings are dates.

This file starts on 2026-09-16. Anything before the entries below is in the git
history rather than here, because reconstructing it after the fact would be
guesswork.

## 2026-10-29

- **Trados: Gemini 4 Argon replaces Gemini 3.1 Pro – not released yet.** AI Settings, Providers and Models, SuperBench and the AI Cost Guide now name Gemini 4 Argon as the top Gemini model, with its prices ($2 / $10 until 30 November 2026, $4 / $20 from 1 December) and its 95% cache discount, marked "from v18/19.20.203". Publish with the release that ships it.

## 2026-10-27

- **Trados: SuperCleaner, a new page – not released yet.** SuperCleaner tidies up Word documents as Trados converts them, so you get fewer tags: it joins pieces of text Word has split for no visible reason, and removes Word's bookkeeping, with optional clean-up for documents converted from PDF. The page covers turning it on, what happens to your file (the original is never changed), what it cleans, and the check that compares every cleaned file with the original and uses the original if anything differs. It is published ahead of the feature with a notice saying so. Listed under *More Tools*.

## 2026-10-25

- **Trados: Add segments to SuperMemory, a new page** (from v18/19.20.201). How to copy a range of reviewed segments into a memory bank with Ctrl+Alt+Shift+A, so the reviewed part of a document becomes the reference for the rest: choosing the range, the bank and the size limits. Linked from *SuperMemory*, *Quick Add* and *Keyboard shortcuts*.
- **Trados: re-importing a combined export of a merged document** (from v18/19.20.201). *Import/Export* now says a row is matched by its file as well as its number, and that a row whose file cannot be told is skipped and named; step 2 also says to click an export before using its buttons.
- **Trados: Proofread on a merged document** (from v18/19.20.201). *AI Proofreader* now says each request holds one file's segments, and that the cards name the file, e.g. *Segment 3 of Acme - Text.docx*.
- **Trados: Batch Translate gives repetitions one translation** (from v18/19.20.201). *Batch Translate* has a new section, *Repetitions get one translation*: what counts as a repetition, which segments decide the translation and which are never changed, what happens when existing translations disagree, the log line, and the note the backup TMX keeps of the AI's own wording. *AI Settings* describes **Keep repetitions consistent in Batch Translate**. *Progress and Logging* says that a run now writes only into the document it was started in, so switching documents during a run is safe.

## 2026-10-23

- **Link previews have a picture.** A docs link pasted into WhatsApp, LinkedIn, Slack or X showed the touch icon stretched into a blur, because Starlight writes every Open Graph tag except the image. `Head.astro` now adds one: a Trados page gets the product site's *Supervertaler for Trados* card, a memoQ page the *for memoQ* card, and every other page the brand card. The pictures are served from supervertaler.com, so the docs and the product site share one set.
- **Trados: the `_shared` bank is made for you.** *SuperMemory* told you to create `_shared` in File Explorer, because the *+ New memory bank…* dialog stripped the underscore. It now says that from v18/19.20.201 Supervertaler makes `_shared` when Trados Studio starts and there is none, that it sends nothing until you write in it, that an existing one is left alone, and that the dialog keeps the name; the File Explorer route stays, for earlier versions. *AI Integration* says that a file still exactly as Supervertaler created it is not sent.
- **memoQ: the `_shared` bank is made for you.** *The Supervertaler Editor* and *Context layers* mentioned `_shared` without saying how it comes to exist. They now say that from v0.1.26 memoQ and the editor make it when it is missing, that it is at the top of the editor's list of memory banks marked *always sent*, and that it sends nothing until you write something in it.
- **Trados: renaming and deleting banks, as they are.** *SuperMemory* said a bank could not be renamed or deleted inside the plugin, which stopped being true in v18/19.20.184. A new section, *Seeing, renaming and deleting*, describes **Settings → Library**: every bank and its files, **Edit**, and the right-click **Set as active**, **Rename**, **Delete** (to `.trash`, restorable) and **Open bank folder**, with what is refused. *Creating* says a new bank gets a `reference/` folder, becomes the active bank and sends nothing until you write in it. *Prompts* calls the tab **Library**, as it has been since v18/19.20.184, and points to it for memory banks. *Data Folder and Team Folder* says how `_shared` comes to exist.
- **Trados and memoQ: a bank called `shared`.** Both *Troubleshooting* pages have a new entry for anyone whose New memory bank turned `_shared` into `shared`: why it has no effect, and how to make it the shared bank.
- **memoQ: the editor's tree shows your memory banks.** *The Supervertaler Editor* said the tree held folders and prompts. It now says the memory banks are below them, `_shared` first, that a bank file opens as plain text and saves with Ctrl+S, that right-click makes a bank the project's bank, and that `_shared` is not in the Bank list. *AI Assistants* and *memoQ and Trados Compared* name the editor as a place to edit bank files, where *AI Assistants* said nothing in memoQ writes to a bank.
- **memoQ: Removing MT Marks, a new page.** memoQ keeps a record of every machine translation inserted into a row and shows it in the Review tab, the edit distance report and bilingual exports, even after the row is rewritten and confirmed. The page explains the editor's new *Remove MT marks from an exported file* and the steps that make it work: export with the skeleton, clean, remove the documents, import the clean copies as new. It also says why an update does not work and where the method works. *The Supervertaler Editor* links to it, and *Troubleshooting (memoQ)* answers "The Review tab says machine translation from MT / Supervertaler".
- **memoQ: Removing MT Marks shows where the command is.** A screenshot of the editor's *memoQ* menu with *Remove MT marks from an exported file…* highlighted, at step 2.

## 2026-10-18

- **Sidekick: text size.** *QuickTrans* has a new section on the **−** and **+** at the end of the Source line and `Ctrl+=` / `Ctrl+-` / `Ctrl+0`, and the window page lists the keys. Neither page mentioned text size before.
- **Sidekick: model lists in two tiers.** *QuickTrans → Choosing models* explains the short list each dropdown opens on (the one Supervertaler for Trados shows) and **Show all models**, which replaced **Fetch all models**. *Installation* says the same in one line.
- **Sidekick: the Scratchpad tab, documented.** The window page describes the third tab, `Ctrl+3`, and the **Opens on:** choice; *Keyboard shortcuts* lists `Ctrl+Alt+N`. All three arrived on 2026-09-19 without a mention here.
- **Sidekick: the starter menu, as it now ships.** *AI actions* no longer lists the Dutch–English translation prompts, Localize or the GitHub-issue summary, and points to QuickTrans for translation; *The window* drops the Local searches section; *Web and local searches* drops LogiTerm and says every search opens in your default browser.
- **Sidekick: Reload and Search the desktop have no key by default.** *Keyboard shortcuts* shows both as none and suggests a key; *Web and local searches*, *Settings and files* and *Installation* no longer send you to `Ctrl+R` or `Ctrl+Shift+D`.
- **Sidekick: *Installation* is about the installer now.** It starts from the download, says what to do when Windows calls the installer unrecognised, and explains the folder it suggests and why your content lives there. *Updating* and *Uninstalling* describe the installer's behaviour, and running the script with your own AutoHotkey moves to *Running it from the source* at the end. The download link points at GitHub's latest release, so it always gives the newest installer.
- **Sidekick: *Settings and files* matches an installed copy.** Where the folder is, the `AutoHotkey` folder inside it, what the installer adds to Windows (it said nothing at all was written outside the folder), that `settings.ini` is written as you change settings rather than copied from the example, and where the key file is when the data folder has moved.
- **Sidekick: the character keys are in the shortcuts table.** *Keyboard shortcuts* lists the eight built-in ones – euro sign, en and em dash, single curly quotes, quotes around the selection, bullet and backtick – with their keys, and says what to do when one clashes with a program's own key.
- **Sidekick: *Installation* no longer says Sidekick asks for administrator rights.** It stopped doing so on 2026-08-30. The note now says what running without them means: its shortcuts do not reach a program started with *Run as administrator*.

## 2026-10-14

- **memoQ: a new page, *memoQ and Trados Compared*.** One table of what each plugin can and cannot do – AI translation, terminology, translation memories and AI assistants – with what to do in memoQ instead, and a short list of what memoQ would need to give plugins to close each gap. Under *Reference (memoQ)*, and linked from the memoQ overview and *AI Assistants*.

- **memoQ: the *Claude Desktop* switch, explained without the guesswork.** *AI Assistants* now says that "hands the segments to the chat" means recording them and inserting what is already staged, not sending anything to Claude; that with the switch on, a row with nothing staged is left exactly as it was and memoQ shows *No staged translation for this segment* (also a new Troubleshooting entry); and that landing on a segment serves a staged translation first in both modes, which the table had wrong for the ticked state. Three bullets are no longer introduced as "two consequences". *Getting Started* and the editor page say what the switch decides – the rows nothing was staged for – rather than only who pays.
- **memoQ: *Which AI apps work?* covers a Claude conversation linked to your computer through the Claude desktop app.** It runs in the cloud but reaches the Supervertaler server on your PC through the desktop app, so the note no longer implies every cloud-hosted Claude is ruled out. It also says the *Claude Desktop* label covers ChatGPT desktop and Claude Code too.

- **memoQ: Parallel requests, for 0.1.20.** *Getting Started* lists it, with the values to choose (4 for a cloud provider, 1 for a model on your own computer); *Local and Cloud Models* explains that it now limits cloud providers too, and that memoQ's own limit is the ceiling. *Segments per request* is called *Segments per batch*, as in the dialogs.
- **Trados: *Providers* has a section, *Local models: what to expect*.** Quality, speed, what narrows the gap (termbases and SuperMemory), SuperBench for testing on your own work, and a link to the case study on supervertaler.com. Its Ollama note now says that models ending in `-cloud` run on Ollama's servers, so the text leaves your computer.
- **memoQ: a new page, *Local and Cloud Models*.** What leaves your computer with each choice (a local model, an Ollama cloud model, an OpenAI-compatible server, the cloud providers, Claude Desktop under a Team or a personal plan); setting up Ollama; context length and a model's own limit; speed without a graphics card, with a picture of the waiting notice; the *Stop translating these segments* link for Pre-translate; the separate Parallel requests value; and what quality to expect, linking to the case study on supervertaler.com. Under *Features (memoQ)* in the menu.
- **memoQ: *Getting Started* lists local models as a provider**, and says the Endpoint is only for Ollama and OpenAI-compatible servers. It still said "Anthropic, OpenAI or Google", although Ollama and OpenAI-compatible have been supported since v0.1.12.

## 2026-10-12

- **Trados: an AI assistant can keep your memory banks up to date** (from v18/19.20.199). The MCP Server page lists the four new tools (`read_supermemory_file`, `append_terminology_row`, `update_supermemory_section`, `write_supermemory_file`) and has a new section, *Keeping your memory bank up to date*, on what it can write and what protects the bank. *SuperMemory* no longer says MCP access is read-only.
- **Trados: `list_project_templates` finds every template Studio offers** (from v18/19.20.199), not only those in the `Project Templates` folders. The MCP Server and Studio Tools pages say so.
- **memoQ: no more "early development" notice.** The banner across every memoQ page, which pointed readers to the Trados plugin as "the stable product", is gone, and the memoQ card on the docs home page says "Source-available, 14-day free trial" like the others instead of "In early development". Supervertaler for memoQ has been released since 0.1.0.
- **memoQ: a screenshot on the overview page** – memoQ with the Supervertaler editor open beside the grid, termbase terms highlighted and the AI's suggestion and term hits in Translation results.
- **memoQ: a termbase ticked with memoQ open works without a restart** (from v0.1.11). *Terminology* drops the step about ticking a termbase to clear *Not configured*, and *Troubleshooting* lists the termbase tick as its own check; both say what v0.1.10 and earlier did.

## 2026-10-09

- **Trados: Studio 2022 is supported** (from v17.20.199), in a third build beside the 2024 and 2026 ones. The overview, requirements and installation pages, the build and version tables on *Trados Studio 2026 & .ttb* (now "Three builds, one product"), Troubleshooting (the minimum Studio, the three downloads and which build greys out which Studio, and the plugin folders for `17`), the docs home page, Usage Statistics and MultiTerm Support say so. The MCP Server page lists `"2022"` among the `instance` values and three Studios side by side.

## 2026-09-30

- **Workbench is in active development again.** The banner on every Workbench page said it was no longer developed; it is gone. The docs home page lists Workbench with the other products instead of as a footnote, and its card says development has resumed.
- **Workbench: the pages catch up with v1.10.370–v1.10.372.** They were last updated for v1.10.369, and the three releases since changed a good deal.
- **Workbench: five new pages.**
  - *Segmentation Rules* – your own break and no-break rules, SRX import and export, and which imports use them.
  - *Inline Codes* – placeholders such as `{name}`, `%s` and `\n` treated like tags.
  - *QA Checks* – saved find-only checks and the tags & codes check.
  - *Check with LanguageTool* – the public service or your own server, and what is sent.
  - *TM Matches Not Appearing* – four checks, and the diagnostic script from v1.10.370–371 with its `--repair` option.
- **Workbench: Settings pages save themselves** (from v1.10.372). The General page explains it, and every "click Save" step is gone, including those for API keys, the language and the custom MT endpoint.
- **Workbench: the AI pages.**
  - *Token Usage & Costs* covers showing costs in euros, the cost of one project in **Project → 📋 Project Info…** (which also shows the AI model in use), and the estimate before a batch run.
  - The Ollama page has the request timeout and keep-warm settings.
  - Chat explains what the 💾 TMs and 📚 Termbases chips send.
  - *Batch Translation* describes the dialog as it really is.
- **Workbench: import, export and CAT tools.**
  - Updating a project by pasting bilingual text, with no file (Ctrl+Shift+V).
  - **Edit → ➕ Add Source Text…**.
  - **📦 Back Up All TMs & Termbases…**.
  - The missing-text check now covers every Okapi format.
  - How each import gets its language pair, including the CafeTran, Trados review DOCX and Déjà Vu fixes.
  - TMX import rewritten with the real steps.
- **Workbench: the editor and QA pages.**
  - Find & Replace can change your TMs too (**Also in writable TMs**).
  - The Source and Target filter boxes take regular expressions (`/pattern/`).
  - The Preview text can be made larger or smaller.
  - The custom spellcheck dictionary can be imported, exported and tidied.
  - The QA menu lists its new items.
- **Workbench: SuperLookup.**
  - Adding your own web resources.
  - Text size for TM results.
  - Exporting the concordance hits.
  - The Direction filter, which no longer exists, is gone from the pages.
- **Workbench: the Language page** says what is translated now – about 1,100 strings, not the 180 of the first pass – and which languages are complete. It also says that the choice saves itself.
- **Workbench: QuickTrans, Voice, Clipboard, termbases and tools** were checked against v1.10.372:
  - **QuickTrans:** the popup's Source row and language combos, auto-fetch for AI providers, the full provider list, and the docked panel;
  - **Voice:** the Settings section is rewritten to match the tab – Always-On is Vosk only, dictation is always faster-whisper, and hold-to-talk is the default;
  - **Clipboard Manager:** snippet and clip right-click menus;
  - **termbases:** real buttons, columns and import format (TSV, with the Non-translatable column);
  - **tools:** the PDF Rescue, TMX Editor, Statistics and Superbrowser labels.
- **Workbench: the data-folder page** lists the settings files and the folders added since it was written. *Contributing* says the help pages live in this repository.
- **Workbench: older mistakes corrected along the way:**
  - the Theme page pointed to a Settings tab that doesn't exist;
  - the UI font scale is under View Settings;
  - the TermLens page still called Alt+0 a Compare Panel key and linked the old stand-alone TermLens plugin;
  - *Setting Up API Keys* described a Test Connection button and a Grok provider that Workbench doesn't have.

## 2026-09-30

- **memoQ: which version you have.** The *Updating* section says the version is in the editor's title bar, from v0.1.5.

## 2026-09-29

- **memoQ: updating from 0.1.0 or 0.1.1.** The *Updating* section says those versions have no update check, and how to tell (no *Check for updates* under Help), so nobody waits for an offer that cannot come. *Later* is described as it behaves – offered again the next time the editor opens, not "tomorrow".
- **memoQ 11 is supported.** The memoQ front page, the installation page's requirements and install steps, *After a memoQ upgrade* and troubleshooting say memoQ 11 and 12, and that the installer installs into every memoQ it finds from 11 up. *Installing by hand* explains the zip's `for-memoQ-11` folder, and why its native file must stay in its subfolder (from v0.1.3).
- **memoQ: updates.** The installation page's *Updating* section describes the daily check for a new version, the editor's offer and **Help → Check for updates**, the notice under Supervertaler's hits in memoQ, and what **Download and install** checks before it runs the installer (from v0.1.2).
- **memoQ: anonymous usage statistics and trial registration** (from v0.1.1). The editor page describes the new *Send anonymous usage statistics* setting and the question the editor asks once; the licensing page says what the trial registration sends and why.
- **memoQ: house rules are judged rule by rule.** The editor page no longer says the style rules always go. The client bank's brief, style guide and domain notes do; each house rule in `_shared` is judged in the job's one question by its **Scope:** line, and everything goes when the question cannot be asked (from v0.1.0). The bank-extracts path is now given as `C:\Users\<you>\Supervertaler\…`, not the author's own drive.
- **memoQ: installing from the direct download.** Step 1 of the installation page links `supervertaler.com/download/memoq`, which now starts the download of the latest installer. The requirements say that versions of memoQ before 12 have not been tested.
- **Trados: a startup that stops at "Start extensions are being executed...".** Troubleshooting has a new entry: on a new installation Supervertaler's first question could open behind Trados's startup screen, so Trados looked stuck. Pressing Enter gets past it, and from v18/19.20.198 the question opens in front.
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

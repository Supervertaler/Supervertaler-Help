---
title: "Terminology"
---

Supervertaler keeps your terminology in **termbases** – the same termbases Supervertaler for Trados and Supervertaler Workbench use, in one shared database – and uses them in two places at once: memoQ's terminology pane, and the AI's prompt.

### Why termbases, and not memoQ's own term bases

memoQ does not let a plugin read its own term bases. A term base attached to your project is visible to you and to memoQ's QA, but not to a machine-translation plugin – so a term marked forbidden in memoQ will not, on its own, stop the AI using it. memoQ confirmed this in September 2026: today the only route is their server API, and a new integration endpoint that will pass terminology to MT plugins is planned for around the start of 2027.

Supervertaler works around it by being a terminology source in its own right. Terms in its termbases reach the model because Supervertaler puts them there, and reach memoQ's grid and pane because Supervertaler is also a terminology provider memoQ consults.

### Where termbases live

One database, `C:\Users\<you>\Supervertaler\resources\supervertaler.db`, shared by all three Supervertaler products. A termbase you create in memoQ is there for Supervertaler for Trados the moment you press OK, and the other way round. If you own only Supervertaler for memoQ, the database is created the first time you make or import a termbase – you need nothing else.

What is *not* shared is which termbases a given product uses. Those choices are memoQ's own, kept in `C:\Users\<you>\Supervertaler\memoq\termbases.txt`, so ticking a termbase for a memoQ project changes nothing in Trados.

### The Termbases window

**memoQ → Termbases…** in the [prompt editor](/memoq/prompt-editor/), or click the **Termbases** row in its context bar. One row per termbase in the database, with four ticks:

| Tick | Scope | Meaning |
|---|---|---|
| **Read** | this memoQ project | Consult it: its terms highlight in the grid and appear in the pane. |
| **Project** | the termbase | This job's own termbase – at most one. Its hits are shaded darker, and it is where a term added from the grid or by Claude goes. |
| **CS** | the termbase | Match its terms case-sensitively. Useful for abbreviations. |
| **AI** | the termbase | Send its matched terms to the model. Without it a termbase is for your eyes only. |

Read is per project, which is why the project is named at the top of the window; the other three belong to the termbase and apply wherever it is used. The line under the table tallies what you have ticked – how many termbases, how many terms, whether one is the project's, how many reach the model.

The window opens on the project memoQ last sent a segment from. In a new project, translate one segment first, or the ticks would be filed against the previous job.

If you also use Supervertaler for Trados, the termbase it treats as the project termbase starts out ticked Project here, so you do not nominate it twice. It is a starting answer, not a link: change it here and memoQ keeps its own from then on.

**Read and AI are separate decisions on purpose.** A large general termbase is often worth *seeing* – every hit in the grid, every entry in the pane – without being worth *sending*: ten thousand generic renderings in a prompt crowd out the dozen that matter for this document. Tick Read on the big one and AI only on the project's.

### Making, filling and managing termbases

The buttons along the bottom of the Termbases window:

- **Terms…** – or double-click a termbase – opens its terms in a grid: source, target, a Forbidden tick and a note, with a filter box for the large ones. Type in the empty last row to add a term, edit a cell to correct one, select and remove one. OK writes everything, Cancel discards it. A pair the termbase already holds, either way round, is refused by name and the rest of your edits still go through.
- **New…** makes an empty termbase. You type the name and the two languages as codes – `nl`, `dut-NL`, `Dutch` all work – and the form says back what it understood.
- **Import…** makes a termbase from a file: a memoQ or Excel export, a Trados export, or one of the glossary files older versions of Supervertaler used. The file's own header supplies the name and languages where it has one, shown for correction before anything is written. See [Importing and exporting](/memoq/glossary-format/).
- **Add to…** pours a file into an existing termbase. If the file runs the other way round from the termbase it is turned; pairs already present, either way round, are skipped – the same rule Supervertaler for Trados applies, so the same file through either product leaves the same termbase.
- **Export…** writes a termbase out, as a Supervertaler glossary file or as a tab-separated file with a header row for a spreadsheet or for Trados.
- **Delete** removes the termbase, its terms and its synonyms – for Supervertaler for Trados and Workbench as well, since they share the database. It says so before it does it.

A termbase you make here is ticked Read for the current project as it is made.

### Setting it up in memoQ

**Options → Terminology plugins.**

1. Tick **Perform terminology plugin lookups while working in the translation grid**. Nothing happens until this is on.
2. Find **Supervertaler terms** in the list. It reads *Not configured* until at least one termbase is ticked Read for the current project – so tick one in the Termbases window first.
3. Tick **Enable plugin**. Its **Options** button opens the prompt editor, which is where terminology is managed.

That is all: a terminology plugin applies to every project, and does not appear in **Project home → Term bases**, which lists memoQ's own term bases only. Restart memoQ after enabling the plugin for the first time.

### What you get

**In the grid.** Matched terms are highlighted in the source segment in blue – darker for the project termbase, lighter for the others, so a project term is recognisable at a glance. A forbidden term gets a warning tint instead.

**In Translation results.** Each match is an entry showing the target term, the source term it matched, and which termbase answered – *Supervertaler · BEIJER*, or *· project termbase*. A forbidden term shows its wording struck through under *Do not use*, in black, which is what black means in memoQ.

**In the prompt.** From the termbases ticked AI only: approved terms are sent as the client's preferred wording, forbidden terms as absolute constraints. While an AutoPrompt-drafted prompt is selected, only the forbidden terms travel – the prompt's own locked table is the authority. See [A drafted prompt is the only source of terminology](/memoq/prompt-editor/#a-drafted-prompt-is-the-only-source-of-terminology).

**In the context bar.** The prompt editor's **Termbases** row summarises the selection – *BRANTS (project) + BEIJER · 1 of 2 to the model* – and opens the window when clicked.

**For Claude, if you use the [MCP server](/memoq/mcp-server/).** Every row your cursor lands on is looked up by this plugin whatever MT engine is selected, and Supervertaler remembers each one – so a document you pre-translated with Google or from TM alone still becomes visible to Claude as you walk through it. Claude can look terms up, and add a term straight into the project termbase: *"we agreed* draagarm *=* support arm *– add it"*.

### Adding a term without leaving the grid

Select a word, press **Alt+Up**, select its translation, press **Alt+Up** again. A small dialog opens with both halves filled in, a Forbidden tick and a note, naming the project termbase it is going into. Press **Add**, and the term is in the termbase at once – and in Supervertaler for Trados and Workbench with it. It shows in the grid and the pane the next time you move onto the segment: memoQ asks a terminology plugin about a segment once and keeps the answer, and gives a plugin no way to say the answer has changed. The dialog is your confirmation that it went in.

It is the same key Supervertaler for Trados uses for the same thing, and it does not mind which order you work in: a word selected in the target cell is recognised as the translation, so you may catch the English first and the Dutch after. After the first press a small note by the cursor shows what was caught and asks for the other half; it takes the focus from nothing, so you can carry on selecting. A second press on the same side replaces that half rather than pairing a word with itself.

The shortcut is live only while memoQ is the window in front. Everywhere else – Explorer, where Alt+Up is the parent folder – it is the key it has always been. Switch it off in the [prompt editor](/memoq/prompt-editor/) under **Settings → Alt+Up adds a term in memoQ**, which takes effect at once; the same tick is in memoQ’s own Supervertaler settings dialog.

If the pair is left half-finished it is forgotten after two minutes, and changing project drops it too, so a word caught in one job can never be written to another job's termbase.

**The other way in.** memoQ's own **Add Term** button on the ribbon, and its Ctrl+E shortcut, work with memoQ's term bases only – a terminology plugin is not among the choices they offer. The one door memoQ opens for a plugin is in the Translation results pane: select both words, right-click any Supervertaler hit, and choose **Add Selection As Alternative**. It ends in the same dialog and the same termbase. The hit you right-click is only the way in; what is added is what you selected.

If the project termbase runs the other way round from your project, the pair is turned to fit it. Nothing ticked Project? The dialog says so and where to fix it, rather than guessing at a background termbase.

### Preferred, not mandatory

Approved terms are given to the model as a strong steer it may override when an entry is clearly wrong for the sentence at hand.

That asymmetry is deliberate, and it comes from a real failure. A technical termbase may quite correctly render *applications* as *aanvragen* – in the sense of a filed application. Told to use terminology verbatim, the model translated "Mashup applications" as "Mashup-aanvragen", which is nonsense. A translator treats a termbase as guidance they may set aside with reason, and the model is asked to do the same.

**Forbidden terms are not softened.** They are stated as absolute, because that is what a forbidden term is for.

### Matching

Matching respects word boundaries, so `wire` does not match inside `wireless`. Where two entries could both match, the longer wins and the shorter one inside it is suppressed: `electric module` beats a bare `module`. Matching ignores case unless the termbase is ticked CS. A termbase stored the other way round from your project – English → Dutch on a Dutch → English job – is read backwards, so its terms are found all the same.

Very short entries are worth avoiding in a termbase you tick Read: a two-letter term fires on almost every segment and crowds out the terms that matter. A termbase of 12,000 terms loads in well under a second and adds under a millisecond to each lookup.

### Formats

See [Importing and exporting termbases](/memoq/glossary-format/).

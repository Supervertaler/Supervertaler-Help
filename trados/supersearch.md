---
title: "SuperSearch"
---

SuperSearch is a cross-file search and replace tool that lets you find text across **all SDLXLIFF files** in your Trados project -- not just the file you currently have open -- and, optionally, across the project's **translation memories** as well. It lives in its own dockable panel, so you can keep it visible while you translate.

Matching text is highlighted in yellow in the results grid, making it easy to spot exactly where the search term appears in each segment.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/549Ulc92FiU" title="SuperSearch in action – cross-file search across a Trados project" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Opening the Panel

There are three ways to open SuperSearch:

| Method          | Description                                                                |
| --------------- | -------------------------------------------------------------------------- |
| **View menu**   | Go to **View > SuperSearch**                                               |
| **Right-click** | Right-click in the editor and choose **SuperSearch** from the context menu |
| **Keyboard**    | Press **Alt+S**                                                            |

The panel docks at the bottom of the editor by default, but you can drag it anywhere -- left, right, floating, or even to a second monitor. Trados remembers the position between sessions.

:::note
**Prefer fewer panels?** You can host SuperSearch as a tab inside the Supervertaler Assistant panel instead of its own dockable panel. Go to **Settings > General > Panels** and tick **Show SuperSearch as a tab in the Supervertaler Assistant panel**, then restart Trados Studio. This requires a Supervertaler licence; without one, SuperSearch stays in its own panel.
:::

:::note
**Quick search from the editor:** Select a word or phrase in the source or target segment, then press **Alt+S** (or right-click > **SuperSearch**). The selected text is automatically entered in the search box and the search runs immediately.
:::

<figure><img src="/.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

## Searching

Type your search query in the text box and press **Enter** (or click **Search**).

### Search Modes

The **mode** dropdown in the search bar controls where SuperSearch looks:

| Mode              | Searches                                                                                          |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| **Everything**    | Project files, translation memories _and_ termbases, merged into one result list                  |
| **Project files** | The project's SDLXLIFF files                                                                       |
| **TMs**           | Only the project's translation memories — a concordance search, like Studio's built-in Concordance |
| **Termbases**     | Only your terminology — Supervertaler, MultiTerm (`.sdltb`) and Trados `.ttb` termbases *(v18.20.155)* |

The mode is remembered across sessions until you change it.

Translation-memory results are found via the project's attached file-based TMs (`.sdltm`) — read from the project settings and the project's `Tm` folder. Server-based (GroupShare) TMs are not searched. TM hits obey the same **Aa**, **.\***, and **Word** options as file results, and the **Scope** dropdown maps to source-side / target-side concordance.

The TM list is re-checked every time you search, so a TM you attach to the project mid-session is picked up without reopening the project. SuperSearch searches every attached TM regardless of its **Enabled** / **Concordance** state in the project's TM settings — use the **TMs** button (see below) to narrow the list.

### Searching your termbases *(from v18.20.155)*

*"Where does this phrase appear?"* and *"what have I called this term?"* are the same question at different granularities, so SuperSearch answers both. Terminology is searched alongside files and TMs in **Everything**, or on its own in **Termbases**.

All three kinds of termbase are included, with nothing extra to configure:

* **Supervertaler termbases** — every termbase in your shared database
* **MultiTerm** — the `.sdltb` termbases attached to the Trados project
* **Trados `.ttb`** — the Studio 2026 termbase format

Terminology is matched **in your project's direction**: a termbase declared the other way round (an EN→NL termbase in an NL→EN project) is oriented before matching, so the **Src** box always means *the language you translate from* — not "whichever column that particular termbase calls source". This is the same treatment TermLens gives your terminology.

Searches read the terminology TermLens already holds in memory, so a termbase search is effectively instant. (Immediately after opening a project TermLens may still be loading, in which case the first search falls back to reading the database and takes longer.)

Only the termbases you have **switched on** are searched — Supervertaler termbases with their **Read** tick set, and MultiTerm/`.ttb` termbases enabled in Trados Project Settings. The Read column is your statement of which terminology applies to the job in hand, so SuperSearch honours it rather than searching everything you own.

Termbase hits show the **termbase name in green** and its **kind** in the Status column (`Supervertaler`, `MultiTerm` or `TTB`).

:::note
TM and termbase results can be read and copied (via the preview pane) but cannot be navigated to or replaced — they are reference material, not document segments. The Replace bar is therefore disabled in **TMs** and **Termbases** mode. To change a term, edit it in the termbase.
:::

### Searching the web *(from v18.20.181)*

The one place a translator still had to leave Studio was the web. SuperSearch now covers that too: select a term, press **Alt+W**, and every reference site you have switched on opens with the query and your project's language pair already filled in. There is nothing to type and no language dropdown to set.

You can also right-click in the editor and choose **Search the web**, or use the **🌐** button in the SuperSearch bar.

:::note
**Alt+W is a second shortcut, not a replacement.** **Alt+S** still searches your files, TMs and termbases into the results grid exactly as before. **Alt+W** is the web half. Both can be rebound in Studio's keyboard shortcut settings.
:::

#### Choosing which sites to search

Click **Web (n)** in the SuperSearch bar — it sits beside **Files**, **TMs** and **TBs**, and works the same way. Forty-one sites ship with the plugin, of which five are on out of the box: **Beijerterm**, **IATE**, **Linguee**, **ProZ.com** and **Reverso**.

The other thirty-six cover bilingual dictionaries (Glosbe, WordReference, bab.la), EU and legal terminology (EUR-Lex, EuroTermBank, Juremy, GEMET), encyclopaedic sources (Wikipedia, Wiktionary, Wikidata), English monolingual and writing references (Collins, Merriam-Webster, Oxford Collocations, SkELL, Etymonline), Dutch resources (Woordenlijst, Synoniemen.net, de Financiële Begrippenlijst), medical databases (EMA, EMC) and general search (Google, Google Patents, GitHub Code).

Only five are enabled initially on purpose — forty tabs opening on your first search would be a poor introduction. Tick whichever you actually use.

**Adding your own** takes a name and a URL template: `{query}` for the search term, plus `{sl}` and `{tl}` for the language codes where the site needs them.

#### Where the results open

A checkbox in that same dialog decides. Neither option is a fallback for the other, and both are worth having:

* **In a Supervertaler window** — one window with a tab per site, reused for every search so tabs refresh in place rather than leaving a trail of windows behind. Tabs load only when you click them.
* **In your own browser** — one new window containing all the tabs, which you close when you are done. Your browser brings your ad blocker and your signed-in sessions with it.

#### Terms taken from the target side

A term selected in the **target** is looked up **in the target language**. Searching a Dutch word in an EN→NL project queries the sites as nl→en, not en→nl — the latter is how you get a screen of nothing and conclude the site is broken.

#### Sites that ask you to prove you are human

Some sites, ProZ.com in particular, block embedded browsers. When that happens the tab shows a banner offering to hand the page to your own browser, where you are usually signed in and pass instantly. It is an offer rather than an automatic jump, so nothing pulls you out of the editor mid-segment — and if the check clears by itself, the page is still there underneath.

### Search Options

| Option             | Description                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------- |
| **Scope** dropdown | Choose _Source & Target_ (default), _Source only_, or _Target only_                         |
| **Aa** checkbox    | Case-sensitive search -- when unchecked, "Hello" matches "hello", "HELLO", etc.             |
| **.\*** checkbox   | Treat the query as a regular expression (see [Regex tips](/trados/supersearch/#regex-tips) below) |
| **Word** checkbox  | Match whole words only -- "cat" won't match "category" or "scatter". Ignored when **.\*** is on |

SuperSearch displays all matching segments in the results grid. The status bar shows the number of results, what was searched (files and/or TMs), and how long the search took.

### Results Grid

Each row shows one matching segment, one TM entry, or one termbase entry:

| Column      | Description                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------- |
| **Found in** | The project-file name, the translation-memory name (blue), or the termbase name (green). Hover for the full path |
| **#**       | Segment number within the file; for TM results, the concordance match score; empty for termbase entries |
| **Source**  | Source text -- matching text is highlighted in yellow                                             |
| **Target**  | Target text -- matching text is highlighted in yellow                                             |
| **Status**  | Confirmation status (Not Translated, Draft, Translated, etc.), "TM" for TM results, or the termbase kind (`Supervertaler`, `MultiTerm`, `TTB`) for terminology |

### Preview Pane

Below the results grid is a preview pane showing the **full source and target text** of the selected result, side by side, with the match highlighted in yellow. This is handy when a segment is too long to read in its grid row. Click any result row to update the preview, and drag the splitter bar between the grid and the preview pane to resize it.

The text in both preview boxes is **selectable**: drag to select, press **Ctrl+C** to copy, or right-click for a menu with **Copy**, **Select All**, **Copy source**, and **Copy target**. This makes it easy to reuse a previous translation verbatim -- select the target phrase and paste it straight into your active segment.

## File, TM and Termbase Selection

Four buttons in the search bar let you narrow what SuperSearch looks at — **Files** for the project's SDLXLIFF files, **TMs** for the project's translation memories, **TBs** for your termbases *(v18.20.155)*, and **Web** for reference sites *(v18.20.181)*. Each button shows how many items are included:

* **Files (16)** -- all 16 files in the project are included
* **Files (12/16)** -- 12 out of 16 files are included (4 excluded)
* **TMs (3)** -- all 3 project TMs are included
* **TMs (1/3)** -- 1 of 3 TMs is included (2 excluded)
* **TBs (2)** -- both available termbases are included
* **Web (5/41)** -- 5 of the 41 available web resources are switched on

Files, TMs and termbases are all discovered when the project opens, so the counts are filled in before your first search. Web resources are your own standing choice rather than a property of the project, so that count is the same in every job until you change it.

Click any button to open its selection dialog:

1. A list shows all the files (or TMs, or termbases) found, with checkboxes
2. **Check** the items you want to include in the search
3. **Uncheck** the items you want to exclude
4. Use **Select All** or **Select None** to quickly toggle everything
5. Click **OK** to apply

The **Files** filter applies in **Project files** and **Everything** modes; the **TMs** filter applies in **TMs** and **Everything** modes; the **TBs** filter applies in **Termbases** and **Everything** modes.

Termbases are listed as *name (kind)* — for example `BEIJER (Supervertaler)` — so two termbases that share a name remain distinguishable.

:::note
These selections persist for the current session. When you switch to a different project, all files, TMs and termbases are included again by default.
:::

## Navigating to a Segment

**Double-click** a row (or select it and press **Enter**) to jump to that segment in the editor.

* If the segment is in the **currently active file**, Trados navigates to it directly.
* If the segment is in a **different file**, SuperSearch attempts to switch to that file and navigate to the segment. If the file is not loaded in the editor, you may need to open it first.
* **TM results** can't be navigated to — they aren't document segments. Double-clicking a TM row just reminds you to use the preview pane to copy the text.

## Find & Replace

Tick the **Replace** checkbox to reveal the replace bar. Replace always operates on **target text only** -- source text is never modified.

| Action          | Description                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Replace**     | Replaces the match in the currently selected result. The segment must be in the active file -- double-click it first to navigate there. |
| **Replace All** | Replaces all target matches across all files. A confirmation dialog shows how many segments in how many files will be affected.         |

### How Replace All works

* For the **active file**: changes go through the Trados API, so they appear immediately and are tracked in Trados's undo history.
* For **other files**: the SDLXLIFF XML is modified directly on disk. You need to reopen those files to see the changes.

:::caution
**Replace All cannot be undone** for files modified on disk. Always review the search results carefully before replacing. Consider saving your project first.
:::

:::note
Replace respects the same **Aa** (case sensitivity) and **.\*** (regex) settings as search. When using regex, you can use capture groups in the replacement (e.g., `$1`, `$2`).
:::

### Matches that span inline tags are skipped

Trados segments often contain inline tags – formatting marks, placeholders, field codes – that interrupt a run of plain text. If your search string would only match across one of these tag boundaries (for example, searching for `important thing` when the segment renders as `important<bold>thing</bold>`), Replace and Replace All will **skip that segment** rather than apply a destructive flatten-and-rewrite that would lose the tag.

You'll see this in the status bar after a Replace All as `…, skipped N (match spans inline tags)`. The skipped segments are left untouched so the formatting survives; you can edit them manually if you want the replacement to happen.

This applies to both the active-file path (Trados API replacements) and the on-disk path (SDLXLIFF XML rewrites). It only kicks in when the match genuinely straddles a tag – ordinary matches inside a single text run are replaced normally and tags are preserved.

## Regex Tips

When the **.\*** checkbox is enabled, the search query is treated as a .NET regular expression. Some useful patterns:

| Pattern          | Matches                                             |
| ---------------- | --------------------------------------------------- |
| `\bword\b`       | "word" as a whole word (not "keyword" or "wording") |
| `(word1\|word2)` | Either "word1" or "word2"                           |
| `\d+`            | One or more digits                                  |
| `"[^"]*"`        | Anything inside double quotes                       |
| `\s{2,}`         | Two or more consecutive whitespace characters       |

:::note
Regex replace supports capture groups. For example, search for `(\w+)\s+(\w+)` and replace with `$2 $1` to swap two words.
:::

## Keyboard Shortcuts

| Shortcut                      | Action                                          |
| ----------------------------- | ----------------------------------------------- |
| **Alt+S**                     | Open SuperSearch (with selected text, if any)   |
| **Alt+W**                     | Search the web for the selected term            |
| **Enter** (in search box)     | Start search                                    |
| **Enter** (in results grid)   | Navigate to selected segment                    |
| **Double-click** (result row) | Navigate to selected segment                    |

## Tips

* Select a term in the editor and press **Alt+S** to instantly search for it across the entire project — or **Alt+W** to look it up on IATE, Linguee, Reverso and the rest, in your project's language pair.
* Use **Source only** scope to find segments where a particular term appears, then check how it was translated across files.
* Use **Target only** scope with Replace to fix a consistent mistranslation across the entire project.
* Use the **Files** and **TMs** buttons to limit the search to specific files or translation memories -- useful in large projects where you only want to search a subset.
* Switch the mode dropdown to **TMs** to use SuperSearch as a concordance tool, **Termbases** to search your terminology, or **Everything** to see project, TM and termbase hits side by side.
* The status bar shows the number of results, what was searched, and the search time in milliseconds.
* You can resize columns by dragging the column header borders.

## See Also

* [Supervertaler](/trados/ai-assistant/) -- AI-powered chat and context
* [Batch Operations](/trados/batch-operations/) -- Batch translate and proofread
* [Keyboard Shortcuts](/trados/keyboard-shortcuts/) -- All shortcuts in one place

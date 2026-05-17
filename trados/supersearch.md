---
title: "SuperSearch"
---

:::note
You are viewing help for 🧩 **Supervertaler for Trados** – the Trados Studio plugin. Looking for help with the standalone app? Visit 🖥️ [Supervertaler Workbench help](https://supervertaler.gitbook.io/help/get-started-1/workbench/).
:::

{% embed url="https://youtu.be/549Ulc92FiU" %}
SuperSearch in action – cross-file search across a Trados project
{% endembed %}

SuperSearch is a cross-file search and replace tool that lets you find text across **all SDLXLIFF files** in your Trados project -- not just the file you currently have open -- and, optionally, across the project's **translation memories** as well. It lives in its own dockable panel, so you can keep it visible while you translate.

Matching text is highlighted in yellow in the results grid, making it easy to spot exactly where the search term appears in each segment.

## Opening the Panel

There are three ways to open SuperSearch:

| Method          | Description                                                                |
| --------------- | -------------------------------------------------------------------------- |
| **View menu**   | Go to **View > SuperSearch**                                               |
| **Right-click** | Right-click in the editor and choose **SuperSearch** from the context menu |
| **Keyboard**    | Press **Alt+S**                                                            |

The panel docks at the bottom of the editor by default, but you can drag it anywhere -- left, right, floating, or even to a second monitor. Trados remembers the position between sessions.

:::note
**Prefer fewer panels?** You can host SuperSearch as a tab inside the Supervertaler Assistant panel instead of its own dockable panel. Go to **Settings > General > Panels** and tick **Show SuperSearch as a tab in the Supervertaler Assistant panel**, then restart Trados Studio. This requires a Supervertaler Assistant licence; without one, SuperSearch stays in its own panel.
:::

:::note
**Quick search from the editor:** Select a word or phrase in the source or target segment, then press **Alt+S** (or right-click > **SuperSearch**). The selected text is automatically entered in the search box and the search runs immediately.
:::

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

## Searching

Type your search query in the text box and press **Enter** (or click **Search**).

### Search Modes

The **mode** dropdown in the search bar controls where SuperSearch looks:

| Mode              | Searches                                                                                          |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| **Project files** | The project's SDLXLIFF files (the default — original SuperSearch behaviour)                       |
| **Files + TMs**   | The project files _and_ the project's translation memories, merged into one result list          |
| **TMs only**      | Only the project's translation memories — a concordance search, like Studio's built-in Concordance |

The mode is remembered across sessions until you change it.

Translation-memory results are found via the project's attached file-based TMs (`.sdltm`) — read from the project settings and the project's `Tm` folder. Server-based (GroupShare) TMs are not searched. TM hits obey the same **Aa**, **.\***, and **Word** options as file results, and the **Scope** dropdown maps to source-side / target-side concordance.

The TM list is re-checked every time you search, so a TM you attach to the project mid-session is picked up without reopening the project. SuperSearch searches every attached TM regardless of its **Enabled** / **Concordance** state in the project's TM settings — use the **TMs** button (see below) to narrow the list.

:::note
TM results can be read and copied (via the preview pane) but cannot be navigated to or replaced — they are reference material, not document segments. In **TMs only** mode the Replace bar is therefore disabled.
:::

### Search Options

| Option             | Description                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------- |
| **Scope** dropdown | Choose _Source & Target_ (default), _Source only_, or _Target only_                         |
| **Aa** checkbox    | Case-sensitive search -- when unchecked, "Hello" matches "hello", "HELLO", etc.             |
| **.\*** checkbox   | Treat the query as a regular expression (see [Regex tips](supersearch.md#regex-tips) below) |
| **Word** checkbox  | Match whole words only -- "cat" won't match "category" or "scatter". Ignored when **.\*** is on |

SuperSearch displays all matching segments in the results grid. The status bar shows the number of results, what was searched (files and/or TMs), and how long the search took.

### Results Grid

Each row shows one matching segment (or, in a TM mode, one TM entry):

| Column      | Description                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------- |
| **File/TM** | The project-file name, or — for TM results — the translation-memory name, shown in blue. Hover for the full path |
| **#**       | Segment number within the file; for TM results, the concordance match score                      |
| **Source**  | Source text -- matching text is highlighted in yellow                                             |
| **Target**  | Target text -- matching text is highlighted in yellow                                             |
| **Status**  | Confirmation status (Not Translated, Draft, Translated, etc.), or "TM" for TM results             |

### Preview Pane

Below the results grid is a preview pane showing the **full source and target text** of the selected result, side by side, with the match highlighted in yellow. This is handy when a segment is too long to read in its grid row. Click any result row to update the preview, and drag the splitter bar between the grid and the preview pane to resize it.

The text in both preview boxes is **selectable**: drag to select, press **Ctrl+C** to copy, or right-click for a menu with **Copy**, **Select All**, **Copy source**, and **Copy target**. This makes it easy to reuse a previous translation verbatim -- select the target phrase and paste it straight into your active segment.

## File and TM Selection

Two buttons in the search bar let you narrow what SuperSearch looks at — **Files** for the project's SDLXLIFF files, and **TMs** for the project's translation memories. Each button shows how many items are included:

* **Files (16)** -- all 16 files in the project are included
* **Files (12/16)** -- 12 out of 16 files are included (4 excluded)
* **TMs (3)** -- all 3 project TMs are included
* **TMs (1/3)** -- 1 of 3 TMs is included (2 excluded)

Click either button to open its selection dialog:

1. A list shows all the files (or TMs) found in the project, with checkboxes
2. **Check** the items you want to include in the search
3. **Uncheck** the items you want to exclude
4. Use **Select All** or **Select None** to quickly toggle everything
5. Click **OK** to apply

The **Files** filter applies in **Project files** and **Files + TMs** modes; the **TMs** filter applies in **Files + TMs** and **TMs only** modes.

:::note
Both selections persist for the current session. When you switch to a different project, all files and all TMs are included again by default.
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

| Shortcut                      | Action                                        |
| ----------------------------- | --------------------------------------------- |
| **Alt+S**                     | Open SuperSearch (with selected text, if any) |
| **Enter** (in search box)     | Start search                                  |
| **Enter** (in results grid)   | Navigate to selected segment                  |
| **Double-click** (result row) | Navigate to selected segment                  |

## Tips

* Select a term in the editor and press **Alt+S** to instantly search for it across the entire project.
* Use **Source only** scope to find segments where a particular term appears, then check how it was translated across files.
* Use **Target only** scope with Replace to fix a consistent mistranslation across the entire project.
* Use the **Files** and **TMs** buttons to limit the search to specific files or translation memories -- useful in large projects where you only want to search a subset.
* Switch the mode dropdown to **TMs only** to use SuperSearch as a concordance tool, or **Files + TMs** to see project and TM hits side by side.
* The status bar shows the number of results, what was searched, and the search time in milliseconds.
* You can resize columns by dragging the column header borders.

## See Also

* [Supervertaler Assistant](ai-assistant.md) -- AI-powered chat and context
* [Batch Operations](batch-operations.md) -- Batch translate and proofread
* [Keyboard Shortcuts](keyboard-shortcuts.md) -- All shortcuts in one place

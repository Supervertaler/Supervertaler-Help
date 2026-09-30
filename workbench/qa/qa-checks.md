---
title: "QA Checks"
---

**QA → 🔎 Run QA Checks…** runs a set of saved checks over the whole project and lists everything they find: double spaces, doubled words, a space before a full stop, a deprecated term, the wrong decimal separator, or any other pattern you care about. Think of it as a linter for your translation. The checks only *find*; nothing in the project is changed.

The same window can also check that every translated segment has the same **inline tags and codes** as its source (see [Tags & codes](#tags--codes) below).

## How QA checks work

A QA check is an ordinary [Find & Replace](/workbench/editor/find-replace/) operation with its **QA** box ticked. That means:

- Checks live in **F&R Sets**, in the Find & Replace dialog. You can keep several sets, for example a "patent QA" set and a "marketing QA" set.
- A check can be plain text, **Whole words**, **Entire segment** or a **Regex** (regular expression), in the source, the target or both, and case-sensitive or not – exactly the options Find & Replace has.
- Sets are shared the same way as other F&R Sets: **📤 Export** and **📥 Import** of `.svfr` files.
- **▶ Run All** in F&R Sets never runs a QA check as a replacement. A check usually has an empty "Replace with", which would otherwise delete every match.

## The starter set

If you have no checks yet, click **➕ Add basic checks** in the QA Checks window. It creates a set called **QA - basic checks** with four checks switched on, all on the target side:

- Double space
- Space before a full stop or comma
- Doubled word (such as "the the")
- Space inside brackets

Three more checks are included but switched off, because they are useful only for some jobs:

- Space at the start or end
- Repeated punctuation (this also catches "...")
- Straight quote (where curly quotes are wanted)

To switch one on, open **Edit → Find…** (`Ctrl+F`), expand the F&R Sets panel, select **QA - basic checks** and tick the **✓** box in front of the check. The **➕ Add basic checks** button disappears once the set exists.

## Adding your own checks

1. Open **Edit → Find…** (`Ctrl+F`).
2. Type what to look for in **Find what**, and set **Search in**, **Match**, **Case sensitive** and **Regex** as needed. Leave **Replace with** empty.
3. Click **Find all** to try the check out on the project.
4. Expand the **F&R Sets** panel, select a set (or create one with **+ New Set**) and click **+ Add Current to Set**.
5. In the list of operations, tick the **QA** box for the new check.

To change a check later, edit its text in the **Find** column of the list, or double-click it to load it back into the fields above. Untick its **✓** box to leave it out of the QA run without deleting it.

:::tip
A few useful patterns, with **Regex** ticked: ` {2,}` (two or more spaces), `\s+$` (trailing spaces), `\d\s+%` (a space between a number and a percent sign). For a term the client no longer wants, type the word and choose **Match: Whole words** – no regex needed.
:::

## Running the checks

1. Choose **QA → 🔎 Run QA Checks…**.
2. Pick a set under **Check set**. Only sets that contain at least one switched-on QA check are listed, with the number of checks in each.
3. Click **▶ Run**.

The window stays open while you work, so you can fix things in the grid and click **▶ Run** again to refresh the list.

:::note
If you change a set in Find & Replace while the QA Checks window is open, choose **QA → 🔎 Run QA Checks…** again to pick up the change.
:::

## The results list

Each finding is one row:

| Column | What it shows |
|--------|---------------|
| **Segment** | The segment number |
| **Check** | The check that found it: its name for the starter checks, its Find pattern for your own |
| **In** | **Source** or **Target** |
| **Found** | The text that matched, with spaces shown as `·` so stray spaces are visible |
| **Context** | The text around the match, with the match itself in `[brackets]` |

- **Double-click** a finding to go to its segment in the grid.
- Click a column header to sort by it.
- The line under the list says how many findings there are, in how many segments. A check with a regular expression that isn't valid is named there in red, and the other checks still run.
- **💾 Export…** saves the findings as a CSV file, for example to send to a reviewer.

## Tags & codes

Tick **Tags & codes match the source** (it is on by default) to also compare each translated segment's inline tags with its source. This lists:

- **Tag/code missing from the target** – a tag the source has but the translation lost;
- **Tag/code not in the source** – a tag in the translation that its source doesn't have.

It covers the usual inline tags (`<b>`, `</b>`, `<1>`, `[2}`, `{2]` and so on) and also your own inline codes: the placeholders such as `{playerName}` or `%s` that you describe under [Settings → 🏷️ Inline Codes](/workbench/settings/inline-codes/). Tags are counted, so a tag that appears twice in the source but only once in the translation is reported too. Segments with no translation yet are skipped.

:::note
The check recognises tags in angle brackets – including self-closing ones such as the `<2/>` of Trados and SDLXLIFF imports, `<br/>` and memoQ's `<mq:ch …/>` (from v1.10.373) – and memoQ's bracket tags (`[2}`, `{2]`). Numbered placeholders in curly brackets, such as Phrase's `{1}`, are included only when one of your inline code patterns matches them. The ready-made **{placeholder}** pattern under **➕ Common patterns** covers `{1}`.
:::

You don't need any saved checks for this: if you have no QA check sets yet, **▶ Run** runs the tag and code check on its own. Untick the box when you only want your saved checks.

See also [Tag Validation](/workbench/qa/tag-validation/).

## Related

- [Find & Replace](/workbench/editor/find-replace/) – where checks are created and stored
- [Check with LanguageTool](/workbench/qa/languagetool/) – grammar, spelling and style
- [Spellcheck](/workbench/qa/spellcheck/) · [AI Proofreading](/workbench/qa/proofreading/)

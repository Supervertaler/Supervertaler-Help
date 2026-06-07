---
title: "Find & Replace"
---

Supervertaler's Find & Replace feature helps you quickly find text and make consistent changes across your translation.

## Opening Find & Replace

- Press `Ctrl+F` or `Ctrl+H`
- Or go to **Edit → Find & Replace**

## Dialog layout

The action buttons are grouped to make destructive actions visually distinct from non-destructive ones. Reading left to right:

- **Find next | Find all | Highlight all | Clear highlights** – non-destructive: searching and highlighting only, no edits made.
- A vertical separator marks the boundary.
- **Replace this | Replace all** – destructive: these modify your translation. They appear with an **amber background** as a visual cue that clicking them changes the document.

The Close button sits at the far right.

### Keyboard shortcuts inside the dialog

| Key | Where | Action |
|---|---|---|
| **Enter** | in the Find field | Triggers **Find next** |
| **Enter** | in the Replace field | Triggers **Replace all** (the existing confirmation prompt still appears first) |
| **Escape** | anywhere | Closes the dialog |

The Enter-in-Replace shortcut is intentional: the Replace all confirmation dialog catches accidental presses, so pressing Enter never silently overwrites your translation.

## Basic Usage

### Finding Text

1. Type your search term in the **Find** field
2. Click **Find all** to see all matches, or press **Enter** for Find next
3. Matches are highlighted in yellow in the grid
4. The results counter shows how many matches were found

### Replacing Text

1. Type your search term in the **Find** field
2. Type your replacement in the **Replace** field
3. Click the amber **Replace all** button, or press **Enter** while the Replace field has focus
4. Confirm the replacement count when the dialog asks
5. A confirmation shows how many replacements were made

## Search Options

### Match

Three mutually exclusive modes (radio buttons):

| Mode | Description |
|------|-------------|
| **Anything** | Matches the search term anywhere in the text (the default) |
| **Whole words** | Matches the search term only as a complete word |
| **Entire segment** | Matches only when the whole segment equals the search term |

### Case sensitive

- ✅ **On**: "Hello" won't match "hello"
- ❌ **Off** (default): "Hello" matches "hello", "HELLO", etc.

### Auto-adjust case

When replacing, adjusts the replacement to match the case pattern of each match — ALL CAPS → uppercased, all lower → lowercased, Title Case → title-cased. It has no effect when **Case sensitive** is on, and is ignored in **Regex** mode.

### Search in

| Scope | Description |
|-------|-------------|
| **Source** | Search the source column |
| **Target** (default) | Search the translations |
| Both | Tick both boxes to search source and target |

### Reset edited to Draft

When a replacement changes a target segment that was **Confirmed**, **Proofread** or **Approved**, that segment is reset to **Draft**, so the segments Find & Replace touched are easy to spot and re-check afterwards.

- ✅ **On** (default): edited finished segments drop back to Draft.
- ❌ **Off**: segments keep their existing status.

This applies to **Replace this**, **Replace all** and **F&R Sets** batch runs. Only segments whose text actually changes are affected, and replacing in the source column never changes a status. The setting is remembered between sessions, and `Ctrl+Z` restores the original text and status together.

## Regular expressions

Tick **Regex** to treat the Find field as a regular expression (Python `re` syntax).

- **Backreferences in Replace:** capture groups in the pattern can be reused in the Replace field as `\1`, `\2`, … (or `\g<name>` for named groups). For example, Find `"([^"]+)"` and Replace `«\1»` turns `"events"` into `«events»`.
- **Case sensitive** still applies (off = the whole pattern matches case-insensitively).
- While Regex is on, the **Match** modes and **Auto-adjust case** don't apply and are greyed out.
- **Invalid patterns are caught:** an unbalanced pattern (e.g. `(`) or a bad backreference (e.g. `\9` with no matching group) shows a clear error and changes nothing — it never crashes or partially replaces.

:::tip
A few handy patterns: `\s+` (runs of whitespace), ` {2,}` (two or more spaces), `\b(\w+)\s+\1\b` (doubled words like "the the"), ` +$` (trailing spaces).
:::

## History Dropdowns

Both the Find and Replace fields remember your recent searches:

- Click the dropdown arrow to see your last 20 entries
- Start typing to filter the history
- History persists between sessions

## F&R Sets (Batch Operations)

Save and reuse multiple find/replace operations as a set.

### Creating a Set

1. Expand the **📁 F&R Sets** panel
2. Click **➕ New Set**
3. Give your set a name (e.g., "Client Style Guide")
4. The set appears in the dropdown

### Adding Operations to a Set

1. Enter your Find and Replace terms
2. Set your options (Match mode, Case sensitive, Regex, Search in) — these are all saved with the operation
3. Click **➕ Add Current to Set**
4. The operation is saved to the active set

### Managing Operations

In the F&R Sets panel:
- **✓ (Enabled) column** – tick to include an operation when you click **Run All**; untick to skip it. (Hover for a reminder.)
- **Edit** – double-click an operation to load it back into the Find/Replace fields.
- **🗑 Delete Operation** – removes the selected operation from the set.
- **🗑 Delete Set** – removes the selected set entirely.

The **Match** column shows each operation's mode, or **Regex** when the operation is a regular expression.

### Running a Batch

1. Select your set
2. Click **▶ Run All**
3. Each enabled operation runs in turn; regex operations (shown as "Regex" in the Match column) run with backreferences
4. See how many replacements were made

:::caution
**An empty "Replace with" deletes matches.** An operation with a blank Replace field replaces every match with nothing — i.e. it deletes the matched text. If a set contains any such operation, Run All lists them and defaults the confirmation button to **No**, so you don't wipe text by accident.
:::

### Importing & exporting sets

Share sets with colleagues:
- **📤 Export** – save the selected set as a `.svfr` file
- **📥 Import** – load a shared `.svfr` file

## Use Cases

### Terminology Consistency

Create a set for client-specific terms:
- "colour" → "color" (US spelling)
- "organisation" → "organization"
- "programme" → "program"

### Style Guide Rules

Enforce style guidelines:
- Double spaces → Single space
- "e.g." → "for example"
- Straight quotes → Curly quotes

### Post-Translation Cleanup

Clean up common MT artifacts:
- Remove unwanted spaces before punctuation
- Fix capitalization issues
- Normalize formatting

## Tips

:::tip
**Pro Tip:** Use regex mode for complex patterns. For example, `\s+` matches any whitespace to clean up extra spaces.
:::

:::note
**Undo Support:** All replacements can be undone with `Ctrl+Z` (within the same session).
:::

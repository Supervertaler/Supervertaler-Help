---
title: "Glossary Format"
---

A plain text file, tab-separated, one term per line.

```
elektrische module	electric module
elektrische module	electrical module	forbidden
koppelmechanisme	coupling mechanism
```

| Column | |
|---|---|
| 1 | source term |
| 2 | target term |
| 3 | *optional* — `forbidden` marks a target that must not be used |

Blank lines are ignored, and so is any line starting with `#`, so the file can carry comments.

:::caution[Tabs, not spaces]
Columns must be separated by actual tab characters. This is the commonest reason a glossary loads with no terms. The options dialog reports how many terms it parsed — check that number after choosing a file.
:::

### Matching

Matching is case-insensitive and respects word boundaries, so `wire` does not match inside `wireless`. Where two entries could both match, the longer wins and the shorter one inside it is suppressed: `electric module` beats a bare `module`.

### Editing while you work

The file is re-read whenever you save it. Keep it open in a text editor beside memoQ, add a term, save, and the next segment sees it — no restart, no reloading the project.

### Size

A real term base export works fine. A 9,000-term glossary loads in well under a tenth of a second and adds under a millisecond to each lookup.

Because matching is case-insensitive, very short entries are worth avoiding: a two-letter term fires on almost every segment and crowds out terms that matter.

### Converting an existing term base

The plugin repository includes a converter for Supervertaler Workbench term base exports:

```bash
python tools/convert_termbase.py BEIJER.tsv BEIJER-glossary.txt
```

It handles the quoting and pipe-separated variants of the export format, drops entries that translate to themselves, and reports what it skipped.

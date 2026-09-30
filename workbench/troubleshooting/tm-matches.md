---
title: "TM Matches Not Appearing"
---

Your TM is full of relevant entries, it opens fine in **✏️ Edit/Maintain TM**,
and still the match panel stays empty. Work through the checks below in order –
the first two explain most cases. If you're still stuck, the
[diagnostic script](#run-the-diagnostic-script) tells you which one it is.

## 1. Is the TM switched on for this project?

A TM gives matches only when its **Read** box is ticked for the open project, and
a new project starts with every TM switched off, so that a new job doesn't
quietly pick up the last job's resources.

1. Open the **💾 TMs** tab.
2. Tick **Read** for the TM(s) you want to use (and **Write** if new
   translations should be saved into one).

When no TM is switched on, the log says so once per project: "No TM is switched
on for this project, so no TM matches can be shown." You'll find the log under
**Settings → 📋 Log**, or in its own window via **Tools → 📋 Log Window…**.

## 2. Does the project have the right language pair?

TM matches are looked up for the project's source and target language. A project
created with the wrong pair finds nothing, even though the TM itself looks
perfectly fine.

- See the project's pair under **Project → 📋 Project Info…** (**Languages**).
- Compare it with the **Languages** column in the **💾 TMs** tab.

Some imports in older versions could create a project with the wrong pair
without telling you:

| Import | Problem | Fixed in |
| --- | --- | --- |
| **CafeTran** bilingual DOCX | Every project became English → Dutch | v1.10.372 |
| **Déjà Vu X3** bilingual RTF | Dutch → Spanish when no languages were found in the file | v1.10.372 |
| **memoQ** bilingual RTF | Dutch → English when the header row couldn't be read | v1.10.372 |
| **memoQ** bilingual DOCX | English → Dutch when the column headers weren't recognised | v1.10.370 |
| **memoQ** XLIFF | Language "unknown" when the file declared none | v1.10.370 |

Current versions read the pair from the file where they can, and ask you to
confirm or pick it where they can't – see
[CAT Tool Integration Overview](/workbench/cat-tools/overview/#the-language-pair).
To fix a project that was created with the wrong pair, import the file again and
choose the right languages. If you've already translated in it, export the
bilingual file first and import that one: the bilingual imports bring existing
translations along.

:::note
**TMs with upper-case language codes.** Before v1.10.370, TM entries tagged with
a bare upper-case language code such as `IT` (as some older TMX files spell it)
could never be found by any project. This mostly affected TMs imported before
v1.10.253. Language codes are now compared regardless of case, so these entries
match as soon as you update – nothing needs re-importing.
:::

## 3. Exact matches appear, but never fuzzy ones

Fuzzy matches are found through a full-text index inside the TM database; exact
(100%) matches don't use it. If that index stops working, exact matches carry on
as normal, **✏️ Edit/Maintain TM** still lists every entry, and yet no fuzzy
match ever appears – with no error anywhere.

Since v1.10.371, Supervertaler tests the index each time it starts and rebuilds
it if it can't find its own entries. The log then shows:

```
[TM] The full-text index cannot find its own rows, so fuzzy matches would come back empty. Rebuilding it from 200,000 translation units - this may take a moment.
[TM] Full-text index rebuilt; fuzzy matching is working again.
```

The rebuild takes a few seconds on a large TM (about 2.6 seconds for 200,000
entries), so that one start-up may take a little longer.

**Fix:** update to v1.10.371 or later and restart Supervertaler. If you can't
update yet, the [diagnostic script](#repairing-the-index-with-the-script) can do
the same repair.

## 4. Look in the log for "TM search failed"

Before v1.10.371, a match search that failed – because of a locked database, a
damaged index or a bad language value, for example – simply showed an empty
match panel, exactly as if the TM had nothing to offer. Now the log says so and
names the cause:

```
⚠️ TM search failed, so the match pane is empty: <the reason>
   This is a fault, not an empty TM. Run scripts/sv_tm_diagnose.py for details.
```

If you see this, run the diagnostic script below and include both in your report.

## Run the diagnostic script

`sv_tm_diagnose.py` is a small Python script that looks at your TM database and
your most recent projects and tells you why matches are missing. By default it
only reads: it opens the database read-only and changes nothing.

It isn't included in the Windows download. You need **Python 3** installed (the
script uses only Python's standard library, so there's nothing else to install).

1. Download
   [`sv_tm_diagnose.py`](https://github.com/Supervertaler/Supervertaler-Workbench/blob/main/scripts/sv_tm_diagnose.py)
   from GitHub (use the **Download raw file** button). If you run Supervertaler
   from source, it's already in the `scripts` folder.
2. Open a command prompt (Terminal on macOS and Linux) in the folder where you
   saved it.
3. Run:

   ```bash
   python sv_tm_diagnose.py
   ```

   (On Windows, use `py sv_tm_diagnose.py` if `python` isn't recognised.)

The script finds `supervertaler.db` in the `Supervertaler` folder in your home
folder, and checks the most recently saved of your projects there and in
`Documents`. If your [data folder](/workbench/reference/data-folder/) is
somewhere else, or you want to check a different project, give both paths, the
database first:

```bash
python sv_tm_diagnose.py "D:\Supervertaler\resources\supervertaler.db" "D:\Jobs\Manual\Manual.svproj"
```

### What it reports

- your Workbench version, operating system, Python and SQLite version;
- the language pair of the project, and which TMs have **Read** ticked for it;
- the language pairs actually stored on the entries of each TM, and whether the
  project can see them;
- whether the full-text index can find entries that are known to exist;
- a **Verdict**, which is one of:
  - *No TM is switched on for this project* – see [check 1](#1-is-the-tm-switched-on-for-this-project);
  - *The full-text index is dead: fuzzy matches cannot work, exact ones can* – see [check 3](#3-exact-matches-appear-but-never-fuzzy-ones);
  - *No active TM entry matches the project's languages* – see [check 2](#2-does-the-project-have-the-right-language-pair);
  - *TMs are on, languages line up and the index works* – then look in the log for "TM search failed" ([check 4](#4-look-in-the-log-for-tm-search-failed)).

When you ask for help, please send the **entire output**.

### Repairing the index with the script

```bash
python sv_tm_diagnose.py --repair
```

With `--repair`, the script rebuilds the full-text index in place – but only if
it found it dead – and then tests it again. If the index is working, nothing is
changed. You can combine `--repair` with the two paths above.

:::caution
`--repair` writes to your TM database. Close Supervertaler (and Supervertaler for
Trados, which shares the same database) before you run it. Supervertaler
v1.10.371 and later make the same repair automatically at start-up, so you only
need this on an older version.
:::

## Still no matches?

Open an issue on [GitHub](https://github.com/Supervertaler/Supervertaler-Workbench/issues)
with the script's full output and any "TM search failed" lines from the log.

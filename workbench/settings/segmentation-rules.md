---
title: "Segmentation Rules"
---

**Settings → 📏 Segmentation Rules** decides where Supervertaler splits text into segments whenever it does the splitting itself (from v1.10.372). That covers:

- plain-text and Markdown imports with **Split lines into sentences** ticked – **Project → Import → Text / Markdown File (TXT, MD)…**, and TXT/MD files in a **📁 Folder (Multiple Files)** import;
- text pasted into **New Project**;
- text added with [**Edit → ➕ Add Source Text…**](/workbench/import-export/formats/#adding-more-source-text-to-a-project).

DOCX and the other document formats are split by the Okapi engine with its own rules, and bilingual files from other CAT tools keep the segments they came with. Neither is affected by this page.

Changes are saved as you make them – there is no Save button. They apply the next time text is split: segments that are already in a project stay as they are.

## Options

- **Start a new segment at every line break** – each line of pasted text becomes at least one segment. When this is off (the default), line breaks inside pasted text count as spaces. Plain-text imports always keep each line of the file as its own paragraph, whatever this says.
- **Use the built-in sentence rules** – on by default. Splits after `.`, `!` or `?` followed by a space and a capital letter or an opening quote, and keeps common abbreviations such as Mr., Dr., e.g. and etc. with their sentence. Untick it to let only your own rules below decide.
- **Extra abbreviations** – a full stop after these never ends a segment. Separate them with commas or spaces; case doesn't matter, and you can leave out the full stop. For example `np, itd, tzn, m.in` for Polish, or `bzw, usw` for German.

## Custom rules

Custom rules work the way SRX rules do in OmegaT, Okapi and other CAT tools. Each rule is either a **Break** or a **No break (exception)**, with one regular expression for the text just before the break and one for the text just after it. Either of the two may be empty.

Rules are checked from top to bottom, before the built-in rules, and at each position the first rule that matches decides. So an exception can stop a split the built-in rules would make, and a break rule can split where they wouldn't.

The table has these columns:

- **On** – untick to switch a rule off without deleting it.
- **Type** – **Break** or **No break (exception)**.
- **Before the break** – a regular expression for the text just before the break.
- **After the break** – a regular expression for the text just after it.
- **Comment** – a note for yourself.

Add rules with **➕ Break rule** or **➕ Exception**, change their order with **▲** and **▼** (earlier rules win), and delete the selected one with **Remove**.

Two examples:

| Type | Before the break | After the break | What it does |
|---|---|---|---|
| Break | `<>` | *(empty)* | Starts a new segment after every `<>` |
| No break (exception) | `\bnp\.` | `\s` | Keeps "np." inside its sentence |

What **Before the break** matches stays at the end of the first segment, so the delimiter isn't lost: `One part<>another part` becomes `One part<>` and `another part`.

A rule with a pattern Supervertaler can't use is marked in red and ignored. Hover over it to see why.

### Break after text…

If you just want to split at a delimiter, you don't need to write a regular expression. Click **➕ Break after text…**, type the delimiter (for example `<>` or `|`) and click OK. Supervertaler adds a break rule for it, with the comment "Break after …".

## Import and export SRX

- **📥 Import SRX…** adds rules from an SRX file, for example OmegaT's `segmentation.srx`. If the file has rule sets for several languages, you choose one; most files end with a general set, often called "Default". If you already have custom rules, you're asked whether to **Add** the imported rules after them or **Replace** them. Java-style classes such as `\p{Lu}` (any capital letter) are translated for you. A rule Supervertaler can't read is marked in red and ignored.
- **📤 Export SRX…** saves your custom rules that are switched on and usable as an SRX file (`segmentation.srx` by default), for use in other tools. The built-in rules and the options at the top are not included.

:::tip
Imported SRX rules usually describe the whole segmentation on their own. Untick **Use the built-in sentence rules** to let them decide by themselves.
:::

## The Test box

The **Test** box at the bottom shows your rules at work. Type or paste text into it, and the list below shows the resulting segments, numbered. It updates as you type and as you change the rules, so you can try a rule out before importing anything.

## Plain-text export puts each line back together exactly

When Supervertaler splits a line, it now remembers the spacing between the segments. **Project → Export → Simple Text File - Translated (TXT)…** rebuilds each line with that same spacing, instead of always putting one space between segments.

This matters when a rule splits where there was no space. A line such as `Cześć<>Siema<>`, split into `Cześć<>` and `Siema<>`, is exported back as one line with no space added. Merging two such segments joins them without a space, too.

:::note
Projects created before v1.10.372 have no recorded spacing, so their segments are joined with one space on export, as before.
:::

## Related

- [Importing Text Files](/workbench/import-export/txt-import/)
- [Multi-File Projects](/workbench/import-export/multi-file/)
- [Import Options](/workbench/import-export/import-options/)

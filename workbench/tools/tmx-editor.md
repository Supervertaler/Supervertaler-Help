---
title: "TMX Editor"
---

Supervertaler includes a built-in TMX editor for inspecting and editing TMX translation memories.

## Where to find it

- Open the **Tools menu** at the top of the window → **✏️ TMX Editor…**. The editor opens in its own window.

## What you can do

- Create, open, edit, and save TMX files (**📁 New**, **📂 Open**, **💾 Save**, **💾 Save As...**).
- Add and delete translation units (**➕ Add TU**, **❌ Delete**).
- Search and filter by source/target text.
- Edit TMX header metadata (**ℹ️ Header**).
- Run basic validation (**✓ Validate**) and view statistics (**📊 Stats**).
- Strip tags from every translation unit at once (**🧹 Clean Tags**).

## Common workflows

### Clean up a TMX before importing

1. Open the TMX in **✏️ TMX Editor**.
2. Fix any obvious formatting issues (wrong language, empty segments, etc.).
3. Save the TMX.
4. Import it into your project via [Importing TMX files](/workbench/translation-memory/importing-tmx/).

### Remove unwanted tags

If you’re trying to simplify a TMX that contains formatting or CAT-tool tags, you can remove them before importing:

1. Click **🧹 Clean Tags**.
2. Tick the kinds of tag to remove – or use **Select All**, **Select None** or **Select Formatting Only**.
3. Choose whether tags are removed completely or replaced with a space, and whether to clean the source, the target or both.
4. **👁️ Preview** summarises your choices; **🧹 Clean Tags** applies them to all translation units.
5. Save the TMX.

:::note
TMX is just XML – some tags are real inline markup (TMX/XLIFF-style), others are literal text like `&lt;b&gt;...&lt;/b&gt;`.
Cleaning tags can improve matching, but it can also remove important formatting. If you’re unsure, test on a copy first.
:::

## Related

- [Importing TMX files](/workbench/translation-memory/importing-tmx/)
- [Translation memory](/workbench/translation-memory/basics/)

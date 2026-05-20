---
title: "Your First Translation Project"
---

Let's walk through creating a complete translation project from start to finish.

## Creating a New Project

### Option 1: Import a Document

1. Go to **File → Import → DOCX...**
2. Select your Word document
3. Choose the source language (e.g., "English")
4. Choose the target language (e.g., "Dutch")
5. Click **Import**

Your document is now segmented and ready for translation.

### Option 2: Import a Text File

1. Go to **File → Import → Text File...**
2. Select your `.txt` file
3. Each line becomes a separate segment

### Option 3: Multi-File Project

1. Go to **File → Import → Folder (Multiple Files)...**
2. Select a folder containing DOCX or TXT files
3. Choose which files to include
4. All files are imported as one project

## Understanding the Interface

After import, you'll see the main window. Along the top are the workspace tabs (**Editor**, **TMs**, **Termbases**, **AI**, **SuperLookup**, **Clipboard Manager**, **Voice**, **Settings**). The **Editor** tab holds the translation grid:

```
┌──────────────────────────────────────────────────────────────────────┐
│ Editor │ TMs │ Termbases │ AI │ SuperLookup │ Clipboard │ Voice │ ⚙   │
├──────────────────────────────────────────────────────────────────────┤
│  # │ Type │ Source                │ Target                │ Status    │
├────┼──────┼───────────────────────┼───────────────────────┼───────────┤
│  1 │  ¶   │ Hello, world!         │                       │  ❌       │
│  2 │  ¶   │ This is a test.       │                       │  ❌       │
│  3 │  ¶   │ Translate me!         │                       │  ❌       │
└────┴──────┴───────────────────────┴───────────────────────┴───────────┘
```

**TMs** and **Termbases** are their own top tabs for managing translation memories and terminology.

### Status Icons

| Icon | Meaning |
|------|---------|
| ❌ | Not started |
| ⚡ | Pre-translated |
| ✏️ | Draft (edited but not confirmed) |
| ✔ | Confirmed |
| 🔒 | Locked |

See [Segment Statuses](../editor/segment-statuses.md) for the full list.

## Translating Your First Segment

1. Click on segment 1's Target cell
2. Type your translation
3. Press `Ctrl+Enter` to confirm
4. The status changes to ✅

### Using AI Translation

1. Click on segment 2
2. Press `Ctrl+T` to translate it with AI
3. The AI translation appears in the Target cell
4. Review, edit if needed, and confirm with `Ctrl+Enter`

## Setting Up Resources

### Add a Translation Memory

1. Go to the **TMs** tab
2. Click **+ Create TM** or **Import TMX**
3. Your TM will automatically provide matches

### Add a Termbase

1. Go to the **Termbases** tab
2. Click **+ Create Termbase**
3. Add terms manually or import from TSV

## Saving Your Project

1. Press `Ctrl+S`
2. Choose a name and location
3. Your project is saved as `.svproj`

:::tip
**Tip:** Supervertaler auto-saves your work periodically, but it's good practice to save manually before closing.
:::

## Exporting the Translation

When you're finished:

1. Go to **File → Export**
2. Choose your format:
   - **DOCX** - Standard Word document with translations
   - **Bilingual Table** - Source and target side by side
   - **Text File** - Plain text output

3. Select destination and click **Export**

## Project Workflow Summary

```
Import Document
      ↓
Set Up TMs & Termbases (optional)
      ↓
Translate Segments (manual or AI)
      ↓
Review & Confirm (Ctrl+Enter)
      ↓
Save Project (.svproj)
      ↓
Export Translation
```

---

## What's Next?

Now that you've completed your first project:

- [Learn keyboard shortcuts](../editor/keyboard-shortcuts.md) for faster work
- [Set up batch translation](../ai-translation/batch-translation.md) for larger documents
- [Explore CAT tool workflows](../cat-tools/overview.md) if you use professional tools

---
title: "The Project Folder"
---

A Supervertaler project isn't just the `.svproj` file — it's a **folder** that
holds the project file together with the documents it works on. Keeping
everything in one folder means a project is self-contained: you can move,
rename, zip or email the folder and it still opens and exports correctly.

## What's in a project folder

```
My Project/
├─ My Project.svproj     ← the project file
├─ source/               ← the original documents you're translating
└─ target/               ← the translated documents you export
```

- **`source/`** — when you **save** a project, its original document is copied
  here, and the project remembers it by a path *relative* to the folder. That's
  what makes the project portable: it no longer depends on the document staying
  at the exact location you first imported it from. Move or rename the original
  afterwards and your export still works.
- **`target/`** — when you run **Project → Export → Export Translated Document**
  (or Simple Text), the Save dialog opens here by default, so your finished
  translations land next to their sources. You can still browse somewhere else;
  this is only the default.

## Why this matters

- **Portability** — hand the whole folder to a colleague, or move it between
  machines, and the structure-preserving export keeps working. Nothing points at
  a file that only exists on your computer.
- **No accidental cross-wiring** — because the source is stored relative to the
  project folder, a project can never end up bound to an unrelated document.

:::tip
Keep the `.svproj` **inside** its folder. If you want to relocate a project,
move or copy the **whole folder**, not just the `.svproj` on its own.
:::

## Existing projects

Projects created before this layout existed still work — they reference their
source by an absolute path, and Supervertaler resolves it as before. The next
time you **save** such a project, its source is copied into `source/` and the
reference switches to the portable relative form automatically.

## Related pages

- [Exporting Translations](exporting.md)
- [Your First Translation Project](../get-started/first-project.md)
- [Multi-File Projects](multi-file.md)

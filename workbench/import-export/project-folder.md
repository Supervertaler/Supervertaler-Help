---
title: "The Project Folder"
---

A Supervertaler project isn't just the `.svproj` file – it's a **folder** that
holds the project file together with the documents it works on. Keeping
everything in one folder means a project is self-contained: you can move,
rename, zip or email the folder and it still opens and exports correctly.

:::note
**New Project** has a "📁 Create a dedicated folder for this project" checkbox
(on by default). When it's on, the first save tucks the `.svproj` into its own
folder as shown below. Turn it off to save the `.svproj` flat, wherever you
choose – the folder layout is never forced, so you can keep your own naming or
nest a project inside a larger job folder.
:::

## What's in a project folder

```
My Project/
├─ My Project.svproj     ← the project file
├─ My Project.svproj.bak ← the previous save (see Backup)
├─ source/               ← the original documents you're translating
├─ target/               ← the translated documents you export
└─ tm/                   ← the auto-backup TMX
```

- **`source/`** – when you **save** a project, its original document is copied
  here, and the project remembers it by a path *relative* to the folder. That's
  what makes the project portable: it no longer depends on the document staying
  at the exact location you first imported it from. Move or rename the original
  afterwards and your export still works.

  Files you **export back into**, such as a memoQ bilingual DOCX or XLIFF, a
  Trados package (SDLPPX), SDLXLIFF files, or a CafeTran, Déjà Vu or PO file, are
  copied here too. Supervertaler keeps using your original as long as it can find
  it, so the export is still offered next to it. The copy in `source/` is used
  only when the original is gone, for example after you moved the folder or
  opened the project on another computer; the export is then offered in
  `target/`. A file is copied again only when it has changed, and two different
  files with the same name get separate copies (`doc.sdlxliff`, `doc_2.sdlxliff`).
- **`target/`** – when you run **Project → Export → Export Translated Document**
  (or Simple Text), the Save dialog opens here by default, so your finished
  translations land next to their sources. You can still browse somewhere else;
  this is only the default.
- **`tm/`** – the automatic backup (**Settings → 💾 Backup**) writes the
  project's translations here as `<project>_backup.tmx`.
- **`.svproj.bak`** – the project as it was at the previous save. If the project
  file is ever damaged, Supervertaler offers to open this copy. See
  [Backup](/workbench/settings/backup/#safe-saving-and-the-svprojbak-copy).

## Why this matters

- **Portability** – hand the whole folder to a colleague, or move it between
  machines, and the structure-preserving export keeps working. Nothing points at
  a file that only exists on your computer.
- **No accidental cross-wiring** – because the source is stored relative to the
  project folder, a project can never end up bound to an unrelated document.

:::tip
Keep the `.svproj` **inside** its folder. If you want to relocate a project,
move or copy the **whole folder**, not just the `.svproj` on its own.
:::

## Existing projects

Projects created before this layout existed still work – they reference their
source by an absolute path, and Supervertaler resolves it as before. The next
time you **save** such a project, its source is copied into `source/` and the
reference switches to the portable relative form automatically.

## Related pages

- [Exporting Translations](/workbench/import-export/exporting/)
- [Your First Translation Project](/workbench/get-started/first-project/)
- [Multi-File Projects](/workbench/import-export/multi-file/)

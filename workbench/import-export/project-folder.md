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
nest a project inside a larger job folder. Your choice is remembered for the
next new project.
:::

## What's in a project folder

```
My Project/
├─ My Project.svproj      ← the project file
├─ My Project.svproj.bak  ← the previous save, kept as a safety copy
├─ source/                ← the original documents you're translating
├─ target/                ← the translated documents you export
├─ tm/                    ← the automatic backup of the project, and TMX exports
├─ glossary/              ← termbases you export
├─ reports/               ← statistics and QA reports you export
└─ qa/xbench/             ← written by QA → Open in Xbench
```

- **`source/`** – when you **save** a project, its original document is copied
  here, and the project remembers it by a path *relative* to the folder. That's
  what makes the project portable: it no longer depends on the document staying
  at the exact location you first imported it from. Move or rename the original
  afterwards and your export still works.
- **Files from other CAT tools** – a project imported from a memoQ bilingual
  DOCX or XLIFF, a Trados review DOCX, SDLPPX package or SDLXLIFF files, or a
  CafeTran, Déjà Vu, PO or plain-text file, needs that file again to export
  your translation back into it. Saving copies it into `source/` as well. Your
  original stays the file Supervertaler works with, so exports are still
  offered next to it; the copy in `source/` is used only when the original
  can't be found – for example after you moved the project folder or opened it
  on another computer. A file is copied again only when it has changed, and two
  different files with the same name get separate copies (`doc.sdlxliff`,
  `doc_2.sdlxliff`).
- **`target/`** – when you run **Project → Export → Export Translated Document**
  (or Simple Text), the Save dialog opens here by default, so your finished
  translations land next to their sources. The bilingual review table does the
  same from v1.10.373. You can still browse somewhere else; this is only the
  default.
- **`tm/`** – the automatic backup (**Settings → 💾 Backup**) exports the
  project as `<project>_backup.tmx` into this folder, the way OmegaT keeps its
  TMs in `tm/`. A backup left next to the `.svproj` by an older version is
  moved here. From v1.10.373, exporting a TM, the TM database or selected
  segments as TMX also opens here.
- **`glossary/`** – from v1.10.373, exporting a termbase from the
  **Termbases** tab opens here.
- **`reports/`** – from v1.10.373, **Export** in the
  [Statistics](/workbench/tools/statistics/) window and in
  [QA Checks](/workbench/qa/qa-checks/) opens here.
- **`qa/xbench/`** – what [Open in Xbench](/workbench/qa/xbench/) writes.

Supervertaler creates each folder the first time something is saved in it.
Before a project has been saved, there's no project folder yet, and the Save
dialogs open wherever they did before.

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

## Safe saving and the backup copy

Saving a project is all-or-nothing. Supervertaler first writes the project to a
temporary file next to it (`My Project.svproj.tmp`) and only then swaps it in
for the real one, in a single step. If something goes wrong halfway – a full
disk, a crash, a power cut – the previous version of the `.svproj` is still
there, whole.

Each save also keeps the version it replaces as **`My Project.svproj.bak`**, the
way OmegaT keeps `omegat.project.bak`. A damaged file never overwrites a good
backup: the `.bak` is only refreshed from a previous save that was itself
complete.

### Opening a damaged project

If a `.svproj` cannot be read, Supervertaler looks for its `.bak` and asks:

> *My Project.svproj is damaged and cannot be read: … A backup copy from the
> previous save (2026-10-01 14:32) is available. Open the backup? Saving then
> replaces the damaged file.*

Click **Yes** to open the backup. The project opens marked as changed, so the
next **Save** writes a good `.svproj` over the damaged one. Anything you did
after that previous save is not in the backup.

:::note
Safe saving and the `.svproj.bak` copy are separate from the timestamped
backups in [Settings → 💾 Backup](/workbench/settings/backup/), which keep a
longer history in a folder of your choice.
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

---
title: "Project Packages (.svpkg)"
---

From v1.10.373, you can pack a whole project into one **`.svpkg`** file and open it on another computer. That covers moving from a Windows laptop to a Mac, carrying on at home, or handing a job to a colleague.

A project's TMs, glossaries and prompts live in Supervertaler's own database and prompt library, not in the project folder, so copying the folder alone leaves them behind. A package takes them along.

## Packing a project

1. Open the project and save it (**Project → Save**).
2. Choose **Project → 📦 Pack Project (.svpkg)…**.
3. Choose where to save the package. By default it goes next to the project folder, named after the project.

The package contains:

| What | From |
|---|---|
| The project file | your `.svproj` |
| The project's folders | `source/`, `target/`, `tm/`, `glossary/`, `reports/` and `qa/` (see [The Project Folder](/workbench/import-export/project-folder/)) |
| The TMs switched on for the project | exported as TMX |
| The glossaries switched on for the project | exported as TSV |
| The project's custom prompt and attached prompts | as they are in your prompt library |

Unsaved changes are saved before packing, so the package has your latest work. Other files that happen to sit next to the project file aren't packed, only the project and its own folders.

## Opening a package

1. Choose **Project → 📦 Open Package (.svpkg)…** and pick the package.
2. Choose where the project folder should go.

Supervertaler unpacks the project into a new folder named after it. If that folder already exists, it adds "(2)" to the name. Then it brings in the resources and opens the project.

- **TMs and glossaries.** If that computer already has a TM or glossary with the same name, the package's entries are added to it. Entries it already contains aren't duplicated, so you can move a project back and forth. Otherwise a new TM or glossary is created. Either way, it's switched on for the project. A copy of each also stays in the project's `tm/` and `glossary/` folders.
- **Prompts.** A prompt goes into your prompt library at the same place it had on the other computer, and the project uses it as before. If you already have a *different* prompt there, yours is kept: the package's copy is saved with "(from package)" added, and the project uses that copy.

When it's done, a summary lists what was added where, for example "TM *Client TM*: 120 new entries added to your TM of that name".

## Good to know

- **A package is a zip file** with a `manifest.json` that describes its contents. You can open it with any zip tool to look inside.
- **Packages made by a newer Supervertaler** can't be opened by an older one. You'll be asked to update.
- **Large projects make large packages.** An SDLPPX or a big TM is packed as it is.
- **If two computers both changed the project**, a package doesn't merge them. Opening a package always creates a new project folder, so nothing is overwritten, and you choose which copy to carry on with.

## See also

- [The Project Folder](/workbench/import-export/project-folder/)
- [TM Basics](/workbench/translation-memory/basics/)
- [Prompt Manager](/workbench/ai-translation/prompt-library/)

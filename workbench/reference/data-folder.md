---
title: "User Data Folder"
---

Supervertaler Workbench keeps your termbases, translation memories, prompt
library, settings, and projects in a single user data folder. This folder is
**shared with [Supervertaler for Trados](https://docs.supervertaler.com/trados/data-folder/)**,
so both programs read and write the same terminology, TMs, and prompts without
duplicating files.

## Folder location

By default the folder lives in your home directory:

```
Windows:        C:\Users\<YourName>\Supervertaler\
macOS / Linux:  ~/Supervertaler/
```

You can choose a different location during first-run setup. The chosen path is
recorded in a small pointer file in your user configuration directory (on
Windows, `%APPDATA%\Supervertaler\config.json`), which both programs read so
they always agree on where the data lives.

## Folder structure

```
Supervertaler/
│
├── prompt_library/              Shared
│   ├── domain_expertise/
│   ├── project_prompts/
│   └── style_guides/
│
├── resources/                   Shared
│   ├── supervertaler.db
│   ├── termbases/
│   ├── tms/
│   ├── non_translatables/
│   └── segmentation_rules/
│
├── workbench/                   Supervertaler Workbench only
│   ├── settings/
│   │   ├── settings.json
│   │   ├── themes.json
│   │   ├── shortcuts.json
│   │   └── ...
│   ├── dictionaries/
│   ├── projects/
│   ├── ai_assistant/
│   ├── voice_scripts/
│   └── web_cache/
│
└── trados/                      Supervertaler for Trados only
    ├── settings/
    ├── projects/
    └── batch_backups/
```

### Shared resources

The **prompt library** and **resources** folders are shared between both
programs. A prompt you create or edit in Workbench is immediately available in
the Trados plugin, and vice versa. The SQLite database (`supervertaler.db`)
holds your termbases and translation memories — Workbench has full read-write
access to it.

### Program-specific folders

Each program stores its own settings, projects, and runtime data in a dedicated
subfolder (`workbench/` or `trados/`), so the two never interfere with each
other. Workbench's `workbench/` subfolder holds your `settings/` (including
`shortcuts.json` and `themes.json`), custom spellcheck `dictionaries/`, saved
`projects/`, AI assistant data, voice scripts, and a web cache.

## Automatic migration

If you're updating from an older version, Workbench reorganises the folder
automatically on its next startup. No manual action is required — your settings
and data are preserved.

## Related

- [Supervertaler for Trados — User Data Folder](https://docs.supervertaler.com/trados/data-folder/)
- [General Settings](../settings/general.md)

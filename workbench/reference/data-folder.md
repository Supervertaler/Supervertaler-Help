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
recorded in a small pointer file in your user configuration directory, which
both programs read so they always agree on where the data lives:

```
Windows:  %APPDATA%\Supervertaler\config.json
macOS:    ~/Library/Application Support/Supervertaler/config.json
Linux:    ~/.config/Supervertaler/config.json
```

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
├── snippet_library/             Workbench: Clipboard Manager snippets
├── text_conversion_library/     Workbench: Clipboard Manager text conversions
├── find_replace_sets/           Workbench: saved Find & Replace sets
├── vosk-models/                 Workbench: speech models for Voice
│
├── workbench/                   Supervertaler Workbench only
│   ├── settings/
│   │   ├── settings.json
│   │   ├── themes.json
│   │   ├── shortcuts.json
│   │   └── ...
│   ├── dictionaries/
│   ├── projects/
│   ├── backups/
│   ├── logs/
│   ├── ai_assistant/
│   ├── voice_scripts/
│   ├── superbrowser_profiles/
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
holds your termbases and translation memories – Workbench has full read-write
access to it.

### Program-specific folders

Each program stores its own settings, projects, and runtime data in a dedicated
subfolder (`workbench/` or `trados/`), so the two never interfere with each
other. Workbench's `workbench/` subfolder holds your `settings/`, custom
spellcheck `dictionaries/` (including `custom_words.txt`), saved `projects/`,
versioned project `backups/` (see [Backup](/workbench/settings/backup/)), the diagnostic log (`logs/supervertaler.log`), AI assistant data,
voice scripts, the Superbrowser logins and a web cache.

A few Workbench libraries sit at the top level of the data folder:
`snippet_library/` and `text_conversion_library/` (the
[Clipboard Manager](/workbench/clipboard/overview/)'s Menu column),
`find_replace_sets/` (saved Find & Replace sets) and `vosk-models/` (the
speech models [Voice](/workbench/voice/overview/) downloads on first use).

### Settings files

Almost all of Workbench's settings are in one file,
`workbench/settings/settings.json`, with four sections: `api_keys`, `general`,
`ui` and `features`. A few things have a small file of their own in the same
folder:

| File | Holds |
| --- | --- |
| `themes.json` | Your custom colour themes |
| `shortcuts.json` | Your keyboard shortcut changes |
| `recent_projects.json` | The recent projects list |
| `find_replace_history.json` | Find & Replace search history |
| `voice_commands.json` | Your voice commands |

Older versions kept settings in separate files (such as `general_settings.json`
and `api_keys.txt`). They are merged into `settings.json` automatically at
startup and renamed with a `.migrated` extension.

:::caution
`settings.json` contains your API keys. Don't share it, or attach it to a
support request, without removing them first.
:::

## Automatic migration

If you're updating from an older version, Workbench reorganises the folder
automatically on its next startup. No manual action is required – your settings
and data are preserved.

## Related

- [Supervertaler for Trados – User Data Folder](https://docs.supervertaler.com/trados/data-folder/)
- [General Settings](/workbench/settings/general/)

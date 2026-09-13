---
title: "Settings and files"
---

Sidekick keeps everything in two places: its own folder, and the key file it shares with the other Supervertaler products. Nothing is written to the registry or to AppData.

### The Sidekick folder

| | |
|---|---|
| `Sidekick.ahk`, `lib\` | the program |
| `data\` | **your content** – the menu, clipboard history, shortcuts, text expansions. Never overwritten by an update. |
| `data.example\` | the starter set, copied into `data\` on first run |
| `settings.ini` | your settings; created from `settings.example.ini` |
| `settings.example.ini` | the documented template – every setting, with a comment saying what it does |
| `packs\` | the language packs, one JSON file per language pair – see [Searches](/sidekick/searches/#language-packs) |

Inside `data\`:

| File | Holds |
|---|---|
| `menu.json` | the menu: snippets, bookmarks, AI prompts, searches, conversions – see [the library](/sidekick/library/) |
| `shortcuts.json` | the shortcuts you made yourself – see [Keyboard shortcuts](/sidekick/keyboard-shortcuts/) |
| `expansions.json` | text expansions – see [Text expansion](/sidekick/text-expansion/) |
| `clipboard.json` | clipboard history |

All plain JSON. Copy the folder to another machine and Sidekick is set up there.

### settings.ini

Open it in any editor, or reach the parts that have a window through the menu:

| Section | Holds | Window |
|---|---|---|
| `[Hotkeys]` | the built-in shortcuts | **Settings → Keyboard shortcuts…** |
| `[AI]` | provider, model and effort for AI actions | – |
| `[Keys]` | API keys (see below) | **Settings → AI providers & keys…** |
| `[QuickTrans]` | which engines, which models, whether AI is fetched automatically, and the language pair (`SourceLang`, `TargetLang`) | **Settings → AI providers & keys…**, **Settings → Language pair…** |
| `[Packs]` | which language packs are installed (`Installed=nl-en`); absent means the pack for the current pair | **Settings → Language packs…** |
| `[Clipboard]` | capture on/off, size, expiry, excluded programs | **Settings → Pause / resume clipboard capture** |
| `[Window]` | the main window's size and position, written automatically | – |

Changes to `settings.ini` made by hand take effect after **Settings → Reload Sidekick** (`Ctrl+R`).

### The shared API key file

API keys are read first from the file all Supervertaler products share:

```
C:\Users\<you>\Supervertaler\settings\api-keys.json
```

One key per provider, plain text. A key pasted into Supervertaler for Trados or Supervertaler for memoQ works in Sidekick, and one entered in Sidekick's **AI providers & keys…** window is written there for the plugins. Sidekick's machine-translation keys sit in the same file under their own names – note that `google` there is Google Translate, not Gemini.

A key in `settings.ini` under `[Keys]` is used only when the shared file has none for that provider.

### Where the tray icon went

Sidekick lives in the system tray. Right-click its icon for the menu; if the icon is hidden, Windows has tucked it behind the **^** overflow arrow. The tray icon follows the taskbar's light or dark theme.

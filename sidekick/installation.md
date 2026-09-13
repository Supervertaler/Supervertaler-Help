---
title: "Installation"
---

Sidekick is a script for [AutoHotkey v2](https://www.autohotkey.com/), so installing it is two steps and takes a couple of minutes. There is nothing to compile and no installer.

### 1. Install AutoHotkey v2

Download it from [autohotkey.com](https://www.autohotkey.com/) and run the installer. It must be **version 2.0 or later** – Sidekick does not run on the older v1.

### 2. Get Sidekick

Either clone the repository or download it as a zip from [github.com/Supervertaler/Supervertaler-Sidekick](https://github.com/Supervertaler/Supervertaler-Sidekick) (the green **Code** button → **Download ZIP**) and unpack it somewhere permanent, for example `C:\Users\<you>\Supervertaler-Sidekick`.

Then double-click `Sidekick.ahk`. Its icon appears in the system tray, and `` ` `` (backtick) opens the window.

On first run Sidekick copies a starter menu into its `data\` folder and opens with a working set of searches, conversions and AI prompts. From there you make it yours – see [Snippets, bookmarks and conversions](/sidekick/library/).

:::note
Sidekick asks for administrator rights when it starts. This is deliberate: without them, Windows ignores its hotkeys in any window that is itself running elevated.
:::

### 3. Start it with Windows

Put a shortcut to `Sidekick.ahk` in your Startup folder: press `Win+R`, type `shell:startup`, press Enter, and drop the shortcut in. Sidekick then loads at sign-in.

### 4. Add API keys

Most of Sidekick works without any key. Clipboard history, snippets, searches, conversions and text expansion need nothing, and QuickTrans translates through MyMemory out of the box.

The AI actions and the other translation engines want a key for each provider you use. Open the menu, go to **Settings → AI providers & keys…**, and paste each key beside its provider. The **Models** button beside each engine asks that provider which models your key can actually use, so you are never guessing at a model name.

Keys go into the file that all Supervertaler products share, `C:\Users\<you>\Supervertaler\settings\api-keys.json`. A key you have already set in Supervertaler for Trados or Supervertaler for memoQ is picked up here without retyping, and the reverse. See [Settings and files](/sidekick/settings/).

### Updating

Pull the repository, or download a fresh zip and unpack it over the old folder. Your `data\` folder and `settings.ini` are never part of the download, so an update cannot touch your content. Then choose **Settings → Reload Sidekick** (or press `Ctrl+R`).

### Uninstalling

Close Sidekick from its tray icon and delete the folder. Nothing is written anywhere else, apart from the shared API key file, which the other Supervertaler products also use.

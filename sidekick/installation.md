---
title: "Installation"
---

Sidekick comes with an installer. It takes a minute, needs no administrator rights, and brings everything Sidekick runs on with it, so there is nothing to install first.

### 1. Download the installer

[Download Supervertaler-Sidekick-Setup.exe](https://github.com/Supervertaler/Supervertaler-Sidekick/releases/latest/download/Supervertaler-Sidekick-Setup.exe) – the link always gives the newest version. Earlier versions, and what changed in each, are on the [releases page](https://github.com/Supervertaler/Supervertaler-Sidekick/releases).

### 2. Run it

Windows may stop it with *Windows protected your PC*. That is because the installer is not signed yet, not because anything is wrong with it: click **More info**, then **Run anyway**.

### 3. Choose a folder

The installer asks where Sidekick should go, and suggests a `sidekick` folder inside your Supervertaler data folder: `C:\Users\<you>\Supervertaler\sidekick`, or the same inside wherever you moved that folder. Your own menu, clipboard history, notes and settings are kept there too, so choose somewhere you will find again. A folder under *Program Files* is refused, because Sidekick saves into its own folder and Windows does not let programs write there.

Leave **Start Sidekick when I sign in to Windows** ticked unless you would rather start it from the Start menu yourself, and finish. Sidekick's icon appears in the system tray – behind the **^** by the clock if Windows has tucked it away – and `` ` `` (backtick) opens the window.

On first run Sidekick copies a starter menu into its `data` folder and opens with a working set of searches, conversions and AI prompts. From there you make it yours – see [Snippets, bookmarks and conversions](/sidekick/library/).

:::note
Sidekick runs without administrator rights, like any ordinary program. One consequence: Windows does not let it reach a program you started with **Run as administrator**, so its shortcuts do nothing while such a window is in front. Start that program normally and they work again.
:::

### 4. Add API keys

Most of Sidekick works without any key. Clipboard history, snippets, searches, conversions and text expansion need nothing, and QuickTrans translates through MyMemory out of the box.

The AI actions and the other translation engines want a key for each provider you use. Open the menu, go to **Settings → AI providers & keys…**, and paste each key beside its provider. Each engine's model list opens on the few models worth recommending; **Models**, or **Show all models**, adds everything your key can use, so you are never guessing at a model name.

Keys go into the file that all Supervertaler products share, `C:\Users\<you>\Supervertaler\settings\api-keys.json` – or the `settings` folder inside wherever you moved your Supervertaler data folder. A key you have already set in Supervertaler for Trados or Supervertaler for memoQ is picked up here without retyping, and the reverse. See [Settings and files](/sidekick/settings/).

### Updating

Run the installer for the newer version – the same download link. It closes Sidekick, replaces the program and starts it again, in the folder you chose the first time. Your `data` folder and `settings.ini` are never part of the installer, so an update cannot touch your content.

### Uninstalling

In Windows Settings, go to **Apps → Installed apps → Supervertaler Sidekick → Uninstall**. That removes the program, its Start menu entry and the sign-in shortcut. Your `data` folder and `settings.ini` stay where they were, in case you reinstall, and the uninstaller says where that is; delete the folder if you do not want them.

### Running it from the source

Sidekick is an [AutoHotkey v2](https://www.autohotkey.com/) script, and the installer is that script with its own copy of AutoHotkey beside it. If you already use AutoHotkey, or want to change the script itself, you can run it straight from the repository instead:

1. Install AutoHotkey **version 2.0 or later** from [autohotkey.com](https://www.autohotkey.com/). Sidekick does not run on the older v1.
2. Clone [github.com/Supervertaler/Supervertaler-Sidekick](https://github.com/Supervertaler/Supervertaler-Sidekick), or download it as a zip (the green **Code** button → **Download ZIP**) and unpack it somewhere permanent.
3. Double-click `Sidekick.ahk`. To start it with Windows, put a shortcut to it in your Startup folder: press `Win+R`, type `shell:startup`, press Enter, and drop the shortcut in.

To update, pull the repository or unpack a fresh zip over the old folder, then choose **Settings → Reload Sidekick**. Do not run an installed copy at the same time: the two would claim the same keys.

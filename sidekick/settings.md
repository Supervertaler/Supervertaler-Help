---
title: "Settings and files"
---

Sidekick keeps everything in two places: its own folder – the one you chose when installing, `C:\Users\<you>\Supervertaler\sidekick` unless you picked another – and the key file it shares with the other Supervertaler products. Sidekick itself writes nothing to the registry or to AppData. The installer adds only what any installed program has: a Start menu entry, a sign-in shortcut if you asked for one, and its line in Windows' list of installed apps.

### The Sidekick folder

| | |
|---|---|
| `Sidekick.ahk`, `lib\` | the program |
| `AutoHotkey\` | the AutoHotkey that runs it, in an installed copy – see [Running it from the source](/sidekick/installation/#running-it-from-the-source) |
| `data\` | **your content** – the menu, clipboard history, shortcuts, text expansions. Never overwritten by an update. |
| `data.example\` | the starter set, copied into `data\` on first run |
| `settings.ini` | your settings, written as you change them; anything it does not mention is at its default |
| `settings.example.ini` | the documented template – every setting, with a comment saying what it does |
| `packs\` | the language packs, one JSON file per language pair – see [Searches](/sidekick/searches/#language-packs) |

Inside `data\`:

| File | Holds |
|---|---|
| `menu.json` | the menu: snippets, bookmarks, AI prompts, searches, conversions – see [the library](/sidekick/library/) |
| `shortcuts.json` | the shortcuts you made yourself – see [Keyboard shortcuts](/sidekick/keyboard-shortcuts/) |
| `expansions.json` | text expansions – see [Text expansion](/sidekick/text-expansion/) |
| `clipboard.json` | clipboard history |

All plain JSON. Copy the `data` folder and `settings.ini` into Sidekick's folder on another computer and Sidekick is set up there.

### settings.ini

Open it in any editor, or reach the parts that have a window through the menu:

| Section | Holds | Window |
|---|---|---|
| `[Hotkeys]` | the built-in shortcuts | **Settings → Keyboard shortcuts…** |
| `[AI]` | provider, model and effort for AI actions | **Settings → AI providers & keys…** (provider and model) |
| `[Keys]` | API keys (see below) | **Settings → AI providers & keys…** |
| `[QuickTrans]` | which engines, which models, whether AI is fetched automatically, and the language pair (`SourceLang`, `TargetLang`) | **Settings → AI providers & keys…**, **Settings → Language pair…** |
| `[Packs]` | which language packs are installed (`Installed=nl-en`); absent means the pack for the current pair | **Settings → Language packs…** |
| `[Clipboard]` | capture on/off, size, expiry, excluded programs | **Settings → Pause / resume clipboard capture** |
| `[Window]` | the main window's size and position, written automatically | – |

Changes to `settings.ini` made by hand take effect after **Settings → Reload Sidekick**.

### The shared API key file

API keys are read first from the file all Supervertaler products share:

```
C:\Users\<you>\Supervertaler\settings\api-keys.json
```

If you moved your Supervertaler data folder, it is the `settings` folder inside that one.

One key per provider, plain text. A key pasted into Supervertaler for Trados or Supervertaler for memoQ works in Sidekick, and one entered in Sidekick's **AI providers & keys…** window is written there for the plugins. Sidekick's machine-translation keys sit in the same file under their own names – note that `google` there is Google Translate, not Gemini.

A key in `settings.ini` under `[Keys]` is used only when neither the shared file nor its locked copy (below) has one for that provider.

### Keys locked to this computer

Each key Sidekick saves, and each key it finds in the shared file when it starts, is also kept in your Windows profile, locked by Windows so that it opens only for your Windows account:

```
C:\Users\<you>\AppData\Roaming\Supervertaler\api-keys.locked.json
```

Supervertaler for Trados and Supervertaler for memoQ read and write the same file. The shared `api-keys.json` is still written as before, so older versions keep working; a later version will stop keeping keys in the data folder. There is nothing to do.

### "Can't be read on this computer"

A key that Windows will not unlock for you – one saved under another Windows sign-in, or one stored before an administrator reset your Windows password – is never shown as an empty box or sent to the provider. The **AI providers & keys…** window says so under that provider's key box:

> Your Anthropic key can't be read on this computer – it was saved under another Windows sign-in, or your Windows password was reset. Paste the key in again; nothing else is affected.

An AI action that needs the key stops with "Can't use your Anthropic key – it can't be read on this computer…" instead of calling the provider, and in QuickTrans that engine's row says the same. Paste the key in again and click **Save**. Until you do, the unreadable copy is kept – leaving the box empty and clicking **Save** does not remove it – because some causes pass by themselves, such as a company network that cannot be reached yet after a password reset.

If the file holding the locked keys is ever damaged, Sidekick keeps a copy of it beside the original (`api-keys.locked.damaged-…json`) and says so at the top of the **AI providers & keys…** window, asking you to paste your keys in again. While the shared file still holds your keys, they are locked again from there when Sidekick starts, so in practice only a key that an action reports as missing needs pasting.

### Where the tray icon went

Sidekick lives in the system tray. Right-click its icon for the menu; if the icon is hidden, Windows has tucked it behind the **^** overflow arrow. The tray icon follows the taskbar's light or dark theme.

---
title: "Clipboard history"
---

Sidekick watches the clipboard and keeps a searchable history of everything you copy. The history survives restarts, and any entry can be pasted straight back into whatever window you came from.

It is text only. Image clips were left out deliberately: for translation work the history that matters is text, and AutoHotkey has no workable way to thumbnail and persist pictures.

### Using it

The history is the left pane of the [window](/sidekick/window/) (`` ` ``), and it also has a window of its own on `Ctrl+Alt+C`. Both work the same way:

| Key | Does |
|---|---|
| `↑` `↓`, `PgUp` `PgDn`, `Home` `End` | move |
| typing | filters the list |
| `Enter` | paste the selected clip into the window you came from |
| `Ctrl+Enter` | copy it to the clipboard without pasting |
| `Alt+1`–`9` | paste the first, second, third… clip straight away |
| `Ctrl+Delete` | delete the selected clip |
| `Esc` | close |

**Ticks.** A clip you have pasted is ticked and greyed in the list. Copy a column of terms, then work down the list pasting each one where it belongs: the ticks show how far you have got. The most recent clips are also listed on the classic popup menu under **Recent clips**.

### Pausing capture

**Settings → Pause / resume clipboard capture** stops recording until you switch it back on, for the moments you would rather nothing was kept. The setting is remembered across restarts.

### Privacy

Three settings in `settings.ini`, under `[Clipboard]`, keep the history from holding things it should not:

| Setting | Does |
|---|---|
| `ExcludedApps` | Never record anything copied while one of these programs is in the foreground. Pipe-separated process names – the obvious use is password managers, e.g. `keepassxc.exe\|1password.exe\|bitwarden.exe`. Empty by default, so that a URL you copy out of your password manager does not silently vanish. |
| `AutoDeleteMinutes` | Discard entries older than this many minutes. `0`, the default, keeps them until you delete them. |
| `MaxItems` | How many entries to keep; the oldest fall off the end. Default `200`. |

Everything is stored in the `data\` folder next to Sidekick, on your own disk. Nothing is sent anywhere. See [Settings and files](/sidekick/settings/).

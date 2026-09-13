---
title: "Keyboard shortcuts"
---

A shortcut is a key to press and something for it to do. Sidekick has a built-in set, and every key in it can be changed, given a second key, or limited to one program. You can also attach a key to anything the menu does. All of it is set in **Settings → Keyboard shortcuts…**; nothing needs an ini file.

### The built-in shortcuts

| Does | Default key |
|---|---|
| Open the palette (search everything) | `Ctrl+Alt+Space` |
| Translate the selection (QuickTrans) | `Ctrl+Alt+T` |
| Open the window (clipboard + menu) | `` ` `` (backtick) |
| Classic popup menu | `Ctrl` + `` ` `` (backtick) |
| Clipboard history | `Ctrl+Alt+C` |
| Library Editor | none |
| Google the selection | `Ctrl+/` |
| Search the desktop (dtSearch) | `Ctrl+Shift+D` |
| Confirm segment (presses Ctrl+Enter) | `Numpad Enter`, in memoQ and Trados Studio only |
| Reload Sidekick | `Ctrl+R` |

**Confirm segment** is there because memoQ and Trados both confirm with Ctrl+Enter, which is two hands. Numpad Enter is one. It is limited to those two programs, so Numpad Enter keeps its normal meaning everywhere else.

### Changing a key

Select a row, press **Change key…**, and press the combination you want. Sidekick refuses a combination Windows will not accept rather than saving one that silently does nothing. **Turn off** frees a key; **Reset to default** puts it back.

**Add another key…** keeps the keys a shortcut has and adds one more. If the existing keys are limited to particular programs, you are asked whether the new one should be too – usually the point, since a global key that presses Ctrl+Enter would send half-written emails.

### Double-tap keys

A key can be a quick double tap of Ctrl, Shift or Alt. In the "Press a shortcut" dialog, tap the modifier twice within about half a second and it is recorded as, for example, "Ctrl twice". The modifier keeps working normally: Ctrl+C followed by a tap does not count, and a triple tap fires once.

Tapping Ctrl twice to confirm a segment in memoQ or Trados is the obvious use: select **Confirm segment**, press **Add another key…**, tap Ctrl twice, answer **Yes** to limit it to the same programs, save.

### Your own shortcuts

**New shortcut…** attaches a key to something of your own. Give it a name, choose what it does, and press the key:

| Kind | Does |
|---|---|
| Press keys | sends a key combination – `^{Enter}` is Ctrl+Enter |
| Type text | types the text, for a character or phrase you use constantly |
| Surround the selection | wraps the selection, e.g. in `<b>` and `</b>` |
| Search the web for the selection | opens a URL with `{q}` replaced by the selection |
| Open a web page | a bookmark on a key |
| Run a program | launches a file or folder |
| Run a built-in action | any of the actions the menu uses, such as a case conversion |

The **Does** column of the list says what each shortcut will do, in words, so a list of forty keys stays readable.

### In settings.ini

The same bindings are stored under `[Hotkeys]` in `settings.ini`, in AutoHotkey notation: `^` is Ctrl, `!` Alt, `+` Shift, `#` Win. Several keys are separated by `|`, a key is limited to a program with `@`, and a double tap is `DoubleCtrl`, `DoubleShift` or `DoubleAlt`:

```ini
ConfirmSegment=NumpadEnter@ahk_exe memoQ.exe|DoubleCtrl@ahk_exe memoQ.exe
```

You never need to write this yourself; the window does it. It is here for anyone who keeps their settings in version control.

---
title: "Spellcheck"
---

Supervertaler includes a powerful spellcheck system that highlights misspellings while you translate, with support for regional language variants.

For grammar and style as well as spelling, you can also [check the translation with LanguageTool](/workbench/qa/languagetool/).

## How It Works

Supervertaler uses a **three-tier spellcheck system** that automatically selects the best available backend:

| Backend | Description | Languages |
|---------|-------------|-----------|
| **Hunspell (cyhunspell)** | Native C library, best accuracy | Any language with .dic/.aff files |
| **Spylls** | Pure Python Hunspell (recommended for Windows) | Bundled: EN, RU, SV + any .dic/.aff files you add |
| **pyspellchecker** | Built-in fallback | EN, NL, DE, FR, ES, PT, IT, RU |

The system automatically falls back through backends: Hunspell → Spylls → pyspellchecker.

:::note
**Windows Users:** Spylls is automatically used since cyhunspell doesn't compile on Python 3.12+. This works great and supports regional variants!
:::

## Features

- **Red wavy underlines** for misspelled words in the translation grid
- **Right-click context menu** with spelling suggestions
- **Add to Dictionary** – Save a word permanently
- **Ignore** – Skip a word for the current session only
- **Regional variants** – Distinguish between en_US "color" and en_GB "colour"

## Language Variants

Supervertaler supports regional language variants. The spellcheck dropdown shows variants like:

- English (US), English (GB), English (AU), English (CA), English (ZA)
- Portuguese (PT), Portuguese (BR)
- Spanish (ES), Spanish (MX), Spanish (AR)
- French (FR), French (CA), French (BE)
- German (DE), German (AT), German (CH)
- Dutch (NL), Dutch (BE)

:::tip
**Regional spelling works correctly!**
- With **English (GB)**: "colour" ✅ correct, "color" ❌ incorrect
- With **English (US)**: "colour" ❌ incorrect, "color" ✅ correct
:::

## Spellcheck Info Dialog

Access detailed information about your spellcheck setup: click the **📝 Spellcheck** button above the grid and choose **ℹ️ Spellcheck Info** from its menu.

The dialog shows:
- Current language and backend
- Available languages
- Diagnostic information (which backends are available/initialized)
- Links to download additional dictionaries
- Custom dictionary word count

## Adding More Dictionaries

To add spellcheck support for additional languages or variants:

1. **Download Hunspell dictionaries** (.dic and .aff files) from:
   - [hunspell.memoq.com](https://hunspell.memoq.com/) – 70+ languages
   - [GitHub: wooorm/dictionaries](https://github.com/wooorm/dictionaries/tree/main/dictionaries) – 92+ languages
   - [LibreOffice Extensions](https://extensions.libreoffice.org/?Tags%5B%5D=50) – Rename .oxt to .zip

2. **Extract the files** – You need both `.dic` and `.aff` files (e.g., `nl_NL.dic` and `nl_NL.aff`)

3. **Place them in the dictionaries folder:**
   - Open Supervertaler
   - Go to Spellcheck Info dialog
   - Click "📁 Open Dictionaries Folder"
   - Copy your .dic and .aff files there
   - You can also organize in subfolders (e.g., `dictionaries/en/en_GB.dic`)

4. **Restart Supervertaler** – The new language will appear in the dropdown

:::note
**Spylls bundled dictionaries** (EN, RU, SV) are stored inside the spylls pip package, not in your dictionaries folder. Add your own .dic/.aff files to the dictionaries folder to extend available languages.
:::

## Custom Dictionary

You can add words that Supervertaler should always accept:

- **Right-click a "misspelled" word** → **Add to Dictionary**
- Or manage the whole list in **📖 Manage Custom Dictionary…**, in the menu of the **📝 Spellcheck** button above the grid

Custom words are stored permanently and apply to all languages. Case doesn't matter: the list is stored in lower case.

### Managing the list

**📖 Manage Custom Dictionary…** opens the list as plain text, one word per line, which you can edit directly. The buttons above it help with bigger changes (from v1.10.372):

| Button | What it does |
|--------|--------------|
| **📥 Import…** | Adds the words from a text file with one word per line, or from a Hunspell `.dic` file. The word count on the first line of a `.dic` file and the `/FLAGS` after each word are dealt with for you, and words already in your list are not added twice. |
| **📤 Export…** | Saves your list as a text file, for example to back it up or share it with a colleague. |
| **🔤 Sort & remove duplicates** | Sorts the list alphabetically and removes words that appear more than once. |
| **📂 Open folder** | Opens the folder where the list is kept, as `custom_words.txt`. |

The line under the list shows how many words it holds, and how many duplicates will be merged when you save.

:::note
Nothing is saved until you click **💾 Save**. **Cancel** closes the dialog without keeping your changes, including any words you imported.
:::

## Troubleshooting

### Spellcheck not working?

1. **Check the language** – Make sure the correct language variant is selected
2. **Check the backend** – Open Spellcheck Info to see which backend is active
3. **Missing dictionaries** – Some languages require manual dictionary installation

### Wrong language variant?

If you need British English but only have US English:
1. Download `en_GB.dic` and `en_GB.aff` from one of the dictionary sources
2. Place them in your dictionaries folder
3. Select "English (GB)" from the dropdown

### Linux crashes?

On Linux, some Hunspell configurations can cause crashes. Try:
- Installing proper Hunspell dictionaries: `sudo apt install hunspell-<lang>` (e.g., `hunspell-pl` for Polish)
- Temporarily disabling spellcheck in Settings → View Settings
- See [Linux-Specific Issues](/workbench/troubleshooting/linux/) for more details

## Technical Details

For developers and advanced users:

| Project | Description |
|---------|-------------|
| [pyspellchecker](https://github.com/barrust/pyspellchecker) | Built-in word frequency spellcheck |
| [spylls](https://github.com/zverok/spylls) | Pure Python Hunspell implementation |
| [Hunspell](http://hunspell.github.io/) | Original C/C++ spellcheck library |

The spellcheck manager is located in `modules/spellcheck_manager.py` and provides:
- Automatic backend selection
- Dictionary file detection (including subdirectories)
- Word caching for performance
- Custom dictionary management

---
title: "Snippets, bookmarks and conversions"
---

Everything on Sidekick's menu is data. The menu is built when Sidekick starts from `data\menu.json`, a file that stays on your machine, and the **Library Editor** changes it without touching the program.

### Snippets

Text inserted at the cursor: boilerplate, standard replies, special characters, regex patterns, dictionary citations. The starter set has an HTML section, twenty-eight special characters (en and em dashes, arrows, primes, accented vowels, subscripts and superscripts, non-breaking space, ™ ® © and so on) and a couple of regex patterns. Pick one from the menu or type its name into the [palette](/sidekick/window/#the-palette--ctrlaltspace).

### Bookmarks

Web addresses and local files or folders you keep reopening: forums, documentation, reference sites, client folders.

### Text conversions

Act on the selection and paste the result back: upper, lower, title and sentence case; single and double curly quotes; round and square brackets; remove soft hyphens; convert double quotes to single; HTML bold. Handy for technical translators who spend their day tidying other people's text.

### The Library Editor

Open **Settings → Edit library…** (or press the key you give it – see [Keyboard shortcuts](/sidekick/keyboard-shortcuts/)). The tree on the left mirrors the menu: its headings become sections, submenus hang under them, and every entry – snippet, search, AI prompt, bookmark, conversion – is reachable. Add, edit, delete and reorder; press **Save & rebuild** and the menu updates without a restart.

### Entry types

Each entry has a kind that decides what it does with the selection:

| Kind | What it does |
|---|---|
| `text` | types out literal text |
| `keys` | sends a key combination, e.g. `^+*` |
| `url` | opens a web address |
| `run` | launches a file or folder |
| `search` | looks the selection up at a URL, with `{q}` replaced by it and `{sl}`/`{tl}` by the language pair – see [Searches](/sidekick/searches/) |
| `multisearch` | opens several search URLs at once in a new browser window – see [Searches](/sidekick/searches/#multisearch--a-batch-at-once) |
| `ai` | runs an AI prompt over the selection – see [AI actions](/sidekick/ai-actions/) |
| `action` | calls a built-in function, such as a case conversion |
| `submenu` | holds other entries |
| `heading`, `separator` | structure only |

The file is plain JSON, so it can also be edited by hand, kept in version control, or copied to another machine.

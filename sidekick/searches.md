---
title: "Web and local searches"
---

Select a term, open the menu, pick a source: the term is looked up there in your browser, in the language pair you are working in. That is a search entry, and the starter menu has twenty of them – IATE, Juremy, JurLex, Van Dale, Linguee, ProZ, Reverso, BabelNet, FELOnline, AcronymFinder, Oxford, Microsoft Terminology, Wikipedia, Wiktionary, Google Patents and Google itself.

### The language pair

One pair serves the whole program: the searches and [QuickTrans](/sidekick/quicktrans/) both read it, and the tray icon's tooltip shows it. Set it in any of three places:

- the **From** and **To** dropdowns in the QuickTrans tab of the [window](/sidekick/window/)
- **Settings → Language pair…**, a small dialog with the same two dropdowns
- **Settings → Swap languages**, which flips the direction – put it on a [key](/sidekick/keyboard-shortcuts/) if you work both ways

Change it once and every search follows. An IATE lookup is one menu entry whether you translate Dutch to English or German to French.

### A search is one line

Adding a source of your own is one entry in the [Library Editor](/sidekick/library/#the-library-editor): a label and an address with placeholders where the term and the languages go.

```json
{
  "kind": "search",
  "label": "IATE",
  "url": "https://iate.europa.eu/search/byUrl?term={q}&sl={sl}&tl={tl}"
}
```

| Placeholder | Becomes | For Dutch → English |
|---|---|---|
| `{q}` | the selected text, percent-encoded | `warmtewisselaar` |
| `{sl}` `{tl}` | two-letter codes | `nl` `en` |
| `{sl_upper}` `{tl_upper}` | the same in capitals | `NL` `EN` |
| `{sl_full}` `{tl_full}` | the language's English name | `dutch` `english` |
| `{sl3}` `{tl3}` | three-letter codes (ISO 639-2/T) | `nld` `eng` |
| `{sl3b}` `{tl3b}` | three-letter codes, bibliographic (ISO 639-2/B) | `dut` `eng` |

Most sites take the two-letter codes. Reverso and Linguee want names, Juremy wants `nld`, ProZ wants `dut`; the starter entries show which is which. The placeholders are the ones SuperLookup used, so a resource list from there transfers unchanged.

The selection is percent-encoded before it is substituted, so terms containing `&`, `?`, `+` or accented characters work. Any site whose search results have their own URL can be a source, and a key in [Keyboard shortcuts](/sidekick/keyboard-shortcuts/) makes the lookup one keystroke from anywhere.

**Sites with no code in the URL.** Van Dale names its dictionaries `gne` and `gen`; JurLex has session ids. There is no placeholder for those, so such an entry carries one address per pair instead, under `by_pair` in `menu.json`:

```json
{
  "kind": "search",
  "label": "Van Dale (Dutch/English)",
  "by_pair": {
    "nl-en": "https://zoeken.vandale.nl/?dictionaryId=gne&query={q}",
    "en-nl": "https://zoeken.vandale.nl/?dictionaryId=gen&query={q}"
  }
}
```

When the current pair is not in the list, the entry says so rather than opening the wrong dictionary.

### MultiSearch – a batch at once

**MultiSearch** opens a whole set of sources in one go, each in its own tab of a fresh browser window, for the current pair. Read down the tabs, close the window, done. The starter batch is eleven sources: Google Patents, IATE, ProZ, Beijerterm, Reverso, Juremy, Linguee, Wikipedia, Wiktionary, AcronymFinder and BabelNet.

It is an entry of kind **multisearch** in the Library Editor: one address per line, the same placeholders. Make as many batches as you like – one for legal, one for engineering – and give each a key.

The window opens in your default browser. Chrome, Edge, Brave and the other Chromium browsers open the whole batch in one new window; Firefox opens the first in a new window and the rest as tabs in it. Anything else gets the tabs in the current window.

### Local searches

- **Google the selection** – `Ctrl+/`
- **Search the desktop** – `Ctrl+Shift+D` – hands the selection to dtSearch, if you have it
- Entries for desktop terminology tools such as LogiTerm ship in the starter set and are easy to drop if you do not use them

### Other language pairs

Every source is pair-aware, so a German-to-English translator sets the pair once and the starter sources just work – IATE, Linguee, ProZ, Reverso, Juremy, BabelNet, Wikipedia and Wiktionary all cover it. The two Dutch-only dictionaries stay put and say so when asked. Ready-made packages of the sites translators in a given pair actually use are planned, so a new install starts with the right list rather than someone else's.

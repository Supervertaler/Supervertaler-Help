---
title: "Web and local searches"
---

Select a term, open the menu, pick a source: the term is looked up there in your browser, in the language pair you are working in. That is a search entry. The starter menu has the sources that work for any language – IATE, Juremy, Linguee, ProZ, Reverso, BabelNet, AcronymFinder, Microsoft Terminology, Wikipedia, Wiktionary, Google Patents and Google itself – and [language packs](#language-packs) add the ones that belong to one language.

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

**Sites with no code in the URL.** Some sites bake the pair into an opaque id – Van Dale, for example, names its Dutch–English and English–Dutch dictionaries `gne` and `gen`. There is no placeholder for those, so such an entry carries one address per direction instead, under `by_pair`:

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

**MultiSearch** opens a whole set of sources in one go, each in its own tab of a fresh browser window, for the current pair. Read down the tabs, close the window, done. The starter batch, at the top of Web searches, is eleven sources: Google Patents, IATE, ProZ, Beijerterm, Reverso, Juremy, Linguee, Wikipedia, Wiktionary, AcronymFinder and BabelNet. A language pack brings its own batch for its pair.

It is an entry of kind **multisearch** in the Library Editor: one address per line, the same placeholders. Make as many batches as you like – one for legal, one for engineering – and give each a key.

The window opens in your default browser. Chrome, Edge, Brave and the other Chromium browsers open the whole batch in one new window; Firefox opens the first in a new window and the rest as tabs in it. Anything else gets the tabs in the current window.

### Language packs

A **language pack** is everything for one language pair, both directions: the bilingual sites, the monolingual dictionaries on either side, and a MultiSearch that opens them all at once. A Dutch and English translator installs **Dutch ⇄ English** and has the lot; a Dutch and German translator installs **Dutch ⇄ German** and nothing else. The installed pack for the pair you are working in appears as one folder at the top of **Web searches**, named after the pair – "Dutch ⇄ English (language pack)" – so a translator with several installed sees the right one after switching the pair.

**Settings → Language packs…** lists the packs Sidekick ships, one checkbox each. Until you save that dialog, the pack for your current pair is installed automatically if there is one, so a fresh install with Dutch → English gets Dutch ⇄ English without being asked.

Pack entries are never written into your menu, so removing a pack is one untick, and the Library Editor only ever shows your own entries.

Sidekick ships Dutch ⇄ English today, with thirteen sources: a MultiSearch over the pair, Beijerterm, Mijnwoordenboek, Woordenlijst, Synoniemen.net, Encyclo, Merriam-Webster, Cambridge, Collins, OneLook, Thesaurus.com, Wordnik and Ludwig. A pack is a small JSON file in the `packs\` folder of the Sidekick folder, in exactly the format of a search entry, so a pack for another pair is a matter of writing one – and contributing it back on GitHub so the next translator in that pair starts with it.

### Local searches

- **Google the selection** – `Ctrl+/`
- **Search the desktop** – `Ctrl+Shift+D` – hands the selection to dtSearch, if you have it
- Entries for desktop terminology tools such as LogiTerm ship in the starter set and are easy to drop if you do not use them

### Other language pairs

Every source is pair-aware, so a German-to-English translator sets the pair once and the starter sources just work – IATE, Linguee, ProZ, Reverso, Juremy, BabelNet, Wikipedia and Wiktionary all cover it. The pair's own sources come from a [language pack](#language-packs); Dutch ⇄ English exists, and more are welcome.

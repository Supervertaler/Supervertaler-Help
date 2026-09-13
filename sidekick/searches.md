---
title: "Web and local searches"
---

Select a term, open the menu, pick a source: the term is looked up there in your browser. That is a search entry, and the starter menu has twenty-five of them – IATE, Juremy, JurLex, Van Dale, Linguee, ProZ, Reverso, BabelNet, FELOnline, AcronymFinder, Oxford, Microsoft Terminology, Wikipedia, Wiktionary, Google Patents and Google itself – most in both directions for Dutch and English, because that is the pair Sidekick grew up with.

### A search is one line

Adding a source of your own is one entry in the [Library Editor](/sidekick/library/#the-library-editor): a label and an address with `{q}` where the term goes.

```json
{
  "kind": "search",
  "label": "Wiktionary (English)",
  "url": "https://en.wiktionary.org/wiki/{q}"
}
```

The selection is percent-encoded before it is substituted, so terms containing `&`, `?`, `+` or accented characters work. Any site whose search results have their own URL can be a source. Give the entry a key in [Keyboard shortcuts](/sidekick/keyboard-shortcuts/) and the lookup is one keystroke from anywhere.

### MultiSearch

**Web searches (multiple engines)** fires a whole batch at once – one browser tab per source – for the pair you choose. The starter set has a Dutch-to-English and an English-to-Dutch batch. Which sources go into a batch is set in the same editor.

### Local searches

- **Google the selection** – `Ctrl+/`
- **Search the desktop** – `Ctrl+Shift+D` – hands the selection to dtSearch, if you have it
- Entries for desktop terminology tools such as LogiTerm and UniLex ship in the starter set and are easy to drop if you do not use them

### Other language pairs

Every source is an editable entry, so a German-to-English translator can replace the Dutch ones in a few minutes. Ready-made search packages per language pair – the sites translators in that pair actually use – are planned, so that a new install starts with the right sources rather than someone else's.

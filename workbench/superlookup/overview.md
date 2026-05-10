{% hint style="info" %}
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
{% endhint %}

SuperLookup is your unified concordance and research hub, bringing together all lookup resources in one place. It lives inside the **Sidekick** panel as its own tab.

## Opening SuperLookup

| How | Shortcut | Notes |
|-----|----------|-------|
| From the translation grid | **Ctrl+K** | Opens Sidekick directly to the SuperLookup tab; selected text is used as the search query automatically |
| From any application (system-wide) | **Ctrl+Alt+L** | Select any text in any app, press the shortcut, and SuperLookup opens with that text pre-filled. Sidekick stays above other windows (including Trados Studio) while it's visible. The sub-tab it lands on is configurable – see **Configurable landing tab** below. |
| From any application (system-wide) | **Ctrl+Alt+Q** | Same as Ctrl+Alt+L but always lands on the QuickTrans sub-tab and starts the MT fan-out immediately. |
| Via Sidekick | **Ctrl+Alt+K** (⌘⌥K on macOS) then click the SuperLookup tab | Ctrl+Alt+K opens Sidekick to whatever tab was last active; click SuperLookup, or right-click the tab title and set it as the default |

## Configurable landing tab

By default, Ctrl+Alt+L lands on the **Termbases** sub-tab. You can change this in **SuperLookup Settings → "Ctrl+Alt+L lands on"** – pick from QuickTrans, TMs, Termbases, or Web Resources. The choice persists across restarts. Whichever sub-tab you choose is fired immediately on the hotkey; the others are deferred until you actually navigate to them, so you don't pay the cost of work you may not look at.

## Tabs

### TM Matches

Search your Translation Memories for similar text:
- Fuzzy matching with percentage scores
- Horizontal (table) or vertical (list) view toggle
- Source TM column shows which TM the match came from
- Search direction: Both, Source only, or Target only

### Glossary Matches

Search your termbases and glossaries:
- Shows Source, Target, Domain, Notes columns
- Right-click to "Edit in Glossary"
- Direction and language filters (Both / Source / Target + From/To)

### Supermemory

Semantic search across all your TMs:
- Finds conceptually similar text (not just word matches)
- Uses AI embeddings to understand meaning
- Useful for finding paraphrased or reworded content

### Machine Translation

Get instant MT from multiple providers:
- Google Translate, DeepL, Microsoft Translator
- Amazon Translate, MyMemory, ModernMT

Configure providers in **Settings → MT Settings**.

### Web Resources

Quick access to online reference sites: IATE, Linguee, ProZ.com, Reverso Context, Wikipedia, Wiktionary, Google, Google Patents, Juremy, AcronymFinder, BabelNet, and more.

Web resource tabs maintain login sessions between searches, so you stay logged in to sites like ProZ.com.

## Search controls

**Language filters** – use the **From** and **To** dropdowns to filter by language pair. Auto-populated from your TMs and termbases.

**Search direction** – **Both** searches source and target columns; **Source** and **Target** restrict to one side.

**Search box** – type a query and press Enter (or click 🔍). When Ctrl+K or Ctrl+Alt+L opens SuperLookup, the selected text is placed in the search box and the search runs immediately.

## Tips

- Double-click a result to copy it to the clipboard.
- Right-click a result for additional options.
- To always open Sidekick to SuperLookup, right-click the SuperLookup tab title and choose **Set as default tab**.

---

## Related pages

- [Sidekick Overview](../sidekick/overview.md)
- [TM Concordance Search](tm-search.md)
- [Glossary Search](glossary-search.md)
- [Machine Translation](mt.md)
- [Web Resources](web-resources.md)

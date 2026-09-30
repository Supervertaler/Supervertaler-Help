---
title: "Web Resources"
---

SuperLookup’s **Web Resources** tab gives you a one-click sidebar of reference sites for terminology and research.

## How it works

- You use the **main SuperLookup search box** (top of the window) and click **Search**.
- The Web Resources tab uses your **From → To** language direction when building URLs.

## Browser modes

In the left sidebar you can choose a mode:

- **Embedded:** opens sites inside Supervertaler (requires `QtWebEngine`).
	- Uses a persistent browser profile so logins/cookies are kept between sessions.
- **External:** opens your default browser.

:::note
When Embedded mode is available, SuperLookup can pre-load searches for all resources at once.
:::

## Search options

- Select a single resource (e.g. IATE) and click **Search**.
- Click **Search All** to load results for all resources (Embedded mode).
- Use **Open in Browser** to open the last search URL in your default browser.

## Included resources

The sidebar includes (by default):

- IATE
- Linguee
- ProZ.com
- Reverso Context
- Google Search
- Google Patents
- Wikipedia (Source)
- Wikipedia (Target)
- Juremy
- Beijerterm
- AcronymFinder
- BabelNet
- Wiktionary (Source)
- Wiktionary (Target)
- GitHub Code (all)
- OPUS Corpus

## Add your own resources

Below the built-in sites you can add lookup sites of your own. Click **⚙ Custom Resources…** in the sidebar, just below the list of sites, to open the **Custom Web Resources** dialog.

To add a site:

1. In your browser, search for something on the site.
2. Copy the address of the results page.
3. In the dialog, click **➕ Add**, type a **Name**, and paste the address.
4. Replace the search term in the address with `{query}`. For example, a search for *Haus* on DWDS gives `https://www.dwds.de/?q=Haus`, which becomes `https://www.dwds.de/?q={query}`.
5. Click **OK**.

The address can also use the same language placeholders as the built-in resources, so a dictionary can follow your **From → To** language pair:

| Placeholder | Inserts | Example |
|-------------|---------|---------|
| `{query}` | the search term (required) | |
| `{sl}` / `{tl}` | source / target language code | `en`, `nl` |
| `{sl_upper}` / `{tl_upper}` | the code in capitals | `EN`, `NL` |
| `{sl_full}` / `{tl_full}` | the language name in lower case | `english`, `dutch` |

Your own sites work like the built-in ones: embedded or in your browser, and included in **🔎 Search All**. They appear with a 🔗 icon below the built-in sites. In the dialog you can rename them (edit the name), reorder them with **▲** and **▼**, and delete them with **🗑 Remove**. They are remembered between sessions.

:::note
Only `https://` and `http://` addresses are accepted, and the address must contain `{query}` and no spaces.
:::

## Show/hide resources

In **SuperLookup → ⚙️ SuperLookup Settings → 🌐 Web Resources**, you can toggle which built-in sites appear in the sidebar. To remove one of your own sites, use **⚙ Custom Resources…**.

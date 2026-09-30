---
title: "Check with LanguageTool"
---

**QA → 📝 Check with LanguageTool…** checks the **target** text of every segment for grammar, spelling and style mistakes with [LanguageTool](https://languagetool.org/). LanguageTool is particularly good at German and Dutch grammar, and catches grammar mistakes that a spellchecker can't.

It checks when you ask it to and lists what it finds. It does not underline mistakes as you type – that is what [Spellcheck](/workbench/qa/spellcheck/) is for.

## Public service or your own server

The **Server** box at the top of the LanguageTool window decides where your text is checked. Pick one of the two addresses in the list, or type your own:

| Server | What it means |
|--------|---------------|
| `https://api.languagetool.org` *(default)* | LanguageTool's free public service. No setup needed, but your text goes to LanguageTool's servers, and it allows about 20 checks a minute. |
| `http://localhost:8081` | A LanguageTool server running on your own computer. Free, no limits, and the text never leaves your machine. |

The address you last checked with is remembered for next time.

### What's sent, and privacy

- Only the **target** text is sent, one request for many segments at a time. Source text, comments and project details are not sent. Segments with no translation yet are skipped.
- The text is sent as it appears in the target cell, inline tags included.
- With the **public service**, that text is processed on LanguageTool's servers. A line under the Server box reminds you of this. For confidential work (or anything your client's NDA covers), use your own server instead: the note then changes to "Using your own LanguageTool server – the text stays there."
- If you have set up a proxy under **Settings → AI Settings → 🌐 HTTP Proxy Settings**, checks go through it, except for a server on `localhost` or `127.0.0.1`.

### Running your own LanguageTool server

LanguageTool is open source, and its server runs anywhere Java does. Supervertaler doesn't install or start it for you. Download LanguageTool, start its HTTP server, for example with

```
java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081
```

and enter `http://localhost:8081` (or whatever address and port you used) in the **Server** box. LanguageTool's own documentation explains the options.

### The public service's limits

The free public service allows about 20 checks a minute and limits the size of each one. Supervertaler sends many segments per request and spaces the requests out automatically, so a large project simply takes a while. If the limit is reached anyway, you're told so: wait a minute and try again, or use your own server.

## Language

The **Language** box is filled in from the project's target language, as a LanguageTool code such as `nl`, `de-DE` or `en-GB`. You can change it for one check, for example to `nl-BE` or `de-CH`, or type `auto` to let LanguageTool work it out. The next time you open the window from the QA menu it starts from the project's language again.

:::tip
LanguageTool needs a regional variant to check spelling in some languages, so a plain project language is filled in with a default: English becomes `en-US`, German `de-DE`, Portuguese `pt-PT`. If your project's target is plain "English" and you write British English, change the box to `en-GB`.
:::

LanguageTool supports many languages, but not all of them. For a language it doesn't support, the check stops with the server's error message.

## Running a check

1. Choose **QA → 📝 Check with LanguageTool…**.
2. Check the **Server** and **Language** boxes.
3. Click **▶ Check target segments**.

A progress bar shows how far it has got, and **Cancel** stops a long check; the findings so far are kept, marked "(stopped early)". The window stays open while you work in the grid.

## Working through the findings

Each finding is one row:

| Column | What it shows |
|--------|---------------|
| **Segment** | The segment number |
| **Issue** | LanguageTool's explanation, with its category in brackets. Hover over it to see the rule's ID. |
| **Found** | The flagged words |
| **Suggestions** | Up to five suggestions, separated by vertical bars (or – when there are none) |
| **Context** | The text around the flagged words, which are shown in `[brackets]` |

What you can do with a finding:

- **Double-click** it to go to its segment in the grid.
- **Right-click** it and choose **Replace with “…”** to use any of the suggestions, or **Go to segment** or **Ignore**.
- Select it and click **✔ Apply first suggestion** to use the first suggestion.
- Select it and click **Ignore** to remove it from the list.

Applying a suggestion changes the target text straight away, and **Ctrl+Z** undoes it. The segment keeps its status. If you have edited the segment since the check and the flagged words are no longer there, nothing is changed and you're asked to run the check again.

**Ignore** only removes the finding from this list; it will be found again the next time you run the check.

## Related

- [Spellcheck](/workbench/qa/spellcheck/) – red underlines as you type
- [QA Checks](/workbench/qa/qa-checks/) – your own saved checks, and tags & codes
- [AI Proofreading](/workbench/qa/proofreading/) – a review of meaning, terminology and style by an AI model

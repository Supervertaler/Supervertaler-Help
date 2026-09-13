---
title: "Text expansion"
---

Type an abbreviation, get the full text. Text expansion watches what you type and replaces a short trigger with its expansion the moment you finish it – `adr` becomes your address, `ovw` becomes *overeenkomstig*, `tabb` becomes a tab character.

It is not the same as a [text conversion](/sidekick/library/#text-conversions), which acts on text you have already selected. Expansion has no selection at all; it works on the keystrokes themselves.

### Editing expansions

Open **Settings → Text expansions…**. Each row is a trigger and what it expands to. Add, edit and delete, then save: Sidekick reloads and the new entries are live.

The entries live in `data\expansions.json`, alongside your other content. See [Settings and files](/sidekick/settings/).

### Built for thousands of entries

This is the one feature that has to be fast on every keystroke of every day, and a working translator's list grows into the thousands. Registering entries one by one at start-up would cost seconds; instead Sidekick writes the list out as a generated script when you save and includes it, so five thousand entries load in a few milliseconds and typing costs nothing. Editing costs one reload.

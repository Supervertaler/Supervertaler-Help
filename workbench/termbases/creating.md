---
title: "Creating Termbases"
---

Termbases help you enforce terminology consistently.

## Create a termbase

1. Open **Project resources → Termbases**
2. Click **Create Termbase**
3. Give it a name and select languages

## Add terms while translating

You can build terminology as you work:

- Select text in both Source and Target
- Use **Add to Termbase** from the context menu

The right-click menu offers several routes: **Add to Termbase** (`Ctrl+Alt+T`, opens the entry dialog), and the quick-adds **Quick Add to Termbase** (`Alt+Left`), **Quick Add to Project Termbase** (`Alt+Up`), and **Quick Add to Background Termbase** (`Alt+Down`).

## Similar Term Found — merge as a synonym

If the term you are adding shares its source with an existing entry (but has a different target), or shares its target (but a different source), Workbench shows a **Similar Term Found** prompt instead of silently creating a near-duplicate. You can:

- **Add as Synonym** — fold the new term into the existing entry as a synonym
- **Add & Edit…** — do that, then open the entry editor to review it
- **Keep Both** — create a separate entry anyway
- **Cancel** — abandon the add

The prompt only appears when there is an actual overlap, so the quick-adds stay instant otherwise. Exact duplicates (same source *and* target) are skipped as before. This matches the behaviour of the Supervertaler for Trados plugin.

## Tips

- Use a separate termbase per client when terminology differs.
- Add high-priority terms first (product names, UI strings).

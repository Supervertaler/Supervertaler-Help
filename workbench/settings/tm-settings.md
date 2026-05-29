---
title: "TM Settings"
---

The **TM settings** box (Settings → General) controls how translation memory matches are inserted and propagated as you work.

## Auto-fill empty segments with 100% TM matches

When you select an empty segment that has a 100% TM match, its translation is filled in automatically. This saves time on repetitive content – exact matches appear without any manual action.

:::note
Only empty segments are auto-filled. Segments that already contain a translation are left untouched.
:::

- **↳ Mark auto-filled segments as confirmed** – when enabled, an auto-filled segment lands as **confirmed**. Otherwise the auto-filled translation is inserted as a **draft** for you to review.

## Auto-propagate confirmed translations to identical segments

When you confirm a segment, its translation is copied to every other segment whose source text is identical. This is the memoQ/Trados-style propagate-on-confirm behaviour – translate a repeated sentence once, confirm it, and the rest of the document catches up automatically.

By default, only **empty** identical segments are filled, and they are inserted as drafts.

- **↳ Mark propagated segments as confirmed** – propagated segments land as **confirmed** instead of **draft**.
- **↳ Overwrite existing translations when propagating** – propagation also replaces existing target content in identical segments. When disabled, only empty segments are filled.

## Auto-confirm 100% TM matches when navigating (Ctrl+Enter)

When enabled, pressing **Ctrl+Enter** automatically inserts, confirms, and skips past any segment that has a 100% TM match, so you can move quickly through perfect matches.

- **↳ Also overwrite existing translations with 100% TM matches** – auto-confirm also replaces existing target content (including pre-translations or machine translations) with the 100% match.

## TM Save Mode

Controls what happens when the same source segment is saved to the TM more than once.

- **Save all translations (with timestamps)** – keeps every version of a translation for a given source, with timestamps. The most recent translation is preferred when showing matches.
- **Save only latest translation (overwrite)** – keeps only the most recent translation, overwriting older ones. This prevents the TM from growing with obsolete entries. *(Default.)*

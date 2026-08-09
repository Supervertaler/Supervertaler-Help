---
title: "Quick Add (Ctrl+Alt+M)"
description: "Capture a term decision without leaving the segment"
---

You have just worked out how a term should be translated for this client. Quick Add records that decision without breaking your rhythm: it appends one row to the active bank's `terminology.md` and puts you back in the segment.

## How to use

1. In the Trados editor, select the source text you want to capture. (Optional — the whole source segment is used if you select nothing.)
2. Press **Ctrl+Alt+M**, or right-click and choose **Add to SuperMemory**.
3. Fill in the dialogue:
   * **Source term** — pre-filled from your selection. The label names your project's source language.
   * **Target term** — pre-filled from the target selection if you made one.
   * **Notes** — why, or when it applies. This is the part that will matter in six months.
   * **Save as raw note** — puts the text in `reference/` instead of the table, for when the decision is not settled enough to be a row.
   * **Also append to active translation prompt** — adds the same pair to the TERMINOLOGY table in your [active prompt](/trados/ai-assistant/super-memory/active-prompt/), so it takes effect on the very next Ctrl+T.
4. Click **Add**.

The row lands in whichever bank is selected in the toolbar dropdown. To capture into a different bank, switch first.

## What gets written

One row, appended to the table in `terminology.md`:

```markdown
| fiche | plug | client | Only in the electrical sense; elsewhere "sheet" |
```

Successive additions accumulate in the same table rather than scattering, so the bank stays something you can read start to finish.

The **Scope** column is filled in as `client`, which is the safe default — it means "true for this client". If a decision later turns out to hold for other clients too, move the row to the `_shared` bank so every client gets it. Move rather than copy, or the two drift apart.

:::note
If the bank's `terminology.md` has no table yet — which is the case for a bank converted from the old layout, where terminology arrives as prose — Quick Add creates one under a **Quick-added terms** heading at the end of the file. Your converted content is left alone.
:::

## Raw notes

Tick **Save as raw note** and the text goes to the bank's `reference/` folder instead, as a plain Markdown note.

Use it when the knowledge is not yet a decision: *"fiche can mean either sheet or plug depending on context — check with the client"*. A table row states a rule, and a rule you are not sure about is worse than a note that says you are not sure.

Nothing reads `reference/` automatically. When you have settled the question, write the row yourself.

## Review what you capture

Quick Add writes what you type, with no AI step in between. That is the point — but it also means a typo in the target term becomes a rule the AI follows.

Open `terminology.md` now and again (**📂 Open folder** in the toolbar) and read down the table. That is a two-minute job for a bank of a hundred rows, and it is the whole reason terminology is kept as a table rather than as a folder of files.

## Related

* [**SuperMemory**](/trados/ai-assistant/super-memory/) — how a bank is structured
* [**Active Prompt**](/trados/ai-assistant/super-memory/active-prompt/) — the prompt Quick Add can also append to
* [**Keyboard Shortcuts**](/trados/keyboard-shortcuts/) — the full list

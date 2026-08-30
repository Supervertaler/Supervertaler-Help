---
title: "Terminology"
---

Supervertaler reads a glossary file and uses it in two places at once: memoQ's terminology pane, and the AI's prompt.

### Why a file, and not a memoQ term base

memoQ does not let a plugin read its own term bases. A term base attached to your project is visible to you and to memoQ's QA, but not to a machine-translation plugin — so a term marked forbidden in memoQ will not, on its own, stop the AI using it.

Supervertaler works around this by being a terminology source in its own right. Terms in its glossary reach the model because Supervertaler puts them there.

### Setting it up

**Options → Terminology plugins.**

1. Tick **Perform terminology plugin lookups while working in the translation grid**. Nothing happens until this is on.
2. Find **Supervertaler terms** in the list. It reads *Not configured* until a glossary is set.
3. Click its **Options**, choose your glossary file, press OK.
4. Tick **Enable plugin**.

Restart memoQ.

The same glossary setting is reachable from the translation engine's options dialog — both halves of the plugin read one file.

### What you get

**In the grid.** Matched terms are highlighted in the source segment: green for approved terms, red for forbidden ones.

**In Translation results.** Each match appears as an entry showing the target term, the source term it matched, and — for a forbidden term — the wording struck through under *Do not use*.

**In the prompt.** Approved terms are sent as the client's preferred wording; forbidden terms as absolute constraints.

### Preferred, not mandatory

Approved terms are given to the model as a strong steer it may override when an entry is clearly wrong for the sentence at hand.

That asymmetry is deliberate, and it comes from a real failure. A patent term base may quite correctly render *applications* as *aanvragen* — in the sense of a patent application. Told to use terminology verbatim, the model translated "Mashup applications" as "Mashup-aanvragen", which is nonsense. A translator treats a term base as guidance they may set aside with reason, and the model is asked to do the same.

**Forbidden terms are not softened.** They are stated as absolute, because that is what a forbidden term is for.

### Format

See [Glossary format](glossary-format.md).

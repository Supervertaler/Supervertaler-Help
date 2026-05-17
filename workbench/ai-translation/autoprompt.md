---
title: "Autoprompt"
---

:::note
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
:::

AutoPrompt uses an LLM to analyse your current project and generate a comprehensive, project-specific translation prompt. The generated prompt embeds the document's domain, language pair, glossary, confirmed translations, detected source defects, terminology collisions, and preference cascades – ready to use as the **Custom Prompt** for AI translation.

## When to use it

AutoPrompt is most useful when:

- You are starting a new project and want a strong starting prompt instead of writing one from scratch.
- You are translating in an unfamiliar domain and want the LLM to identify the EPO / IFRS / Terminologia Anatomica / domain conventions for you.
- You want the prompt to reflect terminology decisions already made elsewhere in the project (confirmed segment translations, attached termbase) without having to retype them.

If you already have a hand-tuned prompt that works for your client, you do not need AutoPrompt – just keep using it.

## Launching it

1. Open the **AI** tab.
2. In the **Prompt Manager** sub-tab, click **✨ AutoPrompt** in the toolbar above the prompt tree.
3. The analysis runs in the AI Assistant chat panel – progress messages appear as it works.
4. When generation finishes, the new prompt is saved to the **Translate** category in your prompt library and is automatically selected as the **Custom Prompt ⭐** for this project.

## What gets analysed

AutoPrompt gathers the following from your project and sends it to your configured AI provider:

| Data | Purpose |
|---|---|
| **Full source document** (up to 50,000 characters) | Domain detection, terminology extraction, defect detection, cascade detection, project-context summary |
| **All termbase entries** | Locked glossary embedded in the generated prompt |
| **Confirmed segment translations** | Used as TM anchors – the highest-authority style and terminology reference, because they are decisions you have already made for this exact document |
| **Translation Memory entries** (if attached) | Style anchors – the LLM matches the register and lexical choices of validated TM pairs |
| **Language pair** | Embedded in the generated prompt |

:::note
For a typical 30,000-word document, AutoPrompt costs roughly $0.20–$0.25 with a Sonnet-class model, or $1.00–$1.15 with an Opus-class model. The full document is sent so the LLM can actually read it and detect real patterns rather than guessing from metadata.
:::

## Source-aware pre-generation passes

Before the meta-prompt is sent to the LLM, Workbench runs several lightweight passes against the source content and injects the findings into the meta-prompt. The findings tell the LLM what to look for and give it concrete document-specific anchors instead of generic scaffolding.

### Domain detection

A keyword-based local pass classifies the document into one of:

- **Patent** – claims, embodiments, prior art, figure references, EP / US / WO patent numbers
- **Legal** – contracts, clauses, statutory references, notarial titles
- **Medical** – clinical terms, dosages, ICD / ATC codes, anatomical terminology
- **Technical** – specifications, software terms, standards
- **Financial** – figures, IFRS / GAAP, regulatory language
- **Marketing** – brand, audience, campaign language
- **General** – fallback for mixed or unclassified content

Keywords are recognised in English, Dutch, and (for high-signal terms) German and French. A separate patent-marker check looks for `conclusie N` / `claim N`, `volgens conclusie`, `uitvoeringsvorm`, `stand der techniek`, `omvattende`, `FIG.` references, and patent-number citations – when three or more distinct markers are present, the domain is locked to **patent** regardless of which other domain happens to have the highest keyword score. This catches the common failure mode where a Dutch or German patent gets misclassified as "legal" because patent applications look superficially legal.

### Terminology-collision detection

A built-in helper scans for known cross-term collisions in the source – groups of source-language terms whose natural English candidates would all map to the same target. Currently the helper covers Dutch mechanical / patent vocabulary (the highest-traffic source-language case): the `mantel` / `huls` / `mantelbuis` / `beschermhuls` cluster, the `pijp` / `buis` / `flexibele buis` cluster, the `voorzijde` / `voorvlak` / `achterzijde` distinction, and the `as` (axle vs geometrical axis) homograph. Each detected collision is presented with the EPO-conventional resolution so the LLM-generated prompt locks the correct mapping rather than picking arbitrarily.

For any other source language or any other domain, the meta-prompt instructs the LLM to **perform its own collision scan** using patterns appropriate to the actual source language and detected domain – with explicit examples for medical (`arteria vs vena`, ligament vs tendon), legal (`agreement vs contract vs covenant`, liability vs responsibility), and financial (`revenue vs turnover vs sales`) collisions. The LLM-driven scan works for every language pair Workbench supports.

### Defect-detection pass

A built-in helper extracts up to five verbatim defect examples from the source – hanging mid-sentence breaks ending in subordinating conjunctions, doubled spaces, plausible verb-ending typos (Dutch `-d` / `-t` confusion), and broken-compound double-space patterns. The Dutch-specific conjunction list catches the highest-traffic case; for other languages the meta-prompt instructs the LLM to perform the scan itself using equivalents in the actual source language (`weil` in German, `parce que` in French, `porque` in Spanish, `perché` in Italian, etc.).

Quoting real defects in the generated prompt is far more effective than abstract "preserve defects faithfully" rules – the translator AI sees the actual surface forms it will encounter, not hypothetical examples.

### Preference-cascade extraction

A built-in helper extracts up to three real `bij voorkeur ... bij nog meer voorkeur` cascades from Dutch sources (and `preferably ... more preferably ... even more preferably` from English). For other languages the meta-prompt instructs the LLM to look for source-language equivalents – `vorzugsweise / besonders bevorzugt` in German, `de préférence / plus préférablement` in French, `preferiblemente / más preferiblemente` in Spanish, `preferibilmente / più preferibilmente` in Italian, and `preferencialmente / mais preferencialmente` in Portuguese.

Quoting one real cascade from the source anchors the generated prompt's anti-truncation rule in a concrete example: "preserve THIS pattern, here is one from your own document".

### TM-anchor wiring

Confirmed source → target pairs from the project's own segments are surfaced as TM anchors of the highest authority – they are locked decisions for this exact document. Pairs from any separately-attached `.tm` file are added with lower priority. If neither source has any pairs, the generated prompt's "Previous Correct Translations" section is omitted entirely (rather than padded with "No TM data available", which used to give the false impression that AutoPrompt had not even looked).

### Legal-entity scaffolding gate

If the source contains no legal-entity markers (BV, NV, GmbH, Ltd., Meester, notaris, etc.), the generated prompt omits the BV/NV/Meester legal-entity-handling and statutory-reference sections. They are noise for a mechanical patent body where no entity names appear in running text, and they used to waste prompt-token budget that could have been spent on real document-specific anchors.

## Output format

Generated prompts are formatted as proper Markdown – `##` headings for each major section, `-` bullet lists, `**bold**` for emphasised terms, a Markdown table for the project-specific glossary, and `---` horizontal rules between major sections. Open one in Obsidian, VS Code, GitHub, or any Markdown-aware viewer and it renders cleanly with a navigable outline.

The Markdown markup is structural – it does not change what the translator AI does at translation time. The generated prompt's inner OUTPUT FORMAT rule still says "translation only, no markdown formatting in the translation output", so per-segment AI translations remain plain target text.

## Translator's Comment methodology (always-on)

Since v1.10.46, every AutoPrompt-generated prompt embeds the **Translator's Comment** (TC) methodology by default, regardless of source language or domain. The methodology asks the translator AI to silently correct obvious mechanical defects in the source (typos, broken words, hanging mid-sentence breaks, doubled spaces, stray punctuation, reference-numeral mismatches that are unambiguous in context, missing diacritics, etc.) and append a single concise comment at the end of the segment in this exact format:

```
⟦TC: short factual description of the fix(es)⟧
```

- The brackets are the mathematical white square brackets **U+27E6** (⟦) and **U+27E7** (⟧). These characters do not occur in source documents, so they are safe as out-of-band markers that can be extracted reliably in post-processing.
- One marker per segment maximum; multiple fixes are joined with semicolons inside one marker.
- Segments with no defects emit no marker.
- When the translator AI inserts a word or short phrase to fill a clear gap, that supplied text is wrapped in standard ASCII square brackets `[like this]` inside the running translation, and the trailing marker references it (e.g. `⟦TC: [bracketed text] supplied to close hanging sentence⟧`).
- Numerical values, dates, dosages, legal scope language, headings, identifiers, and proper names are never silently "corrected" – defects in those zones are preserved verbatim, with an optional `⟦TC: source ambiguous – ...⟧` marker if doubt exists.

The defect categories that count as "obvious" are adapted to the actual source language by the LLM (Dutch -d/-t verb typos, German missing umlauts, French accent slips, Spanish/Italian conjugation typos, etc.).

:::note
**The markers appear inline in the target text** – they are not yet auto-extracted into Workbench segment comments. Extraction into a dedicated comments pane is a separate follow-up. For now, you can copy or strip the markers manually, or run a downstream script that finds `⟦TC: ...⟧` regions and moves them into a structured comment field.
:::

:::caution
**Want a generated prompt without the TC methodology?** Edit the generated prompt after creation and remove the TRANSLATOR COMMENT FORMAT section plus any TRANSLATION MANDATE language about silent correction. A per-project opt-out via a UI toggle may be added in a future version – open an issue if you'd like to see it.
:::

## Reviewing and refining the result

The generated prompt appears in the prompt library tree and is loaded into the **Prompt Editor** automatically. You can:

- **Read through the prompt** to verify it matches your project's actual needs.
- **Edit any section** directly in the editor – the generated prompt is just a regular `.md` file in your prompt library.
- **Use AutoPrompt as a starting point** – the goal is to give you a high-quality first draft, not the final word. Adjust glossary entries, add client-specific quirks, tighten the register guidance.
- **Re-run AutoPrompt later** if the project grows (more confirmed segments, more termbase entries) – each run is independent, so a later run produces a fresh prompt that reflects the project's current state.

## Tips and limitations

- **AutoPrompt cost scales with document size.** For very large projects (hundreds of thousands of words) the per-run cost can become significant. Consider running AutoPrompt against a representative subset rather than the full project for very large jobs.
- **Termbase quality matters.** If you have an attached termbase that contains generic technical words ("system", "board", "installation") that match almost any document, AutoPrompt will include those entries in the locked glossary and force the AI to follow them. Disable irrelevant termbases before running AutoPrompt.
- **AutoPrompt does not guess.** If a pre-generation pass finds nothing in the source (no collisions for this domain / language combination, no defects, no cascades), the corresponding section is omitted from the generated prompt rather than padded with hypothetical examples. Hypothetical examples are worse than nothing.
- **AutoPrompt and Supervertaler for Trados share the same prompt library folder.** A prompt generated in Workbench is immediately visible in the Trados plugin and vice versa.

## See also

- [Prompt Manager](prompt-library.md) – manage and organise generated prompts
- [Creating Prompts](prompts.md) – write prompts from scratch
- [AI Translation Overview](overview.md) – how the Custom Prompt is used during translation

---
title: "Image Context"
---

The **Image Context** viewer lets Supervertaler attach figure images to AI translation requests so the model can see the document's drawings, photos, schematics or labelled parts in addition to the text. When a segment contains `Figure 1`, `Fig. 2A`, `Table 3`, etc., the matching image is shipped with the request so the AI's translation is anchored in what the figure actually depicts — not just the words around it.

The same viewer doubles as Supervertaler's **DOCX image extractor**: point it at a Word document and it pulls every embedded image out into a numbered folder of PNG files, ready to load straight back as AI context. So the most common flow is one button-press: extract from a DOCX → context is auto-loaded → start translating.

## Where to find it

The viewer is folded into the **Prompt Manager** (since v1.10.176; it used to be a standalone AI sub-tab):

1. Switch to the **✨ AI** tab → **Prompt Manager** sub-tab.
2. On the left of the panel, find **Section 4 — Image Context**.
3. Click the green **`Open ▸`** button. The right-hand panel swaps from the Prompt Editor to the Image Context viewer.
4. The viewer's **`← Back to Prompt Editor`** button (or clicking any prompt in Section 5) returns you to the Prompt Editor.

## Extract images from a DOCX

The viewer is a single toolbar at the top, with a results list + image preview below.

1. Add input files to the extraction queue:
	- **📄 Add DOCX** — pick one DOCX file
	- **📁 Add Folder** — add every DOCX file in a folder (batch input)
2. Choose an output strategy:
	- Enable **Auto-folder** to create an `Images` folder next to each DOCX
	- Or set a single output directory in the **Output directory** field
3. Set **Prefix** (default `Fig.`).
4. Click **🖼️ Extract Images**.
5. The freshly-extracted folder is automatically loaded as AI context for figure-aware translation — no second click required.
6. Use **📂 Extracted Files (click to preview)** below to preview images.

## Load a pre-existing folder of images

If you already have a folder of images ready (e.g. one you extracted in an earlier session, or one you assembled by hand):

1. Click **📁 Load Folder** (the green button, to the right of Extract Images).
2. Pick the folder.
3. The images load into the AI context **and** populate the preview list below — just like a fresh extraction.

:::note
**"Add Folder" vs "Load Folder"** — these are the two confusing buttons. **Add Folder** queues a folder of *Word documents* to extract images from. **Load Folder** loads a folder that already contains *image files* directly for AI context. The on-button tooltips spell out the distinction.
:::

## Filename → figure-reference matching

Supervertaler infers the figure reference from each image's filename. Recognised patterns:

| Filename example | Matched reference |
|---|---|
| `Figure 1.png` | `1` |
| `Fig. 2A.jpg` | `2a` |
| `figure3-b.png` | `3b` |
| `Fig 10.tif` | `10` |

When the AI later sees `Figure 1` or `Fig. 2A` in a segment's source text, the matching image (case-insensitive, whitespace-/dash-/dot-normalised) is attached to the request. References that don't match any loaded image are simply ignored — no error, no warning, the segment translates text-only.

## How loaded images reach the AI

When AI translation runs (single-segment or batch), Supervertaler scans each segment's source text for figure references. If a match is found AND a corresponding image file is loaded AND the active model supports vision (Claude Sonnet/Opus 4.x, GPT-4o or newer, Gemini), the image is base64-encoded (or passed as PIL data for Gemini) and attached to the request. Segments without figure references are translated text-only.

A line appears in the log for every match, e.g.

```
🖼️ Detected figure references in segment #42: 1, 2a
✅ Including 2 figure images: 1, 2a
```

If the model is text-only (older GPT, Ollama models without vision, etc.), the figures are silently skipped and a warning goes to the log so you know why visual grounding didn't fire.

## Using images with AutoPrompt (opt-in)

Since v1.10.178, the loaded figures can ALSO be sent to the **AutoPrompt** generator — not just to the per-segment translator. Section 2 of the Prompt Manager has a companion checkbox under the **✨ AutoPrompt** button labelled **"🖼️ Include loaded figure images"**.

Tick it before clicking AutoPrompt to ship the loaded figures alongside the meta-prompt. The LLM then uses the drawings to lock terminology decisions directly into the generated translation prompt — *"part 7 in Figure 1 is labelled 'cylindrical sleeve' → lock 'mantelbuis' → 'cylindrical sleeve' in the termbase"* — instead of having to guess from textual references alone.

- **Off by default** — opting in is a deliberate per-project choice.
- **Adds a small extra cost** — roughly $0.05–$0.30 for 10–20 figures with a Sonnet-class model, more with Opus. Negligible vs. the value of a typical project (a €1000 patent will spend less than 0.1% on visual grounding).
- **Cost-confirmation dialog** pops up before the request so you can back out.

See [AutoPrompt](autoprompt.md) for the full flow and pre-flight gates (vision-model check, missing-figures friendly message, etc.).

## Project persistence

The currently-loaded folder path is saved into the `.svproj` file, so reopening a project automatically re-loads its image context. If the folder has moved or been deleted, you get a warning in the log and the project opens with no images loaded — re-pick the folder via **Load Folder** to restore.

## See also

- [Prompt Manager](prompt-library.md) — where Section 4 (Image Context) lives
- [AutoPrompt](autoprompt.md) — opt-in to ship figures with the meta-prompt
- [AI Translation Overview](overview.md) — how images flow into per-segment translations

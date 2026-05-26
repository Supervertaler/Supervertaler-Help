---
title: "Image Extractor (Superimage)"
---

The Image Extractor pulls embedded images out of DOCX files and saves them as numbered PNG files. It also includes a built-in preview so you can quickly review what was extracted.

## Where to find it

- **Tools → Image Extractor (Superimage)...**

## Where the Image Context viewer lives

Since v1.10.176, the Image Extractor / Image Context viewer is no longer a standalone AI sub-tab — it has been folded into the **Prompt Manager**. To open it:

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

If you already have an `Images` folder ready (e.g. one you extracted in an earlier session, or one you assembled by hand):

1. Click **📁 Load Folder** (the green button, to the right of Extract Images).
2. Pick the folder.
3. The images load into the AI context **and** populate the preview list below — just like a fresh extraction.

:::note
**"Add Folder" vs "Load Folder"** — these are the two confusing buttons. **Add Folder** queues a folder of *Word documents* to extract images from. **Load Folder** loads a folder that already contains *image files* directly for AI context. The on-button tooltips spell out the distinction.
:::

## How loaded images reach the AI

When AI translation runs (single-segment or batch), Supervertaler scans each segment's source text for figure references (`Figure 1`, `Fig. 2A`, `Table 3`, …). If a match is found AND a corresponding image file is loaded AND the active model supports vision (Claude Sonnet/Opus, GPT-4o and later, Gemini), the image is base64-encoded (or passed as PIL data for Gemini) and attached to the request. Segments without figure references are translated text-only.

:::note
**AutoPrompt CAN see your images — opt-in only.** Since v1.10.178, the AutoPrompt button in Section 2 of the Prompt Manager has a companion checkbox labelled **"🖼️ Include loaded figure images"**. Tick it before clicking AutoPrompt to ship the loaded figures alongside the meta-prompt — the LLM then uses the drawings to lock terminology decisions directly into the generated prompt. Off by default; opting in is a deliberate per-project choice that adds a small extra cost ($0.05–$0.30 with Sonnet-class for 10–20 figures). See [AutoPrompt](../ai-translation/autoprompt.md) for the full flow and pre-flight gates.
:::

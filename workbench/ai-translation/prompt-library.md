---
title: "Prompt Library"
---

:::note
You are viewing help for 🖥️ **Supervertaler Workbench** – the free, open-source standalone translation app. Looking for help with the Trados Studio plugin? Visit 🧩 [Supervertaler for Trados help](https://supervertaler.gitbook.io/help/trados/).
:::

Supervertaler includes a Prompt Manager so you can create, organise, and reuse prompts across projects. It lives in the **AI** tab → **Prompt Manager** sub-tab.

## Common uses

- Maintain different prompts per client
- Maintain different prompts per domain
- Switch between "draft" and "final" translation styles

## Prompt Library toolbar

Above the Prompt Library tree you'll find these actions:

| Button | What it does |
|---|---|
| **+ New** | Create a new empty prompt at the current folder. |
| **📁 New Folder** | Create a new folder for organising prompts. |
| **✨ AutoPrompt** | Analyse the current document (domain, tone, terminology) and auto-generate a tailored translation prompt. The new prompt appears in the library and is loaded into the Prompt Editor automatically; if it was created with the activate flag, it also becomes the **Custom Prompt ⭐** for the project. |
| **⚙️ System Prompts** | Open Settings → System Prompts to configure mode-specific system prompts. |
| **🔄 Refresh** | Reload the library from disk. |
| **▸ Collapse all** / **▾ Expand all** | Fold or unfold every folder in the tree. |

## Custom Prompt

The panel above the toolbar shows the **Custom Prompt ⭐** – the prompt that's currently active for AI translation in this project. Right-click any prompt in the library and choose **⭐ Set as Custom Prompt** to make it the active one. AutoPrompt sets the new prompt as Custom Prompt automatically.

## Tips

- Start simple and evolve prompts as you learn what works for your language pair.
- AutoPrompt is a good starting point for new projects, especially in unfamiliar domains – use the auto-generated prompt as a draft and edit it from there.

## External prompts

If you load a prompt from an external file (outside the built-in library), Supervertaler can show it in the editor and save changes back to the same file.

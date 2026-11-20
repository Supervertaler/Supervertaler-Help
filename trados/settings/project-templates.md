---
title: "Project templates"
description: "Keep Supervertaler's project settings in Trados Studio project templates, see what a template holds, apply one to a project you already have, and edit Studio's customer list."
---

A Trados Studio **project template** (a `.sdltpl` file) holds the settings Studio gives a new project: its translation memories, termbases, customer, file types and so on. Supervertaler keeps its own **project settings** in the same template, so one template sets up both Studio and Supervertaler for a new project.

You can make one template per client, per client and end client, or per kind of job.

:::note
From v18/19.20.209.
:::

## What a template holds

| Part | Kept by | Carried into new projects |
| --- | --- | --- |
| Translation memories, MT, termbases, customer, file types, QA and other Studio settings | Trados Studio | Yes, as always |
| Memory bank (by name) | Supervertaler | Yes |
| Translate prompt and proofread prompt (by their place in your prompt library) | Supervertaler | Yes |
| Client name | Supervertaler | Yes |
| Supervertaler termbases: which are read, written to, the Project termbase, and which are sent to the AI | Supervertaler | Yes |
| MultiTerm termbases: which are switched off in Supervertaler, and which are sent to the AI | Supervertaler | Yes |
| Model choices, the reference drawings folder, the termbase database file | Supervertaler | No: the model lists are global, and the others are paths on one computer |

A template holds names, not contents: the name of a memory bank, not its articles; the name of a prompt, not its text.

## Making a template

1. Open a project that is set up the way you want: Studio's TMs and termbases, and Supervertaler's memory bank, prompts, client and termbase ticks.
2. Open Supervertaler's **Settings** and click **OK**. This writes Supervertaler's project settings into the Studio project. (Changing a setting in the project does the same; this step only matters for a project you set up before v20.209.)
3. In Studio's **Projects** view, select the project and choose **Create Project Template**.

Every new project made from that template starts with the same settings, Studio's and Supervertaler's. You don't need to do anything in Supervertaler.

A project takes a copy. Changing the template later does not change projects made from it earlier, and changing a project does not change the template. Studio's own settings work the same way.

## The Project templates window

In Supervertaler's **Settings**, on the **General** tab, under **Project templates**, click **Project templates...**. The window lists every template Studio offers under **New Project**, plus any in Studio's Project Templates folders, with the Studio version and the folder of each. Type in **Filter** to shorten the list.

Pick a template, then choose what the table below shows:

- **What it holds**
- **What applying it to the open project would change**

Drag the bar between the list and the table to give either more room. The template's file is named under the table; click it to open its folder with the file selected. Press **F1** or click **? Help** for this page.

The window works on the project open in Studio: the one in the Editor, or else the one selected in the **Projects** view. With no project open, it only shows what each template holds.

## Seeing what a template holds

**What it holds** lists everything in the template, without a project to compare it with:

- **Supervertaler**: the memory bank, the prompts, the client, and each Supervertaler termbase with its ticks (read, write, project termbase, AI). Termbases the template does not name are off in a project made from it.
- **Translation memories**: each TM and MT provider, with its switches (lookup, concordance, update, penalty). A TM marked *[en-GB → nl-NL only]* is in that language pair's own list: for that pair, a project uses that list instead of the one for all language pairs.
- **Termbases**: Studio's termbases. A server termbase is marked as one.
- **Term recognition**: the termbase index for each language, minimum match value, search depth, search order, and whether terms without a translation are shown.
- **Customer**: Studio's customer.

A TM or termbase whose file is not there is marked *File not there*, with its folder, so you can see when a template points at a file that has moved.

If the template has no Supervertaler project settings yet, the table says so. See [Making a template](#making-a-template).

## Applying a template to a project you already have

Studio only uses a template when it creates a project. Supervertaler can apply one to a project that already exists: one made before you had the template, made from another template, or made from scratch.

1. Open the project in Studio.
2. Open the **Project templates** window and pick the template.
3. Choose **What applying it to the open project would change**. The table lists every TM, termbase, customer and Supervertaler setting, and says for each one whether it is *Kept*, *Added*, *Set* or left alone. What applying changes is in bold.
4. Click **Apply to this project...**. A short question says what will change; click **Yes**. If nothing would change, Supervertaler says so and does not ask.

A short summary follows, and the table then shows the project as it is now.

### What applying does

- **Supervertaler's project settings** come from the template. A setting the template leaves empty stays as the project has it. The project also records the template's name.
- **Translation memories: keep, add.** Every TM list of the project (the one for all language pairs, and each language pair's own) keeps its TMs, in their order and with their switches. The template's TMs that a list does not have yet are added at the end, with the template's switches. A TM in both keeps the project's switches.
  - A language pair with a list of its own gets the template's TMs for that pair.
  - A language pair without a list of its own, where the template's pair has one, gets one: the project's TMs for all pairs plus the template pair's, so nothing it used stops applying.
  - Server TMs are added; Studio asks you to sign in when it needs to. If Studio refuses them, the rest is added and the summary says so.
  - An added TM is used straight away. You do not need to close and reopen the document.
  - A TM whose languages are the project's the other way round (an English → Dutch TM in a Dutch → English project) is marked *used in reverse*: Studio looks things up in it but adds nothing to it.
- **Termbases: keep, add.** The project keeps all its termbases, in their order, with its default termbase and recognition options. The template's termbases it does not have yet are added at the end. A termbase index from the template is added only for a language the project does not map yet. Server termbases are not added: add them in Studio's **Project Settings**.
- **The customer** becomes the template's. If Studio's customer list does not have it, you are asked whether to add it; say **No** and the project keeps its customer.

**Nothing is removed.** The project keeps all its TMs and termbases, and nothing is deleted from any TM or termbase. A TM or termbase file that is not there is left out, and the summary names it. Applying the same template twice adds nothing the second time.

**Not applied:** Studio's other template settings (file types, QA, task sequence, analysis bands, users). Those still come only when Studio creates a project from the template.

A template that cannot be read (moved, deleted, damaged, or on a drive that is offline) changes nothing; the window names the file and says why.

### Projects from a package or GroupShare

A project you received as a package, or from GroupShare, belongs to the agency, and its settings can travel back to them. Supervertaler therefore writes the template's Supervertaler project settings only into its own record on your computer, and leaves the project's Studio TMs, termbases and customer alone.

## Studio customers

Click **Studio customers...** (on the General tab, or in the Project templates window) to see Studio's customer list in alphabetical order.

- **Add** a customer, **Edit** one (name and email; double-clicking a customer does the same), or **Remove** one.
- Changes go straight into Studio's own list, the one **New Project** and **Project Settings** offer.
- Studio's list is kept alphabetical too: after each change made in Supervertaler, and each time Studio starts. A customer added in Studio itself stays at the end of Studio's list until then.
- A name already in the list is refused, also when it differs only in capitals: Studio matches a template's customer ignoring capitals, so two such names could not be told apart.
- **Renaming keeps the customer**: projects that use it still point at it. Studio may show the old name for those projects until their customer is set again.
- **Removing** a customer that projects use: the window says how many and asks first. Those projects keep it as their customer; Studio just stops offering it.

## Using a template on another computer

- **Termbases are found by name.** A template made on one computer finds Supervertaler termbases with the same name on another.
- A memory bank you do not have counts as no memory bank.
- A prompt you do not have is replaced by the default prompt in the list. The project keeps the name, so if you add that prompt later, it is used.
- A termbase you do not have is switched off for you and kept in the project, so its owner gets it back when the project returns.

## Sending a template to someone else

:::caution
A template carries the customer's name, and Supervertaler's client, memory bank and prompt names, and the names of the Supervertaler termbases switched on in it. Check before you send a template to anyone else. The template's file name often names the client too.
:::

## See also

- [General settings](/trados/settings/general/)
- [Per-Project Settings](/trados/settings/project-settings/)
- [SuperMemory](/trados/ai-assistant/super-memory/)
- [Studio translation memories](/trados/settings/general/#studio-translation-memories)

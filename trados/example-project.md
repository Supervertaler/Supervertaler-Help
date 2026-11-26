---
title: "Try the example project"
---

The example project is a small, ready-made Trados project for trying Supervertaler before you use it on real work. It takes a minute to create, and you can delete it or start it afresh whenever you like.

Keep this page open beside Studio while you work through it.

## Create the example project

1. Open Supervertaler's settings: press **Ctrl+Alt+Shift+S**, or click **Supervertaler Settings** on Studio's **Add-Ins** tab. Both work in every view, with or without a project open.
2. On the **AI Settings** tab, click **Open example project…**.
3. Choose the **source language** and the **target language**. One of them has to be English, because the example document is written in English. The lists show languages ("Dutch"); tick **Show language variants** if you want a particular variant, such as "Dutch (Belgium)" or "English (United Kingdom)".
4. Click **Create project**.

Supervertaler creates the project in Studio's own Projects folder and opens the document in the Editor. When it is done, a message lists a few things to try, with a button that opens this page.

## What is in it

* **The document:** an installation and operating guide for an invented water heater, the *Acme AquaLine AL-50*. About 70 segments, with headings, bulleted and numbered lists, two tables, bold and italic text, a link, and numbers with units.
* **A translation memory** with ten entries planted so that you meet every kind of match: three exact matches, one that differs only in its numbers, five fuzzy matches (about 70 to 95%) and one weak match below 70%. It is inside the project folder, in `TM\Supervertaler example.sdltm`.
* **A Supervertaler termbase** with fifteen terms, such as *appliance*, *mains*, *fixing screw* and *inlet filter*. It is named like the project and switched on in the example project only.
* **A memory bank** (SuperMemory) with a short client brief and a few style rules, also named like the project, for example `supervertaler-example-dutch-to-english`. It is switched on for the example project when it opens.

The translation memory and the termbase are there for 22 prepared languages: Chinese (Simplified), Czech, Danish, Dutch, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian (Bokmål), Polish, Portuguese (Brazil), Portuguese (Portugal), Romanian, Russian, Spanish, Swedish, Turkish and Ukrainian. For any other language you get the document and the memory bank; everything below works except FuzzyFixer and TermLens, which have nothing to show.

:::note
The AI features need an API key: add one in **Settings → AI Settings** first. No key? [Clipboard Mode](/trados/clipboard-mode/) lets you use any AI chat in your browser instead.
:::

:::tip
Can't see a panel mentioned below? Studio remembers where each panel goes, so it may be closed, hidden at the edge of the window, or somewhere other than in the pictures. Open it from Studio's **View** tab.
:::

## Things to try

The sentences below are the English ones. If you created the project *into* English, look for the same sentence in your language: the document is the same, in the same order.

### 1. See the translation memory at work

Every sentence with a match in the example translation memory has a Studio comment saying what kind of match it is, so you can find them as you go: look for the comment marker in the Editor, or open the **Comments** pane from Studio's **View** tab for the full list.

Go to the first bullet under **1 Safety instructions**: "Disconnect the appliance from the mains before opening the cover." Studio's **Translation Results** pane shows a 100% match from the example translation memory. So do "Before you open the cover, read the safety instructions." (section 7) and "Connect the hot water pipe to the red outlet." (section 4).

"The maximum water pressure is 0.6 MPa (6 bar)." (section 3) has a match that differs only in its numbers. Studio scores it 100% and fills in the new numbers itself.

### 2. Repair a fuzzy match with FuzzyFixer

Go to section **5 Operation**, to "Press **+** to raise the temperature in steps of 1 °C." The translation memory has "Press + to *change* the temperature…": close, but not the same. Press **Ctrl+Alt+F**. [FuzzyFixer](/trados/fuzzyfixer/) takes the old translation and changes only what the difference requires. Nothing is written until you press **Enter**; **Escape** throws the repair away.

The other fuzzy matches, to try it on more than one:

* "The *AL-50* is intended for domestic use only." (the introduction)
* "Turn the temperature dial clockwise to increase the water temperature." (section 5)
* "Tighten the two lower fixing screws with a 4 mm hex key." (section 4)
* "Do not install the appliance in a room where the temperature can fall below 0 °C." (section 1)

"If the display shows E3, the inlet filter is blocked." (section 6) has only a weak match, below 70%. FuzzyFixer leaves those alone: it would be rewriting, not repairing.

### 3. Look up terms with TermLens

In any segment, the [TermLens](/trados/termlens/) panel shows the example termbase's terms that occur in it, with their translations. Each term has a numbered badge: **Alt+1** inserts the first, **Alt+2** the second, and so on. Try it in "Disconnect the appliance from the mains before opening the cover.", which has two.

### 4. Translate with AI

* **Alt+T** translates the segment you are in, using the termbase and the memory bank.
* **Batch Translate**, in the Supervertaler Assistant's **Batch Operations** tab, translates the whole document. See [Batch Translate](/trados/batch-translate/).

### 5. Proofread

Put a translation in a segment, perhaps with a deliberate mistake, and press **Ctrl+Alt+P**. [Proofread active segment](/trados/ai-proofreader/) says whether it found an issue and shows its correction as changes to your text.

### 6. QuickLauncher

Press **Alt+Q** in the Editor. The [QuickLauncher](/trados/quicklauncher/) menu starts with Translate, FuzzyFixer and Proofread, followed by your own prompts: instructions to the AI about the segment you are in or the text you have selected, such as explaining a term or assessing a translation.

### 7. See what a memory bank does

Supervertaler sends the project's [memory bank](/trados/ai-assistant/super-memory/) with every AI request, so the AI follows it without being told each time. The example bank says, among other things, to keep "Acme" and "AquaLine AL-50" as they are, and to keep a space between a number and its unit.

Open the bank's folder (in the Supervertaler Assistant, **Open folder** next to the memory bank list), change or add a rule in `style.md`, and translate a segment again with **Alt+T**: the translation follows the new rule.

### 8. Explore the Supervertaler Assistant

The **Supervertaler Assistant** pane is where most of Supervertaler lives. If you can't see it, open it from Studio's **View** tab. Its tabs are worth a look one by one:

* **Batch Operations**
  * **Translate** and **Proofread** at the top switch the whole tab between translating the document and checking a translation. The prompt list follows the mode you are in.
  * **AutoPrompt…** asks the AI to write a translation prompt for this project, from the document, the termbase and the memory bank. When it is done, right-click the AI's message, choose **Save as Prompt…** and give it a name. The saved prompt goes straight into the **Prompt** list, selected: from then on Batch Translate uses it. See [AutoPrompt](/trados/generate-prompt/).
  * **Preview prompt** shows exactly what would be sent to the AI, prompt, termbase, memory bank and all, without sending anything.
  * **SuperBench…** has three AI models translate the same segments of this document, and a fourth judge them, so you can see which model suits the work. See [SuperBench](/trados/superbench/).
* **Chat:** talk to the AI about this project. Ask it to explain a sentence, suggest a better term, or check your translation of a segment. See [Chat](/trados/ai-assistant/chat/).
* **Import/Export:** export the document for a proofreader as a Word file, bilingual text or HTML, and bring their corrections back into Studio, with each change shown before it is applied. See [Import/Export](/trados/import-export/).
* **Reports:** the results of a batch proofread, and what your AI calls have cost. See [Reports](/trados/reports/).

Above the tabs is the **SuperMemory** bar: the memory bank in use (the example project's own, `supervertaler-example-…`), **Open folder** to edit its files, and **Report** to see what it contains. See [SuperMemory](/trados/ai-assistant/super-memory/).

## Starting again, and removing it

Click **Open example project…** again and choose the same languages. Supervertaler asks:

* **Open it:** opens the example project as it is, with your changes.
* **Start afresh:** deletes the example project, with its termbase and memory bank, and creates a new one. Close its document in the Editor first.

Choosing other languages creates a second example project next to the first.

When you are done, delete the example project in Studio's **Projects** view like any other project.

## Next: your own work

Everything you tried here works the same way in your own projects. Good next pages:

* [Getting Started](/trados/getting-started/): the settings to check before your first real job.
* [Memory banks](/trados/ai-assistant/super-memory/): create one for each client.
* [AI Cost Guide](/trados/ai-cost-guide/): what AI translation costs, and how to keep it low.

Questions or ideas? Ask on [Reddit (r/Supervertaler)](https://www.reddit.com/r/Supervertaler/), where other users can see the answer too.

---
title: "EverTM Matches"
---

**EverTM Matches** is a pane of its own in Studio's Editor that shows [EverTM](/trados/evertm/)'s matches for the segment you are in, with everything EverTM knows about each: where it came from, its client and project, who translated it and when, and its older translations. You can insert a match, correct it in EverTM, or remove a wrong one. If you switch it on, it shows your project's **Studio TMs'** matches too, so it can stand in for Studio's Translation Results.

*From v18/19.20.210.* It needs a Supervertaler licence (or the trial), like TermLens. EverTM itself, in your project's TM list, stays free.

:::caution[Do this once: free Alt+Shift+1–9]
**Alt+Shift+1** to **9** insert match 1 to 9 from the editor, but Studio uses the same keys for its own **1. Insert symbol** to **9. Insert symbol**, and Studio's own actions always win. Until you change that, the keys silently do nothing.

In **File > Options > Keyboard Shortcuts > Editor**, select **1. Insert symbol** to **9. Insert symbol** and remove their shortcuts (or give them other keys). Or give **EverTM: Insert match 1** to **9** keys of your own there. Do this in each Studio version you use.
:::

## Opening it

**View > EverTM Matches** in the Editor. It opens at the bottom of the Editor; drag it wherever you like and Studio remembers where.

### Translation Results keeps coming to the front

Studio brings its **Translation Results** pane to the front on every segment, and reopens it if you closed it. There is no setting for this in Studio. Two ways round it:

- **Let Supervertaler keep it back.** EverTM Matches > **Options > Keep Translation Results behind Supervertaler's panes**. Translation Results can then share a tab group with TermLens, EverTM Matches or TermPicker: when Studio brings it forward, Supervertaler puts its own pane back. Click the Translation Results tab yourself and it stays in front until you click a Supervertaler tab again. Translation Results still shows for a second or two on each segment: Studio is busy looking the segment up, and no plugin can act until it has finished.
- **Or park it behind Comments.** Studio doesn't bring Translation Results forward when that would hide the **Comments**, **Messages** or **TQA** pane. Drag Translation Results onto the Comments pane so the two become tabs of one group, leave the **Comments** tab selected, and give EverTM Matches a place of its own. Click the Translation Results tab whenever you want it.

## What each match shows

- **Its number and score.** EverTM's scores are green for 100%, orange from 85%, brown below. A [Studio TM](#matches-from-your-studio-tms-too)'s score is blue.
- **The stored source, with the differences from your segment**, as in Translation Results: a word the stored sentence has and yours doesn't is struck through in red; a word yours has is green and underlined where it goes; formatting tags are small grey marks. These are the differences the score is based on. A very long segment can't be compared word by word, and says so.
- **The stored translation**, with a number that differs from your segment already replaced (claim 8 becomes claim 9).
- **A faint line under it:** client · project · date (last changed, else created). A language variant other than your project's is added at the end ("· en-US" in an en-GB project). In a narrow pane, the client and project are shortened; the date is always shown whole.
- **"2 older ▸"** at the right: EverTM holds two older translations of the same sentence and shows only the newest. Click it to see them (see [Older translations](#older-translations)).

## The details under the list

For the match you select:

- **Found in**: a tag for each place that has this translation: green **EverTM**, and a blue tag for each Studio TM.
- **EverTM entry** (or **Studio TM entry**, for a match only a Studio TM has): every field with all its values (Project, Client, Subject, End client, Document, Note), who created and last changed it and when, when it went into EverTM, and its language variants. A Studio TM entry also gives the TM's file or server address.
- **Came from**: where EverTM got the entry, in words. "Confirmed in Studio project BRANTS (HELLO-003)" means EverTM learned it when you confirmed the segment in that project; "imported from Studio TM Acme.sdltm" and "imported from TMX file Acme.tmx" are imports; a Workbench TM's name is shown as it is. This is history. **Found in** is where the translation is now.
- Whether a number was replaced, and whether the formatting couldn't be placed.

Drag the line between the list and the details to give either more room.

## Inserting a match

- **Double-click** it, or select it with **Up/Down** and press **Enter**, or press **1** to **9** while the pane has the keyboard.
- **From the editor: Alt+Shift+1** to **9** (after [freeing those keys](#opening-it) once).
- The cursor stays in the target, so you can keep typing. **Inserting never confirms the segment**; confirm it as usual (Ctrl+Enter), which is also when EverTM learns it.
- Formatting tags land where Translation Results would put them. When they can't be placed with confidence, the text goes in without them and the status line says so.
- It replaces the target, like applying a match in Translation Results: Ctrl+Z undoes it, a locked segment is left alone, and a target with unaccepted tracked changes is not overwritten.
- The segment is labelled as a TM match, "TM, 87%, EverTM" (or the Studio TM's name), and the editor shows the match % as for any TM match.

## Options

**Options ▾** at the top right of the pane:

- **Source and target side by side** (as in Translation Results) or **Source above target**.
- **Lowest match shown**: 50% to 100% (70% to start with).
- **Most matches shown**: 1 to 20 (10 to start with). EverTM's and the Studio TMs' matches count together.
- **Details shown**: a tick for each item of the details area. Untick what you don't need; **Show all** brings them back.
- **Also show matches from the project's Studio TMs** (off to start with): see below.
- **Keep Translation Results behind Supervertaler's panes** (off to start with): see [above](#translation-results-keeps-coming-to-the-front).
- **Best match first** or **Newest first**.

They are remembered between Studio sessions, except the order, which starts on best match first.

## Older translations

EverTM gives you the newest translation of each sentence, so that's all the pane shows at first. To see the others, click **"2 older ▸"** on the match (or right-click it > **Show older translations**). They are listed under its details, best first: your project's own language variant first, then the newest.

- Click one to see its details; **double-click** it (or press **Enter**) to insert it instead of the match, the same way.
- A sentence with many translations shows 50 at a time, with **Show 50 more**.
- Not wanted at all? **Options > Details shown**, untick **Older translations**.

## Removing a wrong translation

A typo you once confirmed, or a bad translation from an agency TM: right-click the match (or an older translation) > **Remove from EverTM**, or select it and press **Delete**. The status line says what was removed and offers **Undo**.

- Every copy of that sentence with that translation goes, whatever its formatting or language variant, in both directions.
- The next translation takes its place, usually within a second.
- **Only EverTM changes.** Your Studio TMs, TMX files and the document are never touched.
- It stays removed: importing a TMX file or Studio TM that has it skips it, and so does Studio's **Update Main Translation Memories**. Confirming it yourself in the editor brings it back.
- To bring one back later: EverTM's window (Project Settings > Translation Memory > EverTM > **Settings**) > **Removed translations...** > select it > **Restore**. It comes back exactly as it was.

## Editing a translation

Right-click a match (or an older translation) > **Edit in EverTM...**, or select it and press **F2**. As in Studio's Edit Translation Unit, a window shows the source and the target to edit, and its fields.

- Tags show as grey markers (‹1›Save‹/1›). Type around them; they can't be typed over. If one goes missing, **Save** says so and saves nothing.
- Fields: Project, Client, End client, Subject, Document and Note. Separate several values with ";".
- **Save** changes EverTM only, never your Studio TMs, files or the target. The status line offers **Undo**.
- Every copy of that translation becomes one translation unit with your text. It keeps its original creation date and is "changed now, by you", so it becomes the newest translation of the sentence. The old text is marked removed, so an import won't bring it back; it is listed in **Removed translations** as "(edited)".

## Matches from your Studio TMs too

**Options > Also show matches from the project's Studio TMs** adds your project's own Studio TMs' matches to EverTM's, for translators who would rather work from this pane than from Translation Results.

- **Which TMs**: those Studio itself looks up in for the document: the project's TM list for its language pair, **Enabled** with **Lookup** ticked. File TMs and GroupShare TMs.
- **Telling them apart:** a Studio TM's match has a **blue stripe** down its left edge, a **blue score**, and its TM's name in a **pale blue tag** under the text. TMs are named with their file extension ("Acme Hydraulics.sdltm"), so they read as Trados memories; a GroupShare TM is marked "(GroupShare)".
- **The same translation in EverTM and a Studio TM shows once, as EverTM's**, with "also in Acme Hydraulics.sdltm" on its faint line ("also in 2 Studio TMs" when several) and every place under **Found in**. On equal scores, EverTM's match comes first.
- **Scores are Studio's own**, with the project's penalty for each TM, as in Translation Results. One difference: a Studio "100%" whose source isn't exactly your segment (Studio does that when only numbers differ) is shown as 99%.
- When a Studio TM has a 100% match, it offers that one alone, as in Translation Results.
- On a segment with no words ("2.", "4.4", "(iii)"), a Studio TM's match is shown only when it is exactly your segment's text: Studio scores any other number 99–100%, which is no help there.
- EverTM's matches appear at once; the Studio TMs' follow a moment later ("searching Studio TMs…" in the status line). Then the status line says how many TMs were searched, what they found, and how long it took.
- **Edit in EverTM**, **Remove from EverTM** and older translations are EverTM's alone. On a Studio TM's match, the right-click menu says to edit or delete it in Studio's Translation Results.
- A TM that can't be opened, or takes more than 5 seconds, is left out of that segment and named in the status line. One that fails or is slow twice is skipped until you open another document.
- Change a TM's **Enabled**, **Lookup** or penalty in Project Settings and the pane follows from the next segment, once Studio has saved the project. You don't have to reopen the document.

## EverTM switched off in a project

The pane follows EverTM's own row in the project's TM list, as Studio does. With its **Enabled** or **Lookup** unticked, the pane shows no EverTM matches, and the status line says "No EverTM matches: EverTM is off in this project's TMs". Your Studio TMs' matches still show if you have switched them on. A document that isn't part of a project always shows EverTM's matches.

## The status line

At the top of the pane:

- Normally: how many translation units EverTM holds, how many matches, and how long the lookup took; with Studio TMs on, also what they found.
- When there's something to know: "EverTM is empty…", "EverTM is being rebuilt…" (matches still come from the index before the rebuild), "The EverTM index could not be opened… Rebuild it.", or "EverTM lookup failed: …".
- "EverTM is not in this project's TMs with Update ticked: segments you confirm won't be learned": EverTM learns your confirmed segments only when it is in the project's TM list with **Update** ticked.
- After an action: "Match 87% inserted", "… inserted without formatting", "Removed from EverTM only…", with **Undo** where it applies.

## While you work

- The lookup runs in the background, so moving from segment to segment is never slowed down. When the pane is hidden, nothing is looked up.
- When you move on, the matches shown turn grey until the new segment's arrive, and grey matches can't be inserted, so a match never lands in the wrong segment.
- A segment you've just confirmed takes EverTM a second or two to take in, so the pane looks the segment you are on up once more after 4 seconds. The sentence you confirmed a moment ago then shows up as a fuzzy match for the next one, which is common in patents. If nothing new turns up, nothing on screen changes.

## What stays with Studio

Analyze, Pre-translate, learning on confirm, Studio's Concordance window and auto-applying the best match all still go through EverTM in your project's TM list. Keep EverTM there, with **Lookup** and **Update** ticked. The pane itself never learns anything.

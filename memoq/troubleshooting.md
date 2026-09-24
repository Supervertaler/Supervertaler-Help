---
title: "Troubleshooting"
---

### Supervertaler does not appear at all

Installing is not enough on its own: memoQ uses a new add-in only once it is switched on – see [Switching it on in memoQ](/memoq/installation/#switching-it-on-in-memoq). Check too that you answered **Yes** to the unsigned-plugin prompt on startup – its default button is *No*.

If memoQ was recently upgraded to a new major version, it installed into a new program folder without the add-ins. Run the Supervertaler installer again; it installs into the newest memoQ it finds. See [Installation](/memoq/installation/#after-a-memoq-upgrade).

### A row was left empty with "Supervertaler left this segment for you"

The model's reply for that row contained something other than the translation – a note, an explanation, markdown – and did again when asked a second time, so it was not written into your document. The message under the row quotes what the model sent; if the translation part is sound, copy it in and delete the rest. See [What the model may send back](/memoq/prompt-editor/#what-the-model-may-send-back).

If it happens often with one prompt, the prompt is probably asking for explanations. Look for lines like "add a brief explanation" and replace them with an instruction to use a `[[TC: …]]` marker.

### "AI translation is paused"

The free trial has ended, or a licensed computer has not been online for 30 days. Terminology, termbases, prompts and memory banks keep working meanwhile. Open **Supervertaler for memoQ** from the Start menu and choose **Help → Licence**: enter a key, or click **Check now** once you are online. See [Licensing](/memoq/licensing/#when-a-licence-lapses).

### It translates, but never learns

**Self-learning MT** is not set. Resource console → MT settings → your resource → **Settings** tab → **Self-learning MT** → *Supervertaler*, then restart memoQ.

Advertising the capability only makes the engine eligible; memoQ does not send confirmations until it is actually selected there.

### Terminology is not showing

Three things must all be true, under **Options → Terminology plugins**:

1. **Perform terminology plugin lookups while working in the translation grid** is ticked
2. **Supervertaler terms** does not read *Not configured* – i.e. at least one termbase is ticked Read for the project in the [Termbases window](/memoq/terminology/#the-termbases-window)
3. **Enable plugin** is ticked for it

### A termbase gives no hits

Check its languages in the Termbases window. A termbase stored the other way round from the project is turned automatically, but one in an unrelated pair – German → English on a Dutch job – is read as stored and simply matches nothing. Then check the Read tick is set for *this* project: the window names the project it applies to at the top, and in a new project the ticks are filed against it only after memoQ has sent a first segment.

### An imported file produced no terms

Almost always the delimiter: a file whose header row uses tabs but whose rows use spaces, or the reverse. Open it with whitespace visible. The import dialog reports how many rows it read; if that is zero the file is being read as one column.

### The panel names the wrong project, or nothing reaches the model

Supervertaler learns which project is open from two channels: a translation request from memoQ, and the [live document link](/memoq/mcp-server/#the-live-document-link), which reports every document memoQ shows. With the link connected, the panel follows within a couple of seconds of your clicking into a segment of the new project. Without it, the plugin has only translation requests – an add-in cannot ask – so until the first request of a session the panel still names the last project memoQ *did* ask about, and a memory bank chosen at that moment is recorded against that earlier project.

**Click the project name** in the panel (or **memoQ → Sync with memoQ now**) to take the project from the document memoQ is showing this instant. If it cannot, it says why: the live link is not connected, memoQ has not reported a document yet, or no project folder holds that document. Where Supervertaler looks is memoQ's own answer – the custom folder set under **Options → Locations → Projects**, the default `C:\Users\<you>\Documents\My memoQ projects` when none is set, and memoQ's register of every project, which names each one's actual folder – so moving your projects folder needs no setting here, and projects left behind in the old location are still found.

If clicking into a segment does not update the panel, memoQ is not calling the engine at all. Open **Project home → Settings → MT settings** and look for the line **“MT plugins are currently disabled.”** A project checked out from a memoQ server can have MT plugins switched off by the project manager, and there is no client-side setting that overrides it. The terminology provider still works in such a project, because it is not an MT plugin; translation through Supervertaler does not, in any mode, and neither does staging from Claude Desktop, which enters the grid through the same engine. Ask the project manager to allow MT plugins, or take the document out through a bilingual export.

If you chose a memory bank while the panel was stale, open the bank chooser again once the right project is shown – that records the choice against the right project – and check the previous project’s row in `C:\Users\<you>\AppData\Local\Supervertaler.memoQ\memory-bank-projects.txt`, one project GUID per line, in case it now names a bank it should not.

### The log

The **Activity** window in the prompt editor (**memoQ → Activity**, or Ctrl+L) shows the same log live. On disk it is:

```
C:\Users\<you>\AppData\Local\Supervertaler.memoQ\plugin.log
```

with a fallback at `C:\Users\<you>\AppData\Local\Temp\Supervertaler-memoQ.log` if that folder cannot be written.


It records what memoQ asked for and what was sent – segment sizes, how many terms matched, how many remembered segments were used, and any errors. It does not contain the text of your translations.

A typical healthy line:

```
translate: 199 src chars, 0 tag(s) -> 239 target chars, 0 tag(s) | recall: used 2 of 7 held | terms: 7
```

meaning: a 199-character segment; two remembered segments and seven terms sent with it; a 239-character translation returned.

---
title: "Troubleshooting"
---

Solutions to common issues with the Supervertaler for Trados plugin.

---

## Plugin not loading

**Symptoms:** The TermLens panel does not appear in Trados Studio, or the plugin ribbon tab is missing.

**Solutions:**

1. **Check Trados version** –the plugin requires **Trados Studio 2024** or later
2. **Verify .NET Framework** –ensure **.NET Framework 4.8** is installed on your system
3. **Reinstall the plugin** –remove the plugin via **Trados Plugin Management**, restart Trados, then install it again
4. **Check for errors** –open **Trados Plugin Management** and look for error messages next to the Supervertaler plugin entry

:::note
After installing or updating the plugin, always restart Trados Studio completely (close all windows, not just the project).
:::

---

## The installer finishes, but the plugin never appears

**Symptoms:** You install from the App Store, the Trados Plugin Installer runs through every step and reports success, and then Supervertaler is not in the **View** menu and not in **Plugin Management**. Reinstalling does exactly the same thing. Often the plugin was working before and disappeared on its own.

This is the most common installation problem, and it has one cause far more often than any other.

### First: was Trados Studio really closed?

**The installer fails silently if Studio is running.** Not with an error – it completes normally and reports success, having changed nothing that matters.

Each install location holds the plugin twice: the package, and an **unpacked** folder that Studio loads from and holds open the whole time it is running. An installer that cannot replace the unpacked folder leaves the old one in place, and **Studio will not re-extract into an unpacked folder that already exists**. The result is a successful install that changes nothing – even with the cleanup checkbox ticked, because that cleanup cannot delete files that are in use either.

So:

1. Close Trados Studio – **every** window, not just your project.
2. Open Task Manager (`Ctrl+Shift+Esc`), look under **Details** for **`SDLTradosStudio.exe`**, and end it if it is still there. Studio can take a few seconds to exit, and can occasionally linger after its windows have closed.
3. Run the installer again, leaving **"Remove this plugin from all installation folders"** ticked.
4. Start Studio.

That is the whole fix in most cases.

### Second: is there more than one copy in the Packages folder?

Look in the folder for your Studio version (full paths further down):

```
...\Trados\Trados Studio\19\Plugins\Packages\
```

There should be **exactly one** file with Supervertaler in the name. If there are two, that is the problem, and it explains why reinstalling never helps.

Both files declare themselves as the same plugin, so Studio finds two copies of one plugin and loads neither. And because each install only ever replaces the file it is named after, a second install lands beside the first rather than on top of it – the fault repairs itself only if you delete **both** by hand and then install once.

This can happen if the plugin has reached your machine by more than one route: from the App Store, from a file sent to you directly, or from an earlier version whose file was named differently. Delete every Supervertaler file you find there, then install once from the App Store.

### Third: is your Studio version greyed out in the installer?

On the installer's first screen, the list of installed Studio versions greys out any version the plugin does not support:

> Studio versions that are not compatible with the plugin will be grayed out.

**Almost always this means you downloaded the other build.** Supervertaler for Trados ships as two separate downloads, and the App Store page asks which you want:

> Trados Studio - 2026 Release, 19.x
> Trados Studio 2024, 18.x

The 2024 build greys out Studio 2026, and the 2026 build greys out Studio 2024 – by design, since each is built against its own Studio. If the version you want is greyed out, go back to the [App Store page](https://appstore.rws.com/plugin/432), click **Download**, and pick the other entry from the dropdown.

If you are certain you downloaded the right build and your Studio version is *still* greyed out, email support@supervertaler.com with the version number from **Help → About**. That means your Studio is outside the range this build declares, which is a fault at our end, not yours.

### Fourth: is it installed but switched off?

Open **Help → Plugin Management** and look for Supervertaler in the list. If it is there but disabled, or shows an error beside it, that is a different problem from a failed install – the entry's error message is the thing to send us.

### Last resort: clean out every copy by hand

Only needed if the steps above do not work. Close Studio, then paste each of these paths into the address bar of a File Explorer window and delete anything with **Supervertaler** in the name – a `.sdlplugin` file in the `Packages` folders, a folder in the `Unpacked` ones.

Replace `<username>` with your own Windows user name. Use the block for your Studio version – `18` is Studio 2024, `19` is Studio 2026.

Each path is one of the three choices the Trados Plugin Installer offers under "Please select the folder where the plugin will be installed", so if you remember which you picked, start with that one – but check all three, because an earlier install may have used a different one.

**Trados Studio 2024**

```
C:\Users\<username>\AppData\Roaming\Trados\Trados Studio\18\Plugins\   <- "All your domain computers" (the default)
C:\Users\<username>\AppData\Local\Trados\Trados Studio\18\Plugins\     <- "This computer for me only"
C:\ProgramData\Trados\Trados Studio\18\Plugins\                        <- "This computer for all users"
```

**Trados Studio 2026**

```
C:\Users\<username>\AppData\Roaming\Trados\Trados Studio\19\Plugins\   <- "All your domain computers" (the default)
C:\Users\<username>\AppData\Local\Trados\Trados Studio\19\Plugins\     <- "This computer for me only"
C:\ProgramData\Trados\Trados Studio\19\Plugins\                        <- "This computer for all users"
```

Inside each one there are two folders that matter, and **both** need clearing:

- `Packages` holds the installed `.sdlplugin` file.
- `Unpacked` holds the files Studio actually loads, extracted from it. This is the one people miss, and it is the one that blocks a reinstall: Studio will not re-extract over an `Unpacked` folder that is already there.

:::note
**Two things that catch people out.** `AppData` is hidden by default, so you cannot browse to it – paste the whole path into the File Explorer address bar instead and press Enter.

You may also see these written as `%AppData%` and `%LocalAppData%`. Those are just Windows shortcuts for `C:\Users\<username>\AppData\Roaming` and `C:\Users\<username>\AppData\Local`, and you can paste them into the address bar in place of the first part of the path if you prefer – they save typing your user name.
:::

Several of these will not exist, or will contain nothing from Supervertaler. That is normal – move on to the next. Delete **every** copy you find, including any that look like the current version: a leftover that looks correct is exactly the kind that wins the race against the new install.

Then start Studio once and close it again, so it writes out a plugin list with nothing from Supervertaler in it, and install once more.

:::note
Your settings, termbases, prompts, memory banks and licence key live in your Supervertaler data folder, not in these plugin folders. Deleting the plugin from all of them and reinstalling does not touch any of your work – see [Data Folder](/trados/data-folder/).
:::

:::tip
Still stuck? Email support@supervertaler.com with your Studio version from **Help → About** and a screenshot of the installer's first screen taken *before* you click Next. Those two things separate every remaining explanation.
:::

---

## A keyboard shortcut does nothing

**Symptoms:** A Supervertaler shortcut – e.g. `Alt+T` (translate segment), `Ctrl+Alt+T` (add term), `Ctrl+Alt+N` (non-translatable), `Ctrl+Alt+G` (AutoTagger), `Alt+Up` (quick-add to project termbase) or `Alt+Q` (QuickLauncher) – has no effect in the editor.

**Solutions:**

1. **Clear the conflicting Trados default** – Trados Studio ships with its own actions bound to these key combinations, and the Trados binding wins. Go to **File → Options → Keyboard Shortcuts**, search for the conflicting Trados action, and delete its binding. The full table of what to delete is in [Keyboard Shortcuts](/trados/keyboard-shortcuts/#first-time-setup-free-up-trados-shortcuts)
2. **Repeat after a reinstall** – reinstalling or resetting Trados Studio restores its default bindings, so the shortcuts stop working again until you clear them once more

---

## "Could not load SQLite" or DLL errors

**Symptoms:** Error messages about missing DLLs or SQLite when opening settings or loading a termbase.

**Solutions:**

- **Restart Trados Studio** after the first install. The plugin pre-loads its own SQLite DLL to avoid conflicts with other plugins, but this requires a clean startup
- If the error persists, reinstall the plugin to restore any missing DLL files

---

## Database locked / "cannot open database"

**Symptoms:** Error when trying to load or write to the termbase database.

**Solutions:**

- **Close Supervertaler Workbench** if it has the same `.db` file open. Two applications writing to the same SQLite file simultaneously can cause lock conflicts
- The plugin uses **read-only mode** where possible to minimise conflicts, but write operations (adding terms) require exclusive access
- Verify the `.db` file is not on a drive that has gone offline (e.g., a disconnected network share)

:::caution
If you share the database via a cloud-sync folder, ensure the file is fully synced before opening it in the plugin. Partially synced files can appear locked or corrupt.
:::

---

## Terms not appearing

**Symptoms:** TermLens shows no matches even though you know the segment contains terms that exist in your termbase.

**Solutions:**

1. **Check the Read toggle** –open [TermLens Settings](/trados/settings/termlens/) and verify the termbase has **Read** enabled
2. **Verify the database path** –ensure the path points to the correct `.db` file
3. **Press F5** to force a full reload of your Supervertaler termbases from disk (note: F5 does not reload MultiTerm termbases)
4. **Reload the database** –click the **gear icon** in the TermLens panel to open settings, then close the dialogue. This forces a reload of the termbase data
5. **Check language pair** –the termbase source and target languages must match the current Trados project languages. Either direction works (the matcher handles inverted-direction termbases automatically), but the language pair itself must match.
6. **Check for reversed entries** –if a single specific term you know exists is silently not matching while other terms in the same segment do, the entry may be stored in the wrong direction in the database (e.g. Dutch text in the English column). This typically affects entries created or edited under v4.19.24 or earlier in projects whose direction was the inverse of the termbase's. Open the **Termbase Editor** (double-click the termbase in TermLens Settings), find the term, check whether the source and target columns contain text in the expected languages, and use **Reverse source/target** to fix it. See [Termbase Management](/trados/termbase-management/) for details.

---

## MultiTerm terms not appearing

**Symptoms:** Green chips from your MultiTerm termbases (`.sdltb` files) are not showing in TermLens, even though the termbases are attached to your Trados project.

**Solutions:**

1. **Check your Trados project** –verify that MultiTerm termbases are attached via **Project Settings > Language Pairs > Termbases**
2. **Check the Read toggle** –open Supervertaler Settings (gear icon) and make sure the MultiTerm termbase's Read checkbox is enabled
3. **Check languages** –the termbase's source and target languages must match the current project's language pair
4. **Navigate to another segment and back** to trigger a MultiTerm auto-refresh (F5 does not reload MultiTerm termbases – only segment navigation does)

:::note
When you add terms in MultiTerm, navigate to a different segment in Trados to trigger the auto-refresh. TermLens checks for file changes on each segment change.
:::

See [MultiTerm Support](/trados/multiterm-support/) for full details.

---

## AI features not working

**Symptoms:** Batch Translate produces no output, or single-segment translation returns an error.

**Solutions:**

1. **Verify the API key** –open [AI Settings](/trados/settings/ai-settings/) and confirm the key is entered correctly with no extra spaces
2. **Check provider endpoint** –ensure the provider's API endpoint is reachable from your network (no firewall or proxy blocking it)
3. **Ollama users** –make sure the Ollama service is running locally:
   ```bash
   ollama serve
   ```
   Then verify the endpoint in AI Settings (default: `http://localhost:11434`)
4. **Custom provider** –double-check the endpoint URL and model name in the Custom OpenAI-compatible settings
5. **Check your API credits** –some providers return errors when your account balance is zero

---

## Database errors on Mac (Parallels)

**Symptoms:** Database locked errors, "cannot open database", or corrupt termbase data when running Trados Studio inside Parallels Desktop on a Mac.

**Cause:** Your Supervertaler data folder is on a Mac-side shared path (e.g., `\\Mac\Home\Supervertaler`). Parallels mounts Mac folders as virtual network shares, and SQLite databases do not work reliably on network filesystems – WAL mode (used by Supervertaler termbases) requires a local filesystem for correct locking.

**Solution:**

1. Move your data folder to the Windows side (e.g., `C:\Users\<username>\Supervertaler`)
2. Copy your `.db` termbase files from the Mac-side location into the new Windows-side folder
3. Update the data folder path in Supervertaler settings, or delete `%AppData%\Supervertaler\config.json` and restart Trados to trigger the first-run setup again

:::note
See [Installation – Running on a Mac (Parallels)](/trados/installation/#running-on-a-mac-parallels) for the recommended setup.
:::

---

## Performance issues

**Symptoms:** The editor feels sluggish, or TermLens takes a long time to display matches.

**Solutions:**

- **Large termbases** (50,000+ terms) may take a moment to index when the database is first loaded on startup. This is a one-time cost per session
- **Close and reopen the editor** if the plugin feels unresponsive after a long session
- **Disable unused termbases** –uncheck **Read** for termbases you do not need for the current project to reduce the matching workload
- **Reduce batch size** in [AI Settings](/trados/settings/ai-settings/) if Batch Translate is slow or timing out

---

## Still having issues?

1. Ask a question in [GitHub Discussions](https://github.com/orgs/Supervertaler/discussions) – the community hub for both Supervertaler Workbench and Supervertaler for Trados
2. Check the [GitHub Issues](https://github.com/Supervertaler/Supervertaler-for-Trados/issues) for known bugs, feature requests, and workarounds
3. Open a new issue to report a bug or request a feature, including:
   - Your Trados Studio version
   - The Supervertaler plugin version
   - Steps to reproduce the problem
   - Any error messages or screenshots

See [Support & Community](/trados/support/) for all the ways to get help.

---

## See Also

- [Support & Community](/trados/support/)
- [MultiTerm Support](/trados/multiterm-support/)
- [TermLens Settings](/trados/settings/termlens/)
- [AI Settings](/trados/settings/ai-settings/)
- [Termbase Management](/trados/termbase-management/)
- [Data Folder](/trados/data-folder/)

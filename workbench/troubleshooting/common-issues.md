---
title: "Common Issues"
---

Solutions to frequently encountered problems.

## Startup Issues

### Application won't start

**Symptoms:** Double-click does nothing, or window briefly appears then closes.

**Solutions:**

1. **Run from command line** to see error messages:
   ```bash
   python Supervertaler.py
   ```

2. **Reset UI preferences** (corrupted window state):
   - Delete `user_data/ui_preferences.json`
   - Restart the application

3. **Check dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Python version** (needs 3.10+):
   ```bash
   python --version
   ```

### "Module not found" error

Install the missing module:
```bash
pip install <module-name>
```

Or reinstall all dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

---

## Import Problems

### "Cannot read file" error

- Close the file in other programs (Word, Excel, etc.)
- Check if the file is read-only
- Try copying the file to a different location

### memoQ bilingual shows no segments

- Ensure you exported as **Bilingual DOCX** (table format)
- Check the file in Word to verify it has a source/target table

### Trados package fails to extract

- The SDLPPX might be corrupted
- Re-export from Trados Studio
- Check if the package includes all required files

### Encoding errors (garbled text)

- Open the source file in Notepad++ to check the detected encoding; if it shows ANSI/Windows-1252 with mojibake, use *Encoding → Convert to UTF-8* and re-save.
- For more stubborn cases, run [`ftfy`](https://pypi.org/project/ftfy/) on the file from the command line.
- Re-export from the source tool with UTF-8 encoding when possible.

---

## Translation Issues

### AI translation returns empty

1. Check your API key is valid
2. Verify you have credits with the provider
3. Check internet connection
4. Try a different model

### "Rate limit exceeded" error

- Wait 1-2 minutes and try again
- Reduce batch size
- Upgrade your API plan

### Wrong translation language

- Check your prompt specifies the correct language pair
- Verify source/target languages are set correctly in project settings

### Tags are removed or moved

Add explicit instructions to your prompt:
```
Keep all formatting tags like {1}, <b>, </b> in exactly 
the same positions in the translation.
```

---

## Reimporting Issues

### Segments don't match on reimport

**Cause:** Segment structure changed.

**Solution:**

- Don’t merge or split segments in Supervertaler.
- Export the matching format for your CAT tool/workflow.
- If you’re working from a bilingual table, don’t modify the table structure in Word.

### Formatting lost on reimport

**Cause:** Tags/placeholders weren’t preserved.

**Solution:**

- Verify tags in Tag view before exporting.
- Ensure tags are balanced and not renumbered.
- Run CAT tool QA after import to catch tag issues early.

---

## Translation Memory Issues

### TM matches not appearing

**Cause:** usually the TM isn't switched on for the project, or the project's language pair doesn't match the TM's. Less often, a damaged full-text index (only 100% matches appear, never fuzzy ones).

**Solution:**

- Open the **💾 TMs** tab and make sure **Read** is ticked for the TM. A new project starts with every TM switched off.
- Check that the project's language pair (**Project → 📋 Project Info…**) matches the TM's **Languages** column.
- Look in the log (**Settings → 📋 Log**) for a line saying the TM search failed.

[TM Matches Not Appearing](/workbench/troubleshooting/tm-matches/) goes through each cause in detail and explains the diagnostic script that pinpoints it.

---

## Export Problems

### Exported DOCX has no translations

- Make sure you translated the segments (target column isn't empty)
- Check you're exporting the correct format
- Verify the segments are confirmed

### "Source file not found" on export

The original imported file was moved or deleted.
- Use **Project → Export → 🔗 Relocate Source Folder** to point to the new location
- Or re-import the source file

### Formatting lost after round-trip

- Keep all inline tags in your translations
- Don't modify the structure of bilingual tables
- Check CAT tool import settings

---

## Performance Issues

### Application is slow

1. **Pick a smaller Per page size** above the grid (the grid shows all segments by default; try 100 or 50)
2. **Disable spellcheck** if not needed (Settings → View)
3. **Close other heavy applications**

### Large files take forever to import

- Very large files (10,000+ segments) may take time
- Consider splitting into smaller files
- Use multi-file import for better organization

---

## Spellcheck Issues

### Spellcheck not working

1. Check spellcheck is enabled: **Settings → View Settings → Spellcheck**
2. Verify the correct language is selected
3. For Hunspell, ensure dictionaries are installed

### Wrong language being checked

Go to **Settings → View Settings → Spellcheck** and select the correct target language.

### Red underlines appear everywhere

The spellcheck language might not match your target language. Or you might need to add technical terms to your dictionary.

---

## UI Issues

### Dark mode colors look wrong

v1.10.372 fixed most of the white panels and light-on-light text in the Dark theme (the Clipboard Manager columns, SuperLookup's web resources list, the info boxes in several tabs, and more), so update first. If something still looks wrong:
- Switch themes back and forth
- Restart the application
- If a panel stays white or unreadable, report it on [GitHub](https://github.com/Supervertaler/Supervertaler-Workbench/issues) with a screenshot

### Window opens off-screen

Delete `user_data/ui_preferences.json` to reset window position.

### Fonts look different/wrong

Go to **Settings → View Settings** and select your preferred font family.

### Can't type ł, ć, @ or other AltGr characters while Supervertaler is running (Windows)

**Cause:** Windows passes the **AltGr** key on as Ctrl+Alt. In versions before v1.10.372, Supervertaler's system-wide hotkeys (such as Ctrl+Alt+L for SuperLookup or Ctrl+Alt+Q for QuickTrans) therefore also caught AltGr+L, AltGr+Q and so on, and swallowed the key – in every application, not just Supervertaler. On a Polish keyboard that meant no **ł**, **ć** or **ó**; on a German keyboard no **@** (AltGr+Q).

**Solution:** update to v1.10.372 or later. When AltGr plus a key types a character on your keyboard layout, you now get the character. The hotkeys still work with the left Ctrl and left Alt keys.

### Settings are forgotten or revert to their defaults

Update to v1.10.372 or later, which fixed several causes:

- The Settings pages now save each change a moment after you make it (there's no **💾 Save** button any more). Before, a change was lost if you left the page without clicking Save.
- Saving the General settings no longer resets settings kept on other pages, such as the AI batch size and all QuickTrans settings.
- Saving the AI Settings no longer deletes your custom OpenAI-compatible MT endpoints.
- A custom AutoHotkey path, and "Do not show this dialog again" in the AutoHotkey setup dialog, are now remembered.

---

## Still Having Issues?

1. Check the [GitHub Issues](https://github.com/Supervertaler/Supervertaler-Workbench/issues) for known bugs
2. Open a new issue with:
   - Your OS and Python version
   - Steps to reproduce the problem
   - Error messages (if any)
   - Screenshots (if helpful)

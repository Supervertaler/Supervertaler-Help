---
title: "Data Folder and Team Folder"
---

Supervertaler keeps everything that is yours – your licence, settings, API keys, termbases, memory banks and prompts – in one **data folder** on your computer. Every Supervertaler product on the computer uses the same data folder, so a prompt or memory bank you create in [Supervertaler Workbench](https://supervertaler.com/workbench) is there in Supervertaler for Trados too, and the other way round.

A **team folder** is optional. It lets a team share its memory banks and prompt library from a folder on a file server, while everything personal stays in each person's own data folder. See [Sharing memory banks and prompts with a team folder](#sharing-memory-banks-and-prompts-with-a-team-folder) below.

## Where your data folder is

**Settings → General → Data folder** shows where your data folder is. Click **Open** to open it in File Explorer, or **Move…** to [move it](#moving-your-data-folder). (From v18/19.20.199.)

By default the data folder is:

```
C:\Users\<YourName>\Supervertaler\
```

You can choose a different location when you first install Supervertaler. The location is recorded in a small file, `%APPDATA%\Supervertaler\config.json`, which every Supervertaler product reads so they all agree on where your data is. To move the folder later, see [Moving your data folder](#moving-your-data-folder).

## What is in it

```
Supervertaler/
│
├── licence/                     Your licence                       Shared
├── settings/                    Your AI provider API keys          Shared
├── prompt_library/              Prompts                            Shared *
├── memory-banks/                SuperMemory banks                  Shared *
│   ├── _shared/
│   └── <bank name>/
│
├── resources/                   Termbases and TMs                  Shared
│   ├── supervertaler.db
│   ├── termbases/
│   ├── tms/
│   ├── non_translatables/
│   └── segmentation_rules/
│
├── trados/                      Supervertaler for Trados only
│   ├── settings/                settings.json, chat_history.json
│   ├── projects/                per-project settings
│   ├── batch_backups/           TMX backups from Batch Translate
│   ├── bank-extracts/           what each document took from your banks
│   ├── usage/                   AI usage and cost records
│   ├── logs/                    the diagnostic log, when it is turned on
│   └── runtime/                 how the MCP server finds Trados Studio
│
├── memoq/                       Supervertaler for memoQ only
└── workbench/                   Supervertaler Workbench only
```

\* When a team folder is set, the prompt library and memory banks come from the team folder instead.

### Shared resources

The **prompt library**, **memory banks** and **resources** folders are shared between all Supervertaler products. Prompts you create or edit in one program are immediately available in the others. The SQLite database (`supervertaler.db`) holds your termbases and translation memories – Workbench has full read-write access, while the Trados plugin reads from it.

The **settings** folder holds your AI provider API keys. They are encrypted so that only your own Windows account can read them.

### Program-specific folders

Each program stores its own settings, projects, and runtime data in a dedicated subfolder (`trados/`, `memoq/` or `workbench/`). This keeps configuration separate so the programs never interfere with each other.

The `trados/batch_backups/` folder contains automatic TMX backup files created during Batch Translate runs. One file is written per run, named by timestamp and project name. These files are not deleted automatically – you can remove old ones manually once your project is safely delivered, or keep them as a translation archive for use in other CAT tools. See [Batch Translate – Backup TMX](/trados/batch-translate/#backup-tmx) for details.

The `trados/bank-extracts/` folder (from v18/19.20.198) holds one Markdown file per translated document whose memory bank was large enough to be narrowed: what was sent from your banks, what was left out and why. It is there for you to read – editing it changes nothing. The newest 200 are kept, and a file not rewritten for 90 days is removed. See [SuperMemory – AI Integration](/trados/ai-assistant/super-memory/ai-integration/#a-large-bank-sends-only-what-each-document-needs).

## Sharing memory banks and prompts with a team folder

*From v18/19.20.199.*

When several translators work together – in an agency, or as a team on a shared remote desktop server – it helps if they all work from the same memory banks and the same prompts. A **team folder** does this: everyone points Supervertaler at the same folder on your file server, and Supervertaler takes the memory banks (including `_shared`) and the prompt library from there.

| Comes from the team folder | Stays in each person's own data folder |
|---|---|
| Memory banks, including `_shared` | Licence |
| Prompt library | Settings and API keys |
| | Termbases and translation memories |
| | AI Assistant chat history, usage records and logs |

:::note
Share the team folder, not the data folder. Pointing everyone at one shared data folder does not work: the licence and settings in it belong to one person, the API keys are encrypted for one Windows account (so your colleagues would find none), and the termbase database is not made for several people writing to it over a network. The team folder shares only what is meant to be shared.
:::

### Setting it up

1. **One person sets it up first.** In **Settings → General → Team folder**, click **Browse…** and choose a folder everyone on the team can reach, for example `\\fileserver\Translation\Supervertaler`.
2. If the folder has no memory banks or prompts yet, Supervertaler offers to copy yours into it, so your colleagues start with them. Your own copies stay where they are, and nothing already in the team folder is ever overwritten.
3. Click **OK**, then restart Trados Studio.
4. **Everyone else** then chooses the same folder in their own **Settings → General → Team folder**, clicks **OK** and restarts Trados Studio.

A network path such as `\\fileserver\Translation\Supervertaler` works for everyone, whatever drive letters their computers use. A mapped drive letter (such as `T:\Supervertaler`) works too, as long as everyone has the same letter.

The team folder is read once, when Trados Studio starts, so a change takes effect the next time you start it. To stop using the team folder, click **Clear**, then **OK**, and restart Trados Studio.

### When the team folder cannot be reached

When Trados Studio starts, Supervertaler waits up to three seconds for the team folder. If it does not answer in time, or cannot be found, Supervertaler uses the memory banks and prompts in your own data folder for that session – and tells you so, in the AI Assistant and under **Team folder** in **Settings → General**. It never switches silently.

Anything you add to a memory bank or prompt in that session is saved in your own data folder, not in the team's. Restart Trados Studio once the team folder can be reached again.

### Working from the same files

Memory banks and prompts are ordinary files in the team folder, so a change one person saves is in the folder for everyone. If two people edit the same file at the same moment, the last one to save wins, as with any shared document.

Supervertaler Workbench does not use the team folder yet: it keeps using the memory banks and prompts in your own data folder.

## Moving your data folder

*From v18/19.20.199.*

1. **Close Supervertaler Workbench**, and memoQ if you use Supervertaler for memoQ. They would otherwise go on saving to the old folder.
2. In **Settings → General → Data folder**, click **Move…** and choose where your data folder should go: an empty folder, or a new one. If you choose a folder that already has files in it, Supervertaler offers to use a `Supervertaler` folder inside it instead. If you choose a folder that already holds a Supervertaler data folder – your old one, say, or one restored from a backup – Supervertaler offers to switch to it as it is, copying nothing.
3. Click **OK**. Supervertaler copies everything in your data folder to the new place, with a progress window you can cancel.
4. **Restart Trados Studio.** From then on, every Supervertaler product on the computer uses the new folder.

Move takes care of the details:

- **Your old folder is left exactly as it is.** Once you have checked that everything is in the new folder, you can delete the old one.
- **Settings that point into the data folder** – such as your termbase and your selected prompts – are updated in the copy.
- **The termbase database is copied safely**, even though Trados Studio has it open.
- **If the copy fails, or you cancel it**, the partial copy is removed and nothing changes.

Until you restart Trados Studio, Supervertaler keeps using the old folder, so anything you change in between is saved there, not in the new one. Restart straight away.

:::note
Choose a folder on your own computer. The termbase database does not work reliably over a network, so Supervertaler warns you if the folder you choose is on a network drive.
:::

### Moving it by hand

On a version before v18/19.20.199, the data folder is moved by hand:

1. **Close Trados Studio**, and any other Supervertaler program that is open: Supervertaler Workbench, and memoQ if you use Supervertaler for memoQ.
2. In File Explorer, **move the whole data folder** to its new place, for example `E:\Work\Supervertaler`.
3. **Tell Supervertaler where it is now.** Paste `%APPDATA%\Supervertaler` into the File Explorer address bar, and open `config.json` in Notepad. Change the path after `"user_data_path"` to the new location, **writing every backslash twice**, just as the existing line does:

   ```json
   {
     "user_data_path": "E:\\Work\\Supervertaler"
   }
   ```

   Your file may have other lines, such as `"team_folder"` – leave those as they are. Save the file.
4. **Start Trados Studio** and check that **Settings → General → Data folder** shows the new location.

:::note
If **Data folder** shows `C:\Users\<YourName>\Supervertaler` instead, Supervertaler could not read the new line and fell back to the default location. Nothing is lost: your licence, settings and termbases are still in the folder you moved. Close Trados Studio, check the line in `config.json` (every backslash written twice, the path in double quotes), and start Trados Studio again.
:::

## Automatic Migration

If you are updating from an older version, both programs will automatically reorganise the folder on their next startup. No manual action is required – your settings, licence, and data are preserved.

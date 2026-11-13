---
title: "Project Settings"
---

Supervertaler for Trados automatically saves and restores your termbase configuration when you switch between Trados projects. This means each project can use its own Supervertaler database, write targets, and termbase settings without manual reconfiguration.

## How it works

When you open a different Trados project (or switch to a document from another project), the plugin:

1. **Saves** the current project's settings to a project-specific file
2. **Loads** the new project's settings (if they exist)
3. **Reloads** the termbase with the new configuration

If no project-specific settings exist yet (first time opening a project), the current global settings are used. Once you make any changes and click OK in Settings, those settings are saved for that project.

:::note
**No action needed:** Per-project settings work automatically in the background. Just configure your termbases as usual – the plugin remembers your choices per project.
:::

## What's saved per project

| Setting | Saved per project? | Notes |
|---------|-------------------|-------|
| Supervertaler database path | Yes | Each project can use a different `.db` file |
| Enabled/disabled termbases (Read toggle) | Yes | Different termbases active per project |
| Write targets | Yes | Different write targets per project |
| Project termbase (pink highlighting) | Yes | Different project termbase per project |
| MultiTerm visibility | Yes | Different MultiTerm termbases enabled per project |
| AI context termbase filters | Yes | Different termbases in AI prompts per project |
| Active prompt | Yes | Each project remembers its [active prompt](/trados/ai-assistant/super-memory/active-prompt/) for Quick Add and Batch Translate |
| API keys and provider settings | No | Shared across all projects |
| Panel font size | No | UI preference, shared |
| Term shortcut style | No | UI preference, shared |
| Dialogue sizes | No | UI layout, shared |

## Storage location

Per-project settings are stored as individual JSON files inside your [user data folder](/trados/data-folder/):

```
C:\Users\{you}\Supervertaler\trados\projects\
```

Each file is named with a hash and the project name (e.g., `a1b2c3d4 - MyProject.json`). The JSON file also contains the original project path for reference.

:::caution
**Moving a Trados project** to a different folder creates a new project key. The plugin will treat it as a new project and use global defaults until you reconfigure. The old project settings file remains in the `projects` folder and can be safely deleted.
:::

## Interaction with global settings

Global settings (`settings.json`) serve as the defaults for projects that don't have their own settings file yet. When you open a project for the first time, the global termbase configuration is used. Once you change settings and click OK, those settings are saved for that specific project.

Settings that are always global (API keys, font size, shortcut preferences) are never overridden by project settings.

## Stamping the project's name and client on Studio TMs

Studio can add a value – the project's name, say – to every translation unit it stores in a TM. It does so only if the TM has a field for that value and you typed the value in the project's TM settings. That is easy to forget. Supervertaler can fill in the project's name and its client for you, each time you open a project.

### Switching it on

Open Supervertaler's settings and go to **General**. Under **Studio translation memories** there are two tick boxes:

- **Stamp the project's name on every unit Studio adds to the project's TMs**
- **Stamp the project's client (its Customer) too**

Both are unticked until you tick them.

### What it fills in

When you open a project, or a document in it, Supervertaler fills in the project's field values. In Studio you find them under **Project Settings > Language Pairs > All Language Pairs > Translation Memory and Automated Translation > Update**, in the **Field values** list.

| Value | Goes into a field called |
| --- | --- |
| The project's name, for example *PROJ-001* | **Project** (also Projekt, Job) |
| The project's customer, for example *Acme* | **Client** (also Customer, Kunde) |

Studio then adds these values to every translation unit it stores: each segment you confirm, and the batch task **Update Main Translation Memories**. This works for file TMs and GroupShare TMs alike. A language pair that has its own list of TMs gets the values in its own settings too.

The values stay in the project's settings, where you can see them, change them or remove them. A project you rename keeps its old name there until you clear it.

### A TM stores only the fields it has

A TM made with Studio's default settings has no Project or Client field, so there is nowhere for the value to go. Click **This project's TMs...**, under the two tick boxes, to see how things stand. The window lists the project's TMs, with **Yes** or **No** for a Project field and for a Client field.

From that window you can add a missing Project or Client field to a file TM of your own:

- **One TM at a time, after a warning**, because adding a field changes the TM.
- **Translation units already in the TM are not changed.** Only those added from then on carry the field.
- **The new field is used straight away.** You do not need to close the document or reopen the project: the next segment you confirm is stored with the value.
- **Never for a GroupShare TM, a read-only TM, or a project that came in a package or from GroupShare.**

### What is never changed or filled in

- **A value you typed in the Field values list yourself** is never changed.
- **A picklist field** is not filled in: Supervertaler cannot make up a value for a list of fixed choices.
- **A field that two of the project's TMs define differently** (as text in one and as a picklist in the other, say) is not filled in. Studio leaves such a field out of its own list too.
- **The document's name** cannot be stamped on a Studio TM: Studio's field values are for the whole project, not for one document. [EverTM](/trados/evertm/#what-is-stamped-on-a-segment-you-confirm) does store the document's name.

### Projects from a package or GroupShare

A project that came in a package or from GroupShare is left alone altogether. Its TMs are usually the agency's, and your project's name should not end up in them unasked.

If you do want it for such a project, open it, click **This project's TMs...** and tick **This project came from a package or GroupShare: stamp its name and client into its TMs anyway**. That choice is kept with the project.

:::note
[EverTM](/trados/evertm/) needs none of this. It stamps the project, client, document and more on every segment you confirm, with a tick box for each in its own window. See [What is stamped on a segment you confirm](/trados/evertm/#what-is-stamped-on-a-segment-you-confirm).
:::

---

## See Also

- [EverTM](/trados/evertm/)
- [TermLens Settings](/trados/settings/termlens/)
- [AI Settings](/trados/settings/ai-settings/)
- [Backup & Restore](/trados/settings/backup/)

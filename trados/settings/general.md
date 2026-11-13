---
title: "General settings"
---

The **General** tab is the first tab of Supervertaler's settings. To open it, click the gear icon in the Supervertaler Assistant panel.

## Appearance

**UI scale** is here. A change takes effect after you restart Trados Studio.

## Privacy

**Share anonymous usage statistics (no personal data)** switches the anonymous ping at startup on or off. The change takes effect the next time you start Trados Studio. See [Usage Statistics](/trados/settings/usage-statistics/) for exactly what is sent and what is not.

## Panels

Tick **Show SuperSearch as a tab in the Supervertaler Assistant panel** to have [SuperSearch](/trados/supersearch/) as a tab in that panel instead of in a panel of its own, then restart Trados Studio. This needs a Supervertaler licence; without one, SuperSearch stays in its own panel.

## Studio translation memories

Studio can add a value – the project's name, say – to every translation unit it stores in a TM. It does so only if the TM has a field for that value and you typed the value in the project's TM settings. That is easy to forget. Supervertaler can fill in the project's name and its client for you, each time you open a project.

### Switching it on

There are two tick boxes:

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

A TM made with Studio's default settings has no Project or Client field, so there is nowhere for the value to go. Click **This project's TMs...**, under the two tick boxes, to see how things stand. The window lists the project's TMs, with a **Project field** and a **Client field** column. Each says one of these:

| The column says | Meaning |
| --- | --- |
| **yes**, with the field's exact name, for example *yes ("Project")* or *yes ("client")* | The TM has the field. |
| **no** | The TM has no such field. |
| **clash: see below** | Two of the project's TMs define the field differently. The window explains below the list. |
| **not text** | The TM has the field, but not as a text field, so it is not filled in. |

From that window you can add a missing Project or Client field to a file TM of your own:

- **One TM at a time, after a warning**, because adding a field changes the TM.
- **The field gets the same name and type as the project's other TMs already use**, so Studio sees one field. The button shows the exact name it will add, for example **Add field "client"...**. If no other TM has the field, it adds "Project" or "Client".
- **Sometimes nothing is added, and the window says why.** That is so when the other TMs already define the field in different ways, when they use a picklist, or when the TM already has the field under another name.
- **Translation units already in the TM are not changed.** Only those added from then on carry the field.
- **The new field is used straight away.** You do not need to close the document or reopen the project: the next segment you confirm is stored with the value.
- **Never for a GroupShare TM, a read-only TM, or a project that came in a package or from GroupShare.**

### What is never changed or filled in

- **A value that is already there** – one you typed, or one a project template brought along – is never changed. If it is not this project's name or client, **This project's TMs...** says so, and **Use this project's values...** replaces it after showing you what changes.
- **A picklist field** is not filled in: Supervertaler cannot make up a value for a list of fixed choices.
- **A field that two of the project's TMs define differently** (as text in one and as a picklist in the other, say, or as text with one value in one TM and several in another) is not filled in. Studio leaves such a field out of its own list too. **This project's TMs...** names the TMs and says how each defines the field. Make them the same in Studio's TM settings (**Fields**). A value that was already there still applies, though Studio no longer lists the field.
- **The document's name** cannot be stamped on a Studio TM: Studio's field values are for the whole project, not for one document. [EverTM](/trados/evertm/#what-is-stamped-on-a-segment-you-confirm) does store the document's name.

"client" and "Client" in two TMs show as two rows in Studio's Field values list, one of them empty. That is only how Studio lists them: both TMs get the value.

:::tip
A project made from a project template inherits the template's Field values, including an old project's name. Clear the Project value in the template once, and new projects start empty, so Supervertaler fills in each project's own name.
:::

### Projects from a package or GroupShare

A project that came in a package or from GroupShare is left alone altogether. Its TMs are usually the agency's, and your project's name should not end up in them unasked.

If you do want it for such a project, open it, click **This project's TMs...** and tick **This project came from a package or GroupShare: stamp its name and client into its TMs anyway**. That choice is kept with the project.

:::note
[EverTM](/trados/evertm/) needs none of this. It stamps the project, client, document and more on every segment you confirm, with a tick box for each in its own window. See [What is stamped on a segment you confirm](/trados/evertm/#what-is-stamped-on-a-segment-you-confirm).
:::

## Data folder

Shows where your data folder is. Click **Open** to open it in File Explorer, or **Move…** to move it. See [Data Folder and Team Folder](/trados/data-folder/).

## Team folder

Optional. A team folder lets a team share its memory banks and prompt library from a folder on a file server, while everything personal stays in each person's own data folder. Click **Browse…** to choose the folder, or **Clear** to stop using it; either takes effect the next time you start Trados Studio. See [Sharing memory banks and prompts with a team folder](/trados/data-folder/#sharing-memory-banks-and-prompts-with-a-team-folder).

---

## See Also

- [Per-Project Settings](/trados/settings/project-settings/)
- [Data Folder and Team Folder](/trados/data-folder/)
- [Usage Statistics](/trados/settings/usage-statistics/)
- [EverTM](/trados/evertm/)

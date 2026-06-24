---
title: "Backup"
---

Supervertaler protects your work with two independent backup mechanisms, both on the **Settings → 💾 Backup** tab. Use the **?** button on that tab (or press **F1**) to return to this page.

## Auto Backup (time-based)

Automatically saves the current project at a regular interval to guard against crashes and forgotten saves.

- **Enable automatic backups** – turn the timer on or off.
- **Backup interval** – how often to save, in minutes (default **5**, range 1–60).

Each run saves the project file and exports a `<project>_backup.tmx` alongside it. This **overwrites** the working files in place — it keeps the latest state current, but it is not a history you can step back through. For that, use timestamped backups below.

## Timestamped project backups (every N saves)

Keeps **immutable, dated snapshots** of the project file (`.svproj`) so you can roll back to an earlier state — like a lightweight version history.

- **Keep timestamped project backups** – enable or disable the feature.
- **Back up every N saves** – how often a snapshot is taken, counted in save operations (default **1** = every save). Both manual saves (Ctrl+S) and the timed auto-backup above count toward N.
- **Keep the last K backups** – how many snapshots to retain per project (default **100**). Older ones are pruned automatically.

Snapshots are written to a dedicated folder under your user-data location:

```
<user data>\workbench\backups\<project name>\<project name>_YYYYMMDD-HHMMSS.svproj
```

Use the **Open folder…** button on the Backup tab to jump straight there.

:::note
Taking a snapshot just copies the project file you already saved, so it adds no noticeable delay — backing up on every save is fine even on large projects.
:::

### Restoring a backup

1. Click **Open folder…** on the Backup tab (or browse to the path above).
2. Find the snapshot with the timestamp you want (filenames sort chronologically).
3. Copy it somewhere safe and rename it (e.g. drop the timestamp), then open it from **Project → Open**, or replace your current `.svproj` with it while Supervertaler is closed.

:::tip
Because every save can be a snapshot and old ones are pruned for you, if something ever goes wrong you can almost always step back to a known-good version from a minute or two earlier.
:::

## Related

- [General Settings](general.md)

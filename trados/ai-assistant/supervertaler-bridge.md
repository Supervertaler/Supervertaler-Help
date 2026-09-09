---
title: "Supervertaler Bridge"
---

The **Supervertaler Bridge** is a small localhost-only HTTP service inside the Trados plugin. It is what the [Supervertaler MCP Server](/trados/mcp-server/) talks to: when Claude Desktop, Claude Code or another AI app reads your open project, searches a TM, runs a QA check or drafts translations into the document, every one of those calls goes over this bridge. It runs in the background, exposes its endpoints on `127.0.0.1` only, and is gated behind a per-session bearer token.

You never need to configure it. This page exists so you know what is running, why it is safe, and where to look if the MCP server cannot find Trados.

## What it does

The bridge exposes the state of the open Trados project to a local client, and accepts a small set of write actions from it:

- The active source segment and your current target draft, with a few surrounding segments
- TM matches Trados has found for the active segment, and concordance search over the project's TMs
- Termbase hits from your enabled termbases, and term lookups
- Project name, file list, languages and statistics
- Inserting or updating translations, adding comments, saving the document

This is the same context the in-Trados Supervertaler Assistant chat uses for its own answers. The full list of operations is the MCP server's [tool table](/trados/mcp-server/#what-it-can-do); the bridge is the plumbing under it.

## When it runs

The bridge is started automatically when **both** of these are true:

1. You have **Assistant access** – a paid subscription or an active trial. Users without Assistant access never start the bridge.
2. You have **opened the Supervertaler Assistant panel** at least once in this Trados session. The panel is lazy – Trados doesn't initialise it until you activate it.

On start it writes a handshake file, `~/Supervertaler/trados/runtime/bridge.json`, holding the port, the token and the Trados process id; the MCP server reads that file to find the running Studio. The bridge is stopped when Trados Studio exits. If Trados crashes or is force-killed, the next start detects the stale handshake and replaces it with a fresh one.

There is no switch to turn the bridge off. Until v18.20.188 a hidden `sidekickBridgeEnabled` setting existed for the retired Supervertaler Workbench integration; it was removed in v18.20.189, since the bridge now exists for the MCP server alone. A user without Assistant access never has a bridge running.

## Privacy and security

The bridge is designed to be safe for everyday use:

- **Loopback-only.** The HTTP listener binds exclusively to `127.0.0.1`. Other devices on your network – even on the same Wi-Fi – can never reach it. There is a defence-in-depth check that rejects any non-loopback `RemoteEndPoint` even if the binding ever drifts.
- **Per-session authentication token.** A fresh GUID is generated every time the bridge starts. Clients must present it as a `Bearer` token. Stale tokens from previous sessions are useless.
- **Random high port.** The bridge picks a random port in the 49152–65535 range to avoid collisions with other local services.
- **No external network access.** The bridge only listens; it never reaches out to any external service.

## Troubleshooting

The bridge writes a diagnostic log to two locations on every start:

- `~/Supervertaler/trados/runtime/bridge.log` – under your Supervertaler user-data folder
- `%TEMP%\Supervertaler-bridge.log` – guaranteed-writable fallback

The log is truncated on every plugin start, so it always reflects the current Trados session. The first lines record the resolved data-folder path so you can see exactly where the plugin is looking.

Useful entries to look for:

| Log line | Meaning |
|----------|---------|
| `Initialize: HasAssistantAccess=false` | Your licence isn't picked up as paid or trial. The bridge is correctly skipped in this case. |
| `port NNNNN bind failed: HttpListenerException code=5` | Windows is refusing to let the plugin bind to a localhost port. Rare; usually means a strict group-policy environment. |
| `Start() complete. Bridge live on http://127.0.0.1:NNNNN/` | All good – the bridge is running and the handshake file should be at `~/Supervertaler/trados/runtime/bridge.json`. |

If `bridge.json` exists and contains `port`, `token`, `pid`, and `startedAt`, the bridge is healthy. The MCP server's `list_trados_instances` tool shows every running Studio it can see.

## Endpoint reference (advanced)

For developers who want to integrate other tools with the bridge, here are the two oldest endpoints; the MCP server's tool definitions (`mcp-tools.json` in the plugin) describe the rest, each with its method, path and parameters. **The URL prefix is versioned** so future schema changes can ship without breaking older clients.

### `GET /v1/active-context`

Returns a JSON snapshot of the current Trados project state. Authentication via `Authorization: Bearer <token>` from the handshake file.

```json
{
  "available": true,
  "project": {
    "name": "ACME-PROJ-001",
    "fileName": "20260101 PROJ-001 Application as filed.docx",
    "sourceLang": "nl-BE",
    "targetLang": "en-US"
  },
  "activeSegment": { "source": "...", "target": "..." },
  "surroundingSegments": [
    { "source": "...", "target": "..." }
  ],
  "tmMatches": [
    { "score": 95, "source": "...", "target": "...", "tmName": "..." }
  ],
  "termbaseHits": [
    { "source": "...", "target": "...", "termbaseName": "...",
      "definition": "...", "domain": "...", "notes": "..." }
  ]
}
```

When no document is active, returns `{"available": false}` with HTTP 200.

### `POST /v1/insert-translation`

Inserts text into the active Trados target segment via the same code path as the in-Chat Apply-To-Target button.

Request body:

```json
{ "text": "The translation to insert" }
```

Response on success:

```json
{ "ok": true }
```

Response on failure (e.g. no active segment):

```json
{ "ok": false, "error": "no active document" }
```

## Related pages

* [Supervertaler MCP Server](/trados/mcp-server/) – the client this bridge exists for
* [Supervertaler](/trados/ai-assistant/) – the in-Trados chat that uses the same context fields the bridge exposes
* [User Data Folder](/trados/data-folder/) – where the handshake file lives

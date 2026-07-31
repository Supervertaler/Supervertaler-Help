---
title: "Superbrowser (Multi-Chat AI Browser)"
---

Superbrowser puts ChatGPT, Claude, and Gemini side by side in one window – three resizable browser columns, each with its own persistent login – so you can put the same question to all three and compare the answers without switching tabs or juggling browser windows.

Open it from **Tools → 🌐 Superbrowser…**. It opens in its own window, so it can live on a second monitor next to your translation work.

<figure><img src="/.gitbook/assets/Supervertaler-Superbrowser.png" alt="The Superbrowser window with ChatGPT, Claude, and Gemini side by side in three labelled columns, each giving its own answer to the question: what is the best CAT tool in 2026?"><figcaption><p>One question, three opinions – ChatGPT, Claude, and Gemini answering “What is the best CAT tool in 2026?” side by side.</p></figcaption></figure>

### How it works

* **Three columns, three services** – ChatGPT (left), Claude (centre), Gemini (right), each in a full embedded browser. Drag the dividers to resize.
* **Persistent logins** – each column keeps its own isolated browser profile, so you sign in once per service and stay signed in between Supervertaler sessions. Profiles are stored under `workbench/superbrowser_profiles/` in your Supervertaler data folder.
* **Custom URLs** – click **Show Configuration** (top right) to point any column at a different address – a specific chat session, a project conversation, or another service entirely – and apply all three at once with **Update URLs**.

### Why compare models?

Different models genuinely differ on translation questions – terminology choices, register, how they handle an ambiguous source. Asking all three at once tells you in seconds whether an answer is a consensus or one model's opinion, which is exactly when a second opinion is worth having.

:::note
Superbrowser was removed in v1.9.385 during a round of simplification, and restored in v1.10.365 after a user asked for it back. If you used it before, your logins should still be there – the removal deliberately left the profile folder on disk, and the restored tool picks it straight back up.
:::

:::caution
The columns are real browser sessions, so each service's own sign-in flow applies. If a provider objects to an embedded browser during login (Google is occasionally strict about this), complete the sign-in once in the column and it will be remembered from then on.
:::

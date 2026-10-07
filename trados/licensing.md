---
title: "Licensing"
---

Supervertaler for Trados uses a simple subscription model: one product, one price, everything included.

## Free Trial

When you first install Supervertaler for Trados, a **14-day free trial** starts automatically. During the trial, all features are unlocked – TermLens, AI Assistant, SuperSearch, memory banks, Studio Tools, and everything else.

No sign-up or credit card is required to start the trial. The remaining days are shown in the **Licence** tab in Settings and in the About dialogue.

## Pricing

| | Monthly | Annual |
|---|---------|--------|
| **Supervertaler for Trados** | €20/month | €200/year |

One plan, all features included: TermLens inline terminology, AI Assistant & Batch Translate, SuperSearch cross-file search & replace, SuperMemory memory banks, Studio Tools, Clipboard Mode, QuickLauncher, Prompt Library, MultiTerm support, Incognito Mode, and all future features.

:::note
Annual plans include **2 months free** compared to monthly billing.
:::

## Purchasing a Licence

1. Visit [supervertaler.com/trados](https://supervertaler.com/trados/) and click **Subscribe**
2. Complete the checkout – you will receive a **licence key** by email
3. Open Trados Studio → **Settings → Licence** tab
4. Paste your licence key and click **Activate**

Your licence allows activation on up to **2 machines** (e.g. a desktop and a laptop).

## Activating Your Licence

1. Open Trados Studio
2. Click the **gear icon** (⚙) on the TermLens or Supervertaler Assistant panel
3. Go to the **Licence** tab
4. Enter your licence key in the text field
5. Click **Activate**

A confirmation message appears when activation succeeds. The Licence tab shows your plan name, masked licence key, status, and last verification date.

:::tip
You can also reach the Licence tab by clicking the licence status text in the **About** dialogue (accessible via the **?** button on any panel).
:::

## Managing Your Subscription

From the **Licence** tab in Settings, you can:

- **Verify Now** – manually check your licence status with the server
- **Deactivate** – remove the licence from this machine (frees up an activation slot)
- **Manage subscription →** – opens the Lemon Squeezy billing portal where you can update payment details or cancel

## Offline Use

After activation, the plugin caches your licence status locally. You can work offline for up to **30 days** before the plugin needs to verify your licence again. When you reconnect to the internet, verification happens automatically in the background.

## What Happens When the Trial Expires

After the 14-day trial ends:

- **No licence** – all features show a "licence required" overlay. Your termbases, settings, and prompt library are preserved.
- **Active licence** – all features are unlocked.

Activating a licence immediately unlocks all features.

## Changing Machines

If you replace a computer or need to move your licence:

1. On the old machine: open **Settings → Licence** and click **Deactivate**
2. On the new machine: enter your licence key and click **Activate**

If you can no longer use the old machine, enter your key on the new one anyway. If the key has no activations left and you brought your data folder over from the old machine, Supervertaler releases the old machine's activation to make room once it has gone a day unused *(from v18/19.20.199)*. Otherwise, for example after a fresh install on a new computer when the old one can no longer be used, [get in touch](https://beijer.uk/contact) and we will free the old activation for you.

## One Licence per Computer and Windows Account *(from v18/19.20.199)*

A licence counts only for the computer and Windows account it was activated on. If one data folder is used from more than one computer or Windows account – shared with colleagues, or synced between your own computers – each of them keeps its own licence record in it, with its own trial and its own activation, and none can overwrite another's. Each colleague needs a licence of their own. To share memory banks and prompts in a team, use a [team folder](/trados/data-folder/#sharing-memory-banks-and-prompts-with-a-team-folder) rather than one shared data folder.

### After renaming your computer or reinstalling Windows

Your licence was activated under the computer's old name or the old Windows installation, so it does not count as it is. Supervertaler tells you so when Trados Studio starts, and **Settings → Licence** explains it above the licence key box. Enter your licence key there and click **Activate**. If the key has no activations left, the old activation recorded in your data folder is released to make room once it has gone a day unused; until then, try again the next day.

## Privacy & Security

The plugin makes **no network calls** except to:

1. **Your chosen AI provider** (OpenAI, Anthropic, Google Gemini, OpenRouter, or local Ollama) – only when you use AI features
2. **Lemon Squeezy licence API** (`api.lemonsqueezy.com`) – for licence activation and periodic validation
3. **Anonymous usage statistics** (on by default; you can turn them off with one click) – a single ping on startup with a random anonymous ID, the plugin, Trados and Windows versions, your system locale and a few display and hardware details, never anything you translate. See [Usage Statistics](/trados/settings/usage-statistics/) for the full list.

The licence validation sends only your licence key and a hashed machine fingerprint (a one-way hash of your computer name, your Windows user ID and the serial number of the drive Windows is installed on). No personal data, no translation content, no termbase information is ever collected.

Your API keys are stored locally in `%LocalAppData%\Supervertaler.Trados\settings.json` and are never transmitted anywhere except to your chosen AI provider.

:::note
The full source code is available on [GitHub](https://github.com/Supervertaler/Supervertaler-for-Trados) for security audit. You can verify exactly what the plugin does and does not transmit.
:::

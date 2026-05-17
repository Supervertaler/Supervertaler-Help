# Deployment to Cloudflare Pages

Step-by-step setup for publishing this site at **`help.supervertaler.com`** on Cloudflare Pages, free tier.  One-time setup; afterwards every `git push` to `main` auto-deploys.

## 0. Prerequisites

- A Cloudflare account.  Sign up free at <https://dash.cloudflare.com/sign-up> if you don't have one.
- DNS for `supervertaler.com` must be managed by Cloudflare (Cloudflare nameservers).  If it's currently elsewhere (Namecheap, GoDaddy, etc.) you'll need to migrate the domain to Cloudflare DNS first — Cloudflare's onboarding walks you through it; it's a 5-minute change at your domain registrar.

## 1. Create the Pages project

1. Log in to <https://dash.cloudflare.com>.
2. Left sidebar → **Workers & Pages** → **Create**.
3. Pick the **Pages** tab → **Connect to Git**.
4. Authorise Cloudflare's GitHub app if prompted, then choose the **`Supervertaler/Supervertaler-Help`** repository.
5. Click **Begin setup**.

## 2. Build configuration

Set the project up exactly as below:

| Field | Value |
|---|---|
| **Project name** | `supervertaler-help` (becomes the default `*.pages.dev` subdomain) |
| **Production branch** | `main` |
| **Framework preset** | **Astro** (Cloudflare auto-detects from `package.json`; selecting this fills the next two fields automatically — confirm the values match below) |
| **Build command** | `npm run build` |
| **Build output directory** | `dist` |
| **Root directory** | *(leave blank — uses repo root)* |
| **Node version** | `22.12.0` or later — set via env var (see below).  The pinned Astro 5 in `package.json` works on 22.11+ too, but newer Node is recommended. |

### Environment variables

In the same setup screen, expand **Environment variables (advanced)** and add:

| Variable | Value |
|---|---|
| `NODE_VERSION` | `22.12.0` (Cloudflare reads this to install the right Node toolchain for the build.) |

Click **Save and Deploy**.  Cloudflare runs `npm install && npm run build` and publishes `dist/` to a `*.pages.dev` URL within ~2 minutes.

## 3. Verify the first deploy works

Once the build finishes (green checkmark in the Cloudflare dashboard), open the assigned `*.pages.dev` URL — something like `https://supervertaler-help.pages.dev/`.

Sanity-check:

- [ ] Landing page loads (the splash with two product cards).
- [ ] Clicking "Open the Trados Plugin docs" lands on `/trados/...` content.
- [ ] Clicking "Open the Workbench docs" lands on `/workbench/...` content.
- [ ] Search (Ctrl+K) returns hits with both Trados and Workbench results.
- [ ] One or two pages with images render with the images visible (not broken).
- [ ] Hint callouts render as styled boxes, not as literal `:::note` text.

If any of those fail, the Cloudflare build log shows what went wrong — open the deploy in the dashboard and scroll the build output.

## 4. Attach the custom domain `help.supervertaler.com`

In the Cloudflare Pages project view:

1. **Custom domains** tab → **Set up a custom domain**.
2. Enter **`help.supervertaler.com`**.
3. Cloudflare creates the DNS CNAME record automatically (since DNS is managed in the same Cloudflare account) and provisions an SSL cert (Let's Encrypt, free).  Takes ~1 minute.
4. The site is now live at <https://help.supervertaler.com>.

## 5. After deploy works: re-point the in-app Help links

In Workbench (`modules/help_system.py`) and Trados (`Core/HelpSystem.cs`), update the base URL constant from `https://supervertaler.gitbook.io/help/` to `https://help.supervertaler.com/`.  Both files have a single base-URL constant + per-topic slug enums, so the change is one edit each.

Once those go out in the next Workbench / Trados version bumps, the in-app **Help** buttons point at the new site.

## 6. Decommission GitBook (when you're confident)

Once `help.supervertaler.com` has been live and stable for a couple of weeks:

1. In GitBook (web UI), replace the site content with a single "We've moved" page linking to <https://help.supervertaler.com>.
2. Optionally configure URL redirects from old GitBook page slugs to the new equivalents (Pro plan feature; on free, the single notice page is the simplest option).
3. Eventually unpublish the GitBook space entirely.

The `Supervertaler-Help` repo's `SUMMARY.md`, `README.md`, and `.gitbook/` folder become dead weight at this point and can be removed in a cleanup commit.

## Local development from here on

After cloning the repo on any machine:

```bash
cd Supervertaler-Help
npm install
npm run dev       # http://localhost:4321/ — hot-reloads on file changes
npm run build     # static build into dist/
npm run preview   # serves the built dist/ at http://localhost:4321/
```

Editing any `.md` file under `trados/` or `workbench/` triggers a live reload in `npm run dev`.  No build step needed during writing — push when ready and Cloudflare rebuilds automatically.

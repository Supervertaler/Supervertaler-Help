// Post-build step: copy the legacy ./.gitbook/assets/ folder into the build
// output as dist/.gitbook/assets/, so existing image references in the .md
// content like `../../.gitbook/assets/screenshot.png` resolve at runtime
// without rewriting every page body.
//
// This bridge stays in place for as long as GitBook is the legacy sync
// target (because GitBook also expects images at `.gitbook/assets/`).  Once
// GitBook is fully decommissioned, the images can be moved to `public/assets/`
// and all references swept in one pass — but doing that now would break the
// GitBook fallback during the migration window.

import { cpSync, existsSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(here, '..');

const src = join(repoRoot, '.gitbook', 'assets');
const destParent = join(repoRoot, 'dist', '.gitbook');
const dest = join(destParent, 'assets');

if (!existsSync(src)) {
  console.warn(`[copy-gitbook-assets] Source ${src} not found — skipping.`);
  process.exit(0);
}

if (!existsSync(destParent)) {
  mkdirSync(destParent, { recursive: true });
}

cpSync(src, dest, { recursive: true });
console.log(`[copy-gitbook-assets] Copied ${src} -> ${dest}`);

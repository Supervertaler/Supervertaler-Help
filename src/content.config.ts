// Astro content collection config for Starlight.
//
// We deliberately keep the Trados and Workbench docs in their existing
// repo-root folders (`./trados/` and `./workbench/`) rather than moving
// them under the conventional `src/content/docs/` path. Two reasons:
//
// 1. GitBook (the legacy host, kept live during the migration window)
//    syncs from those root folders via the existing .gitbook.yaml /
//    SUMMARY.md.  Moving the files would break that sync immediately.
// 2. Zero file moves means zero risk of broken internal links during
//    the migration.  The same .md files render in both systems.
//
// The custom `glob` loader scans the two product folders plus a single
// `index.mdx` at the repo root (the landing page).  The README.md and
// SUMMARY.md at the root are GitBook-only and are deliberately excluded
// from the Starlight build.

import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
  docs: defineCollection({
    loader: glob({
      pattern: [
        '{trados,workbench}/**/*.{md,mdx}',
        'index.mdx',
      ],
      base: './',
      // GitBook's convention is that `<folder>/README.md` is the homepage
      // for that folder.  Astro / Starlight defaults treat README as a
      // regular page, so without this rewrite `trados/README.md` would
      // be served at `/trados/readme/` and `/trados/` would 404.  We
      // rewrite the entry id so README pages become the directory index:
      //
      //   trados/README.md       → id "trados"   → URL /trados/
      //   workbench/README.md    → id "workbench" → URL /workbench/
      //   trados/installation.md → id "trados/installation" → URL /trados/installation/
      //   index.mdx              → id "index"   → URL /  (Starlight default)
      //
      // The rewrite preserves the GitBook convention without renaming
      // any files (which would break the GitBook sync running in parallel).
      generateId: ({ entry }) => {
        const noExt = entry.replace(/\.(md|mdx)$/i, '');
        return noExt.replace(/(^|\/)README$/i, '');
      },
    }),
    schema: docsSchema(),
  }),
};

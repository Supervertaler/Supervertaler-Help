// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
  // Production URL for sitemap / canonical / OpenGraph tags.
  // Update if the chosen subdomain changes.
  site: 'https://help.supervertaler.com',

  integrations: [
    starlight({
      title: 'Supervertaler Help',
      description: 'Help and documentation for the Supervertaler suite — Trados Studio plugin and Workbench standalone app.',

      // Two genuinely separate product trees in the sidebar.  Each product
      // gets its own top-level group, auto-generated from the folder.  This
      // is the first cut — restructure to mirror the SUMMARY.md sections
      // in a later pass once the basic build is verified to work end to end.
      sidebar: [
        {
          label: '🧩 Supervertaler for Trados',
          autogenerate: { directory: 'trados' },
        },
        {
          label: '🖥️ Supervertaler Workbench',
          autogenerate: { directory: 'workbench' },
        },
      ],

      // Social / external links shown in the top-right of the header.
      social: [
        {
          icon: 'github',
          label: 'GitHub: Workbench',
          href: 'https://github.com/Supervertaler/Supervertaler-Workbench',
        },
        {
          icon: 'github',
          label: 'GitHub: Trados plugin',
          href: 'https://github.com/Supervertaler/Supervertaler-for-Trados',
        },
        {
          icon: 'external',
          label: 'supervertaler.com',
          href: 'https://supervertaler.com',
        },
      ],

    }),
  ],

  // Default Astro publicDir is `./public/`; we don't override it.  The legacy
  // `.gitbook/assets/` folder is copied into `dist/.gitbook/assets/` by a
  // post-build script (see _migrate/copy-gitbook-assets.mjs, wired into
  // `npm run build`) so existing `../../.gitbook/assets/foo.png` references
  // in the .md files resolve without any page-body sweep.
});

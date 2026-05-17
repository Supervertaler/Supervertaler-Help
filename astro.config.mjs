// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// Sidebar structure is generated from SUMMARY.md (the GitBook-canonical
// nav) by _migrate/generate_sidebar.py.  Re-run that script whenever
// SUMMARY.md changes; the JS output is committed so Cloudflare Pages
// builds don't depend on Python.
import sidebar from './src/generated/sidebar.js';

// https://astro.build/config
export default defineConfig({
  // Production URL for sitemap / canonical / OpenGraph tags.
  // Update if the chosen subdomain changes.
  site: 'https://help.supervertaler.com',

  integrations: [
    starlight({
      title: 'Supervertaler Help',
      description: 'Help and documentation for the Supervertaler suite — Trados Studio plugin and Workbench standalone app.',

      // Component overrides — see ./src/components/ for the customisations.
      // Head:    injects per-page Pagefind product filter metadata.
      // Search:  replaces the default Pagefind UI with a custom one that
      //          scopes by current section and groups results by product.
      // Sidebar: hides the OTHER product's tree on a product page (so
      //          /trados/* shows only Trados, /workbench/* shows only
      //          Workbench).  Landing page and other non-product pages
      //          still see both trees.
      components: {
        Head: './src/components/Head.astro',
        Search: './src/components/Search.astro',
        Sidebar: './src/components/Sidebar.astro',
      },

      // Sidebar structure imported from ./src/generated/sidebar.js, which
      // is generated from SUMMARY.md by _migrate/generate_sidebar.py.
      // Two top-level groups (🧩 Trados / 🖥️ Workbench), each with the
      // original GitBook section grouping (Get Started, Features,
      // Settings, Reference, etc.) and human-readable labels.
      //
      // The custom Sidebar override (./src/components/Sidebar.astro) hides
      // the OTHER product's tree when the user is on a product page, so
      // /trados/* shows only Trados and /workbench/* shows only Workbench.
      sidebar,

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

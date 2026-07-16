// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightLlmsTxt from 'starlight-llms-txt';

// Sidebar structure is generated from SUMMARY.md (the GitBook-canonical
// nav) by _migrate/generate_sidebar.py.  Re-run that script whenever
// SUMMARY.md changes; the JS output is committed so Cloudflare Pages
// builds don't depend on Python.
import sidebar from './src/generated/sidebar.js';

// https://astro.build/config
export default defineConfig({
  // Production URL for sitemap / canonical / OpenGraph tags.
  // Update if the chosen subdomain changes.
  site: 'https://docs.supervertaler.com',

  integrations: [
    starlight({
      title: 'Supervertaler Docs',
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
        SocialIcons: './src/components/SocialIcons.astro',
        // Footer: default footer + a small "AI-readable docs" note
        // linking the llms.txt endpoints generated at build time.
        Footer: './src/components/Footer.astro',
      },

      // Theme tweaks (sidebar shading, etc.) — see src/styles/custom.css.
      customCss: ['./src/styles/custom.css'],

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

      // llms.txt for AI agents (https://llmstxt.org/): generates
      //   /llms.txt        — index with links to the docs as Markdown
      //   /llms-full.txt   — the entire docs in one Markdown file
      //   /llms-small.txt  — abridged version for small context windows
      // plus per-product subsets under /_llms-txt/. Supervertaler ships
      // an MCP server, so being conveniently machine-readable is part
      // of the product story, not just SEO. Pinned to 0.7.x — newer
      // plugin versions require Starlight >= 0.38.
      plugins: [
        starlightLlmsTxt({
          details:
            'Supervertaler is a suite of AI-enhanced translation tools: ' +
            'a Trados Studio plugin (TermLens terminology, AI assistant, ' +
            'batch operations, MCP server for Claude Desktop) and the ' +
            'standalone Workbench CAT tool.',
          optionalLinks: [
            {
              label: 'supervertaler.com',
              url: 'https://supervertaler.com',
              description: 'Product website',
            },
            {
              label: 'GitHub: Workbench',
              url: 'https://github.com/Supervertaler/Supervertaler-Workbench',
              description: 'Supervertaler Workbench source and releases',
            },
            {
              label: 'GitHub: Trados plugin',
              url: 'https://github.com/Supervertaler/Supervertaler-for-Trados',
              description: 'Supervertaler for Trados issues and releases',
            },
          ],
          customSets: [
            {
              label: 'Supervertaler for Trados',
              description:
                'Docs for the Trados Studio plugin only',
              paths: ['trados/**'],
            },
            {
              label: 'Supervertaler Workbench',
              description:
                'Docs for the standalone Workbench app only',
              paths: ['workbench/**'],
            },
          ],
        }),
      ],

    }),
  ],

  // Default Astro publicDir is `./public/`; we don't override it.  The legacy
  // `.gitbook/assets/` folder is copied into `dist/.gitbook/assets/` by a
  // post-build script (see _migrate/copy-gitbook-assets.mjs, wired into
  // `npm run build`) so existing `../../.gitbook/assets/foo.png` references
  // in the .md files resolve without any page-body sweep.
});

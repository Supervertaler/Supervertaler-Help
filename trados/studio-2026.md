---
title: "Trados Studio 2026 & .ttb Termbases"
---

Trados Studio 2026 introduces a new termbase format –the SQLite-based **`.ttb`** file –and drops the legacy MultiTerm engine that earlier versions relied on. Supervertaler for Trados supports Studio 2026 through a dedicated build that reads `.ttb` termbases directly.

## Two builds, one product

Supervertaler for Trados ships as two separate plugin builds from the same codebase:

| Build | For | Termbase format |
|-------|-----|-----------------|
| **Supervertaler for Trados** | Trados Studio 2024 | MultiTerm `.sdltb` |
| **Supervertaler for Trados (Studio 2026)** | Trados Studio 2026 | `.ttb` |

Install the build that matches your Studio version. The 2024 build will not load in Studio 2026, and vice versa, because the two Studio releases use different plugin frameworks and termbase engines.

## TermLens and `.ttb` termbases

In Studio 2026, TermLens reads the new `.ttb` termbases attached to your project automatically –there is nothing to configure. Terms appear as **green chips** in the TermLens panel, exactly as MultiTerm terms do in the 2024 build, and behave the same way (click to insert, or **Alt+1**–**Alt+9** to insert by number).

`.ttb` termbases are **read-only** in TermLens, just like MultiTerm termbases. To add or edit terms, use Studio 2026's built-in Termbases view.

Everything else –the Supervertaler, Batch Translate, SuperSearch, the Term Picker, AI terminology injection –works identically across both builds.

## What about my existing `.sdltb` termbases?

Studio 2026 cannot open `.sdltb` files directly; the MultiTerm engine that read them is no longer part of the base install. Instead, **RWS provides conversion to the new `.ttb` format**:

* The **Termbases view** in Studio 2026 has a wizard to migrate `.sdltb` → `.ttb`.
* Opening a project package that contains an `.sdltb` termbase converts it to `.ttb` on the fly.
* When a 2026 user sends a package back to someone still on Studio 2024, Studio can create a "compatible" package that the older version converts back to `.sdltb` automatically.

Once your termbase is in `.ttb` form, TermLens picks it up automatically. There is no separate step in Supervertaler –convert in Studio, and the terms appear.

:::note
If you work in both Studio 2024 and Studio 2026, keep using the MultiTerm `.sdltb` build for your 2024 projects. The 2026 build is only for Studio 2026 and its `.ttb` termbases. See [MultiTerm Support](multiterm-support.md) for the 2024 workflow.
:::

## Technical notes

* `.ttb` is a SQLite 3 database with full-text search. TermLens opens it in read-only mode, so Studio can keep using it at the same time with no risk of corruption.
* Studio 2026 is a 64-bit application. The 2026 build is 64-bit to match; the 2024 build remains 32-bit/AnyCPU for the MultiTerm JET driver it depends on.

## See also

* [MultiTerm Support](multiterm-support.md) –the equivalent `.sdltb` workflow in Studio 2024
* [TermLens](termlens.md)
* [Installation (Trados)](installation.md)
* [Troubleshooting](troubleshooting.md)

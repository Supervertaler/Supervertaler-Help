---
title: "Supervertaler for Trados"
---

Supervertaler for Trados is a plugin for **Trados Studio 2024+** that brings Supervertaler’s terminology and AI features directly into the Trados editor. It runs natively inside Trados Studio as a set of dockable panels, so you never have to leave the editor.

<figure><img src="/.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

### Getting Started Screencast

New to Supervertaler? Watch the [Getting Started screencast](https://www.youtube.com/watch?v=bOIwMAoP7xc) (16 min) for a walkthrough of all the basics – TermLens, prompt generation, AI translation, the Chat window, and more.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/bOIwMAoP7xc" title="Supervertaler for Trados – Getting Started (16 min)" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Key Features

#### TermLens (Inline Terminology)

Live terminology display that shows the source text word by word, with termbase translations underneath each matched term. Colour-coded by termbase type:

* **Blue** for regular termbase matches
* **Pink** for project termbase matches (higher priority)
* **Yellow** for non-translatable terms
* **Green** for MultiTerm termbase matches (`.sdltb` files attached to your Trados project, or `.ttb` termbases in Trados Studio 2026)

Numbered badges let you insert terms with **Alt+1** through **Alt+9**. Project termbases are detected automatically from your Trados project and are read-only. On Trados Studio 2026 these are the new `.ttb` termbases –see [Trados Studio 2026 & .ttb](studio-2026.md).

#### Supervertaler

A conversational AI chat panel that is aware of your current segment, matched terminology, and TM matches. Ask questions about translation choices, get alternative phrasings, or request explanations –all without leaving Trados.

#### Batch Translate

Translate multiple segments at once using AI. Choose a scope (empty segments, all segments, filtered segments), pick a prompt, and let the AI work through your file. Progress is shown in real time.

#### Prompt Library

A built-in Default Translation Prompt and Default Proofreading Prompt to get you started, plus QuickLauncher prompts for common tasks. Create your own custom prompts in the Prompt Manager – duplicate the default and tailor it to your domain.

#### Termbase Management

Create, edit, and import termbases in Supervertaler's `.db` format. Quick-add terms with keyboard shortcuts, mark terms as non-translatable, and manage multiple termbases per project.

#### SuperMemory

Self-organising, AI-maintained translation knowledge base. Stores client profiles, terminology decisions, domain conventions, and style preferences as interlinked Markdown files. The AI consults the active memory bank automatically when translating. Keep separate banks per client or domain and switch between them from the toolbar dropdown. Quick-add terms and corrections while translating with Ctrl+Alt+M. [Learn more →](ai-assistant/super-memory.md)

### System Requirements

| Requirement    | Version             |
| -------------- | ------------------- |
| Trados Studio  | 2024 (v18) or later |
| Windows        | 10 or 11            |
| .NET Framework | 4.8                 |

There are two builds: one for **Trados Studio 2024** (MultiTerm `.sdltb` termbases) and one for **Trados Studio 2026** (`.ttb` termbases). Install the build that matches your Studio version –see [Trados Studio 2026 & .ttb](studio-2026.md).

### Shared Termbase Format

Supervertaler for Trados uses the same SQLite-based termbase format (`.db`) as [Supervertaler Workbench](https://help.supervertaler.com/workbench/). Termbases created in either tool are fully compatible – you can open the same `.db` file in both applications.

### Context-Sensitive Help

Press **F1** at any time to open context-sensitive help for the panel or dialogue that currently has focus.

### Next Steps

<table data-view="cards"><thead><tr><th></th><th></th></tr></thead><tbody><tr><td><strong>Installation</strong></td><td><a href="installation.md">Install the plugin →</a></td></tr><tr><td><strong>Getting Started</strong></td><td><a href="getting-started.md">Set up termbases and AI →</a></td></tr><tr><td><strong>TermLens</strong></td><td><a href="termlens.md">Inline terminology display →</a></td></tr><tr><td><strong>Supervertaler</strong></td><td><a href="ai-assistant.md">Chat with AI in Trados →</a></td></tr><tr><td><strong>MultiTerm Support</strong></td><td><a href="multiterm-support.md">Use MultiTerm termbases in TermLens →</a></td></tr><tr><td><strong>Batch Translate</strong></td><td><a href="batch-translate.md">Translate segments in bulk →</a></td></tr><tr><td><strong>Keyboard Shortcuts</strong></td><td><a href="keyboard-shortcuts.md">All shortcuts at a glance →</a></td></tr></tbody></table>

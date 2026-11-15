---
title: "Chat"
---

The **Chat** tab is the conversational heart of the Supervertaler Assistant – a context-aware chat that already knows your current segment, its terminology and TM matches, so you can ask questions and get answers grounded in the document you are translating. (See the [Overview](/trados/ai-assistant/) for opening the pane and the basics of chatting.)

Two features extend what a chat can do:

- **[File Attachments](/trados/ai-assistant/file-attachments/)** – attach images or documents (a reference PDF, a style guide, a screenshot of the source layout) to a message for the AI to use as context.
- **[Studio Tools](/trados/ai-assistant/studio-tools/)** – ask the assistant about your Trados installation in plain language (projects, translation memories, termbases, templates) and it looks the answer up for you.

## Include full document content in AI context (from v18/19.20.208)

In a strip just above the box you type in is the tick box **Include full document content in AI context**. When it is ticked, the whole document goes to the AI as context with every message, so the AI can see what kind of document this is and what the rest of it says. A long document is cut down to the number of segments set as **Max segments** in [AI Settings](/trados/settings/ai-settings/#max-segments). It costs more input tokens: untick it to spend less, for instance when you ask many small questions.

- **What follows it:** Chat and [QuickLauncher](/trados/quicklauncher/).
- **The batch features have a tick box of their own**, with the same label, on the [Batch Operations tab](/trados/batch-operations/#include-full-document-content-in-ai-context-from-v181920208): Batch Translate, Batch Proofread, Translate active segment (`Alt+T`), Clipboard Mode, Preview prompt and SuperBench follow that one. Neither box changes the other.

Before v18/19.20.208 there was one tick box for everything, in Settings → AI Settings. It is gone from there. Both new tick boxes start with the value it had, so nothing changes until you untick one of them. What is sent is described under [Include full document content](/trados/settings/ai-settings/#include-full-document-content).

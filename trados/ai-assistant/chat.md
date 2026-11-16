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

## Supervertaler's own notices are not sent to the AI (from v18/19.20.208)

Some of the text in the chat is written by Supervertaler itself, not by the AI: the memory bank report, "Switched to memory bank …", "Prompt saved as …" and the result of **Harvest changes**. These notices are shown in the chat and are still there after a restart, but they are not part of your conversation with the AI:

- **They are not sent to the AI.** Before v18/19.20.208 each notice was sent with every later chat message, as if the AI had written it, and you paid for it as input tokens. A memory bank report alone can be a few hundred words.
- **They do not take up places in the remembered conversation.** The chat sends your last 10 to 13 messages along with each new one. A notice used to take one of those places, so a few of them pushed your real questions and answers out.
- **Still sent:** error messages in the chat, and the list made by **Reference numbers** on the Batch Operations tab, so that you can ask the AI about them.
- **Chats saved before v18/19.20.208** load as before. The notices already in them were saved as answers and are still sent as such until you clear the chat.

## Buttons that answer in the chat (from v18/19.20.208)

Three things on the SuperMemory bar, above the tabs, write their answer into the chat: the **☰ Report** button, **Harvest changes**, and **(match by project name)** in the Memory Bank dropdown. From v18/19.20.208 the pane switches to the Chat tab and scrolls to the answer, whichever tab you clicked from. Before, the pane stayed on the tab you were on, so from the Batch Operations, Import/Export or Reports tab the button seemed to do nothing. An error from **Open folder** is shown the same way.

Notices you did not ask for, such as "Switched to memory bank …" when you open another project, still arrive in the chat without taking you away from the tab you are working on.

## The saved chat

The conversation is saved after every message and put back the next time Trados Studio starts (see [Chat History](/trados/ai-assistant/#chat-history)). Before v18/19.20.208 it could be lost at start-up: if Studio opened with a document already open and that project used a different memory bank, the earlier conversation was replaced by the one notice about the switch. That is fixed.

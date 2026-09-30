---
title: "PDF Rescue"
---

## Overview

**PDF Rescue** is a specialised AI-powered OCR tool designed to extract clean, editable text from poorly formatted PDFs. Built into Supervertaler, it uses vision-capable LLM OCR to intelligently recognise text, formatting, redactions, stamps, and signatures–producing professional, translator-ready documents.

### 🎯 The Problem It Solves

Have you ever received a PDF translation job where:
- The text won't copy-paste cleanly?
- Line breaks are all over the place?
- Formatting is completely broken?
- Traditional OCR produces gibberish?
- Redacted sections show as black boxes?
- Stamps and signatures clutter the text?

**PDF Rescue fixes all of this.**

###  Real-World Success Story

> *"I had a client reach out for a rush job–a 4-page legal document that had clearly been scanned badly. Traditional OCR couldn't handle it, and manual retyping would have taken hours.*
> 
> *I used PDF Rescue's one-click PDF import, processed all 4 pages with AI OCR, and it produced a flawless Word document that I could immediately start working with. What would have been a multi-day nightmare became a straightforward job I could deliver on time.*
> 
> *I was able to tell my client that I could handle the job–and delivered professional quality. PDF Rescue literally saved a client relationship."*
> 
> – Michael Beijer, Professional Translator

---

## ✨ Key Features

### 1. 📄 **One-Click PDF Import**
- **No external tools needed** – Import PDFs directly
- **Automatic page extraction** – Each page saved as high-quality PNG (2x resolution)
- **Persistent storage** – Images saved next to source PDF in `{filename}_images/` folder
- **Client-ready** – Images can be delivered to end clients if needed

### 2. 🧠 **Smart AI-Powered OCR**
- **Vision-capable LLM OCR** – High accuracy OCR
- **Context-aware** – Understands document structure and formatting
- **Intelligent cleanup** – Fixes line breaks, spacing, and formatting issues
- **Redaction handling** – Inserts descriptive placeholders like `[naam]`, `[bedrag]` in document language
- **Stamps & signatures** – Detects and describes non-text elements: `[stempel]`, `[handtekening]`

### 3. 🎨 **Optional Formatting Preservation**
- **Markdown-based** – Uses `**bold**`, `*italic*`, `__underline__`
- **Toggle on/off** – User-controlled via checkbox
- **Clean output** – Markdown converted to proper formatting in DOCX export
- **Visual preview** – See formatting markers before export

### 4. 📊 **Batch Processing**
- **Process selected** – Work on individual images
- **Process all** – Batch process entire document
- **Progress tracking** – Visual progress bar and status updates
- **Skip processed** – Already-processed images are skipped (unless re-selected)

### 5. 📝 **Comprehensive Logging**
- **Activity log integration** – All operations logged with timestamps
- **PDF import progress** – Each page extraction logged
- **OCR processing** – Per-image processing logged
- **DOCX export** – Export operations tracked

### 6. 👁️ **Full Transparency**
- **"Show Prompt" button** – View exact instructions sent to AI
- **Configuration display** – See model, formatting settings, max tokens
- **No black boxes** – Complete visibility into AI processing

### 7. 📊 **Professional Session Reports**
- **Markdown format** – Clean, readable documentation
- **Complete configuration** – All settings recorded
- **Processing summary** – Table of all images and status
- **Full extracted text** – All OCR results included
- **Statistics** – Character/word counts and averages
- **Supervertaler branding** – Professional client-ready reports

### 8. 💾 **Flexible Export Options**
- **Markdown + Word export** – One click writes a Markdown file, a formatted Word document (with optional bold/italic/underline) and a session report
- **Copy to clipboard** – Quick text extraction
- **Session reports** – Professional MD documentation

### 9. 🚀 **Standalone Mode**

If you run Supervertaler from source, PDF Rescue can also run on its own, outside Supervertaler:

```bash
python modules/pdf_rescue_Qt.py
```

Full-featured standalone application with all capabilities.

---

## 🎯 Workflow

### Quick Start (5 Steps)

1. **Open PDF Rescue** – Open the **Tools menu** at the top of the window → **📄 PDF Rescue…**. The tool opens in its own window.
2. **Import PDF** – Click "📄 Import PDF", select your badly-formatted PDF
3. **Check formatting option** – Leave "Preserve formatting" checked (default)
4. **Process** – Click "⚡ Process ALL" to OCR all pages
5. **Export** – Click "💾 Export Markdown & Word" to create the Word document

**That's it!** You now have a clean, editable Word document ready for translation.

---

### Detailed Workflow

#### Step 1: Import Your PDF

**Method 1: Direct PDF Import** (Recommended)
```
Click: 📄 Import PDF
→ Select PDF file
→ Automatic page extraction to {filename}_images/ folder
→ All pages added to processing queue
```

**Method 2: Manual Image Import**
```
Click: ➕ Add Image Files → Select individual images
OR
Click: 📂 Folder → Select folder with images
```

**Result**: All images listed in left panel with ✓ status indicators

---

#### Step 2: Configure Settings

**Model Selection** (the **AI Model** dropdown; vision-capable models, grouped by provider):
- **OpenAI**: `gpt-5.5` (Recommended – flagship, the default), `gpt-5.4-mini` (budget option)
- **Claude**: `claude-sonnet-5-5`, `claude-opus-5-5`, `claude-fable-5-1`
- **Gemini**: `gemini-3.1-flash-lite`, `gemini-2.5-pro`, `gemini-3.1-pro-preview`

The **Model Capabilities** box below the dropdown says what each model is good at.

**Formatting Option**:
- ✓ **Preserve formatting (bold/italic/underline)** – Enabled by default
- Unchecked = Plain text output only

**Extraction Instructions**:
- Default instructions optimized for badly formatted PDFs
- Handles redactions, stamps, signatures automatically
- Can customize if needed (advanced)
- Click **"👁️ Show Prompt"** to see exact AI instructions

---

#### Step 3: Process Images

**Option A: Process Selected**
```
1. Select image(s) in list
2. Click: 🔍 Process Selected
3. View result in preview pane
```

**Option B: Process All** (Recommended)
```
1. Click: ⚡ Process ALL
2. Confirm batch processing dialog
3. Watch progress bar
4. All pages processed automatically
```

**Processing Details**:
- Each image sent to the OCR model
- Text extracted with context awareness
- Formatting detected (if enabled)
- Redactions/stamps/signatures handled
- Results stored in memory
- ✓ indicator appears when processed

---

#### Step 4: Review & Export

**Review Extracted Text**:
- Click any processed image in list
- Preview pane shows extracted text
- Formatting shown as markdown (`**bold**`, `*italic*`, etc.)
- Verify quality before export

**Export Options**:

1. **💾 Export Markdown & Word** (Primary export)
   - Asks for one file name and writes three files: `name.md` (the extracted text as Markdown), `name.docx` (the formatted Word document) and `name_report.md` (the session report)
   - Markdown converted to proper formatting in the Word document
   - A heading per page (*Page 1: filename*)
   - Ready for translation work

2. **📋 Copy All**
   - All text to clipboard
   - Includes page separators
   - Quick paste into any application

3. **📊 Session Report**
   - Professional markdown documentation
   - Complete configuration record
   - All extracted text included
   - Statistics and metadata
   - Client-ready deliverable

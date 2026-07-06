---
title: "Termbase Basics"
---

Termbases help ensure consistent terminology across your translations.

## What is a Termbase?

A termbase is a database of terms with their translations:

| Source (EN) | Target (NL) | Domain | Notes |
|-------------|-------------|--------|-------|
| software | software | IT | Don't translate |
| click | klikken | IT | Verb |
| machine learning | machinaal leren | AI | Official term |

## Why Use Termbases?

1. **Consistency**: Same term = same translation every time
2. **Efficiency**: Don't look up the same term twice
3. **Quality**: Use approved terminology
4. **Client requirements**: Follow style guides

## Termbase Features in Supervertaler

### Automatic Highlighting

Terms from active termbases are highlighted in the source text:
- Green background by default
- Hover to see the translation
- Higher priority = darker shade

### Multiple Termbases

Maintain separate termbases for:
- Different clients
- Different domains (legal, medical, IT)
- Different projects

### Priority Levels

Assign priority (1-10) to terms:
- Priority 1 (highest): Must be used
- Priority 5: Standard terms
- Priority 10: Optional/suggestions

### Forbidden Terms

Mark terms as "forbidden" to flag text that should NOT be translated or should be avoided.

## Creating Your First Termbase

1. Go to the **Termbases** tab
2. Click **+ Create Termbase**
3. Enter a name (e.g., "Client ABC Terminology")
4. Choose source and target languages
5. Click **Create**

## Adding Terms

### Manually

1. Click on your termbase
2. Click **+ Add Term**
3. Enter source term, target term
4. Optionally add domain, notes, priority
5. Click **Save**

### From Selection

1. Select text in the source column
2. Right-click → **Add to Termbase**
3. Enter the target translation
4. Choose which termbase to add to

### Import from File

1. Go to the **Termbases** tab
2. Click **Import**
3. Select a TSV file (tab-separated: source, target, domain, notes)
4. Watch the progress dialog

## Termbase Settings

### Activation

Termbases must be activated to show matches:
- ✅ **Read**: Terms are highlighted and shown in lookups
- ✅ **Write**: New terms can be added during translation

### Highlight Style

Choose how terms appear in the grid:
- **Background**: Green background shading
- **Dotted Underline**: Subtle underline
- **Semibold**: Bold text

Go to **Settings → View Settings → Termbase Highlight Style**.

---

## See Also

- [Creating Termbases](creating.md)
- [Importing Terms](importing.md)
- [Term Highlighting](highlighting.md)
- [Sending Terms to the AI](ai-injection.md)
- [TermLens (Inline Terminology)](termlens.md)
- [Term Extraction](extraction.md)

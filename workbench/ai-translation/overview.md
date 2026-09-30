---
title: "Overview"
---

Supervertaler integrates with leading AI language models for high-quality translation.

## Supported Providers

| Provider | Models |
|----------|--------|
| **OpenAI** | GPT-5.5, GPT-5.4 Mini |
| **Anthropic** | Claude Sonnet 4.6, Claude Haiku 4.5, Claude Opus 4.8 |
| **Google** | Gemini 3.1 Flash-Lite, Gemini 2.5 Pro, Gemini 3.1 Pro (Preview), Gemma 4 26B MoE |
| **Mistral** | Mistral Large, Mistral Small |
| **DeepSeek** | DeepSeek V4 Pro, DeepSeek V4 Flash |
| **OpenRouter** | 200+ models via a single API key |
| **Ollama** | TranslateGemma, Qwen 3, Aya Expanse (local, free) |
| **Custom** | Any OpenAI-compatible endpoint |

See [Supported LLM Providers](/workbench/ai-translation/providers/) for setup instructions for each provider.

## Quick Start

1. [Set up API keys](/workbench/get-started/api-keys/)
2. Open a project with segments to translate
3. Select a segment
4. Press `Ctrl+T` to translate

## Translation Methods

### Single Segment

Translate one segment at a time:
- Select a segment
- Press `Ctrl+T` or click **Translate** button
- AI translation appears in the target cell
- Review, edit, and confirm

### Batch Translation

Translate multiple segments at once:
- Select segments (Shift+click for range)
- Press `Ctrl+Shift+T` or use **Translate → Batch Translate**
- Configure options in the dialog
- All selected segments are translated

:::note
Supervertaler has multiple batch scopes (selected / not-started / etc.). Start with **Translate → Batch Translate → Translate all not-started & pre-translated**.
:::

### TM + AI Hybrid

Combine Translation Memory with AI:
1. TM matches are checked first
2. High matches (e.g., >90%) are used directly
3. Lower matches are AI-translated with TM context
4. No matches use pure AI translation

## Prompts

Prompts control how the AI translates. A good prompt includes:

- Translation direction (source → target language)
- Domain/subject matter
- Style guidelines
- Terminology rules
- Special instructions

### Example Prompt

```
You are a professional Dutch-to-English translator specializing 
in technical documentation. 

Maintain formal register. Use American English spelling. 
Keep all formatting tags like {1}, <b>, </b> in place.

Translate naturally while preserving the original meaning.
```

See [Creating Prompts](/workbench/ai-translation/prompts/) and [Prompt Manager](/workbench/ai-translation/prompt-library/) for more.

## Provider Selection

### In Settings

1. Go to the **⚙️ Settings** tab
2. Open **🤖 AI Settings**
3. Choose your preferred provider under **🤖 LLM Provider Selection** and the model under **📦 Model Selection**

There is no Save button: the change is saved a moment after you make it.

### Where to check which model is in use

The status bar shows the current model. **Project → 📋 Project Info…** lists it too, with its provider, at the top of the **AI & Prompts** section, and the Batch Translate dialog shows it as **📊 Current LLM**.

## Quality Tips

### Get Better Results

1. **Use specific prompts** - Include domain, style, and rules
2. **Provide context** - Enable "include context" for surrounding segments
3. **Add termbase terms** - Attach terminology for consistent translations (see [Sending Terms to the AI](/workbench/termbases/ai-injection/))
4. **Post-edit** - AI is great but not perfect; always review

### Common Issues

| Issue | Solution |
|-------|----------|
| Wrong terminology | Add terms to termbase, include in prompt |
| Inconsistent style | Be more specific in your prompt |
| Tags removed/moved | Explicitly tell AI to preserve tags |
| Too literal | Ask for "natural, fluent" translation |

**Slightly garbled tags are repaired for you.** Some models return a numbered inline tag a little wrong: `< 1>`, `</ 1 >`, `<1 />`, or HTML-escaped as `&lt;1&gt;`. Since v1.10.372, AI translations – batch, single-segment and FuzzyFixer – are repaired as they arrive, and each such tag is put back into its exact form instead of ending up in your target as plain text. Only tags that the source segment really contains are touched, so an ordinary `<` or `>` in the text is left alone. A tag pair left empty, with the words outside it, is not guessed at: the [tag check](/workbench/qa/tag-validation/) still reports it.

## Cost Management

### API costs

Cloud providers typically charge by usage (tokens). Pricing and free tiers change over time, so treat each provider dashboard as the source of truth.

Supervertaler logs the tokens and cost of every AI call. The Batch Translate dialog shows an estimate before you start, and **Project → 📋 Project Info…** shows what the project has cost so far. See [Token Usage & Costs](/workbench/ai-translation/usage-costs/).

### Reducing Costs

1. **Use Ollama** (local) when appropriate
2. **Translate only what you need** (for example not-started segments)
3. **Pre-translate with TM** when you have good matches
4. **Use smaller/faster models** for drafts, larger models for final passes

---

## Learn More

<table data-view="cards">
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Single Segment</strong></td>
<td><a href="single-segment.md">Translate one at a time →</a></td>
</tr>
<tr>
<td><strong>Batch Translation</strong></td>
<td><a href="batch-translation.md">Translate in bulk →</a></td>
</tr>
<tr>
<td><strong>Creating Prompts</strong></td>
<td><a href="prompts.md">Write effective prompts →</a></td>
</tr>
<tr>
<td><strong>Local AI (Ollama)</strong></td>
<td><a href="ollama.md">Free, private AI →</a></td>
</tr>
</tbody>
</table>

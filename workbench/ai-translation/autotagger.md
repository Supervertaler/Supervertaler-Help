---
title: "AutoTagger"
---

AutoTagger looks at where the inline tags sit in the **source** segment and inserts that same set of tags into your **existing translation** at the right places – without changing any of the translated words.

It is for the common case where a target has the correct translation but is **missing its tags or has them in the wrong spots** – typically after machine translation, pasting from another tool, or typing the target by hand. Those segments otherwise trip tag-validation checks even though the wording is fine.

## How it works

1. AutoTagger strips whatever tags are currently in the target.
2. It asks the AI to re-place the **full set of tags from the source** at the correct positions in your translation.
3. It **validates** the result before writing it: the tag set must match the source, the words must be unchanged, and the tags must be well-formed.
4. If the AI's output doesn't validate, it **retries once**. If it still fails, AutoTagger leaves the target **untouched** – so it never writes broken tags.

Because the words are preserved exactly, AutoTagger is safe to run on a translation you have already reviewed.

## Running it on a single segment

Run AutoTagger on the active segment one of three ways:

- Click the **🏷️ AutoTagger** button on the editor toolbar.
- Choose **Translate → 🏷️ Auto-tag Current Segment**.
- Press **Ctrl+Alt+G**.

Undo (`Ctrl+Z`) reverts it.

## Running it on many segments

Use **Bulk Operations → 🏷️ Auto-tag Segments** to re-tag segments that are **already translated**. It runs over the selected segments (or all segments if none are selected) and the whole run is a single Undo.

> **Note:** Ordinary AI translation (single-segment or Batch Translate) already places inline tags as part of the translation, so you do **not** need to run AutoTagger after translating. AutoTagger is for fixing tags on text that was translated some **other** way (MT, paste, hand-typed). The older "Fix tags with AutoTagger after translating" toggle in the Batch Translate dialog was removed in v1.10.319 for this reason.

## Configuring it

Settings → **System Prompts** → **AutoTagger Instruction**. This editable template tells the AI how to place the tags. It supports these placeholders:

| Placeholder | Meaning |
| ------------- | ------- |
| `{{SOURCE_TEXT}}` | The source segment, with its inline tags |
| `{{TARGET_TEXT}}` | Your current translation (tags stripped) |
| `{{TAG_LIST}}` | The list of tags that must be placed |

## Tracking cost

AutoTagger's AI calls are logged under their own **"AutoTagger"** task in [Token Usage & Costs](usage-costs.md) (a bulk pass logs the tag-placement step as AutoTagger). Group the usage table by Task to see them broken out.

---

## See Also

- [FuzzyFixer](fuzzyfixer.md)
- [Tag Validation](../qa/tag-validation.md)
- [Batch Translation](batch-translation.md)
- [Prompts](prompts.md)
- [Token Usage & Costs](usage-costs.md)

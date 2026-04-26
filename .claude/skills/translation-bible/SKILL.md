---
name: translation-bible
description: Maintain translation-bible.md as the project's long-term memory. Auto-trigger when an agent in the translation loop is about to introduce a proper noun, encounters a proper noun in source text, detects an inconsistency with an earlier translation, or is constructing the glossary during guideline preparation. Internal — users rarely invoke directly.
---

# translation-bible

This skill enforces bible discipline during the multi-agent translation loop. It frames `translation-bible.md` as the project's **long-term memory** — the mechanism that maintains coherence and consistency across an entire book (Wu et al. 2024, §3.2.1, "Long-Term Memory Management").

## When to trigger

Any of:

- An agent is about to **introduce a new proper noun** (person, place, organization, dated event, technical term, cultural reference) in a draft.
- An agent **encounters a proper noun in source text** for the first time.
- An agent **detects an inconsistency** between a current draft and a prior chapter in `OUTPUT.md` involving a proper noun, date, or canonical translation.
- The Junior Editor (Addition agent) is **constructing the glossary** during Algorithm 1 / guideline preparation.

## The discipline

### Rule 1 — Check before introducing

Before writing a proper noun in any draft, search `translation-bible.md` for the source term. If it's there, use the canonical target translation. No exceptions.

### Rule 2 — Add when missing

If the proper noun isn't in the bible, add it before continuing the draft. Pick the appropriate section (People, Places, Organizations, Dates and historical events, Technical terms, Cultural references). Fill source name, target name, and a notes column with disambiguating context (era, role, alternate spellings).

During Algorithm 1 glossary construction, the Junior Editor adds liberally; the Senior Editor (Subtraction) prunes generic terms in the next iteration. Outside Algorithm 1, only add things that genuinely warrant canonical treatment — common nouns don't belong in the bible.

### Rule 3 — Bible is authoritative on conflicts

If a current draft conflicts with the bible:

- **If the bible is right:** fix the draft.
- **If the bible is wrong** (you've found stronger evidence — e.g., the source spells the name differently than the bible records, or the era is wrong): fix the bible *first*, then update any prior translations in `OUTPUT.md` that used the old form, *then* continue the current draft.

A prior translation in `OUTPUT.md` that contradicts the bible is a bug, not a precedent.

### Rule 4 — Style decisions go in the bible too

Decisions that aren't entries-per-se but shape the translation systematically (transliteration system, name order, honorific handling, measurement conversions, currency treatment) belong in the **Style decisions** section. Once recorded, treat them as binding.

### Rule 5 — Log contested decisions

When you choose between two reasonable translations of the same term, log it in the **Decisions log** with the date and a one-sentence reason. This prevents future passes from re-litigating settled choices.

## Read/write protocol

- **Read:** before any draft step that mentions a proper noun, scan the relevant section. Don't skip — partial recall isn't reliable across a long book.
- **Write:** edit `translation-bible.md` directly with the Edit tool. Preserve table structure. Don't reorder existing rows.
- **Commit:** bible updates ride along with the chapter commit they came from (`feat(translation): add ch{N}` or `chore(bible): record decision on {term}`). Don't accumulate uncommitted bible changes across multiple chapters.

## What does NOT go in the bible

- Common nouns translated literally.
- One-off transliterations of incidental background characters who never recur.
- Synonym choices that are local to a single sentence's voice.
- Anything you can derive from re-reading source text — the bible is for *decisions*, not raw lookups.

When in doubt, leave it out. A bloated bible slows every future read step.

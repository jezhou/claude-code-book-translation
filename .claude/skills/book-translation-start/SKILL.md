---
name: book-translation-start
description: Run the multi-agent translation loop on the next chapter from sources/. Trigger when the user says "translate the next batch," "translate the next chapter," "run the loop," "start translating," when the user asks to translate from sources/, or on /book-translation-start. Requires agent-personas.md and translation-bible.md to exist (run book-translation-setup first if not).
---

# book-translation-start

Runs one full pass of the multi-agent translation loop, faithful to Wu et al. 2024, *(Perhaps) Beyond Human Translation* (arXiv:2405.11804). The output is a polished translated chapter appended to `OUTPUT.md`.

## Preconditions

- `agent-personas.md` exists (run `book-translation-setup` if not).
- `translation-bible.md` exists.
- `sources/` has at least one un-translated chapter.
- The user's CLAUDE.md project header (source language / target language / target audience) is filled.

## The loop at a glance

```
Preparation         → Selection → Guideline (Algorithm 1)
Execution           → Translation → Localization → Proofreading   (each is Algorithm 2)
Final Review        → Senior Editor solo: per-chapter quality + inter-chapter flow
Append + commit     → OUTPUT.md, then split_book.py, then conventional commit
```

See `loop-diagram.md` for the mermaid version. See `algorithms.md` for Algorithm 1 (Addition-by-Subtraction) and Algorithm 2 (Trilateral) — both have a max of 2 iterations with early exit.

## Persona discipline

Every agent **must** adopt its persona from `agent-personas.md` before producing text. Read the persona, become the persona, then act. This is a precondition for every Action / Critique / Judgment / Addition / Subtraction step below — not a one-time setup.

## Stage 1 — Preparation [paper §3.2.1]

### Selection

Default unit: **one chapter**. Pick the next un-translated chapter from `sources/`.

If `sources/` is OCR'd page files (no chapter structure), gather pages that comprise one chapter and treat the gathered set as the unit. Note this in the guideline as a deviation from per-chapter batching.

### Guideline construction (Algorithm 1: Addition-by-Subtraction)

Run the Junior Editor (Addition agent) and Senior Editor (Subtraction agent) per `algorithms.md` Algorithm 1. Iterate up to 2 times; early exit if no further changes.

The output is a guideline with **exactly five components** [paper §3.2.1]:

1. **Glossary** — proper nouns appearing in this chapter, cross-referenced against `translation-bible.md`. Junior Editor extracts liberally; Senior Editor prunes generic words. New entries delegate to the `translation-bible` skill for the actual write.
2. **Book Summary** — short context on where this chapter sits in the book.
3. **Tone** — the narrative voice for this chapter.
4. **Style** — the prose style.
5. **Target Audience** — re-state who this is being written for. (Pulled from CLAUDE.md, refined for chapter specifics.)

Use `guideline-scaffold.md` (bundled) as the structure. The guideline is prefixed to every Action prompt in Stage 2.

## Stage 2 — Execution [paper §3.2.2]

Three sub-stages, each running **Algorithm 2 (Trilateral Collaboration)**: Action → Critique → Judgment, max 2 iters, early exit when Judgment approves. Roles are fixed across sub-stages:

| Sub-stage | Action | Critique | Judgment |
|---|---|---|---|
| Translation | Translator | Junior Editor | Senior Editor |
| Localization | Localization Specialist | Junior Editor | Senior Editor |
| Proofreading | Proofreader | Junior Editor | Senior Editor |

Each sub-stage's output feeds the next.

- **Translation** — fidelity-first source-to-target draft. Translator works from the guideline + source chapter.
- **Localization** — adapt for the target audience. Eliminate translationese, smooth idioms, ensure cultural references land. The Localization Specialist is monolingual target — they must not see the source.
- **Proofreading** — grammar, consistency, punctuation. Cross-check names/dates against `translation-bible.md`. Proofreader is also monolingual target.

## Stage 3 — Final Review [paper §3.2.2]

Senior Editor solo. Two checks, both required:

1. **Per-chapter quality** — does the chapter meet publication standard?
2. **Inter-chapter flow** — read the closing of the previous chapter in `OUTPUT.md` and the opening of this one. Tense, voice, narrative thread should flow naturally.

If either check fails, identify the specific defect and loop back to the relevant Stage 2 sub-stage. Do not loop endlessly — if the same defect persists after a second pass, surface it to the user.

## Append, split, commit

On Senior Editor approval:

1. Append the chapter to `OUTPUT.md` using the heading conventions in that file's comment block (the `###` chapter level by default).
2. Run `python3 split_book.py` to regenerate `book/src/`.
3. Commit with a conventional message: `feat(translation): add ch{N} — {title}`.
4. Report to the user: chapter title, word count, any flagged ambiguities the Junior Editor logged.

## When to stop

One invocation = one chapter. If the user asked for "the next few chapters," confirm the count, then loop the whole skill that many times — don't try to batch multiple chapters into one Trilateral pass (the paper translates chapter-by-chapter for a reason: long-context Critique/Judgment quality degrades).

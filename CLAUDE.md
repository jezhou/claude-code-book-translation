# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Further agent instructions are found in @AGENTS.md

## Project Purpose

This is a **{{SOURCE_LANGUAGE}}-to-{{TARGET_LANGUAGE}}** translation project. The source material is a **{{GENRE}}** titled **"{{BOOK_TITLE}}"** by **{{AUTHOR}}**. The goal is to produce a polished {{TARGET_LANGUAGE}} translation readable by **{{TARGET_AUDIENCE}}** (e.g. "American readers familiar with literary memoirs").

## Key Files

- `./sources/` — Source text files ({{SOURCE_LANGUAGE}}). Chunking strategy: **{{CHUNKING_STRATEGY}}** (e.g. "one file per scanned page", "one file per chapter"). Files may split mid-sentence due to OCR/chunk boundaries.
- `translation-bible.md` — Glossary/bible of all standardized names, places, organizations, dates, technical terms, cultural references, and known inconsistencies. **Always consult this file during translation for proper nouns and facts.** Update it as new proper nouns appear.
- `agent-personas.md` — The personas each agent in the loop must adopt before beginning work. **ALL AGENTS MUST USE THEIR ASSIGNED PERSONA BEFORE BEGINNING THEIR WORK.**
- `./drafts/` — Per-batch working drafts (e.g. `part1-batch1-draft.md`). Use these when translating large chunks across multiple agent passes.
- `OUTPUT.md` — The single canonical output file for the translated book. Continuously append new translations here and revise as needed. When complete, this file should contain the entire book in {{TARGET_LANGUAGE}}.
- `book/` — mdBook project for the web version. Chapter files in `book/src/` are generated from `OUTPUT.md` by `split_book.py`.

## Translation Architecture

The translation uses a multi-agent loop with three phases (adapted from TransAgents):

1. **Preparation** — Selection of source text, then Planning (Addition/Subtraction) to produce a Guideline for the translators.
2. **Execution** — Three sequential stages, each with an Action/Critique/Judgement sub-loop:
   - **Translation** — Initial {{SOURCE_LANGUAGE}}-to-{{TARGET_LANGUAGE}} translation
   - **Localization** — Adapt for {{TARGET_AUDIENCE}}
   - **Proofreading** — Polish grammar, style, and readability
3. **Final Review** — Last pass before appending to `OUTPUT.md`.

See `README.md` for the full loop diagram. See `templates/guideline.template.md` for the per-batch guideline scaffold.

The translation is much stronger when the agents adopt personas as part of the multi-agent loop. **ALL AGENTS MUST USE THEIR ASSIGNED PERSONA BEFORE BEGINNING THEIR WORK.** Personas are in `agent-personas.md`.

While translating, it is better to work a few chunks at a time and look ahead if you need more context on the translation. Don't bite off more than you can chew — keep translations as close to the source as possible.

## Translation Style Rules

- Target audience: **{{TARGET_AUDIENCE}}**.
- Source text may have OCR/scan errors and awkward breaks — read ahead across chunk boundaries as needed for coherent translation, but work incrementally.
- Some {{SOURCE_LANGUAGE}} words/phrases don't translate 1-to-1; prioritize natural, readable {{TARGET_LANGUAGE}} over literal fidelity.
- Cross-reference `translation-bible.md` for standardized proper nouns, place names, historical facts, and known inconsistencies.

## Output

All translated text goes into a single `OUTPUT.md` file. The agent should continuously append translations and revise as new context comes in. `split_book.py` then splits `OUTPUT.md` into per-chapter files in `book/src/` for mdBook.

After each update to `OUTPUT.md`, commit the new translations to git using conventional commits.

## Git

Configure your own git preferences here. Example conventions:

- Use conventional commits (`feat:`, `fix:`, `chore:`, `docs:`).
- Commit after each completed batch in `OUTPUT.md`.
- Push to `main` to trigger the GitHub Pages deploy.

## Installed Skills (optional)

Add skill references here as you install them. Common ones for translation projects:

- `docx` — for reading/writing Word documents (useful if you have a copy-edited reference translation in .docx form).

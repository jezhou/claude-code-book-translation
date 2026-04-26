# CLAUDE.md

Guidance for Claude Code on this repository.

## Project

Translating from **{{SOURCE_LANGUAGE}}** to **{{TARGET_LANGUAGE}}** for **{{TARGET_AUDIENCE}}**. Book metadata (title, author, translator, language code) lives in `book/book.toml`.

## How to work this project

The translation method is provided by four skills under `.claude/skills/`:

- **`book-translation-setup`** — one-time scaffolding. Generates `agent-personas.md` and `translation-bible.md`, fills `book.toml`. Run this first on a fresh project.
- **`book-translation-ingest`** — splits raw source material (PDF, large text file, OCR scans) into per-chapter files in `sources/`. Run after setup, before translating.
- **`book-translation-start`** — runs the multi-agent loop on the next chapter from `sources/`. The user invokes this per session.
- **`translation-bible`** — auto-triggers to maintain `translation-bible.md` (the project's long-term memory) whenever a proper noun is introduced or a continuity issue is found.

Method follows Wu et al. 2024, *(Perhaps) Beyond Human Translation* (arXiv:2405.11804).

## Layout

- `sources/` — source-language files. Default unit = chapter; OCR'd page files also work.
- `drafts/` — optional working drafts when a chapter spans multiple agent passes.
- `OUTPUT.md` — canonical output. Append-only. `split_book.py` regenerates `book/src/` from it.

After each approved chapter, commit with conventional commits and push to `main` (deploys via `.github/workflows/deploy.yml`).

---
name: book-translation-setup
description: One-time setup for a book translation project — generates agent-personas.md and translation-bible.md, helps fill book.toml + CLAUDE.md. Trigger when the user says "set up this translation project," "create personas," "scaffold the bible," when agent-personas.md is missing on first translation attempt, or on /book-translation-setup.
---

# book-translation-setup

This skill scaffolds a fresh book translation project so `book-translation-start` has everything it needs to run the multi-agent loop.

The method this template implements is from Wu et al. 2024, *(Perhaps) Beyond Human Translation: Harnessing Multi-Agent Collaboration for Translating Ultra-Long Literary Texts* (arXiv:2405.11804). Faithfulness to the paper matters; deviate only when noted.

## When to run

Run once per project, after the user has cloned the template. Re-run if the user wants to regenerate personas (e.g., for a different genre).

## What to produce

By the end of this skill, the project root must contain:

1. A filled `book/book.toml` (title, authors, translator, description, language code, repo URL).
2. A filled CLAUDE.md project header (source language, target language, target audience).
3. `agent-personas.md` — five personas using the paper's profile fields and role constraints.
4. `translation-bible.md` — empty bible with the canonical sections.

## Steps

### 1. Gather project facts

Ask the user (only what's still unknown — read `book.toml` and `CLAUDE.md` first):

- Source language and dialect/era (e.g., "Mandarin Chinese, Hunanese influence, mid-20th-century rural")
- Target language (e.g., "American English")
- Target audience (e.g., "American readers familiar with literary memoirs")
- Genre (memoir, fiction, biography, poetry, ...)
- Book title, author, translator's display name
- Repo URL (for `book.toml`)

### 2. Fill book.toml and CLAUDE.md

Edit `book/book.toml` placeholders directly. Update CLAUDE.md's one-line project header. Don't duplicate metadata — `book.toml` is canonical for title/author/translator/description/language; `CLAUDE.md` only carries source/target/audience because those shape Claude's behavior.

### 3. Generate agent-personas.md

Use `personas-scaffold.md` (bundled) as the structure. Generate five personas — one per paper-canonical role [paper §3.1]:

- **Senior Editor**
- **Junior Editor**
- **Translator**
- **Localization Specialist**
- **Proofreader**

(The paper also has a CEO whose only job is selecting the Senior Editor. In a single-Claude-loop world this collapses to "the user picked the project," so we omit it.)

Use the paper's profile fields [paper §3.1, Figure 1]: Name, Languages, Nationality, Gender, Age, Education, Personality, Hobbies, Years of working, Profession. Drop "Rate per word" — vestigial here.

**Persona constraints — MUST honor:**

- **Translator** is from or deeply familiar with the source-text region/era/dialect. They understand idioms and cultural references at a gut level.
- **Senior Editor** is bilingual; bridges source-region roots and target-publishing experience.
- **Localization Specialist** is intentionally **monolingual in the target language** [paper §4.2.2, MHP rationale]. No source-language ability. They evaluate the prose as a target reader would, with no source-text contamination.
- **Proofreader** is also **monolingual in the target language** for the same reason.
- **Junior Editor** has a continuity/research temperament. Detail-obsessed. Their job in the loop is to flag inconsistencies and keep the bible honest.

Tailor the personas to the user's source material — don't ship generic placeholder names. A Hunanese memoir gets a Translator from Hunan; a French detective novel gets one from Marseille; etc.

### 4. Scaffold translation-bible.md

Copy `bible-scaffold.md` (bundled) to `translation-bible.md` at the project root. Don't pre-fill entries — the bible grows as the loop encounters proper nouns. The `translation-bible` skill auto-handles updates from there.

### 5. Confirm and commit

Show the user the four files you created/edited. Ask if they want to tweak any personas before committing. On confirmation, commit with a message like `chore: scaffold translation project`.

## Done state

- `agent-personas.md` exists with 5 paper-canonical roles, each with the paper's profile fields, all four persona constraints honored.
- `translation-bible.md` exists, empty but with all canonical sections.
- `book.toml` and CLAUDE.md have no `{{PLACEHOLDER}}` strings remaining.
- Project is ready for the user to drop sources into `sources/`.

## Hand-off

If `sources/` is empty or contains only raw material (a single large file, a PDF, a `raw/` subdirectory), tell the user to invoke `book-translation-ingest` next to split it into per-chapter files. If `sources/` already has per-chapter files, point them straight at `book-translation-start`.

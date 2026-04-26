# Agent Instructions

Generic workflow notes for agents working in this translation project. Customize this file for your project's process.

## Working loop

Each batch should flow through the full multi-agent loop:

1. **Preparation**
   - **Selection**: pick a source chunk (size: enough context, not so much that it's hard to hold in one pass — typical: 5–15 pages).
   - **Planning**: produce a guideline from `templates/guideline.template.md` — identify key proper nouns, tone, time period, flagged ambiguities. Update `translation-bible.md` if new terms appear.

2. **Execution** — each stage has three roles:
   - **Action** — produces the draft.
   - **Critique** — reviews for a specific concern (fidelity, naturalness, grammar).
   - **Judgement** — decides whether to accept, revise, or re-run.

   Stages (in order):
   - **Translation** — from source to target language. Fidelity-first.
   - **Localization** — adapt idioms, cultural refs, sentence rhythm for the target audience.
   - **Proofreading** — polish grammar, consistency, punctuation. Cross-check `translation-bible.md`.

3. **Final Review** — one more pass across the full batch before appending to `OUTPUT.md`.

## Persona rule

Every agent takes on its assigned persona from `agent-personas.md` **before** producing any text. The persona shapes voice, priorities, and what the agent flags.

## Bible discipline

- Before introducing any proper noun for the first time: check `translation-bible.md`. If it's not there, add it.
- If you encounter an inconsistency with an earlier chapter, fix the bible first, then the draft.
- The bible is authoritative. Past translations that contradict it are bugs.

## Session close-out

When ending a work session:

1. Make sure `OUTPUT.md` reflects the latest approved translation.
2. Commit with a conventional message (e.g. `feat(translation): add part 3 chapters 20–22`).
3. Push to `main` — deploys via `.github/workflows/deploy.yml`.

If you use an issue tracker like [beads (bd)](https://github.com/steveyegge/beads) for tracking work, document the commands here. This template does not assume one.

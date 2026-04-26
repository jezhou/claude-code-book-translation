# Translation Bible

The project's **long-term memory** (Wu et al. 2024, §3.2.1). Single source of truth for proper nouns, place names, dates, technical terms, cultural references, and style decisions.

This file is authoritative. If a past translation contradicts the bible, fix the past translation — not the bible — unless the bible itself is wrong.

The `translation-bible` skill auto-maintains this file during the loop. You shouldn't normally need to edit by hand; entries arrive as the agents encounter new proper nouns.

---

## People

| Source name | Target name (canonical) | Notes |
|---|---|---|

## Places

| Source name | Target name (canonical) | Notes |
|---|---|---|

## Organizations / Institutions

| Source name | Target name (canonical) | Notes |
|---|---|---|

## Dates and historical events

| Source reference | Canonical form | Notes |
|---|---|---|

## Technical terms / Jargon

| Source term | Target term | Notes |
|---|---|---|

## Cultural references

| Source reference | Treatment in translation | Notes |
|---|---|---|

## Decisions log

Record decisions about contested translations so future passes don't re-litigate.

- {{DATE}} — Decided to render `{{SOURCE_TERM}}` as `{{TARGET_TERM}}` rather than `{{ALTERNATIVE}}` because {{REASONING}}.

## Style decisions

- Transliteration system: Hanyu Pinyin without tone marks (default; Wade-Giles permitted for figures whose names have established English forms, e.g., Confucius, Mencius, Lao Tzu)
- Name order: Surname-given for Chinese names (e.g., Zhuangzi, Wang Yangming); given-surname for Western names
- Honorifics: drop generic prefixes (lao-, xiao-); keep philosophically loaded titles (zi 子, fuzi 夫子) with first-occurrence gloss
- Philosophical terms: render core terms (e.g., 道, 仁, 氣) with a chosen English equivalent on first use, then keep pinyin (dao, ren, qi) thereafter — bible captures the chosen pairing per term
- Measurements: convert li/jin/etc. to imperial in narrative; preserve original with bracketed conversion in directly quoted classical text
- Citations: classical citations follow Chicago author-date when in scholarly notes; in-line attributions in the body use the canonical English title (e.g., "Analects 4.15") with pinyin transliteration on first appearance

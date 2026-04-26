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

- Transliteration system: {{e.g., Hanyu Pinyin without tone marks}}
- Name order: {{e.g., Surname-given for source-region names; given-surname for Western names}}
- Honorifics: {{e.g., drop "lao" prefix; keep "shifu" with footnote on first appearance}}
- Measurements: {{e.g., convert li to miles in dialogue, keep li with footnote in formal narration}}
- Currency: {{e.g., yuan kept as "yuan", historical currencies footnoted on first use}}

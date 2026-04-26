# Heading detection patterns

Regex patterns for finding chapter and matter boundaries in raw source material. Use these in `book-translation-ingest`'s structure detection step. All patterns are anchored to a line by themselves (`^…$`) and case-insensitive unless noted.

When scanning a source, try patterns in this order: front matter → chapter → back matter. First match per line wins.

---

## Chapter patterns

### English

| Pattern | Matches | Notes |
|---|---|---|
| `^Chapter\s+\d+\b.*$` | `Chapter 1`, `Chapter 12: The River` | Most common |
| `^Chapter\s+[IVXLC]+\b.*$` | `Chapter I`, `Chapter XII` | Roman numeral form |
| `^CHAPTER\s+(\d+\|[IVXLC]+)\b.*$` | All-caps variant | Common in older books |
| `^\d+\.\s+\w+` | `1. The Beginning` | Numbered with period |
| `^[IVXLC]+\.\s+\w+` | `I. Prologue` | Roman with period — also matches matter, validate context |

### Chinese

| Pattern | Matches | Notes |
|---|---|---|
| `^第[一二三四五六七八九十百零〇\d]+章.*$` | `第一章`, `第十二章 河流` | Standard form |
| `^第[一二三四五六七八九十百零〇\d]+回.*$` | `第一回` | Classical novel form |
| `^第[一二三四五六七八九十百零〇\d]+节.*$` | `第一节` | "Section" — sometimes a sub-chapter |
| `^[一二三四五六七八九十]+、` | `一、` | Numbered list-style chapter |

### Japanese

| Pattern | Matches | Notes |
|---|---|---|
| `^第[一二三四五六七八九十百〇\d]+章.*$` | `第一章` | Same as Chinese |
| `^第[一二三四五六七八九十百〇\d]+話.*$` | `第一話` | "Episode" form, common in light novels |

### Spanish / French / German / Italian

| Pattern | Matches | Notes |
|---|---|---|
| `^Cap[íi]tulo\s+(\d+\|[IVXLC]+)\b.*$` | Spanish `Capítulo 1` | |
| `^Chapitre\s+(\d+\|[IVXLC]+)\b.*$` | French `Chapitre 1` | |
| `^Kapitel\s+\d+\b.*$` | German `Kapitel 1` | |
| `^Capitolo\s+(\d+\|[IVXLC]+)\b.*$` | Italian `Capitolo 1` | |

### Russian

| Pattern | Matches | Notes |
|---|---|---|
| `^Глава\s+(\d+\|[IVXLC]+)\b.*$` | `Глава 1` | |

### Heuristic fallbacks (any language)

When no explicit pattern matches, try these:

- **Centered ALL CAPS short line** preceded by ≥3 blank lines and followed by ≥1 blank line. Often indicates an unnumbered named chapter.
- **Roman numeral or single integer alone on a line**, surrounded by blank lines.
- **`* * *` or `***` or `§` decorations** — these are usually scene breaks *within* a chapter, not chapter boundaries. Don't split on them.

Always show fallback-detected chapters to the user explicitly — fallbacks have higher false-positive rates.

---

## Front matter patterns

| Section | Pattern hints (case-insensitive) |
|---|---|
| Title page | First non-blank page; very short (typically <20 lines); contains the book title verbatim |
| Copyright | `^(Copyright\|©)`, `^All rights reserved`, `\bISBN\b`, `^Library of Congress` |
| Dedication | `^Dedicated to\b`, `^For\s+\w+`, very short (<10 lines), often centered |
| Epigraph | Quote in italics or block-indented before any chapter; often attributed to another author |
| Table of contents | `^(Table of )?Contents$`, followed by chapter list with page numbers |
| Foreword / Preface / Introduction | `^Foreword$`, `^Preface$`, `^Introduction$`, `^Author's Note$`, `^Translator's Note$`, `^A Note (from\|on)\b` |
| Prologue | `^Prologue$` (treat as Chapter 0) |
| List of illustrations | `^(List of )?Illustrations$`, `^Plates$`, `^Figures$` |
| Maps | `^Map(s)?$`, `^List of Maps$` |

Non-English equivalents for the common ones:

| Section | Chinese | Spanish | French | German |
|---|---|---|---|---|
| Foreword | 序 / 前言 / 序言 | Prólogo / Prefacio | Préface / Avant-propos | Vorwort |
| Introduction | 引言 / 导论 | Introducción | Introduction | Einleitung |
| Prologue | 楔子 / 序章 | Prólogo | Prologue | Prolog |
| Dedication | 献给 / 题献 | Dedicatoria | Dédicace | Widmung |

---

## Back matter patterns

| Section | Pattern hints |
|---|---|
| Epilogue | `^Epilogue$`, Chinese `^尾声$` / `^结语$`, Spanish `^Epílogo$`, French `^Épilogue$` |
| Afterword | `^Afterword$`, `^Author's Afterword$` |
| About the author | `^About the Author$`, `^The Author$` |
| About the translator | `^About the Translator$` |
| Acknowledgments | `^Acknowle?dge?ments$`, `^Thanks$`, Chinese `^致谢$` / `^鸣谢$` |
| Notes | `^Notes$`, `^Endnotes$`, `^Translator's Notes$` |
| Glossary | `^Glossary$`, Chinese `^术语表$` |
| Bibliography | `^Bibliography$`, `^References$`, `^Sources$` |
| Index | `^Index$` (skip — almost never worth translating) |
| Appendix | `^Appendix(\s+[A-Z\d\|IVXLC]+)?\b.*$` |

---

## Disambiguating matter from chapters

- A `Chapter N` heading is unambiguous — always treat as chapter.
- A bare named heading like `Foreword` or `Epilogue` is matter, not a chapter.
- A bare integer or Roman numeral with no "Chapter" prefix could be either. Check context: does it appear in a numbered sequence with the rest of the chapters? Then chapter. Standalone before/after the numbered run? Probably matter.
- When uncertain, classify as a chapter and flag in the manifest. Better to over-translate matter than to skip a real chapter.

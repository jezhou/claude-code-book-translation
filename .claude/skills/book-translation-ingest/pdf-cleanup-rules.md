# PDF cleanup rules

Heuristics for stripping noise from text extracted from PDFs. Apply these *after* heading detection but *before* writing per-chapter files. Conservative — when in doubt, keep the line.

## Always strip

- **Standalone page numbers.** A line containing only digits (optionally surrounded by punctuation: `- 42 -`, `[ 42 ]`, `42.`). Only strip if isolated on its own line, not embedded in text.
- **Repeated running headers.** A short line (≤6 words) that appears at the top or bottom of ≥3 different pages with the same text. Common: book title, chapter title, author name. Detect by frequency, not by position alone.
- **Repeated running footers.** Same idea, bottom of page. Often the publisher name or chapter number.
- **Form-feed characters** (`\f`) and other control characters.
- **Hyphenated line breaks at end of physical line.** `tomor-\nrow` → `tomorrow`. Only when the next line starts lowercase and the joined word looks valid in the source language.

## Often strip (but check)

- **Decorative dividers between sections.** Long runs of `─`, `=`, `*`, or `·`. Strip the line, but keep a single `* * *` if it's a meaningful scene break inside a chapter.
- **OCR garbage.** Lines that are >50% non-letter characters and don't form recognizable words. Flag in manifest before deleting.
- **Copyright watermarks** repeated on every page.

## Never strip

- **Footnote markers** (`¹`, `²`, `*`, `[1]`) and the corresponding footnote text. Translator handles these.
- **Italic/bold markers** if you've extracted them as `*text*` or `_text_`. Preserve formatting.
- **Dialogue dashes / em-dashes / quote marks.** Preserve as-is — these carry meaning.
- **Block indents and quoted passages.** Preserve paragraph structure with double-newlines.
- **Anything you're unsure about.** Flag in `MANIFEST.md` and let the user decide on first read.

## Whitespace normalization

- Collapse runs of >2 blank lines to exactly 2 (paragraph break).
- Strip trailing whitespace on every line.
- Convert tabs to single spaces in body text; preserve tabs only if the source uses them structurally (rare in books).
- Normalize all line endings to LF.

## Joining lines across page boundaries

PDFs often split mid-paragraph at page boundaries. Heuristic for joining:

- If the last non-blank line of page N ends without sentence-final punctuation (`.`, `!`, `?`, `。`, `！`, `？`, `”`, `"`) AND the first non-blank line of page N+1 starts lowercase or with a continuation, join them with a space.
- If the last line of page N ends with a hyphen joining a word, join without space (de-hyphenate).
- If both sides have clear sentence-final punctuation, leave the paragraph break.

When in doubt, leave the break — joining wrong is harder to detect than splitting wrong.

## Multi-column layouts

Some PDFs (academic, magazines, parallel translations) use 2+ columns. PDF tools sometimes interleave columns into mush. If extracted text reads non-sequentially:

- Stop. Tell the user and ask for input. Don't try to fix this heuristically — it usually requires re-extracting with column-aware tooling.
- Common signals: sentences that switch topics mid-line; alternating paragraphs that don't connect.

## What to flag in MANIFEST.md

- Pages where >20% of original characters were stripped (potential over-cleaning).
- OCR garbage lines that were preserved (let the user review).
- Mid-sentence splits at page boundaries that *weren't* joined (potential under-joining).
- Suspected multi-column failures.
- Any line where a heading was detected but seemed weak (e.g., matched a fallback pattern, not a primary one).

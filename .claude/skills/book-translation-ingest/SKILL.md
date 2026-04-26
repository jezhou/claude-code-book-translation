---
name: book-translation-ingest
description: Process raw source material (PDF, large text file, .docx, .epub, OCR scans) and split it into per-chapter files in sources/ that the translation loop can consume. Trigger when the user says "ingest this book," "split my source material," "prep my PDF," "process the source," when sources/ contains a single large file or a raw/ subdirectory, or on /book-translation-ingest. Always show the proposed split before writing files.
---

# book-translation-ingest

Bridges the gap between "I have a book file" and "the translation loop can run." Most users arrive with one big PDF or one massive `.txt` — this skill turns that into the per-chapter layout `book-translation-start` expects.

## When to run

- After `book-translation-setup`, before `book-translation-start`.
- When `sources/` contains a single large file, a `raw/` subdirectory, or the user points to source material elsewhere.
- Re-run if the user gets new source material mid-project (e.g., a missing chapter, a corrected scan).

## Inputs handled

| Input | How to read it | Splitting strategy |
|---|---|---|
| One large `.txt` or `.md` | Read directly | Detect chapter headings (see `heading-patterns.md`), split there |
| One `.pdf` | Read with the built-in PDF tool. For PDFs >10 pages, read in page ranges | Apply `pdf-cleanup-rules.md` (strip headers/footers/page numbers), then detect headings |
| `.docx` | Use the `docx` skill if installed; else extract text first | Same as `.txt` |
| `.epub` | Extract text from each `.xhtml` inside (one per chapter, usually) | One file per `.xhtml` is often already the right split |
| OCR scans (multiple PDFs/images) | Read each page individually | One file per page (`page-001.txt`, …); no further splitting — the loop assembles |
| Already-split files | No-op | Confirm with the user, exit |

## Steps

### 1. Inspect

List what's in `sources/`. Look for:

- A `raw/` subdirectory (user dropped raw material here)
- A single large file at `sources/` root
- Multiple files (already split? OCR pages?)
- The user may also point you at a path outside the repo — read from there, write to `sources/`.

If ambiguous (e.g., is this OCR or clean text?), ask one or two questions. Don't ask more.

### 2. Detect structure

Read enough of the source to find:

- **Chapter boundaries.** Use `heading-patterns.md` for the user's source language. For a typical novel/memoir, this is `^Chapter \d+`, `^第.+章`, `^[IVXLC]+\.`, or similar.
- **Front matter.** Title page, copyright, dedication, table of contents, foreword/preface/introduction. These often precede Chapter 1 and have distinctive headings.
- **Back matter.** Epilogue, afterword, about-the-author, acknowledgments, appendices, index. Often follow the last numbered chapter.

Front/back matter detection patterns (case-insensitive, anchored to a line by itself, with optional leading numbering):

| Section | Pattern hints |
|---|---|
| Title page | First page of a PDF; very short text; large isolated title |
| Copyright | "Copyright ©", "All rights reserved", ISBN |
| Dedication | "Dedicated to", "For …" — usually <5 lines |
| Table of contents | "Contents" / "Table of Contents" header followed by chapter list |
| Foreword | "Foreword" / "Preface" / "Introduction" — usually has its own author |
| Epilogue | "Epilogue" / "Afterword" |
| About the author | "About the Author" / "About the Translator" |
| Acknowledgments | "Acknowledgments" / "Acknowledgements" / "Thanks" |
| Appendix | "Appendix A", "Appendix I" |

Skip TOC entirely — it gets regenerated from `OUTPUT.md` headings via `split_book.py`. Skip indices unless the user specifically asks.

### 3. Show the proposed split — DO NOT WRITE YET

This is the critical step. Wrong chapter detection silently corrupts the rest of the project. Present to the user:

```
Proposed split for "{book title}":

  Front matter:
    sources/00-title.txt           (1 page)
    sources/01-foreword.txt        ("A Note from the Editor", 4 pages)

  Chapters:
    sources/02-ch01.txt            "Chapter 1: The Village" (12 pages)
    sources/03-ch02.txt            "Chapter 2: My Father's Hands" (9 pages)
    ...
    sources/27-ch26.txt            "Chapter 26: Going Home" (15 pages)

  Back matter:
    sources/28-epilogue.txt        "Epilogue" (3 pages)
    sources/29-about.txt           "About the Author" (1 page)

  Skipped:
    Table of contents (regenerated from OUTPUT.md)
    Copyright page

Total: 28 chapter-equivalent files. Proceed? (or tell me what to fix)
```

If the user pushes back, adjust and re-show. Common fixes:
- "Combine these — they're really one chapter": merge before writing.
- "Chapter 1 starts at the wrong place": shift the boundary.
- "This isn't a chapter, it's part of the foreword": reclassify.

Only proceed once the user confirms.

### 4. Split

Write files to `sources/`. Conventions:

- **Naming:** zero-padded numeric prefix preserving order, then a descriptive suffix. `NN-ch{N}.txt` for chapters, `NN-{type}.txt` for matter. Numeric prefix orders the loop's traversal; suffix is informational.
- **Encoding:** UTF-8, LF line endings, normalized whitespace (collapse runs of blank lines to max 2; strip trailing whitespace; preserve paragraph breaks).
- **PDF cleanup:** apply `pdf-cleanup-rules.md` — strip running headers/footers, isolated page numbers, OCR artifacts.
- **Don't lose anything.** If unsure whether a fragment is content or a header, keep it and flag it in the manifest.
- **OCR pages:** one file per page, `page-001.txt` through `page-NNN.txt`. No splitting. Add a manifest note that this is OCR — the loop will need to assemble pages into chapter-units.

### 5. Write the manifest

Create `sources/MANIFEST.md` with:

- Source material: file(s) ingested, format, page count.
- Detection method: which heading patterns matched, anything heuristic.
- File listing: one line per output file with detected title and page span.
- Flagged issues: low-confidence OCR pages, mid-sentence page boundaries, untitled chapters, ambiguous matter sections.
- Any user overrides made during step 3.

The Junior Editor reads `MANIFEST.md` on first loop run. It's the project's record of how the source got chunked.

### 6. Stop

Do not start translating. Tell the user:

```
Ingested. {N} files written to sources/. {M} flagged issues — see sources/MANIFEST.md.
Next: ask me to "translate the next chapter" to invoke book-translation-start.
```

## Things to be careful about

- **Don't strip too aggressively.** Better to leave a stray page number in the text than to delete a real line of dialogue. The loop's Translator can handle minor noise; missing content can't be recovered without re-ingesting.
- **Footnotes and endnotes.** Preserve as-is in the chapter file. The Translator handles voice; the Proofreader handles placement.
- **Multi-volume books.** Each volume gets its own ingest pass. Suggest the user separate volumes into `sources/vol1/`, `sources/vol2/` and run ingest per volume.
- **Bilingual source material** (e.g., parallel translation already exists). Ask the user whether the existing translation should be archived as reference (`sources/_reference/`) or ignored entirely.
- **Show, don't act.** Step 3 (proposed split) is non-skippable. Even if you're 99% sure, confirm — the cost of a wrong split compounds across every chapter that follows.

## What this skill does NOT do

- Translate. That's `book-translation-start`.
- Generate personas or the bible. That's `book-translation-setup`.
- Edit `OUTPUT.md`. Source material lives in `sources/`; translated output lives in `OUTPUT.md`. Don't cross-contaminate.

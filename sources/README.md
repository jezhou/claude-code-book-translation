# Source files

Drop your source-language files here. The agent reads from this directory.

## Chunking strategy

Pick whichever fits your material. Document your choice in `CLAUDE.md` so the agent stays consistent.

- **Per-page** (good for OCR'd scans): `page-001.txt`, `page-002.txt`, ...
- **Per-chapter** (good for clean source): `ch01.txt`, `ch02.txt`, ...
- **Per-scene / per-section**: `01-prologue.txt`, `02-childhood-river.txt`, ...

Files may split mid-sentence — that's fine, the agent reads ahead across boundaries.

## File format

Plain UTF-8 text is simplest. The agent can also read PDFs, .docx, and images directly via Claude Code's built-in tools.

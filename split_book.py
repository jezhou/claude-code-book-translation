#!/usr/bin/env python3
"""Split OUTPUT.md into individual chapter files for mdBook.

This is a generic, opinionated splitter:

  # Title          → frontmatter (kept whole)
  ## Section       → its own page (Foreword, Part X, About, ...)
  ### Chapter      → its own page (Chapter N, Epilogue, ...)

Customize the heading regexes and section types in `SECTION_RULES` below if
your book has a different structure.

Also generates `book/src/SUMMARY.md` listing the produced files in order.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass

INPUT = "OUTPUT.md"
OUTDIR = "book/src"


# Each rule is (regex, section_type). The first match wins.
# section_type drives the filename and heading promotion.
SECTION_RULES: list[tuple[re.Pattern, str]] = [
    (re.compile(r"^# (?P<title>.+)$"), "frontmatter"),
    (re.compile(r"^## Foreword\b.*$"), "foreword"),
    (re.compile(r"^## About the Author\b.*$"), "about"),
    (re.compile(r"^## (?P<title>Part [IVXLC]+:.*)$"), "part"),
    (re.compile(r"^### (?P<title>Chapter \d+:.*)$"), "chapter"),
    (re.compile(r"^### (?P<title>Epilogue:.*)$"), "epilogue"),
]


@dataclass
class Section:
    type: str
    title: str
    content: str


def read_input() -> str:
    with open(INPUT, "r", encoding="utf-8") as f:
        return f.read()


def split_into_sections(text: str) -> list[Section]:
    lines = text.split("\n")
    sections: list[Section] = []

    current_type: str | None = None
    current_title: str = ""
    current_lines: list[str] = []

    def flush():
        if current_type is not None:
            content = "\n".join(current_lines).strip()
            sections.append(Section(current_type, current_title, content))

    for line in lines:
        stripped = line.strip()

        # Skip horizontal rules and "End of Part X" decorations.
        if stripped == "---" or re.match(r"^_End of Part", stripped):
            continue

        matched = False
        for pattern, section_type in SECTION_RULES:
            m = pattern.match(line)
            if not m:
                continue
            flush()
            current_type = section_type
            current_title = m.groupdict().get("title", section_type.capitalize())
            current_lines = [line] if section_type == "frontmatter" else []
            matched = True
            break

        if matched:
            continue

        if current_type is not None:
            current_lines.append(line)

    flush()
    return sections


def write_file(filepath: str, content: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.rstrip() + "\n")


def roman_lower(n: int) -> str:
    vals = [
        (1000, "m"), (900, "cm"), (500, "d"), (400, "cd"),
        (100, "c"), (90, "xc"), (50, "l"), (40, "xl"),
        (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i"),
    ]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


def main() -> None:
    text = read_input()
    sections = split_into_sections(text)

    files: list[tuple[str, str]] = []  # (filename, summary_title)
    file_num = 0
    chapter_num = 0
    part_num = 0

    for sec in sections:
        if sec.type == "frontmatter":
            name = f"{file_num:02d}-frontmatter.md"
            write_file(os.path.join(OUTDIR, name), sec.content)
            files.append((name, sec.title))
        elif sec.type == "foreword":
            name = f"{file_num:02d}-foreword.md"
            write_file(os.path.join(OUTDIR, name), f"# Foreword\n\n{sec.content}")
            files.append((name, "Foreword"))
        elif sec.type == "part":
            part_num += 1
            name = f"{file_num:02d}-part-{roman_lower(part_num)}.md"
            write_file(os.path.join(OUTDIR, name), f"# {sec.title}\n")
            files.append((name, sec.title))
        elif sec.type == "chapter":
            chapter_num += 1
            name = f"{file_num:02d}-ch{chapter_num:02d}.md"
            write_file(os.path.join(OUTDIR, name), f"# {sec.title}\n\n{sec.content}")
            files.append((name, sec.title))
        elif sec.type == "epilogue":
            name = f"{file_num:02d}-epilogue.md"
            write_file(os.path.join(OUTDIR, name), f"# {sec.title}\n\n{sec.content}")
            files.append((name, sec.title))
        elif sec.type == "about":
            name = f"{file_num:02d}-about.md"
            write_file(os.path.join(OUTDIR, name), f"# About the Author\n\n{sec.content}")
            files.append((name, "About the Author"))
        else:
            name = f"{file_num:02d}-{sec.type}.md"
            write_file(os.path.join(OUTDIR, name), sec.content)
            files.append((name, sec.title or sec.type))

        file_num += 1

    summary_lines = ["# Summary", ""]
    for name, title in files:
        summary_lines.append(f"- [{title}]({name})")
    write_file(os.path.join(OUTDIR, "SUMMARY.md"), "\n".join(summary_lines))

    print(f"Generated {file_num} files + SUMMARY.md in {OUTDIR}/")


if __name__ == "__main__":
    main()

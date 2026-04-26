# Source Manifest

Record of how the source material was ingested and split into per-chapter files.

## Source material

- **File ingested:** `sources/pg25142.txt`
- **Source URL:** https://www.gutenberg.org/cache/epub/25142/pg25142.txt
- **Format:** UTF-8 plain text, single file, 29,626 lines
- **Original work:** 王陽明全集 (*The Complete Works of Wang Yangming*) by 王守仁 (Wang Shouren / Wang Yangming, 1472–1529)
- **Source edition:** Project Gutenberg eBook #25142, produced by Nai-Wen Cai, released April 23, 2008
- **License:** Public domain in the U.S. (Project Gutenberg License)

## Detection method

The text is structured in four 卷 (volumes), each containing a varying number of 錄 (sub-volumes). Sub-volume headers are anchored to a line by themselves and follow a consistent pattern:

- Volume header: `^卷[一二三四]　[knownVolName]` — e.g., `卷一　知行錄`
- Sub-volume header: `^[知行靜心悟真順生]+錄之[一二三四五六七八九十]+　[title]` — e.g., `知行錄之一　傳習錄上`

Boundaries detected by `grep` against these patterns and then verified by inspection. Each 錄 was treated as one chapter-equivalent translation unit since each is itself a substantial work and corresponds to a coherent textual division in the traditional edition.

## Skipped sections

| Lines | Content | Reason |
|---|---|---|
| 1–29 | Project Gutenberg header | License boilerplate, not source content |
| 30–40 | Title block (王陽明全集 / 〔明〕王守仁 / 全四卷) | Already captured in `book/book.toml` |
| 41–68 | Volume + sub-volume table of contents | Regenerated automatically from `OUTPUT.md` headings via `split_book.py` |
| 29276–29626 | Project Gutenberg footer + license | License boilerplate, not source content |

## File listing

42 chapter-equivalent files. Numbered sequentially in traditional order across the four volumes. Naming: `NN-juan{V}-{vol-seq}-{romanized-title}.txt`.

### Volume I — 卷一 知行錄 (Records of Knowledge and Action)

| File | Title | Source lines | Output lines |
|---|---|---|---|
| `01-juan1-01-chuanxi-shang.txt` | 知行錄之一　傳習錄上 | 70–752 | 683 |
| `02-juan1-02-chuanxi-zhong.txt` | 知行錄之二　傳習錄中 | 753–1614 | 862 |
| `03-juan1-03-chuanxi-xia.txt` | 知行錄之三　傳習錄下 | 1615–2539 | 925 |
| `04-juan1-04-gongyi-1.txt` | 知行錄之四　公移一 | 2540–3344 | 805 |
| `05-juan1-05-gongyi-2.txt` | 知行錄之五　公移二 | 3345–4203 | 859 |
| `06-juan1-06-gongyi-3.txt` | 知行錄之六　公移三 | 4204–4850 | 647 |
| `07-juan1-07-sanzheng-yigao.txt` | 知行錄之七　三征公移逸稿 | 4851–5862 | 1012 |
| `08-juan1-08-zhengfan-gongyi.txt` | 知行錄之八　征藩公移 | 5863–6645 | 783 |

### Volume II — 卷二 靜心錄 (Records of the Quiet Mind)

| File | Title | Source lines | Output lines |
|---|---|---|---|
| `09-juan2-01-wenlu-1.txt` | 靜心錄之一　文錄一 | 6646–7291 | 646 |
| `10-juan2-02-wenlu-2.txt` | 靜心錄之二　文錄二 | 7292–7713 | 422 |
| `11-juan2-03-wenlu-3.txt` | 靜心錄之三　文錄三 | 7714–8184 | 471 |
| `12-juan2-04-waiji-3.txt` | 靜心錄之四　外集三 | 8185–8880 | 696 |
| `13-juan2-05-xubian-2a.txt` | 靜心錄之五　續編二 | 8881–9232 | 352 |
| `14-juan2-06-xubian-2b.txt` | 靜心錄之六　續編二 | 9233–9890 | 658 |
| `15-juan2-07-waiji-1.txt` | 靜心錄之七　外集一 | 9891–10921 | 1031 |
| `16-juan2-08-waiji-2.txt` | 靜心錄之八　外集二 | 10922–12194 | 1273 |
| `17-juan2-09-gaoming-jiwen.txt` | 靜心錄之九　誥命﹒祭文增補﹒傳記﹒增補 | 12195–13039 | 845 |
| `18-juan2-10-xushuo-xuba.txt` | 靜心錄之十　序說﹒序跋增補 | 13040–14609 | 1570 |

### Volume III — 卷三 悟真錄 (Records of Awakening to Truth)

| File | Title | Source lines | Output lines |
|---|---|---|---|
| `19-juan3-01-wenlu-4.txt` | 悟真錄之一　文錄四 | 14610–15414 | 805 |
| `20-juan3-02-wenlu-5.txt` | 悟真錄之二　文錄五 | 15415–15717 | 303 |
| `21-juan3-03-waiji-4.txt` | 悟真錄之三　外集四 | 15718–16584 | 867 |
| `22-juan3-04-waiji-5.txt` | 悟真錄之四　外集五 | 16585–16951 | 367 |
| `23-juan3-05-waiji-6.txt` | 悟真錄之五　外集六 | 16952–17354 | 403 |
| `24-juan3-06-waiji-7.txt` | 悟真錄之六　外集七 | 17355–18103 | 749 |
| `25-juan3-07-xubian-1.txt` | 悟真錄之七　續編一 | 18104–18375 | 272 |
| `26-juan3-08-xubian-3.txt` | 悟真錄之八　續編三 | 18376–18757 | 382 |
| `27-juan3-09-xubian-4.txt` | 悟真錄之九　續編四 | 18758–19207 | 450 |
| `28-juan3-10-bulu.txt` | 悟真錄之十　補　錄 | 19208–19850 | 643 |
| `29-juan3-11-shideji.txt` | 悟真錄之十一　世德紀 | 19851–21226 | 1376 |
| `30-juan3-12-shideji-fulu.txt` | 悟真錄之十二　世德紀　附錄 | 21227–22312 | 1086 |

### Volume IV — 卷四 順生錄 (Records of Following Nature)

| File | Title | Source lines | Output lines |
|---|---|---|---|
| `31-juan4-01-bielu-1.txt` | 順生錄之一　別錄一 | 22313–23031 | 719 |
| `32-juan4-02-bielu-2.txt` | 順生錄之二　別錄二 | 23032–23520 | 489 |
| `33-juan4-03-bielu-3-zoushu-3.txt` | 順生錄之三　別錄三奏疏三 | 23521–24192 | 672 |
| `34-juan4-04-bielu-4-zoushu-4.txt` | 順生錄之四　別錄四奏疏四 | 24193–24832 | 640 |
| `35-juan4-05-bielu-5-zoushu-5.txt` | 順生錄之五　別錄五奏疏五 | 24833–25439 | 607 |
| `36-juan4-06-bielu-6-zoushu-6.txt` | 順生錄之六　別錄六奏疏六 | 25440–25986 | 547 |
| `37-juan4-07-bielu-7-zoushu-7.txt` | 順生錄之七　別錄七奏疏七 | 25987–26551 | 565 |
| `38-juan4-08-nianpu-1.txt` | 順生錄之八　年譜一 | 26552–27188 | 637 |
| `39-juan4-09-nianpu-2.txt` | 順生錄之九　年譜二 | 27189–27628 | 440 |
| `40-juan4-10-nianpu-3.txt` | 順生錄之十　年譜三 | 27629–28387 | 759 |
| `41-juan4-11-nianpu-fulu-1.txt` | 順生錄之十一　年譜附錄一 | 28388–28861 | 474 |
| `42-juan4-12-nianpu-fulu-2.txt` | 順生錄之十二　年譜附錄二 | 28862–29275 | 414 |

## Flagged issues

- **Two sub-volumes share the title 續編二** (`13-juan2-05-xubian-2a.txt` and `14-juan2-06-xubian-2b.txt`, originally 靜心錄之五 and 靜心錄之六). This appears to be an artifact of the source edition — both share the literal title in the TOC. Filenames disambiguate with `-2a` / `-2b`. Translator should verify whether this is an editorial duplication or two distinct sections that happen to share a title.
- **奏疏 doubled labels in Volume IV** (sources 33–37): titles appear as `別錄N奏疏N` (e.g., `別錄三奏疏三`) — meaning these are simultaneously labeled as 別錄 part of the four-volume scheme AND as 奏疏 (memorials to the throne) in their own right. Preserved both labels in the filename.
- **Mid-text reference at line 14531** (`(卷二十八），連同陽明幼子王正億編錄的《陽明先生家乘》三卷`) is body content inside `18-juan2-10-xushuo-xuba.txt`, not a structural break — verified before splitting.
- **No OCR artifacts** — Project Gutenberg edition is clean digital text, so no header/footer stripping or OCR cleanup was needed.

## Cleanup applied

- Stripped trailing whitespace per line.
- Collapsed runs of >2 blank lines to 2.
- Preserved final newline.
- UTF-8, LF line endings throughout.

## User overrides during ingest

- Translation order: keep traditional order (no reshuffle to put 傳習錄 first).
- Existing `pg25142.txt` retained as canonical raw, not deleted.
- Filenames use Pinyin romanization rather than Chinese characters.

## Next step

Run `book-translation-start` (say "translate the next chapter") to begin the multi-agent translation loop. Files are processed in numeric-prefix order, so the first chapter to translate will be `01-juan1-01-chuanxi-shang.txt` (傳習錄上, the most famous and accessible part — the *Chuanxi lu* / *Instructions for Practical Living*).

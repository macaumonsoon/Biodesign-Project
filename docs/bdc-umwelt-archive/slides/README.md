# Slide decks — Extinction Archive (Mammoth)

Two independent Marp sources:

| Language | Marp source | Exported PDF | Exported PPTX |
|----------|-------------|--------------|----------------|
| English | `BDC_Extinction_Archive_Mammoth.md` | `export/BDC_Deck_EN.pdf` | `export/BDC_Deck_EN.pptx` |
| 中文 | `BDC_Extinction_Archive_Mammoth_zh.md` | `export/BDC_Deck_ZH.pdf` | `export/BDC_Deck_ZH.pptx` |

## Build (PDF + PPTX)

From the **repository root** (`Biodesign_Project_2/`):

```bash
cd slides
mkdir -p export

# Use --no-stdin so Marp does not hang in automated shells / CI.

npx --yes @marp-team/marp-cli --no-stdin BDC_Extinction_Archive_Mammoth.md --pdf --allow-local-files -o export/BDC_Deck_EN.pdf
npx --yes @marp-team/marp-cli --no-stdin BDC_Extinction_Archive_Mammoth.md --pptx --allow-local-files -o export/BDC_Deck_EN.pptx

npx --yes @marp-team/marp-cli --no-stdin BDC_Extinction_Archive_Mammoth_zh.md --pdf --allow-local-files -o export/BDC_Deck_ZH.pdf
npx --yes @marp-team/marp-cli --no-stdin BDC_Extinction_Archive_Mammoth_zh.md --pptx --allow-local-files -o export/BDC_Deck_ZH.pptx
```

**Notes**

- Marp needs a **Chromium-based** browser for PDF/PPTX. If conversion fails, install Chrome or set `CHROME_PATH` / `MARP_CHROME_PATH` per [Marp CLI](https://github.com/marp-team/marp-cli).
- **`--pptx-editable`** requires **LibreOffice** (`soffice`). Without it, use plain `--pptx` (default above) — slides are still openable in Microsoft PowerPoint / Keynote.

One-liner alternative (PDF only, from `slides/`):

```bash
npx --yes @marp-team/marp-cli *.md -I . --pdf -o export/
```

…then rename outputs if needed (CLI may derive names from input filenames).

## Preview links (local)

- Open **`slides/preview.html`** in your browser (double-click or Cursor → Open in Browser).  
  This page links to `export/*.pdf` and `export/*.pptx` **after** you run the build.

**There is no built-in public URL** for files on disk. Paths for manual paste:

- `file://` + full path to `slides/preview.html` (works on your machine only).  
  Example pattern: `file:///Users/you/Desktop/Cursor/Biodesign_Project_2/slides/preview.html`

## Cursor-specific

1. **Marp preview:** Extension “Marp for VS Code” → open `BDC_Extinction_Archive_Mammoth.md` → use the Marp icon / preview.
2. **Live Preview:** Optional extension to preview `preview.html` (static HTML + relative links).

## Citations note

Core papers (Wooller et al. 2021 *Science*; Lynch et al. 2015 *Cell Reports*; Nogués-Bravo et al. 2008 *PLoS Biology*) + software (+1) are embedded in both decks. Swap years for R if you standardize on a different R release for your Methods slide.

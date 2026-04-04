# Extinction Archive — Slides

Theme: **archival biodigital** — dark earth background, ochre accent (`#c45c2a`), signal teal (`#5cb89a`), museum-style top rule.

**Slide geometry:** PDFs use **standard widescreen 16:9** — same as PowerPoint / Keynote default (**13.333″ × 7.5″**, i.e. **338.67 mm × 190.5 mm**), so you can match layouts when rebuilding in PPT.

## PDF exports (official deck)

| File | Language |
|------|----------|
| [`export/Extinction_Archive_EN.pdf`](./export/Extinction_Archive_EN.pdf) | English |
| [`export/Extinction_Archive_ZH.pdf`](./export/Extinction_Archive_ZH.pdf) | 中文 |

**Regenerate PDFs** (requires macOS `Arial Unicode.ttf` for CJK):

```bash
pip3 install fpdf2
python3 scripts/build_extinction_archive_slides.py
```

**Marp source** (optional; needs Chromium for `--pdf`):

- [`Extinction_Archive_EN.md`](./Extinction_Archive_EN.md)
- [`Extinction_Archive_ZH.md`](./Extinction_Archive_ZH.md)
- Theme: [`themes/extinction-archive.css`](./themes/extinction-archive.css)

## Browser preview (HTML)

Open locally (full paths):

- **English:** `preview/Extinction_Archive_preview_EN.html`
- **中文:** `preview/Extinction_Archive_preview_ZH.html`

macOS Terminal:

```bash
open "/Users/dad71/Desktop/Cursor/Biodesign_Project_2/slides/preview/Extinction_Archive_preview_EN.html"
open "/Users/dad71/Desktop/Cursor/Biodesign_Project_2/slides/preview/Extinction_Archive_preview_ZH.html"
```

Or use **Live Server** / “Open with Browser” in your editor.

### Download links from preview

Each HTML page has a top-right link to download the matching PDF from `../export/`.

## Push to GitHub (optional)

After you commit `slides/` (for example under `docs/bdc-umwelt-archive/slides/`), use **Raw** links:

- `https://github.com/macaumonsoon/Biodesign-Project/raw/main/docs/bdc-umwelt-archive/slides/export/Extinction_Archive_EN.pdf`
- `https://github.com/macaumonsoon/Biodesign-Project/raw/main/docs/bdc-umwelt-archive/slides/export/Extinction_Archive_ZH.pdf`

If you keep slides at repo root instead, change the path segment accordingly. Opening a `raw` PDF link in a browser **downloads or previews** the file. HTML previews work best **locally** or via **GitHub Pages** (raw HTML is often served as plain text).

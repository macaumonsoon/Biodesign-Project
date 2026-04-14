#!/usr/bin/env python3
"""
Extract per-page text from a PDF.

Engines:
  - pypdf (pure Python): pip install pypdf
  - pdftotext (Poppler): brew install poppler  →  often better layout for some PDFs

Usage:
  python3 scripts/extract_pdf_text.py "/path/to/file.pdf"
  python3 scripts/extract_pdf_text.py file.pdf --out-dir ./pdf_text_pages
  python3 scripts/extract_pdf_text.py file.pdf --engine pdftotext
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def extract_pypdf(pdf_path: Path) -> list[str]:
    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    pages: list[str] = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages.append(text)
    return pages


def extract_pdftotext(pdf_path: Path) -> list[str]:
    bin_name = "pdftotext"
    if not shutil.which(bin_name):
        raise RuntimeError(
            "pdftotext not found. Install Poppler, e.g. `brew install poppler` (macOS)."
        )
    # Page count via pdfinfo if available, else fall back to pypdf count only
    n_pages = None
    pdfinfo = shutil.which("pdfinfo")
    if pdfinfo:
        out = subprocess.run(
            [pdfinfo, str(pdf_path)],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        for line in out.splitlines():
            if line.startswith("Pages:"):
                n_pages = int(line.split(":", 1)[1].strip())
                break
    if n_pages is None:
        from pypdf import PdfReader

        n_pages = len(PdfReader(str(pdf_path)).pages)

    texts: list[str] = []
    for p in range(1, n_pages + 1):
        proc = subprocess.run(
            [bin_name, "-layout", "-f", str(p), "-l", str(p), str(pdf_path), "-"],
            capture_output=True,
            text=True,
            check=True,
        )
        texts.append(proc.stdout or "")
    return texts


def main() -> int:
    ap = argparse.ArgumentParser(description="Extract per-page text from a PDF.")
    ap.add_argument("pdf", type=Path, help="Path to PDF")
    ap.add_argument(
        "--engine",
        choices=("auto", "pypdf", "pdftotext"),
        default="auto",
        help="auto: use pdftotext if on PATH, else pypdf",
    )
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Write page-001.txt, page-002.txt, ... here",
    )
    args = ap.parse_args()
    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.is_file():
        print(f"Not a file: {pdf_path}", file=sys.stderr)
        return 1

    engine = args.engine
    if engine == "auto":
        engine = "pdftotext" if shutil.which("pdftotext") else "pypdf"

    try:
        if engine == "pdftotext":
            pages = extract_pdftotext(pdf_path)
        else:
            pages = extract_pypdf(pdf_path)
    except Exception as e:
        print(e, file=sys.stderr)
        return 1

    if args.out_dir:
        out_dir = args.out_dir.expanduser().resolve()
        out_dir.mkdir(parents=True, exist_ok=True)
        for i, text in enumerate(pages, start=1):
            (out_dir / f"page-{i:03d}.txt").write_text(text, encoding="utf-8")
        print(f"Wrote {len(pages)} files to {out_dir}")
    else:
        for i, text in enumerate(pages, start=1):
            print(f"===== PAGE {i} =====")
            print(text.rstrip())
            print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Generate animals CSV, PostgreSQL INSERTs, and archive.json from the team's extinct-species list.

Usage:
  python3 scripts/extinction_archive_db/generate_archive_exports.py

Optional: set SOURCE_CSV to your unified list path (defaults to Bio-design-resources path).
Outputs (under repo data/extinction_archive/):
  - animals_full.csv
  - archive_import.sql
  - archive.json
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "data" / "extinction_archive"
DEFAULT_SOURCE = REPO_ROOT / "data/extinction_archive/source_extinct_animals.csv"
LEGACY_SOURCE = Path(
    "/Users/dad71/Desktop/Cursor/Bio-design-resources/AI Project 2-Cursor/Database/"
    "extinct_animals_database统一高优先级数据库（87种）.csv"
)

# Extra species not in source CSV (from team sample / curriculum)
EXTRA_ROWS: list[dict[str, str]] = [
    {
        "类别": "Mammals",
        "中文/英文俗名": "斑驴 / Quagga",
        "学名": "Equus quagga quagga",
        "灭绝时期/年份": "1883",
        "主要分布": "South Africa",
        "感官重建潜力评分": "7",
        "音乐层叠潜力评分": "6",
        "数据可用性": "Medium",
        "3D模型参考链接": "Sketchfab Quagga",
        "灭绝原因分析": "狩猎取皮+牧场竞争",
        "备注（paleo-data / 项目相关性）": "商业毛皮狩猎案例",
    },
    {
        "类别": "Mammals",
        "中文/英文俗名": "比利牛斯山羊 / Pyrenean Ibex",
        "学名": "Capra pyrenaica pyrenaica",
        "灭绝时期/年份": "2000",
        "主要分布": "Pyrenees, Spain",
        "感官重建潜力评分": "8",
        "音乐层叠潜力评分": "7",
        "数据可用性": "High",
        "3D模型参考链接": "Museum specimens",
        "灭绝原因分析": "狩猎+栖息地丧失+疾病",
        "备注（paleo-data / 项目相关性）": "克隆尝试案例，现代灭绝",
    },
]


def _norm(s: str) -> str:
    return (s or "").strip()


def split_names(cell: str) -> tuple[str, str]:
    """Return (zh_hint, en_primary) from '中文 / English' or 'English'."""
    cell = _norm(cell)
    if " / " in cell:
        a, b = cell.split(" / ", 1)
        return _norm(a), _norm(b)
    if "/" in cell:
        a, b = cell.split("/", 1)
        return _norm(a), _norm(b)
    return "", cell


def parse_extinction_year(raw: str) -> int | None:
    r = _norm(raw)
    if not r:
        return None
    r_nc = r.replace(",", "")
    # “×年前” before generic digit match so "~4,000年前" does not become +4000 CE
    if "年前" in r:
        m2 = re.search(r"([\d,]+)", r_nc)
        if m2:
            return -int(m2.group(1).replace(",", ""))
    m = re.search(r"(-?\d{3,5})", r_nc)
    if m:
        try:
            return int(m.group(1))
        except ValueError:
            pass
    if "17世纪" in r or "17 世纪" in r:
        return 1681
    if "18世纪" in r:
        return 1750
    if "1800s" in r or "19 世纪" in r:
        return 1850
    if "19-20世纪" in r:
        return 1920
    if "19世纪晚期" in r:
        return 1890
    if "20世纪晚期" in r:
        return 1990
    if "~1920s" in r or "1920s" in r:
        return 1925
    if "~1930s" in r or "1930s" in r:
        return 1935
    if "~1950s" in r or "1950s" in r:
        return 1950
    if "1940s" in r:
        return 1945
    if "~1878" in r:
        return 1878
    if "~1870" in r:
        return 1870
    if "~2023" in r:
        return 2023
    if "~2010" in r:
        return 2010
    if "~1930" in r and "确认" not in r:
        return 1930
    if "~1914" in r:
        return 1914
    return None


def wikipedia_url(scientific_name: str) -> str:
    name = (
        scientific_name.replace(" spp.", "")
        .replace(" spp", "")
        .strip()
    )
    parts = name.split()
    if len(parts) >= 2:
        t = f"{parts[0]}_{parts[1]}"
    elif len(parts) == 1:
        t = parts[0]
    else:
        t = "Extinction"
    return f"https://en.wikipedia.org/wiki/{t}"


def pharm_block(
    scientific_name: str,
    category: str,
    causes: str,
    notes: str,
) -> tuple[bool, str]:
    """Heuristic pharm / bioprospecting framing for the course narrative."""
    blob = f"{causes} {notes} {scientific_name}".lower()
    rhino = "rhino" in blob or "犀" in blob or "bicornis" in blob
    mammoth = "mammuthus" in scientific_name.lower()
    thyla = "thylacinus" in scientific_name.lower()
    if rhino:
        return (
            True,
            "Illegal horn trade driven partly by traditional-medicine demand; extinction "
            "illustrates regulatory and enforcement gaps for species exploited for "
            "unverified medicinal claims. Conservation pharmacology angle: protect "
            "remaining rhino taxa and support evidence-based substitutes.",
        )
    if mammoth:
        return (
            False,
            "No historic pharmaceutical use. De-extinction and aDNA research may yield "
            "insights into cold-adaptation proteins and comparative immunogenomics; "
            "any medical application remains speculative and ethically contested.",
        )
    if thyla:
        return (
            False,
            "No direct pharmaceutical use. Loss of genetic diversity limits future "
            "biobank and comparative physiology research; de-extinction debate touches "
            "biotech governance rather than proven drug leads.",
        )
    if "壶菌" in blob or "chytrid" in blob or ("真菌" in blob and "amphib" in category.lower()):
        return (
            False,
            "Amphibian pathogens are central to One Health and emerging infectious "
            "disease research; extinction underscores links between ecosystem health and "
            "biomedical surveillance (not direct drug sourcing from this species).",
        )
    return (
        False,
        "No direct pharmaceutical use documented. Included to show how anthropogenic "
        "drivers (hunting, habitat loss, climate, invasive species) erase potential "
        "future natural-product and comparative biology options.",
    )


def human_intervention(causes: str) -> str:
    c = _norm(causes)
    if not c:
        return "Human-related drivers not yet summarized."
    mapping = {
        "狩猎": "hunting",
        "人类": "human activity",
        "气候": "climate change",
        "栖息地": "habitat loss",
        "入侵": "invasive species",
        "偷猎": "poaching",
        "污染": "pollution",
        "筑坝": "damming",
        "捕捞": "overfishing",
        "过度": "overexploitation",
    }
    extra = "; ".join(f"{k}→{v}" for k, v in mapping.items() if k in c)
    return f"{c}. ({extra})" if extra else c


def short_description(
    category: str,
    en_name: str,
    scientific_name: str,
    distribution: str,
    notes: str,
) -> str:
    bits = [
        f"[{category}] {en_name} ({scientific_name}).",
        f"Historic range: {distribution}." if distribution else "",
        _norm(notes),
    ]
    return " ".join(b for b in bits if b)


def sketchfab_query_url(scientific_name: str) -> str:
    q = scientific_name.replace(" ", "+")
    return f"https://sketchfab.com/search?q={q}"


def load_rows(source: Path) -> list[dict[str, str]]:
    if not source.exists():
        print(f"Warning: source CSV not found: {source}", file=sys.stderr)
        return []
    with source.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return [dict(r) for r in reader]


def build_animals(source: Path | None = None) -> list[dict[str, Any]]:
    src = source or DEFAULT_SOURCE
    rows = load_rows(src) + EXTRA_ROWS
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for r in rows:
        sn = _norm(r.get("学名", ""))
        if not sn or sn in seen:
            continue
        seen.add(sn)
        zh, en = split_names(r.get("中文/英文俗名", ""))
        common = en or zh or sn
        cat = _norm(r.get("类别", ""))
        dist = _norm(r.get("主要分布", ""))
        causes = _norm(r.get("灭绝原因分析", ""))
        notes = _norm(r.get("备注（paleo-data / 项目相关性）", ""))
        year_raw = _norm(r.get("灭绝时期/年份", ""))
        year = parse_extinction_year(year_raw)
        pharm_rel, pharm_nt = pharm_block(sn, cat, causes, notes)
        desc = short_description(cat, common, sn, dist, notes)
        model = _norm(r.get("3D模型参考链接", ""))

        sensory = r.get("感官重建潜力评分", "")
        music = r.get("音乐层叠潜力评分", "")
        davail = _norm(r.get("数据可用性", "")).lower() or "unknown"

        out.append(
            {
                "scientific_name": sn,
                "common_name": common,
                "common_name_zh": zh,
                "category": cat,
                "extinction_year": year,
                "extinction_period_raw": year_raw,
                "extinction_location": dist,
                "description": desc,
                "image_url": "",
                "pharm_related": pharm_rel,
                "pharm_notes": pharm_nt,
                "human_intervention_summary": human_intervention(causes),
                "main_causes": causes,
                "wikipedia_url": wikipedia_url(sn),
                "sensory_reconstruction_score": int(sensory) if str(sensory).isdigit() else None,
                "music_layering_score": int(music) if str(music).isdigit() else None,
                "data_availability": davail,
                "model_3d_reference": model,
                "internal_notes": notes,
            }
        )
    return out


def sql_escape(s: str | None) -> str:
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"


def animals_to_csv(animals: list[dict[str, Any]], path: Path) -> None:
    columns = [
        "scientific_name",
        "common_name",
        "common_name_zh",
        "category",
        "extinction_year",
        "extinction_period_raw",
        "extinction_location",
        "description",
        "image_url",
        "pharm_related",
        "pharm_notes",
        "human_intervention_summary",
        "main_causes",
        "wikipedia_url",
        "sensory_reconstruction_score",
        "music_layering_score",
        "data_availability",
        "model_3d_reference",
        "internal_notes",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        w.writeheader()
        for a in animals:
            row = {k: a.get(k, "") for k in columns}
            row["pharm_related"] = str(row["pharm_related"]).lower()
            w.writerow(row)


def animals_to_sql(animals: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        "-- Extinction Archive: schema + data (PostgreSQL)",
        "-- Table name `references` is reserved; using `literature_references`.",
        "",
        "DROP TABLE IF EXISTS archival_media CASCADE;",
        "DROP TABLE IF EXISTS literature_references CASCADE;",
        "DROP TABLE IF EXISTS animals CASCADE;",
        "",
        """CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    scientific_name VARCHAR(255) UNIQUE NOT NULL,
    common_name VARCHAR(255) NOT NULL,
    common_name_zh VARCHAR(255),
    category VARCHAR(128),
    extinction_year INTEGER,
    extinction_period_raw TEXT,
    extinction_location TEXT,
    description TEXT,
    image_url TEXT,
    pharm_related BOOLEAN DEFAULT FALSE,
    pharm_notes TEXT,
    human_intervention_summary TEXT,
    main_causes TEXT,
    wikipedia_url TEXT,
    sensory_reconstruction_score SMALLINT,
    music_layering_score SMALLINT,
    data_availability VARCHAR(32),
    model_3d_reference TEXT,
    internal_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);""",
        "",
        """CREATE TABLE archival_media (
    id SERIAL PRIMARY KEY,
    animal_id INTEGER NOT NULL REFERENCES animals(id) ON DELETE CASCADE,
    media_type VARCHAR(50) NOT NULL CHECK (media_type IN ('image', 'video', 'document', 'article')),
    title TEXT,
    url TEXT NOT NULL,
    caption TEXT,
    source TEXT
);""",
        "",
        """CREATE TABLE literature_references (
    id SERIAL PRIMARY KEY,
    animal_id INTEGER NOT NULL REFERENCES animals(id) ON DELETE CASCADE,
    citation_text TEXT,
    url TEXT
);""",
        "",
        "CREATE INDEX idx_animals_pharm_related ON animals(pharm_related);",
        "CREATE INDEX idx_animals_extinction_year ON animals(extinction_year);",
        "CREATE INDEX idx_archival_media_animal ON archival_media(animal_id);",
        "CREATE INDEX idx_literature_animal ON literature_references(animal_id);",
        "",
    ]

    vals = []
    for a in animals:
        vals.append(
            "("
            + ", ".join(
                [
                    sql_escape(a["scientific_name"]),
                    sql_escape(a["common_name"]),
                    sql_escape(a.get("common_name_zh") or ""),
                    sql_escape(a.get("category") or ""),
                    str(a["extinction_year"]) if a["extinction_year"] is not None else "NULL",
                    sql_escape(a.get("extinction_period_raw") or ""),
                    sql_escape(a.get("extinction_location") or ""),
                    sql_escape(a.get("description") or ""),
                    sql_escape(a.get("image_url") or ""),
                    "TRUE" if a["pharm_related"] else "FALSE",
                    sql_escape(a.get("pharm_notes") or ""),
                    sql_escape(a.get("human_intervention_summary") or ""),
                    sql_escape(a.get("main_causes") or ""),
                    sql_escape(a.get("wikipedia_url") or ""),
                    str(a["sensory_reconstruction_score"])
                    if a.get("sensory_reconstruction_score") is not None
                    else "NULL",
                    str(a["music_layering_score"])
                    if a.get("music_layering_score") is not None
                    else "NULL",
                    sql_escape(a.get("data_availability") or ""),
                    sql_escape(a.get("model_3d_reference") or ""),
                    sql_escape(a.get("internal_notes") or ""),
                ]
            )
            + ")"
        )

    lines.append(
        "INSERT INTO animals (scientific_name, common_name, common_name_zh, category, "
        "extinction_year, extinction_period_raw, extinction_location, description, image_url, "
        "pharm_related, pharm_notes, human_intervention_summary, main_causes, wikipedia_url, "
        "sensory_reconstruction_score, music_layering_score, data_availability, "
        "model_3d_reference, internal_notes) VALUES\n"
        + ",\n".join(vals)
        + ";"
    )

    # Media: Wikipedia + Sketchfab search per animal
    media_rows: list[str] = []
    ref_rows: list[str] = []
    for i, a in enumerate(animals, start=1):
        if a.get("wikipedia_url"):
            media_rows.append(
                f"({i}, 'article', 'Wikipedia overview', {sql_escape(a['wikipedia_url'])}, "
                f"'Species article (verify media rights separately)', 'Wikipedia')"
            )
        sf = sketchfab_query_url(a["scientific_name"])
        media_rows.append(
            f"({i}, 'document', '3D model search (Sketchfab)', {sql_escape(sf)}, "
            f"'Team note / model discovery; check license before embed', 'Sketchfab search')"
        )
        ref_rows.append(
            f"({i}, {sql_escape('Wikipedia — ' + a['scientific_name'])}, {sql_escape(a['wikipedia_url'])})"
        )

    lines.append("")
    lines.append(
        "INSERT INTO archival_media (animal_id, media_type, title, url, caption, source) VALUES\n"
        + ",\n".join(media_rows)
        + ";"
    )
    lines.append("")
    lines.append(
        "INSERT INTO literature_references (animal_id, citation_text, url) VALUES\n"
        + ",\n".join(ref_rows)
        + ";"
    )
    lines.append("")
    lines.append(
        "SELECT setval(pg_get_serial_sequence('animals', 'id'), "
        "(SELECT COALESCE(MAX(id), 1) FROM animals));"
    )

    path.write_text("\n".join(lines), encoding="utf-8")


def animals_to_json(animals: list[dict[str, Any]], path: Path) -> None:
    payload = {
        "meta": {
            "project": "Extinction Archive / Umwelt Archive",
            "schema_version": 1,
            "animal_count": len(animals),
            "notes": "image_url left blank — attach Commons/Wikimedia URLs after manual QC. "
            "PostgreSQL table references renamed to literature_references.",
        },
        "animals": [],
    }
    for idx, a in enumerate(animals, start=1):
        entry = {
            "id": idx,
            **a,
            "archival_media": [
                {
                    "media_type": "article",
                    "title": "Wikipedia overview",
                    "url": a["wikipedia_url"],
                    "caption": "Species article",
                    "source": "Wikipedia",
                },
                {
                    "media_type": "document",
                    "title": "3D model search (Sketchfab)",
                    "url": sketchfab_query_url(a["scientific_name"]),
                    "caption": "Discovery link; verify license before production embed",
                    "source": "Sketchfab search",
                },
            ],
            "references": [
                {
                    "citation_text": f"Wikipedia — {a['scientific_name']}",
                    "url": a["wikipedia_url"],
                }
            ],
        }
        payload["animals"].append(entry)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    if len(sys.argv) > 1:
        source = Path(sys.argv[1])
    else:
        source = DEFAULT_SOURCE if DEFAULT_SOURCE.exists() else LEGACY_SOURCE
    animals = build_animals(source)
    if not animals:
        print("No animals built; check SOURCE_CSV path.", file=sys.stderr)
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    animals_to_csv(animals, OUT_DIR / "animals_full.csv")
    animals_to_sql(animals, OUT_DIR / "archive_import.sql")
    animals_to_json(animals, OUT_DIR / "archive.json")
    print(f"Wrote {len(animals)} animals to {OUT_DIR}/")


if __name__ == "__main__":
    main()

# Extinction Archive — exported data

| File | Purpose |
|------|---------|
| `source_extinct_animals.csv` | Frozen copy of the team’s unified high-priority list (edit this, then regenerate). |
| `animals_full.csv` | Wide CSV for Excel / pandas: animals + pharm fields + Umwelt scores. |
| `archive_import.sql` | PostgreSQL: `DROP` / `CREATE` / `INSERT` for `animals`, `archival_media`, `literature_references`. |
| `archive.json` | Single-file API/static-site bundle: each animal includes nested `archival_media` and `references`. |
| `archival_media_research.csv` | Per-species **portal + curated archival URLs** (IUCN, GBIF, BHL, NFSA, NHM, xeno-canto, etc.). See `docs/research/archival_media_by_species.md`. |

**Regenerate** after changing the source list:

```bash
python3 scripts/extinction_archive_db/generate_archive_exports.py
```

**Regenerate archival URL matrix** (after editing curated links in the script):

```bash
python3 scripts/extinction_archive_db/generate_archival_media_research.py
```

**Import into PostgreSQL** (requires `psql`):

```bash
export DATABASE_URL="postgresql://USER:PASS@HOST:5432/DBNAME"
python3 scripts/extinction_archive_db/import_to_postgres.py
```

Note: the SQL file uses **`literature_references`** instead of `references` because `references` is reserved in PostgreSQL.

**Convention:** `extinction_year` uses **negative integers** for entries like `~4,000年前` (years-before-present style, e.g. `-4000`), and **positive CE years** for dated historic extinctions (e.g. `1936`). Refine in the generator’s `parse_extinction_year()` if you need strict calendar years.

`image_url` is left empty for manual QC; use Wikimedia Commons after checking licensing.

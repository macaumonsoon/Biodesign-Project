#!/usr/bin/env python3
"""
Run generated SQL against PostgreSQL using the `psql` client (recommended).

  export DATABASE_URL="postgresql://user:pass@localhost:5432/dbname"
  python3 scripts/extinction_archive_db/import_to_postgres.py

Or explicitly:
  psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f data/extinction_archive/archive_import.sql

Regenerate SQL/CSV/JSON after editing the source list:
  python3 scripts/extinction_archive_db/generate_archive_exports.py
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from shutil import which

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SQL = REPO_ROOT / "data" / "extinction_archive" / "archive_import.sql"


def main() -> int:
    sql_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SQL
    if not sql_path.is_file():
        print(f"SQL file not found: {sql_path}", file=sys.stderr)
        print("Run: python3 scripts/extinction_archive_db/generate_archive_exports.py", file=sys.stderr)
        return 1

    url = os.environ.get("DATABASE_URL")
    if not url:
        print(
            "Set DATABASE_URL to a PostgreSQL connection string, e.g.\n"
            "  export DATABASE_URL=postgresql://user:pass@localhost:5432/mydb",
            file=sys.stderr,
        )
        return 1

    psql = which("psql")
    if not psql:
        print(
            "psql not found in PATH. Install PostgreSQL client tools, or run the SQL file "
            "from any GUI client (DBeaver, TablePlus, etc.).",
            file=sys.stderr,
        )
        return 1

    cmd = [psql, url, "-v", "ON_ERROR_STOP=1", "-f", str(sql_path)]
    print("Running:", " ".join(cmd[:2]), "-v ON_ERROR_STOP=1 -f", sql_path)
    r = subprocess.run(cmd)
    return r.returncode


if __name__ == "__main__":
    raise SystemExit(main())

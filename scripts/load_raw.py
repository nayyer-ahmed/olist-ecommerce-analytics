"""Load the raw Olist CSV files into a local DuckDB database."""
from pathlib import Path
import duckdb

# 1. Settings: where the raw files are and where the database goes
RAW_DIR = Path("data/raw")
DB_PATH = Path("data/olist.duckdb")

# 2. Open (or create) the database file and make a "raw" shelf in it
con = duckdb.connect(str(DB_PATH))
con.execute("CREATE SCHEMA IF NOT EXISTS raw")

# 3. Load each CSV as its own table
for csv_file in sorted(RAW_DIR.glob("*.csv")):
    table = csv_file.stem.replace("olist_", "").replace("_dataset", "")
    con.execute(f"""
        CREATE OR REPLACE TABLE raw.{table} AS
        SELECT * FROM read_csv_auto('{csv_file.as_posix()}')
    """)
    rows = con.execute(f"SELECT COUNT(*) FROM raw.{table}").fetchone()[0]
    print(f"raw.{table:<36} {rows:>9,} rows")

con.close()
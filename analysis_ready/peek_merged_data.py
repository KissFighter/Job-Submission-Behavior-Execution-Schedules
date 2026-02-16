#!/usr/bin/env python3
import argparse
import csv
import gzip
import json
from pathlib import Path
from typing import Dict, Iterable, TextIO


DEFAULT_COLUMNS = [
    "JobID",
    "JobIDRaw",
    "JobName",
    "Partition",
    "Account",
    "User",
    "Group",
    "State",
    "Submit",
    "Start",
    "End",
    "Elapsed",
    "ElapsedRaw",
    "ReqCPUS",
    "ReqMem",
    "ReqNodes",
    "AllocCPUS",
    "AllocNodes",
]


def open_maybe_gzip(path: Path) -> TextIO:
    if path.suffix == ".gz":
        return gzip.open(path, mode="rt", encoding="utf-8", errors="replace", newline="")
    return path.open(mode="r", encoding="utf-8", errors="replace", newline="")


def pick_columns(row: Dict[str, str], columns: Iterable[str]) -> Dict[str, str]:
    return {k: row.get(k, "") for k in columns}


def run_pandas_check(path: Path, delimiter: str, sample_rows: int) -> None:
    try:
        import pandas as pd
    except ImportError:
        print("pandas is not installed. Install with: pip install pandas")
        return

    df = pd.read_csv(
        path,
        sep=delimiter,
        nrows=sample_rows,
        na_values=["Unknown", "None", "N/A"],
        keep_default_na=True,
        low_memory=False,
    )

    print("=== Pandas Basic Check (sample) ===")
    print(f"Sample shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print("Columns:")
    print(", ".join(df.columns.tolist()))
    print("")

    dtype_rows = []
    missing_ratio = df.isna().mean().fillna(0.0) * 100
    for col in df.columns:
        dtype_rows.append(
            {
                "column": col,
                "dtype": str(df[col].dtype),
                "non_null": int(df[col].notna().sum()),
                "missing_pct_sample": round(float(missing_ratio[col]), 2),
            }
        )

    print("Dtype / Non-null / Missing% (sample):")
    print(json.dumps(dtype_rows, ensure_ascii=False, indent=2))
    print("")


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview first N rows from merged cluster job file.")
    parser.add_argument(
        "--path",
        default="/Volumes/Store/427/iccp-cluster-usage-analysis-selected/analysis_ready/whole_cluster_usage_merged_raw.txt.gz",
        help="Path to merged file (.txt or .txt.gz).",
    )
    parser.add_argument("--n", type=int, default=5, help="Number of rows to preview.")
    parser.add_argument("--delimiter", default="|", help="Field delimiter. Default: '|'.")
    parser.add_argument(
        "--full",
        action="store_true",
        help="Show full row fields. Default is key columns only.",
    )
    parser.add_argument(
        "--pandas",
        action="store_true",
        help="Run a basic pandas-based schema/dtype/missingness check on sample rows.",
    )
    parser.add_argument(
        "--pandas-n",
        type=int,
        default=2000,
        help="Sample size for --pandas check. Default: 2000.",
    )
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if args.pandas:
        run_pandas_check(path=path, delimiter=args.delimiter, sample_rows=args.pandas_n)

    with open_maybe_gzip(path) as f:
        reader = csv.DictReader(f, delimiter=args.delimiter)
        if reader.fieldnames is None:
            raise RuntimeError("Input file has no header row.")

        print(f"File: {path}")
        print(f"Total columns in header: {len(reader.fieldnames)}")
        print("Header columns:")
        print(", ".join(reader.fieldnames))
        print("")

        shown = 0
        for idx, row in enumerate(reader, start=1):
            shown += 1
            extra = row.pop(None, None)
            print(f"[Row {idx}]")
            if extra:
                print(f"extra_fields_not_in_header: {len(extra)}")
            if args.full:
                payload = row
            else:
                payload = pick_columns(row, DEFAULT_COLUMNS)
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            print("")
            if shown >= args.n:
                break

        if shown == 0:
            print("No data rows found.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
import gzip
import re
from pathlib import Path
from typing import List, TextIO


MONTH_ORDER = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


def sort_key(path: Path):
    name = path.name.lower()
    m = re.match(r"^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\d{2}\.txt$", name)
    if m:
        return (0, MONTH_ORDER[m.group(1)], name)
    return (1, name)


def open_text_write(path: Path) -> TextIO:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".gz":
        return gzip.open(path, mode="wt", encoding="utf-8", errors="replace", newline="")
    return path.open(mode="w", encoding="utf-8", errors="replace", newline="")


def open_text_read(path: Path) -> TextIO:
    return path.open(mode="r", encoding="utf-8", errors="replace", newline="")


def merge_files(files: List[Path], output: Path, strict_header: bool) -> None:
    total_data_lines = 0
    merged_files = 0
    expected_header = None

    with open_text_write(output) as out:
        for file_path in files:
            with open_text_read(file_path) as f:
                header = f.readline()
                if header == "":
                    print(f"[skip] empty file: {file_path}")
                    continue

                header_cmp = header.rstrip("\r\n")
                if expected_header is None:
                    expected_header = header_cmp
                    out.write(header)
                else:
                    if header_cmp != expected_header:
                        msg = f"header mismatch in file: {file_path}"
                        if strict_header:
                            raise ValueError(msg)
                        print(f"[warn] {msg}")

                data_lines = 0
                for line in f:
                    out.write(line)
                    data_lines += 1

                merged_files += 1
                total_data_lines += data_lines
                print(f"[ok] {file_path.name}: {data_lines} data lines")

    print("")
    print("Merge completed.")
    print(f"Merged files: {merged_files}")
    print(f"Total data lines (without header): {total_data_lines}")
    print(f"Output file: {output}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge monthly whole-cluster-usage txt files into one file with a single header."
    )
    parser.add_argument(
        "--input-dir",
        required=True,
        help="Directory containing monthly txt files (e.g., whole-cluster-usage).",
    )
    parser.add_argument(
        "--glob",
        default="*25.txt",
        help="File glob under input directory. Default: *25.txt",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output path (.txt or .txt.gz). Example: ./whole_cluster_usage_merged_raw.txt.gz",
    )
    parser.add_argument(
        "--strict-header",
        action="store_true",
        help="Fail if any file header differs from the first file header.",
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output = Path(args.output)
    if not input_dir.exists() or not input_dir.is_dir():
        raise NotADirectoryError(f"Input directory not found: {input_dir}")

    files = sorted([p for p in input_dir.glob(args.glob) if p.is_file()], key=sort_key)
    if not files:
        raise FileNotFoundError(f"No files matched glob '{args.glob}' in {input_dir}")

    print(f"Input directory: {input_dir}")
    print(f"Matched files: {len(files)}")
    for p in files:
        print(f"  - {p.name}")
    print("")

    merge_files(files=files, output=output, strict_header=args.strict_header)


if __name__ == "__main__":
    main()


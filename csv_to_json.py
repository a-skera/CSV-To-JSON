
import csv
import json
import argparse
from pathlib import Path


def convert_csv_to_json(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() != ".csv":
        raise ValueError("Input file must be a CSV file.")

    records = []

    with input_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        if not reader.fieldnames:
            raise ValueError("CSV file is empty or has no header row.")

        for row in reader:
            records.append(dict(row))

    with output_path.open(
        mode="w",
        encoding="utf-8"
    ) as json_file:

        json.dump(
            records,
            json_file,
            indent=4,
            ensure_ascii=False
        )

    print(f"[+] Conversion successful!")
    print(f"[+] Records converted: {len(records)}")
    print(f"[+] Output saved to: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert CSV files to JSON."
    )

    parser.add_argument("input", help="Input CSV file")
    parser.add_argument(
        "-o",
        "--output",
        help="Output JSON file",
        default=None
    )

    args = parser.parse_args()

    output_file = args.output or str(
        Path(args.input).with_suffix(".json")
    )

    try:
        convert_csv_to_json(args.input, output_file)
    except Exception as error:
        print(f"[-] Error: {error}")

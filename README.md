# CSV to JSON Converter

A lightweight command-line utility written in Python that converts CSV files into JSON format.

Built with Python's standard library, this tool requires no external dependencies and is easy to use.

## Features

- Convert CSV files into JSON arrays.
- Automatically use the first row as JSON object keys.
- Support UTF-8 and UTF-8 with BOM.
- Support custom CSV delimiters (comma, semicolon, etc.).
- Preserve values as strings, including leading zeros.
- Preserve empty cells as empty strings.
- Choose a custom output filename.
- No external Python packages required.

## Requirements

- Python 3.9 or later.
- No additional dependencies.

## Usage

### Basic conversion

```bash
python csv_to_json.py input.csv
```

This creates `input.json` in the same directory.

### Specify an output file

```bash
python csv_to_json.py input.csv --output output.json
```

### Use a custom delimiter

```bash
python csv_to_json.py input.csv --delimiter ";"
```

### Display help

```bash
python csv_to_json.py --help
```

## Example

### Input (`users.csv`)

```csv
ID,Name,Role
001,John,Administrator
002,Alex,Analyst
003,Sarah,Engineer
```

### Output (`users.json`)

```json
[
    {
        "ID": "001",
        "Name": "John",
        "Role": "Administrator"
    },
    {
        "ID": "002",
        "Name": "Alex",
        "Role": "Analyst"
    },
    {
        "ID": "003",
        "Name": "Sarah",
        "Role": "Engineer"
    }
]
```

## Notes

- The first CSV row must contain column headers.
- All values are preserved as strings rather than automatically converted to numbers or other data types.
- Empty cells remain empty strings.
- The input file must have a `.csv` extension.

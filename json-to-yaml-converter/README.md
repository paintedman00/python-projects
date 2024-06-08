# JSON-YAML Converter

A simple command-line tool to convert files between JSON and YAML formats.

## Features

- Convert JSON files to YAML.
- Convert YAML files to JSON.
- Handles multiple files in a single command.

## Requirements

- Python 3.x
- `pyyaml` library

You can install the required library using pip:

```bash
pip install pyyaml
```

## Installation

Clone the repository:

```bash
git clone https://github.com/paintedman00/json-yaml-converter.git
cd json-yaml-converter
```

## Usage

This script provides a command-line interface to convert files between JSON and YAML formats.

### Convert JSON to YAML

To convert JSON files to YAML, use the `-y` or `--yaml` option:

```bash
python converter.py -f file1.json file2.json -y
```

### Convert YAML to JSON

To convert YAML files to JSON, use the `-j` or `--json` option:

```bash
python converter.py -f file1.yaml file2.yaml -j
```

### Command-line Options

- `-f` or `--file`: Specify one or more files to be converted.
- `-j` or `--json`: Convert YAML files to JSON.
- `-y` or `--yaml`: Convert JSON files to YAML.

## Examples

### Convert a single JSON file to YAML

```bash
python converter.py -f example.json -y
```

### Convert multiple YAML files to JSON

```bash
python converter.py -f example1.yaml example2.yaml -j
```


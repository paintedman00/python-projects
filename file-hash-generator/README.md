
# File Hash Generator

A command-line tool to generate hashes and determine the file type of given files.

## Features

- Generate multiple types of hashes (MD5, SHA1, SHA256, SHA512, CRC32, Adler32) for files.
- Determine the file type of given files.
- Handle multiple files in a single command.

## Requirements

- Python 3.x
- `filehash` library
- `python-magic` library

You can install the required libraries using pip:

```bash
pip install filehash python-magic
```

## Installation

Clone the repository:

```bash
git clone https://github.com/paintedman00/file-hash-generator.git
cd file-hash-generator
```

## Usage

This script provides a command-line interface to generate hashes and determine the file type of files.

### Generate Hashes and File Type

To generate hashes and determine the file type, run the script with the files as arguments:

```bash
python generate_hashes.py -f file1.txt file2.jpg
```

### Get Only File Type

To get only the file type of the given files, use the `-t` or `--type` option:

```bash
python generate_hashes.py -f file1.txt file2.jpg -t
```

### Example Output

```
------------------ file1.txt META DATA ------------------
Filename: file1.txt
File Type: text/plain
md5: 5eb63bbbe01eeed093cb22bb8f5acdc3
sha1: 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed
sha256: 7d793037a0760186574b0282f2f435e7e6e8cb8d9
sha512: e4d909c290d0fb1ca068ffaddf22cbd0
crc32: 3c0d6fd0
adler32: 062c0215
----------------------------------------------------------

------------------ file2.jpg META DATA ------------------
Filename: file2.jpg
File Type: image/jpeg
md5: 1c1efab43b60f56f19e1b0d06a9a6d5b
sha1: 6dcd4ce23d88e2ee9568ba546c007c63de331585
sha256: 4b227777d4dd1fc61c6f884f48641d02f2f435e7e6e8cb8d9
sha512: 2c70f0b3d179abf5babcff9c7b7f34b4b2b3a22fb0
crc32: 3c0d6fd0
adler32: 062c0215
----------------------------------------------------------
```

### Command-line Options

- `-f` or `--file`: Specify one or more files to process.
- `-t` or `--type`: Get only the file type of the given files.

## Error Handling

- Displays appropriate messages for files that cannot be found.
- Handles errors during hash generation and file type determination.

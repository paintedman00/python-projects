
## README for Image Metadata Extractor

# Image Metadata Extractor

A command-line tool to extract metadata from image files.

## Features

- Extract EXIF metadata from image files.
- Handle multiple image files in a single command.
- Provide detailed error messages for unidentified images and decoding issues.

## Requirements

- Python 3.x
- `Pillow` library

You can install the required library using pip:

```bash
pip install Pillow
```

## Installation

Clone the repository:

```bash
git clone https://github.com/paintedman00/image-metadata-extractor.git
cd image-metadata-extractor
```

## Usage

This script provides a command-line interface to extract metadata from image files.

### Extract Metadata from Images

To extract metadata from image files, run the script with the image files as arguments:

```bash
python extract_metadata.py -f image1.jpg image2.png
```

### Example Output

```
------------------ image1.jpg META DATA ------------------
ImageWidth              : 1920
ImageHeight             : 1080
DateTime                : 2021:01:01 12:00:00
CameraModel             : Canon EOS 80D
...
----------------------------------------------------------

------------------ image2.png META DATA ------------------
No EXIF data found
----------------------------------------------------------
```

### Command-line Options

- `-f` or `--files`: Specify one or more image files to extract metadata from.

## Error Handling

- Displays appropriate messages for unidentified images.
- Handles decoding errors for byte data in EXIF metadata.

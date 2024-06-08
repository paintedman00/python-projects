# Image Metadata Cleaner

A command-line tool to remove metadata from image files.

## Features

- Remove all metadata from image files.
- Save cleaned images with a new filename prefix (`clean_`).

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
git clone https://github.com/paintedman00/image-metadata-cleaner.git
cd image-metadata-cleaner
```

## Usage

This script provides a command-line interface to clean metadata from image files.

### Clean Metadata from Images

To clean metadata from image files, run the script with the image files as arguments:

```bash
python clean_metadata.py -f image1.jpg image2.png
```

### Example Output

```
Clean Image File: clean_image1.jpg
Clean Image File: clean_image2.png
```

### Command-line Options

- `-f` or `--files`: Specify one or more image files to clean metadata from.

## Error Handling

- Displays appropriate messages for unidentified images.
- Handles errors during image reading and processing.

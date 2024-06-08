import argparse
import os
from PIL import Image
from PIL.ExifTags import TAGS


def extract_img_metadata(files):
    for file in files:
        print(f"------------------ {file} META DATA ------------------")

        if os.path.isfile(file):
            try:
                # Read the image
                image = Image.open(file)

                # Extract EXIF data
                exif_data = image.getexif()

                # Iterate over EXIF data values
                for tag_id in exif_data:
                    tag = TAGS.get(tag_id, tag_id)
                    data = exif_data.get(tag_id)

                    if isinstance(data, bytes):
                        try:
                            data = data.decode()
                        except UnicodeDecodeError:
                            data = "Cannot decode bytes data"

                    print(f"{tag:25}: {data}")

                print("----------------------------------------------------------")

            except Image.UnidentifiedImageError:
                print(f"Cannot identify image: {file}")
                print("----------------------------------------------------------")
        else:
            print(f"No file found: {file}")
            print("----------------------------------------------------------")


def main():
    parser = argparse.ArgumentParser(description='Extract metadata from images')

    parser.add_argument('-f', '--files', nargs='+', type=str, help='Image file(s)', required=True)

    args = parser.parse_args()
    files = args.files

    if files:
        extract_img_metadata(files)


if __name__ == '__main__':
    main()

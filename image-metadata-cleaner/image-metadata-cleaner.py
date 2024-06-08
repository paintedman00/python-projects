import argparse
from PIL import Image, UnidentifiedImageError


def clean_image_metadata(files):
    for file in files:
        try:
            # Open image file
            image = Image.open(file)

            # Create a new image with the same mode and size
            stripped = Image.new(image.mode, image.size)
            stripped.putdata(list(image.getdata()))

            # Save the cleaned image
            clean_filename = f"clean_{file}"
            stripped.save(clean_filename)

            print(f"Clean Image File: {clean_filename}")

        except UnidentifiedImageError:
            print(f"Cannot identify image: {file}")
        except IOError:
            print(f"Problem reading image: {file}")


def main():
    parser = argparse.ArgumentParser(description='Delete metadata in images')

    parser.add_argument('-f', '--files', nargs='+', type=str, help='Image file(s)', required=True)

    args = parser.parse_args()
    files = args.files

    if files:
        clean_image_metadata(files)


if __name__ == '__main__':
    main()

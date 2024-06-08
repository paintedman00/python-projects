import argparse
import os
from filehash import FileHash
import magic


def generate_file_hashes(files):
    # Declare the type of hash you want
    hash_algorithms = {
        "md5": FileHash('md5'),
        "sha1": FileHash('sha1'),
        "sha256": FileHash('sha256'),
        "sha512": FileHash('sha512'),
        "crc32": FileHash('crc32'),
        "adler32": FileHash('adler32')
    }

    # Iterate through the files
    for file in files:
        if os.path.isfile(file):
            try:
                file_info = {
                    "filename": file,
                    "filetype": magic.from_file(file)
                }

                # Generate hashes
                for name, hasher in hash_algorithms.items():
                    file_info[name] = hasher.hash_file(file)

                print(file_info)

            except Exception as e:
                print(f"Error processing {file}: {e}")
        else:
            print(f"No File Found: {file}")


def get_file_types(files):
    # Iterate through the files
    for file in files:
        if os.path.isfile(file):
            try:
                file_type = magic.from_file(file)
                print(f"Filename: {file}, File Type: {file_type}")
            except Exception as e:
                print(f"Error processing {file}: {e}")
        else:
            print(f"No File Found: {file}")


def main():
    parser = argparse.ArgumentParser(description='Get the hashes and file type of file(s)')

    parser.add_argument('-f', '--file', nargs='+', type=str, help='Submit file(s)', required=True)
    parser.add_argument('-t', '--type', action='store_true', help='Get only the file type of file(s)')

    args = parser.parse_args()

    if args.file:
        files = args.file

        if args.type:
            get_file_types(files)
        else:
            generate_file_hashes(files)


if __name__ == '__main__':
    main()

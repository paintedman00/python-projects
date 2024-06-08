import argparse
import json
import os
import yaml


def json2yaml(files):
    for file in files:
        if os.path.isfile(file):
            filename_full = os.path.basename(file)
            filename, extension = os.path.splitext(filename_full)

            if extension == '.json':
                with open(file, "r") as source_file:
                    source_content = json.load(source_file)

                new_filename = f'{filename}.yaml'
                if os.path.exists(new_filename):
                    print(f"ERROR: {new_filename} already exists")
                else:
                    with open(new_filename, "w") as target_file:
                        yaml.dump(source_content, target_file)
                    print(f"YAML File Converted: {new_filename}")
            else:
                print(f"Extension NOT Valid for file: {file}")


def yaml2json(files):
    for file in files:
        if os.path.isfile(file):
            filename_full = os.path.basename(file)
            filename, extension = os.path.splitext(filename_full)

            if extension == ".yaml":
                with open(file, "r") as source_file:
                    source_content = yaml.safe_load(source_file)

                new_filename = f'{filename}.json'
                if os.path.exists(new_filename):
                    print(f"ERROR: {new_filename} already exists")
                else:
                    with open(new_filename, "w") as target_file:
                        json.dump(source_content, target_file, indent=4)
                    print(f"JSON File Converted: {new_filename}")
            else:
                print(f"Extension NOT Valid for file: {file}")


def main():
    parser = argparse.ArgumentParser(description='Convert JSON to YAML and YAML to JSON')

    parser.add_argument('-f', '--file', nargs='+', type=str, help='Submit a file(s)', required=True)
    parser.add_argument('-j', '--json', action='store_true', help='Convert YAML to JSON')
    parser.add_argument('-y', '--yaml', action='store_true', help='Convert JSON to YAML')

    args = parser.parse_args()

    if args.file:
        files = args.file

        if args.json:
            yaml2json(files)

        if args.yaml:
            json2yaml(files)


if __name__ == '__main__':
    main()
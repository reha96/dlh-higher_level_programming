#!/usr/bin/python3
"""A script that adds all arguments to a Python list,
and then save them to a file'"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__(
    "6-load_from_json_file"
).load_from_json_file


def main(*argv):
    f = "add_item.json"
    elements = []
    try:
        elements = load_from_json_file(f)
    except FileNotFoundError:
        pass

    elements.append(argv)
    save_to_json_file(elements, f)


if __name__ == "__main__":
    main(*sys.argv[1:])

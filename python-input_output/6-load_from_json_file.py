#!/usr/bin/python3
"""A module that writes a function that creates an Object from a 'JSON
file'"""

import json


def load_from_json_file(filename):
    """function that creates an Object from a 'JSON
    file'

        Args:
            filename (_type_): _description_
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())

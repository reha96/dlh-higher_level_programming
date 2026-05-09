#!/usr/bin/python3
"""A module that writes a function that writes an Object to a text file,
using a JSON representation:"""

import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation

        Args:
            my_obj (_type_): _description_
            filename (_type_): _description_
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))

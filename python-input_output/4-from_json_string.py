#!/usr/bin/python3
"""A module that writes a function that returns an object (Python data
structure) represented by a JSON string:"""

import json


def from_json_string(my_str):
    """function that returns an object (Python data
    structure) represented by a JSON string

    Args:
        my_str (_type_): _description_
    """
    return json.loads(my_str)

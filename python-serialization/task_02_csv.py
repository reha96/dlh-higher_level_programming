#!/usr/bin/python3
"""gain experience in reading data from one format (CSV)
and converting it into another format (JSON) using
serialization techniques"""

import csv
import json


def convert_csv_to_json(filename):
    """takes the CSV filename as its parameter and writes
    the JSON data to data.json

    Args:
        filename (_type_): _description_
    """
    try:
        out = []
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            out.extend(reader)
        with open("data.json", "a") as f:
            f.write(json.dumps(out))
        return True
    except Exception:
        return False

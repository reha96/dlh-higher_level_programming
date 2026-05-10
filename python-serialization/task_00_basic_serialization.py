#!/usr/bin/python3
"""a basic serialization module that adds the functionality to
serialize a Python dictionary to a JSON file and deserialize
the JSON file to recreate the Python Dictionary."""

import pickle


def serialize_and_save_to_file(data, filename):
    """serialize and save data to the specified file

    Args:
        data (_type_): _description_
        filename (_type_): _description_
    """
    with open(filename, mode="wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """load and deserialize data from the specified file

    Args:
        filename (_type_): _description_
    """
    with open(filename, mode="rb") as file:
        return pickle.load(file)

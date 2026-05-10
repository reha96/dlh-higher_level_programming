#!/usr/bin/env python3
"""a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary."""

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


# Sample data to be serialized
data_to_serialize = {"name": "John Doe", "age": 30, "city": "New York"}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, "data.json")

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize("data.json")

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)

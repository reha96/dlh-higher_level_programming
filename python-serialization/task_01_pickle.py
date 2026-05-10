#!/usr/bin/python3
"""Learn how to serialize and deserialize custom Python
objects using the pickle module.

"""

import pickle


class CustomObject:
    """Create a custom Python class named CustomObject"""

    def __init__(self, name, age, is_student):
        """init

        Args:
            name (_type_): _description_
            age (_type_): _description_
            is_student (bool): _description_
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display string

        Returns:
            str: _description_
        """
        print(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Is Student: {self.is_student}"
        )

    def serialize(self, filename):
        """serialize the current instance of the object and
        save it to the provided filename

        Args:
            filename (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            with open(filename, mode="wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, mode="rb") as file:
                return pickle.load(file)
        except Exception:
            return None

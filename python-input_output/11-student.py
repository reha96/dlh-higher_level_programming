#!/usr/bin/python3
"""
Write a class Student that defines a student by:

    Public instance attributes:
    first_name
    last_name
    age
    Instantiation with first_name, last_name and age: def __init__(self,
    first_name, last_name, age):
    Public method def to_json(self): that retrieves a dictionary
    representation of a Student instance (same as 8-class_to_json.py)
    You are not allowed to import any module

"""


class Student:
    """
    create Student class
    """

    def __init__(self, first_name, last_name, age):
        """initiation method
        Args:
            first_name (_type_): _description_
            last_name (_type_): _description_
            age (_type_): _description_
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student instance"""
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            out = self.__dict__.copy()
            all_keys = set(self.__dict__.keys())
            pop_keys = all_keys - set(attrs)
            try:
                for key in pop_keys:
                    out.pop(key)
            except Exception:
                pass
            return out

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute

                Args:
                    json (_type_): _description_
        """
        return self.__dict__.update(json)

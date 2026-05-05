#!/usr/bin/python3
"""This module creates a class that defines a square without
importing any modules."""


class Square:
    """Create a class called Square that defines a square."""

    def __init__(self, size=0):
        """Initializes the size of the Square, as a private
        attribute.
        1) size must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer.
        2) if size is less than 0, raise a ValueError exception
        with the message size must be >= 0

        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance method def area(self) returns the
        current square area."""
        return self.__size ** 2

#!/usr/bin/python3
"""This module creates a class that defines a square without
importing any modules."""


class Square:
    """Create a class called Square that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size of the Square, as a private
        attribute.
        1) size must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer.
        2) if size is less than 0, raise a ValueError exception
        with the message size must be >= 0

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def position(self):
        """Public instance method def position(self) returns the
        current position."""
        return self.__position

    @position.setter
    def position(self, position):
        if (
            not isinstance(position, tuple) or len(position) != 2
            or not all(isinstance(p, int) and p >= 0 for p in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Public instance method def area(self) returns the
        current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Public instance def size(self) returns the
        current size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Public instance def size(self, size) sets the
        current size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        if self.size == 0:
            print("")
        if self.position[1] > 0:
            for i in range(self.position[1]):
                print("")
        for j in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

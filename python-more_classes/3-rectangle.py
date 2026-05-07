#!/usr/bin/python3
"""This module creates a class that defines a Rectangle."""


class Rectangle:
    """Create a class Square."""

    def __init__(self, width=0, height=0):
        """Initialization of Square class
        with private width and height attributes"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter property of Square class
        private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter property of Square class
        private attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return self.__width

    @property
    def height(self):
        """getter property of Square class
        private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter property of Square class
        private attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
        return self.__height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        out = []
        for i in range(self.__height):
            for j in range(self.__width):
                out.append("#")
            out.append("\n")
        return "".join(out)

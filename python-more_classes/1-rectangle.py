#!/usr/bin/python3
"""This module creates a class that defines a Rectangle."""


class Rectangle:
    """Create a class Square."""

    def __init__(self, width=0, height=0):
        """Initialization of Square class
        with private width and height attributes"""
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return self.__height

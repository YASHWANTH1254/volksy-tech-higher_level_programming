#!/usr/bin/python3
"""1-rectangle."""


class Rectangle:
    """class rectangle."""
    def __init__(self, width=0, height=0):
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width.setter"""
        return self.__width

    @width.setter
    def width(self, value):
        """args:"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Args:"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

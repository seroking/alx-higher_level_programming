#!/usr/bin/python3
"""
Module : 1-rectangle.py
class Rectangle
"""


class Rectangle:
    """
    Define a class with private attributes.

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width,height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
    """

    def __init__(self, width=0, height=0):
        """ initialize rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ return perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ print the rectangle with '#' """
        i = 0
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rect

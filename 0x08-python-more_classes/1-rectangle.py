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
    """

    def __init__(self, width=0, height=0):
        """ initialise the instance of the rectangle """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ retrieve width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height of the rectangle if type = int and value > 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
            self.__height = value

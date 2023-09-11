#!/usr/bin/python3
"""
module : '8-rectangle.py'
class:
    class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass Rectangle inherite from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area of the Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """ str """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

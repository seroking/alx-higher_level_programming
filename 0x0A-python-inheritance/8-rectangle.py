#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """subclass Rectangle inherite from BaseGeometry """
    def __init__(self, width, height):
        """ instantiation of the class rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

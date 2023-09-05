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

    Attributes:
        number_of_instances : number of instances created and not deleted
        print_symbol (any type): used to print string representation

    Functions:
        __init__(self, width,height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __rep__(self)
        bigger_or_equal(rect_1, rect_2)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialize rectangle """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """ deletion message of an instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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
        """ Prints rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = "\n".join([str(self.print_symbol) * self.__width
                         for row in range(self.__height)])
        return rec

    def __repr__(self):
        """ String representation of the class """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns new rectangle instance with width == height == size """
        return cls(size, size)

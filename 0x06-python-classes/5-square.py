#!/usr/bin/python3

""" square size exception """


class Square:
    """ class square """

    def __init__(self, size=0):
        """Initiate instance
        attributes :
            size (int) : size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ get or set  he size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the square """
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with '#' ."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

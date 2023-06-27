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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

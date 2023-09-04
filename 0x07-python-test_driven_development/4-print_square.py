#!/usr/bin/python3
"""
module : print_square.py
"""
def print_square(size):
    """
    print a square of '#' with the lenght size
    args:
        size : (int)
    """
    l = size
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0 and isinstance(size, int):
        raise ValueError("size must be >= 0")
    elif size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")


    while l > 0:
        print('#' * size)
        l -= 1

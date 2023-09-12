#!/usr/bin/python3
"""
module : 0-read_file.py
functions:
    read_file
"""


def read_file(filename=""):
    """ read a file """
    with open(filename, "r", encoding="utf-8"):
        """ working in a file """
        read_file = f.read()
        print(read_file, end="")

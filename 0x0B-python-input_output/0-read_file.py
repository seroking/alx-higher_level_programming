#!/usr/bin/python3
"""
module : 0-read_file.py
functions:
    read_file
"""


def read_file(filename=""):
    """ read a file """
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()


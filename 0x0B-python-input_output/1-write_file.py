#!/usr/bin/python3
"""
module : '1-write_file.py'

functions:
    write_file
"""


def write_file(filename="", text=""):
    """ write a text in the file and create it if it doesn't exist """
    with open(filename, "w", encoding="UTF-8") as f:
        w_file = f.write(text)

    return w_file

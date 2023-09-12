#!/usr/bin/python3
"""
module : '2-append_write.py'
functions:
    append_write
"""


def append_write(filename="", text=""):
    """ appen text to a file"""
    with open(filename , "a", encoding="UTF-8") as f:
        a_file = f.write(text)

    return a_file

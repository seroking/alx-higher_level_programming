#!/usr/bin/python3
"""
module : 0-lookup.py
functions:
    def lookup(obj)
"""


def lookup(obj):
    """
    return the list of attributes and methods of an objects
    """
    return dir(obj)

#!/usr/bin/python3
"""
module : 4-inherits_from.py

functions :
    inherits_from
"""


def inherits_from(obj, a_class):
    """
    return a bolean
    """
    return isinstance(obj, a_class) and not type(obj) is a_class

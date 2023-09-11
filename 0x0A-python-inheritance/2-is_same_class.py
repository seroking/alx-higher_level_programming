#!/usr/bin/python3
"""
module : is_same_class.py

functions :
    is_same_class
"""


def is_same_class(obj, a_class):
    """
    function returns True if the object is an instance of the specified class ;
    otherwise False
    """
    return obj.__class__ is a_class

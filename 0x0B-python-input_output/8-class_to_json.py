#!/usr/bin/python3
"""
This is '8-class_to_json' module.

"""


def class_to_json(obj):
    """returns the dictionary description for JSON serialization of an object"""
    my_dict = {}
    for item in dir(obj):
        if (not item.startswith("__")) and (not callable(getattr(obj, item))):
            my_dict[item] = getattr(obj, item)
    return my_dict

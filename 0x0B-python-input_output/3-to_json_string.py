#!/usr/bin/python3
"""
Module : '3-to_json_string.py'
Functions:
    to_json_string
"""


def to_json_string(my_obj):
    """ return JSON representation """
    import json
    return json.dumps(my_obj)

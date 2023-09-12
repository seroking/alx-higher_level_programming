#!/usr/bin/python3
""" module: 6-load_from_json_file.py """


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    import json


    with open(filename, "r", encoding="UTF-8") as f:
        json.loads(f)

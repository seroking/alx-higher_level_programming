#!/usr/bin/python3
""" module : '5-save_to_json_file.py' """


def save_to_json_file(my_obj, filename):
    """ save a file of json representation"""
    import json

    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(my_obj, f)

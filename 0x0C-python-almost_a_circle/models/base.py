#!/usr/bin/python3
"""
modules : base.py

classes:
    Base
functions:
    def __init__(self, id=None)
"""


import json

class Base:
    """ Base class representation """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """
        self.id = id
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs == None:
            return []
        else:
            text = Base.to_json_string(list_objs)
            with open("{}.json".format(cls.__name__), "w", enconding="UTF-8") as f:
                f.write(text)

#!/usr/bin/python3
"""
modules : base.py

classes:
    Base
"""


import json


class Base:
    """
    defines Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    Static Methods:
        to_json_string(list_dictionaries)
        from_json_string(json_string)
    Class Methods:
        save_to_file(cls, list_objs)
        load_from_file(cls)
        create(cls, **dictionary)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """
        self.id = id
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ transform a dictionnary into json str"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save the json str on a file"""
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """load a json string """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create a dummy obj"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load json str from a jsonfile"""
        filename = cls.__name__ + ".json"
        if not filename:
            return []
        else:
            with open(filename, "r", encoding="UTF-8") as f:
                read_json = f.read()
                dict_list = Base.from_json_string(read_json)
                return [cls.create(**d) for d in dict_list]

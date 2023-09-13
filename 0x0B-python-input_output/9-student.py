#!/usr/bin/python3
""" module: 9-student.py"""


class Student:
    """ representation of the class student """
    def __init__(self, first_name, last_name, age):
        """ Student representation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a json repr of dictionary of student"""
        my_dict = {}
        for item in dir(self):
            if (not item.startswith("__")) /
            and (not callable(getattr(self, item))):
                my_dict[item] = getattr(self, item)

        return my_dict

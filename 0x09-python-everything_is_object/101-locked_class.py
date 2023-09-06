#!/usr/bin/python3
""" LockedClass
"""
class LockedClass:
    if name != "first_name" and hasattr(self, name):
        raise AttributeError("You can only set the 'first_name' attribute")
    super().__setattr__(name, value)

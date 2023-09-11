#!/usr/bin/python3
"""
module : 5-base_geometry.py

class:
    BaseGeometry
"""


class BaseGeometry:
    """ empty class"""
    def area(self):
        """method that raise ana exeption """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate the value"""
        if type(value) not in [float, int]:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

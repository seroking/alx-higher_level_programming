#!/usr/bin/python3
"""
class Square

Inherits : from Rectangle;
Inits    : superclass' id, width (as size), height (as size), x, y
Contains : public attribute size
Prints   : [Square] (<id>) <x>/<y> - <size>
Updates attributes : arg1=id, arg2=size, arg3=x, arg4=y
Returns  : dictionary representation of attributes
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    defines a class Square; inherits from class Rectangle
    Inherited Attributes:
        id
        __weight
        __height
        __x
        __y
    Class Attributes:
        size
    Inherted Methods:
        Base.init(self, id=None)
        Rectangle.init(self, width, height, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        x(self)
        x(self, value)
        y(self)
        y(self, value)
        area(self)
        display(self)
    Methods:
        __str__
        __init__(self, size, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        size(self)       size(self, value)
        to_dictionary(self)
    """
        def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """ setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        """ str representation"""
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}").format(self.__class__.__name__, self.id,
                                                   self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ update all attributes"""
        if args:
            for k, val in enumerate(args):
                if k == 0:
                    self.id = val
                elif k == 1:
                    self.size = val
                elif k == 2:
                    self.x = val
                else:
                    self.y = val
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            elif "size" in args:
                self.size = kwargs["size"]
            elif "x" in kwargs:
                self.x = kwargs["x"]
            elif "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ attributes to dictionary"""
        return {"id": self.id, "x": self.x,
                "size": self.size, "y": self.y}

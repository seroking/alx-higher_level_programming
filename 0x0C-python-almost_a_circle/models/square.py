#!/usr/bin/python3
""" module: square.py """


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
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
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

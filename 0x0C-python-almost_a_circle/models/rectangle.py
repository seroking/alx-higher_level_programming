#!/usr/bin/python3
""" module: rectangle.py"""


from models.base import Base


class Rectangle(Base):
    """
    defines a class Rectangle; inherits from class Base
    Inherited Attributes:
        id
    Class Attributes:
        __width
        __height
        __x
        __y
    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
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
        __str__
        to_dictionary(self)
        """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """  representation str """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def area(self):
        """ return the area of the rectangle"""
        return (self.width * self.height)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer ")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer ")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer ")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer ")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def display(self):
        """ display the rectangle with all dimensions"""
        print("\n" * self.y +
              "\n".join(" " * self.x + "#" * self.width
                        for i in range(self.height)))

    def update(self, *args, **kwargs):
        """ update all value of attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ transform all attributes to a dictionnary"""
        return {
                'x': self._Rectangle__x,
                'y': self._Rectangle__y,
                'id': self.id,
                'height': self._Rectangle__height,
                'width': self._Rectangle__width
                }

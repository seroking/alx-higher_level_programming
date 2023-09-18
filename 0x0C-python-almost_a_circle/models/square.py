#!/usr/bin/python3
""" module: square.py """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ representaion of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return ("[square] ({}) {}/{} - {}").format(self.id,
                                                   self.x, self.y, self.size)

    def update(self, *args, **kwargs):
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
        return {"id": self.id, "x": self.x,
                "size": self.size, "y": self.y}

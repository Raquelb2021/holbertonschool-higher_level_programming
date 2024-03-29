#!/usr/bin/python3
"""class square"""


from models.rectangle import Rectangle
"""importing Rectangle"""


class Square(Rectangle):
    """class square that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Call the super class with id, x, y, width and height
           The width and height must be assigned to the value of size
        """
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """__str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square"""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, arg in zip(attributes, args):
                setattr(self, i, arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Square instance to dictionary representation"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

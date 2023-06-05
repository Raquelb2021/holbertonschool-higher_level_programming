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
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
                else:
                    for key, value in kwargs.items():
                        if hasattr(self, key):
                            setattr(self, key, value)

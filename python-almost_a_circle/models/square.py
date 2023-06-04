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

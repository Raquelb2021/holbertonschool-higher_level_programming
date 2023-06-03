#!/usr/bin/python3
"""
class rectangle inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """initializes base class
    with private attributes
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangles and the attributes
        width, height, x, y, and id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """setting the x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """setthing the y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height

    def display(self):
        """
        prints the rectangle instance using the # character
        """
        print("\n" * self.y, end="")
        """print self.y newlines to move the rectangle down,
        by self.y rows
        """
        for i in range(self.height):
            print(" " * self.x + '#' * self.width)
            """spaces to move the rectangle to the right by self.x columns
            before printing the # characters
            """

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

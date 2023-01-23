#!/usr/bin/python3
"""This program use the string str() and print()"""


class Rectangle:
    """ class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ constructor """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ Public instance method that returns the rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return for print"""
        str = ''
        if self.width == 0 or self.height == 0:
            return ('')
        else:
            new = []
            for i in range(self.height):
                new.append('#' * self.__width)
                if i < (self.height - 1):
                    new.append('\n')
            return string.join(new)

#!/bin/usr/python3
"""This program gets the perimeters of a retangle"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """method that execute after create an object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = value

    def area(self):
        """public instance method, that returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """public intance method, that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__width * 2)

    def __str__(self):
        """returns the string representation of the object"""
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            new = []
            for i in range(0, self.__height):
                new.append('#' * self.width)
            if i < (self.__height - 1):
                new.append('\n')
        return string.join(new)

    def __repr__(self):
        """returns the object representation in string format"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

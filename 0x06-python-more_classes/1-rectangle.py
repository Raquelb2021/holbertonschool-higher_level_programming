#!/usr/bin/python3
"""This program defines a rectangle and return area and perimeter"""


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
            return (self.__width + self.__height * 2)

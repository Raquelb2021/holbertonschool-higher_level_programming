#!/usr/bin/python3
"""This program define a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """This __init__ method execute after create an object"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """the getter method to get the properties using an object"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """the getter methods"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')
        else:
            self.__height = value

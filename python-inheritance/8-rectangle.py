#!/usr/bin/python3
"""Defines a class Rectangle that inherits from a base class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry"""


    def __init__(self, width, height):
        """The __init method of the Rectangles class takes two arguments"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
"""This is a modulo docstring"""
"""Defines a class Rectangle that inherits from a base class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry"""


def __init__(self, width, height):
    """The __init method of the Rectangles class takes two arguments"""

    """width and height, and validates"""
    """them using the integer_validator method"""
    """inherited from the BaseGeometry class"""
    """The validated values are then assigned to the private instance"""
    """variables __width and __height."""

    self.integer_validator("width", width)
    self.integer_validator("height", height)

    self.__width = width
    self.__height = height

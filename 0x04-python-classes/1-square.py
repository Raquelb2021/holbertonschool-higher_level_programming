#!/usr/bin/python3
"""Square module"""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Private instance attribute: size"""

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

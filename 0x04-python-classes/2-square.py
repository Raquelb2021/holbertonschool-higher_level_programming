#!/usr/bin/python3
"""square area"""
class Square:
    """Private instance attribute: size"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """that returns the current square area"""
        return (self.__size * self.__size)

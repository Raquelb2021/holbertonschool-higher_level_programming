#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """class square"""

    def __init__(self, size=0):
        """initialize the data"""
        self.__size = size

    @property
    def size(self):
        """Return the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
                print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

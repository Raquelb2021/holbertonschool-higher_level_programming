#!/usr/bin/python3


class Square:
    """Class Square"""

    def __init__(self, size=0):
        """initializes a square"""
        self.__size = size

    @property
    def size(self):
        """Getter"""
        return (self.__size)

    @size.setter
    """setter"""
    def size(self, value):
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
        for i in range(self.size):
            print("#" * self.size)

            if self.__size == 0:
                print()

#!/usr/bin/python3
"""This module define a funtion print_square"""


def print_square(size):
    """Function that takes teh argument size as parameter
    and print a square using the character # """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
        for row in range(size):
            [print("#", end="") for col in range(size)]
            print("")

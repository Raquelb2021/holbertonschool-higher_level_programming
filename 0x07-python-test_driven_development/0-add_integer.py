#!/usr/bin/python3
"""Define an integer additon function"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b
    a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b

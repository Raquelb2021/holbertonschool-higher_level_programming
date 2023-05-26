#!/usr/bin/python3
"""Module docstring for inherits_from"""


def inherits_from(obj, a_class):
    """This function check if the object is an instance of a"""
    """specified class or an instance of a subclass of the specified class"""

    """It also uses the type() function and the != operator"""
    """to check if the exact class of the object is not equal"""
    """to the specified class. If both conditions are True, it means"""
    """that the object is an instance of a subclass"""
    """(directly or indirectly) of the specified class."""

    return isinstance(obj, a_class) and type(obj) != a_class

#!/usr/bin/python3
"""This is a module docstring"""
"""defines a class new class MyList that inherits from list"""


class MyList(list):
    """This is a class docstring, class that extends the built-in list class"""
    def print_sorted(self):
        """This is a function docstring"""
        """print the list in sorted ascending order"""
        sortedlist = sorted(self)
        print(sortedlist)

#!/usr/bin/python3
"""Private class attribute"""


class Base:
    """Class base has a private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        """
        This class will be the “base” of all other classes in this project.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

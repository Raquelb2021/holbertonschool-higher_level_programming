#!/usr/bin/python3
"""Fuction that reads a text file"""


def read_file(filename=""):
    """This coode opens a file,
    named  my_file_0.txt and read it using open()
    the with statement ensures that the file is properly closed
    afeter the operations are perfomed"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

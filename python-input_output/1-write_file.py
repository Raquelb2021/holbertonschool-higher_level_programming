#!/usr/bin/python3
"""Write a text in the file"""


def write_file(filename="", text=""):
    """This function takes 2 argument:

    filename: name of the file to write to,

    text: the string to write to the file."""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)

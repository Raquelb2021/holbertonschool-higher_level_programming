#!/usr/bin/python3
"""Append a string at the end of a txt file"""


def append_write(filename="", text=""):
    """ The 'a' character is used to append a string,
    at the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))

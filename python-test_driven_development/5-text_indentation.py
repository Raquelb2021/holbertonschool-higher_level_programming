#!/usr/bin/python3
"""Text_indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
        print("\n".join(line.strip()
            for line in text.split("\n")))

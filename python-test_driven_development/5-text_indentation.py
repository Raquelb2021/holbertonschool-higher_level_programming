#!/usr/bin/python3
"""Text_indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = [".", ":", "?"]
    for idx, i in enumerate(text):
        if i in special_chars:
            print(i, end="\n")
            print()
        elif i == " ":
            if text[idx -1] in special_chars:
                continue
            else:
                print(i, end="")
        else:
            print(i, end="")

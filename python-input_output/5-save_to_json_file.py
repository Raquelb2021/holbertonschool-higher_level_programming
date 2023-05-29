#!/usr/bin/python3
"""task 5"""


def save_to_json_file(my_obj, filename):
    """
    args:
    my_obj: the obj to be written in the text file
    filename: is the file

    return: A string containing the JSON representation of the input obj
    """
    import json
    with open(filename, 'w', encoding="utf-8") as file:
        return json.dump(my_obj, file)

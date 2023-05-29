#!/usr/bin/python3
"""task 5 Json"""


def from_json_string(my_str):
    """
    Return: the object python data structure
    list and dictionary

    """
    import json
    return json.loads(my_str)

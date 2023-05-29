#!/usr/bin/python3
"""Import json to convert a python object into a json string"""

import json
"""
Returns th JSON representation of an object as a string

Args:
    my_obj: The object to be serialized.
    This can be any Pyhton object,
    that is JSON serializable,
    such as a
    dictionary, list, tuple, string, integr, float, boolean
    or None.

    Returns:
    A string containing the JSON representation of the input object.
    """


def to_json_string(my_obj):
    return json.dumps(my_obj)

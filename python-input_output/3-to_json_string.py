#!/usr/bin/python3
"""Using Json bult-in package"""

import json
"""Import json to convert a python object into a json string"""


def to_json_string(my_obj):

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


return json.dumps(my_obj)

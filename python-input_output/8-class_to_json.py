#!/usr/bin/python3


def class_to_json(obj):
    """
    Returns the dictionary
    description with simples data
    structure
    for JSON serialization of an object
    """
    return obj.__dict__

#!/usr/bin/python3
"""
    Returns the dictionary
    description with simples data
    structure
    for JSON serialization of an object
    """


def class_to_json(obj):
    return obj.__dict__

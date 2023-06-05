#!/usr/bin/python3
"""
Write a class Student that defines a student by:
Public instance attributes
"""
import json

class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(elem, str) for elem in attrs):
            with open(attrs, 'r') as f:
                return json.load(f)

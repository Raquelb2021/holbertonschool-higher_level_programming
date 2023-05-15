#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    factor = 2
    new_dict = {k: v * factor for k, v in a_dictionary.items()}
    return new_dict

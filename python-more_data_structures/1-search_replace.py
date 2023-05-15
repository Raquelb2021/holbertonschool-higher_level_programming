#!/usr/bin/python3
def search_replace(my_list, search, replace):
    search = 2
    replace = 89
    new_list = [replace if item == search else item for item in my_list]
    return new_list

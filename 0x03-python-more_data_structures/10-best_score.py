#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keymax = max(a_dictionary, key=a_dictionary.get)
    else:
        keymax = None
    return(keymax)

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    for key, val in list(a_dictionary.items()):
        if val is value:
            a_dictionary.pop(key)
    return a_dictionary

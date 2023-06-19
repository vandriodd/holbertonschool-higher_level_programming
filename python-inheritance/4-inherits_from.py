#!/usr/bin/python3
"""
    4-inherits_from module
"""


def inherits_from(obj, a_class):
    """ Checks if object inherits from subclass or not """
    return isinstance(obj, a_class) and type(obj) is not a_class

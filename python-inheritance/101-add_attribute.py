#!/usr/bin/python3
"""
    101-add_attribute module
"""


def add_attribute(obj, attr, value):
    """ Adds an attribute to a class if it's possible """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

#!/usr/bin/python3
"""
    1-write_file module
"""


def write_file(filename="", text=""):
    """ Writes on a file and returns the number of chars written """
    with open(filename, mode="w", encoding="utf-8") as file:
        amount_chars = file.write(text)
    return amount_chars

#!/usr/bin/python3
"""
    9-student module
"""


class Student:
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """ Initializes an instance of Student Class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns JSON format """
        return self.__dict__

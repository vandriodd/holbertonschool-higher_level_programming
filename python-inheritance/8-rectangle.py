#!/usr/bin/python3
"""
    8-rectangle module
"""


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ Returns the area (not implemented) """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Initializes """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

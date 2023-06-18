#!/usr/bin/python3

""" Defines Rectangle class """


class Rectangle:
    """ Defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Initializes a rectangle
        Args:
            width (int): width of new rectangle
            height (int): height of new rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ Height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of new rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of new rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

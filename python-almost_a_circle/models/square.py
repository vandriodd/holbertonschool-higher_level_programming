#!/usr/bin/python3
"""
    square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes an instance of Square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns details about the Square instance """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

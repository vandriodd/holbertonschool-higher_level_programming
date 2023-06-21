#!/usr/bin/python3
"""
    100-my_int module
"""


class MyInt(int):
    """ MyInt class """

    def __eq__(self, argument):
        """ Function that changes equal to negation """
        return super().__ne__(argument)

    def __ne__(self, argument):
        """ Function that changes negation to equal """
        return super().__eq__(argument)

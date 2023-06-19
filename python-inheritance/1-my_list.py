#!/usr/bin/python3
"""
    1-my_list module
"""


class MyList(list):
    """ MyList class that inherits from list """

    def print_sorted(self):
        """ Prints the list in a sorted way """
        print(sorted(self))

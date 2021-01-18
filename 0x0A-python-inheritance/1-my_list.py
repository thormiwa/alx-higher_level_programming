#!/usr/bin/python3

"""
A module for class MyList
"""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """A method that prints the list sorted"""
        print(sorted(self))

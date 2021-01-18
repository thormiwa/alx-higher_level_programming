#!/usr/bin/python3

"""
A is_same_class module.
"""


def is_same_class(obj, a_class):
    """A method that returns True if the object is exactly an instance of the
    specified class else False."""
    return type(obj) is a_class

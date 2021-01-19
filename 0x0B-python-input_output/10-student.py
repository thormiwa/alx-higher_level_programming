#!/usr/bin/python3
"""A module for class student."""


class Student:
    """A class named student"""

    def __init__(self, first_name, last_name, age):
        """Initialize student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        new_dict = {}
        if (attrs is not None):
            for a in attrs:
                if a in self.__dict__:
                    new_dict[a] = self.__dict__[a]
            return new_dict
        else:
            return self.__dict__

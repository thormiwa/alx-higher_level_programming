#!/usr/bin/python3


def no_c(my_string):
    no_copy = [a for a in my_string if a != 'c' and a != 'C']
    return ("".join(no_copy))

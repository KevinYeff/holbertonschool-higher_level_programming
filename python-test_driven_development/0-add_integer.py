#!/usr/bin/python3
"""
This is "0-add_integer" module
this module contains add_integers function that adds two integers
"""


def add_integer(a, b=98):
    """Return the addition of two numbers
    Parameters:
    a must be an integer or float.
    b must be an integer or float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be and integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    return a + b

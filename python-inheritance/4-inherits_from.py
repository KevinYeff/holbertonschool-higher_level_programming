#!/usr/bin/python3
"""
task 4
"""


def inherits_from(obj, a_class):
    """
    Note:
    The object needs to be an instance of a class not the class itself,
    a = True is a bool so bool is bool not an instance.
    Return True if an object is an instance of a class...
    otherwise return False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

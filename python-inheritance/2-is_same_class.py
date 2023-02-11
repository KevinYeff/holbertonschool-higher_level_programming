#!/usr/bin/python3
"""
Task 2
"""


def is_same_class(obj, a_class):
    """
    Notes: first try was using isinstance(), but sice everything is an
    object, we can use that for this task.
    Returns true if obj is exactly an instance of specified class
    """
    return type(obj) is a_class

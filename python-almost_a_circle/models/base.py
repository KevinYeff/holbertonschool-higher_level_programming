#!/usr/bin/python3
"""
Class Module
"""


class Base:
    """
    Initializing Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            """ Assing the public instance attribute id"""
            self.id = id
        else:
            """
            Increment the private class
            and assing the new value to the
            public instance attribute id
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#!/usr/bin/python3
"""
Module 9 Student to JSON
"""


class Student:
    """
    Public instace method
    """

    def __init__(self, first_name, last_name, age):
        """
        Public instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    Public method that retrieves a dictionary
    """

    def to_json(self):
        """
        Returns a dictionary representation of a Student instance
        """
        return self.__dict__

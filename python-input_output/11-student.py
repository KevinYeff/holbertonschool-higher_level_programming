#!/usr/bin/python3
"""
Module 11 Student to disk and reload
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

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            """ create a empty dictionary """
            filteredDict = {}
            """ attribute in list of attributes """
            for attr in attrs:
                """ if attribute exists in the dictionary we add """
                if attr in self.__dict__:
                    filteredDict[attr] = self.__dict__[attr]
            """ return the filtered dictionary """
            return filteredDict
    """
    Public method
    """

    def reload_from_json(self, json):
        """
        Replacing the attributes with the elements in the json dictionary
        """
        for i in json:
            """
            traversing the elements of the json dictionary
            and replacing the attributes of the dictionary
            """
            self.__dict__[i] = json[i]

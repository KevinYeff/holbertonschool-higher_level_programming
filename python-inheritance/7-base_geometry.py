#!/usr/bin/python3
"""
Task 7 Class based on previous task
"""


class BaseGeometry:
    """
    Public instance method
    """

    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")
    """
    Public isntance method
    """

    def integer_validator(self, name, value):
        """
        Note:
        We can assume that name is always a string.
        function that validates the value and raises
        exceptions with messages
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

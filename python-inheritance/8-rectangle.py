#!/usr/bin/python3
"""
Task 8 Class Rectangle that inherits from BaseGeometry
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


"""
Defines a Class Named Rectangle
"""


class Rectangle(BaseGeometry):
    """
    Defines the class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Inicializes an instance of the class Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
"""
Defines a Class named Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Should return a representation of the object as a string of chars
        """
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width,
                                   self.__height)

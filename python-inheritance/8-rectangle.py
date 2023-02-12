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

#!/usr/bin/python3
"""
Defines a Class named Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines the class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Inicializes an instance of the class Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of a Square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Should return a representation of the object as a string of chars
        """
        return "[{}] {}/{}".format(self.__class__.__name__, self.__size,
                                   self.__size)

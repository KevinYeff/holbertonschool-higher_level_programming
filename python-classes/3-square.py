#!/usr/bin/python3
""" Class """


class Square:
    """initializing the instance with private attribute size"""

    def __init__(self, size=0):
        """Initializing using conditions considering errors"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """Public instance method"""

    def area(self):
        """Returns the square area"""
        return self.__size ** 2

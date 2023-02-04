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
    """defining method as getter"""
    @property
    def size(self):
        return self.__size
    """defining method as a setter"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """Public instance method"""

    def area(self):
        """Returns the square area"""
        return self.__size ** 2
    """Public instance method"""

    def my_print(self):
        """prints a square of size size.__self"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

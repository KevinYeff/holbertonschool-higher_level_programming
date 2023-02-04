#!/usr/bin/python3
""" Class """


class Square:
    """initializing the instance with private attribute size"""

    def __init__(self, size=0, position=(0, 0)):
        """ New way to print square"""
        self.size = size
        self.position = position
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
    """ position getter """
    @property
    def position(self):
        return self.__position
    """ position setter """
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        """Public instance method"""

    def area(self):
        """Returns the square area"""
        return self.__size ** 2
    """Public instance method"""

    def my_print(self):
        """prints a square based on position and size"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

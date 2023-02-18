#!/usr/bin/python3
"""
Module class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """ Initializing the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        defining "private" attributes
        Python modifies internally the name of the attributes
        to _ClassName__attribute to avoid colisions
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """
        Super class, this super call will use the logic of
        the __init__ of the Base class
        """
        super().__init__(id)

    @property
    def width(self):
        """
        Getter method for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x attribute
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y attribute
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """
    Updating class rectangle; adding the public method area
    """

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.width * self.height

    """
    Updating the class Rectangle; by adding the public method display
    """

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        """
        for row in range(0, self.height):
            for fill in range(0, self.width):
                print("#", end="")
            print(end='\n')

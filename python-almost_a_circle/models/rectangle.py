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
        self.__y = value

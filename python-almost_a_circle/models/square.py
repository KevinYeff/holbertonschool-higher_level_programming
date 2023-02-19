#!/usr/bin/python3
"""
Module class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class and uses the logic of the Rectangle
        class, the width and height are assigned to the value of size
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloading method returns a string representation of
        the Square instance
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
    """
    Updating the class Square by adding getter and setter
    """
    @property
    def size(self):
        """
        Retrieves the width value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter module for Square but uses Rectangle's attributes
        """
        self.width = value
        self.height = value

    """
    Updating the Square Class by addind the public method update()
    """

    def update(self, *args, **kwargs):
        """
        Method that updates the attributes of the class Square
        """
        attributes = ['id', 'size', 'x', 'y']

        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    """
    Updating the Square class so that it returns a dictionary
    """

    def to_dictionary(self):
        """
        Method that returns a dictionary representation of the Square class
        """
        dictionary = {}
        attributes = ['id', 'size', 'x', 'y']

        for passdAttr in attributes:
            dictionary[passdAttr] = getattr(self, passdAttr)
        return dictionary

"""
Module class Rectangle
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
                                                 self.height)

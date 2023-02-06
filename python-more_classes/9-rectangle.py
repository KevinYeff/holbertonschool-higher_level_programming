#!/usr/bin/python3
""" Class, defines a rectangle"""


class Rectangle:
    """ Empty class  """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieving """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieving """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """task 2 """

    def area(self):
        """ Calculates the área of a rectangle and returns it """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.height)

    """ task 3"""

    def __str__(self):
        """ Prints a rectangle """
        if self.width == 0 or self.height == 0:
            return ""
        return ("\n".join([(str(self.print_symbol) * self.__width)
                           for i in range(self.__height)]))
    """ task 4 """

    def __repr__(self):
        """ String representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    """ Task 5 """

    def __del__(self):
        """ Method that executes when an object is deleted """
        print("Bye rectangle...")
        """task 6"""
        Rectangle.number_of_instances -= 1
    """ task 8 """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area
        Parameters:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1
        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    """ task 9 """
    @classmethod
    def square(cls, size=0):
        """ returns a new rectangle instance with w=h=s. """
        return cls(size, size)

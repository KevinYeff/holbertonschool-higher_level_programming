#!/usr/bin/python3
"""
Module 12 Pascal's triangle
"""


def pascal_triangle(n):
    """
    Return an empty list if n is equal or less than 0
    """
    if n <= 0:
        return []
    """
    Initializing a variable with a list that contains a list with a
    single element
    """
    triangle = [[1]]
    """
    Traversing n times
    """
    for i in range(1, n):
        """
        initializing a list with a single element "1" for every iteration
        """
        row = [1]
        """
        Sum 2 elements of the previous position
        """
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        """
        Add 1 to the end of the row
        """
        row.append(1)
        """
        add the row to the triangle
        """
        triangle.append(row)
    """
    Return the Pascal's triangle
    """
    return triangle

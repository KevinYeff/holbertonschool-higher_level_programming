#!/usr/bin/python3
"""
This module divides the elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function that divides the elements of a given matrix
    Parameters:
    matrix must be a list of lists (integers and floats)
    div the divider
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list or not all(map(lambda x: type(x) == list, matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    n = len(matrix[0])
    if not all(map(lambda x: len(x) == n, matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(map(lambda x:
                   all(map(lambda y: type(y) in [int, float], x)), matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    return [[round(y / div, 2) for y in x] for x in matrix]

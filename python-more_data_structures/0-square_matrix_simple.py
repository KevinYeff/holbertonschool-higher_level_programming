#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = [list(map(lambda y: y ** 2, x)) for x in matrix]
    return (newMatrix)

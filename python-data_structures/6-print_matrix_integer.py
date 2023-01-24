#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix[0:]:
        sep = ""
        for j in i[0:]:
            print(sep, end="")
            print("{:d}".format(j), end="")
            if j != i[-1]:
                sep = " "
        print("")

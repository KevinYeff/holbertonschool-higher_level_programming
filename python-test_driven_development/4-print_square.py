#!/usr/bin/python3
""" Module that prints a square """


def print_square(size):
    """Pints a square with the "#" character"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

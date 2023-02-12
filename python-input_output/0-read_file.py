#!/usr/bin/python3
"""
Module 0, Read file
"""


def read_file(filename=""):
    """
    Open and print a file
    """
    with open("my_file_0.txt", mode="r", encoding="utf-8") as fd:
        print(fd.read(), end="")

#!/usr/bin/python3
"""
Module 1 Write to a file
"""


def write_file(filename="", text=""):
    """
    Opens and writes a text in to a file
    Shuould create a file if it does not exits
    should overwrite
    Returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        return fd.write(text)

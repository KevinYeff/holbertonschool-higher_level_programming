#!/usr/bin/python3
"""
Module 2 Append to file
"""


def append_write(filename="", text=""):
    """
    Opens and append text in to a file
    Returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as fd:
        return fd.write(text)

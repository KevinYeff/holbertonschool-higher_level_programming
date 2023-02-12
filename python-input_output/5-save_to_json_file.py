#!/usr/bin/python3
"""
Module 5 Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        json.dump(my_obj, fd)

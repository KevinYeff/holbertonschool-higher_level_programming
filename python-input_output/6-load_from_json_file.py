#!/usr/bin/python3
"""
Module 6 Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an object from a JSONM file
    """
    with open(filename, mode="r", encoding="utf-8") as fd:
        """
        opens a JSON file and creates an object from it
        """
        return json.load(fd)

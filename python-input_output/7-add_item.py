#!/usr/bin/python3
"""
Module 7 Load, add, save
"""

from os import path
import sys

saveToJsonFile = __import__('5-save_to_json_file').save_to_json_file
loadFromJsonFile = __import__('6-load_from_json_file').load_from_json_file

if path.exists("add_item.json"):
    JSONfile = loadFromJsonFile("add_item.json")
else:
    JSONfile = []

for argument in sys.argv[1:]:
    JSONfile.append(argument)

saveToJsonFile(JSONfile, "add_item.json")

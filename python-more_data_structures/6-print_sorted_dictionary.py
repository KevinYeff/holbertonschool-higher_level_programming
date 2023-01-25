#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print(f"{keyValue}: {a_dictionary[keyValue]}")
     for keyValue in sorted(a_dictionary)]

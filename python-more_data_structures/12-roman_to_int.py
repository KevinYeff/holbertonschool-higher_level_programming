#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    romanNumbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    length = len(roman_string)
    total = romanNumbers[roman_string[-1]]

    i = length - 2
    while i < length and i >= 0:
        if romanNumbers[roman_string[i]] >= romanNumbers[roman_string[i + 1]]:
            total += romanNumbers[roman_string[i]]
            i -= 1
        else:
            total -= romanNumbers[roman_string[i]]
            i -= 1
    return total

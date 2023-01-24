#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for i in my_string[0:]:
        if i == 'c' and i == 'C':
            continue
        else:
            newString += i
    return newString

#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == my_list[0:0]:
        return None
    maxInteger = my_list[0]
    for i in my_list[0:]:
        if i > maxInteger:
            maxInteger = i
    return maxInteger

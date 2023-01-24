#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    for i in my_list[0:]:
        if i == idx:
            del my_list[i]
    return my_list

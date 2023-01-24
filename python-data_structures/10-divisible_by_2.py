#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = list(my_list)
    for i in my_list[0:]:
        if i % 2 == 0:
            newList[i] = True
        else:
            newList[i] = False
    return (newList)

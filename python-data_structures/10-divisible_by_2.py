#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    for i in my_list[0:]:
        if i % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return (newList)

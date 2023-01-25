#!/usr/bin/python3
def uniq_add(my_list=[]):
    newList = set(my_list)
    # newList = list(filter(lambda x: my_list.count(x) == 1, my_list))
    total = sum(newList)
    # total = sum(map(lambda x: x, newList))
    return total

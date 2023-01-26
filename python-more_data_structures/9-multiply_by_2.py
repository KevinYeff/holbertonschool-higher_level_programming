#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = {value: a_dictionary[value] * 2
               for value in a_dictionary}
#    for value in newDict:
#       newDict[value] *= 2
    return (newDict)

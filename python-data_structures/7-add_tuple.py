#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == tuple_a[0:0]:
        tuple_a = 0, 0
    elif tuple_a == tuple_a[0:1]:
        tuple_a = (tuple_a[0], 0)
    if tuple_b == tuple_b[0:0]:
        tuple_b = 0, 0
    elif tuple_b == tuple_b[0:1]:
        tuple_b = (tuple_b[0], 0)
    addTuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return (addTuple)

#!/usr/bin/python3
"""
Task 1
Class MyList inherits from list.
this class will inherit all the methods or attributes that the
built-in class "list" has.
"""


class MyList(list):
    """
    extends or inherits from "list" class
    """

    def print_sorted(self):
        """
        Prints a list of ints sorted and in ascending order
        """
        print(sorted(self))

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    dividedList = []
    div = 0
    for elem in range(list_length):
        try:
            div = my_list_1[elem] / my_list_2[elem]
        except TypeError:
            print("wrong type")
            div = 0
        except (ZeroDivisionError, ValueError):
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            dividedList.append(div)
    return dividedList

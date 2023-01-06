#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = 0
    for elem in my_list:
        if elem > max:
            max = elem
    return max

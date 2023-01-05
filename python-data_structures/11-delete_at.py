#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    my_list = del(my_list)
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list

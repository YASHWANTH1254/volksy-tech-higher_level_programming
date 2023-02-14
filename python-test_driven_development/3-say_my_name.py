#!/usr/bin/python3
"""Module built for Python 0x07 task 2. Error in project formatting scheme."""


def say_my_name(first_name, last_name=""):
    """Function that print"""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is " + first_name, end="")
    if first_name is not "":
        print(" ", end="")
    print(last_name)

#!/usr/bin/python3
"""Module built for Python 0x07 task 3. Error in project formatting scheme."""


def print_square(size):
    """Function that prints a square of a given size in '#' character."""
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        for col in range(size):
            print('#', end="")
        print()

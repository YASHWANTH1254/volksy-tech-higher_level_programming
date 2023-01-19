#!/usr/bin/python3
"""module pascal."""


def pascal_triangle(n):
    """return a list of integer."""

    pascal = []
    numbers = []
    prev = []
    limit = 0

    if n <= 0:
        return pascal

    for line in range(n):
        numbers.append(1)

        if limit > 0:
            i = 0
            j = 1

            for index in range(limit - 1):
                numbers.append(prev[i] + prev[j])
                i += 1
                j += 1

            numbers.append(1)

        pascal.append(numbers)
        limit += 1
        prev = numbers
        numbers = []

    return pascal

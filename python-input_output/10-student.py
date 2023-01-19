#!/usr/bin/python3
""" Class that defines a student """


class Student:
    """ Student class with an instance and a public method """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method."""

        dictionary = {}
        if type(attrs) is list and all([type(elem) is str for elem in attrs]):
            for k, v in self.__dict__.items():
                if k in attrs:
                    dictionary[k] = v
            return dictionary
        else:
            return self.__dict__

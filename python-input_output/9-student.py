#!/usr/bin/python3
""" Class that defines a student """


class Student:
    """ Student class with an instance and a public method """

    def __init__(self, first_name, last_name, age):
        """instance of student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """public method."""
        return self.__dict__

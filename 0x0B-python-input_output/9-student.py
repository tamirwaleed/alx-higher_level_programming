#!/usr/bin/python3
""" A student class """


class Student():
    """ the class """
    def __init__(self, first_name, last_name, age):
        """ initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns the json representation """
        return self.__dict__

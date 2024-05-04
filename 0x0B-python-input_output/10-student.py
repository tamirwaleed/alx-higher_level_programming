#!/usr/bin/python3
""" A student class """


class Student():
    """ the class """
    def __init__(self, first_name, last_name, age):
        """ initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns the json representation """
        if type(attrs) is list:
            check = True
            for x in attrs:
                if type(x) is not str:
                    check = False
            if check is False:
                return {y: getattr(self, y) for y in attrs}
        else:
            return self.__dict__

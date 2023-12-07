#!/usr/bin/python3
''' student class
(no not a classroom)'''


class Student:
    ''' the class '''
    def __init__(self, first_name, last_name, age):
        ''' instantiation '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' dictionary '''
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

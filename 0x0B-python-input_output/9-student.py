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

    def to_json(self):
        ''' dictionary '''
        return self.__dict__

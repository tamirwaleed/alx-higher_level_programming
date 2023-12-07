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
        try:
            for elem in attrs:
                if type(elem) == str:
                    return self.__dict__
        except:
            return self.__dict__
        dics = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                dics[key] = value
        return dics

#!/usr/bin/python3
""" The base class of all classes """


import json


class Base:
    """ the class itself """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        else:
            result = "["
            for x in list_dictionaries:
                result += json.dumps(x)
            return result + "]"

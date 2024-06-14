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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        my_list = []
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                elem = obj.to_dictionary()
                my_list.append(elem)
        with open(filename, "w") as fd:
            json_list = Base.to_json_string(my_list)
            new_list = json.loads(json_list)
            return json.dump(new_list, fd)

    @staticmethod
    def from_json_string(json_string):
        """ returns list of json string """
        my_list = []
        if json_string is None or len(json_string) == 0:
            return my_list
        else:
            return json.loads(json_string)

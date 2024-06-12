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
                elem = {'x': getattr(obj, "x"),
                        'y': getattr(obj, "y"),
                        'id': getattr(obj, "id"),
                        'height': getattr(obj, "height"),
                        'width': getattr(obj, "width")}
                my_list.append(elem)
        with open(filename, "w") as fd:
            new_list = Base.to_json_string(my_list)
            return json.dump(new_list, fd)

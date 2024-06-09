#!/usr/bin/python3
""" The base class of all classes """


class Base:
    """ the class itself """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantization """
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects

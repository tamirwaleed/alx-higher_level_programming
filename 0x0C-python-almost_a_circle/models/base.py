#!/usr/bin/python3
''' this has the class '''


class Base:
    ''' this is the class '''
    __nb_objects = 0
    def __init__(self, id=None):
        ''' the class constructor '''
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

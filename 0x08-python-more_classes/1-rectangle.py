#!/usr/bin/python3
""" The Rectangle module """


class Rectangle:
    """ the class """
    def __init__(self, width = 0, height = 0):
        """ instantiation """
        self.__width = width
        self.__height = height
    
    @property
    def height(self):
        """ getter """
        return self.__height
    
    @property
    def width(self):
        """ getter """
        return self.__width
    
    @height.setter
    def height(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    
    @width.setter
    def width(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

#!/usr/bin/python3
""" the square module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Our Class """
    def __init__(self, size):
        """ Initialization """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ finds area """
        return self.__size * self.__size

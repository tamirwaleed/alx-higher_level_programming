#!/usr/bin/python3
""" This is task 4"""


class Square:
    """ A class for a square """
    def __init__(self, size=0):
        """ Instantization """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ A method to find the area """
        return (self.__size ** 2)

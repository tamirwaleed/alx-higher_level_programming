#!/usr/bin/python3
""" This is task 6"""


class Square:
    """ A class for a square """
    def __init__(self, size=0):
        """ Instantization """
        self.__size = size

    @property
    def size(self):
        """ property """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ A method to find the area """
        return (self.__size ** 2)

    def my_print(self):
        """ A method to print the square """
        s = self.__size
        if s == 0:
            print()
        else:
            for i in range(s):
                for j in range(s):
                    print("#", end="")
                print()

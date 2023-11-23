#!/usr/bin/python3
""" This is task 7"""


class Square:
    """ A class for a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Instantization """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ property """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter """
        if (type(value) is not tuple or
            len(value) != 2 or
            not all(x >= 0 for x in value) or
            not all(type(x) is int for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ A method to find the area """
        return (self.__size ** 2)

    def my_print(self):
        """ A method to print the square """
        s = self.__size
        if s == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(s):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(s):
                    print("#", end="")
                print()

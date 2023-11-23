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
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

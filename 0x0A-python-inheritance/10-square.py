#!/usr/bin/python3
""" Square module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ the new class """
    def __init__(self, size):
        """ to initialize """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

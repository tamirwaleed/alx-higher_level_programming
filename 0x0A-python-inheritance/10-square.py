#!/usr/bin/python3
""" Square module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ the new class """
    def __init__(self, size):
        """ initialize """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

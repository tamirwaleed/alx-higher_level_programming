#!/usr/bin/python3
''' Square module '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Square Class '''
    def __init__(self, size):
        ''' Initialization '''
        super().integer_validator(size)
        self.__size = size


    def area(self):
        ''' Area '''
        return self.__size ** 2

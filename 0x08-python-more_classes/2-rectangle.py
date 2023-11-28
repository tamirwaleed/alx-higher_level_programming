#!/usr/bin/python3
''' This defines a rectangle '''


class Rectangle:
    ''' The class '''
    def __init__(self, width=0, height=0):
        ''' Initialization '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' Width prop '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' Height prop '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' Area '''
        return (self.width * self.height)

    def perimeter(self):
        ''' Perimeter '''
        return ((self.width + self.height) * 2)

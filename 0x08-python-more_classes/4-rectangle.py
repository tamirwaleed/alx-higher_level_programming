#!/usr/bin/python3
''' This defines a rectangle '''


class Rectangle:
    ''' The class '''
    def __init__(self, width=0, height=0):
        ''' Initialization '''
        self.__width = width
        self.__height = height

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
        return (self.__width * self.__height)

    def perimeter(self):
        ''' Perimeter '''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        ''' Why document '''
        x = ""
        w, h = self.__width, self.__height
        if self.__width == 0 or self.__height == 0:
            return (x)
        for i in range(h):
            for j in range(w):
                x = x + "#"
            x = x + "\n"
        x = x[:-1]
        return (x)

    def __repr__(self):
        ''' Why document '''
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

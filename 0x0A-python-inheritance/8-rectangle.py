#!/usr/bin/python3
''' Geometry module '''


class BaseGeometry:
    ''' New class '''
    def area(self):
        ''' raises an exception '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    ''' Rectangle Class '''
    def __init__(self, width, height):
        ''' Initialization '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

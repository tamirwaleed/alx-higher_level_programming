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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

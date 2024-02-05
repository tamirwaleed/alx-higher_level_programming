#!/usr/bin/python3
""" Base Geometry """


class BaseGeometry:
    """ Our geometry class """
    def area(self):
        """ the area method """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ validator """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
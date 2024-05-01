#!/usr/bin/python3
""" the geometry base module """


class BaseGeometry:
    """ class defined """
    def area(self):
        """ Finds the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))

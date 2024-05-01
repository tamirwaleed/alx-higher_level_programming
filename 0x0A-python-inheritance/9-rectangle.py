#!/usr/bin/python3
""" the rectangle module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Our Class """
    def __init__(self, width, height):
        """ Initialization """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ finds area """
        return self.__width * self.__height

    def __str__(self):
        """ returns a string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

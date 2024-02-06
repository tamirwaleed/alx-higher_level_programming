#!/usr/bin/python3
""" Rectangle module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Our rectangle class """
    def __init__(self, width, height):
        """ to initialize """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ finds area """
        return self.__width * self.__height

    def __str__(self):
        """ string rep """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

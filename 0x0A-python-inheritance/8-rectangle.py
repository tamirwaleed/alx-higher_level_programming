#!/usr/bin/python3
""" the rectangle module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Our Class """
    def __init__(self, width, height):
        """ Initialization """
        super().integer_validator("width",width)
        self.__width = width
        super().integer_validator("height",height)
        self.__height = height

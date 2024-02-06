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

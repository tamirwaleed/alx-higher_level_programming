#!/usr/bin/python3
""" The rectangle module """


from models.base import Base


class Rectangle(Base):
    """ the class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantization """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__

    def set_width(self, width):
        """ setter """
        self.__width = width

    def get_width(self):
        """ getter """
        return self.__width

    def set_height(self, height):
        """ setter """
        self.__height = height

    def get_height(self):
        """ getter """
        return self.__height

    def set_xself, x):
        """ setter """
        self.__x = x

    def get_x(self):
        """ getter """
        return self.__x

    def set_y(self, y):
        """ setter """
        self.__y = y

    def get_y(self):
        """ getter """                                                          
        return self.__y

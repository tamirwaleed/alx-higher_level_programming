#!/usr/bin/python3
""" The Rectangle module """


class Rectangle:
    """ the class """
    def __init__(self, width=0, height=0):
        """ instantiation """
        self.width = width
        self.height = height
 
    def __del__(self):
        """ farewell message """
        print("Bye rectangle...")

    def __str__(self):
        """ prints the rectangle """
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    s = s + "#"
                s = s + "\n"
            return s[:-1]

    def __repr__(self):
        """ returns a recreatable version of the object """
        return "Rectangle(" + str(self.__width) + \
            ', ' + str(self.__height) + ")"

    @property
    def height(self):
        """ getter """
        return self.__height

    @property
    def width(self):
        """ getter """
        return self.__width

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ finds the area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ finds the permieter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

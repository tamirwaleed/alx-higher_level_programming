#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ The class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialization """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ deletion """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns Area """
        return self.width * self.height

    def perimeter(self):
        """ Returns perimeter """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return ((self.height + self.width) * 2)

    def __str__(self):
        """ Prints it with # """
        if self.height == 0 or self.width == 0:
            return ""
        else:
            rect = ""
            for i in range(self.height):
                for j in range(self.width):
                    rect = rect + Rectangle.print_symbol
                rect = rect + "\n"
            return rect[0:-1]

    def __repr__(self):
        """ Recreates the instance """
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

#!/usr/bin/python3
""" The rectangle module """


from models.base import Base


class Rectangle(Base):
    """ the class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantization """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle """
        for i in range(self.__height):
            line = ""
            for j in range(self.__width):
                line += "#"
            print(line)

    def __str__(self):
        """ returns string represenation """
        line1 = "[Rectangle] ({}) {}/{}".format(self.id, self.x, self.y)
        line1 += " - {}/{}".format(self.width, self.height)
        return line1

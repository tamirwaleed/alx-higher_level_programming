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

    def integer_validator(value):
        """ checks the integers """
        if type(value) is not int:
            raise TypeError("{} must be am integer".format(value.__name__))
    
    def width_height_check(value):
        """checks height and width """
        if value <= 0:
            raise ValueError("{} must be > 0".format(value.__name__))

    def x_y_check(value):
        """ checks x & y """
        if value < 0:
            raise ValueError("{} must be >= 0".format(value.__name__))

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        integer_validator(value)
        width_height_check(value)
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        integer_validator(value)
        width_height_check(value)
        self.__height = value

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter """
        integer_validator(value)
        x_y_check(value)
        self.__x = value

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter """
        integer_validator(value)
        x_y_check(value)
        self.__y = value

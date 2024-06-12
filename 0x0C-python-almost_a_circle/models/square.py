#!/usr/bin/python3
""" The square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ the class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Instantization """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
        self.__size = value

    def __str__(self):
        """ returns string represenation """
        line1 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        line1 += " - {}".format(self.size)
        return line1

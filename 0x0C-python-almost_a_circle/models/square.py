#!/usr/bin/python3
""" The square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ the class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Instantization """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """ assigns values to arguments """
        if len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                else:
                    break
                i += 1
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    @property
    def size(self):
        """ getter """
        return self.width

    @size.setter
    def size(self, value):
        """ setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ returns string represenation """
        line1 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        line1 += " - {}".format(self.width)
        return line1

    def to_dictionary(self):
        """ returns the dict representation """
        return {'id': getattr(self, "id"),
                'x': getattr(self, "x"),
                'size': getattr(self, "size"),
                'y': getattr(self, "y")}

#!/usr/bin/python3
""" The square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ the class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Instantization """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns string represenation """
        line1 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        line1 += " - {}".format(self.width)
        return line1

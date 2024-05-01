#!/usr/bin/python3
""" my bizarro world integer """


class MyInt(int):
    """ the class which is a rebel """
    def __eq__(self, value):
        """ reverse equality """
        return self.real != value

    def __ne__(self, value):
        """ reverse non-equality """
        return self.real == value

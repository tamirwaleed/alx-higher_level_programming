#!/usr/bin/python3
""" a new integer """


class MyInt(int):
    """ bizarro integer """
    def __eq__(self, value):
        """ changes equality """
        return int(self) != value

    def __ne__(sef, value):
        """ changes non equality """
        return int(self)  == value

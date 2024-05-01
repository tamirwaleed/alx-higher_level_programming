#!/usr/bin/python3
""" inherits from list """


class MyList(list):
    """ the class """
    def print_sorted(self):
        """ the function """
        print(sorted(self))

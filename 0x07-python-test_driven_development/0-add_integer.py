#!/usr/bin/python3
""" module that adds 2 integers """


def add_integer(a, b=98):
    """ takes two integres with a default 98 """
    if type(a) in (float, int) && type(b) in (float, int):
        return (int(a) + int(b))
    elif type(a) not in (float, int):
        raise TypeError("a must be an integer")
    else:
        raise TypeError("b must be an integer")

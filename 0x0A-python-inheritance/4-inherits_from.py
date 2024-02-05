#!/usr/bin/python3
""" Another one """


def inherits_from(obj, a_class):
    """ direct subclass """
    return type(obj) != a_class and isinstance(obj, a_class)

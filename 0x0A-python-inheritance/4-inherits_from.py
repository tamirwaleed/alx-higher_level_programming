#!/usr/bin/python3
""" checks if the object is an INSTANCE
of a certain CLASS"""


def inherits_from(obj, a_class):
    """ the function returns True or False"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False

#!/usr/bin/python3
""" checks if the object is an INSTANCE """


def is_same_class(obj, a_class):
    """ the function returns True or False"""
    if type(obj) is a_class:
        return True
    else:
        return False

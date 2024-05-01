#!/usr/bin/python3
""" checks if object descends from class """


def is_kind_of_class(obj, a_class):
    """ the function """
    if isinstance(obj, a_class):
        return True
    else:
        return False

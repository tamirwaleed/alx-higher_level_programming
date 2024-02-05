#!/usr/bin/python3
""" Third module """


def is_same_class(obj, a_class):
    """ checks instance """
    if isinstance(obj, a_class):
        return True
    else:
        return False

#!/usr/bin/python3
""" can i??? """


def add_attribute(obj, att, value):
    """ adds attribute """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

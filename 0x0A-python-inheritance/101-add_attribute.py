#!/usr/bin/python3
""" adds a new attribute """


def add_attribute(obj, att, value):
    """ adds a new attribute if possible """
     if not hasattr(obj, __dict__):
         raise TypeError("can't add new attribute")
     setattr(obj, att, value)

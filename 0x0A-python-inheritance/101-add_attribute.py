#!/usr/bin/python3
''' adds attribute '''


def addattrib_(obj, attr, value):
    ''' the function '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

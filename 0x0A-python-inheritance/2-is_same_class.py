#!/usr/bin/python3
''' 3rd task '''


def is_same_class(obj, a_class):
    ''' Checks if the object is exactly an instance of the specified class
    Args:
    obj and class
    Return:
    True or False '''
    if type(obj) == a_class:
        return True
    else:
        return False

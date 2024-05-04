#!/usr/bin/python3
""" returns the dictionary description of a JSON object """


def class_to_json(obj):
    """ receives the object """
    return obj.__dict__

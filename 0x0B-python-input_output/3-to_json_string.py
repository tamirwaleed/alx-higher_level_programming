#!/usr/bin/python3
""" returns the json representation of an object """


import json


def to_json_string(my_obj):
    """ function that takes an object """
    return json.dumps(my_obj)

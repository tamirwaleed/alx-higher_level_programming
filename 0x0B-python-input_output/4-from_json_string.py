#!/usr/bin/python3
""" returns the python representation of a JSON string """


import json


def from_json_string(my_str):
    """ function that takes an object """
    return json.loads(my_str)

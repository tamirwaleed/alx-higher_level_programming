#!/usr/bin/python3
""" writes the json representation of an object into a file"""


import json


def save_to_json_file(my_obj, filename):
    """ function that takes an object """
    with open(filename, "w") as fd:
        return json.dump(my_obj, fd)

#!/usr/bin/python3
""" loads the json representation of an object from a file"""


import json


def load_from_json_file(filename):
    """ function that takes an object """
    with open(filename, "r") as fd:
        return json.load(fd)

#!/usr/bin/python3
''' 7th module '''


import json


def load_from_json_file(filename):
    ''' load from json '''
    with open(filename, "r") as fd:
        return json.load(fd)

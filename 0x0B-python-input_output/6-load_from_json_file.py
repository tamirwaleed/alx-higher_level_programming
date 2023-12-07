#!/usr/bin/python3
''' From json file '''


import json


def load_from_json_file(filename):
    ''' function '''
    with open(filename) as fd:
        return (json.load(fd))

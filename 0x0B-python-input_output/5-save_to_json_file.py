#!/usr/bin/python3
""" 6th module """


import json


def save_to_json_file(my_obj, filename):
    ''' save to json '''
    with open(filename, "w") as fd:
        return json.dump(my_obj, fd)


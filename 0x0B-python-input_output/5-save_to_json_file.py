#!/usr/bin/python3
''' To JSON file '''


import json


def save_to_json_file(my_obj, filename):
    ''' function '''
    with open(filename, 'w') as fd:
        return (json.dump(my_obj, fd))

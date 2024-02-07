#!/usr/bin/python3
''' the add module '''


import sys

if __name__ == ""__main__:
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    reqlist = []
    try:
        jk = load_from_json_file("add_item.json")
    except:
        jk = []
    jk.extend(sys.argv[1:])
    save_to_json_file(jk, "add_item.json")

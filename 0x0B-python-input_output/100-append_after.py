#!/usr/bin/python3
''' APPENDS AFTER '''


def append_after(filename="", search_string="", new_string=""):
    ''' the function '''
    text = ""
    with open(filename) as fd:
        for line in fd:
            text = text + line
            if search_string in line:
                text = text + new_string
    with open(filename, 'w') as fg:
        fg.write(text)

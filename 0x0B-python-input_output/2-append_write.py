#!/usr/bin/python3
''' Appending module '''


def append_write(filename="", text=""):
    ''' The Function '''
    with open(filename, 'a') as fd:
        (fd.append(text))
